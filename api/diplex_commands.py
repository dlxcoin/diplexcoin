import requests
import json

# request example
# curl --user diplex_user:diplex_password --data-binary '{"jsonrpc": "1.0", "id":"curltext", "method": "getinfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:****/

def get_info():
    headers = {
        'content-type': 'text/plain;',
    }

    data = '{"jsonrpc": "1.0", "id":"curltext", "method": "getinfo", "params": [] }'

    response = requests.post(DIPLEXCOIN_URL, headers=headers, data=data, auth=(RPC_USER, RPC_PASSWORD))
    return response._content



def get_new_address(account):
    headers = {'content-type': 'text/plain;'}

    data = '{"jsonrpc": "1.0", "id":"curltext", "method": "getnewaddress", "params": ["'+str(account)+'"] }'

    response = requests.post(DIPLEXCOIN_URL, headers=headers, data=data, auth=(RPC_USER, RPC_PASSWORD))
    struct = json.loads(response._content)
    return struct['result']


def get_balance(address):
    headers = {'content-type': 'text/plain;'}

    data = '{"jsonrpc": "1.0", "id":"curltext", "method": "getbalance", "params": ["'+str(get_account(address))+'"] }'

    response = requests.post(DIPLEXCOIN_URL, headers=headers, data=data, auth=(RPC_USER, RPC_PASSWORD))
    struct = json.loads(response._content)
    return struct['result']


def get_account(address):
    headers = {'content-type': 'text/plain;'}

    data = '{"jsonrpc": "1.0", "id":"curltext", "method": "getaccount", "params": ["'+address+'"] }'

    response = requests.post(DIPLEXCOIN_URL, headers=headers, data=data, auth=(RPC_USER, RPC_PASSWORD))
    struct = json.loads(response._content)
    return struct['result']




def send_from(address_to, amount, address_from=RPC_ADDR):
    headers = {'content-type': 'text/plain;'}

    data = '{"jsonrpc": "1.0", "id":"curltext", "method": "sendfrom", "params": ["'+get_account(address_from)+'", "'+address_to+'", '+str(Decimal(amount)*Decimal(0.99999))+'] }'

    response = requests.post(DIPLEXCOIN_URL, headers=headers, data=data, auth=(RPC_USER, RPC_PASSWORD))
    struct = json.loads(response._content)
    return struct


def transfer_admin(amount, address_from):
    headers = {'content-type': 'text/plain;'}

    data = '{"jsonrpc": "1.0", "id":"curltext", "method": "sendfrom", "params": ["'+get_account(address_from)+'", "'+settings.RPC_ADDR+'", '+str(Decimal(amount)*Decimal(0.99999))+'] }'

    response = requests.post(DIPLEXCOIN_URL, headers=headers, data=data, auth=(RPC_USER, RPC_PASSWORD))
    struct = json.loads(response._content)
    return struct['result']