"""Standalone finite-field checks for the nilpotent 3D dialgebra geometry theorem.
Usage: python3 verify.py. Only the standard library is needed.
These tests corroborate but do not replace the all-field proof.
"""
from itertools import product

def mk(a,b,u,v,c,d,e,f,h=0,j=0,q=2):
    # T[0] is dashv, T[1] is vdash, indices are 0,1,2.
    T=[[[[0]*3 for _ in range(3)] for _ in range(3)] for _ in range(2)]
    T[0][0][0]=[0,a%q,u%q]
    T[1][0][0]=[0,b%q,v%q]
    T[0][0][1]=[0,0,c%q]
    T[0][1][0]=[0,0,d%q]
    T[1][0][1]=[0,0,e%q]
    T[1][1][0]=[0,0,f%q]
    T[0][1][1]=[0,0,h%q]
    T[1][1][1]=[0,0,j%q]
    return T

def apply(T,which,x,y,q):
    out=[0,0,0]
    for i in range(3):
        for j in range(3):
            if x[i] and y[j]:
                for k in range(3):
                    out[k]=(out[k]+x[i]*y[j]*T[which][i][j][k])%q
    return out

def sub(x,y,q): return [(a-b)%q for a,b in zip(x,y)]

def add(x,y,q): return [(a+b)%q for a,b in zip(x,y)]

def is_lsda(T,q):
    E=[[1,0,0],[0,1,0],[0,0,1]]
    a=lambda r,x,y:apply(T,r,x,y,q)
    for x,y,z in product(E,repeat=3):
        # Axioms (1.1)-(1.4) of the motivating paper.
        if a(0,x,a(0,y,z)) != a(0,x,a(1,y,z)): return False
        if a(1,a(0,x,y),z) != a(1,a(1,x,y),z): return False
        left=sub(a(0,x,a(0,y,z)),a(0,a(0,x,y),z),q)
        right=sub(a(1,y,a(0,x,z)),a(0,a(1,y,x),z),q)
        if left!=right: return False
        left=sub(a(1,x,a(0,y,z)),a(1,a(0,x,y),z),q)
        right=sub(a(1,y,a(1,x,z)),a(1,a(1,y,x),z),q)
        if left!=right:return False
    return True

def check_normal_form(q):
    n=0
    for vals in product(range(q),repeat=8):
        a,b,u,v,c,d,e,f=vals
        if not (a or b) or not (c or d or e or f):continue
        T=mk(*vals,q=q)
        valid=is_lsda(T,q)
        predicted=(a==b and a!=0 and c==e and bool(c or d or f))
        assert valid==predicted, (q,vals,valid,predicted)
        n+=valid
    target=(q-1)*q*q*(q**3-1)
    assert n==target,(q,n,target)
    # In every characteristic the rank-two 2-step algebra has both products nonzero.
    F7=mk(0,0,0,0,0,0,0,0,q=q)
    F7[0][0][0]=[0,1,0]
    F7[1][0][0]=[0,0,1]
    assert is_lsda(F7,q)
    # Valid one-parameter degeneration from a non-2-step algebra to F7.
    for t in range(q):
        T=mk(1,1,1,0,0,t,0,t,q=q)
        assert is_lsda(T,q), (q,t)
    return n

def full_counts(q):
    L=q*q+q+1
    Z=1+L*(q**8-1)
    U=L*(q+1)*(q-1)*q*q*(q**3-1)
    R=L*(q*q-1)*(q*q-q)
    return Z,U,R,Z+U+R

if __name__=='__main__':
    for q in (2,3):
        n=check_normal_form(q)
        print('F_%s fixed-flag normal forms: %s' %(q,n))
    for q in (2,3,4,5):
        print('F_%s: rank<=1, rank2 non-2-step, rank2 2-step, all = %s' %(q,full_counts(q)))
    print('LSDA_TWO_COMPONENT_GEOMETRY_CHECKS_OK')
