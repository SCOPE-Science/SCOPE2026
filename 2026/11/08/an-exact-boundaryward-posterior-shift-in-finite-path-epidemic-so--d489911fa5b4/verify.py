"""Independent finite-state checks for known-age SI source inference on paths.
Run with Python 3 using only the standard library: python verify.py.
The mathematical proofs are analytic; grid checks are diagnostic, not proofs.
"""
from math import exp, factorial, isclose

CHECKS = 0

def check(truth, label):
    global CHECKS
    CHECKS += 1
    if not truth:
        raise AssertionError(label)


def poisson_tail(r, u):
    if r <= 0:
        return 1.0
    term = exp(-u) * (u ** r) / factorial(r)
    result = term
    for j in range(r + 1, 260):
        term *= u / j
        result += term
        if term < 1e-19 and j > max(20, int(2*u)):
            break
    return result


def formula_likelihood(s, k, u):
    return poisson_tail(s - 1, u) * exp(-u) * u**(k-s)/factorial(k-s)


def uniformized_likelihood(n, s, k, u):
    """Direct CTMC calculation: independent of Poisson frontier-tail formula.

    Uniformization at total rate 2 per unit rescaled time, even at
    partially saturated boundaries. State is the currently infected interval.
    """
    state = {(s, s): 1.0}
    poisson_weight = exp(-2*u)
    result = 0.0
    total_weight = 0.0
    for step in range(180):
        result += poisson_weight * state.get((1, k), 0.0)
        total_weight += poisson_weight
        if poisson_weight < 1e-18 and step > max(20, 4*u):
            break
        nxt = {}
        for (left, right), mass in state.items():
            choices = 0
            if left > 1:
                dest = (left - 1, right)
                nxt[dest] = nxt.get(dest, 0.0) + 0.5*mass
                choices += 1
            if right < n:
                dest = (left, right + 1)
                nxt[dest] = nxt.get(dest, 0.0) + 0.5*mass
                choices += 1
            nxt[(left, right)] = nxt.get((left, right), 0.0) + (1-0.5*choices)*mass
        state = nxt
        poisson_weight *= (2*u)/(step+1)
    check(abs(total_weight-1.0) < 1e-12, 'uniformization total mass')
    return result


def posteriors(k, u, prior=None):
    if prior is None:
        prior = [1.0]*k
    weights = [prior[s-1]*formula_likelihood(s,k,u) for s in range(1,k+1)]
    z = sum(weights)
    return [w/z for w in weights]


def main():
    for n in range(4, 11):
        for k in range(2, n):
            for u in (0.08, 0.25, 0.7, 1.0, 2.0, 4.0, 8.0):
                for s in range(1, k+1):
                    a = formula_likelihood(s,k,u)
                    b = uniformized_likelihood(n,s,k,u)
                    check(isclose(a,b,rel_tol=3e-11,abs_tol=4e-14),
                          f'CTMC mismatch: n={n},k={k},s={s},u={u}: {a} vs {b}')
    for k in range(3, 15):
        for u in (0.01, 0.03, 0.1, 0.4, 1.0, 2.0, 5.0, 10.0, 25.0):
            lik = [formula_likelihood(s,k,u) for s in range(1,k+1)]
            ratios = [lik[s+1]/lik[s] for s in range(k-1)]
            for s in range(len(ratios)-1):
                check(ratios[s] > ratios[s+1], 'strict spatial ratio decline')
            check(abs(sum(posteriors(k,u))-1)<2e-14, 'posterior normalized')
        for u,v in ((0.01,0.03), (0.03,0.2), (0.2,1.0), (1.0,3.0),(3.0,8.0)):
            p, q = posteriors(k,u), posteriors(k,v)
            for cutoff in range(1,k):
                check(sum(p[:cutoff]) < sum(q[:cutoff]), 'MLR stochastic source shift')
            # Robustness under a nonuniform strictly positive prior.
            prior = [s*s + (k-s+1)/4 for s in range(1,k+1)]
            pp, qq = posteriors(k,u,prior), posteriors(k,v,prior)
            for cutoff in range(1,k):
                check(sum(pp[:cutoff]) < sum(qq[:cutoff]), 'arbitrary prior stochastic shift')
    for k in range(3,18):
        thresholds = []
        for s in range(1,(k-1)//2+1):
            def ratio(u):
                return (k-s)*poisson_tail(s,u)/(u*poisson_tail(s-1,u))
            left,right=0.00001,float(2*k+2)
            check(ratio(left)>1 and ratio(right)<1,'root bracket')
            for _ in range(100):
                mid=(left+right)/2
                if ratio(mid)>1:
                    left=mid
                else:
                    right=mid
            root=(left+right)/2
            thresholds.append(root)
            check(abs(ratio(root)-1)<2e-12, 'root equation')
            post=posteriors(k,root)
            check(abs(post[s-1]-post[s])<1e-12, 'adjacent posterior tie')
            check(all(post[s-1]>=v-1e-12 for v in post), 'tie is global MAP')
        check(all(a>b for a,b in zip(thresholds,thresholds[1:])), 'ordered thresholds')
    print(f'PASS {CHECKS} independent CTMC, posterior, and threshold diagnostics')
    print('k=5 transitions: s=3 -> 2 -> 1, approximately 2.149126 and 3.920690 in scaled time')
    print('Finite-grid calculations are not proofs of the universal claims.')

if __name__ == '__main__':
    main()
