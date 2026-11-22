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

The proof is the exact likelihood-ratio pairing of two central Poisson-binomial masses under bit complementation and the interchange of the two survival probabilities. All strictness statements require \(0<\ell<h<1\), \(r\ge1\), equal environmental prior probabilities, and a strict majority criterion for \(2r+1\) individuals.

Run `python3 verify.py` from the same directory to obtain `11303 exact assertions passed`. It uses Python `fractions.Fraction`, no external dependencies, and constructs Poisson-binomial masses by direct convolution. It tests both sides of the central-mass reciprocity and the closed-form adjacent difference; no part of the proof depends upon the finite test grid.

No test supports extending the theorem to even-sized cohorts, arbitrary quorum levels, unbalanced state frequencies, or correlated individuals conditional on state. The biological assumptions are idealizations. Mathematical correctness and historical priority are not independently certified.
