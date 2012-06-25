from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTPException
from zope import interface, schema
from zope.component import getMultiAdapter
from z3c.form import form, field, button
from plone.app.z3cform.layout import wrap_form

from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.utils import checkEmailAddress
from Products.CMFDefault.exceptions import EmailAddressInvalid
from Products.statusmessages.interfaces import IStatusMessage
from ftw.pdfgenerator.interfaces import IPDFAssembler

from seantis.sendbook import _

class InvalidEmailAddress(schema.ValidationError):
    _(u'Invalid email address')

def validateaddress(value):
    try:
        checkEmailAddress(value)
    except EmailAddressInvalid:
        raise InvalidEmailAddress(value)
    return True

class ISendbookForm(interface.Interface):
    """ Define form fields """

    sender = schema.TextLine(title=_('sender_title', default=u'Sender'),
                            description=_('sender_description', default=u''),
                            required=True,
                            constraint=validateaddress)
    receiver = schema.TextLine(title=_('receiver_title', default=u'Receiver'),
                            description=_('receiver_description', default=u''),
                            required=True,
                            constraint=validateaddress)
    

class SendbookForm(form.Form):
    """ Define Form handling """

    fields = field.Fields(ISendbookForm)
    ignoreContext = True
    label = _('form_label', default=u'Send book as PDF')
    description = _('form_description', default=u'')
    
    def compose_mail(self, sender, receiver):
        # Create PDF file
        assembler = getMultiAdapter((self.context, self.request), IPDFAssembler)
        pdf_file = assembler.build_pdf()
        
        # Compose mail
        msg = MIMEMultipart()
        msg['Subject'] = _('Book')
        msg['From'] = sender
        msg['To'] = receiver
        # Text block
        part = MIMEText(_('Book PDF attached'))
        msg.attach(part)
        # PDF attachement
        part = MIMEApplication(pdf_file)
        filename = '%s.pdf' % self.context.id
        part.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(part)
        return msg

    @button.buttonAndHandler(_(u'Send'))
    def handleApply(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        
        # Send mail
        mail_host = getToolByName(self, 'MailHost')
        try:
            msg = self.compose_mail(data['sender'], data['receiver'])
            mail_host.send(msg, immediate=True)
            msg = _(u'Message sent.')
            IStatusMessage(self.request).addStatusMessage(msg, type='info')
            self.request.RESPONSE.redirect(self.context.absolute_url())
        except SMTPException:
            msg = _('Error while sending email.')
            IStatusMessage(self.request).addStatusMessage(msg, type='error')
        
    @button.buttonAndHandler(_(u'Cancel'))
    def handleCancel(self, action):
        self.request.RESPONSE.redirect(self.context.absolute_url())
        
SendbookView = wrap_form(SendbookForm)
