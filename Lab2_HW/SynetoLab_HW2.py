def letter_count(string):
    frequency = {}
    for c in string:
        if c in frequency:
            frequency[c] += 1
        else:
            frequency[c] = 1
    return frequency

frequency = letter_count('Python gives you superpowers.')

print(frequency)