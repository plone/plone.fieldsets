import unittest

from zope.component import testing
from zope.testing import doctest

OPTIONFLAGS = (doctest.REPORT_ONLY_FIRST_FAILURE |
               doctest.ELLIPSIS |
               doctest.NORMALIZE_WHITESPACE)

def test_suite():
    return unittest.TestSuite((
        doctest.DocFileSuite(
            'fieldsets.txt',
            setUp=testing.setUp,
            tearDown=testing.tearDown,
            optionflags=OPTIONFLAGS),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
