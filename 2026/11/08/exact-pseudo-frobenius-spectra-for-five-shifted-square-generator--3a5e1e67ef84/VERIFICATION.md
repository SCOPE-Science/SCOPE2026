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

# Checks and limits

The standard-library program `square_pf_verify.py` was executed and its exact output preserved as `square_pf_verify.log`. It constructs the 16 coin-length residues, verifies the 16-shift rule for numbers through 20,001 (diagnostic only), evaluates every one of the 256 table predicates, and checks all wrap conditions in the 16 representative parameter classes. Its independent shortest-path Apéry calculation compares the theorem with exact pseudo-Frobenius sets for each integer parameter from 34 through 512 and five further parameters through 4,096. Seven direct gapset checks avoid reliance on the Apéry implementation. The failure at 33 is checked by an explicit missing semigroup member.

The proof covers infinitely many parameters because the coin-length recurrence establishes stabilization by strong induction and because the 256 finite symbolic cases transfer unchanged or monotonically for all larger parameters. Neither the finite diagnostic checks nor the output log alone establishes the infinite statement. Other published literature may contain equivalent results. Independent audit has not been performed.
