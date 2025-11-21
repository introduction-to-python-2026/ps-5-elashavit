from sympy import Matrix, Rational, lcm

def build_matrix(reactants, products, atom_maps, atoms):
    num_react = len(reactants)
    num_prod = len(products)

    rows = []
    for atom in atoms:
        row = []
        for i in range(num_react):
            row.append(atom_maps[i].get(atom, 0))
        for i in range(num_prod):
            row.append(-atom_maps[num_react + i].get(atom, 0))
        rows.append(row)

    return Matrix(rows)


def balance_reaction(reaction):
    from string_utils import count_atoms_in_molecule

    # Remove spaces and split
    reaction = reaction.replace(" ", "")
    react_str, prod_str = reaction.split("->")
    reactants = react_str.split("+")
    products = prod_str.split("+")

    all_molecules = reactants + products
    atom_maps = [count_atoms_in_molecule(m) for m in all_molecules]

    atoms = sorted({atom for m in atom_maps for atom in m})
    matrix = build_matrix(reactants, products, atom_maps, atoms)

    nullspace = matrix.nullspace()
    vec = [Rational(x) for x in nullspace[0]]

    # Make positive
    for x in vec:
        if x != 0:
            if x < 0:
                vec = [-c for c in vec]
            break

    # REQUIRED BY TESTS → normalize so LAST coefficient = 1
    last = vec[-1]
    vec = [x / last for x in vec]

    return vec
