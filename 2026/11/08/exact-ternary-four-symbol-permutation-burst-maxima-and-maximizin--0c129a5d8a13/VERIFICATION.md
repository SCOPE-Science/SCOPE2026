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

Reproduce the standalone mathematical checks with `python3 verify.py` in a directory containing the supplied file.

The program computes the exact endpoint-changing multiset counts, independently checks every such count by enumerating distinct permutations, checks the complete five-class transition table, symbolically certifies all three phases of the infinite induction over quadratic count polynomials with exact rational coefficients, and verifies the proposed closed suffix-maximization recurrences and tie-count formulas to length \(300\). It separately enumerates all channel outputs for every ternary source word at lengths \(4\)–\(10\), \(88{,}533\) source words in total. Successful execution prints `VERIFY_OK`. These finite tests check implementation and boundary cases. The all-length assertion rests on the proof by induction using the explicit finite transition table, not on extrapolation from enumerated lengths. No independent audit has been performed.
