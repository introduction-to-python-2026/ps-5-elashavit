def split_before_uppercases(formula):
    parts = []
    start = 0

    for i in range(1, len(formula)):
        if formula[i].isupper():
            parts.append(formula[start:i])
            start = i

    parts.append(formula[start:])
    return parts


def split_at_digit(element):
    name = ""
    number = ""

    for ch in element:
        if ch.isdigit():
            number += ch
        else:
            name += ch

    if number == "":
        number = 1
    else:
        number = int(number)

    return name, number


def count_atoms_in_molecule(molecular_formula):
    atom_counts = {}
    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)
        atom_counts[atom_name] = atom_counts.get(atom_name, 0) + atom_count
    return atom_counts


def parse_chemical_reaction(reaction_equation):
    reaction_equation = reaction_equation.replace(" ", "")
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")






