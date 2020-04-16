capitals = {
    'Timis': 'Timisoara',
    'Bihor': 'Oradea',
    'Arad': 'Arad',
    'Hunedoara': 'Deva',
    'Caras-Severin': 'Resita',
}

def judet(capital):
    for c in capitals:
        if(capitals[c] == capital):
            return c
    return 'Unknown'

print(judet('Arad'))