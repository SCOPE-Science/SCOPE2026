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

Without the hub a set must hit every peripheral pair; then a pairmate can defend an unselected peripheral vertex, and the hub can be added by any legal exchange. With the hub, an untouched pair must use the hub as guard, so a second untouched pair makes the exchange fail. This proves the two secure-set criteria and excludes every secure singleton for m≥2. Quotient edges encode exactly the untouched pairs, counting loops and repetitions. For the upper bound choose distinct edges e,f missed by the hub class. A non-hub class outside their endpoint union cannot partner with the hub, and needs a common endpoint of both edges as a partner. In the disjoint case there is none. In the pairwise-intersecting case, a common endpoint C cannot partner with two outside classes: any edge not incident to C would have those two classes as endpoints and would contradict intersection with e in the hub-deleted quotient; having no such edge would make C secure. Hence there are at most |supp(e)∪supp(f)|+|supp(e)∩supp(f)|≤4 non-hub classes. The hub with m−2 whole pairs plus four singletons attains five, including m=2. The quotient conditions thus recognize all valid partitions. The independent guard-exchange check /workspace/checks/4.py confirmed the subset criterion through m=7 and the reported labelled-vertex optimal partition counts 1,81,1174,12290 through m=5; the unbounded result rests on the proof. In the prose, the edge test more conventionally is a vertex-cover test on quotient edges.

## originality

PASS

The inspected secure-coalition bounds do not give the general constant-five formula, and the published coalition graph for a partition encodes already determined partners rather than peripheral incidences. No distinct covering statement was identified in the checked sources for ordinary secure domination on friendship graphs.

## value

PASS

This computes a natural coalition invariant on an unbounded canonical family where the previously checked upper bound increases with order. The fixed maximum and incidence criterion give both a benchmark and a direct way to recognize all extremizers, including partitions with repeated or loop incidences, without enumerating exchanges.

The dated certificate retains the supplied scientific assessment, sources and limitations.
