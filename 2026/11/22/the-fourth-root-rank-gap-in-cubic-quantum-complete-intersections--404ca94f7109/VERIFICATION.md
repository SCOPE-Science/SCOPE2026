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

The proof derives a full multiplication table and reduced commutator matrix over any field, then exhaustively counts disjoint rank strata. The standalone checker independently constructs the full PBW commutator matrix and evaluates its rank without using the reduced symbolic proof matrix.

Run `python3 checker.py` with Python 3. The captured successful output is `checker-output.txt`. Exhaustive tests cover all seven active coefficient coordinates for the indicated field/twist pairs, with scalar and socle coefficients free; larger prime fields are sampled. The checker includes an explicit degree-two polynomial model for \(\mathbb F_4\). Direct enumeration at finitely many fields does not constitute a proof of the universal formula; the normal-form and rank-stratum argument supplies that proof. No independent mathematical audit has been performed.
