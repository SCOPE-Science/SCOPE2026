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

# Reproducible checks

Run `python verify.py` with a standard Python interpreter. This exhaustively lists all q-ary words and every nonzero cyclic rotation for q=3 and n=2,...,8; q=4 and n=2,...,6; q=5 and n=2,...,5. The checker calculates the complete observed multiplicity histogram from Hamming comparisons and separately computes the Möbius-inverted predicted histogram from the exact formulas. It asserts equality for all 16 complete finite domains, including zero-count cases.

The proof of the general statement requires the referenced Gabrić two-shift lemma, plus the mathematical deductions written in RESULT.md. The numerical checks alone cannot establish an infinite theorem. No independent scientific audit has been performed.
