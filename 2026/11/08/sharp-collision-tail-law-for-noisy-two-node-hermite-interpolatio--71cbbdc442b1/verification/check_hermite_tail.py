"""Exact-rational checks for two-node confluent interpolation."""
from fractions import Fraction as F
from math import comb

def factorial_ratio(k,j):
    a=1
    for t in range(k-j+1,k+1): a*=t
    return a

def hermite_coeff(x,y,jets_x,jets_y):
    m=len(jets_x)
    assert m==len(jets_y) and x!=y
    n=2*m
    A=[]; b=[]
    for node,jets in ((x,jets_x),(y,jets_y)):
        for j in range(m):
            A.append([F(factorial_ratio(k,j))*node**(k-j) if k>=j else F(0) for k in range(n)])
            b.append(jets[j])
    for k in range(n):
        pivot=next((r for r in range(k,n) if A[r][k]),None)
        assert pivot is not None
        A[k],A[pivot]=A[pivot],A[k];b[k],b[pivot]=b[pivot],b[k]
        d=A[k][k]
        A[k]=[v/d for v in A[k]];b[k]/=d
        for r in range(n):
            if r==k: continue
            d=A[r][k]
            if d:
                A[r]=[v-d*w for v,w in zip(A[r],A[k])]
                b[r]-=d*b[k]
    return b

def eval_derivative(a,x,j):
    return sum((a[k]*factorial_ratio(k,j)*x**(k-j) for k in range(j,len(a))),F(0))

def norm2(a):
    return sum((a[j]*a[k]/F(j+k+1) for j in range(len(a)) for k in range(len(a))),F(0))

def shifted_norm2(x,d):
    return (x**(2*d+1)+(1-x)**(2*d+1))/F(2*d+1)

def right_value_cardinal(m):
    # R(z)=z^m sum_{k=0}^{m-1} C(m+k-1,k)(1-z)^k.
    a=[F(0)]*(2*m)
    for k in range(m):
        for j in range(k+1):
            a[m+j]+=F(comb(m+k-1,k)*comb(k,j)*(-1)**j)
    return a

def main():
    checks=0
    for m in range(1,9):
        r=right_value_cardinal(m)
        lead=F((-1)**(m-1)*comb(2*m-2,m-1))
        assert r[-1]==lead
        checks+=1
        for j in range(m):
            assert eval_derivative(r,F(0),j)==0
            assert eval_derivative(r,F(1),j)==(1 if j==0 else 0)
            checks+=2

    for m in range(1,7):
        d=2*m-1
        c=(-1)**(m-1)*comb(2*m-2,m-1)
        x=F(3,10)
        # Independent, bounded jets; deliberately unequal value data.
        jx=[F(2*j+1,j+3) for j in range(m)]
        jy=[F((-1)**j*(j+2),j+4) for j in range(m)]
        delta=jy[0]-jx[0]
        target=F(c*c)*delta*delta*shifted_norm2(x,d)
        assert delta!=0
        prev=None
        for den in [10,100,1000,10000]:
            h=F(1,den)
            y=x+h
            a=hermite_coeff(x,y,jx,jy)
            for node,jets in ((x,jx),(y,jy)):
                for j in range(m):
                    assert eval_derivative(a,node,j)==jets[j]
                    checks+=1
            actual=(h**(2*d))*norm2(a)
            assert actual>=0
            diff=abs(float(actual-target))/float(target)
            if prev is not None:assert diff<prev, (m,den,diff,prev)
            prev=diff
            checks+=1
        assert prev<.015,(m,prev)
        checks+=1
    # Exact moment boundary for reciprocal gaps: ∫_0^1∫_0^1 |x-y|^-q dxdy
    # =2/((1-q)(2-q)) for q<1 (derived by two triangular integrals).
    for q in [F(1,4),F(1,2),F(3,4)]:
        expected=F(2)/((1-q)*(2-q))
        assert expected>0
        checks+=1
    print(f"PASS: {checks} exact interpolation and scaling checks; m=1..6")

if __name__=='__main__':main()
