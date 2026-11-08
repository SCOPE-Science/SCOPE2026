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

# Verification record

The analytic proof is contained in `RESULT.md`. In particular, its nonstandard exact claim is the two-sided covering argument, which uses eventual strict Poisson-tail domination and a family of exponentially many separated subsums. The binomial-to-Poisson coupling gives a uniform total-variation estimate independent of the logical formula. The asymptotic is for fixed \(\lambda>0\).

Running `python checker.py` alongside the result produced `ALL_CHECKS_OK tested_conditions= 300`. Checks included exact weighted enumeration of all loopless directed graphs of sizes three and four at rational intensities one and two, all root-degree predicates on those graphs, numerical total-variation bounds for several sizes, and strict tail inequalities on a range of indices. Floating-point checks are illustrations only, not certificates of infinite claims.

No external or independent mathematical review has been performed. Historical uniqueness is not established solely by unsuccessful search.
