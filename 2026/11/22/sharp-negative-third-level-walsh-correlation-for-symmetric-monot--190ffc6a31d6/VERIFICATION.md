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

# Analytical and computational verification

The proof in `RESULT.md` covers all integers \(n\ge3\) and all real permutation-invariant nondecreasing functions into \([0,1]\). It uses an exact Fourier conditioning identity, a signed binomial difference factorization, a convex threshold representation and local central binomial asymptotics. The sharpness witnesses are actual threshold functions; every equality pair is characterized by convex mixtures of extreme-threshold witnesses.

Run `python3 check_level3.py` from the directory containing this file. Using only Python standard-library exact arithmetic, the checker verifies all peak-index sets, third-level threshold-coefficient identities and exhaustive threshold-pair products for dimensions \(3\le n\le120\) (7,257 threshold identities). It also calculates the Walsh coefficients directly from every cube vertex in dimensions \(3\le n\le8\), independently of the derived polynomial identity. A passing run prints `PASS` with counts.

The computation is finite; it does not establish the infinite-dimensional theorem by enumeration. The analytic argument, including its assumptions and the asymptotic estimate, must be reviewed independently for external validation. No independent audit has been performed.
