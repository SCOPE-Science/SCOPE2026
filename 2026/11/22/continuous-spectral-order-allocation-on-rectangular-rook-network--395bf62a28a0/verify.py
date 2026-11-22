"""Reproduce exact rook-product spectral identities and scalar optimality checks.
Only Python's standard library is required. This is finite verification, not a substitute for proof.
"""
from fractions import Fraction as Q
from math import log, sqrt


def invdet(A):
    n=len(A); H=[list(map(Q,row))+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    det=Q(1)
    for k in range(n):
        r=next(i for i in range(k,n) if H[i][k])
        if r!=k:
            H[k],H[r]=H[r],H[k]; det=-det
        t=H[k][k];det*=t
        H[k]=[z/t for z in H[k]]
        for i in range(n):
            if i==k:continue
            t=H[i][k]
            if t:H[i]=[z-t*w for z,w in zip(H[i],H[k])]
    return [r[n:] for r in H],det


def direct(m,n,x,y):
    N=m*n;L=[[Q(0) for _ in range(N)] for _ in range(N)]
    for i in range(m):
        for j in range(n):
            u=i*n+j
            for k in range(i+1,m):
                v=k*n+j;L[u][u]+=x;L[v][v]+=x;L[u][v]-=x;L[v][u]-=x
            for k in range(j+1,n):
                v=i*n+k;L[u][u]+=y;L[v][v]+=y;L[u][v]-=y;L[v][u]-=y
    Z=[[L[i][j]+Q(1,N) for j in range(N)] for i in range(N)]
    I,det=invdet(Z)
    F1=sum(I[i][i] for i in range(N))-1
    F2=sum(I[i][j]*I[j][i] for i in range(N) for j in range(N))-1
    a=m*x;b=n*y
    G1=(m-1)/a+(n-1)/b+Q((m-1)*(n-1))/(a+b)
    G2=Q(m-1)/a**2+Q(n-1)/b**2+Q((m-1)*(n-1))/(a+b)**2
    D=a**(m-1)*b**(n-1)*(a+b)**((m-1)*(n-1))
    assert (F1,F2,det)==(G1,G2,D),(m,n,x,y)


def opt(m,n,p):
    s=p+1.0
    lo=0.0;hi=1.0
    for _ in range(160):
        q=(lo+hi)/2
        f=m*q**(-s)+(n-m)*(1+q)**(-s)-n
        if f>0:lo=q
        else:hi=q
    q=(hi+lo)/2
    b=2/(n*(m-1)*q+m*(n-1)); a=q*b
    x=a/m;y=b/n
    assert abs(n*m*(m-1)*x/2+m*n*(n-1)*y/2-1)<2e-12
    def cost(z):
        bb=2/(n*(m-1)*z+m*(n-1));aa=bb*z
        if p==0:return -((m-1)*log(aa)+(n-1)*log(bb)+(m-1)*(n-1)*log(aa+bb))
        return (m-1)*aa**(-p)+(n-1)*bb**(-p)+(m-1)*(n-1)*(aa+bb)**(-p)
    if n>m:
        assert q<1
        if q<0.999 and n<1000:
            assert cost(q)<=cost(q*0.99)+1e-7*abs(cost(q))
            assert cost(q)<=cost(q*1.01)+1e-7*abs(cost(q))
    if p==0:assert abs(q-sqrt(m/n))<1e-9
    return q,x/y,n*m*(m-1)*x/2


def main():
    checks=0
    for m,n in [(2,2),(2,3),(2,4),(3,3),(3,4)]:
        for x,y in [(Q(1,6),Q(1,9)),(Q(2,7),Q(3,11))]:
            direct(m,n,x,y);checks+=1
    for m in (2,3,4,5):
        for n in (m,m+1,m+4,2*m+7):
            for p in (0,0.3,1,2,3):
                q,ratio,share=opt(m,n,p)
                assert 0<share<1
                checks+=1
    for p in (0,0.5,1,2,4):
        m=3;n=100000000
        q,ratio,share=opt(m,n,p)
        predicted=(m/((p+1)*n))**(1/(p+2))
        assert abs(q/predicted-1)<0.025,(p,q/predicted)
        pred_ratio=m**(-(p+1)/(p+2))*(p+1)**(-1/(p+2))*n**((p+1)/(p+2))
        assert abs(ratio/pred_ratio-1)<0.025
        checks+=1
    for alpha in (0.5,1.0,2.0):
        n=10**20; order=alpha*log(n)
        q,ratio,share=opt(3,n,order)
        assert abs(q-(2.718281828459045**(-1/alpha)))<0.035,(alpha,q)
        checks+=1
    print('PASS',checks,'exact matrix identities, unique-root checks and asymptotic diagnostics')
if __name__=='__main__':main()
