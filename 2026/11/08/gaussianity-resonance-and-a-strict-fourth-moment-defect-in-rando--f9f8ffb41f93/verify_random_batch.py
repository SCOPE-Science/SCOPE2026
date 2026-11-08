"""Exact rational checks for a harmonic random-batch Euler model.

Usage: python3 verify_random_batch.py
Standard library only; finite calculations check algebra, not infinite-theorem scope.
"""
from fractions import Fraction as F
from itertools import combinations


def partitions(items, p):
    """Enumerate unlabeled equipartitions into p-element batches."""
    items = tuple(items)
    if not items:
        yield ()
        return
    first = items[0]
    for tail in combinations(items[1:], p-1):
        block = (first,) + tail
        remain = tuple(x for x in items[1:] if x not in tail)
        for rest in partitions(remain, p):
            yield (block,) + rest


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def mul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def add(A, B):
    return [[a+b for a,b in zip(row, other)] for row,other in zip(A,B)]


def scale(A, c):
    return [[c*a for a in row] for row in A]


def equal(A,B):
    assert A == B, (A,B)


def projector(n, blocks):
    P=eye(n)
    for block in blocks:
        for i in block:
            for j in block:
                P[i][j]-=F(1,len(block))
    return P


def check(N,p,alpha,kappa,tau):
    I=eye(N)
    J=[[F(1,N) for _ in range(N)] for _ in range(N)]
    H=add(I,scale(J,-1))
    m=F(N,N-1)
    c=F(p,p-1)
    a=1-alpha*tau
    b=a-kappa*tau*c
    q=m/c
    rho=(1-q)*a*a+q*b*b
    assert rho == 1-2*(alpha+kappa*m)*tau+(alpha*alpha+2*alpha*kappa*m+kappa*kappa*c*m)*tau*tau
    parts=list(partitions(range(N),p))
    assert len(parts)>1
    Ps=[projector(N,blocks) for blocks in parts]
    for P in Ps:
        equal(mul(P,P),P)
        equal(mul(P,J),scale(J,0))
    avgP=scale([[sum(P[i][j] for P in Ps) for j in range(N)] for i in range(N)],F(1,len(Ps)))
    equal(avgP,scale(H,q))
    avgL=scale(avgP,c)
    equal(avgL,scale(H,m))
    avgL2=scale(avgL,c)
    # Exact expected square of the random update; two spectral blocks.
    avgA2=scale(I,a*a)
    avgA2=add(avgA2,scale(avgP,b*b-a*a))
    equal(avgA2,add(scale(J,a*a),scale(H,rho)))
    # The pairs (0,1) sample two different projection norms.
    w=[F(1), F(-1)]+[F(0)]*(N-2)
    norms=[]; together=[]
    for P, blocks in zip(Ps, parts):
        pw=[sum(P[i][j]*w[j] for j in range(N)) for i in range(N)]
        norms.append(sum(x*x for x in pw))
        together.append(any(0 in block and 1 in block for block in blocks))
    assert set(norms)=={F(2),2-F(2,p)}
    assert all(t==(z==2) for t,z in zip(together,norms))
    s=F(sum(together),len(parts))
    assert s==F(p-1,N-1)
    avg=sum(norms,F(0))/len(norms)
    var=sum((z-avg)**2 for z in norms)/len(norms)
    assert var==F(4,p*p)*s*(1-s)
    # Reflection step, for every partition, is a scalar times an orthogonal matrix.
    star=F(2)/(2*alpha+kappa*c)
    aa=1-alpha*star
    for P in Ps:
        R=add(I,scale(P,-2))
        equal(mul(R,R),I)
        A=add(scale(I,aa),scale(P,-kappa*star*c))
        equal(A,scale(R,aa))
    assert star < F(2)*(alpha+kappa*m)/(alpha*alpha+2*alpha*kappa*m+kappa*kappa*c*m)
    if tau < F(2)*(alpha+kappa*m)/(alpha*alpha+2*alpha*kappa*m+kappa*kappa*c*m):
        v=tau/(1-rho)
        bound=F(12)*v*v*(b*b-a*a)**2*F((p-1)*(N-p),p*p*(N-1)*(N-1))
        assert (bound==0)==(tau==star)
    return len(parts)


count=0
for N,p in [(4,2),(6,2),(6,3),(8,2),(8,4)]:
    for alpha,kappa,tau in [(F(1),F(1),F(1,4)), (F(2),F(3),F(1,7)),(F(1),F(2),F(1,2))]:
        count+=check(N,p,alpha,kappa,tau)
# A precise example with positive fourth-excess lower bound.
N,p=4,2
alpha=kappa=F(1)
tau=F(1,4)
m=F(4,3); c=F(2); a=1-alpha*tau; b=a-kappa*c*tau
rho=F(11,48)
v=tau/(1-rho)
assert v==F(12,37)
bound=F(12)*v*v*(b*b-a*a)**2*F((p-1)*(N-p),p*p*(N-1)*(N-1))
assert bound==F(24,1369)
assert F(2)/(2*alpha+kappa*c)==F(1,2)
assert F(2)*(alpha+kappa*m)/(alpha*alpha+2*alpha*kappa*m+kappa*kappa*c*m)==F(14,19)
print(f'PASS: exact partition/projector/resonance checks across {count} partition cases')
print(f'N=4, p=2, alpha=kappa=1, h=1/4: variance v={v}, fourth excess lower bound={bound}')
print('Reflection h=1/2; exact mean-square stability endpoint h=14/19')
