# Node installation and configuration

#Linux

1. Download

$ cd /your_path_to_dir

$ mkdir diplexnode

$ cd /diplexnode

$ wget https://github.com/Diplex-master/d1/raw/master/release/diplexcoind

2. Make diplexcoind exucatable

$ chmod +x diplexcoind

3. Config

$ cd /root/.diplexcoin/  // replace "root" with the name of your home directory //

$ nano diplecoin.conf

// add following strings

rpcuser = username

rpcpassword = userpass

rpcport = 8332

server = 1

rpcclienttimeout = 30

enableaccounts = 1

staking = 0

rpcallowip = 127.0.0.1 // if you want to restrict access to localhost only, use * to open worldwide //

rpcbind = 127.0.0.1

rest = 1

// save file

4. Run diplexcoind

$ cd /your_path_to_dir/diplexnode

$ chmod +X diplexcoind

$ ./diplexcoind -daemon
