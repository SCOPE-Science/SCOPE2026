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

# Verification and boundaries

The polynomial recurrence in `RESULT.md` was independently instantiated in `check_local.py` using exact SymPy expressions. The source file was executed in the package working directory and reported `ALL EXACT SAMPLE CHECKS PASSED` for degrees \(5,7,11,13,17,19,23,25,29,31\). For each degree it checked the highest homogeneous part, the point-at-infinity tangent factor, the generic-branch polynomial's nonzero squarefree roots, and the equality of local delta with arithmetic-genus defect. The small degrees \(5,7\) are outside the theorem and function only as consistency checks.

The universal proof uses invariant theory, local algebraic expansions and the cyclic order-three stabilizer of the triple-cycle fixed point. This is not an infinite computational certificate. Numerical or finite symbolic checks cannot by themselves establish squarefreeness at every degree; the proof establishes orbit separation and transversality uniformly in characteristic zero. The source article is used for its verified affine quotient model and genus, not as evidence for the new local branches.

No independent audit or external formal certification has been performed.
