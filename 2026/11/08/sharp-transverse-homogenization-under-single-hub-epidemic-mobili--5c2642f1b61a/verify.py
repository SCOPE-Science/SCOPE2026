"""Exact-rational verification of the sharp transverse epidemic relaxation theorem.
Requires Python 3 and sympy. All algebraic checks use integer or rational arithmetic.
"""
import random
from fractions import Fraction
import sympy as s

def matrix(m, q, seed):
    rng=random.Random(seed)
    B=s.zeros(m)
    w=(1-q)/s.Integer(4*m)
    for i in range(m):
        for j in range(i+1,m):
            z=w*s.Rational(rng.randrange(0,5),4)
            B[i,j]=B[j,i]=z
    for i in range(m):
        B[i,i]=(1-q)-sum(B[i,j] for j in range(m) if i!=j)
    assert all(t>=0 for t in B)
    Phi=B.row_join(s.ones(m,1)*q)
    Phi=Phi.col_join((s.ones(1,m)*q).row_join(s.Matrix([[1-m*q]])))
    assert Phi==Phi.T and all(sum(Phi[i,j] for j in range(m+1))==1 for i in range(m+1))
    return Phi,B

def check(m,q,beta,gamma,zeta,seed):
    n=m+1
    Phi,B=matrix(m,q,seed)
    D=s.diag(*([s.Integer(1)]*m+[zeta]))
    L=beta*Phi*D*Phi-gamma*s.eye(n)
    P=s.eye(m)-s.ones(m,m)/m
    Q=s.zeros(m,n)
    Q[:m,:m]=P
    # The centered leaf component obeys a closed exact equation,
    # even if the epidemic's full Perron mode is growing.
    assert Q*L==(beta*B**2-gamma*s.eye(m))*Q
    assert P*B==B*P
    C=s.Matrix.hstack(*[s.eye(m)[:,i]-s.eye(m)[:,m-1] for i in range(m-1)])
    for k in range(m-1):
        v=C[:,k].col_join(s.zeros(1,1))
        assert L*v==(beta*B**2*C[:,k]-gamma*C[:,k]).col_join(s.zeros(1,1))
    # The quotient of the full system, separately from the transverse modes.
    A=s.Matrix([[1-q,q],[m*q,1-m*q]])
    K=s.Matrix([[1]*m+[0],[0]*m+[1]]).T
    assert L*K==K*(beta*A*s.diag(1,zeta)*A-gamma*s.eye(2))
    # Spectral bound: every eigval on U has gamma-beta*mu^2 decay,
    # and Gershgorin/Symmetric row sum gives |mu|<=1-q.
    # Exact symmetric diagonal dominance certifies the Loewner bounds.
    assert all((1-q)-sum(abs(B[i,j]) for j in range(m))==0 for i in range(m))
    assert all((1-q)+B[i,i]>=sum(abs(B[i,j]) for j in range(m) if j!=i) for i in range(m))
    return 1

def endpoints(m,q,beta,gamma):
    P=s.ones(m,m)/m
    D=s.eye(m)
    worst=(1-q)*D
    best=(1-q)*P
    for B,exp in [(worst,-gamma+beta*(1-q)**2),(best,-gamma)]:
        v=s.Matrix([s.Integer(1),-s.Integer(1)]+[s.Integer(0)]*(m-2))
        assert B**2*v*beta-gamma*v==exp*v
    for j in range(0,13):
        a=s.Rational(j,12)
        B=(1-q)*(a*D+(1-a)*P)
        v=s.Matrix([s.Integer(1),-s.Integer(1)]+[s.Integer(0)]*(m-2))
        assert beta*B**2*v-gamma*v==(-gamma+beta*(1-q)**2*a**2)*v
    return 15

def main():
    m=3; q=s.Rational(1,4); beta=s.Rational(2,3); gamma=s.Integer(1); zeta=s.Integer(5)
    A=s.Matrix([[1-q,q],[m*q,1-m*q]])
    Q=beta*A*s.diag(1,zeta)*A/gamma
    assert sorted(Q.eigenvals())==[0,s.Rational(4,3)]
    assert gamma-beta*(1-q)**2==s.Rational(5,8)
    c=0
    for m in range(2,8):
        for q in [s.Rational(1,2*m),s.Rational(1,m+1),s.Rational(1,m)]:
            for beta,gamma in [(s.Rational(1,2),s.Integer(1)),(s.Rational(2,3),s.Integer(1))]:
                for zeta in [s.Integer(3),s.Integer(5)]:
                    c+=check(m,q,beta,gamma,zeta,c+23)
            c+=endpoints(m,q,s.Rational(2,3),s.Integer(1))
    print('VERIFY_OK',c,'exact rational families; every endpoint and 13 interpolations')
if __name__=='__main__':main()
