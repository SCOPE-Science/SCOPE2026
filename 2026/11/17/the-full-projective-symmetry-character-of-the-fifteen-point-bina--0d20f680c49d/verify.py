from itertools import combinations
from collections import Counter
from math import gcd
vs=range(1,16)
lines={sum(1<<(i-1) for i in (a,b,a^b)) for a in vs for b in vs if a<b and a^b>b}
good=bytearray(1<<15)
for s in range(1<<15):good[s]=not any(s&line==line for line in lines)
faces=sum(good)
print('lines',len(lines),'faces',faces,flush=True)

def order(p):
 q=list(range(16));cur=list(range(16));t=0
 while 1:
  t+=1;cur=[p[x] for x in cur]
  if cur==q:return t

def character(p):
 seen=set();orbits=[]
 for a in vs:
  if a in seen:continue
  x=a;orb=0
  while x not in seen:
   seen.add(x);orb|=1<<(x-1);x=p[x]
  if good[orb]:orbits.append(orb)
 sets=[(0,1)]
 for orb in orbits:
  sets += [(mask|orb,-sgn) for mask,sgn in sets if good[mask|orb]]
 return -sum(s for _,s in sets)

cc=Counter(); byord={}; rep={}; summa=0;counts=0
for a in vs:
 for b in vs:
  if b in (a,):continue
  for c in vs:
   if c in (a,b,a^b):continue
   for d in vs:
    u={0,a,b,c,a^b,a^c,b^c,a^b^c}
    if d in u:continue
    p=[0]*16
    for i in range(16):p[i]=((a if i&1 else 0)^(b if i&2 else 0)^(c if i&4 else 0)^(d if i&8 else 0))
    ch=character(p);od=order(p);counts+=1;summa+=ch
    cc[(od,ch)]+=1;rep.setdefault((od,ch),(a,b,c,d));byord[od]=byord.get(od,0)+1
print('GL size',counts,'sum',summa,'invariants',summa//counts,'distribution',sorted(cc.items()),'reps',rep,'byord',byord,flush=True)
assert counts==20160
assert character(list(range(16)))==77
assert summa%counts==0

# Independent signed oriented-chain trace on one representative of each (order, character) type.
def oriented_chain_trace(p):
    answer=-1  # augmented empty face
    for m in range(1,1<<15):
        if not good[m]:continue
        els=[x for x in vs if m>>(x-1)&1]
        mapped=[p[x] for x in els]
        if set(mapped)!=set(els):continue
        parity=sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))%2
        answer += (-1 if len(els)%2==0 else 1)*(-1 if parity else 1)
    return answer
for key,cols in rep.items():
 a,b,c,d=cols
 perm=[(a if i&1 else 0)^(b if i&2 else 0)^(c if i&4 else 0)^(d if i&8 else 0) for i in range(16)]
 assert oriented_chain_trace(perm)==key[1], (key,oriented_chain_trace(perm))
print('DIRECT_CHAIN_TRACES_OK',len(rep),'representatives',flush=True)
print('CAP_GL4_CHARACTER_PASS',flush=True)
