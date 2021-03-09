import json
import math
import locale


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    # print(invoice)
    result = f"Statement for {invoice['customer']}\n"

    for perf in invoice['performances']:
        # play = play_for(perf)
        # this_amount = amount_for(perf)

        volume_credits += volume_credits_for(perf)

        if "comedy" ==  play_for(perf)["type"]:
            volume_credits += math.floor(perf["audience"] / 5)
        result += f"  { play_for(perf)['name']}: {usd(total_amount)} seats)\n"
        total_amount += amount_for(perf)

    result += f"Amount owed is {usd(total_amount)}\n"
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


def volume_credits_for(a_performance):
    result  = 0
    result += max(a_performance['audience'] - 30, 0)
    if "comedy" == play_for(a_performance)['type']:
        result += math.floor(a_performance['audience']/ 5)
    return result

def usd(a_number):
    locale.setlocale(locale.LC_ALL, 'en_US.utf-8')
    return locale.format_string('%.2f', a_number / 100, True)



if __name__ == "__main__":
    with open('invoices.json') as f:
        invoices = json.load(f)
    with open('plays.json') as f:
        plays = json.load(f)
    invoice = invoices[0]
    result = statement(invoice, plays)
    print(result)
