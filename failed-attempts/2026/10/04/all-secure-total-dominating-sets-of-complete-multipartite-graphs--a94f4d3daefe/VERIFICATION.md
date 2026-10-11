---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

A subset of a complete multipartite graph is total dominating exactly when it meets at least two parts. With at least three represented parts, replacing a defender can remove at most one represented part, so security is automatic. With exactly two parts \(X_i,X_j\), an omitted vertex of \(X_i\) is defensible exactly when \(X_i\) is already full or at least two selected vertices remain in \(X_j\), and symmetrically. This proves the support criterion, from which the enumerator and minimum cases follow by direct counting. An independent definition-level brute-force recheck matched the criterion on representative multipartite profiles.

## originality

FAIL

A previously published SCOPE record, SCOPE-20261004-03760d8f9284, states exactly the same all-set support criterion for secure total domination on complete multipartite graphs and derives an algebraically equivalent cardinality polynomial and the same minimum-size cases. Because that prior classification determines every cardinality coefficient, the current record's extra explicit minimum-set counts are mechanical corollaries and do not survive implication-level originality.

## value

FAIL

The classification and enumerator are mathematically natural, but this record does not fill an unknown gap because an already published record supplies the same feasible-set theorem and polynomial. Under the shared value standard, recomputing a known exact classification is not a new worthwhile finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
