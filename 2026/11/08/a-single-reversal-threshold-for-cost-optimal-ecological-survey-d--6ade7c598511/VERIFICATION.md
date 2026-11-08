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

# Reproducible verification

Run `python3 verify.py` from the directory containing `verify.py`.

The delivered program uses only Python's standard library. Its actual execution returned `PASS 1274 arithmetic/finite-grid diagnostic checks` and the documented crossover and cap examples. Exact-rational identities check rate and second-derivative normalization at integer shapes; floating-point tests diagnose derivative signs and both sides of the crossover for real shapes and occupancies. A finite sweep cannot establish universal uniqueness: that is supplied by the analytical \(F'''(x)>0\) proof in RESULT.md.

The source's 2009 first-public date is supported by its 11 May 2009 electronic-publication record. No external review or independent scientific validation is claimed.
