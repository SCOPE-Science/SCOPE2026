"""Independent exact-arithmetic spot checks for the weighted-rook Gauss endpoint theorem.
Run with Python 3: python verify.py. A finite verifier supplements, not replaces, the proof.
"""
from fractions import Fraction as F
from itertools import product


def mm(A,B):
    n=len(A);m=len(B[0]);k=len(B)
    return [[sum((A[i][z]*B[z][j] for z in range(k)),F(0)) for j in range(m)] for i in range(n)]


def inv(A):
    n=len(A)
    M=[list(A[i])+[F(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        k=next(k for k in range(j,n) if M[k][j])
        M[j],M[k]=M[k],M[j]
        v=M[j][j]; M[j]=[x/v for x in M[j]]
        for i in range(n):
            if i==j:continue
            w=M[i][j]
            if w:M[i]=[x-w*y for x,y in zip(M[i],M[j])]
    return [r[n:] for r in M]


def Lap(p,q,a,b):
    n=p*q; M=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(p):
        for j in range(q):
            u=i*q+j
            for k in range(p):
                if k!=i:
                    v=k*q+j; M[u][u]+=a; M[u][v]-=a
            for l in range(q):
                if l!=j:
                    v=i*q+l; M[u][u]+=b; M[u][v]-=b
    return M


def gauss(x):
    return (x*x-6*x+12)/(x*x+6*x+12)


def direct(p,q,a,b,h):
    L=Lap(p,q,a,b);L2=mm(L,L);n=p*q
    Den=[[h*h*L2[i][j]+6*h*L[i][j]+12*F(i==j) for j in range(n)] for i in range(n)]
    Num=[[h*h*L2[i][j]-6*h*L[i][j]+12*F(i==j) for j in range(n)] for i in range(n)]
    return mm(Num,inv(Den))


def spectral(p,q,a,b,h,i,j,k,l):
    P=p*a;Q=q*b; x=gauss(h*P);y=gauss(h*Q);z=gauss(h*(P+Q))
    # e0p_{ik}=1/p, e1p_{ik}=delta_ik-1/p, and similarly for q
    return (1+ (p*F(i==k)-1)*x+(q*F(j==l)-1)*y+(p*F(i==k)-1)*(q*F(j==l)-1)*z)/(p*q)


def coeff(p,P,Q):
    return [144*p*Q,72*Q*(2*P+p*Q),
       12*Q*((6-p)*P*(P+Q)+p*Q*Q),
       6*P*Q*(P+Q)*(2*P-(p-2)*Q),
       P*Q*(P+Q)*(P*(P+Q)-(p-1)*Q*Q)]

def D(x,h):return (h*x)**2+6*h*x+12


def check():
    checks=0
    params=[(2,2,F(1),F(1)),(2,3,F(1),F(1)),(3,3,F(1),F(1)),
      (2,4,F(5,4),F(1)),(2,5,F(25,16),F(1)),
      (2,5,F(1),F(1)),(3,4,F(1),F(1)),(4,4,F(1),F(1)),
      (5,2,F(1),F(25,16)),(2,6,F(1),F(1))]
    for p,q,a,b in params:
        P=p*a;Q=q*b
        c=coeff(p,P,Q)
        for h in (F(1,5),F(1),F(4),F(25)):
            lhs=sum((c[k]*h**k for k in range(5)),F(0))
            rhs=(Q/D(Q,h)+(p-1)*((P+Q)/D(P+Q,h)-P/D(P,h)))*D(P,h)*D(Q,h)*D(P+Q,h)
            assert lhs==rhs,(p,q,a,b,h,lhs,rhs);checks+=1
            # Direct inverse vs spectral on a whole transition matrix
            if h in (F(1,5),F(4)) and p*q<=16:
                T=direct(p,q,a,b,h)
                for i,j,k,l in product(range(p),range(q),range(p),range(q)):
                    assert T[i*q+j][k*q+l]==spectral(p,q,a,b,h,i,j,k,l)
                    checks+=1
        # Infinity-sign necessary conditions and selected sufficient examples.
        A=P*(P+Q)-(p-1)*Q**2
        B=Q*(P+Q)-(q-1)*P**2
        if p==2 and q==5 and a==F(25,16):
            assert A>0 and B>0
            for h in [F(1),F(2),F(100),F(100000)]:
                entries=[spectral(p,q,a,b,h,0,0,i,j) for i in range(p) for j in range(q)]
                assert all(v>0 for v in entries); checks+=1
        if p==2 and q==5 and a==1:
            assert A<0
            h=F(10000)
            assert spectral(p,q,a,b,h,0,0,0,1)<0;checks+=1
    # For each admitted integer pair the rationally represented interval is nonempty.
    possible=[]
    for p,q in product(range(2,20),repeat=2):
        # existence of r>0 both inequalities iff (p-1)(q-1)<=? use exact sign on roots
        import math
        rp=(math.sqrt(4*p-3)-1)/2
        rq=(math.sqrt(4*q-3)-1)/2
        if rp*rq<1+1e-10: possible.append((p,q))
    assert set(possible)=={(2,2),(2,3),(3,2),(2,4),(4,2),(2,5),(5,2),(3,3)}
    checks+=len(possible)
    print('VERIFY_OK',checks)

if __name__=='__main__': check()
