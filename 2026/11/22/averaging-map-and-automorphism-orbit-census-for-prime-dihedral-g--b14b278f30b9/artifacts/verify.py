"""Reproduce counts of conjugation-averaging maps on prime dihedral groups."""
from itertools import product
from math import gcd


def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def phi(n):
    return sum(gcd(i,n)==1 for i in range(1,n+1))

def neck(m,k):
    return sum(phi(d)*k**(m//d) for d in divisors(m))//m

def pred(p):
    m=(p-1)//2
    s=sum(phi(d)*p**((p-1)//d) for d in divisors(p-1) if d>1)
    return {
      'all':p**(p+1)+p*(2**(p+1)-1)+p**m,
      'pointed':p**p+p*(2**p-1)+p**m,
      'orbits':4*neck(m,4)+(p**(p+1)+s)//(p-1)+neck(m,p)-1,
      'pointed_orbits':2*neck(m,4)+(p**p+s)//(p-1)+neck(m,p)-1
    }

def verify(p, orbit_test=True):
    n=2*p
    def mul(x,y):
        a,b=x%p,x//p;c,d=y%p,y//p
        return (a+(1 if b==0 else -1)*c)%p + p*((b+d)%2)
    def inv(x):
        a,b=x%p,x//p
        return ((-a if b==0 else a)%p)+p*b
    def conj(x,y): return mul(mul(x,y),inv(x))
    def perm_aut(u,v,x):
        a,b=x%p,x//p
        return (u*a+v*b)%p+p*b
    def orbits_by_generator(x):
        seen=set();orbs=[]
        for a in range(n):
            if a in seen: continue
            orb=[];y=a
            while y not in seen:
                orb.append(y);seen.add(y);y=conj(x,y)
            orbs.append(orb)
        return orbs
    maps={}
    def add(A,h):
        A=tuple(A)
        assert A not in maps,('duplicate',p,h)
        maps[A]=h
    add([0]*n,'one')
    # Rotation-image maps; H=<r>. Rotation points fixed, reflection points one orbit.
    for vals in product(range(p),repeat=p+1):
        if not any(vals):continue
        A=[vals[i] for i in range(p)]+[vals[p]]*p
        add(A,'rot')
    # Each reflection-generated subgroup, maps fixed on reflection-conjugacy orbits.
    for k in range(p):
        t=p+k;orbs=orbits_by_generator(t)
        assert len(orbs)==p+1
        for bits in product((0,1),repeat=p+1):
            if not any(bits):continue
            A=[-1]*n
            for orb,b in zip(orbs,bits):
                for x in orb:A[x]=t if b else 0
            add(A,'reflection')
    # Fully conjugation-equivariant maps with generated image G.
    for vals in product(range(p),repeat=(p-1)//2):
        A=[0]*n
        for i,v in enumerate(vals,1):
            A[i]=v;A[p-i]=(-v)%p
        for k in range(p):A[p+k]=p+k
        add(A,'whole')
    for A,h in maps.items():
        for x in range(n):
            for y in range(n):
                if conj(A[x],A[y]) != A[conj(A[x],y)]:
                    raise AssertionError(('averaging failed',p,h,A,x,y))
    total=len(maps);pointed=sum(A[0]==0 for A in maps)
    got={'all':total,'pointed':pointed}
    if orbit_test:
        seen=set();orbits=0;pointed_orbits=0
        for A in maps:
            if A in seen:continue
            images=set()
            for u in range(1,p):
                for v in range(p):
                    B=[-1]*n
                    for x in range(n):
                        B[perm_aut(u,v,x)]=perm_aut(u,v,A[x])
                    images.add(tuple(B))
            assert images.issubset(maps),('aut-closure fails',p)
            assert not images&seen
            seen|=images
            orbits+=1
            pointed_orbits+=(A[0]==0)
        assert seen==set(maps)
        got.update(orbits=orbits,pointed_orbits=pointed_orbits)
    expect=pred(p)
    assert all(got[k]==expect[k] for k in got),(p,got,expect)
    print('p',p,'measured',got,'predicted',expect,flush=True)
    return got

if __name__=='__main__':
    verify(3)
    verify(5)
    print('PRIME_DIHEDRAL_AVERAGING_VERIFIED')
