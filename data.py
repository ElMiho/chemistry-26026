import periodictable as pt

symbol_to_number = dict()
number_to_symbol = dict()
for el in pt.elements:
    symbol_to_number[el.symbol] = el.number
    number_to_symbol[el.number] = el.symbol

electron_configuration_list = [("1s", 2), ("2s", 2), ("2p", 6), 
                               ("3s", 2), ("3p", 6), ("4s", 2), 
                               ("3d", 10), ("4p", 6), ("5s", 2), 
                               ("4d", 10), ("5p", 6), ("6s", 2), 
                               ("4f", 14), ("5d", 10), ("6p",6),
                               ("7s", 2), ("5f", 14), ("6d", 10),
                               ("7p", 6), ("5h", 18), ("6f", 14),
                               ("7d", 10), ("6h", 18), ("7f", 14),
                               ("7h", 18)]

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