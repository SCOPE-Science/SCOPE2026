"""Standalone exact arithmetic checks for parabolic line-frequency sampling.
The primary theorem is proved symbolically; these are finite corroborations.
No network access or external libraries required.
"""
from fractions import Fraction
from itertools import combinations
from cmath import exp, pi

def rank_integer(A):
    if not A:return 0
    M=[[Fraction(x) for x in row] for row in A]
    rows,cols=len(M),len(M[0]); r=0
    for j in range(cols):
        pivot=next((i for i in range(r,rows) if M[i][j]),None)
        if pivot is None:continue
        M[r],M[pivot]=M[pivot],M[r]
        v=M[r][j]
        for k in range(j,cols):M[r][k]/=v
        for i in range(r+1,rows):
            if M[i][j]:
                v=M[i][j]
                for k in range(j,cols):M[i][k]-=v*M[r][k]
        r+=1
        if r==rows:break
    return r

def prime_field(p):
    return list(range(p)),lambda a,b:(a+b)%p,lambda a,b:(a*b)%p,p

def field9():
    p=3
    def add(u,v):return (u%p+v%p)%p +p*((u//p+v//p)%p)
    def mul(u,v):
        a,b=u%p,u//p; c,d=v%p,v//p
        return (a*c+2*b*d)%p +p*((a*d+b*c)%p)
    return list(range(9)),add,mul,3

def measure_rows(c,E,add,mul,p):
    q=len(E);zero=E[0];neg=lambda z:next(t for t in E if add(t,z)==zero)
    def r(x):return add(c,neg(x))
    seen=set();rows=[]
    for x in E:
        if x in seen:continue
        y=r(x);seen|={x,y}
        row=[0]*q
        row[E.index(x)]=1;row[E.index(y)]=1
        rows.append(row)
    return rows

def affine_span_size(C,E,add,p):
    zero=E[0];neg=lambda z:next(t for t in E if add(z,t)==zero)
    gen=[add(c,neg(C[0])) for c in C[1:]]
    H={zero}
    for a in gen:
        H={add(h,multiple(a,k,add,zero)) for h in H for k in range(p)}
    return len(H)

def multiple(a,k,add,zero):
    r=zero
    for _ in range(k):r=add(r,a)
    return r

def rank_complex(A,tol=1e-7):
    if not A:return 0
    M=[list(row) for row in A];rows=len(M);cols=len(M[0]);r=0
    for j in range(cols):
        z=max(range(r,rows),key=lambda i:abs(M[i][j]),default=None)
        if z is None or abs(M[z][j])<tol:continue
        M[r],M[z]=M[z],M[r]
        v=M[r][j]
        for k in range(j,cols):M[r][k]/=v
        for i in range(r+1,rows):
            if abs(M[i][j])>tol:
                v=M[i][j]
                for k in range(j,cols):M[i][k]-=v*M[r][k]
        r+=1
        if r==cols:break
    return r

def fourier_rows(C,E,add,mul,p):
    zero=E[0];neg=lambda x:next(z for z in E if add(x,z)==zero)
    tr=lambda z:z if len(E)==p else (2*(z%p))%p
    return [[exp(2j*pi*tr(mul(s,add(mul(t,t),neg(mul(c,t)))))/p)
             for t in E] for c in C for s in E]

def check_case(field):
    E,add,mul,p=field;q=len(E)
    tested=0
    # all nonempty collections up to size 3 (or 4 for F_9)
    for r in range(1, min(4,q)+1):
        for C in combinations(E,r):
            Hsize=affine_span_size(C,E,add,p)
            want=(q//Hsize-1)//2
            rows=[]
            for c in C:rows+=measure_rows(c,E,add,mul,p)
            got=q-rank_integer(rows)
            assert got==want,(q,C,Hsize,got,want)
            direct=q-rank_complex(fourier_rows(C,E,add,mul,p))
            assert direct==want,(q,C,Hsize,direct,want)
            tested+=1
    return tested

if __name__=='__main__':
    results=[]
    for p in (3,5,7):results.append((p,check_case(prime_field(p))))
    results.append((9,check_case(field9())))
    # Field-nine two-view instance: invisible support is exactly six.
    E,add,mul,p=field9();rows=[]
    for c in (0,1):rows+=measure_rows(c,E,add,mul,p)
    for support in combinations(range(9),5):
        minor=[[row[j] for j in support] for row in rows]
        assert rank_integer(minor)==5
    # The two disjoint three-site cosets of the additive span of 1
    # have identical projections in both views.
    H={0,1,2};neg=lambda z:next(t for t in E if add(t,z)==0)
    x=3;y=neg(x)   # slopes {0,1}; cosets of +/-alpha
    A={add(x,h) for h in H};B={add(y,h) for h in H}
    assert not (A & B)
    for row in rows:assert sum(row[t] for t in A)==sum(row[t] for t in B)
    assert sum(n for _,n in results)>250
    print('CHECK_OK exact_incidence_rank_cases='+str(results))
