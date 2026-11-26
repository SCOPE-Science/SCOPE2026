---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Since the unerased frame has operator 2I and the erased columns have rank at most 4<N, the largest retained eigenvalue is 2. The smallest is 2 minus the top erased-Gram eigenvalue; the latter is 1 plus the operator norm of the cross block in a mixed mask, and 1 for a single-basis mask. Thus the first three minima are as stated. For 2+2, diagonal phase changes give a 2×2 matrix proportional to [1 1; 1 ω^t], giving Gram eigenvalues 1±σ_+(t), 1±σ_−(t). They transfer to the retained spectrum with the N−4 copies of 2. Over nonzero differences, the maximal cross norm occurs at t=±1 in prime order and at t=0 in composite order, the latter attained by a proper factor pair. Both strictly beat the 3+1 norm √(3/N); the minima are positive and the condition number is the ratio of singular values, hence the square root stated. In prime order there are N Fourier pairs per unordered coordinate pair. In composite order there are gcd(h,N)−1 nonzero Fourier differences for each ordered coordinate difference h and N starting points per ordered pair in each basis; divide by four. The N=4 example has cross norm one and destroys spanning, and in smaller dimensions with four columns to erase not enough columns remain. A fresh independent NumPy check of all 9,211 masks in dimensions 5–9 and all 2,846 complete 2+2 spectra found the expected optima and counts (50, 36, 147, 80, 81). Replay files: branches/2285f9c1-b1bd-4abc-937c-538e2208421b/independent_fourier_erasure_check.py and independent_fourier_erasure_check.log. The finite numerical check is not the all-dimensional proof; the frozen script was not run.

## originality

PASS

The orthogonal-block reduction, norm/Gram equivalence, and elementary Fourier-minor identity are standard. The supported distinct result is the sharp optimization over all four-column deletion patterns in the full coordinate–Fourier union in every order, with the exact equality set and count and the first arithmetic distinction. The closest general guarantees and exact harmonic-frame results inspected do not give that classification.

## value

PASS

The smallest retained frame bound is a deterministic stability guarantee for a canonical measurement frame. Identifying the first deletion size at which nonzero zero-divisors affect that guarantee gives a mathematical reason for the four-erasure cutoff. The equality masks and complete 2+2 spectra make the result useful beyond a uniform sufficient bound, including the loss of spanning in dimension four.

The dated certificate retains the supplied scientific assessment, sources and limitations.
