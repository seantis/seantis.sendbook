from Products.PloneTestCase.ptc import PloneTestCase
from seantis.sendbook.tests.layer import SENDBOOK_INTEGRATION_TESTING

class TestCase(PloneTestCase):

    layer = SENDBOOK_INTEGRATION_TESTING
