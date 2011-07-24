import web, os, re, json, string, urllib
import pprint
import bitcoin
from btcdjson import BitcoindJson
from sqlite3 import dbapi2 as sqlite

btcd = bitcoin.connect_to_remote('eli', 'isthemaster')

urls = (
    '/', 'main',
    '/api/(.*)', 'API',
    '/tests', 'testingInterface'
)

    
btcJson = BitcoindJson('eli', 'isthemaster')



db = sqlite.connect('main.db')
dbc = db.cursor()

render = web.template.render('templates/')

class API:
    def GET(self, action = None):
        request = web.input()
        result = btcJson(action, web.input())
        return result
    
    
class testingInterface:
    def GET(self):
        return render.tests()
    
        
class main:
    def GET(self):
        get = web.input(loadPartial=False)
        
        
        if get.loadPartial != False:
            
            content = web.template.frender('templates/partial/' + get.loadPartial + '.html')()
        
        else:
            dashboard = web.template.frender('templates/partial/dashboard.html')()
            content = render.main(unicode(dashboard))

        return content


app = web.application(urls, globals(), True)

if __name__ == "__main__":
    app.run()
