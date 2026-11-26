"""Exact finite-field consistency tests for the dihedral Fourier commutator theorem.
No external dependencies. Tests direct structure constants against constructed commutators.
"""
import random
from math import gcd


def root(n,p):
    if (p-1)%n: raise ValueError('n must divide p-1')
    for a in range(1,p):
        if pow(a,n,p)==1 and all(pow(a,n//d,p)!=1 for d in range(2,n+1) if n%d==0 and all(d%j for j in range(2,int(d**.5)+1))):
            return a
    raise AssertionError('root not found')


def det(a,b,p): return (a[0]*b[1]-a[1]*b[0])%p


def cycle_vectors(c,p):
    m=len(c)
    assert m>=3
    if m>3:
        q=cycle_vectors(c[:-2]+[1],p)
        v=((c[-1]*q[-1][0]+c[-2]*q[0][0])%p,
           (c[-1]*q[-1][1]+c[-2]*q[0][1])%p)
        ans=q+[v]
    else:
        if not any(c): ans=[(0,0)]*3
        else:
            shift=next(i for i,v in enumerate(c) if v!=0)
            cc=[c[(shift+i)%3] for i in range(3)]
            r=pow(cc[0],-1,p)
            rotated=[(1,0),(0,cc[0]),(-cc[1]*r%p,-cc[2]%p)]
            ans=[None]*3
            for i in range(3): ans[(shift+i)%3]=rotated[i]
    assert all(det(ans[i],ans[(i+1)%m],p)==c[i]%p for i in range(m))
    return ans


def commutator(u,v,n,p):
    z=[0]*n
    for i in range(n):
        for j in range(n):
            t=(u[i]*v[j]-v[i]*u[j])%p
            z[(2*j-i)%n]=(z[(2*j-i)%n]+t)%p
    return z


def check(n,p,seed=159,rounds=100):
    w=root(n,p)
    assert pow(w,n,p)==1
    rng=random.Random(seed+n*1000+p)
    nonfixed={i for i in range(n) if (3*i)%n !=0}
    cycles=[]
    remain=set(nonfixed)
    while remain:
        i=min(remain); o=[]; j=i
        while j not in o:
            assert j in remain
            o.append(j);remain.remove(j);j=(-2*j)%n
        assert j==i and len(o)>=3
        cycles.append(o)
    for z in range(rounds):
        target=[rng.randrange(p) if k in nonfixed else 0 for k in range(n)]
        U=[0]*n;V=[0]*n
        for orbit in cycles:
            c=[target[(-i)%n]*pow(n,-1,p)%p for i in orbit]
            xy=cycle_vectors(c,p)
            for a,(x,y) in zip(orbit,xy): U[a]=x;V[a]=y
        uu=[sum(U[k]*pow(w,k*j,p) for k in range(n))%p for j in range(n)]
        vv=[sum(V[k]*pow(w,k*j,p) for k in range(n))%p for j in range(n)]
        zz=[sum(target[k]*pow(w,k*j,p) for k in range(n))%p for j in range(n)]
        assert commutator(uu,vv,n,p)==zz,(n,p,z)
    return [len(o) for o in cycles], len(nonfixed)




def check_product_group(moduli,p,rounds=32):
    import itertools
    S=list(itertools.product(*(range(n) for n in moduli)))
    size=len(S);pos={v:i for i,v in enumerate(S)}
    roots=[root(n,p) for n in moduli]
    z=lambda x:tuple((-2*v)%n for v,n in zip(x,moduli))
    inv=lambda x:tuple((-v)%n for v,n in zip(x,moduli))
    fixed={x for x in S if z(x)==x}
    unseen=set(S)-fixed
    cycles=[]
    while unseen:
        x=min(unseen); cyc=[]; y=x
        while y not in cyc:
            assert y in unseen
            unseen.remove(y);cyc.append(y);y=z(y)
        assert y==x and len(cyc)>=3
        cycles.append(cyc)
    rng=random.Random(size+p)
    def fourier(a,j):
        v=1
        for n,r,k,t in zip(moduli,roots,a,j):
            v=v*pow(r,k*t,p)%p
        return v
    mat=[[fourier(a,j) for a in S] for j in S]
    invn=pow(size,-1,p)
    for _ in range(rounds):
        target={a:(0 if a in fixed else rng.randrange(p)) for a in S}
        U={a:0 for a in S};V={a:0 for a in S}
        for cyc in cycles:
            c=[target[inv(a)]*invn%p for a in cyc]
            xy=cycle_vectors(c,p)
            for a,(x,y) in zip(cyc,xy):U[a]=x;V[a]=y
        u=[sum(row[t]*U[a] for t,a in enumerate(S))%p for row in mat]
        v=[sum(row[t]*V[a] for t,a in enumerate(S))%p for row in mat]
        wanted=[sum(row[t]*target[a] for t,a in enumerate(S))%p for row in mat]
        obtained=[0]*size
        for i,a in enumerate(S):
            for j,b in enumerate(S):
                g=tuple((2*y-x)%n for x,y,n in zip(a,b,moduli))
                obtained[pos[g]]=(obtained[pos[g]]+u[i]*v[j]-v[i]*u[j])%p
        assert obtained==wanted,(moduli,p)
    print(f'group={moduli}, p={p}, derived_dim={size-len(fixed)}, cycles={[len(c) for c in cycles]}, trials={rounds} OK')

def main():
    for n,p in [(1,7),(3,7),(5,11),(7,29),(9,19),(11,23),(13,53),(15,31),(21,43),(25,101)]:
        cycles,dimension=check(n,p,rounds=60)
        assert dimension==n-gcd(n,3)
        print(f'n={n}, p={p}, derived_dim={dimension}, cycle_lengths={cycles}, trials=60 OK')
    # Independent brute enumeration of all edge-minor target vectors for small fields.
    import itertools
    for p in (2,3):
        for m in range(3,7):
            for c in itertools.product(range(p),repeat=m):
                v=cycle_vectors(list(c),p)
                assert tuple(det(v[i],v[(i+1)%m],p) for i in range(m))==c
            print(f'cycle minors complete, field={p}, length={m}')
    for g,p in [((3,5),31),((5,5),11),((3,9),19),((3,3,5),31),((7,7),29)]:
        check_product_group(g,p,rounds=24)
    print('VERIFY_OK')

if __name__=='__main__': main()
