import imaplib


def mail_time():
    import gi
    gi.require_version('Notify', '0.7')
    from gi.repository import Notify
    Notify.init("Mail Check")
    new_mail = Notify.Notification.new("You have mail.")
    new_mail.show()

mailcall = imaplib.IMAP4_SSL('imap.gmail.com', '993')
mailcall.login('@gmail.com', '')
mailcall.select()
a = len(mailcall.search(None, 'UnSeen')[1][0].split())
if a > 0:
    mail_time()

# TODO call the username and password from a gpg encrypted file
