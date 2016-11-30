# Check Gmail

I use Mutt as an email client. Mutt is a small, but very powerful text-based
email client for Unix operating systems. It's very fully featured, but I'm
using gmail, and I was resorting to opening Mutt to see if I had any new email.
A clumsy and inefficient method of doing so, IMO. So I wrote Check Gmail to
check gmail for me.

Just a simple script to check a gmail account, to see if there is any unread
email. If there is, you will get a Gnome notification. This assumes you are
using Gnome.

## Operating instructions

Put your username (your gmail address) and password in the script, in place of
'username' and 'password'. Make sure you leave the single quotes in place, or
it won't work. Open a terminal and run check_gmail.py:

    python check_gmail.py

Check and make sure the permissions are 755:

    ls -l check_gmail.py

If they're not, set them to 755. Now you can run it like this:

    ./check_gmail.py

To have it run periodically, without your own interaction, enter the following
into a crontab:

    */5 * * * * /path/to/check_gmail.py

I'm not going to lie, if you don't actually check your email when you get
a notification, it might get a little annoying when you start getting that
notification every 5 minutes. If so, change it to every 30 minutes, or
something. Or just check your damn email.

