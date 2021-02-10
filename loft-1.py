import operator
import re


def get_max_key_in_dict(data):
    '''return tuple (key, value) with max value'''
    return max(data.items(), key=operator.itemgetter(1))


def computing_frequency_and_length(s):
    if not isinstance(s, str):
        print('data is not string')  # check for unexpected type
    else:
        conv_s = re.findall(r'\w+', s)  # return list for words in string
        print('Word with max frequency',
              get_max_key_in_dict({w: conv_s.count(w) for w in set(conv_s)}))
        print('-' * 40)
        print('Word with max len',
              get_max_key_in_dict({w: len(w) for w in set(conv_s)}))


if __name__ == '__main__':
    computing_frequency_and_length(input('Please input a string:\n'))
