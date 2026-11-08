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

# Reproduction and limits
The included `verify.py` is a standalone Python 3 program. Run `python3 verify.py` in a directory containing this file. It enumerates each automorphism by the coefficient tuple in nine small prime-field cases, constructs its substitution matrix without conjugacy or normal-form reduction, computes its fixed-space dimension by modular Gaussian elimination, and compares the complete histogram with the closed formula. All nine cases passed; the script terminates with `VERIFY_OK`.

The tested pairs are \((5,2),(5,3),(5,4),(7,3),(7,4),(7,5),(7,6),(11,3),(11,4)\), with the first entry the prime field order. The most demanding case checks every one of the \(6\cdot7^4=14406\) actual automorphisms at \((q,n)=(7,6)\). The mathematical argument, not these finite checks, is the basis for the theorem for all finite extensions in characteristic greater than the truncation length. No independent audit has been performed.
