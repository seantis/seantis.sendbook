from zope.component import provideAdapter, adapts
from zope.interface import Interface, implements
from ftw.pdfgenerator.interfaces import IPDFAssembler

from seantis.sendbook.browser.sendbook import SendbookForm
from seantis.sendbook.tests import TestCase
        
class DummyAssembler(object):
    
    adapts(Interface, Interface)
    implements(IPDFAssembler)
    
    def __init__(self, context, request):
        pass
    
    def build_pdf(self):
        return u'File content'

class SendbookFormTests(TestCase):
    
    def test_compose_mail(self):
        provideAdapter(DummyAssembler)
        context = object()
        request = self.portal.REQUEST
        form = SendbookForm(context, request)
        msg = form.compose_mail('sender@example.com', 'receiver@example.com')
        self.assertEqual('sender@example.com', msg['From'])
        self.assertEqual('receiver@example.com', msg['To'])
        text_part = msg.get_payload()[0]
        self.assertEqual('text/plain', text_part.get_content_type())
        pdf_part = msg.get_payload()[1]
        self.assertEqual('application/octet-stream', pdf_part.get_content_type())
