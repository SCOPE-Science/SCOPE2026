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

Run `python3 verify.py` from the same directory. The verifier uses only the Python standard library, independently enumerates each periodic interval and tests its shortest period and extension maximality, sums rational exponents, and compares with the gap formula. It exhausts all \(\sum_{n=2}^{25}\binom n2=2600\) possible two-one words, all sharp-extremum and equality cases for lengths 8–25, and 873 random examples within length 75. It also evaluates the gap formula over all words at lengths 60, 120, 240, 480, and 960 to show the gradual approach to the continuum law. See `verification_output.txt` for recorded output.

The mathematical proof separately establishes every finite-length formula and the weak limit. Finite enumeration is not an infinite proof. The limiting distribution is checked symbolically by the simplex-area integration in `RESULT.md`, not certified by Monte Carlo. No external or independent scientific audit has been performed.
