"""Exact rational checks for the frequency-dependent loop-area theorem.
Run: python3 checker.py. No third-party packages are required.
"""
from fractions import Fraction as F
from itertools import combinations
from math import pi, cos, sin, sqrt


def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out


def area_polynomial(t,q,c):
    assert len(t)==len(q)==len(c)
    n=len(t); ans=[F(0)]*max(1,n-1)
    for i,j in combinations(range(n),2):
        a=(q[i]*c[j]-q[j]*c[i])*(t[j]-t[i])
        p=[F(1)]
        for k in range(n):
            if k not in (i,j): p=mul(p,[F(1),t[k]**2])
        for k,v in enumerate(p): ans[k]+=a*v
    return ans


def evalpoly(p,x):
    out=F(0)
    for c in reversed(p):out=out*x+c
    return out


def detrank(M):
    mat=[list(map(F,row)) for row in M]
    m=len(mat);n=len(mat[0]); piv=[];r=0
    for j in range(n):
        k=next((i for i in range(r,m) if mat[i][j]),None)
        if k is None: continue
        mat[k],mat[r]=mat[r],mat[k]
        d=mat[r][j]
        mat[r]=[x/d for x in mat[r]]
        for i in range(m):
            if i!=r and mat[i][j]:
                z=mat[i][j];mat[i]=[a-z*b for a,b in zip(mat[i],mat[r])]
        piv.append(j);r+=1
        if r==m:break
    return r


def amplitude_phase(omega,t,weights):
    # z_i(t) = alpha_i cos(omega*t) + beta_i sin(omega*t).
    a=sum(float(w)/(1+(omega*float(x))**2) for w,x in zip(weights,t))
    b=sum(float(w)*omega*float(x)/(1+(omega*float(x))**2) for w,x in zip(weights,t))
    return a,b


def quadrature(omega,t,q,c,N=2000):
    aq,bq=amplitude_phase(omega,t,q)
    ac,bc=amplitude_phase(omega,t,c)
    step=2*pi/N
    # dC = (-ac*sin(theta) +bc*cos(theta)) dtheta
    return step*sum((aq*cos(step*k)+bq*sin(step*k)) *
        (-ac*sin(step*k)+bc*cos(step*k)) for k in range(N))


def formula(omega,t,q,c):
    p=area_polynomial(t,q,c)
    numer=0.0
    for z in reversed(p): numer=numer*omega*omega+float(z)
    den=1.
    for x in t: den*=1+(omega*float(x))**2
    return pi*omega*numer/den


def run():
    checks=0
    # Two modes cannot reverse orientation (for a non-degenerate pair).
    for t in ([F(1),F(2)], [F(1),F(10)], [F(2),F(9)]):
        q=[F(1),F(2)];c=[F(3),F(1)]
        p=area_polynomial(t,q,c)
        assert len(p)==1 and p[0]!=0; checks+=1
    t3=list(map(F,[1,2,4]));q3=[F(1),F(1,2),F(1)]
    c3=[F(1,2),F(1),F(1,2)]
    p3=area_polynomial(t3,q3,c3)
    assert p3==[F(-3,4),F(21,2)];checks+=1
    assert evalpoly(p3,F(1,14))==0;checks+=1
    assert evalpoly(p3,F(0))<0 and evalpoly(p3,F(1))>0;checks+=1
    t4=list(map(F,[1,2,3,4]));q4=[F(1)]*4
    c4=[F(469,760),F(373,475),F(519,3800),F(1)]
    p4=area_polynomial(t4,q4,c4)
    assert p4==[F(1),F(-5,2),F(1)],p4;checks+=1
    assert evalpoly(p4,F(1,2))==0 and evalpoly(p4,F(2))==0;checks+=1
    assert evalpoly(p4,F(1,4))>0 and evalpoly(p4,F(1))<0 and evalpoly(p4,F(3))>0;checks+=1
    # Exact surjectivity matrices for a family of distinct positive time constants.
    for n in range(2,11):
        t=list(map(F,range(1,n+1)));q=[F(1)]*n
        cols=[]
        for j in range(n):
            c=[F(0)]*n;c[j]=F(1)
            cols.append(area_polynomial(t,q,c))
        M=[[cols[j][i] for j in range(n)] for i in range(n-1)]
        assert detrank(M)==n-1,(n,M)
        checks+=1
        assert area_polynomial(t,q,q)==[F(0)]*(n-1);checks+=1
    # Independent numerical integration of the signed loop and exact polynomial.
    for t,q,c in [(t3,q3,c3),(t4,q4,c4),([F(1),F(3)],[F(2),F(1)],[F(1),F(3)])]:
        for omega in [0.1,0.3,0.6,1.,2.,3.,10.]:
            direct=quadrature(omega,t,q,c)
            algebraic=formula(omega,t,q,c)
            assert abs(direct-algebraic)<5e-12,(direct,algebraic)
            checks+=1
    print('PASS',checks,'exact rational assertions / numerical quadrature comparisons')
    print('three-mode numerator',p3,'root squared',F(1,14))
    print('four-mode numerator',p4,'roots squared',F(1,2),F(2))

if __name__=='__main__':run()
