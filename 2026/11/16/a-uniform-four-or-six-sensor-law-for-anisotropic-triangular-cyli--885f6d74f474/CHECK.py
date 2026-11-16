"""Finite numerical corroboration for the odd triangular-cylinder sampling theorem.

The analytic Vandermonde proof in RESULT.md covers all odd cycle lengths;
these finite floating-point checks are not substituted for that proof.
"""
import math
import numpy as np


def spectrum(N, gamma):
    mu = [2*math.cos(2*math.pi*s/N) for s in range((N+1)//2)]
    groups = {}
    for r in range(3):
        for k in range(N):
            x = ((2 if r == 0 else -1) + gamma*mu[min(k, N-k)])/(2*(1+gamma))
            key = round(x, 9)
            groups.setdefault(key, []).append((r, k))
    return groups


def sampling_matrix(N, sites, frequencies):
    return np.array([
        [np.exp(2j*math.pi*(r*x/3 + k*y/N)) for r, k in frequencies]
        for x, y in sites], dtype=complex)


def rank(A):
    return int(np.linalg.matrix_rank(A, tol=1e-7))


def main():
    assertions = 0
    cases_checked = 0
    for N in range(3, 36, 2):
        mu = [2*math.cos(2*math.pi*s/N) for s in range((N+1)//2)]
        resonant = {3/(mu[t]-mu[s]) for t in range(len(mu)) for s in range(t+1, len(mu))}
        six = {3/(mu[t]-mu[s]) for t in range(1, len(mu)) for s in range(t+1, len(mu))}
        points4 = [(0,0), (0,1), (1,1), (1,2)]
        points6 = [(x, y) for x in range(3) for y in (0, 1)]
        cases = [(v, v in six) for v in resonant] + [(0.47, False), (math.sqrt(2), False), (2.73, False)]
        for gamma, expected_six in cases:
            groups = spectrum(N, gamma)
            maxdim = max(map(len, groups.values()))
            assert maxdim == (6 if expected_six else 4), (N, gamma, maxdim)
            assertions += 1
            points = points6 if expected_six else points4
            for idx in groups.values():
                F = sampling_matrix(N, points, idx)
                assert rank(F) == len(idx), (N, gamma, idx)
                assertions += 1
            cases_checked += 1
    # Verify actual finite-time observation rank, including a six-site resonance.
    for N in (3, 5, 7, 9):
        mu = [2*math.cos(2*math.pi*s/N) for s in range((N+1)//2)]
        six = [3/(mu[t]-mu[s]) for t in range(1, len(mu)) for s in range(t+1, len(mu))]
        for gamma in [0.47] + six[:1]:
            groups = spectrum(N, gamma)
            is_six = len(max(groups.values(), key=len)) == 6
            points = [(x,y) for x in range(3) for y in (0,1)] if is_six else [(0,0),(0,1),(1,1),(1,2)]
            freqs = [(r,k) for r in range(3) for k in range(N)]
            eig = {(r,k): ((2 if r==0 else -1)+gamma*mu[min(k,N-k)])/(2*(1+gamma)) for r,k in freqs}
            A = np.array([[eig[f]**t*np.exp(2j*math.pi*(f[0]*x/3+f[1]*y/N))
                           for f in freqs] for t in range(N+1) for x,y in points], dtype=complex)
            assert rank(A) == 3*N, (N, gamma, rank(A))
            assertions += 1
    print(f"PASS: {cases_checked} parameter cases; {assertions} finite assertions")


if __name__ == "__main__":
    main()
