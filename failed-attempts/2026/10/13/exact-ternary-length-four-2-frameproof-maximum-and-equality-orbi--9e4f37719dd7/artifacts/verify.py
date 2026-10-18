from itertools import product
from collections import Counter, deque
from hashlib import sha256

WORDS=list(product(range(3), repeat=4))
INDEX={w:i for i,w in enumerate(WORDS)}
N=len(WORDS)

def separates(a,b,c):
    for z,x,y in ((a,b,c),(b,a,c),(c,a,b)):
        if not any(z[r]!=x[r] and z[r]!=y[r] for r in range(4)):
            return False
    return True

def valid_code(C):
    for i in range(len(C)):
        for j in range(i+1,len(C)):
            for k in range(j+1,len(C)):
                if not separates(WORDS[C[i]],WORDS[C[j]],WORDS[C[k]]):
                    return False
    return True

# For increasing indices i<j<k, allowed[i][j] is a bitset of legal k.
allowed=[[0]*N for _ in range(N)]
bad=0
for i in range(N):
    for j in range(i+1,N):
        m=0
        for k in range(j+1,N):
            if separates(WORDS[i],WORDS[j],WORDS[k]):
                m |= 1<<k
            else:
                bad += 1
        allowed[i][j]=m

def enumerate_normalized(target, collect=False):
    count=0; nodes=0; out=[]
    def rec(chosen,cand):
        nonlocal count,nodes
        nodes += 1
        if len(chosen)==target:
            count += 1
            if collect: out.append(tuple(chosen))
            return
        need=target-len(chosen)
        while cand:
            if cand.bit_count()<need: return
            lsb=cand & -cand
            v=lsb.bit_length()-1
            cand ^= lsb
            nc=cand
            for u in chosen:
                nc &= allowed[u][v]
            rec(chosen+[v],nc)
    rec([0], ((1<<N)-1)^1)
    return count,nodes,out

c13,n13,_=enumerate_normalized(13,False)
if c13!=0: raise SystemExit('size-13 code exists')
c12,n12,norm=enumerate_normalized(12,True)
if c12!=832: raise SystemExit(('normalized count',c12))

# Coordinatewise translations act transitively on the 81 words. Translating
# normalized maxima reconstructs every labeled maximum.
allmax=set()
for C in norm:
    for t in WORDS:
        D=tuple(sorted(INDEX[tuple((WORDS[v][r]+t[r])%3 for r in range(4))] for v in C))
        allmax.add(D)
if len(allmax)!=5616: raise SystemExit(('labeled count',len(allmax)))
if c12*81 != len(allmax)*12: raise SystemExit('incidence double count failed')
if not all(valid_code(C) for C in allmax): raise SystemExit('invalid maximum')

# Generators of (S_3)^4 semidirect S_4: adjacent coordinate swaps and
# adjacent symbol transpositions in each coordinate.
gens=[]
for a,b in ((0,1),(1,2),(2,3)):
    mp=[]
    for w in WORDS:
        x=list(w); x[a],x[b]=x[b],x[a]; mp.append(INDEX[tuple(x)])
    gens.append(mp)
for r in range(4):
    for a,b in ((0,1),(1,2)):
        mp=[]
        for w in WORDS:
            x=list(w)
            if x[r]==a: x[r]=b
            elif x[r]==b: x[r]=a
            mp.append(INDEX[tuple(x)])
        gens.append(mp)

unseen=set(allmax); orbit_sizes=[]; reps=[]
while unseen:
    seed=min(unseen); q=deque([seed]); seen={seed}
    while q:
        C=q.popleft()
        for mp in gens:
            D=tuple(sorted(mp[v] for v in C))
            if D not in seen:
                if D not in allmax: raise SystemExit('symmetry left census')
                seen.add(D); q.append(D)
    unseen -= seen
    orbit_sizes.append(len(seen)); reps.append(seed)
order=(6**4)*24
pairs=sorted((s,order//s,r) for s,r in zip(orbit_sizes,reps))
if [x[0] for x in pairs]!=[432,5184]: raise SystemExit(('orbits',pairs))
if [x[1] for x in pairs]!=[72,6]: raise SystemExit(('stabilizers',pairs))

profiles=[]
for s,stab,C in pairs:
    coord=sorted(tuple(sorted(Counter(WORDS[v][r] for v in C).values(), reverse=True)) for r in range(4))
    dist=Counter(sum(a!=b for a,b in zip(WORDS[C[i]],WORDS[C[j]])) for i in range(12) for j in range(i+1,12))
    profiles.append((s,coord,tuple(sorted(dist.items()))))
expected=[
 (432,[(4,4,4)]*4,((2,18),(3,36),(4,12))),
 (5184,[(4,4,4),(5,4,3),(5,4,3),(5,4,3)],((2,21),(3,33),(4,12)))
]
if profiles!=expected: raise SystemExit(('profiles',profiles))

def fmt(C): return ','.join(''.join(map(str,WORDS[v])) for v in C)
blob='\n'.join(','.join(map(str,C)) for C in sorted(allmax)).encode()
digest=sha256(blob).hexdigest()
print('VERIFY_OK maximum=12 normalized_maxima=832 labeled_maxima=5616 size13=0 natural_group=31104 orbits=2 orbit_sizes=432,5184 stabilizers=72,6 bad_triples=%d nodes12=%d nodes13=%d census_sha256=%s' % (bad,n12,n13,digest))
for s,stab,C in pairs:
    print('REP orbit=%d stabilizer=%d %s' % (s,stab,fmt(C)))
