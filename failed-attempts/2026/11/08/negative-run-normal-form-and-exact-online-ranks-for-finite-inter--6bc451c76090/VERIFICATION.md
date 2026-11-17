---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Direct source RESULT.md establishes positive-history Cartesian threshold endpoint ranges of cardinalities L and R, hence additive rank floor(log2 L)+floor(log2 R). Negative-only histories are disjoint maximal unqueried runs; a site query gives independent positive endpoint counts i*(ell-i+1) and a split-run negative branch. The standard complete mistake-tree recursion yields exactly the stated integer-partition recurrence with empty-space sentinel -1. For n=2^(k+1)-1, centered intervals give two 2^k threshold factors and thus Ldim >=2k; the total n(n+1)/2<2^(2k+1) gives the matching upper bound. Three points cannot be shattered in the positive-negative-positive pattern, two can for n>=3. Independently recomputed full version-space ranks by bitmasks for n=1..8 yielding 0,1,2,3,3,4,4,4; source verifier separately read, not treated as universal proof.

## originality

FAIL

Decisive mathematical duplication: the earlier published Nov 2, 2026 Resultary interval theorem establishes exactly the same positive-history product rank and all-negative unqueried-run recurrence for ANY finite block multiset, not merely a table up to n=55. New source repeats that theorem with a different sentinel convention. Its infinite dyadic equality is a routine two-line consequence of threshold-product additivity and cardinality information bounds and does not constitute a substantively independent theorem.

## value

FAIL

The positive/negative conditional online-rank recurrence and all-instance computation have real learning-theory value, but were fully proved by the earlier Nov 2 theorem. The remaining dyadic equality is a standard threshold-product versus information-count calculation, and static VC=2 is textbook. Repackaging established results has no novel standalone scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
