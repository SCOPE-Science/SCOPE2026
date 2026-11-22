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

The direct checker `verify_frozen.py` compares the full word-by-word star-swap definition against a separately implemented expansion of the composition grammar; it also checks the cubic rational generating function's integer recurrence. The exact checked alphabet/length ranges are documented in the verification script and in RESULT.md. The binomial balanced-census identity through multiplicity six and an explicit family up to multiplicity twenty-four are reproduced.

The proof covers all alphabet sizes and lengths in its stated domain by an exhaustive local analysis of allowable swaps, a unique combinatorial decomposition, and a frequency count. Numerical checks corroborate those deductions but do not extend the stated scope. No independent audit or external certification is claimed.
