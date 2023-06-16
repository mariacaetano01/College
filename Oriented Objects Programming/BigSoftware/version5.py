# import enum method to avoid possible comparisons with strings later
from enum import Enum 

# 'enumerated' class to store brands that produce instruments
class Builder(Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collings"
    OLSON = "olson"
    RYAN = "ryan"
    PRS = "prs"
    ANY = "any"

# 'enumerated' class to store instrument types
class Type(Enum):
    ACOUSTIC = "acoustic"
    ELECTRIC = "eletric"

# 'enumerated' class to store kinds of wood used to produce instruments
class Wood(Enum):
    INDIAN_ROSEWOOD = "indian_rosewood"
    BRAZILIAN_ROSEWOOD = "brazilian_rosewood"
    MAHOGANY = "mahogany"
    MAPLE = "maple"
    COCOBOLO = "ococobolo"
    CEDAR = "cedar"
    ADIRONDACK = "adirondack"
    ALDER = "alder"
    SITKA = "sitka"
    
# 'enumerated' class to store types of mandolin
class Style(Enum):
    A = "a"
    F = "f"

# MODIFICATION: new class
# 'enumerated' class to store types of intruments   
class InstrumentType(Enum):
    GUITAR = "Guitar"
    BANJO = "Banjo"
    DOBRO = "Dobro"
    FIDDLE = "Fiddle"
    BASS = "Bass"
    MANDOLIN = "Mandolin"
    SAX = "Sax"
    UNSPECIFIED = "Unspecified"

# MODIFICATION: new class instrument 
# Now all instruments are objects of this class, without any subclass
class Instrument:
    def __init__(self, serial_number, price, spec):
        self.serial_number = serial_number
        self.price = price
        self.spec = spec

    def get_serial_number(self):
        return self.serial_number

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price

    def get_spec(self):
        return self.spec

# MODIFICATION: new class InstrumentSpec
# Now all instruments' specifications are objects of this class, without any subclass
class InstrumentSpec:
    def __init__(self, properties=None):
        if properties is None:
            self.properties = {}
        else:
            self.properties = properties.copy()

    # MODIFICATION
    # method to retrun instruments' specific property
    def get_property(self, property_name):
        return self.properties.get(property_name)

    # MODIFICATION
    # new method to return instruments's properties
    def get_properties(self):
        return self.properties

    # MODIFICATION
    # new query method to match intruments during the searhcing
    def matches(self, other_spec):
        for property_name in other_spec.get_properties():
            if self.properties.get(property_name) != other_spec.get_property(property_name):
                return False
        return True

# class Invenotory, to store intruments objects
class Inventory:
    def __init__(self):
        self.inventory = []

    # method to include new instruments objects into the inventory list object
    def add_instrument(self, serial_number, price, spec):
        instrument = Instrument(serial_number, price, spec)
        self.inventory.append(instrument)

     # search guitars or mandolins by its serial number
    def get_instrument(self, serial_number):
        for instrument in self.inventory:
            if instrument.get_serial_number() == serial_number:
                return instrument
        return None

    # MODIFICATION: new query method
    def search(self, search_spec):
        # search_spec is a InstrumentSpec object
        matching_instruments = []
        for instrument in self.inventory:
            if instrument.get_spec().matches(search_spec):
                matching_instruments.append(instrument)
        return matching_instruments
    
# MODIFICATION: new method with ready dictionaries to use as Specifications
def initialize_inventory(inventory):
    properties = {
        "instrumentType": InstrumentType.GUITAR.value,
        "builder": Builder.COLLINGS.value,
        "model": "CJ",
        "type": Type.ACOUSTIC.value,
        "numstrings": 6,
        "topwood": Wood.INDIAN_ROSEWOOD.value,
        "backwood": Wood.SITKA.value
    }
    inventory.add_instrument("11277", 3999.95, InstrumentSpec(properties))

    properties = {
        "instrumentType": InstrumentType.GUITAR.value,
        "builder": Builder.GIBSON.value,
        "model": "Les Paul",
        "type": Type.ELECTRIC.value,
        "numstrings": 6,
        "topwood": Wood.MAPLE.value,
        "backwood": Wood.MAPLE.value
    }
    inventory.add_instrument("70108276", 2295.95, InstrumentSpec(properties))

    properties = {
        "instrumentType": InstrumentType.MANDOLIN.value,
        "builder": Builder.GIBSON.value,
        "model": "F5-G",
        "type": Type.ACOUSTIC.value,
        "topwood": Wood.MAPLE.value,
        "backwood": Wood.MAPLE.value,
        "style": Style.A.value
    }
    inventory.add_instrument("9019920", 5495.99, InstrumentSpec(properties))

    properties = {
        "instrumentType": InstrumentType.BANJO.value,
        "builder": Builder.GIBSON.value,
        "model": "RB-3",
        "type": Type.ACOUSTIC.value,
        "numstrings": 5,
        "backwood": Wood.MAPLE.value
    }
    inventory.add_instrument("8900231", 2945.95, InstrumentSpec(properties))

# FIFTH VERSION TESTS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    inventory = Inventory()
    initialize_inventory(inventory)

    properties = {
        "builder": Builder.GIBSON.value,
        "backwood": Wood.MAPLE.value
    }
    
    client_spec = InstrumentSpec(properties)
    matching_instruments = inventory.search(client_spec)
    
    if matching_instruments:
        for instrument in matching_instruments:
            spec = instrument.get_spec()
            print(spec.get_property("instrumentType"), "com as seguintes propriedades:")
            for property_name, property_value in spec.get_properties().items():
                if property_name == "instrumentType":
                    continue
                print (f"{property_name}: {property_value}")
            print (f"It can be yours for just $ {instrument.get_price()}")
            print()
    else:
        print("\033[34m\nNothing Found\033[0m\n")
