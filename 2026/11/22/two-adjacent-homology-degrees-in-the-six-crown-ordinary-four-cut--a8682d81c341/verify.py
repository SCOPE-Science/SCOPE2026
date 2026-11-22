"""Standalone exact elementary cellular/Morse verification for four-cut dual of crown six."""
from itertools import combinations
from functools import lru_cache
from collections import Counter, deque

N=12
ORDER=[3,2,4,7,1,11,9,0,5,6,10,8]

def forbidden_quads():
    bad=set()
    for ids in combinations(range(N),4):
        ls=[i for i in ids if i<6]; rs=[i-6 for i in ids if i>=6]
        if not ls or not rs:
            bad.add(sum(1<<i for i in ids)); continue
        reached={ls[0]};todo=[ls[0]]
        while todo:
            x=todo.pop()
            adj=[6+j for j in rs if j!=x] if x<6 else [i for i in ls if i!=x-6]
            for y in adj:
                if y not in reached: reached.add(y);todo.append(y)
        if len(reached)!=4:bad.add(sum(1<<i for i in ids))
    return bad

BAD=forbidden_quads()
FACES={m for m in range(1,1<<N) if all((m&b)!=b for b in BAD)}
assert len(BAD)==165
assert Counter(x.bit_count()-1 for x in FACES)=={0:12,1:66,2:220,3:330,4:120,5:20}

def boundary(s):
    vs=[i for i in range(N) if s>>i&1]
    return [(s^(1<<i),(-1)**k) for k,i in enumerate(vs)]

UN=set(FACES); PAIRS=[]
for v in ORDER:
    for x in sorted(list(UN),key=lambda x:(x.bit_count(),x)):
        if x>>v&1:continue
        y=x|(1<<v)
        if y in UN:
            UN.remove(x);UN.remove(y);PAIRS.append((x,y))
CRITICAL=UN
assert Counter(x.bit_count()-1 for x in CRITICAL)=={0:1,3:66,4:1}
# Exact directed-Hasse acyclicity: match-reversed up-arcs, all other down-arcs.
matched={(lo,up) for lo,up in PAIRS}
out={s:[] for s in FACES}
indeg={s:0 for s in FACES}
for s in FACES:
    for t,c in boundary(s):
        if t not in FACES:continue
        a,b=(t,s) if (t,s) in matched else (s,t)
        out[a].append(b)
        indeg[b]+=1
Q=deque(x for x in FACES if not indeg[x]); seen=0
while Q:
    a=Q.popleft();seen+=1
    for b in out[a]:
        indeg[b]-=1
        if indeg[b]==0:Q.append(b)
assert seen==len(FACES), ('cyclic matching',seen,len(FACES))
edge_count=sum(map(len,out.values()))

pair_3_to_4={lo:up for lo,up in PAIRS if lo.bit_count()==4}
crit3=set(x for x in CRITICAL if x.bit_count()==4)
crit4=next(x for x in CRITICAL if x.bit_count()==5)

@lru_cache(None)
def reduced_3_face(t):
    if t in crit3:return {t:1}
    if t not in pair_3_to_4:return {}   # upper 3-cell matched with 2-cell
    u=pair_3_to_4[t]
    coeff=dict(boundary(u))[t]
    out={}
    for face,c in boundary(u):
        if face==t:continue
        for z,v in reduced_3_face(face).items():
            out[z]=out.get(z,0)-c*coeff*v
    return {z:v for z,v in out.items() if v}

co={}
for t,c in boundary(crit4):
    for z,v in reduced_3_face(t).items():
        co[z]=co.get(z,0)+c*v
co={z:v for z,v in co.items() if v}
assert co=={},co
# Independent mod-2 boundary-rank sanity check (not a substitute for the integral Morse proof).
def rank_mod2(rows):
    pivots={}
    for x in rows:
        while x:
            p=x.bit_length()-1
            if p not in pivots:
                pivots[p]=x
                break
            x^=pivots[p]
    return len(pivots)

by_dim={j:sorted(s for s in FACES if s.bit_count()==j+1) for j in range(6)}
mod2_ranks=[]
for dim in range(1,6):
    lower={s:j for j,s in enumerate(by_dim[dim-1])}
    vectors=[]
    for face in by_dim[dim]:
        vec=0
        for sub,_ in boundary(face):vec^=(1<<lower[sub])
        vectors.append(vec)
    mod2_ranks.append(rank_mod2(vectors))
assert mod2_ranks==[11,55,165,99,20],mod2_ranks
# Moreover complete chain homotopy type follows from critical cells and zero Morse boundary.
print('forbidden_quadruples',len(BAD))
print('face_vector',[sum(x.bit_count()==i for x in FACES) for i in range(1,7)])
print('matched_pairs',len(PAIRS),'critical_dimensions',dict(Counter(x.bit_count()-1 for x in CRITICAL)))
print('gradient_dag',len(FACES),'nodes',edge_count,'edges')
print('morse_boundary_4_to_3_nonzeros',len(co))
print('dual_homotopy_type', 'S4 wedge 66 S3')

print('boundary_ranks_mod2',mod2_ranks)
