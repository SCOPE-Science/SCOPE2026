"""Standalone exact certificate for a 25-vertex simplicial complex and its affine symmetries.
Requires only Python 3.9+; no external dependencies.
"""
from collections import Counter,deque
from functools import lru_cache

MOD=5
N=MOD*MOD
VERTICES=[(i,j) for i in range(MOD) for j in range(MOD)]
ADJ=[0]*N
for x,(a,b) in enumerate(VERTICES):
    for y,(c,d) in enumerate(VERTICES):
        if (a-c)%MOD in (1,MOD-1) and (b-d)%MOD in (1,MOD-1):
            ADJ[x]|=1<<y
assert all(z.bit_count()==4 for z in ADJ)

faces=[]
def list_faces(free,face):
    faces.append(face)
    while free:
        bit=free&-free;free-=bit
        vertex=bit.bit_length()-1
        list_faces(free&~ADJ[vertex],face|bit)
list_faces((1<<N)-1,0)
faces=sorted(faces,key=lambda f:(f.bit_count(),f))
assert len(faces)==25531
face_set=set(faces)
assert len(face_set)==len(faces)
count=Counter(f.bit_count()-1 for f in faces)
assert count=={-1:1,0:25,1:250,2:1300,3:3850,4:6745,5:7100,6:4450,7:1550,8:250,9:10}

# A fixed vertex-priority acyclic matching on the augmented face poset.
ORDER=[5,12,18,6,3,14,24,2,15,11,1,9,0,22,16,20,17,23,7,4,8,10,13,19,21]
remain=set(faces)
paired={}
for v in ORDER:
    bit=1<<v
    for f in list(remain):
        if f&bit:continue
        upper=f|bit
        if upper in remain:
            remain.remove(f);remain.remove(upper)
            paired[f]=upper
            paired[upper]=f
assert len(remain)==9
assert all(f.bit_count()==5 for f in remain)
assert len(paired)==len(faces)-9

# Exact directed Hasse diagram. Nonmatching edges are downward; matching edges upward.
faces_idx={f:i for i,f in enumerate(faces)}
indeg=[0]*len(faces)
out=[[] for _ in faces]
cover_count=0
for top in faces:
    sub=top
    while sub:
        bit=sub&-sub;sub-=bit
        bottom=top^bit
        if paired.get(bottom)==top:
            u=faces_idx[bottom];v=faces_idx[top]
        else:
            u=faces_idx[top];v=faces_idx[bottom]
        out[u].append(v)
        indeg[v]+=1
        cover_count+=1
queue=deque(i for i in range(len(faces)) if indeg[i]==0)
visited=0
while queue:
    u=queue.popleft();visited+=1
    for v in out[u]:
        indeg[v]-=1
        if indeg[v]==0:queue.append(v)
assert visited==len(faces),f'Matching has cycle: {len(faces)-visited}'

# The original-metric radius-three 5-by-5 torus Rips complex has exactly
# the above forbidden graph: maximum graph distance four occurs at (±2,±2).
# Multiplying each coordinate by 3 turns (±2,±2) into (±1,±1).

def orbit_char(s,t,a,b,swap):
    # s,t in {1,-1}, a,b in F5; swap before applying coordinate signs/translations.
    perm=[]
    for x,y in VERTICES:
        if swap:x,y=y,x
        perm.append(((s*x+a)%5)*5+((t*y+b)%5))
    assert len(set(perm))==25
    seen=set();cycs=[]
    for z in range(N):
        if z in seen:continue
        c=[];w=z
        while w not in seen:
            c.append(w);seen.add(w);w=perm[w]
        assert w==z
        cycs.append(c)
    allowed=[]
    for cycle in cycs:
        if all(not (ADJ[x]&(1<<y)) for x in cycle for y in cycle):
            allowed.append(cycle)
    k=len(allowed)
    conflict=[0]*k
    for i,A in enumerate(allowed):
        for j,B in enumerate(allowed):
            if i==j or any(ADJ[x]&(1<<y) for x in A for y in B):
                conflict[i]|=1<<j
    @lru_cache(None)
    def independent_sum(mask):
        if mask==0:return 1
        pivot=mask&-mask;idx=pivot.bit_length()-1
        return independent_sum(mask^pivot)-independent_sum(mask&~conflict[idx])
    # Signed reduced Lefschetz = -independence polynomial at -1
    # (a union of r vertex-permutation cycles contributes (-1)^(r-1)).
    return -independent_sum((1<<k)-1)

def predicted(s,t,a,b,swap):
    # Four-dimensional rational augmentation representations on each coset set A/L_±.
    # For each preserved coset family: fixed cosets minus 1; swapped families: trace 0.
    # The 1-d line is the sign of coordinate-factor interchange.
    sign=-1 if swap else 1
    # Determine linear map on displacement vectors from affine transformation.
    def linear(x,y):
        if swap:x,y=y,x
        return ((s*x)%5,(t*y)%5)
    for slope in (2,3):
        generator=(1,slope)
        new=linear(*generator)
        new_slope=(new[1]*pow(new[0],-1,5))%5
        if new_slope!=slope:continue
        # A coset class of L_slope represented by q=y-slope*x mod5.
        # On coset labels: q -> linear_const*q + shift.
        p0=linear(0,0)
        p1=linear(0,1)
        coef=(p1[1]-slope*p1[0]-p0[1]+slope*p0[0])%5
        shift=(b-slope*a)%5
        fixed=sum((coef*q+shift)%5==q for q in range(5))
        sign+=fixed-1
    return sign

hist=Counter()
for swap in (False,True):
    for s in (-1,1):
        for t in (-1,1):
            for a in range(5):
                for b in range(5):
                    actual=orbit_char(s,t,a,b,swap)
                    expected=predicted(s,t,a,b,swap)
                    assert actual==expected,(swap,s,t,a,b,actual,expected)
                    hist[actual]+=1
assert hist=={9:1,4:8,1:75,-1:116},hist
assert sum(trace*mult for trace,mult in hist.items())==0
print('faces:',len(faces))
print('face sizes (-1 through 9):',tuple(count[j] for j in range(-1,10)))
print('Hasse covers:',cover_count)
print('Morse pairs:',len(paired)//2)
print('critical faces:',len(remain),'all dimension 4')
print('DAG vertices topologically sorted:',visited)
print('symmetries and predicted characters checked:',200)
print('character value multiplicities:',sorted(hist.items()))
print('fixed rational top homology dimension:',sum(k*v for k,v in hist.items())//200)
print('PASS')
