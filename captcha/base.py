""" Captcha.Base

Base class for all types of CAPTCHA tests. All tests have one or
more solution, determined when the test is generated. Solutions
can be any python object,

All tests can be solved by presenting at least some preset number
of correct solutions. Some tests may only have one solution and require
one solution, but other tests may require N correct solutions of M
possible solutions.

SimpleCaptcha Package
Forked from PyCAPTCHA Copyright (C) 2004 Micah Dowty <micah@navi.cx>
"""
import random
import string
import time
import shelve

__all__ = ["BaseCaptcha", "Factory", "PersistentFactory"]


def random_identifier(alphabet=string.ascii_letters + string.digits,
                      length=24):
    return "".join([random.choice(alphabet) for i in range(length)])


class BaseCaptcha(object):
    """Base class for all CAPTCHA tests"""
    # Subclasses can override these to set the solution criteria
    min_correct_solutions = 1
    max_incorrect_solutions = 0

    def __init__(self):
        self.solutions = []
        self.valid = True

        # Each test has a unique identifier, used to refer to that test
        # later, and a creation time so it can expire later.
        self.id = randomIdentifier()
        self.creation_time = time.time()

    def add_solution(self, solution):
        self.solutions.append(solution)

    def test_solutions(self, solutions):
        """Test whether the given solutions are sufficient for this CAPTCHA.  A
        given CAPTCHA can only be tested once, after that it is invalid and
        always returns False. This makes random guessing much less effective.
        """
        if not self.valid:
            return False
        self.valid = False

        num_correct = 0
        num_incorrect = 0

        for solution in solutions:
            if solution in self.solutions:
                num_correct += 1
            else:
                num_incorrect += 1

        return num_correct >= self.min_correct_solutions and \
            num_incorrect <= self.max_incorrect_solutions
