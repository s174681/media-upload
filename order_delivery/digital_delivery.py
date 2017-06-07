class DigitalDelivery:

    def __init__(self):
        pass

    def deliver(self, email, animation_ref):
        pass

from mailer import send_mail


class EmailDelivery(DigitalDelivery):
    def deliver(self, email, animation_ref):
        send_mail(to=email, vars={'download_url': animation_ref})

    def __init__(self, mailer):
        DigitalDelivery.__init__(self)