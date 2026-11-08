#!/usr/bin/env python3
"""Standalone numerical checks of a Euclidean inradius theorem.

All authoritative claims are established by the accompanying proof; these
finite checks test support functions independently on polynomial Newton summands.
Requires Python 3 and scipy for the optional linear-programming comparison.
"""
import math
from decimal import Decimal, localcontext
from itertools import product

def supports(n, d):
    # Each summand is the Newton simplex of
    # 1+y_j+y_j*y_(j+1)+...+y_j*...*y_(j+k-1).
    atoms=[]
    for k in range(1,d+1):
        for j in range(n-k+1):
            vertices=[]
            for t in range(k+1):
                vertices.append(tuple(int(j<=i<j+t) for i in range(n)))
            atoms.append(vertices)
    return atoms

def h(atoms, direction):
    return sum(max(sum(a*b for a,b in zip(vertex,direction)) for vertex in summand)
               for summand in atoms)

def facets(n,d):
    for i in range(n):
        a=[0]*n; a[i]=1;yield ('upper',i),tuple(a),1
        yield ('lower',i),tuple(-v for v in a),1
    for ell in range(1,d):
        for i in range(n-ell):
            a=[0]*n;a[i]=-1;a[i+ell]=1
            yield ('gap',i,ell),tuple(a),math.sqrt(2)

def radius(n,d):
    cumulative=sum(min(d,j) for j in range(1,n))
    return min(d/2, (d+cumulative)/(2+(n-1)*math.sqrt(2)))

def center(n,d,r):
    w=[0]*n
    for k in range(1,d+1):
        for j in range(n-k+1):
            for i in range(j,j+k):w[i]+=1
    b=[min(d,n-i-1) for i in range(n-1)]
    x=[w[0]-r]
    for i in range(n-1):x.append(min(w[i+1]-r,x[-1]+b[i]-math.sqrt(2)*r))
    return x,w,b

def exercise():
    assertions=0
    for n in range(3,17):
        for d in range(3,n+1):
            atoms=supports(n,d)
            r=radius(n,d)
            x,w,b=center(n,d,r)
            assert min(w)==d;assert abs(w[0]-d)<1e-12
            assertions+=2
            assert min(x)>=r-1e-9
            assertions+=1
            assert (math.sqrt(2)*r > (d-1)/2)
            assertions+=1
            for label,a,norm in facets(n,d):
                support=h(atoms,a)
                slack=support-sum(t*v for t,v in zip(a,x))-r*norm
                assert slack>=-1e-8,(n,d,label,slack)
                assertions+=1
            # Compare every individual long-difference support with the closed identity.
            for ell in range(2,d):
                for i in range(n-ell):
                    a=[0]*n;a[i]=-1;a[i+ell]=1
                    h_direct=h(atoms,a)
                    h_formula=sum(b[i:i+ell])-ell*(ell-1)//2
                    assert h_direct==h_formula
                    assertions+=1
            short=(d+sum(b))/(2+(n-1)*math.sqrt(2)) < d/2
            if short:
                assert abs(x[-1]-r)<1e-8
                tangencies=[]
                for label,a,norm in facets(n,d):
                    if abs(h(atoms,a)-sum(t*v for t,v in zip(a,x))-r*norm)<1e-8:
                        tangencies.append(label)
                assert set(tangencies)=={('upper',0),('lower',n-1)}|{('gap',i,1) for i in range(n-1)},(n,d,tangencies)
                assertions+=2
            else:
                assert abs(r-d/2)<1e-10
                assertions+=1
    print('Direct Newton-simplex support checks:',assertions)
    try:
        import numpy as np
        from scipy.optimize import linprog
    except ImportError:
        print('scipy unavailable: skipped independent linear programs')
        return
    compared=0
    strict_cases=0
    for n in range(3,13):
        for d in range(3,n+1):
            atoms=supports(n,d)
            A=[];rhs=[]
            for label,a,norm in facets(n,d):
                A.append(list(a)+[norm]);rhs.append(h(atoms,a))
            obj=[0]*n+[-1]
            ans=linprog(obj,A_ub=np.array(A),b_ub=np.array(rhs),bounds=[(None,None)]*(n+1),method='highs')
            assert ans.success,(n,d,ans.message)
            assert abs(ans.x[-1]-radius(n,d))<2e-7,(n,d,ans.x[-1],radius(n,d))
            compared+=1
            if abs(radius(n,d)-d/2)<1e-9:
                # Strict feasibility in the affine space of centers with
                # the first and last coordinates fixed to half-width.
                rows=[]; upper=[]
                for lab,a,norm in facets(n,d):
                    if lab in {('upper',0),('lower',0),('upper',n-1),('lower',n-1)}:
                        continue
                    rows.append(list(a)+[1.0])
                    upper.append(h(atoms,a)-norm*d/2)
                margin=linprog([0]*n+[-1], A_ub=np.array(rows),b_ub=np.array(upper),
                               A_eq=np.array([[1.0 if j==i else 0.0 for j in range(n+1)]
                                              for i in (0,n-1)]),
                               b_eq=[d/2,d/2],
                               bounds=[(None,None)]*n+[(0,None)],method='highs')
                assert margin.success,(n,d,margin.message)
                assert margin.x[-1]>1e-7,(n,d,margin.x[-1])
                strict_cases+=1
    print('Independent linear-program optima:',compared)
    print('Positive relative-interior margins in long regime:',strict_cases)

if __name__=='__main__':exercise()
