import random
import string

class DataGenerator:
    @staticmethod
    def random_string(length=10):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))

    @staticmethod
    def random_int(min_value=0, max_value=100):
        return random.randint(min_value, max_value)

    @staticmethod
    def random_float(min_value=0.0, max_value=100.0):
        return random.uniform(min_value, max_value)

# Example usage
if __name__ == '__main__':
    print("Random String:", DataGenerator.random_string())
    print("Random Integer:", DataGenerator.random_int())
    print("Random Float:", DataGenerator.random_float())