"""Pencil/dual-conic arithmetic enumeration over GF(9), plus quadratic base extension."""
from itertools import product, combinations
from collections import Counter
from math import gcd

class F9:
    q=9
    @staticmethod
    def add(a,b):return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
    @staticmethod
    def neg(a):return ((-a%3)%3)+3*((-(a//3))%3)
    @staticmethod
    def sub(a,b):return F9.add(a,F9.neg(b))
    @staticmethod
    def mul(a,b):
        x,y=a%3,a//3;z,w=b%3,b//3
        return ((x*z+2*y*w)%3)+3*((x*w+y*z)%3)
    @staticmethod
    def pow(a,n):
        t=1
        while n:
            if n&1:t=F9.mul(t,a)
            a=F9.mul(a,a);n>>=1
        return t
    @staticmethod
    def inv(a):
        assert a
        return F9.pow(a,7)

a,m,s=F9.add,F9.mul,F9.sub

def dot(v,w):
    z=0
    for x,y in zip(v,w):z=a(z,m(x,y))
    return z

def matvec(H,v):return [dot(row,v) for row in H]

def cross(v,w):
    return [s(m(v[1],w[2]),m(v[2],w[1])),s(m(v[2],w[0]),m(v[0],w[2])),s(m(v[0],w[1]),m(v[1],w[0]))]

def norm(v):
    for x in v:
        if x:
            ix=F9.inv(x)
            return tuple(m(y,ix) for y in v)
    raise ValueError('zero')

def vectors(n):
    for j in range(n):
        for tail in product(range(9),repeat=n-1-j):
            yield (0,)*j+(1,)+tail

def hessian(D):
    A,B,C,E,F,G=D
    return [[m(2,A),B,C],[B,m(2,E),F],[C,F,m(2,G)]]

def determinant(H):
    e1=s(m(H[1][1],H[2][2]),m(H[1][2],H[2][1]))
    e2=s(m(H[1][0],H[2][2]),m(H[1][2],H[2][0]))
    e3=s(m(H[1][0],H[2][1]),m(H[1][1],H[2][0]))
    return a(s(m(H[0][0],e1),m(H[0][1],e2)),m(H[0][2],e3))

def adj(H):
    a0,b,c=H[0];d,e,f=H[1];g,h,i=H[2]
    return [[s(m(e,i),m(f,h)),s(m(c,h),m(b,i)),s(m(b,f),m(c,e))],
            [s(m(f,g),m(d,i)),s(m(a0,i),m(c,g)),s(m(c,d),m(a0,f))],
            [s(m(d,h),m(e,g)),s(m(b,g),m(a0,h)),s(m(a0,e),m(b,d))]]

def line_square(L):
    x,y,z=L
    return (m(x,x),m(2,m(x,y)),m(2,m(x,z)),m(y,y),m(2,m(y,z)),m(z,z))

def conic_add(C,Lsq,lam):return tuple(a(c,m(lam,e)) for c,e in zip(C,Lsq))

def graph(D,points,lines):
    H=hessian(D);Ah=adj(H)
    nbr=[[] for _ in points]
    for (i,j),ell in lines.items():
        if dot(ell,matvec(Ah,ell))==0:
            nbr[i].append(j);nbr[j].append(i)
    assert all(len(z) in (0,2) for z in nbr)
    vis=set();sizes=[]
    for i in range(len(points)):
        if i in vis or not nbr[i]:continue
        stack=[i];vis.add(i);cnt=0
        while stack:
            v=stack.pop();cnt+=1
            for w in nbr[v]:
                if w not in vis:vis.add(w);stack.append(w)
        sizes.append(cnt)
    assert not sizes or len(set(sizes))==1
    return (sizes[0],len(sizes)) if sizes else (0,0)

def run():
    pts=[(m(t,t),t,1) for t in range(9)]+[(1,0,0)]
    lines={(i,j):cross(pts[i],pts[j]) for i,j in combinations(range(10),2)}
    C=(0,0,1,2,0,0)
    all_lines=Counter();counts=Counter();two_double=0
    for L in vectors(3):
        k=sum(dot(L,P)==0 for P in pts)
        all_lines[k]+=1
        if k==1:continue
        assert k in (0,2)
        Lsq=line_square(L)
        good=[]
        for lam in range(1,9):
            D=conic_add(C,Lsq,lam)
            if determinant(hessian(D))==0:continue
            good.append(D)
            g=graph(D,pts,lines)
            counts[(k,g)]+=1
            two_double+=1
        assert len(good)==7,(L,k,len(good))
    assert all_lines==Counter({2:45,0:36,1:10}),all_lines
    assert two_double==567
    expected=Counter({(2,(4,2)):45,(2,(8,1)):90,(0,(5,2)):72,(0,(10,1)):72,(2,(0,0)):180,(0,(0,0)):108})
    assert counts==expected,(counts,expected)
    # All 9 geometric (2,2) pencil members over F3 have rational cycles after extending to F9.
    # Restrict to lines defined over F3 by embedding their coefficients as constants.
    f3_pts=[(t*t%3,t,1) for t in range(3)]+[(1,0,0)]
    f3_conics=[]
    for L in vectors(3):
        if any(x>=3 for x in L):continue
        if sum(dot(L,P)==0 for P in f3_pts)==1:continue
        Lsq=line_square(L)
        for lam in (1,2):
            D=conic_add(C,Lsq,lam)
            if determinant(hessian(D)):
                f3_conics.append(D)
    assert len(f3_conics)==9,len(f3_conics)
    for D in f3_conics:
        assert graph(D,pts,lines)==(4,2)
    return {'q':9,'line_counts_by_conic_intersection':dict(sorted(all_lines.items())),
            'contact_22_pairs_per_fixed_C':two_double,
            'rational_cycle_counts':{str(k):v for k,v in sorted(counts.items())},
            'F3_contact_22_pairs_lifted_to_F9':len(f3_conics),
            'all_F3_lifts_have_two_four_cycles':True}
if __name__=='__main__':
    import json
    print(json.dumps(run(),sort_keys=True))
