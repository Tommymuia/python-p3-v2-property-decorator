#!/usr/bin/env python3

class Dog:
    approved_breeds = [
        "Corgi", "Beagle", "Pug", "Dalmatian", "Bulldog", "Labrador", "Golden Retriever", "Mutt"
    ]

    def __init__(self, name="Fido", breed="Mutt"):
        # Use property setters to validate
        self.name = name
        self.breed = breed

    # Name property with validation
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            raise ValueError("Name must be a string between 1 and 25 characters.")
        self._name = value

    # Breed property with validation
    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value not in self.approved_breeds:
            raise ValueError("Breed must be in list of approved breeds.")
        self._breed = value

    # Example instance methods (optional, for your previous tests)
    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")
