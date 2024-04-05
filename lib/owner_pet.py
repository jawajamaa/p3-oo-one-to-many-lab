class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = list()

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.owner = owner
        if pet_type in type(self).PET_TYPES:
            self.pet_type = pet_type
            type(self).all.append(self)
            # line below only works is type(self).all is a dict()
            # type(self).all[self.name] = self.pet_type
        else:
            raise Exception("Pet not in PET_TYPES")
           

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # owner_list = list()
        # for pet in Pet.all:
        #     if pet.owner == self:
        #         owner_list.append(pet)
        # return owner_list 
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("Please enter a pet from the class Pet")

    def get_sorted_pets(self):
        # sorted_list = list()
        for pet in Pet.all:
            return sorted(Pet.all, key=pet.name.casefold())
            # breakpoint()
        # return sorted(Pet.all, key=pet.name.lower())

pet = Pet("Fido", "dog")
