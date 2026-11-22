"""Independent rational checks for a three-bath ferromagnetic Ising triangle.

Run: python3 verify.py (requires sympy).
The general proof is analytic; the finite tests detect normalization/sign errors.
"""
from fractions import Fraction as F
from itertools import product
from sympy import Rational, Matrix, zeros

STATES=list(product((-1,1),repeat=3))

def direct(a,b,c):
    ts=(Rational(a.numerator,a.denominator),Rational(b.numerator,b.denominator),Rational(c.numerator,c.denominator))
    L=zeros(8,8)
    for col,s in enumerate(STATES):
        for i in range(3):
            h=sum(s[j] for j in range(3) if j!=i)
            rate=(1-ts[i]*s[i]*h/2)/2
            new=list(s);new[i]=-new[i]
            row=STATES.index(tuple(new))
            L[row,col]+=rate
            L[col,col]-=rate
    M=L.copy(); M[7,:]=Matrix([[1]*8]); rhs=Matrix([0]*7+[1])
    pi=M.inv()*rhs
    cc={(i,j):sum(pi[k]*s[i]*s[j] for k,s in enumerate(STATES)) for i,j in [(0,1),(0,2),(1,2)]}
    flows=[]
    for i in range(3):
        total=0
        for k,s in enumerate(STATES):
            h=sum(s[j] for j in range(3) if j!=i)
            rate=(1-ts[i]*s[i]*h/2)/2
            dE=2*s[i]*h # J=1
            total+=pi[k]*rate*dE
        flows.append(total)
    return cc,flows, pi, L

def formula(a,b,c):
    d=32-a*b*c-2*(a*b+a*c+b*c)
    corr={
        (0,1):(c+4)*(a*b+2*a+2*b)/d,
        (0,2):(b+4)*(a*c+2*a+2*c)/d,
        (1,2):(a+4)*(b*c+2*b+2*c)/d,
    }
    q=[2*((b-a)*(c+4)+(c-a)*(b+4))/d,
       2*((a-b)*(c+4)+(c-b)*(a+4))/d,
       2*((a-c)*(b+4)+(b-c)*(a+4))/d]
    return corr,q

def test():
    vals=[F(1,8), F(1,3), F(1,2), F(3,4), F(7,8)]
    cnt=0
    for a,b,c in product(vals,repeat=3):
        dc,df,pi,L=direct(a,b,c)
        fc,ff=formula(a,b,c)
        assert dc==fc, (a,b,c,dc,fc)
        assert df==ff, (a,b,c,df,ff)
        assert sum(df)==0
        assert all(z>0 for z in pi)
        assert all(z==0 for z in L*pi)
        cnt+=1
    print('EXACT_8_STATE_CHECKS_PASSED',cnt)
    for x,y in [(F(1,5),F(4,5)),(F(1,9),F(8,9)),(F(2,5),F(3,5))]:
        f1=formula(x,y,y)[1][0]
        f2=sum(formula(x,x,y)[1][:2])
        r=(8-x*y-2*x)/(8-x*y-2*y)
        assert f1/f2==r and 1<r<F(4,3)
    print('RECTIFICATION_IDENTITIES_PASSED')
if __name__=='__main__':test()
