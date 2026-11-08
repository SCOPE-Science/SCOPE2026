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

# Verification summary

Run `python3 verify.py` in the same directory. It uses only the Python standard library. Its first check enumerates all pairs of distinct round-two vectors, represented by four orbit types, on eight coefficient coordinates. This covers all overlap patterns of supports of size at most four and verifies the complete ten-row transition table. Its second check compares multinomial orbit counts with the asserted closed-form binomial polynomials for every \(2\le n\le24\). Its third check directly constructs the full ternary affine Steiner system on \(3^d\) points and simulates parallel propagation for every \(1\le d\le9\), checking all four stated cumulative counts and the three-round completion threshold.

Expected successful final line: `VERIFY_OK`. These are finite computational checks and a finite table certificate; the extension to all dimensions uses the support-at-most-eight reduction proved in `RESULT.md`. The auxiliary verifier does not provide independent certification.
