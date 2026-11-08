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

The exact formula for regular-simplex face content is derived by counting congruent regular faces. The product-face convolution and codimension-two identity are proved in `RESULT.md`; no finite experiment is treated as proof of a universal assertion.

`verify.py` is a standalone Python 3 standard-library check. It was executed directly from the research package inputs and returned `PASS`, finding 8,188 ordered compositions of dimensions 3 through 13 and 24,567 assertions. Assertions compare direct face-polynomial convolution with the independently organized codimension-two identity and test the claimed sharp bounds and equality types. The script also evaluates the elementary radical inequalities used in the proof. The independently reviewed theorem requires all positive dimensions and is secured by the symbolic inequalities in the proof, not these bounded computations.

The Basit–Lángi single-simplex input is cited as a published theorem and is not claimed to have been independently reproved. Historical originality has only been checked against specified literature, available research records, and accessible older claims. Independent audit: not performed.
