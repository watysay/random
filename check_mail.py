# coding: utf-8

import getpass, imaplib

# foireux
# éléments à reprendre dans la sélection/recherche/affichage

# connexion
#M = imaplib.IMAP4()
M = imaplib.IMAP4_SSL('imap.gmail.com')

# auth
#M.login(getpass.getuser(), getpass.getpass())
M.login('sebastien.manic@gmail.com', getpass.getpass())

# a trier/refaire/adapter
M.select()
typ, data = M.search(None,'UNSEEN')
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    print 'Message %s\n%s\n' % (num, data[0][1])

    
# fin
M.close()
M.logout()
