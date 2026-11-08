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

The accompanying `verify.py` is a standalone Python 3 script using only the standard library. Run `python3 verify.py` from the extracted package directory.

The code checks exactly with rational arithmetic, over a bounded grid, the two factorizations used in the proof, the sign-polynomial parameter slope, and positivity of the implicit denominator; it also checks numerical roots, threshold ordering, monotonicity of the threshold frontier, numerical maximizers over dense grids, and finite-difference derivatives. It independently solves the original branching fixed point by monotone iteration and compares it to the canceled-equation root. On execution it printed `PASS 26587 assertions`.

The proof of the all-parameter statement is the explicit Descartes sign-variation, polynomial factorization and strict-monotonicity argument in `RESULT.md`; finite checks alone do not establish these universal statements. The model assumes independent transmissions and an asymptotic configuration-model limit. There is no external validation or independent audit.
