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
        # play = play_for(perf)
        this_amount = amount_for(perf)

        volume_credits += max(perf["audience"] - 30, 0)

        if "comedy" ==  play_for(perf)["type"]:
            volume_credits += math.floor(perf["audience"] / 5)
        result += f"  { play_for(perf)['name']}: {locale.format_string('%.2f', this_amount / 100, True)} ({perf['audience']} seats)\n"
        total_amount += this_amount

    result += f"Amount owed is {locale.format_string('%.2f', total_amount / 100, True)}\n"
    result += f"You earned {volume_credits} credits\n"
    return result


def amount_for(a_performance):
    result = 0
    if play_for(a_performance)['type'] == 'tragedy':
        result = 40000
        if a_performance['audience'] > 30:
            result += 1000 * (a_performance["audience"] - 30)
    
    elif play_for(a_performance)['type'] == 'comedy':
        result = 30000
        if a_performance['audience'] > 20:
            result += 10000 + 500 * (a_performance["audience"] - 20)
        result += 300 * a_performance["audience"]
    else:
        raise Exception(f"unkownn type: {play_for(a_performance)['type']}")

    return result
    

def play_for(a_performance):
    return plays[a_performance['playID']]

if __name__ == "__main__":
    with open('invoices.json') as f:
        invoices = json.load(f)
    with open('plays.json') as f:
        plays = json.load(f)
    invoice = invoices[0]
    result = statement(invoice, plays)
    print(result)
