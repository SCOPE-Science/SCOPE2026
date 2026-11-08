"""Exact finite checks of sharp variance and equality geometry for layered path metrics.

All comparisons use fractions, not floating point. Infinite-family conclusions
require the mathematical proof, not finite enumeration.
"""
from fractions import Fraction
from itertools import product


def variance(a):
    length = len(a)
    total = sum(a)
    return Fraction(sum(x*x for x in a), length) - Fraction(total*total, length*length)


def lattice_profiles(n, m, intrafibre):
    """All integer feasible functions, first vertex pinned to zero.

    intrafibre=2 gives independent fibres, intrafibre=1 clique fibres.
    """
    N = n*m
    distances = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            distances[i][j] = (intrafibre if i//m==j//m and i!=j
                               else abs(i//m-j//m))
    a = [0]
    count = 0
    best = Fraction(-1)
    winners = []
    identity_checks = 0
    def walk(t):
        nonlocal count, best, winners, identity_checks
        if t == N:
            count += 1
            V = variance(a)
            if V>best:
                best=V
                winners=[tuple(a)]
            elif V==best:
                winners.append(tuple(a))
            if n>=3:
                mns=[Fraction(sum(a[i*m:(i+1)*m]),m) for i in range(n)]
                vs=[variance(a[i*m:(i+1)*m]) for i in range(n)]
                deficits=[]
                for i in range(n):
                    for j in range(i+1,n):
                        dist=j-i
                        diff=(mns[i]-mns[j])**2
                        if dist==1:
                            deficits.append(Fraction(1)-diff-vs[i]-vs[j])
                        else:
                            deficits.append(Fraction(dist*dist)-diff-2*(vs[i]+vs[j]))
                assert all(z>=0 for z in deficits), (n,m,intrafibre,a,deficits)
                missing=sum((n-2-(1 if i in (0,n-1) else 2))*vs[i] for i in range(n))
                lhs=n*n*(Fraction(n*n-1,12)-V)
                rhs=sum(deficits)+missing
                assert lhs==rhs,(lhs,rhs,a)
                identity_checks+=1
            return
        lo=max(a[j]-distances[t][j] for j in range(t))
        hi=min(a[j]+distances[t][j] for j in range(t))
        for value in range(lo,hi+1):
            a.append(value)
            walk(t+1)
            a.pop()
    walk(1)
    return count,best,winners,identity_checks


def winner_geometry(n,m,f,inside):
    if n>=4:
        return all(f[i*m+j]==f[0]+i for i in range(n) for j in range(m)) or all(
            f[i*m+j]==f[0]-i for i in range(n) for j in range(m))
    if n==3:
        center=f[m]
        if not all(x==center for x in f[m:2*m]):
            return False
        return all(abs(x-center)==1 for x in f[:m]+f[2*m:]) and sum(f[:m])+sum(f[2*m:])==2*m*center
    return False



def weighted_examples():
    # Exact unbalanced conditional masses; all fibres retain total mass 1/n.
    for n in (3,4):
        m=2
        # two points per fibre, internal distance two
        weights=((Fraction(i+1,i+3),Fraction(2,i+3)) for i in range(n))
        weights=list(weights)
        assert all(sum(w)==1 for w in weights)
        adj=[[] for _ in range(n*m)]
        for i in range(n*m):
            for j in range(i):
                d=2 if i//m==j//m else abs(i//m-j//m)
                adj[i].append((j,d))
        a=[0]
        best=Fraction(-1)
        winners=[]
        count=0
        def walk(t):
            nonlocal best,winners,count
            if t==n*m:
                count+=1
                M=[sum(weights[i][j]*a[i*m+j] for j in range(m)) for i in range(n)]
                V=[sum(weights[i][j]*(a[i*m+j]-M[i])**2 for j in range(m)) for i in range(n)]
                mu=sum(M)/n
                var=sum((x-mu)**2+v for x,v in zip(M,V))/n
                if var>best:
                    best=var;winners=[tuple(a)]
                elif var==best:
                    winners.append(tuple(a))
                pairloss=[]
                for i in range(n):
                    for j in range(i+1,n):
                        gap=j-i
                        if gap==1:
                            loss=1-(M[i]-M[j])**2-V[i]-V[j]
                        else:
                            loss=gap*gap-(M[i]-M[j])**2-2*(V[i]+V[j])
                        assert loss>=0
                        pairloss.append(loss)
                excess=sum((n-2-(1 if i in (0,n-1) else 2))*V[i] for i in range(n))
                assert n*n*(Fraction(n*n-1,12)-var)==sum(pairloss)+excess
                return
            lo=max(a[j]-d for j,d in adj[t]);hi=min(a[j]+d for j,d in adj[t])
            for z in range(lo,hi+1):
                a.append(z);walk(t+1);a.pop()
        walk(1)
        assert best==Fraction(n*n-1,12)
        assert all(winner_geometry(n,m,f,2) for f in winners)
        assert len(winners)==2
        print('UNBALANCED_EXACT_CONDITIONAL_MEASURES_OK',n,count,best,len(winners))

def run():
    cases=[(3,2,2),(3,3,2),(4,2,2),(4,3,2),(5,2,2),
           (3,2,1),(3,3,1),(4,2,1),(4,3,1),(5,2,1)]
    for n,m,inside in cases:
        count,best,winners,identities=lattice_profiles(n,m,inside)
        expected=Fraction(n*n-1,12)
        assert best==expected,(n,m,inside,best,expected)
        assert all(winner_geometry(n,m,f,inside) for f in winners)
        assert len(winners)==(2 if n>=4 or inside==1 else (6 if m==2 else 20))
        print('EXACT_LAYERED_METRIC',n,m,'internal',inside,'integer_profiles',count,
              'max',best,'optimizers',len(winners),'deficit_checks',identities)
    count,best,winners,_=lattice_profiles(2,2,2)
    assert best==Fraction(1,2)
    assert best>Fraction(2*2-1,12)
    print('TWO_LAYER_SHARPNESS_OK',count,best)
    weighted_examples()
    print('ALL_PATH_FIBRE_VARIANCE_CHECKS_OK')


if __name__=='__main__':
    run()
