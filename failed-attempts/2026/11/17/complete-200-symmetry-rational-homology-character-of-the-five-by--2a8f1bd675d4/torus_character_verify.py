"""Exact equivariant Euler-trace certificate for the 5x5 toroidal hard-square complex.
No external packages required. The graph and group are defined from first principles.
"""
from itertools import product
from collections import Counter
import json

P=5
V=[(a,b) for a in range(P) for b in range(P)]
IDX={v:i for i,v in enumerate(V)}
ADJ=[0]*25
for i,(a,b) in enumerate(V):
    for c,d in (((a+1)%P,b),((a-1)%P,b),(a,(b+1)%P),(a,(b-1)%P)):
        ADJ[i]|=1<<IDX[(c,d)]

# Independently enumerate independent subsets for identity trace and face counts.
FACES=[]
def expand(remaining, selected):
    if remaining==0:
        FACES.append(selected)
        return
    bit=remaining&-remaining
    i=bit.bit_length()-1
    expand(remaining^bit,selected)
    expand((remaining^bit)&~ADJ[i],selected|bit)
expand((1<<25)-1,0)
assert len(FACES)==25531
assert [sum(f.bit_count()==j for f in FACES) for j in range(11)]==[1,25,250,1300,3850,6745,7100,4450,1550,250,10]

def permutation(g):
    sw,sx,sy,tx,ty=g
    result=[]
    for x,y in V:
        a,b=(y,x) if sw else (x,y)
        result.append(IDX[((sx*a+tx)%P,(sy*b+ty)%P)])
    return result

def orbit_trace(perm):
    """Reduced Lefschetz via the independent-set polynomial of vertex orbit graph at -1."""
    assert sorted(perm)==list(range(25))
    seen=set();good=[]
    for v in range(25):
        if v in seen:continue
        orbit=[];w=v
        while w not in seen:
            seen.add(w);orbit.append(w);w=perm[w]
        mask=sum(1<<u for u in orbit)
        if any(ADJ[u]&mask for u in orbit):continue
        good.append(mask)
    n=len(good)
    conflicts=[0]*n
    for i,mask in enumerate(good):
        neighbor_mask=0
        for u in range(25):
            if mask>>u&1:neighbor_mask|=ADJ[u]
        for j in range(n):
            if i!=j and neighbor_mask&good[j]:conflicts[i]|=1<<j
    # The alternating sum includes the empty orbit subset. Trace is minus that sum.
    def independent_sum(avail):
        if not avail:return 1
        bit=avail&-avail
        i=bit.bit_length()-1
        return independent_sum(avail^bit)-independent_sum((avail^bit)&~conflicts[i])
    return -independent_sum((1<<n)-1)

rows=[];distinct=set();hist=Counter()
for sw,sx,sy,tx,ty in product(range(2),(1,-1),(1,-1),range(5),range(5)):
    g=(sw,sx,sy,tx,ty)
    p=permutation(g)
    t=orbit_trace(p)
    distinct.add(tuple(p));rows.append({'g':list(g),'trace':t});hist[t]+=1
assert len(rows)==len(distinct)==200
assert hist==Counter({-1:116,1:75,4:8,9:1}),hist
assert sum(r['trace'] for r in rows)==0
trans=[r for r in rows if r['g'][:3]==[0,1,1]]
assert len(trans)==25 and Counter(r['trace'] for r in trans)==Counter({-1:16,4:8,9:1})
assert sum(r['trace'] for r in trans)==25
# Explicit signed-simplex trace independently at 3 chosen nontrivial symmetry elements.
lookup={tuple(r['g']):r['trace'] for r in rows}
def simplex_trace(g):
    perm=permutation(g)
    ans=-1
    for f in FACES:
        if not f:continue
        vs=[i for i in range(25) if f>>i&1]
        image=[perm[i] for i in vs]
        if set(vs)!=set(image):continue
        inversions=sum(image[i]>image[j] for i in range(len(image)) for j in range(i+1,len(image)))
        ans+=(-1)**(len(vs)-1+inversions)
    return ans
for g in [(0,1,1,0,0),(0,1,1,1,0),(1,-1,1,0,0),(0,-1,-1,2,3)]:
    assert simplex_trace(g)==lookup[g],(g,simplex_trace(g),lookup[g])
with open('torus_character_data.json','w',encoding='utf8') as f:
    json.dump({'graph':'C5 Cartesian C5','group_size':200,'f_vector':[sum(f.bit_count()==i for f in FACES) for i in range(11)], 'histogram':dict(sorted(hist.items())),'invariant_dimension':0,'translation_invariant_dimension':1,'trace_rows':rows},f,separators=(',',':'),ensure_ascii=False)
print('TORUS_5X5_200_SYMMETRY_TRACES_PASS')
print('augmented_faces=25531 distinct_group_elements=200')
print('histogram='+json.dumps(dict(sorted(hist.items()))))
print('full_invariants=0 translation_invariants=1')
print('independent_signed_simplex_crosschecks=4')
