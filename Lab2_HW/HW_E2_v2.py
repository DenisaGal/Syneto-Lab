capitals = {
    'Alba': 'Alba Iulia',
    'Arad': 'Arad',
    'Argeș': 'Pitești',
    'Bacău': 'Bacău',
    'Bihor': 'Oradea',
    'Bistrița-Năsăud': 'Bistrița',
    'Botoșani': 'Botoșani',
    'Brăila': 'Brăila',
    'Brașov': 'Brașov',
    'Buzău': 'Buzău',
    'Călărași': 'Călărași',
    'Caraș-Severin': 'Reșița',
    'Cluj': 'Cluj-Napoca',
    'Constanța': 'Constanța',
    'Covasna': 'Sfântu Gheorghe',
    'Dâmbovița': 'Târgoviște',
    'Dolj': 'Craiova',
    'Galați': 'Galați',
    'Giurgiu': 'Giurgiu',
    'Gorj': 'Târgu Jiu',
    'Harghita': 'Miercurea Ciuc',
    'Hunedoara': 'Deva',
    'Ialomița': 'Slobozia',
    'Iași': 'Iași',
    'Ilfov': 'București',
    'Maramureș': 'Baia-Mare',
    'Mehedinți': 'Drobeta Turnu-Severin',
    'Mureș': 'Târgu Mureș',
    'Neamț': 'Piatra Neamț',
    'Olt': 'Slatina',
    'Prahova': 'Ploiești',
    'Sălaj': 'Zalău',
    'Satu-Mare': 'Satu-Mare',
    'Sibiu': 'Sibiu',
    'Suceava': 'Suceava',
    'Teleorman': 'Alexandria',
    'Timiș': 'Timișoara',
    'Tulcea': 'Tulcea',
    'Vâlcea': 'Râmnicu Vâlcea',
    'Vaslui': 'Vaslui',
    'Vrancea': 'Focșani',

}

def judet(capital):
    for c in capitals:
        if(capitals[c] == capital):
            return c
    return 'Unknown'

print(judet('Timișoara'))