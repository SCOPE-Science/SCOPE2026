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

# Verification record

The symbolic proof in `RESULT.md` gives a complete two-variable atomic-type inventory and an induction covering all counting thresholds and unrestricted quantifier nesting. It uses the group fact that square roots are unique in finite odd-order groups. This is the decisive nonexperimental argument.

Run `python verify.py` with Python 3.10 or later. The program builds thirteen explicit finite odd-order group multiplication tables, checks identity, inverses and associativity, computes the nonidentity \(3\)-torsion count, enumerates **all** atomic relation evaluations on the variables and the constant, refines the resulting complete pair-type counts with a shared palette, checks predicted positive/negative equivalences, and checks the distinct inverse/square/square-root cases. `verification_output.txt` stores actual standard output from a completed execution.

The verified examples include cyclic and elementary abelian groups of order \(25\), nonabelian and abelian exponent-three groups of order \(27\), and the nonabelian Frobenius group of order \(21\) compared with the abelian group of the same order. The checker is finite and does **not** enumerate all groups of a fixed order or prove the infinite theorem by itself.

The published-source comparison is incomplete historically. Independent expert audit has not been performed.
