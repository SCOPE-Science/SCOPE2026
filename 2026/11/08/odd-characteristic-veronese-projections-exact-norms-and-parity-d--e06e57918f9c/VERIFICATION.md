---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The actual RESULT.md derives the full-cone multiplier kernel (1+G(A))/(2q^{m(m+1)/2}), diagonalizes symmetric quadratic forms by rank/type and uses orthogonal-orbit counts for even-rank discriminant imbalance q^{-r/2}; the displayed rank counts sum to q^{m(m+1)/2}. Reconstructed Gaussian sums and all symmetric matrices for q=3,5,7,m=2 gave L=2.080222610686, 3.257312629200, 4.431876640769, agreeing with the formula. Independent high-precision rank-sum calculations at m=8..17 gave q^m(H_m-S_q) approaching the two claimed C_q,parity constants for q=3 and 5; the proof's Euler-product expansion and super-exponential nullity tail, rather than finite tests, justify fixed-q asymptotics. Boundary rank zero and q mod 4 imaginary phase are included. Only odd q and fixed q in asymptotics are claimed.

## originality

PASS

Exact rank-one-cone endpoint operator norm and two positive parity corrections are assembled from classical Gauss sums, orthogonal type counts and Fulman–Goldstein nullity law; none of the checked source statements explicitly gives this complete L1 convolution norm or the two-term coefficient. Historical priority is qualified because Hodges's symmetric-matrix exponential-sum full article could not be accessed with lawful routes.

## value

PASS

An exact sharp L1 and Linfinity projection norm on a canonical finite-field Veronese cone controls endpoint amplification, and the positive two-parity finite-size bias gives usable precise asymptotics. This is a natural spectral quantity, not a decorative rank-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
