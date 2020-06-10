<?php
include('vendor/rmccue/requests/library/Requests.php');

const RPC_URL = 'http://127.0.0.1:****/'
const RPC_USER = 'diplex_user'
const RPC_PASSWORD = 'diplex_password'

# request example
# curl --user diplex_user:diplex_password --data-binary '{"jsonrpc": "1.0", "id":"curltext", "method": "getinfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:****/


function getInfo(){
	Requests::register_autoloader();
	$headers = array(
	    'content-type' => 'text/plain;'
	);

	$data = '{"jsonrpc": "1.0", "id":"curltext", "method": "getinfo", "params": [] }';

	$options = array('auth' => array(self::RPC_USER, self::RPC_PASSWORD));

	$response = Requests::post(self::RPC_URL, $headers, $data, $options);

	return json_decode($response)
}

function getNewAddress(account){
	Requests::register_autoloader();
	$headers = array(
	    'content-type' => 'text/plain;'
	);

	$data = '{"jsonrpc": "1.0", "id":"curltext", "method": "getnewaddress", "params": ["'.account.'"] }';

	$options = array('auth' => array(self::RPC_USER, self::RPC_PASSWORD));

	$response = Requests::post(self::RPC_URL, $headers, $data, $options);

	return json_decode($response)['result']
}

function getBalance(address){
	Requests::register_autoloader();
	$headers = array(
	    'content-type' => 'text/plain;'
	);

	$data = '{"jsonrpc": "1.0", "id":"curltext", "method": "getbalance", "params": ["'.getAccount(address).'"] }';

	$options = array('auth' => array(self::RPC_USER, self::RPC_PASSWORD));

	$response = Requests::post(self::RPC_URL, $headers, $data, $options);

	return json_decode($response)['result']
}

function getAccount(address){
	Requests::register_autoloader();
	$headers = array(
	    'content-type' => 'text/plain;'
	);

	$data = '{"jsonrpc": "1.0", "id":"curltext", "method": "getaccount", "params": ["'.address.'"] }';

	$options = array('auth' => array(self::RPC_USER, self::RPC_PASSWORD));

	$response = Requests::post(self::RPC_URL, $headers, $data, $options);

	return json_decode($response)['result']
}

function sendFrom(address_to, amount, address_from=self::RPC_ADDR){
	Requests::register_autoloader();
	$headers = array(
	    'content-type' => 'text/plain;'
	);

	$data = '{"jsonrpc": "1.0", "id":"curltext", "method": "getbalance", "params": ["'.address_from.'","'.address_to.'","'.amount.'"] }';

	$options = array('auth' => array(self::RPC_USER, self::RPC_PASSWORD));

	$response = Requests::post(self::RPC_URL, $headers, $data, $options);

	return json_decode($response)['result']
}

