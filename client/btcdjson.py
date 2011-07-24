import json, bitcoin

from bitcoin.connection import BitcoinConnection

class BitcoindJson (BitcoinConnection):
    def __call__(self, method, args = None, toJson = True):
        result = {}

        try:
            selfMethod = getattr(self, method)
            result['result'] = selfMethod(**args)
        except AttributeError, e:
            print 'AttributeError: {0} '.format(e)
            result['error'] = 'No such method'
        
        if json:
            jsoned = json.dumps(result, indent = 2)
            return jsoned
        else:
            return result
    
    # Reflected Functions
    
    def getAccount (self, address):
        result = self.getaccount(address)
        return result
    
    def getAccountAddress (self, account):
        result = self.getaccountaddress(account)
        return result
    
    def getAddressesByAccount (self, account):
        result = self.getaddressesbyaccount(account)
        return result
        
    def getReceivedByAccount (self, account, minconf = 1):
        minconf = int(minconf)

        result = self.getreceivedbyaccount(account, minconf);

        return result
        
    def getReceivedByAddress (self, address, minconf = 1):
        minconf = int(minconf)
        result = self.getreceivedbyaddress(address, minconf);
        return result
        
    def getBalance (self, account = None):
        return self.getbalance(account)
    
    def getInfo (self):
        info = self.getinfo()
        retval = {
            'errors': info.errors,
            'blocks': info.blocks,
            'paytxfee': info.paytxfee,
            'keypoololdest': info.keypoololdest,
            'genproclimit': info.genproclimit,
            'connections': info.connections,
            'difficulty': info.difficulty,
            'testnet': info.testnet,
            'version': info.version,
            'proxy': info.proxy,
            'hashespersec': info.hashespersec,
            'balance': info.balance,
            'generate': info.generate
        }
        
        return retval
    
    def listReceivedByAccount (self, minconf = 1, includeempty = False):
        minconf = int(minconf)
        includeempty = bool(includeempty)
        
        result = self.listreceivedbyaccount(minconf, includeempty)
        retval = []
        
        for acc in result:
            account = {
                'account': acc.account,
                'confirmations': acc.confirmations,
                'amount': acc.amount,
                'label': acc.label
            }
            
            retval.append(account)
            
        return retval
    
    def listReceivedByAddress (self, minconf = 1, includeempty = False):
        minconf = int(minconf)
        includeempty = bool(includeempty)
        
        result = self.listreceivedbyaddress(minconf, includeempty)
        retval = []
        
        for acc in result:
            address = {
                'account': acc.account ,
                'confirmations': acc.confirmations,
                'amount': acc.amount,
                'address': acc.address
            }
            
            retval.append(address)
            
        
        return retval
    
    def listTransactions (self, account = '', count = 10):
        count = int(count)
        
        result = self.listtransactions(account, count)
        retval = json.loads(result)
        
        return retval

    def endFuncion (self):
        pass