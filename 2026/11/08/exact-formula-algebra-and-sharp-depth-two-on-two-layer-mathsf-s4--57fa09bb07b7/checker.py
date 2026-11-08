"""Independent finite checks for the two-layer S4 x S5 modal-profile theorem.
No external dependencies. Run: python3 checker.py
"""
from itertools import product, combinations
from math import comb

def profile_count(k,m):
    q=1<<k
    return sum(s*comb(q*q,s) for s in range(1,min(m,q*q)+1))

def successors(m, modality, w):
    i,j=w
    if modality=='a':
        return [(r,j) for r in range(i,2)]
    return [(i,h) for h in range(m)]

def sem(f,V,w):
    op=f[0]
    if op=='var':return bool(V[w[1]][w[0]] & (1<<f[1]))
    if op=='top':return True
    if op=='not':return not sem(f[1],V,w)
    if op=='and':return sem(f[1],V,w) and sem(f[2],V,w)
    if op=='or':return sem(f[1],V,w) or sem(f[2],V,w)
    if op in ('a','b'):
        return any(sem(f[1],V,t) for t in successors(len(V),op,w))
    if op in ('A','B'):
        return all(sem(f[1],V,t) for t in successors(len(V),op.lower(),w))
    raise AssertionError(op)

def NOT(x):return ('not',x)
def AND(a,b):return ('and',a,b)
def OR(a,b):return ('or',a,b)
def dia(x,s):return (s,x)
def box(x,s):return (s.upper(),x)

def litbit(i,v):return ('var',i) if v else NOT(('var',i))
def bit_type(k,val):
    f=('top',)
    for i in range(k):f=AND(f,litbit(i,(val>>i)&1))
    return f

def up(k,i):
    p=('var',i)
    return OR(AND(p,box(p,'a')),AND(NOT(p),dia(p,'a')))

def paired(k,a,b):
    f=('top',)
    for i in range(k):
        f=AND(f,litbit(i,(a>>i)&1))
        u=up(k,i)
        f=AND(f,u if (b>>i)&1 else NOT(u))
    return f

def observed(V,w):
    row,j=w
    if row==0:
        S=frozenset(V)
        return (V[j],S)
    upper=V[j][1]
    S=frozenset((b,b) for a,b in V)
    return ((upper,upper),S)

def test(k,m):
    q=1<<k
    type_to_points={}
    count=0
    for z in product(range(q*q),repeat=m):
        V=[(d//q,d%q) for d in z]
        for row in range(2):
            for j in range(m):
                w=(row,j)
                t=observed(V,w)
                type_to_points.setdefault(t,[]).append((V,w))
                for a in range(q):
                    for b in range(q):
                        assert sem(paired(k,a,b),V,w)==(t[0]==(a,b)),('pair',k,m,V,w)
                        assert sem(dia(paired(k,a,b),'b'),V,w)==((a,b) in t[1]),('support',k,m,V,w,a,b)
                        count+=1
    assert len(type_to_points)==profile_count(k,m),(len(type_to_points),profile_count(k,m))
    # All types distinguishable by their primitive and depth-two tests.
    signs=set()
    for c,S in type_to_points:
        sig=(c,tuple((a,b) in S for a in range(q) for b in range(q)))
        assert sig not in signs
        signs.add(sig)
    # Cross-check invariance for independently generated nested formulas.
    fs=[('top',)]+[('var',i) for i in range(k)]
    import random
    rng=random.Random(k*101+m)
    for h in range(70):
        if not fs:break
        op=rng.choice(['not','and','or','a','b','A','B'])
        f=(op,rng.choice(fs),rng.choice(fs)) if op in ('and','or') else (op,rng.choice(fs))
        fs.append(f)
    for f in fs:
        for t,points in type_to_points.items():
            target=sem(f,*points[0])
            for v,w in points[1:]:assert sem(f,v,w)==target,('invariance',k,m,f,t)
    print('PASS',k,m,'pointed types',len(type_to_points),'pair/support checks',count,'formulas',len(fs))

def sharp():
    V1=[(0,0),(1,0)]
    V2=[(0,0),(1,1)]
    w=(0,0)
    for val in product([False,True],repeat=2):
        # Every depth-zero formula corresponds to some Boolean function of p.
        # Compare both depth-one diamonds (and their duals) on these four types.
        f=OR(AND(('var',0),('top',)),('top',)) if False else None
        def truth(v):return val[1] if v else val[0]
        for modality in 'ab':
            left=any(truth(V1[j][i]) for i,j in successors(2,modality,w))
            right=any(truth(V2[j][i]) for i,j in successors(2,modality,w))
            assert left==right
    A=box(dia(('var',0),'b'),'a')
    assert not sem(A,V1,w) and sem(A,V2,w)
    print('PASS depth-two sharpness on two columns')

if __name__=='__main__':
    for k,m in [(0,1),(0,4),(1,1),(1,2),(1,3),(1,4),(2,1),(2,2)]:test(k,m)
    sharp()
    print('TWO_LAYER_PRODUCT_PROFILE_OK')
