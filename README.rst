====================== Python CAPTCHA package ======================

About
-----

This is the SimpleCaptcha package, a Python module implementing CAPTCHAs:
automated tests that humans should pass, but current computer programs can't
(or have difficulty with). These tests are often used for security and bot
detection.

This is a fork of the slightly older PyCAPTCHA package by Micah Dowty, and
credit for the majority of the functionality in the package can be credited to
him. Main goals/changes from the original:

- Better PEP8 compliance, mainly with respect to module/function/parameter names
- A new name so it can be released via PIP for easy installation
- Integration with more modern methods for storing Captcha solutions
- Python 3.3 support and good test coverage
- Refactor for use with Pillow since since PIL is being left behind

**Note**: These goals are not yet implemented, and as such this package should
be considered unstable and not ready for production.

Examples
--------

Included are several example programs:

-  examples/simple\_example.py is a bare-bones example that just generates and
  displays an image.

-  examples/http\_example.py is a longer example that uses BaseHTTPServer to
  simulate a CAPTCHA's use in a web environment. Running this example and
  connecting to it from your web browser is a quick and easy way to see
  PyCAPTCHA in action

-  examples/modpython\_example.py is a version of http\_example that runs from
  an Apache server equipped with a properly configured mod\_python.

Dependencies
------------

-  Python 2.2.1 or later
-  the Python Imaging Library, required for visual CAPTCHAs

Contacts
--------

Micah Dowty micah@navi.cx

'scanline' on irc.freenode.net
