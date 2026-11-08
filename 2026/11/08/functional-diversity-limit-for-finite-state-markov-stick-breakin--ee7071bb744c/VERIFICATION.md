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

# Reproducibility and verification

Execute `python3 verify.py` using only Python's standard library. It checks exact two-state stationary probabilities, the nonconstant transition eigenvalue, the asymptotic Brownian variance coefficient, 65 exact lag-covariance identities, 11 finite enumerations of all Markov state paths, and 19 geometric-series consistency cases. The current saved execution returns 121 exact rational checks passed.

The finite enumerations and rational identities check the stated covariance and normalization, not convergence of the occupancy process. The full mathematical verification is the proof in `RESULT.md`: uniformly bounded Markov break fractions yield a high-probability \(O(\log\log n)\) occupancy/renewal coupling, a finite-state martingale functional central limit theorem supplies the log-residual-walk limit, and the inverse-map theorem yields the distinct-species functional limit. A Borel--Cantelli subsequence argument provides the almost-sure law.

No independent audit, proof-assistant certification, or empirical confirmation of an infinite theorem is claimed. Historical priority remains subject to further checking of general stationary-frequency occupancy theorems.
