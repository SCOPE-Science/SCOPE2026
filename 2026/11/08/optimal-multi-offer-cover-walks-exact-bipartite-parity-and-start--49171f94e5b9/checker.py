"""Exact checks for multi-offer cover walks on complete bipartite graphs.

Only Python standard library is needed. The infinite results are proved in RESULT.md;
these finite rational checks are independent reproducibility tests, not infinite proofs.
"""
from fractions import Fraction
from itertools import product


def fvals(n, d, horizon):
    """Completion CDF from one initially collected label, by count-state recursion."""
    state = [Fraction(0) for _ in range(n+1)]
    state[1] = Fraction(1)
    out = [state[n]]
    for _ in range(horizon):
        nxt = [Fraction(0) for _ in range(n+1)]
        for j in range(1, n):
            q = Fraction(j, n) ** d
            nxt[j] += state[j] * q
            nxt[j+1] += state[j] * (1-q)
        nxt[n] += state[n]
        state = nxt
        out.append(state[n])
    return out


def labeled_cover(a, b, d, start_a, horizon):
    """Independent labeled-mask enumeration of actual offered neighbors."""
    n = a+b
    A = tuple(range(a))
    B = tuple(range(a, n))
    start = A[0] if start_a else B[0]
    states = {(start, 1 << start): Fraction(1)}
    full = (1 << n)-1
    out = [sum((v for (pos, mask), v in states.items() if mask == full), Fraction(0))]
    for _ in range(horizon):
        nxt = {}
        for (pos, mask), prob in states.items():
            targets = B if pos < a else A
            weight = prob / (len(targets)**d)
            for offered in product(targets, repeat=d):
                new_targets = [x for x in offered if not (mask >> x) & 1]
                chosen = new_targets[0] if new_targets else offered[0]
                key = (chosen, mask | (1 << chosen))
                nxt[key] = nxt.get(key, Fraction(0)) + weight
        states = nxt
        out.append(sum((v for (pos, mask), v in states.items() if mask == full), Fraction(0)))
    return out


def computed_cover(a,b,d,horizon):
    F_a = fvals(a,d,horizon)
    F_b = fvals(b,d,horizon)
    def val(F, t):
        return F[t] if t>=0 else Fraction(0)
    ans_a,ans_b=[],[]
    for t in range(horizon+1):
        if t%2:
            k=(t-1)//2
            ans_a.append(F_a[k]*F_b[k])
            ans_b.append(F_a[k]*F_b[k])
        else:
            k=t//2
            ans_a.append(F_a[k]*val(F_b,k-1))
            ans_b.append(val(F_a,k-1)*F_b[k])
    return ans_a,ans_b


def execute():
    totals = {'labeled_cdf_equalities':0,'parity_equalities':0,'strict_even_inequalities':0,'lr_minors':0}
    for a in range(1,5):
        for b in range(1,5):
            for d in (2,3):
                horizon=10
                f_a,f_b=computed_cover(a,b,d,horizon)
                x_a=labeled_cover(a,b,d,True,horizon)
                x_b=labeled_cover(a,b,d,False,horizon)
                for t in range(horizon+1):
                    assert f_a[t]==x_a[t],('CDF-A',a,b,d,t,f_a[t],x_a[t])
                    assert f_b[t]==x_b[t],('CDF-B',a,b,d,t,f_b[t],x_b[t])
                    totals['labeled_cdf_equalities']+=2
                    if t%2:
                        assert f_a[t]==f_b[t]
                        totals['parity_equalities']+=1
                    elif a>b and t//2>=a-1:
                        assert f_a[t]>f_b[t]
                        totals['strict_even_inequalities']+=1
    for d in (2,3,4):
        F={n:fvals(n,d,34) for n in range(1,9)}
        for a in range(2,9):
            for b in range(1,a):
                Fa,Fb=F[a],F[b]
                for k in range(a-1,35):
                    assert Fa[k]*Fb[k-1] > Fa[k-1]*Fb[k],('CDF-ratio',a,b,d,k)
                    totals['strict_even_inequalities']+=1
        # actual mass-function MLR order, with available support
        for n in range(2,8):
            fa,fb=F[n+1],F[n]
            for k in range(n,33):
                p_a=fa[k]-fa[k-1]
                q_a=fa[k+1]-fa[k]
                p_b=fb[k]-fb[k-1]
                q_b=fb[k+1]-fb[k]
                assert q_a*p_b >= p_a*q_b,('MLR',n,d,k)
                totals['lr_minors']+=1
    assert computed_cover(3,2,2,4)[0][-1] == Fraction(10,27)
    print('PASS',totals)
    print('K3,2 two-offer: CDF at t=4 from larger part 10/27, smaller part 0.')
    print('Exact mean advantage from larger part: 23/28 (proved independently using pgfs).')

if __name__ == '__main__':
    execute()
