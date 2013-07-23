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


class Factory(object):
    """Creates BaseCaptcha instances on demand, and tests solutions.  CAPTCHAs
    expire after a given amount of time, given in seconds.  The default is 15
    minutes.  """

    def __init__(self, lifetime=60*15):
        self.lifetime = lifetime
        self.stored_instances = {}

    def new(self, cls, *args, **kwargs):
        """Create a new instance of our assigned BaseCaptcha subclass, passing
        it any extra arguments we're given. This stores the result for later
        testing.  """
        self.clean()
        inst = cls(*args, **kwargs)
        self.stored_instances[inst.id] = inst
        return inst

    def get(self, id):
        """Retrieve the CAPTCHA with the given ID. If it's expired already,
        this will return None. A typical web application will need to new() a
        CAPTCHA when generating an html page, then get() it later when its
        images or sounds must be rendered.  """
        return self.stored_instances.get(id)

    def clean(self):
        """Removed expired tests"""
        expired_ids = []
        now = time.time()
        for inst in self.stored_instances.values():
            if inst.creationTime + self.lifetime < now:
                expired_ids.append(inst.id)
        for id in expired_ids:
            del self.stored_instances[id]

    def test(self, id, solutions):
        """Test the given list of solutions against the BaseCaptcha instance
        created earlier with the given id. Returns True if the test passed,
        False on failure. In either case, the test is invalidated. Returns
        False in the case of an invalid id.  """
        self.clean()
        inst = self.stored_instances.get(id)
        if not inst:
            return False
        result = inst.testSolutions(solutions)
        return result


class PersistentFactory(Factory):
    """A simple persistent factory, for use in CGI or multi-process
    environments where the state must remain across python interpreter
    sessions.  This implementation uses the 'shelve' module.  """

    def __init__(self, filename, lifetime=60*15):
        Factory.__init__(self, lifetime)
        self.stored_instances = shelve.open(filename)
