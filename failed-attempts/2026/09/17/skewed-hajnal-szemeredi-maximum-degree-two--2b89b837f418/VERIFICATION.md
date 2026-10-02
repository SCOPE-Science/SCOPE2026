---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The flow proof for bipartite path/even-cycle components is correct: the only nontrivial cut is a single color because twice each component independence number covers its order, and the local path/cycle arrangement criterion realizes the component multiplicities. The odd-cycle-transversal lemma is also valid, and the one-large/two-large case split correctly proves the stated maximum-degree-two skewed-coloring theorem.

## originality

FAIL

A published Resultary record, 'Exact prescribed color-class sizes for graphs of maximum degree two' (2026/9/17/SCOPE-prescribed-colorings-max-degree-two--9aaf81e2ad5d), is strictly stronger and was inspected at its actual Git blob c2d4e4bd1b4f60d0b85b1dd19e890d324fde9c80. It characterizes all prescribed profiles for every maximum-degree-two graph by two inequalities. For bipartite graphs its second inequality is automatic, giving exactly the submitted Theorem 2, and its consequence section directly proves Birken's r=2 conjecture. Thus the final claim is covered, not merely similar.

## value

FAIL

The mathematics is clean, but after the stronger exact maximum-degree-two characterization is accounted for, the submitted final claim has no independent gap left to fill. It is a weaker covered special case/corollary, so it fails the requested value criterion as a new finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
