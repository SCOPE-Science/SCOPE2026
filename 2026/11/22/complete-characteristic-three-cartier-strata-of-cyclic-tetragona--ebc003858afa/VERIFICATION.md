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

# Reproducibility and independent-review status

Run `python3 verify_cartier.py` in a directory containing the extracted script. It needs only the Python standard library. The program recomputes the Cartier matrix by the coefficient formula rather than importing a serialized expected matrix; checks its entries, ranks of the first eight powers, and polynomial squarefreeness over the prime field; and checks the six explicit squarefree witnesses.

The symbolic proof in RESULT.md, not exhaustive enumeration over a finite field, establishes the assertion for *all* algebraically closed characteristic-three coefficient values. The code is a useful regression check of the nonstandard matrix calculation and example smoothness.

The result has passed self-review only. No independent audit has been performed, and historical priority remains provisional.
