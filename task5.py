strings = ['hello', 'bananas', 'apple', 'world', 'bananas']
def frequently_strings(strings):
    max_frequency = 0
    frequency_indicator = {}

    for string in strings:
        if string in frequency_indicator:
           frequency_indicator[string] += 1
        else:
            frequency_indicator[string] = 1

    for string, frequency in frequency_indicator.items():
        if frequency > max_frequency:
            max_frequency = frequency
            highest_frequency = string

    return highest_frequency


print(frequently_strings(strings))