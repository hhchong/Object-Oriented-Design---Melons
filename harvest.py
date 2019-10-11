############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, name, code, first_harvest, color, is_seedless,
                 is_bestseller):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, *pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code

    def check_attributes(self):
        """Return a list of all instance attributes
        Helper Function
        """
        return [self.name, self.pairings, self.code, self.first_harvest,
                self.color, self.is_seedless, self.is_bestseller]


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('Muskmelon', 'musk', 1998, 'green', True, True)
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType("Casaba", "cas", 2003, "orange", False, None)
    cas.add_pairing('strawberries', 'mint')
    all_melon_types.append(cas)

    cren = MelonType('Crenshaw', 'cren', 1996, 'green', True, None)
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('Yellow Watermelon', 'yw', 2013, 'yellow', False, True)
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types

melon_types = make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs with')
        for pairing in melon.pairings:
            print('-', pairing)


# print_pairing_info(melon_types)

    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    lookup = {}
    for melon in melon_types:
        lookup[melon.code] = lookup.get(melon.code, melon)

    return lookup

melons_by_id = make_melon_type_lookup(melon_types)

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, melon_type, shape_rating, color_rating, harvest_field,
                 harvested_by):

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_field = harvest_field
        self.harvested_by = harvested_by

    def print_attributes(self):
        print([self.melon_type, self.shape_rating, self.color_rating, self.harvest_field, self.harvested_by])

    def is_sellable(self):
        """Returns True or False whether melon can be sold

        True if shape and color rating greater than 5 and not from Field 3 """
        
        return self.shape_rating > 5 and self.color_rating > 5 and self.harvest_field != 3

def make_melons(melon_file, melons_by_id):
    """Returns a list of Melon objects."""
    all_melons = []

    for line in melon_file:
        line = line.rstrip().split()
        melon_id = melons_by_id[line[5]]
        melon_shape = int(line[1])
        melon_color = int(line[3])
        melon_harvested_by = line[8]
        melon_field = int(line[-1])
        melon = Melon(melon_id, melon_shape, melon_color, melon_field, melon_harvested_by)

        all_melons.append(melon)


    # melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    # all_melons.append(melon_1)

    # melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    # all_melons.append(melon_2)

    # melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    # all_melons.append(melon_3)

    # melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    # all_melons.append(melon_4)

    # melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    # all_melons.append(melon_5)

    # melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    # all_melons.append(melon_6)

    # melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    # all_melons.append(melon_7)

    # melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    # all_melons.append(melon_8)

    # melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')
    # all_melons.append(melon_9)

    return all_melons

melon_file = open("harvest_log.txt")

all_melons = make_melons(melon_file, melons_by_id)

def get_sellability_report(all_melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in all_melons:
        if melon.is_sellable():
            status = "GOOD TO GO"
        else:
            status = "DO NOT SELL"
        print(f'Harvested by {melon.harvested_by} from Field {melon.harvest_field} ({status})')


get_sellability_report(all_melons)