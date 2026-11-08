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

# Verification of the mathematical finding

The package contains a self-contained `CHECK.py` requiring only the Python standard library. Running `python CHECK.py` reconstructs allocations from two independent, exact rational algorithms: an event-based unfilled-quota algorithm and a direct lower-contour-polytope breakpoint algorithm. They agree on all \(864\) enumerated three-agent preference/quota cases. The analytical single-quota formula is checked for \(6{,}480\) four-agent profiles. For \(216\) three-agent profiles at quotas \((1,1,0)\), all \(3\cdot5\) nontrivial unilateral reports are checked by the strictly positive top-prefix probability test; the script verifies \(30\) vulnerable profiles, \(36\) improving reports, the \(186/24/6\) distribution of improvement counts, and a \(5/12\) rational expected-utility gain in the explicit example.

The infinite-market strategyproofness and dimensional minimality claims are proved in RESULT.md, not established by the finite program. The script's exact rational operations avoid floating-point tolerance choices, but no formal proof assistant or independent human audit is claimed. Reproducing the checker does not establish originality.
