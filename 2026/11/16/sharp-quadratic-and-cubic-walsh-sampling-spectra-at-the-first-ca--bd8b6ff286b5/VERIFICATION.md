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

Run `python3 verify_direct.py` and `python3 verify_distance.py`; both require only Python 3 and SymPy. The first generates all balanced length-eight words, filters prefix ballot paths, evaluates every degree-two and degree-three Walsh character, computes symbolic Gram determinants and the kernel witness. The second independently generates Dyck paths by recursion, uses the binomial Krawtchouk identity to construct Gram entries and exactly factors both determinants. Both compare symbolic expressions with the explicitly reported polynomials and check ranks; the distance checker certifies all algebraic-root intervals by rational sign changes. Both scripts completed successfully on the supplied code.

**Limits:** The verification is finite and exhaustive for fourteen paths only; it does not imply any statement for longer words. Sharp constants concern Euclidean singular values of the particular unnormalized Walsh sampling matrices. Graded-rank comparisons do not establish priority of the spectral polynomials, and no independent external audit was carried out.
