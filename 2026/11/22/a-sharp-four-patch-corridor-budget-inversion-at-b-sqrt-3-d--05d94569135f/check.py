"""Reproduce symbolic resolvent identities and invasion-window examples.
Requires Python 3 and SymPy; all algebraic equalities are exact.
"""
import sympy as sp

z=sp.symbols('z',positive=True)

def laplacian(n,edges):
    L=sp.zeros(n)
    for i,j in edges:
        L[i,i]+=1; L[j,j]+=1
        L[i,j]-=1; L[j,i]-=1
    return L

def rooted_response(n,edges,root):
    L=laplacian(n,edges)
    E=len(edges)
    return sp.factor((z*sp.eye(n)+L/E).inv()[root,root])

path=[(0,1),(0,3),(1,2)]
diamond=[(0,1),(0,2),(0,3),(1,2),(2,3)]
F_p=rooted_response(4,path,0)
F_d=rooted_response(4,diamond,0)
assert sp.simplify(F_p-(3*z+1)*(9*z*z+9*z+1)/(z*(3*z+2)*(9*z*z+12*z+2)))==0
assert sp.simplify(F_d-(5*z+1)/(z*(5*z+4)))==0
assert sp.simplify(F_p-F_d+3*(3*z*z-1)/((3*z+2)*(5*z+4)*(9*z*z+12*z+2)))==0
rp=sp.factor(1/F_p-z)
rd=sp.factor(1/F_d-z)
assert sp.simplify(rp-3*z*(6*z*z+6*z+1)/((3*z+1)*(9*z*z+9*z+1)))==0
assert sp.simplify(rd-3*z/(5*z+1))==0
assert sp.simplify(rp-rd-3*z*z*(3*z*z-1)/((3*z+1)*(5*z+1)*(9*z*z+9*z+1)))==0
assert sp.simplify((rp-rd).subs(z,1/sp.sqrt(3)))==0

p3=[(0,1),(0,2)]
k3=[(0,1),(0,2),(1,2)]
Fc=rooted_response(3,p3,0)
Fe=rooted_response(3,p3,1)
Ft=rooted_response(3,k3,0)
assert sp.simplify(Fc-Fe+2/((2*z+1)*(2*z+3)))==0
assert sp.simplify(Fc-Ft+2/(3*(z+1)*(2*z+3)))==0
assert sp.simplify(Fe-Ft-2*(z+2)/(3*(z+1)*(2*z+1)*(2*z+3)))==0

# Two rational parameter settings yield opposite invasion decisions.
examples=[(sp.Rational(1,2),sp.Rational(107,250),'path'),
          (sp.Rational(1),sp.Rational(51,100),'diamond')]
for d,r,winner in examples:
    P=rp.subs(z,d)
    D=rd.subs(z,d)
    assert (P<r<D) if winner=='path' else (D<r<P)
    for edges,expected in [(path,winner=='path'),(diamond,winner=='diamond')]:
        M=sp.diag(r,-d,-d,-d)-laplacian(4,edges)/len(edges)
        # Inertia via shifted positive definite matrix and Schur rank-one condition.
        Q=sp.eye(4)*d+laplacian(4,edges)/len(edges)
        assert all(x>0 for x in [Q[:i,:i].det() for i in range(1,5)])
        u=r+d
        x=sp.simplify(u*Q.inv()[0,0]-1)
        assert (x>0)==expected

# Independent numerical spectral check (not a substitute for the exact proof).
import numpy as np
for z0 in [0.08,0.25,0.5,sp.sqrt(3)/3,0.7,1.0,2.0,6.0]:
    delta=float((rp-rd).subs(z,z0))
    for d0 in [float(z0)]:
        g=1.0
        values=[]
        for edges in [path,diamond]:
            L=np.array(laplacian(4,edges),dtype=float)/len(edges)
            A=np.diag([g,-d0,-d0,-d0])-L
            values.append(np.linalg.eigvalsh(A)[-1])
        # Compare thresholds, not Perron growth rankings at arbitrary g.
        for edges,resp in [(path,F_p),(diamond,F_d)]:
            t=float((1/resp-z).subs(z,z0))
            L=np.array(laplacian(4,edges),dtype=float)/len(edges)
            A=np.diag([t,-d0,-d0,-d0])-L
            assert abs(np.linalg.eigvalsh(A)[-1])<1e-10

print('PASS: exact 4-node Green functions, sharp crossing, 3-node minimality, rational invasion windows, numerical eigenvalue boundaries')
