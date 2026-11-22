"""Floating-point spot checks of the log-matrix theorem (optional: NumPy/SciPy).
Not an infinite proof; use verify.py for exact rational-mixture certificates.
"""
import numpy as np
from scipy.linalg import eigh

def partitions(n):
    def build(t,m):
        if len(t)==n:
            yield tuple(t);return
        for a in range(m+2):
            yield from build(t+[a],max(m,a))
    yield from build([0],0)

def main():
    assertions=0
    for n in range(2,9):
        for case in range(2):
            c=np.array([1+((7*i+3*n+case)%4) for i in range(n-1)],dtype=float)
            q=np.array([1+((5*i+2*n+case)%3) for i in range(n)],dtype=float)
            A=np.diag(q)
            for i,a in enumerate(c):
                A[i,i]+=a;A[i+1,i+1]+=a;A[i,i+1]-=a;A[i+1,i]-=a
            lam,Q=eigh(A)
            B=(Q*np.log(lam))@Q.T
            assert max(abs(B[i,j]) for i in range(n) for j in range(i+1,n))>0
            W=B*B
            for k in range(1,n+1):
                target=tuple(i%k for i in range(n))
                def score(t):return sum(4*W[i,j] for i in range(n) for j in range(i+1,n) if t[i]==t[j])
                x=score(target)
                eps=3e-13
                for t in partitions(n):
                    if max(t)+1!=k:continue
                    d=score(t)-x
                    assert d>=-eps,(n,k,case,t,d)
                    if t!=target:assert d>eps,(n,k,case,t,d)
                    assertions+=2
    r=(3-np.sqrt(5))/2
    for n in (40,160):
        A=np.diag([2.]+[3.]*(n-2)+[2.])
        A+=np.diag(-np.ones(n-1),1)+np.diag(-np.ones(n-1),-1)
        lam,Q=eigh(A)
        B=(Q*np.log(lam))@Q.T
        for k in (1,2,3,5):
            v=sum(4*B[i,j]**2 for i in range(n) for j in range(i+1,n) if (j-i)%k==0)/n
            limit=4/k**2*sum(r**(2*k*l)/l**2 for l in range(1,80))
            assert abs(v-limit)<0.09*limit, (n,k,v,limit)
            assertions+=1
    print('PASS',assertions,'log-matrix floating-point comparisons, n<=8 and homogeneous limits')
if __name__=='__main__':main()
