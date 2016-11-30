import imaplib


mailcall = imaplib.IMAP4_SSL('imap.gmail.com', '993')
mailcall.login('slammingrooves@gmail.com', 'dnazuedrhfqrnkjx')
mailcall.select()
a = len(mailcall.search(None, 'UnSeen')[1][0].split())
print(a)

# TODO call the username and password from a gpg encrypted file
