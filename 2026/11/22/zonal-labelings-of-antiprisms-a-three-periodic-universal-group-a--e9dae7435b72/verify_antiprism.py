#!/usr/bin/env python3
"""Independent finite checks for zonal labelings of antiprism graphs.

Usage: python3 verify_antiprism.py
No dependencies other than the Python 3 standard library.
"""
from itertools import product
from math import gcd, prod


def group(moduli):
    return list(product(*(range(m) for m in moduli)))


def add(a,b,M):
    return tuple((x+y)%m for x,y,m in zip(a,b,M))


def neg(a,M):
    return tuple(-x % m for x,m in zip(a,M))


def sm(a,b,c,M):
    return add(add(a,b,M),c,M)


def order(a,M):
    from math import lcm
    return lcm(*(m//gcd(v,m) for v,m in zip(a,M)))


def subgroup(a,b,M):
    zero=tuple(0 for _ in M)
    have={zero}; frontier=[zero]
    while frontier:
        x=frontier.pop()
        for v in (a,b):
            y=add(x,v,M)
            if y not in have:
                have.add(y);frontier.append(y)
    return len(have)


def face_valid(top,bottom,M):
    n=len(top); z=tuple(0 for _ in M)
    if any(x==z for x in top+bottom):return False
    if any(sm(top[i],top[(i+1)%n],bottom[i],M)!=z for i in range(n)):return False
    if any(sm(bottom[i],bottom[(i+1)%n],top[(i+1)%n],M)!=z for i in range(n)):return False
    s=z
    for x in top:s=add(s,x,M)
    if s!=z:return False
    s=z
    for x in bottom:s=add(s,x,M)
    return s==z


def exact_by_two_seed(n,M):
    """Build all possibilities using first side triangle then the next,
    and test every face, including both outer n-gons."""
    E=group(M)
    out=[]
    for a,b in product(E, repeat=2):
        top=[a,b]
        for _ in range(n-2):
            top.append(neg(add(top[-2],top[-1],M),M))
        bottom=[neg(add(top[i],top[(i+1)%n],M),M) for i in range(n)]
        if face_valid(top,bottom,M):out.append((top,bottom))
    return out


def formula_counts(n,M):
    E=group(M); Q=len(E); z=tuple(0 for _ in M)
    if n%3:return 0,0,0
    T=[x for x in E if 4%order(x,M)==0]
    T2=[x for x in T if 2%order(x,M)==0]
    dbl={add(x,x,M) for x in T}
    strong=len(T2)**2*(len(dbl)-1)*(len(dbl)-2)
    return (Q-1)*(Q-2),strong,None


def direct_full(n,M):
    """Independently enumerate all (2n)-vertex assignments, no recurrences."""
    E=group(M); z=tuple(0 for _ in M)
    count=0
    for vals in product([x for x in E if x!=z],repeat=2*n):
        if face_valid(vals[:n], vals[n:], M):count+=1
    return count


def verify():
    groups=[(2,), (3,), (4,), (5,), (6,), (8,), (2,2), (2,4), (4,4), (2,2,2), (4,2,2), (4,4,2)]
    cases=0
    for M in groups:
        for n in range(3,14):
            L=exact_by_two_seed(n,M)
            predicted,strong,_=formula_counts(n,M)
            assert len(L)==predicted,(n,M,len(L),predicted)
            nstrong=sum(all(order(v,M)==4 for v in top+bot) for top,bot in L)
            assert nstrong==strong,(n,M,nstrong,strong)
            if n%3==0:
                triples=set((top[0],top[1],top[2]) for top,bot in L)
                unseen=set(triples); orbits=0; strong_orbits=0
                while unseen:
                    tri=unseen.pop()
                    from itertools import permutations
                    orbit=set(permutations(tri))
                    assert orbit.issubset(triples)
                    unseen.difference_update(orbit)
                    orbits+=1
                    if all(order(x,M)==4 for x in tri):strong_orbits+=1
                t2=sum(2%order(x,M)==0 for x in group(M))
                t3=sum(3%order(x,M)==0 for x in group(M))
                assert orbits==(prod(M)**2-3*t2+2*t3)//6,(n,M,orbits)
                assert strong_orbits==strong//6,(n,M,strong_orbits,strong)
                assert (prod(M)**2-3*t2+2*t3)%6==0
            ngenerative=sum(subgroup(top[0],top[1],M)==prod(M) for top,bot in L)
            if n%3:
                assert ngenerative==0
            elif len(M)==1 and M[0]==2:
                assert ngenerative==0
            elif n%3==0 and (len(M)==1 or (len(M)<=2 and M!=(2,))):
                assert ngenerative>0,(n,M)
            else:
                assert ngenerative==0,(n,M)
            if n%3==0 and M==(4,4):
                assert nstrong==96 and ngenerative==96
            cases+=1
    print('ALL_AB_GROUP_TWO_SEED_COUNTS_AND_ORDERS_PASS',cases)
    fcases=[(3,(2,)),(3,(3,)),(3,(4,)),(3,(2,2)),(4,(2,)),(4,(3,)),(4,(4,)),(5,(2,)),(5,(3,)),(6,(2,))]
    for n,M in fcases:
        c=direct_full(n,M)
        assert c==formula_counts(n,M)[0],(n,M,c)
    print('INDEPENDENT_FULL_VERTEX_EXHAUSTION_PASS',len(fcases))
    print('FINITE_GROUP_FULL_SYMMETRY_ORBIT_FORMULA_PASS')
    print('FOUR_TORSION_AND_GENERATIVE_C4xC4_96_PASS')
    print('VERIFY_OK')

if __name__=='__main__':verify()
