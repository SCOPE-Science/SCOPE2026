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

# Reproducibility and scope

Run `python3 verify.py` under ordinary Python 3 (standard library only). The program checks base-\(p\) binomial congruences for every index in each of five prime-power degree ranges, confirms the scroll's rank-one minors on selected complete prime-field affine incidence charts, and counts images there. The recorded execution is in `verification_output.txt`; the terminal marker is `ALL_CHECKS_PASSED`.

The finite point sets and finite degree ranges do not prove a general claim; the general proof is the Lucas congruence plus a triangular parameter inversion and the standard prime scroll ideal. The generic degree \(m\) is established via a function-field valuation, not from prime-field cardinality. The theorem is not independently certified or audited.
