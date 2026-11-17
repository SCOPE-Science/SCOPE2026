# Auxiliary derivation of compact explicit Rule 30 witnesses from the transfer graph.
from collections import defaultdict

def nextpair(s,p):
 m=(1<<p)-1;b=s>>p;c=s&m
 return ((((b>>1)|((b&1)<<(p-1)))^(b|c))<<p)|b

def rule30(v):
 n=len(v);return ''.join(str(int(v[(i-1)%n])^(int(v[i])|int(v[(i+1)%n]))) for i in range(n))

def tperiod(v):
 w=rule30(v)
 for t in range(1,13):
  if w==v:return t
  w=rule30(w)
 raise Exception('unbounded')
for p,min_states in [(6,[121]),(12,[131029,98193,24561])]:
 for st in min_states:
  cyc=[st];k=nextpair(st,p)
  while k!=st:
   cyc.append(k);k=nextpair(k,p)
  n=len(cyc)
  v=''.join(str((cyc[(-j)%n]>>p)&1) for j in range(n))
  print('time_height',p,'spatial_length',n,'bit_string',v,'temporal_least',tperiod(v))
