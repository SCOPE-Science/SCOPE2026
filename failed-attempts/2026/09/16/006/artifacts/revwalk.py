import itertools, random
from flipsearch import stacked_chain, faceset_of, find_moves, apply_rev, check_valid, strand_of_facets
from math import comb
def C(n,r):
    return comb(n,r) if 0<=r<=n else 0
def formula(d,k,i):
    return (k-2)*C(d*(k-1),i+1)-(k-1)*C(d*(k-2),i+1)+d*(k-1)*C(d*(k-2),i-1)

def excess(beta,d,k):
    return [b-formula(d,k,i) for i,b in enumerate(beta)]

random.seed(1)
d=4; t=2; k=t+1
facets,colors,n=stacked_chain(d,t)
faces=faceset_of(facets)
print('start strand:',strand_of_facets(facets,n))
# greedy walk: random reverse moves, up to 40 accepted (validity-checked), track max excess
cur=facets; curfaces=faces
best=0; hist=[]
for step in range(40):
    fwd,rev=find_moves(cur,curfaces)
    random.shuffle(rev)
    moved=False
    for (B,A) in rev:
        new=apply_rev(cur,B,A)
        ok,msg=check_valid(new,d,colors)
        if ok:
            cur=new; curfaces=faceset_of(cur); moved=True
            break
    if not moved:
        print('stuck at',step); break
    beta=strand_of_facets(cur,n)
    ex=excess(beta,d,k)
    mx=max(ex); hist.append((step,mx,beta))
    if mx>best:
        best=mx
        print('STEP',step,'excess',ex,'strand',beta)
print('best excess:',best)
for h in hist: print(h[0],h[1])
