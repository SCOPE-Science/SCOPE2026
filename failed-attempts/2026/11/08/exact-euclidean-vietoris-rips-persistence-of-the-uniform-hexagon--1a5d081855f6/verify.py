"""Independent exact combinatorial checks for the uniform hexagonal antiprism.
Run: python verify.py, from the directory containing collapse_certificate.json.
Only Python's standard library is needed.
"""
import collections
import itertools
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parent
CERT=json.loads((ROOT/'collapse_certificate.json').read_text(encoding='utf-8'))
SHELLS=('1','1+s3','3','4','1+2s3')
N=12

def dist2(u,v):
    assert 0<=u<v<N
    a,b=u%6,v%6
    if (u<6)==(v<6):
        d=min((a-b)%6,(b-a)%6)
        return {1:'1',2:'3',3:'4'}[d]
    d=(a-b)%6 if u<6 else (b-a)%6
    return {0:'1',1:'1',2:'1+s3',5:'1+s3',3:'1+2s3',4:'1+2s3'}[d]

DS={e:dist2(*e) for e in itertools.combinations(range(N),2)}
assert collections.Counter(DS.values())==collections.Counter({'1':24,'1+s3':12,'3':12,'4':6,'1+2s3':12})
# Independent Euclidean numerical check: radius 1, half-height^2 = (sqrt(3)-1)/4.
h=math.sqrt(math.sqrt(3)-1)
P=[]
for j in range(N):
    angle=(j%6)*math.pi/3+(math.pi/6 if j>=6 else 0)
    P.append((math.cos(angle),math.sin(angle),-h/2 if j>=6 else h/2))
VALUES={'1':1.,'1+s3':1+math.sqrt(3),'3':3.,'4':4.,'1+2s3':1+2*math.sqrt(3)}
for (u,v),code in DS.items():
    calculated=sum((a-b)**2 for a,b in zip(P[u],P[v]))
    assert abs(calculated-VALUES[code])<1.e-12,(u,v,calculated,code)

def mask(face):
    assert len(set(face))==len(face) and all(0<=i<N for i in face)
    return sum(1<<i for i in face)

def simplex_set(stage):
    assert 1<=stage<=5
    allowed=set(SHELLS[:stage]);F=set()
    for b in range(1,1<<N):
        vertices=[i for i in range(N) if b>>i&1]
        if all(DS[(i,j)] in allowed for i,j in itertools.combinations(vertices,2)):
            F.add(b)
    return F

def facevector(F):
    c=collections.Counter(b.bit_count()-1 for b in F)
    return [c[d] for d in range(max(c)+1)]

def f2rank(vectors):
    piv={}
    for x in vectors:
        while x:
            j=x.bit_length()-1
            if j not in piv:
                piv[j]=x;break
            x^=piv[j]
    return len(piv)

def bettis(F):
    graded={d:sorted(f for f in F if f.bit_count()==d+1) for d in range(12)}
    ranks={}
    for d in range(1,12):
        if not graded[d]:continue
        index={b:i for i,b in enumerate(graded[d-1])}
        cols=[]
        for f in graded[d]:
            faces=(f^(1<<i) for i in range(N) if f>>i&1)
            cols.append(sum(1<<index[s] for s in faces))
        ranks[d]=f2rank(cols)
    return [len(graded[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(12)]

EXPECTED_F={1:[12,24,12],2:[12,36,36,12],3:[12,48,76,48,12],4:[12,54,112,105,36,2]}
EXPECTED_B={1:[1,1],2:[1,1],3:[1,0,3],4:[1,0,0,2],5:[1]}
for stage in range(1,6):
    F=simplex_set(stage)
    if stage<5: assert facevector(F)==EXPECTED_F[stage],(stage,facevector(F))
    if stage==5: assert len(F)==(1<<N)-1
    b=bettis(F)
    assert b[:len(EXPECTED_B[stage])]==EXPECTED_B[stage] and all(x==0 for x in b[len(EXPECTED_B[stage]):])
    print('stage',stage,'facevector',facevector(F),'mod2_betti',b[:max(4,len(EXPECTED_B[stage]))])
    if stage<=3:
        rows=CERT['stages'][str(stage)]; Pairs=rows['pairs']
        assert len(Pairs)=={1:18,2:43,3:65}[stage]
        for alpha,beta in Pairs:
            a,z=mask(alpha),mask(beta)
            assert a in F and z in F and a&z==a and z.bit_count()==a.bit_count()+1
            cofaces=[q for q in F if q.bit_count()==a.bit_count()+1 and q&a==a]
            assert cofaces==[z],(stage,alpha,beta)
            F.remove(a);F.remove(z)
        assert F=={mask(x) for x in rows['remaining']}
        assert facevector(F)=={1:[6,6],2:[5,5],3:[12,31,23]}[stage]
        print('verified_free_pairs',len(Pairs),'remainder',facevector(F))

# At stage 2 the integer angular cochain gives an integral winding number.
F2=simplex_set(2)
ANGLE={v:2*(v%6)+(1 if v>=6 else 0) for v in range(N)}
def angular_delta(u,v):
    x=(ANGLE[v]-ANGLE[u])%12
    return x if x<=6 else x-12
for t in (f for f in F2 if f.bit_count()==3):
    i,j,k=[v for v in range(N) if t>>v&1]
    assert angular_delta(i,j)+angular_delta(j,k)+angular_delta(k,i)==0
assert sum(angular_delta(i,(i+1)%6) for i in range(6))==12
print('integral_winding_cochain','closed_on_all_triangles','upper_cycle_value',1)

# Each new same-layer chord at stage 3 is homotopic, via an added triangle,
# to two already present consecutive same-layer edges.
for upper in (False,True):
    offset=0 if upper else 6
    for i in range(6):
        x=offset+i;y=offset+(i+1)%6;z=offset+(i+2)%6
        assert mask([x,y,z]) in simplex_set(3)
# The upper 6-gon is bounded by an explicit 2-chain in stage 3.
triangles=[[0,1,2],[0,2,4],[2,3,4],[0,4,5]]
edge_parity=collections.Counter()
for tr in triangles:
    assert mask(tr) in simplex_set(3)
    for a,b in itertools.combinations(sorted(tr),2):edge_parity[(a,b)]+=1
assert {e for e,c in edge_parity.items() if c%2}=={tuple(sorted((i,(i+1)%6))) for i in range(6)}
print('stage3','upper_boundary_filling_4_triangles','verified')

# The forbidden pairs just below the diameter constitute one twelve-cycle.
missing={e for e,value in DS.items() if value=='1+2s3'}
nb={v:set() for v in range(N)}
for i,j in missing:nb[i].add(j);nb[j].add(i)
assert all(len(x)==2 for x in nb.values())
seen={0};todo=[0]
while todo:
    v=todo.pop()
    for w in nb[v]:
        if w not in seen:seen.add(w);todo.append(w)
assert len(seen)==12 and len(missing)==12
print('penultimate_forbidden_graph','one_C12','verified')
print('VERIFY_OK')
