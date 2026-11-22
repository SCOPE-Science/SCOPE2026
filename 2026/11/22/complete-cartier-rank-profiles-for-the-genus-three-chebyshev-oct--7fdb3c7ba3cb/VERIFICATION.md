---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The general theorem is proved by a tame degree-two quotient and exact monomial Hasse–Witt support; no extrapolation from experiments is needed. In the genus-seven cover \(w^2=z^{16}+1\), the involution identifies pairs of holomorphic differentials indexed by \((1,7),(2,6),(3,5)\). The nonzero Hasse–Witt arrows are computed exactly by multiplication by \(p\) modulo 16, and their binomial coefficients are all invertible modulo \(p\). The three-dimensional restriction therefore gives exact ranks at every prime \(p\ge5\).

Execute the standalone source `check_chebyshev_octic.py` with Python 3. It independently constructs the genus-three hyperelliptic Hasse–Witt matrix directly from the octic polynomial for every prime \(5\le p<200\), checks ranks through the third power, and checks the eight residue-arrow computations. At preparation, all 44 prime tests passed. This is a finite reproducibility check only; it is not an independent audit and does not establish unproved Newton-slope properties.
