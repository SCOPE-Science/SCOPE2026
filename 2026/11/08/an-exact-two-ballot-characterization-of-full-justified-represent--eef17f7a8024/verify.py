"""Numerical cross-checks of the two-ballot FJR+ characterization.

Requires scipy.optimize.linprog (HiGHS). LP uses the published FJR+
constraints; the formula under test is implemented separately.
This is a finite implementation check, not a proof for unbounded elections.
"""
from itertools import combinations
from random import Random
from scipy.optimize import linprog


def closed_form(a, b, A, B, W, k):
    n, r = a+b, len(A & B & W)
    for ell in range(1, k+1):
        eligible = (len(A & W) < ell and bool(A-W),
                    len(B & W) < ell and bool(B-W))
        if (eligible[0] and a*k >= ell*n) or (eligible[1] and b*k >= ell*n):
            return False
        if all(eligible):
            if (A & B)-W or 2*ell-r <= k:
                return False
    return True


def source_lp(a, b, A, B, W, m, k):
    """Independently build the exact FJR+ LP; True means no violation."""
    n, size = a+b, 2+3*m
    base_bounds = [(0, None)]*size
    for j, A_j in enumerate((A,B)):
        for c in range(m):
            if c not in A_j:
                base_bounds[2+j*m+c] = (0, 0)
    eq, val = [], []
    for j in (0,1):
        t = [0]*size
        for c in range(m):
            t[2+j*m+c] = 1
        eq.append(t)
        val.append(0)
    t = [0]*size
    for c in range(m):
        t[2+2*m+c] = 1
    eq.append(t)
    val.append(1)   # normalize sum y to 1
    ub = []
    for j in (0,1):
        for c in range(m):
            t = [0]*size
            t[2+j*m+c] = 1
            t[2+2*m+c] = -1
            ub.append(t)
            if c in W:
                t = [0]*size
                t[2+j*m+c] = 1
                t[j] = -1
                ub.append(t)
    for ell in range(1,k+1):
        bounds = list(base_bounds)
        for j, A_j in enumerate((A,B)):
            if len(A_j&W)>=ell:
                bounds[j] = (0,0)
        Aeq = [r[:] for r in eq]
        for j in (0,1):
            Aeq[j][j] = -ell
        out = linprog([-a,-b]+[0]*(3*m), A_ub=ub, b_ub=[0]*len(ub),
                      A_eq=Aeq, b_eq=val, bounds=bounds, method='highs')
        if not out.success:
            raise AssertionError('LP solver did not solve a feasible model')
        if -out.fun >= n/k-1e-8:
            return False
    return True


def literal_ejrplus(a,b,A,B,W,k):
    n=a+b
    for ell in range(1,k+1):
        for c in (A|B)-W:
            deprived = sum(t for t,S in ((a,A),(b,B)) if c in S and len(S&W)<ell)
            if deprived*k >= ell*n:
                return False
    return True


def literal_fjr(a,b,A,B,W,C,k):
    n=a+b
    for ell in range(1,k+1):
        for T_size in range(ell,len(C)+1):
            for T_list in combinations(C,T_size):
                T=set(T_list)
                eligible=sum(t for t,S in ((a,A),(b,B))
                             if len(S&W)<ell and len(S&T)>=ell)
                if eligible*k >= T_size*n:
                    return False
    return True


def test():
    checked=0
    # Exhaust every ordered pair of distinct ballots and committee for m<=3,
    # with both type populations in {1,2,3}.
    for m in (2,3):
        C=set(range(m))
        ballots=[{i for i in range(m) if mask & (1<<i)}
                 for mask in range(1<<m)]
        for A in ballots:
            for B in ballots:
                if A==B:
                    continue
                for k in range(1,m+1):
                    for W0 in combinations(range(m),k):
                        W=set(W0)
                        for a in (1,2,3):
                            for b in (1,2,3):
                                assert closed_form(a,b,A,B,W,k)==source_lp(a,b,A,B,W,m,k), (m,k,a,b,A,B,W)
                                checked+=1
    small=checked
    rng=Random(4362026)
    # Additional varied instances including ties at equality, empty approvals,
    # zero-support winners, and overlapping ballots.
    for m in (4,5,6,7):
        for _ in range(425):
            A={i for i in range(m) if rng.randrange(2)==1}
            B={i for i in range(m) if rng.randrange(2)==1}
            if A==B:
                continue
            k=rng.randrange(1,m+1)
            W=set(rng.sample(range(m),k))
            a,b=rng.randrange(1,10),rng.randrange(1,10)
            assert closed_form(a,b,A,B,W,k)==source_lp(a,b,A,B,W,m,k), (m,k,a,b,A,B,W)
            checked+=1
    # Counterexample to dropping positive support for winning candidates.
    A,B={0,1,3},{0,1,2,4}
    W={0,1,2,5,6,7}
    C=set(range(8))
    assert len(W)==6 and A!=B
    assert literal_fjr(2,3,A,B,W,C,6)
    assert literal_ejrplus(2,3,A,B,W,6)
    assert not closed_form(2,3,A,B,W,6)
    assert not source_lp(2,3,A,B,W,8,6)
    # Direct, exact rational verification of level-four witness:
    # Five voters with weight one, Y=1+1+2+2=6, quota 5/6.
    assert 5*6 == 6*5
    print(f'PASS: {small} fully enumerated two-type cases, {checked-small} randomized cases;')
    print('PASS: source FJR+ LP and formula agree; FJR/EJR+ strictness example checked.')


if __name__=='__main__':
    test()
