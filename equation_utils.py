from sympy import symbols, Eq, solve as sympy_solve, Rational

ELEMENTS = [
    'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
    'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
    'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
    'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr',
    'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn',
    'Sb', 'I', 'Te', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd',
    'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb',
    'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg',
    'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
    'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm',
    'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds',
    'Rg', 'Cn', 'Uut', 'Uuq', 'Uup', 'Uuh', 'Uus', 'Uuo'
]

def generate_equation_for_element(compounds, coefficients, element):
    eq = 0
    for i, compound in enumerate(compounds):
        if element in compound:
            eq += coefficients[i] * compound[element]
    return eq

def build_equations(reactant_atoms, product_atoms):
    reactant_coeffs = list(symbols(f'a0:{len(reactant_atoms)}'))
    product_coeffs = list(symbols(f'b0:{len(product_atoms)}'))
    product_coeffs = product_coeffs[:-1] + [Rational(1)]

    equations = []
    for element in ELEMENTS:
        lhs = generate_equation_for_element(reactant_atoms, reactant_coeffs, element)
        rhs = generate_equation_for_element(product_atoms, product_coeffs, element)
        if lhs != 0 or rhs != 0:
            equations.append(Eq(lhs, rhs))

    return equations, reactant_coeffs + product_coeffs[:-1]

def my_solve(equations, coefficients):
    solution = sympy_solve(equations, coefficients)
    result = [solution[c] if c in solution else Rational(1) for c in coefficients]
    return result

def balance_reaction(reaction):
    from string_utils import count_atoms_in_molecule

    reactants_str, products_str = reaction.replace(" ", "").split("->")
    reactants = reactants_str.split("+")
    products = products_str.split("+")

    all_molecules = reactants + products
    atom_maps = [count_atoms_in_molecule(m) for m in all_molecules]

    atoms = sorted({atom for m in atom_maps for atom in m})
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

    A = Matrix(rows)
    nullspace = A.nullspace()
    vec = [Rational(x) for x in nullspace[0]]

    for i, x in enumerate(vec):
        if x != 0:
            if x < 0:
                vec = [-c for c in vec]
            break

    positive_coeffs = [x for x in vec if x > 0]
    min_coeff = min(positive_coeffs)
    vec = [x / min_coeff for x in vec]

    return vec



