"""Exact finite checks for paired-weight Lipschitz variance on crown graphs.

Requires only Python's standard library. This checker does not establish
universality; the corresponding theorem is proved by the tight-edge lemma.
"""
from fractions import Fraction
from itertools import product
from math import gcd


def check(n, weights):
    assert len(weights) == n and min(weights) > 0
    q = [Fraction(w, sum(weights)) for w in weights]
    N=2*n
    best=Fraction(-1)
    winners=set()
    count=0
    # Only integer potentials need consideration; normalize min(f)=0.
    for z in product(range(4), repeat=N):
        if min(z) != 0: continue
        if any(abs(z[i]-z[n+j])>1 for i in range(n) for j in range(n) if i!=j): continue
        count+=1
        mu=sum(q[i]*(z[i]+z[n+i])/2 for i in range(n))
        var=sum(q[i]*(z[i]*z[i]+z[n+i]*z[n+i])/2 for i in range(n))-mu*mu
        if var>best:
            best=var;winners={z}
        elif var==best:winners.add(z)
    D=min(abs(sum(q[i]*s[i] for i in range(n))) for s in product((-1,1),repeat=n))
    formula=max(Fraction(1,4)+2*max(q),Fraction(1,2)-D*D/4)
    assert best==formula,(n,weights,best,formula)
    for z in winners:
        rng=max(z)-min(z)
        if rng==3:
            assert any((z[i]==0 and z[n+i]==3 and
                        all(z[j]==2 and z[n+j]==1 for j in range(n) if j!=i)) or
                       (z[i]==3 and z[n+i]==0 and
                        all(z[j]==1 and z[n+j]==2 for j in range(n) if j!=i)) or
                       (z[n+i]==0 and z[i]==3 and
                        all(z[j]==1 and z[n+j]==2 for j in range(n) if j!=i)) or
                       (z[n+i]==3 and z[i]==0 and
                        all(z[j]==2 and z[n+j]==1 for j in range(n) if j!=i)) for i in range(n))
        else:
            assert rng==2 and (
                (all(z[n+i]==1 for i in range(n)) and all(z[i] in (0,2) for i in range(n))) or
                (all(z[i]==1 for i in range(n)) and all(z[n+i] in (0,2) for i in range(n))))
    return count,best,len(winners)


if __name__=='__main__':
    for n,ws in [(3,[1,1,1]),(3,[2,3,5]),(4,[1]*4),(4,[1,2,3,5]),
                 (5,[1]*5),(5,[1,2,3,4,5])]:
        c,b,m=check(n,ws)
        print('EXACT_WEIGHTED_CROWN_OK',n,ws,'admissible',c,'maximum',b,'optimizers',m)
    print('ALL_WEIGHTED_CROWN_CHECKS_OK')


def check_arbitrary(n, masses):
    """Independent exhaustive test, all integer feasible functions in 0..3."""
    assert len(masses)==2*n and min(masses)>0
    p=[Fraction(v,sum(masses)) for v in masses]
    alpha=sum(p[:n]); beta=1-alpha
    def disc(weights):
        return min(abs(sum(x*sign for x,sign in zip(weights,ss)))
                   for ss in product((-1,1),repeat=len(weights)))
    DA=disc(p[:n]);DB=disc(p[n:])
    ext=[Fraction(1,4)+2*(p[i]+p[n+i])-
         (alpha-Fraction(1,2)+2*(p[n+i]-p[i]))**2 for i in range(n)]
    fmax=max(alpha-DA**2,beta-DB**2,*ext)
    best=Fraction(-1); winners=[];count=0
    for z in product(range(4),repeat=2*n):
        if min(z)!=0 or any(abs(z[i]-z[n+j])>1 for i in range(n) for j in range(n) if i!=j):continue
        count+=1
        mean=sum(p[k]*z[k] for k in range(2*n))
        var=sum(p[k]*z[k]**2 for k in range(2*n))-mean**2
        if var>best:best=var;winners=[z]
        elif var==best:winners.append(z)
    assert best==fmax,(n,masses,best,fmax)
    for z in winners:
        zmin=min(z); zmax=max(z)
        if zmax-zmin==3:
            assert any((z[i]==0 and z[n+i]==3 and
                        all(z[j]==2 and z[n+j]==1 for j in range(n) if j!=i)) or
                       (z[i]==3 and z[n+i]==0 and
                        all(z[j]==1 and z[n+j]==2 for j in range(n) if j!=i)) for i in range(n))
        else:
            assert (all(z[n+i]==1 for i in range(n)) and all(z[i] in (0,2) for i in range(n))) or \
                   (all(z[i]==1 for i in range(n)) and all(z[n+i] in (0,2) for i in range(n))) or \
                   (all(z[i]==0 for i in range(n)) and all(z[n+i]==1 for i in range(n))) or \
                   (all(z[i]==1 for i in range(n)) and all(z[n+i]==0 for i in range(n)))
    print('EXACT_ARBITRARY_VERTEX_MASSES_OK',n,masses,'admissible',count,'maximum',best,'winners',len(winners))

if __name__=='__main__':
    for n,m in [(3,[1,2,3,4,5,6]),(3,[7,4,2,3,5,9]),
                (4,[1,3,2,5,4,6,7,8]),(4,[1]*8),
                (5,[1,4,2,9,3,7,5,6,8,10]),(5,[1]*10)]:
        check_arbitrary(n,m)
    print('ALL_ARBITRARY_WEIGHTED_CROWN_CHECKS_OK')
