def wordify1(n):
    if n<20: return ["","one","two","three","four","five","six","seven","eight","nine","ten",
    "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"][n]
    if n<100: return " ".join([["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"][(n-20)/10],wordify(n%10)]).rstrip()
    if n<1000: return " ".join([wordify(n/100)+" hundred",wordify(n%100)]).rstrip()

def wordify(n):
    r = ''
    h = n / (10 ** 2)
    t = (n - h * (10 ** 2)) / 10
    d = n % 10
    print h, t, d
    if h is not 0:
        if t is 0 and d is 0:
            r += turn_dict[str(h)] + ' hundred'
        else:
            r += turn_dict[str(h)] + ' hundred '
            if t is 1:
                r += turn_dict[str(t * 10 + d)]
            else:
                if t is 0:
                    r += turn_dict[str(d)]
                else:
                    if d is not 0:
                        r += turn_dict[str(t * 10)] + ' ' + turn_dict[str(d)]
                    else:
                        r += turn_dict[str(t * 10)]
    else:
        if t is 1:
            r += turn_dict[str(t * 10 + d)]
        else:
            if t is 0:
                r += turn_dict[str(d)]
            else:
                if d is not 0:
                    r += turn_dict[str(t * 10)] + ' ' + turn_dict[str(d)]
                else:
                    r += turn_dict[str(t * 10)]
    return r


turn_dict = {
    '0': '',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety',
}

print wordify(326)