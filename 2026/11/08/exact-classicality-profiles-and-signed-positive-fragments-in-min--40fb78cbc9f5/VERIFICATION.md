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

# Reproducibility and limits

Execute `python3 checker.py` with Python 3 and no external dependencies. It enumerates every signed depth-\(k\) profile for \(k=1,\ldots,7\), confirming counts \(4,12,36,108,324,972,2916\), and confirms all unsigned flags occur. It computes exact signed-positive lattice antichain counts by a finite-poset branching recursion at depths \(1,2,3\), giving \(5,83,70806\) upsets of the punctured signed profile poset. The depth-one empty upset is not representable by positive terms, hence four rather than five logical classes. A different check enumerates all monotone four-argument truth tables and obtains 83 distinct restrictions at depth two. It also checks the usual Dedekind counts through five generators. Successful terminal marker: `LETF_LADDER_FINITE_CHECKS_OK`.

Proof of global bivaluation extendibility and the universal classification for all depths is in `RESULT.md`; finite computations are corroboration only. The present review is not independent verification. Originality remains subject to specialist inspection of unsearched/abstract-only literature, and no claim is made about propagation logic or arbitrary formulas.
