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

# Verification details

The accompanying `verify_finite.py` is a standalone Python 3 checker using only exact finite-field arithmetic and the standard library. For each candidate it separately tests whether the map is bijective, then checks the square class of every admissible nonzero coefficient and the full cycle-decomposition signature; all arithmetic is finite and integer-exact.

A successful execution printed `ODD_Q_INDEX_TWO_PARITY_OK` for the following tuples in the format \((q,\text{tested maps},\text{permutation maps},\text{admissible zero-coefficient cases},\text{tested exponents})\):

- \((3,108,36,12,3)\)
- \((5,600,160,16,4)\)
- \((7,735,135,15,3)\)
- \((9,3240,432,32,4)\)
- \((11,3630,379,19,3)\)

Total: \(8313\) candidates and \(1142\) positive permutation cases. The \(q=9\) case uses a genuine degree-four extension over the prime field. These finite tests are diagnostic only; the unbounded mathematical statement follows from the coset-sign and Frobenius proof in `RESULT.md`.

The independent-audit field above reports only that no independent audit has yet occurred. No external formal certificate is claimed.
