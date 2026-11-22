#!/usr/bin/env python3
"""Exact, standard-library verification of signed dihedral Lefschetz calculations for GP(n,2).
This file computes mathematical certificates; finite checks supplement the stated matrix proof.
"""
from functools import lru_cache
from math import gcd

def edge(a,b): return (a,b) if a<b else (b,a)

def gp_edges(n):
    e=set()
    for j in range(n):
        e.add(edge(j,(j+1)%n))
        e.add(edge(n+j,n+(j+2)%n))
        e.add(edge(j,n+j))
    return e

def quotient(n, a=0, reflection=True):
    p=lambda v: n*(v//n)+((a-(v%n))%n if reflection else (a+v%n)%n)
    orbit_id={}; orbits=[]
    for v in range(2*n):
        if v not in orbit_id:
            z=v; o=[]
            while z not in orbit_id:
                orbit_id[z]=len(orbits);o.append(z);z=p(z)
            orbits.append(o)
    forbidden=set(); edges=set()
    for u,v in gp_edges(n):
        i,j=orbit_id[u],orbit_id[v]
        if i==j: forbidden.add(i)
        else:edges.add(edge(i,j))
    keep=sorted(set(range(len(orbits)))-forbidden)
    result={tuple(sorted(orbits[i])):set() for i in keep}
    for i,j in edges:
        if i in keep and j in keep:
            oi=tuple(sorted(orbits[i]));oj=tuple(sorted(orbits[j]));
            result[oi].add(oj);result[oj].add(oi)
    return result

def strip_edges(n,a):
    # Vertices are (layer,position) with first layer 0=outer, 1=inner.
    if n%2:
        assert a==0
        m=(n-1)//2; L=m+1; start=0
        ban={(1,1),(0,m)}
        extras={edge((1,m-1),(1,m))}
    elif a==0:
        m=n//2;L=m+1; start=0
        ban={(1,1),(1,m-1)};extras=set()
    else:
        assert a==1
        m=n//2;L=m; start=1
        ban={(0,1),(0,m)}
        extras={edge((1,1),(1,2)),edge((1,m-1),(1,m))}
    E=set()
    for j in range(start,start+L):E.add(edge((0,j),(1,j)))
    for j in range(start,start+L-1):E.add(edge((0,j),(0,j+1)))
    for j in range(start,start+L-2):E.add(edge((1,j),(1,j+2)))
    E|=extras
    E={e for e in E if e[0] not in ban and e[1] not in ban}
    V={(i,j) for i in (0,1) for j in range(start,start+L)}-ban
    return V,E

def strip_matches_quotient(n,a):
    qs=quotient(n,a,True)
    # each orbit is identified via representative j in an interval
    if n%2:
        start=0;end=(n-1)//2
    elif a==0:
        start=0;end=n//2
    else:
        start=1;end=n//2
    equiv={}
    for orb in qs:
        r=min([v%n for v in orb if start<=v%n<=end])
        equiv[orb]=(orb[0]//n,r)
    V,E=strip_edges(n,a)
    gotE={edge(equiv[x],equiv[y]) for x,nbrs in qs.items() for y in nbrs}
    return V==set(equiv.values()) and E==gotE

def signed_independent(E,vertices):
    vertices=sorted(vertices); ids={v:i for i,v in enumerate(vertices)}
    adj=[0]*len(vertices)
    for u,v in E:
        a=ids[u];b=ids[v];adj[a]|=1<<b;adj[b]|=1<<a
    @lru_cache(None)
    def rec(mask):
        if not mask:return 1
        i=max((j for j in range(len(vertices)) if mask>>j&1),key=lambda x:(mask&adj[x]).bit_count())
        return rec(mask&~(1<<i))-rec(mask&~(1<<i)&~adj[i])
    return rec((1<<len(vertices))-1)

def quotient_sum(n,a,refl=True):
    Q=quotient(n,a,refl)
    V=list(Q)
    E={edge(x,y) for x,neigh in Q.items() for y in neigh}
    return signed_independent(E,V)

def matrix_mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def matrix_power(A,n):
    size=len(A);R=[[int(i==j) for j in range(size)] for i in range(size)]
    while n:
        if n&1:R=matrix_mul(R,A)
        A=matrix_mul(A,A);n//=2
    return R

def T_matrix():
    T=[[0]*8 for _ in range(8)]
    for st in range(8):
        outer_prev=(st>>2)&1; inner_prevprev=(st>>1)&1; inner_prev=st&1
        for out,inner in ((0,0),(1,0),(0,1)):
            if out and outer_prev or inner and inner_prevprev:continue
            nxt=4*out+2*inner_prev+inner
            T[st][nxt]+=(-1)**(out+inner)
    return T

def dim(n):
    q,r=divmod(n,5)
    return 3*q-1 if r==0 else 3*q+r-2

def rotation_formula(n,a):
    d=gcd(n,a)
    return (-1)**(dim(n)+d)*(1-5*(d%5==0))

def reflection_formula(n,a):
    # Seeds n=5..24, indexed by n%20, exact independently by orbit sums.
    seed={5:(0,0),6:(-1,1),7:(1,1),8:(1,-1),9:(-1,-1),
          10:(0,0),11:(-1,-1),12:(-1,1),13:(1,1),14:(1,-1),
          15:(0,0),16:(1,-1),17:(-1,-1),18:(-1,1),19:(1,1),
          20:(0,0),21:(1,1),22:(1,-1),23:(-1,-1),24:(-1,1)}
    b=5+(n-5)%20
    return seed[b][a%2] if n%2==0 else seed[b][0]

def run():
    T=T_matrix();T4=matrix_power(T,4);T5=matrix_power(T,5)
    I=[[int(i==j) for j in range(8)] for i in range(8)]
    assert matrix_mul(T4,[[T5[i][j]+I[i][j] for j in range(8)] for i in range(8)])==[[0]*8 for _ in range(8)]
    print('TRANSFER_IDENTITY: T^4(T^5+I)=0 PASS')
    count=0
    for n in range(11,38):
        for a in ([0] if n%2 else [0,1]):
            assert strip_matches_quotient(n,a),(n,a)
            count+=1
    print('REFLECTION_STRIP_GRAPHS:',count,'PASS')
    # Exact seed traces (not relying on homology calculation)
    for n in range(5,25):
        for a in ([0] if n%2 else [0,1]):
            W=quotient_sum(n,a,True)
            tr=(-1)**(dim(n)+1)*W
            assert tr==reflection_formula(n,a),(n,a,tr,reflection_formula(n,a))
    print('REFLECTION_SEEDS: n=5..24 PASS')
    # Verify base pairs n->n+10 that precede the uniform transfer identity threshold.
    for n in range(11,16):
        for a in ([0] if n%2 else [0,1]):
            assert quotient_sum(n+10,a,True)==-quotient_sum(n,a,True)
    print('SMALL_RECURSION_SEEDS: n=11..15 PASS')
    for n in range(5,23):
        for a in range(n):
            w=quotient_sum(n,a,False)
            actual=(-1)**(dim(n)+1)*w
            assert actual==rotation_formula(n,a),(n,a,actual,rotation_formula(n,a))
    print('ROTATIONS: n=5..22 all group elements PASS')
    for n in range(5,28):
        for a in ([0] if n%2 else [0,1]):
            w=quotient_sum(n,a,True)
            assert (-1)**(dim(n)+1)*w==reflection_formula(n,a)
    print('REFLECTIONS: n=5..27 PASS')
    print('QUOTIENT_RANKS:')
    for n in range(5,31):
        inv=(sum(rotation_formula(n,a)+reflection_formula(n,a) for a in range(n)))//(2*n)
        expect=int(n%20 in (1,7,13,19))
        assert inv==expect,(n,inv,expect)
        print(n,inv,end='; ')
    print('\nALL TESTS PASS')

if __name__=='__main__':run()
