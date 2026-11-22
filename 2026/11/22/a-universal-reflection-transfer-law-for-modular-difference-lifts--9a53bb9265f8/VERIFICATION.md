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
# Verification

The `check_reflection.py` program is a finite consistency checker, not an infinite proof. Run with Python 3 using `python3 check_reflection.py`.

Checks completed successfully in the delivered package:
- 18 noble-means triples (3 substitution parameters, 2 moduli, 3 memory lengths), every factor length 1–8.
- 30 periodic-base triples (5 base periods, 2 moduli, 3 memory lengths), every factor length 1–8; the base factor languages in this set are determined exactly by cyclic enumeration.
- The explicit length-0 through length-8 example for substitution parameter 1, modulus 3, memory 3 matches the symbolic formula.

These tests do not replace the full argument: the proof is the reversible-word characterization by the sign change under ordinary reversal plus the orbit count of an affine reflection involution modulo the memory length. No external mathematical audit was performed.
