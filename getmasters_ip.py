import redis

def redis_sentinel_connection():
    redis_db = redis.StrictRedis(host="192.168.0.194", port=26379)
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

with open("D:\Python\Twemproxy_orcestrator\ip_addresses.txt","w") as f:
    for ip in get_masters():
        f.write('{}\n'.format(ip))

