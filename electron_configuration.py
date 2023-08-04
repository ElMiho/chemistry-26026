import data

def electron_configuration(atom, charge = 0):
    atom_number = data.symbol_to_number[atom]

    electrons_missing = atom_number
    configuration = []
    for orbital, electrons in data.electron_configuration_list:
        if electrons_missing <= 0:
            break
        elif electrons_missing < electrons:
            configuration.append((orbital, electrons_missing))
        else:
            configuration.append((orbital, electrons))
        electrons_missing -= electrons
    
    return configuration

print(electron_configuration("Xe"))
