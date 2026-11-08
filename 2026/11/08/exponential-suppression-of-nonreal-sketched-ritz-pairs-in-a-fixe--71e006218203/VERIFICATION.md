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

The standard-library executable `verify_srr.py` checks the exact rational trace-discriminant identity across 3,000 inputs, an exact full-rank three-row witness, and the consistency of the derived Gaussian parabola event and the original sketched two-by-two discriminant. It independently samples the original Gaussian sketches at four sketch dimensions and compares their event frequencies to one-dimensional angular quadrature. It also evaluates scaled asymptotic ratios at five larger sketch dimensions.

Reproduction: run `python3 verify_srr.py` in the directory containing this file. The script prints the number of supplementary assertions and selected numerical outcomes; it requires only Python 3 and its standard library. The statistical and numerical comparisons are not proofs of the distribution law, the infinite-domain integral or the infinite-sketch limit. Those follow from the Wishart mixture calculation, exact discriminant identity, polar integration and dominated convergence in `RESULT.md`.

The mathematics is reviewed within the same research process only. No external or independent mathematical validation is claimed.
