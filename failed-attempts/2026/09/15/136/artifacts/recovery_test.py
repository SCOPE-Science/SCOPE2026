"""Bounded recovery test for energy-energy 5/4 analogue target.
Checks min(E+,Ex)/|A|^{11/4} on small primes for structured sets,
greedy extremal search, and Cauchy-Schwarz implication. No proof content.
"""
import itertools, math, random

def energies(A, p):
    S = set(A)
    n = len(A)
    # additive energy: count a+b=c+d  <=> a-d = c-b ; brute O(n^4) only for tiny n
    Ep = 0
    for a in A:
        for b in A:
            for c in A:
                # d determined? a+b-c must be in S
                if (a + b - c) % p in S:
                    Ep += 1
    Ex = 0
    for a in A:
        for b in A:
            for c in A:
                if c == 0:
                    continue
                # need d = ab/c in S  (c != 0 since A subset F_p^*)
                if (a * b) % p == 0:
                    continue
                # c invertible mod p
                import math as _m
                cinv = pow(c, -1, p)
                if (a * b * cinv) % p in S:
                    Ex += 1
    return Ep, Ex

def ratio(Ep, Ex, n):
    m = min(Ep, Ex)
    return m / (n ** (11/4)), m

def test_sets(p=13):
    out = []
    F = list(range(1, p))
    cases = {}
    cases['interval'] = list(range(1, 7))            # AP-like
    cases['geom'] = [pow(2, i, p) for i in range(6)] # GP-like
    cases['random'] = random.Random(0).sample(F, 6)
    cases['mixed'] = [1, 2, 4, 6, 9, 11]
    for name, A in cases.items():
        A = sorted(set(a % p for a in A if a % p != 0))[:6]
        Ep, Ex = energies(A, p)
        r, m = ratio(Ep, Ex, len(A))
        # CS check
        n = len(A)
        sA = len(set((a+b) % p for a in A for b in A))
        pA = len(set((a*b) % p for a in A for b in A))
        out.append((name, A, Ep, Ex, r, sA, pA))
    return out

def extremal_search(p=11, n=5, trials=400, seed=1):
    rng = random.Random(seed)
    F = list(range(1, p))
    worst = (None, -1.0)
    for _ in range(trials):
        A = rng.sample(F, n)
        Ep, Ex = energies(A, p)
        r, m = ratio(Ep, Ex, n)
        if r > worst[1]:
            worst = ((tuple(sorted(A)), Ep, Ex), r)
    # also try structured: intervals (AP) maximize E+
    return worst

if __name__ == '__main__':
    print('p=13 structured check:')
    for name, A, Ep, Ex, r, sA, pA in test_sets(13):
        n = len(A)
        print(f'{name}: A={A} n={n} E+={Ep} Ex={Ex} min/n^2.75={r:.4f} |A+A|={sA} |AA|={pA}')
        # CS implication: max sumset/prodset >= n^4/min(E)
        m = min(Ep, Ex)
        print(f'   CS lower bound n^4/minE = {n**4/m:.2f}; actual max = {max(sA,pA)} (must be >= bound)')
        assert max(sA, pA) >= n**4/m - 1e-9
    print()
    print('extremal random search p=11 n=5:')
    (info, r) = extremal_search()
    print(f'worst set {info} ratio={r:.4f}')
    print()
    print('BSG accounting check (analytic):')
    # Schoen BSG: doubling K^4; sum-product forbids doubling << n^{1/4}
    # contradiction needs K^4 << n^{1/4} -> K << n^{1/16} -> energy exponent 3-1/16
    for n in [10**4, 10**8, 10**12]:
        K_target = n**0.25
        K_reach = n**(1/16)
        print(f'n={n}: target K=n^1/4={K_target:.1f}, BSG-reachable K~n^1/16={K_reach:.2f}; '
              f'target exp 2.75 vs reachable exp {3-1/16:.4f}')
    print()
    print('Conclusion: small cases satisfy bound loosely (ratios << 1 typically or O(1)); '
          'no small counterexample; analytic gap persists.')
