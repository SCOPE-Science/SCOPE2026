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

Execute `python3 cross_eighth_check.py` in a directory containing the script. The check computes, using integer arithmetic, every Laurent phase coefficient from the direct fourth-power Fourier convolution for dimensions two through six. It compares the results with the proposed sum-of-squares formula, tests selected closed coefficient identities and checks endpoint polynomial values. The expected final output is `EXACT_CROSS_EIGHTH_PASS`.

The observed result was `EXACT_CROSS_EIGHTH_PASS`, with 481 exact Laurent coefficients compared. This is a finite supplemental calculation, not a proof for unbounded dimension. The proof of the general identity is the multinomial classification and coefficient formulas in `RESULT.md`. Dimension three is an explicit check against a previously available theorem, not a new-claim dimension.

No independent scientific audit, independent numerical replication or external certification is claimed. Prior mathematical literature may contain equivalent identities not located in the documented searches.
