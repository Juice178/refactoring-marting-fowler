import json
import math
import locale


def statement(invoice, plays):
    def enrich_performance(a_performance):
        result = a_performance.copy()
        result['play'] = play_for(result)
        result['amount'] = amount_for(result)
        result['volume_credits'] = volume_credits_for(result)
        return result

    def volume_credits_for(a_performance):
        result  = 0
        result += max(a_performance['audience'] - 30, 0)
        if "comedy" == a_performance['play']['type']:
            result += math.floor(a_performance['audience']/ 5)
        return result

    def play_for(a_performance):
        return plays[a_performance['playID']]

    def amount_for(a_performance):
        result = 0
        if a_performance['play']['type'] == 'tragedy':
            result = 40000
            if a_performance['audience'] > 30:
                result += 1000 * (a_performance["audience"] - 30)
        
        elif a_performance['play']['type'] == 'comedy':
            result = 30000
            if a_performance['audience'] > 20:
                result += 10000 + 500 * (a_performance["audience"] - 20)
            result += 300 * a_performance["audience"]
        else:
            raise Exception(f"unkownn type: {a_performance['type']}")

        return result

    statement_data = {}
    statement_data['customer'] = invoice['customer']
    statement_data['performances'] = list(map(enrich_performance, invoice['performances']))

    return render_plain_text(statement_data, plays)

def render_plain_text(data, plays):
    # print(data)
    def total_amount():
        result = 0
        for perf in data['performances']:
            result += perf['amount']
        return result

    def usd(a_number):
        locale.setlocale(locale.LC_ALL, 'en_US.utf-8')
        return locale.currency(a_number / 100)

    def total_volume_credits():
        result = 0
        for perf in data['performances']:
            result += perf['volume_credits']
        return result


    result = f"Statement for {data['customer']}\n"
    # print(data)
    for perf in data['performances']:
        result += f"  { perf['play']['name']}: {usd(perf['amount'])} ( {perf['audience']} seats)\n"

    # total_amount = apple_sauce()

    result += f"Amount owed is {usd(total_amount())}\n"
    result += f"You earned {total_volume_credits()} credits\n"
    return result


if __name__ == "__main__":
    with open('invoices.json') as f:
        invoices = json.load(f)
    with open('plays.json') as f:
        plays = json.load(f)
    invoice = invoices[0]
    result = statement(invoice, plays)
    print(result)
