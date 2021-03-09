import json
import math
import locale


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    # print(invoice)
    result = f"Statement for {invoice['customer']}\n"

    locale.setlocale(locale.LC_ALL, 'en_US.utf-8')

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        this_amount = 0

        if play['type'] == 'tragedy':
            this_amount = 40000
            if perf['audience'] > 30:
                this_amount += 1000 * (perf["audience"] - 30)
        
        elif play['type'] == 'comedy':
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf["audience"] - 20)
            this_amount += 300 * perf["audience"]
        else:
            raise Exception(f"unkownn type: {play['type']}")

        volume_credits += max(perf["audience"] - 30, 0)

        if "comedy" == play["type"]:
            volume_credits += math.floor(perf["audience"] / 5)
        result += f"  {play['name']}: {locale.format_string('%.2f', this_amount / 100, True)} ({perf['audience']} seats)\n"
        total_amount += this_amount

    result += f"Amount owed is {locale.format_string('%.2f', total_amount / 100, True)}\n"
    result += f"You earned {volume_credits} credits\n"
    return result
    

if __name__ == "__main__":
    with open('invoices.json') as f:
        invoices = json.load(f)
    with open('plays.json') as f:
        plays = json.load(f)
    invoice = invoices[0]
    result = statement(invoice, plays)
    print(result)
