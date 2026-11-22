"""Exact certificate for rational tangent incompatibility of smooth binary cubic-quartic sections.
Run: python3 verify_tangent_rigidity.py. Requires SymPy for geometric Jacobian checks.
"""
import itertools
from collections import Counter
import sympy as S

EXPS=[m for m in itertools.product(range(5),repeat=4) if sum(m)==4]
IX={m:i for i,m in enumerate(EXPS)}

def monom(t):return 1<<IX[tuple(t)]
def cubic_times(terms,k):
    v=0
    for m in terms:
        a=list(m);a[k]+=1;v^=monom(a)
    return v

def echelon(vec):
    b={}
    for v in vec:
        while v:
            i=v.bit_length()-1
            if i not in b:b[i]=v;break
            v^=b[i]
    return list(b.values())

def pair(i,j):
    a=[0]*4;a[i]=2;a[j]=1
    b=[0]*4;b[i]=1;b[j]=2
    return (tuple(a),tuple(b))

G_TERMS=pair(0,1)+pair(2,3)
J4=[cubic_times(pair(i,j),k) for i,j in itertools.combinations(range(4),2) for k in range(4)]
G4=[cubic_times(G_TERMS,k) for k in range(4)]
assert len(echelon(J4))==20 and len(echelon(G4))==4
base=echelon(G4)
for v in echelon(J4):
    if len(echelon(base+[v]))>len(base):base.append(v)
assert len(base)==20
QUOT=base[4:]

# A class mask uniquely describes a quartic modulo G times a linear form.
def polynomial(mask):
    p=0
    for i in range(16):
        if mask>>i&1:p^=QUOT[i]
    return p

def gradient(P,v):
    out=0
    for j,m in enumerate(EXPS):
        if not(P>>j&1):continue
        for k in range(4):
            if m[k]%2 and all(not e or v>>i&1 for i,e in enumerate(m) if i!=k) and (m[k]==1 or v>>k&1):out^=1<<k
    return out

def grad_G(p):
    return ((p>>1)&1) | (((p>>0)&1)<<1) | (((p>>3)&1)<<2) | (((p>>2)&1)<<3)

PTS=tuple(range(1,16))
GRAD=[[gradient(a,p) for p in PTS] for a in QUOT]
all_smooth_at_F2=[];current=[0]*15;prev=0
for t in range(1<<16):
    c=t^(t>>1);switch=c^prev
    if switch:
        j=switch.bit_length()-1
        for k in range(15):current[k]^=GRAD[j][k]
    prev=c
    if all(current[k] not in (0,grad_G(p)) for k,p in enumerate(PTS)):
        all_smooth_at_F2.append(c)
assert len(all_smooth_at_F2)==288
U=set(all_smooth_at_F2)

# Normal forms under the 15 symplectic transvections.
R={}
for j,v in enumerate(base):
    z=v;c=1<<j
    while z:
        n=z.bit_length()-1
        if n not in R:R[n]=(z,c);break
        a,b=R[n];z^=a;c^=b
assert len(R)==20

def coordinates(p):
    z=p;mask=0
    while z:
        a,b=R[z.bit_length()-1];z^=a;mask^=b
    return mask>>4

def form(x,y):return ((x&1)*((y>>1)&1)) ^ (((x>>1)&1)*(y&1)) ^ (((x>>2)&1)*((y>>3)&1)) ^ (((x>>3)&1)*((y>>2)&1))

def poly_mul(a,b):
    out=set()
    for x in a:
        for y in b:
            z=tuple(i+j for i,j in zip(x,y))
            if z in out:out.remove(z)
            else:out.add(z)
    return out

def change(poly,v):
    rows=[]
    for i in range(4):
        row=1<<i
        if v>>i&1:
            for j in range(4):
                if form(v,1<<j):row^=1<<j
        rows.append({tuple(int(j==k) for j in range(4)) for k in range(4) if row>>k&1})
    res=0
    for j,m in enumerate(EXPS):
        if not(poly>>j&1):continue
        q={(0,0,0,0)}
        for k,a in enumerate(m):
            for _ in range(a):q=poly_mul(q,rows[k])
        for z in q:res^=monom(z)
    return res

TRANS=[[coordinates(change(v,a)) for v in QUOT] for a in PTS]
def act(mask,columns):
    z=0
    for k in range(16):
        if mask>>k&1:z^=columns[k]
    return z

ORBS=[]
while U:
    a=min(U);orb={a};queue=[a]
    for x in queue:
        for T in TRANS:
            y=act(x,T)
            assert y in all_smooth_at_F2
            if y not in orb:orb.add(y);queue.append(y)
    ORBS.append(orb);U-=orb
assert sorted(len(o) for o in ORBS)==[144,144]

X,Y,Z,W=S.symbols('x y z w');V=(X,Y,Z,W)
def expression(poly):
    return sum(S.prod(V[k]**m[k] for k in range(4)) for j,m in enumerate(EXPS) if poly>>j&1)

g=sum(S.prod(V[k]**a[k] for k in range(4)) for a in G_TERMS)
def geometrically_smooth(mask):
    f=expression(polynomial(mask))
    dg=[S.diff(g,x) for x in V];df=[S.diff(f,x) for x in V]
    jac=[dg[i]*df[j]-dg[j]*df[i] for i in range(4) for j in range(i+1,4)]
    for k in range(4):
        subs={V[k]:1};vars=[x for i,x in enumerate(V) if i!=k]
        gb=S.groebner([h.subs(subs) for h in [g,f]+jac],*vars,modulus=2)
        if list(gb)!=[S.Integer(1)]:return False
    return True

assert geometrically_smooth(27773)
assert not geometrically_smooth(27760)
SMOOTH=next(o for o in ORBS if 27773 in o)
assert 27760 not in SMOOTH

# Each rational tangent is an isotropic line in the fixed symplectic cubic.
LINES=sorted({tuple(sorted((a,b,a^b))) for a in PTS for b in PTS if a!=b and form(a,b)==0})
assert len(LINES)==15

def matching(mask):
    gradp=[gradient(polynomial(mask),p) for p in PTS]
    mt=[]
    for p,d in zip(PTS,gradp):
        g=grad_G(p)
        eligible=[j for j,L in enumerate(LINES) if p in L and all(((d&t).bit_count()%2==0) and ((g&t).bit_count()%2==0) for t in L)]
        assert len(eligible)==1
        mt.append(eligible[0])
    assert len(set(mt))==15
    return tuple(mt)

MT={a:matching(a) for a in SMOOTH}
assert len(set(MT.values()))==144
hist=Counter()
for i,a in enumerate(sorted(SMOOTH)):
    for b in sorted(SMOOTH)[i+1:]:
        d=sum(i==j for i,j in zip(MT[a],MT[b]))
        hist[d]+=1
        assert d>0
        assert a^b not in all_smooth_at_F2
EXPECTED={1:360,2:1440,3:2160,4:720,5:1152,6:1440,7:1440,8:1080,10:504}
assert dict(hist)==EXPECTED and sum(hist.values())==144*143//2
# The entire incidence graph has 288 perfect matchings (not merely those obtained from sections).
OPTIONS={p:[i for i,L in enumerate(LINES) if p in L] for p in PTS}
state={0:1}
for p in PTS:
    nextstate={}
    for used,count in state.items():
        for i in OPTIONS[p]:
            if not used>>i&1:nextstate[used|(1<<i)]=nextstate.get(used|(1<<i),0)+count
    state=nextstate
assert state=={(1<<15)-1:288}
ALLMATCH={a:matching(a) for o in ORBS for a in o}
assert len(set(ALLMATCH.values()))==288
adj={a:set() for a in ALLMATCH}
for i,a in enumerate(sorted(ALLMATCH)):
    for b in sorted(ALLMATCH)[i+1:]:
        if all(x!=y for x,y in zip(ALLMATCH[a],ALLMATCH[b])):
            adj[a].add(b);adj[b].add(a)
assert Counter(len(n) for n in adj.values())==Counter({2:144,4:144})
remaining=set(adj);component_sizes=[]
while remaining:
    u=min(remaining);component={u};queue=[u]
    for x in queue:
        for y in adj[x]:
            if y not in component:component.add(y);queue.append(y)
    remaining-=component;component_sizes.append(len(component))
    good=component&SMOOTH;bad=component-SMOOTH
    assert len(good)==4 and len(bad)==4
    assert all(len(adj[x]&bad)==2 and len(adj[x]&good)==2 for x in bad)
    assert all(len(adj[x]&bad)==2 and len(adj[x]&good)==0 for x in good)
    # The cross-orbit subgraph is a connected 8-cycle; the bad subgraph is a 4-cycle.
    assert all(len(adj[x]&(component-SMOOTH))==2 for x in component)
    crossseen={u};crossqueue=[u]
    for t in crossqueue:
        for w in adj[t]:
            if (t in SMOOTH) != (w in SMOOTH) and w not in crossseen:
                crossseen.add(w);crossqueue.append(w)
    assert crossseen==component
assert len(component_sizes)==36 and set(component_sizes)=={8}
print('TANGENT_RIGIDITY_OK',len(SMOOTH),sum(hist.values()),sorted(hist.items()),'DISJOINT_GRAPH',len(component_sizes),'C8_PLUS_C4')
