


def split_before_uppercases(formula):
    if not formula:
        return []

    splitted_formula = []
    start = 0

    for i in range(1, len(formula)):
        if formula[i].isupper():
            splitted_formula.append(formula[start:i])
            start = i

    splitted_formula.append(formula[start:])
    return splitted_formula


def split_at_digit(formula):
     if not formula:
        return "", 1

    for i, ch in enumerate(formula):
        if ch.isdigit():
            j = i
            while j < len(formula) and formula[j].isdigit():
                j += 1
            prefix = formula[:i]
            number_part = int(formula[i:j])
            return prefix, number_part

    return formula, 1


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
    
