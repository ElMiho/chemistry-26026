import itertools
from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

element_oxidation_numbers = {
    "H": [-1, 1],
    "He": [0],
    "Li": [1],
    "Be": [2],
    "B": [3],
    "C": [-4, 2, 4],
    "N": [-3, 1, 2, 3, 4, 5],
    "O": [-2, -1, 2, -1/2],
    "F": [-1],
    "Ne": [0],
    "Na": [1],
    "Mg": [2],
    "Al": [3],
    "Si": [-4, 4],
    "P": [-3, 3, 5],
    "S": [-2, 2, 4, 6],
    "Cl": [-1, 1, 3, 4, 5, 6, 7],
    "K": [1],
    "Ar": [0],
    "Ca": [2],
    "Sc": [3],
    "Ti": [2, 3, 4],
    "V": [2, 3, 4, 5],
    "Cr": [2, 3, 4, 5, 6],
    "Mn": [2, 3, 4, 6, 7],
    "Fe": [2, 3],
    "Ni": [2],
    "Co": [2, 3],
    "Cu": [1, 2],
    "Zn": [2],
    "Ga": [3],
    "Ge": [-4, 4],
    "As": [-3, 3, 5],
    "Se": [-2, 4, 6],
    "Br": [-1, 1, 3, 5],
    "Kr": [4, 2],
    "Rb": [1],
    "Sr": [2],
    "Y": [3],
    "Zr": [4],
    "Nb": [4, 5],
    "Mo": [ 3, 4, 6],
    "Tc": [4, 6, 7],
    "Ru": [3, 4, 6, 8],
    "Rh": [2, 3, 4],
    "Pd": [2, 4],
    "Ag": [1],
    "Cd": [2],
    "In": [3],
    "Sn": [2, 4],
    "Sb": [-3, 3, 5],
    "Te": [-2, 4, 6],
    "I": [-1, 1, 5, 7],
    "Xe": [6, 4, 2],
    "Cs": [1],
    "Ba": [2],
    "La": [3],
    "Hf": [4],
    "Ta": [5],
    "W": [4, 6],
    "Re": [4, 6, 7],
    "Os": [4, 8],
    "Ir": [3, 4],
    "Pt": [2, 4],
    "Au": [1, 3],
    "Hg": [1, 2],
    "Tl": [1, 3],
    "Pb": [2, 4],
    "Bi": [3, 5],
    "Po": [2],
    "At": [-1],
    "Rn": [0]
}

grammar = Grammar(
    """
    compound = atom_unit{1,} charge?
    atom_unit = atom unit?
    atom = ~"[A-Z]"~"[a-z]"?
    unit = "_"~"[0-9]"*
    charge = "^"~"[1-9]"{1} ("+" / "-")
    """
)

class IniVisitor(NodeVisitor):
    def visit_compound(self, node, visited_children):
        """ Returns the overall output. """
        output = {}
        for child in visited_children:
            output.update(child[0])
        return output

    def visit_atom_unit(self, node, visited_children):
        key, values = visited_children
        return {key: dict(values)}

    def visit_atom(self, node, visited_children):
        return [key for key in visited_children]

    def visit_unit(self, node, visited_children):
        pass
    
    def visit_charge(self, node, visited_children):
        pass

    def generic_visit(self, node, visited_children):
        """ The generic visit method. """
        return visited_children or node
    
# tree = grammar.parse("BrO_4^2-")
# iv = IniVisitor()
# output = iv.visit(tree)
# print(output)

def parse(compound: str) -> [tuple]:
    expression = grammar.parse(compound)
    to_be_explored = [expression]
    while to_be_explored != []:
        current = to_be_explored.pop()
        print(f"{current.text}: {[x.text for x in current.children]}")
        for child in current.children:
            to_be_explored.append(child)

# parse("BrO_4^2-")

def oxidation_number(list, charge):
    # for element, amount in list:
    #     if amount == 1:
    #         print(f"{element}", end="")
    #     else:
    #         print(f"{element}{amount}", end="")
    # print(f"{charge}")

    oxidation_numbers = []
    amounts = []
    for element, amount in list:
        oxidation_numbers.append(element_oxidation_numbers[element])
        amounts.append(amount)

    dict_list = []
    for tuple in itertools.product(*oxidation_numbers):
        res = 0
        oxidation_dict = dict()
        for idx, x in enumerate(tuple):
            res += amounts[idx] * x
            oxidation_dict[list[idx][0]] = x
        if res == charge:
            dict_list.append(oxidation_dict)

    return dict_list

# print(oxidation_number([('S', 1), ('O', 4)], -2))