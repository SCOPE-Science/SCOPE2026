import math, itertools

def accepts(w,beta,start=0.0):
 d=start
 for a,b in zip(w,w[1:]):
  d+= beta if a=='0' else -1
  if a=='1' and (b=='1') != (d>=0): return False
 return True

def disc(w,beta):return beta*w.count('0')-w.count('1')

def lastclose(prefix,beta):
 s=prefix
 # append a sufficiently large zero run and its entire forced one run.
 if s.endswith('1'):
  d=disc(s,beta)
  while d>=0:
   s+='1';d-=1
  s+='0'
 s+='00000000'
 d=disc(s,beta)
 s+='1'*(math.floor(d)+1)
 assert -1-1e-10 < disc(s,beta)<0 and accepts(s,beta)
 return s

def connect(u,v,beta):
 x=lastclose(u,beta)
 e=disc(x,beta)
 assert -1<e<0
 for m in range(1,20001):
  d=e+beta*m
  if d < 0:continue
  L=math.floor(d)+1
  r=d-L
  t=x+'0'*m+'1'*L+('0'+v[1:] if v.startswith('0') else v[1:])
  if accepts(t,beta) and u in t and v in t and t.find(v,u.__len__())>=0:
   return m,t
 raise AssertionError((u,v))
for beta in [math.sqrt(2),math.sqrt(3)/2,(1+math.sqrt(5))/2,math.pi]:
 words=[''.join(z) for n in range(1,7) for z in itertools.product('01',repeat=n) if accepts(''.join(z),beta)]
 for u in words:
  for v in words:
   m,t=connect(u,v,beta)
 print('PASS',beta,'prefixes',len(words),'tested',len(words)**2)
