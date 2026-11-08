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

# Reproduction and limitations
The exact result follows from the symbolic proof in RESULT.md, independently of a finite search. With Python 3, execute `python VERIFY.py` to reproduce the deterministic rational checks of the two-by-two determinant identity, the sharp lower-bound identity, symmetry in both part sizes, representative values and limiting cases. The standard-library checker performs 1,610 parameter/check groups. This test does not itself prove the assertion for all dimensions, replace the order-interval lemma, or independently assess publication priority. An independent mathematical audit has not been performed.
