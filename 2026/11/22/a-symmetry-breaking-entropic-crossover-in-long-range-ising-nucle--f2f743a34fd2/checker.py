"""Finite, independently reproducible consistency checks for a power-law Ising gate crossover.

Python 3, standard library only. The theorem for all beta is proved separately;
these checks cover small chain sizes, exact finite-chain linear solves, and shape gaps.
"""
from decimal import Decimal, localcontext
from itertools import combinations
from math import comb


def energy(n, subset, q, J, h):
    s = set(subset)
    spins = [1 if i in s else -1 for i in range(n)]
    val = -h * sum(spins)
    for i in range(n):
        for j in range(i + 1, n):
            weight = ((Decimal(j-i).ln() * (-q)).exp())
            val -= J * weight * spins[i] * spins[j]
    return val


def gap(n, subset, J):
    m = n // 2
    S = set(subset)
    E = set(range(m))
    def crosslog(T):
        return sum((Decimal(j-i).ln() for i in range(n) for j in range(i+1,n)
                    if (i in T) != (j in T)), Decimal(0))
    return 2 * J * (crosslog(E) - crosslog(S))


def solve_linear(A, b):
    n = len(b)
    for i in range(n):
        piv = max(range(i,n), key=lambda k:abs(A[k][i]))
        assert A[piv][i] != 0
        A[i], A[piv] = A[piv], A[i]
        b[i], b[piv] = b[piv], b[i]
        div = A[i][i]
        for j in range(i+1,n):
            r = A[j][i]/div
            if r == 0: continue
            A[j][i]=Decimal(0)
            for k in range(i+1,n): A[j][k]-=r*A[i][k]
            b[j]-=r*b[i]
    x=[Decimal(0)]*n
    for i in range(n-1,-1,-1):
        x[i]=(b[i]-sum((A[i][j]*x[j] for j in range(i+1,n)),Decimal(0)))/A[i][i]
    return x


def exact_mean(n,q,J,h,beta):
    goal=(1<<n)-1
    vals=[energy(n, [i for i in range(n) if mask>>i&1],q,J,h)
          for mask in range(goal+1)]
    M=[[Decimal(0) for _ in range(goal)] for _ in range(goal)]
    b=[Decimal(1) for _ in range(goal)]
    for i in range(goal):
        for j in range(n):
            nxt=i^(1<<j)
            w=(-(beta*max(vals[nxt]-vals[i],Decimal(0)))).exp()/n
            M[i][i]+=w
            if nxt < goal: M[i][nxt]-=w
    return solve_linear(M,b)[0],vals


def crossover(n,J,lam):
    m=n//2
    Z=sum(((-lam*gap(n,S,J)).exp() for S in combinations(range(n),m)),Decimal(0))
    return Decimal(n*n)/(Decimal(m*(n-m))*Z)


def main():
    with localcontext() as ctx:
        ctx.prec=75
        J=Decimal('1'); h=Decimal('0.3')
        cases=0
        # The edge intervals, and only them, maximize cross-log distance for every k.
        for n in range(3,11):
            for k in range(1,n):
                edge=set(range(k)); rhs=sum((Decimal(j-i).ln() for i in range(n)
                    for j in range(i+1,n) if (i in edge)!=(j in edge)),Decimal(0))
                for subset in combinations(range(n),k):
                    S=set(subset)
                    lhs=sum((Decimal(j-i).ln() for i in range(n) for j in range(i+1,n)
                         if (i in S)!=(j in S)),Decimal(0))
                    assert rhs + Decimal('1e-50') >= lhs
                    if S not in (edge,set(range(n-k,n))):
                        assert rhs-lhs > Decimal('1e-45')
                    cases+=1
        # At exact uniform coupling the central layer is a parallel gate.
        for n in (3,4,5,6):
            m=n//2
            limit=Decimal(n*n)/(Decimal(m*(n-m))*comb(n,m))
            for beta in (Decimal(3),Decimal(5),Decimal(7)):
                value,En=exact_mean(n,Decimal(0),J,h,beta)
                Eedge=En[(1<<m)-1]
                rel=value*(-beta*(Eedge-En[0])).exp()
                assert abs(rel/limit-1) < Decimal('0.25')
                cases+=1
        # In the 1/beta symmetry-breaking window the entire gate has finite weights.
        for n in (4,5):
            for lam in (Decimal('0.5'),Decimal('2')):
                errors=[]
                for beta in (Decimal(4),Decimal(7),Decimal(10)):
                    q=lam/beta
                    value,En=exact_mean(n,q,J,h,beta)
                    rel=value*(-beta*(En[(1<<(n//2))-1]-En[0])).exp()
                    err=abs(rel-crossover(n,J,lam))
                    errors.append(err)
                    cases+=1
                assert errors[-1]<errors[0],(n,lam,errors)
        # Explicit N=4 shape splitting spectrum (two occurrences of each value).
        n=4;m=2
        spectrum=sorted(gap(n,S,J) for S in combinations(range(n),m))
        target=sorted([Decimal(0)]*2 + [2*Decimal(3).ln()]*2 + [4*Decimal(2).ln()]*2)
        assert all(abs(a-b)<Decimal('1e-60') for a,b in zip(spectrum,target))
        cases+=1
        print('PASS: finite checks',cases, 'edge rearrangement, exact Markov hitting solves, gate crossover')

if __name__=='__main__':
    main()
