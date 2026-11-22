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

The companion standalone Python 3 program `verify.py` has no third-party dependencies. Run `python3 verify.py` in this directory; `check_output.txt` records the actual run. Its independent direct finite-diagram count checks 36 cases over all parameter partitions with at most four vertices and new tuple arity at most three. The complementary block-based enumerator counts separately using assignments of new equivalence classes. The direct routine does not use the claimed moment polynomial.

The script computes all integer partitions through size twelve and verifies the first one-type collision and exact binary separation. It also checks the odd moment diagonal for the first seven arities and five explicit no-bounded-arity polynomial witnesses. These computations are not proofs of the infinite reconstruction theorem. The proof uses exact block classification, partition-lattice Möbius inversion, parity of the diagonal coefficient, Newton identities, and a nonvanishing polynomial evaluation. The first unary collision minimality is certified by complete finite enumeration.

No independent audit has been performed. This verification does not certify exhaustive publication priority, a sharp recovery bound for each fixed parameter cardinality, or old graph reconstruction beyond the equivalence-class profile.
