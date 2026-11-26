---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

There are at most two forbidden common neighbors for a same-side pair, so it has distance two; for an omitted cross edge, first choose another right vertex adjacent to its left endpoint, then another left vertex adjacent to both right vertices, giving distance three. Nonempty sets distinguish opposite parts by parity. For two unselected vertices on the same side, the only landmark that can distinguish them is a selected deleted partner of either; thus the undistinguished class consists of the k empty-pair ends plus the unselected unmatched vertices on that side. This proves both inequalities and they exclude the empty set under a,b>=3. Split the generating function at k=0 and k=1. In the latter case all unmatched vertices and all nonempty pair singletons are essential, while any doubleton is reducible; in the former case omit exactly one unmatched vertex on each nonempty unmatched side, which makes every pair singleton essential except when both unmatched sides are empty. This gives the three minimal polynomials, the exact gap condition, and includes t=0. For a crown the empty-pair count is Binomial(n,(1-s)^2), so the asserted limit is its mass at zero and one in the Poisson limit. Independently used Floyd–Warshall and full subset comparison for seven examples covering zero, partial, saturated unequal, and crown deletions; e.g. (4,4,2) has 87 resolving sets with 16 minimal of size 4 and 4 of size 5. Replay: python3 /workspace/review-evidence/replay.py 3. The recorded BFS run is separate. The supplied script uses int.bit_count(), so it requires Python 3.10+ rather than the advertised 3.9+; this does not affect the mathematical conclusion or current replay.

## originality

PASS

The ordinary crown dimension and its complete minimum-basis count are covered, as is resolution on the chain-graph boundary t=0,1. The substantial distinct result is the all-set and inclusion-minimal census on the whole matching-deleted family, especially the interior 2<=t<min(a,b) and saturated unequal bicliques, with an exact upper-dimension transition. The consulted crown and chain statements do not imply that extension. The crown reliability limit is a consequence, not the independent reason for this judgment.

## value

PASS

The minimum dimension conceals larger inclusion-minimal sets. Exact polynomials both quantify and structurally explain that discrepancy, and the transition at matching saturation is not visible from crown dimensions or decision complexity. The full resolving polynomial can also be used for random landmark reliability, as illustrated at the crown endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
