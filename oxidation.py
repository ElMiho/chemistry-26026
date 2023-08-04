import itertools
from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

import data

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
        oxidation_numbers.append(data.element_oxidation_numbers[element])
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

print(oxidation_number([('S', 1), ('O', 4)], -2))