import redis
import os

def redis_sentinel_connection():
    try:
        redis_db = redis.StrictRedis(host="", port=)
    except:
        print("Cant Connect to Redis Server")
        raise
    return redis_db

def get_sentinal_info():
    connection = redis_sentinel_connection()
    sentinel_info = connection.info()
    return sentinel_info

def get_master_info(num):
    info = get_sentinal_info()
    return info["master{}".format(num)]

def get_masters():
    ip_list = []
    info = get_sentinal_info()
    count = info["sentinel_masters"]
    for i in range(count):
        master_info = get_master_info(i)
        ip_list.append(master_info['address'])
    return ip_list

def write_ip_file():
    list_ip = get_masters()
    with open("D:\\Python\\Twemproxy_orcestrator\\ipaddr.txt", "w") as f:
        f.writelines(",".join(list_ip))

def read_ip_file():
    with open("D:\\Python\\Twemproxy_orcestrator\\ipaddr.txt", "r") as f:
        return f.readline()


def make_conf_file():
    with open("D:\\Python\\Twemproxy_orcestrator\\nutcracker.yml", "w") as f:
        f.write("""
redis_test_configuration:
    listen: 
    client_connections: 2
    hash: fnv1a_64
    hash_tag: "{}"
    distribution: modula
    timeout: 400
    preconnect: true
    auto_eject_hosts: true
    redis: true
    redis_auth: 
    server_retry_timeout: 2000
    server_failure_limit: 1
    servers:\n""")
        f.write("\n".join('    - {} 1'.format(i) for i in get_masters()))

def make_compare():
    string1 = ",".join(get_masters())
    if os.path.exists("ipaddr.txt") == False or os.path.getsize("ipaddr.txt") == 0:
        write_ip_file()
        make_conf_file()
        print( 'File created' )
    elif read_ip_file() != string1:
        make_conf_file()
        write_ip_file()
        print( 'Text added' )
    else:
        print('Nothing to do')

make_compare()




