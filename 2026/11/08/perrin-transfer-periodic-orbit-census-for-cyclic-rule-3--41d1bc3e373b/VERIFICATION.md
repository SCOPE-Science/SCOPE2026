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

# Computation and proof cross-checks

Two standalone Python 3 programs require only the standard library. Run them in the same directory as the scripts with `python3 verify_rule3.py` and `python3 verify_independent.py`.

`verify_rule3.py` constructs every labelled state on rings of lengths \(3\) through \(14\) and applies the local Rule 3 update directly. It compares the computed recurrent state set to cyclic avoidance of \(101\), checks the cubic shift law on every state, and verifies \(204\) time-dependent fixed-point counts for temporal exponents from \(1\) through \(2n\).

`verify_independent.py` separately enumerates words of lengths \(1\) through \(18\), comparing direct pattern-avoidance and maximal-independent-set indicators against the two transfer-matrix traces and the Perrin recurrence. It also uses arithmetic Möbius inversion to check the complete nonnegative integral temporal-orbit decompositions on rings of lengths \(3\) through \(19\). Captured output logs are included and show both scripts passing.

The proof's essential nonstandard step—odd temporal fixed points on a periodic ring correspond to maximal independent sets on a coprime step-cycle—is established directly in RESULT.md. Neither exhaustive tests through finite lengths nor an observed sequence would justify the claims for arbitrary \(n\); that generality rests on the displayed Boolean identities and the transfer-graph bijections. There has been no external independent audit.
