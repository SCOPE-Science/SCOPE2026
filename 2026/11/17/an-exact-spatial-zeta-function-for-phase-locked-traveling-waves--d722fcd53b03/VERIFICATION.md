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

# Reproducible mathematical checks

Run `python verification/check_rule6.py` with Python 3 and `sympy`. The file constructs the exact sixteen-state transfer operator using the five-neighborhood Rule 6 phase-lock equation and obtains symbolic expressions for \(\det(tI-T)\) and \(\det(I-zT)\), which establish the zeta formula for all ring lengths. It separately and exhaustively tests all indexed binary configurations of sizes \(3\) through \(15\), comparing the phase-lock predicate against matrix traces. That direct check covers 65,528 labelled inputs; it verifies return after \(2n\) updates on all accepted words. Output captured in `verification/check_rule6.out`.

The finite direct enumeration is not claimed to establish the infinite theorem. No external independent audit was performed. The program's dependencies and command are stated in the source and this file. General Rule 6 recurrent states and general wave velocities remain outside the claim.
