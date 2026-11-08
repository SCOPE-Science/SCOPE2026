"""Exact, self-contained checks for a three-vertex neighborhood confidence process.

The mathematical arguments in RESULT.md cover all permitted real parameters;
these finite tests are additional cross-checks, not substitutes for proof.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter


def ndw_step(state, leaf, rho, eps):
    """Pure neighborhood-DW update on the static path leaf-center-leaf.

    leaf is 0 or 2; both directed receptiveness decisions use the
    *preinteraction* state, as in the asymmetric corrected update rule.
    """
    a, c, b = state
    values = list(state)
    d_leaf = abs(a-b)/2  # leaf tests other leaf through center's mean
    # Center always sees its own opinion in the selected leaf's neighborhood.
    if d_leaf < eps:
        values[leaf] = state[leaf]+rho*(c-state[leaf])
    values[1] = c+rho*(state[leaf]-c)
    return tuple(values)


def variance_about_mean(s):
    m = sum(s)/3
    return sum((x-m)**2 for x in s)


def test_receptiveness_and_invariant():
    checked=0
    for a,b in [(F(0),F(1)),(F(1,8),F(7,8)),(F(0),F(1,2))]:
        for c in (a,(a+b)/2,b):
            for rho in (F(1,8),F(1,3),F(1,2)):
                for eps in ((b-a)/4,(b-a)/2,3*(b-a)/4):
                    s=(a,c,b)
                    for leaf in (0,2):
                        u=ndw_step(s,leaf,rho,eps)
                        if eps<=(b-a)/2:
                            assert u[0]==a and u[2]==b
                            assert u[1]==(1-rho)*c+rho*s[leaf]
                        else:
                            assert a<=u[0]<=u[1]<=u[2]<=b
                            assert u[2]-u[0]<=b-a
                            assert sum(u)==sum(s)
                            assert variance_about_mean(u)<=variance_about_mean(s)
                        checked+=1
    return checked


def test_high_confidence_generator():
    checked=0
    for den in (2,3,4,5,6):
        for ia,ic,ib in product(range(den+1), repeat=3):
            if not ia<=ic<=ib or ia==ib: continue
            s=tuple(F(x,den) for x in (ia,ic,ib))
            eps=F(1)
            rho=F(1,3)
            V=variance_about_mean(s)
            vs=sum(variance_about_mean(ndw_step(s,k,rho,eps)) for k in (0,2))/2
            assert vs==V-rho*(1-rho)*((s[0]-s[1])**2+(s[1]-s[2])**2)
            assert vs <= (1-rho*(1-rho))*V
            checked+=1
    return checked


def test_finite_law_and_moments():
    checked=0
    a,b=F(0),F(1)
    z=F(1,3)
    eps=F(1,4)
    rho=F(1,2)
    for t in range(1,11):
        masses=Counter()
        for words in product((0,2),repeat=t):
            s=(a,z,b)
            for leaf in words: s=ndw_step(s,leaf,rho,eps)
            masses[s[1]]+=1
        theoretical={F(z+k,2**t) for k in range(2**t)}
        assert set(masses)==theoretical
        assert set(masses.values())=={1}
        n=2**t
        mean=sum(x*v for x,v in masses.items())/n
        var=sum((x-mean)**2*v for x,v in masses.items())/n
        q=1-rho
        expected_mean=F(1,2)+q**t*(z-F(1,2))
        expected_variance=rho/(4*(2-rho))*(1-q**(2*t))
        assert mean==expected_mean and var==expected_variance
        checked+=1
    return checked


def test_general_moment_recursion():
    checked=0
    for rho in (F(1,10), F(1,3),F(1,2)):
        for a,b in ((F(0),F(1)),(F(1,4),F(3,4))):
            q=1-rho
            M=(a+b)/2
            target_var=rho*(b-a)**2/(4*(2-rho))
            assert target_var==q*q*target_var+rho*rho*(b-a)**2/4
            for z in (a,M,b):
                m=z
                v=F(0)
                for t in range(1,21):
                    v=q*q*v+rho*rho*(b-a)**2/4
                    m=q*m+rho*M
                    assert m==M+q**t*(z-M)
                    assert v==target_var*(1-q**(2*t))
                    checked+=1
    return checked

if __name__=='__main__':
    c1=test_receptiveness_and_invariant()
    c2=test_high_confidence_generator()
    c3=test_finite_law_and_moments()
    c4=test_general_moment_recursion()
    print('VERIFY_OK', 'local transitions',c1, 'high-confidence Bellman',c2,
          'dyadic exact laws',c3,'moment recurrences',c4)

# Extra star-family checks: the source's directed eligibility criterion is
# computed from the entire set of leaves, not from just the selected leaf.
def star_step(leaves, hub, selected, rho, eps):
    p=sum(leaves, F(0))/len(leaves)
    b=leaves[selected]
    new_hub=hub+rho*(b-hub)
    upd=list(leaves)
    if abs(b-p)<eps:
        upd[selected]=b+rho*(hub-b)
    return tuple(upd),new_hub

def test_frozen_stars():
    checked=0
    for m in range(2,10):
        for k in range(1,m):
            leaves=tuple([F(0)]*(m-k)+[F(1)]*k)
            p=F(k,m)
            for eps in (min(p,1-p),min(p,1-p)/2):
                for rho in (F(1,8),F(1,3),F(1,2)):
                    for z in (F(0),F(1,3),F(1)):
                        for selected in range(m):
                            new_leaves,new_hub=star_step(leaves,z,selected,rho,eps)
                            assert leaves==new_leaves
                            assert new_hub==(1-rho)*z+rho*leaves[selected]
                            checked+=1
    return checked

def test_biased_moment_recursion():
    checked=0
    for m in range(2,11):
        for k in range(1,m):
            p=F(k,m)
            for rho in (F(1,10),F(1,3),F(1,2)):
                q=1-rho
                target=rho*p*(1-p)/(2-rho)
                assert target==q*q*target+rho*rho*p*(1-p)
                for t in range(1,16):
                    assert target*(1-q**(2*t))==q*q*target*(1-q**(2*(t-1)))+rho*rho*p*(1-p)
                    checked+=1
    return checked

if __name__=='__main__':
    c5=test_frozen_stars()
    c6=test_biased_moment_recursion()
    print('STAR_VERIFY_OK', 'directed frozen-star updates',c5,'biased moments',c6)
