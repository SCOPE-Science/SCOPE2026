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

# Verification and reproducibility

The proof in `RESULT.md` is an analytical proof for every integer \(k\ge1\), not an extrapolation of finite experiments. The earlier entropy and intrinsic-ergodicity results used are identified by exact theorem numbers and source.

The standalone Python 3 standard-library program `check.py` was run directly from the same package folder and printed:

`VERIFY_OK exact_phase_convolutions=252 finite_tail_checks=65 coboundary_tests=8313`

Checks: exact rational evaluation for every phase and residue when \(2\le N\le22\), including the normalization and closed correlation formula; independently truncated double-geometric enumeration for \(2\le N\le11\) with a proven omitted-mass bound; and precise integer verification of generator-by-generator height jumps and multi-step telescoping for \(2\le N\le18\). All necessary files are contained in the package.

Limits: finite checks cannot prove a result for infinitely many parameters, stochastic independence, ergodic maximality, or convergence in law. Those statements rely on the explicit inverse coding, Reyes' maximal-entropy uniqueness, Bernoulli mixing, finite geometric sums, and exponential integrability proven in `RESULT.md`. The originality survey has a historical-priority residual risk. Independent validation is not performed.
