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

# Reproducible checks and limits

Run `python verify_distinguishing_spectrum.py` with a standard Python 3 interpreter. The program independently tests literal scattered-subsequence membership and the theorem's combinatorial expression, with no third-party dependencies. It passed 488 parameter cases and 127,920 literal first-layer candidate words; it separately passed 5,912 permutation-pair configurations checking inversion-graph reconstruction, endpoint bounds, and equality rigidity.

The submitted verifier makes finite checks only; the universal claims are derived in `RESULT.md` from greedy embeddings, multiset support, and binomial identities. The experiment does not certify all finite or infinite instances, bibliographic priority, independent audit, or anything about unequal repetition exponents and longer distinguishing words.
