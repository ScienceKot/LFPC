# TASK # 1: Generation of strings.

# Importing the shortening libraries
import random
nonterminal_symbols = set(['S', 'A', 'B'])
terminal_symbols = set(['a', 'b', 'c'])

# Setting the minimal length of the generated strings.
length_of_generated_strings = len(nonterminal_symbols) + 2

# Setting up the set of productions.
set_of_productions = tuple([
    ('S', 'aS'),
    ('S', 'bS'),
    ('S', 'cA'),
    ('A', 'aB'),
    ('B', 'aB'),
    ('B', 'bB'),
    ('B', 'c')
])

# Converting the set_of_productions into a dictionary.
set_of_productions = {nonterminal[0] : [prod[1] for prod in set_of_productions if prod[0] == nonterminal[0]] for nonterminal in set_of_productions}

# Generation of the strings.
starting_symbol = 'S'
strings = [starting_symbol] * 5

# Creation of the list with the state of finishness of generation of the strings.
finish_condition = [True] * 5

# TREES & TABLES
derivation_trees = [dict() for i in range(5)]
derivation_table = [[] for i in range(5)]

# Generating strings until all of them will not have at least length 5
while all(finish_condition):
    # Iterating throw all strings.
    for i in range(len(strings)):
        # Trying to catch the IndexError, that may appear when a generated string has only terminal strings
        try:
            to_replace = random.choice(list(nonterminal_symbols.intersection(set(list(strings[i])))))
        except IndexError:
            # Restarting the process with the new empty strings.
            strings = [starting_symbol] * 5
            derivation_trees = [dict()] * 5
            derivation_table = [[] for i in range(5)]
            break
        # Replacing the nonterminal symbol with a random one from its set of productions.
        replace_with = random.choice(set_of_productions[to_replace])
        strings[i] = strings[i].replace(
            to_replace,
            replace_with,
            1
        )
        # Creation of the derivation table.
        derivation_table[i].append(f'{to_replace}->{replace_with}')
    # Filtering strings that has a length lower that 'length_of_generated_strings
    finish_condition = list(filter(lambda x : len(x) < length_of_generated_strings, strings))

    # If we have all strings with the length higher or equal to five, that we end the process of string generations.
    if len(finish_condition) == 0:
        finish_condition = [False] * 5

# Generation of the derivation trees
for i in range(len(derivation_trees)):
    replaced = [].copy()
    for j in range(len(derivation_table[i])):
        replaced_symbol = derivation_table[i][j].split('->')[0]
        replaced.append(replaced_symbol)
        derivation_trees[i][tuple(replaced)] = derivation_table[i][j].split('->')[1]

# Convertion of the regular grammar to Finite Automaton (FA).
finite_automaton = dict()
for prod in set_of_productions:
    for result in set_of_productions[prod]:
        if len(result) == 2:
            finite_automaton[(prod, result[0])] = result[1]
        else:
            finite_automaton[(prod, result)] = 'Q'

# Printing out the result.
print("THE GENERATED STRINGS : ", end='')
print(strings)

# Printing out the derivation tree.
print("THE DERIVATION TREES : ")
print(derivation_trees)

# Printing out the derivation tables.
print("THE DERIVATION TABLES : ")
print(derivation_table)

# Printing out the Generated Finite Automaton.
print("THE GENERATED FINITE AUTOMATON : ")
print(finite_automaton)

# The Grammar type by Chomsky classification is regular grammar.
print('The Grammar type by Chomsky classification is regular grammar.')
