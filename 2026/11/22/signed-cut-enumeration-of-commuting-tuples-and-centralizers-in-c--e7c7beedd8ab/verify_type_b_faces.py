"""Direct finite arithmetic checks of Coxeter type-B face-monoid statements.
All input sizes are small; the proof is independent of this enumeration.
Run: python verify_type_b_faces.py
"""
from itertools import combinations, permutations, product
from math import factorial, comb, prod
from functools import lru_cache

@lru_cache(None)
def stirling(n,k):
    if k<0 or k>n: return 0
    if k==n==0: return 1
    return k*stirling(n-1,k)+stirling(n-1,k-1)

def ordered_partitions(items):
    if not items:
        yield ()
        return
    x=items[0]
    for p in ordered_partitions(items[1:]):
        for j in range(len(p)):
            yield p[:j]+(p[j]+(x,),)+p[j+1:]
        for j in range(len(p)+1):
            yield p[:j]+((x,),)+p[j:]

def sign(x):return int(x>0)-int(x<0)

def covector(coords):
    n=len(coords)
    return (tuple(map(sign,coords))+
            tuple(sign(coords[i]-coords[j]) for i in range(n) for j in range(i+1,n))+
            tuple(sign(coords[i]+coords[j]) for i in range(n) for j in range(i+1,n)))

def all_faces(n):
    faces={}
    for zmask in range(1<<n):
        zero=tuple(j for j in range(n) if zmask>>j&1)
        remain=tuple(j for j in range(n) if not zmask>>j&1)
        for p in ordered_partitions(remain):
            for signs in product((-1,1),repeat=len(remain)):
                signs=dict(zip(remain,signs))
                coords=[0]*n
                for j,block in enumerate(p,1):
                    for i in block:coords[i]=j*signs[i]
                v=covector(coords)
                assert v not in faces
                faces[v]=(len(zero),tuple(len(b) for b in p))
    return faces

def compatible(u,v):
    return all(x*y!=-1 for x,y in zip(u,v))

def face_count(n):
    return sum(comb(n,z)*2**(n-z)*sum(factorial(k)*stirling(n-z,k) for k in range(n-z+1)) for z in range(n+1))

def tuples_formula(n,t):
    a=(1<<t)-1
    return sum(comb(n,z)*2**(n-z)*sum(a**k*factorial(k)*stirling(n-z,k) for k in range(n-z+1)) for z in range(n+1))

def central_formula(z,blocks):
    return (1<<len(blocks))*face_count(z)*prod(sum(factorial(k)*stirling(b,k) for k in range(b+1)) for b in blocks)

def all_chambers(n):
    for pp in permutations(range(1,n+1)):
        for ep in product((-1,1),repeat=n):
            yield tuple(x*e for x,e in zip(pp,ep))

def chamber_faces(ch):
    n=len(ch); out=set()
    for mask in range(1<<n):
        coords=[0]*n
        j=0; magnitude=0
        for i in range(n):
            # bit i means boundary before label at index i, including central boundary.
            if mask>>i&1: magnitude+=1
            coords[abs(ch[i])-1]=sign(ch[i])*magnitude
        out.add(covector(coords))
    return out

def common_cuts(ch,dh):
    n=len(ch)
    return sum(set(ch[j:])==set(dh[j:]) for j in range(n))

def check():
    for n in range(0,5):
        faces=all_faces(n); vv=list(faces); assert len(vv)==face_count(n)
        # independent sign-vector pair checks
        if n>0:
            actual=0
            for v in vv:
                c=sum(compatible(v,w) for w in vv)
                assert c==central_formula(*faces[v]),(n,faces[v],c,central_formula(*faces[v]))
                actual+=c
            assert actual==tuples_formula(n,2),(n,actual,tuples_formula(n,2))
        print('pair_and_centralizers',n,len(vv),tuples_formula(n,2))
    for n in (1,2,3):
        vv=list(all_faces(n)); cm=[[int(compatible(v,w)) for w in vv] for v in vv]
        for t in (3,4) if n<=2 else (3,):
            # clique graph matrices: count ordered tuples by enumerating all ordered t-tuples of indices
            total=0
            for inds in product(range(len(vv)),repeat=t):
                if all(cm[inds[i]][inds[j]] for i in range(t) for j in range(i+1,t)):
                    total+=1
            assert total==tuples_formula(n,t),(n,t,total,tuples_formula(n,t))
            print('higher_tuple',n,t,total)
    for n in (1,2,3):
        fs=all_faces(n)
        cs=list(all_chambers(n))
        cl={ch:chamber_faces(ch) for ch in cs}
        assert len(cs)==2**n*factorial(n)
        assert all(len(v)==2**n and v<=fs.keys() for v in cl.values())
        for a in cs:
            for b in cs:
                assert len(cl[a]&cl[b])==2**common_cuts(a,b),(n,a,b)
        # each face belongs to at least one chamber cone, every compatible pair has common chamber
        assert set().union(*cl.values())==set(fs)
        for x in fs:
            for y in fs:
                assert (any(x in cl[ch] and y in cl[ch] for ch in cs))==compatible(x,y)
        print('chamber_and_overlap',n,len(cs))
    print('VERIFY_OK')

if __name__=='__main__': check()
