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

# Verification and limits
Run `python verify.py` using Python 3 and SymPy. The script constructs a finite cellular model for each \(3\le m\le11\) and \(1\le k<2m\), with one sphere sheet for every permitted polar part and a separate edge at each end of its capped cylinder. It checks that the two cellular boundary maps compose to zero, computes the exact rational matrix ranks, and compares the three Betti numbers against the theorem in 117 cases. It also checks Euler characteristics, including the \(k=1\) exception. Expected and observed output is `ALL_VERIFY_OK cases=117 max_total_cells=75`.

The checker only tests finite instances and rational ranks, not arbitrary parameters or integer torsion. The proof of the integral homotopy classification is the uniform orbit-sheet homeomorphism and graph-of-spheres contraction in `RESULT.md`. The record does not claim any external or independent audit.
