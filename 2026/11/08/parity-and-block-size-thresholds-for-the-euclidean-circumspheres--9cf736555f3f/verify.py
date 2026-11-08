"""Standalone exact verification for path-block polytope enclosing spheres.

Run with Python 3: python verify.py. Requires Python standard library; optional
SciPy provides a separate numerical optimization corroboration.
"""
from fractions import Fraction as Q
from itertools import product

checks=0

def check(condition, context):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(context)


def supports(m):
    return [b for b in product((0,1), repeat=m) if all(b[i]+b[i+1]<=1 for i in range(m-1))]


def candidate(m,a):
    if m%2==0:
        p=[Q(1,2)]*m
        r=Q(m*(2*a-1),4*a)
        active=lambda b:sum(b)==m//2 if a>1 else True
        count=(m//2+1)*a**(m//2) if a>1 else None
    else:
        h=min(Q(1), Q(m+a-1,2*m))
        p=[h if i%2==0 else 1-h for i in range(m)]
        if a<=m+1:
            r=Q(m*(2*a-1),4*a)+Q((a-1)**2,4*m*a)
        else:
            r=Q((m+1)*(a-1),2*a)
        odd=tuple(int(i%2==0) for i in range(m))
        even=tuple(int(i%2==1) for i in range(m))
        active=lambda b:(True if a==1 else (b in (odd,even) if a<=m+1 else b==odd))
        count=(a**((m+1)//2)+a**((m-1)//2) if 1<a<=m+1 else a**((m+1)//2)) if a>1 else None
    return p,r,active,count


def test_exact(m,a):
    p,r,active,count=candidate(m,a)
    S=supports(m)
    c=[x/a for x in p]
    base=a*sum(x*x for x in c)
    w=[1-2*x for x in c]
    ncontacts=0
    for b in S:
        d=base+sum(x for x,y in zip(w,b) if y)
        check(d<=r,(m,a,b,d,r,'enclosure'))
        check((d==r)==active(b),(m,a,b,d,r,'contacts'))
        if d==r:
            ncontacts+=a**sum(b)
    if count is not None:
        check(ncontacts==count,(m,a,'contact-count',ncontacts,count))
    else:
        check(ncontacts==sum(a**sum(b) for b in S),(m,a,'all-contact'))
    # Explicit barycentric contact measure: random colors in occupied blocks,
    # and support chosen from the two alternating supports.
    odd=tuple(int(i%2==0) for i in range(m))
    even=tuple(int(i%2==1) for i in range(m))
    if m%2==0:
        mixture=((Q(1,2),odd),(Q(1,2),even))
    else:
        mixture=((p[0],odd),(1-p[0],even))
    for i in range(m):
        expected=sum(prob*support[i] for prob,support in mixture)
        check(expected==p[i],(m,a,i,'barycenter'))
    for prob,b in mixture:
        if prob>0:
            check(active(b),(m,a,b,'support contacts'))
    expected_norm=sum(prob*sum(b) for prob,b in mixture)
    check(expected_norm-sum(x*x/a for x in p)==r,(m,a,'barycentric-radius'))
    check(len(p)==m and all(0<=x<=1 for x in p),(m,a,'coordinates'))
    return len(S),ncontacts


def run():
    configurations=0; vertex_checks=0
    for m in range(2,19):
        for a in range(1,min(21,m+8)):
            num, nc=test_exact(m,a)
            vertex_checks+=num
            configurations+=1
    print(f'EXACT PASS: {configurations} configurations; {vertex_checks} support-distance comparisons; {checks} exact assertions')
    try:
        import numpy as np
        from scipy.optimize import minimize
    except ImportError:
        print('SciPy unavailable; numerical optimization omitted.')
        return
    nopt=0
    for m in range(2,12):
        for a in (1,2,3,m,m+1,m+2,2*m):
            p,r,_,_=candidate(m,a)
            p=np.array([float(x) for x in p])
            x0=np.full(m,0.5)
            constraints=[{'type':'ineq','fun':lambda x,i=i:1-x[i]-x[i+1]} for i in range(m-1)]
            constraints += [{'type':'ineq','fun':lambda x,i=i:x[i]} for i in range(m)]
            result=minimize(lambda x:sum((x-a/2)**2),x0, method='SLSQP',constraints=constraints,
                 bounds=[(0,1)]*m,options={'ftol':1e-9,'maxiter':500})
            check(result.success or max(abs(result.x-p))<1e-6,(m,a,result.message))
            check(max(abs(result.x-p))<1e-6,(m,a,'numeric QP',result.x,p))
            nopt+=1
    print(f'NUMERIC QP PASS: {nopt} independent SLSQP solutions matched exact centers')

if __name__=='__main__':
    run()
