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

# Reproduction and verification

The accompanying `verify.py` uses Python's standard library only. Execute `python verify.py` to enumerate all permutations for \(1\le n\le8\), compare their two generator products directly, reconstruct the proposed center, and check its entire product table using a separately generated reduced word. The test's observed center counts are \(1,2,2,3,3,4,4,5\), and successful execution prints `TYPE_A_HECKE_CENTER_VERIFIED`.

The proof for all \(n\) is independent of the finite enumeration: it derives the exact two-sided simple-generator test, uses an outer-pair induction to classify every central permutation, and proves the power law by an explicit Demazure reduced word. The checker validates implementations in small degrees but does not constitute an infinite certificate or an independent mathematical audit.
