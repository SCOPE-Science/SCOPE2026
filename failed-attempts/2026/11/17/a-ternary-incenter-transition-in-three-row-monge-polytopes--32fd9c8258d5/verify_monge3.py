"""Independent rational and linear-programming checks for three-row Monge inballs.

Requires Python, scipy and numpy.  The theorems are proved separately;
finite verification is not a proof for unrestricted column counts.
"""
from fractions import Fraction as F
from math import floor, sqrt
import numpy as np
from scipy.optimize import linprog

assertions=0

def chk(predicate, context=''):
    global assertions
    assertions+=1
    if not predicate: raise AssertionError(context)

def dual(q):
    u=[min(2*j,q-j) for j in range(q+1)]
    v=[min(j,2*(q-j)) for j in range(q+1)]
    chk(u[0]==u[-1]==v[0]==v[-1]==0, f'end dual {q}')
    for j in range(1,q+1):
        du=u[j]-u[j-1];dv=v[j]-v[j-1]
        for a in (-du,du-dv,dv):
            chk(a<=1,f'dual bound q={q} j={j} coeff={a}')
    chk(sum(u)+sum(v)==2*(q*q//3), f'dual objective q={q}')
    return u,v

def zcenter(q,a,b):
    z=[]
    for j in range(1,q+1):
        h=max(F(0),a-j,j-b)
        z.extend((h+j-a,h,h+b-j))
    return z

def constraints(q,z):
    for j in range(q):
        for i in range(3): chk(z[3*j+i]>=0,f'negative z q{q} j{j} i{i}')
    for j in range(q-1):
        for i in (0,1):
            A=z[3*(j+1)+i]-z[3*j+i]+z[3*j+i+1]-z[3*(j+1)+i+1]
            chk(A==1,f'contrast q{q} j{j} i{i} {A}')
    chk(sum(z)==2*(q*q//3), f'mass q{q} got {sum(z)}')

def representative(q):
    m,r=divmod(q,3)
    if r==0: return F(m), F(2*m)
    if r==1: return F(m+1), F(2*m+1)
    return F(m+1), F(2*m+2)

def lp_check(q):
    # Minimize sum of Z subject to adjacent Monge contrasts >= 1, and Z>=0.
    c=np.ones(3*q)
    A=[]; b=[]
    for j in range(q-1):
        for i in (0,1):
            row=np.zeros(3*q)
            # A=z(i,j+1)+z(i+1,j)-z(i,j)-z(i+1,j+1)>=1
            row[3*(j+1)+i]=-1
            row[3*j+i+1]=-1
            row[3*j+i]=1
            row[3*(j+1)+i+1]=1
            A.append(row);b.append(-1)
    res=linprog(c, A_ub=np.array(A),b_ub=np.array(b),bounds=(0,None),method='highs')
    chk(res.success,f'LP failure q{q}')
    chk(abs(res.fun-2*(q*q//3))<1.e-7,f'LP objective q{q}, got {res.fun}')
    return res.fun

for q in range(3,37):
    dual(q)
    a,b=representative(q)
    z=zcenter(q,a,b)
    constraints(q,z)
    m,r=divmod(q,3)
    if r==0:
        for aa in (F(m),F(m,1)+F(1,2),F(m+1)):
            for bb in (F(2*m),F(2*m,1)+F(1,2),F(2*m+1)):
                constraints(q,zcenter(q,aa,bb))
        chk(zcenter(q,F(m),F(2*m))!=zcenter(q,F(m+1),F(2*m)), 'a freedom')
        chk(zcenter(q,F(m),F(2*m))!=zcenter(q,F(m),F(2*m+1)), 'b freedom')
    L=sqrt(1-1/(3*q))
    radius=1/(3*q*L+4*(q*q//3))
    center=np.array([float(radius*L+2*radius*zi) for zi in z]).reshape(q,3).T
    chk(abs(center.sum()-1)<1e-11, f'sum c q{q}')
    chk(center.min()>=radius*L-1e-12,'coordinate facet')
    for j in range(q-1):
        for i in (0,1):
            slack=center[i,j+1]+center[i+1,j]-center[i,j]-center[i+1,j+1]
            chk(abs(slack-2*radius)<1e-11,'Monge ball distance')
    # First 16-column linear programs are wholly independent from explicit dual.
    if q<=16: lp_check(q)

print('PASS',assertions,'assertions; exact rational feasibility and dual bounds for 3<=q<=36; independent scipy LP for 3<=q<=16; all center candidates and ball constraints verified')
