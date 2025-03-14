#Jacob Juarez

import sys
import os

# Check if the file exists in the directory
file_path = 'C:/Users/jacob/homeworkfolder-JacobJuarez24/Labs/Lab 05/Code_to_Test.py'
if os.path.exists(file_path):
    print(f"File found: {file_path}")
else:
    print(f"File not found: {file_path}")

sys.path.append('C:/Users/jacob/homeworkfolder-JacobJuarez24/Labs/Lab 05')
print("Updated sys.path:", sys.path)

# Import the Code_to_Test module
try:
    import Code_to_Test
except ImportError as e:
    print(f"Error importing: {e}")

import unittest
from io import StringIO
import sys
from unittest.mock import patch


class TestFarm(unittest.TestCase):

    def setUp(self):
        # Create test animals for the farm using Code_to_Test module
        self.dog = Code_to_Test.Dog("Buddy", 3, breed="Golden Retriever")
        self.cat = Code_to_Test.Cat("Whiskers", 2, breed="Siamese")
        self.bird = Code_to_Test.Bird("Tweety", 1, breed="Canary")
        self.horse = Code_to_Test.Horse("Spirit", 5)
        self.sheep = Code_to_Test.Sheep("Dolly", 4)
        self.pig = Code_to_Test.Pig("Porky", 2)

        # Create a farm and add animals
        self.farm = Code_to_Test.Farm()
        self.farm.add_animal(self.dog)
        self.farm.add_animal(self.cat)
        self.farm.add_animal(self.bird)
        self.farm.add_animal(self.horse)
        self.farm.add_animal(self.sheep)
        self.farm.add_animal(self.pig)

    def test_animal_types(self):
        # Test that animals are correctly initialized
        self.assertEqual(self.dog.name, "Buddy")
        self.assertEqual(self.cat.breed, "Siamese")
        self.assertEqual(self.bird.name, "Tweety")
        self.assertEqual(self.horse.age, 5)
        self.assertEqual(self.sheep.name, "Dolly")
        self.assertEqual(self.pig.age, 2)

    def test_add_animal(self):
        # Test that animals are added to the farm
        new_dog = Code_to_Test.Dog("Max", 4, breed="Bulldog")
        self.farm.add_animal(new_dog)
        self.assertIn(new_dog, self.farm.animals)

    def test_remove_animal(self):
        # Test that animals are removed from the farm
        self.farm.remove_animal("Buddy")
        self.assertNotIn(self.dog, self.farm.animals)

    def test_show_animals(self):
        # Test that all animals on the farm are shown correctly
        output = StringIO()
        sys.stdout = output  # Redirect stdout to capture printed statements
        self.farm.show_animals()
        sys.stdout = sys.__stdout__  # Reset stdout

        animals_on_farm = "\n".join(str(animal) for animal in self.farm.animals)
        self.assertIn("Buddy", animals_on_farm)  # Check if dog is in the list
        self.assertIn("Whiskers", animals_on_farm)  # Check if cat is in the list

    def test_invalid_animal_type(self):
        # Test that invalid animal types are not accepted
        with patch("builtins.input", return_value="elephant"):
            with patch("sys.stdout", new_callable=StringIO) as fake_out:
                self.farm.add_animal(None)  # Simulate invalid animal type
                output = fake_out.getvalue().strip()
                self.assertIn("Invalid animal type", output)  # Check if error message appears

    def test_remove_nonexistent_animal(self):
        # Test trying to remove an animal that doesn't exist on the farm
        result = self.farm.remove_animal("NonExistent")
        self.assertEqual(result, "Animal NonExistent not found on the farm.")

    def test_edge_case_show_no_animals(self):
        # Test showing animals when there are no animals on the farm
        empty_farm = Code_to_Test.Farm()
        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            empty_farm.show_animals()
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "No animals on the farm")  # Check if the message matches

    def test_show_animal_count(self):
        # Test to ensure that the farm has the correct number of animals
        self.assertEqual(len(self.farm.animals), 6)  # There should be 6 animals initially

    def test_add_multiple_animals(self):
        # Test adding multiple animals at once
        new_cat = Code_to_Test.Cat("Snowball", 3, breed="Persian")
        new_bird = Code_to_Test.Bird("Chirpy", 2, breed="Parrot")
        self.farm.add_animal(new_cat)
        self.farm.add_animal(new_bird)
        self.assertIn(new_cat, self.farm.animals)
        self.assertIn(new_bird, self.farm.animals)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'])
