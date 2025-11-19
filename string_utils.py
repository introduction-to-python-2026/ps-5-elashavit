


def split_before_uppercases(formula):
    parts = []
    start = 0
    for i in range(1, len(formula)):
        if formula[i].isupper():
            parts.append(formula[start:i])
            start = i
    parts.append(formula[start:])
    return parts


def split_at_digit(formula):
    name = ""
    num = ""
    for char in formula:
        if char.isdigit():
            num += char
        else:
            name += char
    return name, int(num) if num else 1


def count_atoms_in_molecule(molecular_formula):
    """Returns a dictionary of atom counts. Example: H2O -> {'H': 2, 'O': 1}"""

    # Step 1: initialize dictionary
    atom_counts = {}

    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)

        # Step 2: update dictionary
        atom_counts[atom_name] = atom_counts.get(atom_name, 0) + atom_count

    # Step 3: return result
    return atom_counts


def parse_chemical_reaction(reaction_equation):
    reaction_equation = reaction_equation.replace(" ", "")
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")


def count_atoms_in_reaction(molecules_list):
    return [count_atoms_in_molecule(m) for m in molecules_list]
    
