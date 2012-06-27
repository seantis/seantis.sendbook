from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

class SendbookTestLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import seantis.sendbook
        self.loadZCML(package=seantis.sendbook)

        # Install product and call its initialize() function
        z2.installProduct(app, 'seantis.sendbook')

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'seantis.sendbook:default')

    def tearDownZope(self, app):
        # Uninstall product
        z2.uninstallProduct(app, 'seantis.sendbook')

SENDBOOK_FIXTURE = SendbookTestLayer()
SENDBOOK_INTEGRATION_TESTING = IntegrationTesting(bases=(SENDBOOK_FIXTURE,), name="Sendbook:Integration")
