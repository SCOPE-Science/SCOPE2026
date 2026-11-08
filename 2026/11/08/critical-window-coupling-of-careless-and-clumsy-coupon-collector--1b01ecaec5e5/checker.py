"""Exact finite-state tests of rare-loss coupon-collector coupling lemmas.

Run with Python >=3.10: python checker.py
These finite tests do not prove the asymptotic statements.
"""
from fractions import Fraction as F
from math import comb

checks = 0

def test(assertion, message):
    global checks
    checks += 1
    if not assertion:
        raise AssertionError(message)


def D0_prob(n, eps, mask):
    if mask == 0:
        return 1-eps
    if mask.bit_count() == 1:
        return eps/n
    return F(0)


def D1_prob(n, p, mask):
    return p**mask.bit_count() * (1-p)**(n-mask.bit_count())


def clumsy_step(n, eps, distribution):
    out = {}
    for state, mass in distribution.items():
        for a in range(n):
            new = state | (1 << a)
            out[new] = out.get(new, F(0)) + mass*(1-eps)/n
            # A clumsy loss refreshes one selected label to absent.
            minus = state & ~(1 << a)
            out[minus] = out.get(minus, F(0)) + mass*eps/n
    return {k:v for k,v in out.items() if v}


def careless_step(n, p, distribution):
    out = {}
    for state, mass in distribution.items():
        for a in range(n):
            augmented = state | (1<<a)
            for mask in range(1<<n):
                after = augmented & ~mask
                prob = D1_prob(n,p,mask)
                out[after] = out.get(after,F(0)) + mass*prob/n
    return {k:v for k,v in out.items() if v}


def joint_step(n, eps, distribution):
    out = {}
    for (b,v), mass in distribution.items():
        for a in range(n):
            bnew=b | (1<<a)
            vnew=v | (1<<a)
            k=(bnew,vnew)
            out[k] = out.get(k,F(0)) + mass*(1-eps)/n
            for j in range(n):
                bn=b & ~(1<<j)
                vn=(v | (1<<a)) & ~(1<<j)
                k=(bn,vn)
                out[k] = out.get(k,F(0)) + mass*eps/(n*n)
    return {k:v for k,v in out.items() if v}


def run():
    for n in range(2,10):
        for c in (F(1,3), F(1), F(2)):
            if c >= n: continue
            eps = c/n
            p = c/(n*n)
            total0=sum((D0_prob(n,eps,m) for m in range(1<<n)),F(0))
            total1=sum((D1_prob(n,p,m) for m in range(1<<n)),F(0))
            test(total0==total1==1, ('loss laws',n,c))
            tv=sum((abs(D0_prob(n,eps,m)-D1_prob(n,p,m)) for m in range(1<<n)),F(0))/2
            exact=eps*(1-(1-p)**(n-1))
            test(tv==exact, ('exact loss-set TV',n,c,tv,exact))
            test(exact<=c*c/(n*n),('TV upper bound',n,c))

    for n in range(2,6):
        for c in (F(1,2),F(1)):
            eps=c/n
            alpha=F(n-1,n)
            beta=1-(1-eps)/n
            dist={0:F(1)}
            joint={(0,0):F(1)}
            for t in range(1,11):
                dist=clumsy_step(n,eps,dist)
                joint=joint_step(n,eps,joint)
                test(sum(dist.values(),F(0))==1, ('clumsy mass',n,c,t))
                test(sum(joint.values(),F(0))==1,('joint mass',n,c,t))
                test(all((b & v)==b for b,v in joint),('subset coupling',n,c,t))
                missing=sum((mass for mask,mass in dist.items() if (mask&1)==0),F(0))
                exact_u=eps+(1-eps)*alpha**t
                test(missing==exact_u, ('missing marginal',n,c,t))
                mismatched=sum((mass for (b,v),mass in joint.items() if b!=v),F(0))
                bound=eps*eps*n/(1-eps) + eps*(1-eps)*t*beta**(t-1)
                test(mismatched<=bound, ('point coupling upper bound',n,c,t,mismatched,bound))
                marginal={}
                for (b,v),mass in joint.items():
                    marginal[b]=marginal.get(b,F(0))+mass
                test(marginal==dist,('joint B marginal',n,c,t))

    for n in range(2,6):
        for c in (F(1,2),F(1)):
            eps=c/n
            p=c/(n*n)
            db={0:F(1)}
            dc={0:F(1)}
            for t in range(1,9):
                db=clumsy_step(n,eps,db)
                dc=careless_step(n,p,dc)
                test(sum(dc.values(),F(0))==1,('careless mass',n,c,t))
                test(sum(db.values(),F(0))==1,('clumsy mass 2',n,c,t))
                # Both models are permutation invariant: equal mass on equal sizes.
                for d in (db,dc):
                    masses_by_size={}
                    for mask,mass in d.items():
                        s=mask.bit_count()
                        if s in masses_by_size:
                            test(masses_by_size[s]==mass,('exchangeability',n,c,t))
                        else:
                            masses_by_size[s]=mass
    print(f'PASS: {checks} exact-rational checks')

if __name__ == '__main__': run()
