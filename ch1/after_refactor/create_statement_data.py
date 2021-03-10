import json
import math
import locale
from functools import reduce
from dataclasses import dataclass


def create_statement_data(invoice, plays):
    def enrich_performance(a_performance):
        calculator = create_performance_calculator(a_performance, play_for(a_performance))
        # print(calculator.performance, calculator.play)
        result = a_performance.copy()
        result['play'] = calculator.play
        result['amount'] = calculator.amount()
        result['volume_credits'] = calculator.volume_credits()
        return result

    def play_for(a_performance):
        return plays[a_performance['playID']]

    def total_amount(data):
        return reduce(lambda x, y: x + y['amount'], data['performances'], 0)

    def total_volume_credits(data):
        return reduce(lambda x, y: x + y['volume_credits'], data['performances'], 0)

    statement_data = {}
    statement_data['customer'] = invoice['customer']
    statement_data['performances'] = list(map(enrich_performance, invoice['performances']))
    statement_data['total_amount'] = total_amount(statement_data)
    statement_data['total_volume_credits'] = total_volume_credits(statement_data)

    return statement_data


def create_performance_calculator(a_performance, a_play):
    if a_play['type'] == "tragedy":
        return TragedyCalculator(a_performance, a_play)
    elif a_play['type'] == "comedy":
        return ComedyCalculator(a_performance, a_play)
    else:
        raise Exception(f"unkownn play: {a_play['type']}")


@dataclass
class PerformanceCalculator:
    performance: dict
    play: dict

    def amount(self) -> int:
        raise Exception("Subclass responsibility")

    def volume_credits(self) -> int:
        result  = 0
        result += max(self.performance['audience'] - 30, 0)
        if "comedy" == self.play['type']:
            result += math.floor(self.performance['audience']/ 5)
        return result


class TragedyCalculator(PerformanceCalculator):
    def amount(self) -> int:
        result = 40000
        if self.performance['audience'] > 30:
            result += 1000 * (self.performance['audience'] - 30)
        return result


class ComedyCalculator(PerformanceCalculator):
    def amount(self) -> int:
        result = 30000
        if self.performance['audience'] > 20:
            result += 10000 + 500 * (self.performance['audience'] - 20)
        result += 300 * self.performance['audience']
        return result