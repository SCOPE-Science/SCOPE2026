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

# Reproducibility

Execute `python3 verify_path_variance.py` with any reasonably modern Python 3 interpreter; only the standard library is needed. The checker generates the exact polynomial of each path-source outbreak's first two moments independently by enumeration of open-edge subsets, then compares the resulting variance to the closed polynomial in the mathematical proof.

The command checks 45,052 source-edge configurations, 75 moment polynomials, 2,870 coefficient-sign patterns for location comparisons through 41 vertices, and the exact rational examples for six vertices. These computations were successfully executed from the delivered source code before inclusion.

The mathematical proof is not a finite search: its coefficient decomposition establishes one sign change of a polynomial quotient for arbitrary length and pair of source locations, and a strict near-one asymptotic establishes existence of the crossing. The Python checks are reproducibility diagnostics only, not an infinite-length certificate.

No independent scientific validation has been performed. Other epidemic models, general graphs, arbitrary edge probabilities, and temporal outbreak statistics lie outside the theorem.
