# lib/owner.py
class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        # Returns all the pets of this owner
        return self._pets

    def add_pet(self, pet):
        # Ensure pet is an instance of the Pet class
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type. Must be an instance of the Pet class.")
        
        # Assign owner to the pet
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        # Returns a sorted list of pets by their names
        return sorted(self._pets, key=lambda pet: pet.name)

class Pet:
    # Class variables
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        # Validate that the pet_type is valid
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Must be one of {Pet.PET_TYPES}")
        
        self.pet_type = pet_type
        self.owner = owner
        
        # Add this pet instance to the all class variable list
        Pet.all.append(self)

    @staticmethod
    def get_all():
        # Return all instances of Pet
        return Pet.all
