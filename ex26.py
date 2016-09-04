def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "\nLet's practice everything."
print '\nYou\'d need to know about escapes with the \'\\\' character:'
print '\n1: \'\\n\' splits stuff across \n a newline'
print '\n2: \'\\t\' adds a \t tab character wherever you put it.'
print '\nIt\'s up to you figure out the rest of the escape sequences.'

poem = """

          The lovely world
    with logic so firmly planted
           cannot discern
          the needs of love
nor comprehend passion from intuition
     and requires an explantion
        where there is none.

"""


print "\n-------------------------------------",
print poem,
print "-------------------------------------\n"

five = 10 - 2 + 3 - 6
print "This should be five: %s\n" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d\n" % start_point
print "We'd have %d beans, %d jars, and %d crates.\n" % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:\n"
print "We'd have %d beans, %d jars, and %d crates.\n" % secret_formula(start_point)


sentence = "All good\tthings come to those who wait."
print 'Here is the sentence: %r\n' % sentence

words = break_words(sentence)
print 'Each word in a list: %r\n' % words
sorted_words = sort_words(words)
print 'Sorting the list: %r\n' % sorted_words
print 'Printing the first word from the unsorted list: ',
print_first_word(words)
print '\n', 'Printing the last word from the unsorted list: ',
print_last_word(words)
print '\n', 'Printing the first word from the sorted list: ',
print_first_word(sorted_words)
print '\n', 'Printing the last word from the sorted list: ',
print_last_word(sorted_words)

sorted_words = sort_sentence(sentence)
print '\n', 'Using sort_sentence method, here is the list: ', sorted_words
print '\n', 'Printing the first and last word from the sentence: '
print_first_and_last(sentence)
print '\n', 'Printing the first and last word from the sentence sorted: '
print_first_and_last_sorted(sentence)
