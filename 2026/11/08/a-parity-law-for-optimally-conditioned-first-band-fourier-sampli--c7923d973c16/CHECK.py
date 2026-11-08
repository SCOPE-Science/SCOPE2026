"""Independent exact-count and direct-character checks for ternary-sphere sampling."""
import cmath
import itertools
import math
import numpy as np
from fractions import Fraction


def counts(d):
    return [sum(math.comb(d,w)*2**w for w in range(j,d+1,3)) for j in range(3)]

def scalars(d,j):
    A=counts(d); B=counts(d-1); C=counts(d-2)
    g=Fraction(B[j]-B[(j-1)%3],A[j])
    h=Fraction(C[j]-2*C[(j-1)%3]+C[(j-2)%3],A[j])
    return g,h

def eigenvalues(d,j):
    g,h=map(float,scalars(d,j))
    B=np.array([[1, math.sqrt(2*d)*g],[math.sqrt(2*d)*g,1+g+2*(d-1)*h]],float)
    return sorted([1-g]*d+[1+g-2*h]*(d-1)+list(np.linalg.eigvalsh(B)))

def direct(d,j):
    xs=np.array([x for x in itertools.product(range(3),repeat=d) if sum(z!=0 for z in x)%3==j],dtype=np.int64)
    omega=np.exp(2j*np.pi/3)
    V=np.ones((len(xs),2*d+1),dtype=np.complex128)
    for i in range(d):
        V[:,2*i+1]=omega**xs[:,i]
        V[:,2*i+2]=omega**(-xs[:,i])
    return sorted(np.linalg.eigvalsh(V.conj().T@V/len(xs)).real)

def condition(d,j):
    e=eigenvalues(d,j)
    return float('inf') if e[0]<1e-10 else e[-1]/e[0]

def predicted(d):
    X=3**(d//2)
    if d%2==0:
        if d%4==0:
            return 0,(X+3)/(X+2-2*d)
        return 0,(X-2+2*d)/(X-3)
    sign=(-1)**((d-1)//2)
    R=math.sqrt(8*d+1)
    return 1,(2*X+sign+R)/(2*X+sign-R)

def main():
    assertions=0
    for d in range(4,9):
        for j in range(3):
            a=np.array(eigenvalues(d,j)); b=np.array(direct(d,j))
            assert len(a)==len(b)==2*d+1
            assert np.max(np.abs(a-b))<3e-12,(d,j,a,b)
            assert len([x for x in itertools.product(range(3),repeat=d) if sum(z!=0 for z in x)%3==j])==counts(d)[j]
            assertions+=len(a)+1
    for d in range(4,45):
        best=min(range(3),key=lambda j:condition(d,j))
        j,c=predicted(d)
        assert best==j,(d,best,j)
        assert math.isclose(condition(d,j),c,rel_tol=2e-10,abs_tol=2e-10),(d,c,condition(d,j))
        for z in range(3):
            assert min(eigenvalues(d,z))>=-2e-12,(d,z)
        assertions+=5
    # Exact sample moments and two-level collapse for optimal even dimensions.
    for d in range(4,100,2):
        g,h=scalars(d,0)
        assert g==h,(d,g,h)
        assertions+=1
    print('CHECK_OK assertions=',assertions,'max_d_direct=8 max_d_formulas=44')

if __name__=='__main__':
    main()
