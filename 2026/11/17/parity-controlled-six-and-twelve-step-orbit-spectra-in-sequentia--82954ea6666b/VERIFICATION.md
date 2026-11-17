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

The theorem is proved by the explicit petal-pair recurrence and invariant quotient/direct-sum analysis in RESULT.md. This file records reproductions, not an independent audit or formal proof certification.

Execute `python3 checks/verify_state.py`: all 43,688 labelled binary configurations on friendship graphs with 1 through 7 petals are enumerated, their least periods determined by direct stepping, and the period distributions compared to the theorem. The recorded output is in `checks/state_output.txt`.

Execute `python3 checks/verify_linear.py`: an independent row-operation construction of the GF(2) sweep matrix is tested for 40 petal counts and 12 positive exponents per count. Each rank is compared to the exact fixed-space formula, and the claimed global period identity is confirmed. Output is in `checks/matrix_output.txt`.

Finite tests do not replace the full all-parameter proof. No external mathematical validation or outside certification is asserted. Historical priority remains subject to additional literature review.
