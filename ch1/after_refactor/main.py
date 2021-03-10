import json
import math
import locale
from functools import reduce
from create_statement_data import create_statement_data


def statement(invoice, plays):
    return render_plain_text(create_statement_data(invoice, plays))

def render_plain_text(data):
    def usd(a_number):
        locale.setlocale(locale.LC_ALL, 'en_US.utf-8')
        return locale.currency(a_number / 100)

    result = f"Statement for {data['customer']}\n"
    # print(data)
    for perf in data['performances']:
        result += f"  { perf['play']['name']}: {usd(perf['amount'])} ( {perf['audience']} seats)\n"

    # total_amount = apple_sauce()

    result += f"Amount owed is {usd(data['total_amount'])}\n"
    result += f"You earned {data['total_volume_credits']} credits\n"
    return result


if __name__ == "__main__":
    with open('invoices.json') as f:
        invoices = json.load(f)
    with open('plays.json') as f:
        plays = json.load(f)
    invoice = invoices[0]
    result = statement(invoice, plays)
    print(result)
