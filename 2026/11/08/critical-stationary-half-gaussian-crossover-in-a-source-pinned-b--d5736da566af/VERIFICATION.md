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

# Verification details

Run `python verify.py` with Python 3, NumPy, SciPy, and SymPy. The program independently constructs the reduced finite contact-process generator, solves each invariant vector via a sparse stationary linear system, and checks normalization, nonnegativity within numerical tolerances, stationary drift identities, symbolic generator algebra, and Gaussian integral/mean identities. The present package completed 59 asserted checks for offsets \(c=-1,0,1\) and graph part sizes \(n=6,12,24,48\). The corresponding stationary rescaled means increase toward the explicit predictions, providing finite-size consistency evidence rather than a convergence proof.

The unbounded-size theorem is established separately in `RESULT.md` by uniform stationary moment bounds, weak generator convergence, zero-flux uniqueness at the entrance boundary, and uniform integrability. This verification does not assert an external independent check or numerical certification of infinitely many graph sizes.
