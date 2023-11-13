import unittest
from math_quiz import get_random_int, get_random_op, calculation


class TestMathGame(unittest.TestCase):

    def test_get_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_op(self):
        operator = {'+', '-', '*'}
        for _ in range(1000):
            random_ope = get_random_op()
            self.assertIn(random_ope, operator)

    def test_calculation(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7), (2, 2, '-', '2 - 2', 0), (4, 1, '*', '4 * 1', 4)]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            test_problem, test_answer = calculation(num1, num2, operator)
            self.assertEquals(test_problem, expected_problem)
            self.assertEquals(test_answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
