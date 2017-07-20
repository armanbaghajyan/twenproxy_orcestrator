mylist= ['192.168.0.194:6379','192.168.0.194:6380']


with open("D:\Python\Twemproxy_orcestrator\\nutcracker1.yml","wt") as f:
    f.write("\n".join('    - {} 1'.format(i) for i in mylist))

f = open("D:\Python\Twemproxy_orcestrator\\nutcracker.yml","r")
g = open("D:\Python\Twemproxy_orcestrator\\nutcracker1.yml","r")
h = open("D:\Python\Twemproxy_orcestrator\\nutcracker3.yml","a")
for line in f:
    h.write(line)
for line in g:
    h.write(line)
f.close()
g.close()
h.close()
