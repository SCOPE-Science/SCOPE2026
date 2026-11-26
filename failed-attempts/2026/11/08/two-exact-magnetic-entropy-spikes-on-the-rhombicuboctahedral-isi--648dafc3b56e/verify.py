import itertools,collections,json
S=list(itertools.product([-1,1],repeat=3));P=range(3)
V=[(s,p) for s in S for p in P];ind={v:i for i,v in enumerate(V)}
E=[];Et=[];Eo=[]
for v,(s,p) in enumerate(V):
 for w,(t,q) in enumerate(V):
  if v>=w:continue
  triangle=(s==t and p!=q)
  ext=(p==q and s[p]==t[p] and sum(s[z]!=t[z] for z in P)==1)
  if triangle or ext:E.append((v,w))
  if triangle:Et.append((v,w))
  if ext:Eo.append((v,w))
assert len(E)==48 and len(Et)==24 and len(Eo)==24
# Combinatorial enumerator field 4 (each triangle zero or one minority)
pol4=collections.Counter()
for choices in itertools.product(range(4),repeat=8):
 down={3*i+c-1 for i,c in enumerate(choices) if c}
 if not any(x in down and y in down for x,y in Eo):pol4[len(down)]+=1
print('F4',dict(sorted(pol4.items())))
# Field 2: exactly one or two down in each triangle, no intertriangle down edge
pol2=collections.Counter()
opts=[t for r in (1,2) for t in itertools.combinations(range(3),r)]
for choices in itertools.product(range(6),repeat=8):
 down={3*i+j for i,c in enumerate(choices) for j in opts[c]}
 if not any(x in down and y in down for x,y in Eo):pol2[len(down)]+=1
print('F2',dict(sorted(pol2.items())))
# h0: each non-triangular edge antialigned. six independent ext 4-cycle components
zero=collections.Counter()
for ts in itertools.product([-1,1],repeat=6):
 spin={(s,p): (s[0]*s[1]*s[2])*ts[2*p+(s[p]>0)] for s in S for p in P}
 if all(len({spin[(s,p)] for p in P})>1 for s in S):
  zero[sum(v==-1 for v in spin.values())]+=1
print('F0',dict(sorted(zero.items())))
assert list(sorted(pol4.items()))==list(enumerate([1,24,228,1104,2940,4368,3536,1440,234]))
assert dict(pol2)=={8:234,9:552,10:444,11:144,12:18}
assert dict(zero)=={12:18}
print('All constrained structural enumerations: PASS')
