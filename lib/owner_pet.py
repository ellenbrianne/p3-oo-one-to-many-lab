class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=""):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.add_instance(self)

    def get_pet_type(self):
        return self._pet_type
                
    def set_pet_type(self, pet_type):
        if pet_type in self.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception

    pet_type = property(get_pet_type, set_pet_type)

    @classmethod
    def add_instance(cls, self):
        cls.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
        
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception
        
    def get_sorted_pets(self):    
        owned_pets = [pet for pet in Pet.all if pet.owner == self]
        def get_name(obj):
            return obj.name
        owned_pets.sort(key=get_name)
        return owned_pets