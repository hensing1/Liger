import sys
import re
import csv


def main():
    if len(sys.argv) not in (2, 3):
        print("Verwendung: liger.py anzahl_generationen {resultat.csv}")

    num_generations = int(sys.argv[1])

    generation = ("Tiger", "Löwe")  # tuple, not set, because we want to keep it ordered

    for i in range(num_generations - 1):
        crosstable = make_crosstable(generation)
        new_generation = set(crosstable.values()) - set(generation)
        generation += tuple(new_generation)

    crosstable = make_crosstable(generation)
    full_table = make_full_table(generation, crosstable)
    pretty_print(full_table)

    if len(sys.argv) == 3:
        print_to_csv(full_table, sys.argv[2])


def make_crosstable(generation: tuple):
    crosstable = {}
    for father in generation:
        for mother in generation:
            crosstable[father, mother] = breed(father, mother)
    return crosstable


def breed(father, mother):
    if father == mother:
        return father

    # special cases
    if father == "Tiger" and mother == "Löwe":
        return "Töwe"
    if father == "Löwe" and mother == "Tiger":
        return "Liger"

    father_prefixes = re.sub(r'ger|we$', '', father)
    return father_prefixes + "-" + mother


def make_full_table(generation, crosstable):
    table = []

    # header row
    table.append([""] + list(generation))

    # table body
    for fem_specimen in generation:
        new_row = [female(fem_specimen)]
        for specimen in generation:
            new_row.append(crosstable[specimen, fem_specimen])
        table.append(new_row)

    return table


def female(specimen):
    if specimen[-1:][0] == "e":
        return re.sub(r'e$', 'in', specimen)
    return specimen + "in"


def pretty_print(table):
    col_sizes = []
    padding = 3
    for i in range(len(table[0])):
        col_sizes.append(
            padding + max([len(entry) for entry in [table[col][i] for col in range(len(table))]]))  # bleugh

    lines = []
    for row in table:
        formatted_row = []
        for entry, col_size in zip(row, col_sizes):
            formatted_row.append('{:<{width}}'.format(entry, width=col_size))
        formatted_row[1:1] = ['|  ']
        lines.append(''.join(formatted_row))

    lines[1:1] = ['{:_<{width}}'.format('', width=sum(col_sizes))]

    for line in lines:
        print(line)


def print_to_csv(table, filename):
    with open(filename, 'w', newline='', encoding='utf8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(table)

    print(f"Gespeichert in {filename}.")


if __name__ == '__main__':
    main()
