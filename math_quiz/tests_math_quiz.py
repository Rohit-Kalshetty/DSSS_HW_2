import unittest
from math_quiz import function_A, function_B, function_C


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        result = function_B()
        self.assertGreaterEqual(result, 0)
        pass

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (10, 3, '-', '10 - 3', 7),
                (6, 2, '*', '6 * 2', 12),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                result_problem, result_answer = function_C(num1, num2, operator)
                self.assertEqual(result_problem, expected_problem)
                self.assertEqual(result_answer, expected_answer)
                pass

if __name__ == "__main__":
    unittest.main()
