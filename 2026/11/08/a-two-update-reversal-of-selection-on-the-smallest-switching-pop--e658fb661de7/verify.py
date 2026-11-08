"""Exact, dependency-free polynomial certificate for the three-vertex alternating-network theorem.
Run: python verify.py. Coefficients are ascending and all operations use exact Python integers.
"""
import itertools
from fractions import Fraction

def add(a,b):
    n=max(len(a),len(b)); z=[0]*n
    for i,x in enumerate(a):z[i]+=x
    for i,x in enumerate(b):z[i]+=x
    while len(z)>1 and z[-1]==0:z.pop()
    return tuple(z)
def neg(a):return tuple(-v for v in a)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    while len(z)>1 and z[-1]==0:z.pop()
    return tuple(z)
def powp(a,n):
    p=(1,)
    for k in range(n):p=mul(p,a)
    return p
def scale(a,k):return tuple(k*x for x in a)
ZERO=(0,); ONE=(1,); R=(0,1); A=(2,1); B=(1,2); D=scale(mul(A,B),2)
def mm(X,Y):
    n=len(X); p=len(Y);m=len(Y[0]); Z=[[ZERO for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            z=ZERO
            for k in range(p):z=add(z,mul(X[i][k],Y[k][j]))
            Z[i][j]=z
    return Z

def matrices():
    # Six symmetry-reduced states: (hub, number of mutant leaves)
    # (0,0),(0,1),(0,2),(1,0),(1,1),(1,2).
    S=[[ZERO for _ in range(6)] for _ in range(6)]
    C=[[ZERO for _ in range(6)] for _ in range(6)]
    for Z in (S,C): Z[0][0]=D;Z[5][5]=D
    def setrow(M,i,items):
        for j,v in items.items():M[i][j]=v
    # Entries of the one-step transition matrices multiplied by
    # d=2(r+2)(2r+1), so all coefficients are integers.
    setrow(S,1,{0:B,1:scale(B,3),4:scale(mul(R,B),2)})
    setrow(S,2,{1:scale(A,2),5:scale(mul(R,A),4)})
    setrow(S,3,{0:scale(B,4),4:scale(mul(R,B),2)})
    setrow(S,4,{1:scale(A,2),4:scale(mul(R,A),3),5:mul(R,A)})
    setrow(C,1,{0:scale(B,2),1:scale(B,2),2:mul(R,B),4:mul(R,B)})
    setrow(C,2,{1:scale(A,2),2:scale(mul(R,A),2),5:scale(mul(R,A),2)})
    setrow(C,3,{0:scale(B,2),3:scale(B,2),4:scale(mul(R,B),2)})
    setrow(C,4,{1:A,3:A,4:scale(mul(R,A),2),5:scale(mul(R,A),2)})
    for M in (S,C):
        for row in M:
            x=ZERO
            for q in row:x=add(x,q)
            assert x==D
    return S,C

def det(X):
    n=len(X);ans=ZERO
    for perm in itertools.permutations(range(n)):
        inv=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        z=ONE
        for i,j in enumerate(perm):z=mul(z,X[i][j])
        ans=add(ans, neg(z) if inv%2 else z)
    return ans

def certificate(t,S,C):
    Bmat=mm(mm(S,S) if t==2 else S,mm(C,C) if t==2 else C)
    d=powp(D,2*t)
    ids=(1,2,3,4)
    X=[[sub(d if i==j else ZERO,Bmat[ids[i]][ids[j]]) for j in range(4)] for i in range(4)]
    b=[Bmat[ids[i]][5] for i in range(4)]
    dt=det(X)
    vals=[]
    for j in (0,2):
        Y=[row.copy() for row in X]
        for i in range(4):Y[i][j]=b[i]
        vals.append(det(Y))
    num=add(scale(vals[0],2),vals[1]); return num,scale(dt,3)

M=(1,1,1) # 1+r+r^2
P6=(544,2960,5560,6379,5560,2960,544)
D1=(80,532,1334,1751,1334,532,80)
D2=(14080,205696,1325168,4967936,12074388,20132868,23783565,20132868,12074388,4967936,1325168,205696,14080)
num1=neg(mul(mul(powp(R,2),sub(R,ONE)),mul(add(scale(R,2),ONE),(16,31,16))))
num2=mul(mul(mul(powp(R,2),sub(R,ONE)),mul(add(R,(2,)),powp(add(scale(R,2),ONE),2))),P6)

def test_symbolic():
    S,C=matrices()
    for t,Dpoly,delta in ((1,D1,num1),(2,D2,num2)):
        # Rho = numerator / denominator. Target: Rho - r^2/(1+r+r^2) = delta/((1+r+r^2)*Dpoly)
        n,d=certificate(t,S,C)
        lhs=sub(mul(sub(mul(n,M),mul(d,powp(R,2))),Dpoly),mul(d,delta))
        assert lhs==ZERO,(t,lhs)
        assert all(x>0 for x in Dpoly)
        if t==2:assert all(x>0 for x in P6)
        print('IDENTITY_OK',t,'determinant-polynomial degree',len(d)-1)

# Independent direct eight-state matrix (without leaf aggregation) evaluated exactly.
def direct_prob(rate,tau):
    masks=range(8)
    def step(edges):
        nbr=[[] for _ in range(3)]
        for i,j in edges:nbr[i].append(j);nbr[j].append(i)
        P=[[Fraction(0) for _ in masks] for _ in masks]
        for state in masks:
            w=[rate if state>>i&1 else Fraction(1) for i in range(3)];tot=sum(w)
            for i in range(3):
                for j in nbr[i]:
                    new=(state | (1<<j)) if state>>i&1 else (state &~(1<<j))
                    P[state][new]+=w[i]/tot/len(nbr[i])
        return P
    def product(A,B):
        return [[sum(A[i][k]*B[k][j] for k in masks) for j in masks] for i in masks]
    P=step([(0,1),(0,2)]);Q=step([(0,1),(0,2),(1,2)])
    R=[[int(i==j) for j in masks] for i in masks]
    for M0 in [P]*tau+[Q]*tau:R=product(R,M0)
    ids=range(1,7)
    A=[[Fraction(int(i==j))-R[i][j] for j in ids] for i in ids]
    b=[R[i][7] for i in ids]
    for k in range(6):
        j=next(i for i in range(k,6) if A[i][k]);A[k],A[j]=A[j],A[k];b[k],b[j]=b[j],b[k]
        v=A[k][k]; A[k]=[a/v for a in A[k]];b[k]/=v
        for i in range(6):
            if i==k:continue
            v=A[i][k];A[i]=[a-v*c for a,c in zip(A[i],A[k])];b[i]-=v*b[k]
    return (b[0]+b[1]+b[3])/3 # masks 001,010,100 => b indices 0,1,3

def evalpoly(P,r):
    return sum(Fraction(x)*r**k for k,x in enumerate(P))
def test_independent():
    for j in range(1,21):
        r=Fraction(j,7)
        for t,Dpoly,delta in ((1,D1,num1),(2,D2,num2)):
            x=direct_prob(r,t)
            predicted=r*r/(1+r+r*r)+evalpoly(delta,r)/(evalpoly(M,r)*evalpoly(Dpoly,r))
            assert x==predicted,(r,t,x,predicted)
    print('EIGHT_STATE_OK: 40 exact independent tests')
if __name__=='__main__':
    test_symbolic();test_independent();print('VERIFY_OK')
