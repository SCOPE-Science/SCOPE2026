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

# Reproducible checks

Run `python3 verification/check_cycle_extensions.py` after installing NumPy. The script enumerates integer-valued one-Lipschitz dual potentials anchored at the first vertex for graph cycles with \(3\le n\le12\), computes rational support-function values of the uniform measure, each antipodal pair, and signed perturbation examples, and checks the exact distance-matrix row-sum identity. It prints `SIGNED_CYCLE_CHEBYSHEV_SIMPLEX_ALL_CHECKS_PASS` on success. The enumeration is a finite check; the theorem for all \(n\ge3\) and all admissible real \(R\) relies on the complete analytic proof in RESULT.md. No external or independent validation has been performed.
