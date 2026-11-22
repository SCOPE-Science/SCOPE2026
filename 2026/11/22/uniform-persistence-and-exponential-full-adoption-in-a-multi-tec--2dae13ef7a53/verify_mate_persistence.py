"""Exact transition checks and reproducible numerical stress tests for the MATE persistence theorem.

The analytic inequalities are established in the accompanying proof; finite checks
support the matrix orientation, path length and indexing, not the infinite theorem.
"""
from fractions import Fraction as Q
from itertools import product
import random


def transition(gamma, delta, opinion):
    m = len(gamma)
    P = [[Q(0) for _ in range(2*m)] for _ in range(2*m)]
    for k in range(m):
        P[k][k] = 1-delta[k]
        P[m+k][k] = delta[k]
        P[m+k][m+k] = 1-sum((gamma[r]*opinion[r] for r in range(m) if r!=k),Q(0))
        for r in range(m):
            if r!=k:
                P[r][m+k] = gamma[r]*opinion[r]
    assert all(sum(P[i][j] for i in range(2*m))==1 for j in range(2*m))
    return P


def mm(A,B):
    size=len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(size)),Q(0))
             for j in range(size)] for i in range(size)]


def test_four_steps():
    rng = random.Random(173)
    checks=0
    for m in range(2,7):
        for rep in range(35):
            delta=[Q(rng.randint(1,8),10) for _ in range(m)]
            gamma=[Q(rng.randint(1,5),10*m) for _ in range(m)]
            xlo=Q(1,9)
            op=[[xlo+Q(rng.randint(0,7),10)*(1-xlo) for _ in range(m)] for _ in range(4)]
            q=min(min(delta),min(gamma)*xlo)
            P=[transition(gamma,delta,v) for v in op]
            F=mm(P[3],mm(P[2],mm(P[1],P[0])))
            for k,j in product(range(m),range(2*m)):
                assert F[k][j]>=q**4,(m,rep,k,j,F[k][j],q**4)
                checks+=1
    return checks


def simulation_check():
    # Two communities with strictly positive directed reciprocal contacts.
    # Three technologies, nonzero opinion/adoption feedback, a single initial seed.
    n,m=2,3
    W=[[0.0,1.0],[1.0,0.0]]
    lam,xi,p=1/3,1/3,1/2
    beta,gamma,delta=1/12,1/8,1/4
    s=[2/3,1.0]
    a=[[1/3,0.0,0.0],[0.0]*m]
    d=[[0.0]*m for i in range(n)]
    x=[[p]*m for i in range(n)]
    b0=1/3
    xlo=(1-lam-xi)*p
    q=min(delta,gamma*xlo)
    eta=q**4
    c=beta*xlo*eta*1.0
    B=b0*c**(n-1)
    rho=beta*xlo*eta*B
    state=[]
    for t in range(70):
        b=[1-s[i] for i in range(n)]
        state.append((s[:],[v[:] for v in a],[v[:] for v in d],[v[:] for v in x],b))
        aa=[[0.0]*m for i in range(n)]
        dd=[[0.0]*m for i in range(n)]
        ss=[0.0]*n
        xx=[[0.0]*m for i in range(n)]
        for i in range(n):
            pressure=[sum(W[i][j]*a[j][k] for j in range(n)) for k in range(m)]
            total=sum(beta*x[i][k]*pressure[k] for k in range(m))
            ss[i]=s[i]*(1-total)
            for k in range(m):
                aa[i][k]=(1-delta)*a[i][k]+s[i]*beta*x[i][k]*pressure[k]+gamma*x[i][k]*sum(d[i][r] for r in range(m) if r!=k)
                dd[i][k]=delta*a[i][k]+d[i][k]*(1-sum(gamma*x[i][r] for r in range(m) if r!=k))
                xx[i][k]=(1-lam-xi)*p+lam*sum(W[i][j]*x[j][k] for j in range(n))+xi*pressure[k]
        s,a,d,x=ss,aa,dd,xx
        for i in range(n):
            assert abs(s[i]+sum(a[i])+sum(d[i])-1)<2e-13
            assert min(x[i])>=xlo-1e-13
    tests=0
    for t in range(1,len(state)-4):
        for i,k in product(range(n),range(m)):
            assert state[t+4][1][i][k] +1e-13 >= eta*state[t][4][i]
            tests+=1
    for t in range(11,len(state)-1):
        for i in range(n):
            assert state[t][4][i]+1e-13>=B
            assert min(state[t][1][i])+1e-13>=eta*B
            assert state[t+1][0][i] <= (1-rho)*state[t][0][i]+1e-13
            tests+=3
    return tests, state[-1][0], (eta,B,rho)

if __name__ == '__main__':
    exact=test_four_steps()
    numeric,ending,constants=simulation_check()
    print('PASS: exact four-step matrix inequalities:',exact)
    print('PASS: numerical MATE state/persistence/decay comparisons:',numeric)
    print('Final susceptible fractions:',ending)
    print('Certified conservative eta, B, rho:',constants)
