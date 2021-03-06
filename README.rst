.. image:: https://travis-ci.org/icook/simplecaptcha.png?branch=master
    :target: https://travis-ci.org/icook/simplecaptcha

About
-----

This is the SimpleCaptcha package, a Python module implementing CAPTCHAs:
automated tests that humans should pass, but current computer programs can't
(or have difficulty with). These tests are often used for security and bot
detection.

This is a fork of the slightly older PyCAPTCHA package by Micah Dowty, and
credit for the majority of the functionality in the package is his.

Main goals/changes from the original:

- **X** Better PEP8 compliance, mainly with respect to module/function/parameter names
- **X** A new name so it can be released via PIP for easy installation
- Integration with more modern methods for storing Captcha solutions
- **X** Python 3.3 support and decent test coverage
- **X** Refactor for use with Pillow since since PIL is being left behind

Dependencies
------------

-  Python 2.6, 2.7, or 3.3
-  Pillow, a new port of the Python Image Library
