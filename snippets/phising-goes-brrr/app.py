#
# This used for flooding phisnig site
# Use at your own risk
#

import requests, random, string

##
## datatype using string.printable or similar,
## or create your own array ['a','b','c'] for example
##
def randomizer(datatype, length):
    return ''.join(random.choice(datatype) for i in range(length))
##
## while(1), endless pain
## sometimes the phising site got instant suspended
##
while (1):
    ##
    ## in order to make the scammer get confused
    ## create a list full of random name in json
    ## join data with username
    ## voila, randomized username with legit name.
    ##
    data = {
        'username': '' + randomizer(string.ascii_lowercase, 5) + '@mail.adrress.tld',
        'password': randomizer(string.printable, 16),
        'submit': 'Submit'
    }

    ##
    ## fit your data here,
    ## including url, method
    ## in this case using post
    ##
    doom = requests.post(
        'https://yubi.fbk.local/post_debug', ## yes, this is local site, for testing purpose, replace this.
        data = data
    )
    print(str(doom.status_code) + " -> " + str(data))

