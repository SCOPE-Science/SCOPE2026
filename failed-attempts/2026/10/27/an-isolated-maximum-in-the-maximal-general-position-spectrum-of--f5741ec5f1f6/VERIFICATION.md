---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For n>=4 all leaves form a general-position set and all proper leaf subsets extend to it. A set of size at least three cannot use both a core and its private leaf, since that core lies on every path from its leaf to a third selected vertex. After rotating a selected core to 0, index the other occupied fibers. A pair of those indices with a shortest cycle route through 0 is forbidden, since pendant endpoints add the same lengths to both cycle routes. Put m=floor(n/2). The m-1 distinct matched pairs (-s,m-s), 1<=s<=m-1, are forbidden pairs: the route through 0 has length m, including an equally short route when n is even. At most n-m other fibers may be occupied. Equality is realized by the leaves at 1,...,m and, for odd n only, at -m, together with core 0. Two positive indices have a strictly shorter route avoiding 0, while in the odd case a route through 0 from -m to any positive listed index has length >m. No selected leaf is interior to a geodesic. Any extension retains the selected core and would exceed the established cardinality bound. Since ceil(n/2)+1<n for n>=4, only all leaves achieve n. The missing-size count between the two largest maximal cardinalities is floor(n/2)-2 for n>=6, with n=4,5 having no gap. Replay: RESULT.md lines 19–45. The frozen enumeration and matching script and recorded outputs were inspected, not executed; the finite checks do not establish the all-n result or say every smaller cardinality occurs.

## originality

FAIL

Shown covered: the earlier Resultary classification eea66c0e3a48 explicitly gives the unique maximum and its root-eligibility rule directly implies the sharp next-largest maximal size and hence the gap. The matching is an alternate proof, not a distinct spectrum finding.

## value

FAIL

A large gap in a maximal spectrum of subcubic graphs is a mathematically natural phenomenon. Here, however, the exact endpoint is obtained mechanically from the older same-family classification by bounding the remaining positive gaps and choosing unit gaps. The matching offers a clean restatement but no demonstrated structural or classification gain beyond that known result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
