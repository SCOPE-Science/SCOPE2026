---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Two white non-bridge vertices in the same clique cannot be separated by a first force on either. Under the resulting one-per-clique restriction, the only possible four-white configuration has both bridge endpoints white and no first force. With three whites, either the opposite clique forces its white bridge endpoint and then forces across the bridge, or a non-bridge blue helper clears the opposite clique's lone white non-bridge vertex before the bridge force. In each case the last internal white is forced within its clique. The other triple cases follow by exchanging the sides, and every allowed smaller white set is a subset of an allowed triple, so follows by blue-set monotonicity. Both cliques have the required helpers for p,q≥3. Counting triples gives (p−1)+(q−1)+2(p−1)(q−1); counting pairs excludes precisely internal same-side pairs. This gives every coefficient and the minimum size. An independently written closure check matched the criterion and counts on all 14,400 subsets in the 16 ordered pairs 3≤p,q≤6; replay: python /workspace/branches/d6109c61-1838-413a-b817-f87179e5cdb6/recheck_barbell.py. The uniform conclusion comes from the proof, not the census.

## originality

FAIL

A distinct published Resultary record gives the same all-set classification and exactly the same polynomial under the same rule and p,q≥3. The four displayed triple types merely unpack its criterion at the minimum size. This is demonstrated duplicate coverage, not a concern inferred from inaccessible literature.

## value

FAIL

An otherwise unrecorded full classification on this natural test family could be useful to distinguish extremal size from the actual choices at a bridge. Here the exact classification, all coefficients and minimum-set count are already available. The reformulation in white vertices exposes no new cases, quantitative gain, or independently useful mathematical consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
