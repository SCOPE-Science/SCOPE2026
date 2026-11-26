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

In the finite classical S5 scope, reflexivity makes E^r test containment of the entire radius-r graph ball. The least r for all events is the maximum component diameter: deleting the far endpoint of a diametral pair supplies a counterexample at one step less, and zero diameter is already depth zero. An n−1 geodesic uses every vertex and an extra edge would shorten it. On that path, each agent's nonsingleton classes are a matching (a class of size ≥3 creates a triangle). Assigning every edge its nonempty set of agents with disjoint adjacent sets is therefore a bijection. Fixing one orientation per undirected labelled path counts the words without identifying distinct agent assignments; orientation reversal is already accounted for in n!/2. Grouping the next subset by size gives the stated recurrence, including the two-world value 2^k−1 and the separate one-world case. Independently iterated E on all events of all ordered frames for n=2..4, k=2,3 and reproduced the quoted counts through inclusion–exclusion over missing edge positions (python /workspace/branches/independent_math_checks.py, section 2). Separate direct enumeration of 239,549 small frames matched the path/subset count (python /workspace/branches/c8a972c1-f76e-41b1-9e78-60b522639569/independent_check.py). These are bounded reproductions, not a substitute for the general argument; the uploaded checker was inspected, not run.

## originality

FAIL

An earlier Resultary finding, 2026/10/18/SCOPE-extremal-common-knowledge-depth-path-coloured-s5-frames-and-thei--c1daefff85ba, covers the whole claim: the diameter identity, sharp spanning-path equality class, edge/agent subset bijection and ordered labelled all-k census. Its transfer matrix is the frozen recurrence in matrix form, with the same n=1 and n=2 limits; it additionally gives fixed-k asymptotics. This is verified prior coverage, not a failure to establish priority because of inaccessible literature.

## value

FAIL

Uniform finite unfolding depth and its extremal prevalence are natural invariants, but the frozen record contributes no new exact fact beyond the earlier all-k classification and count. Rewriting the transfer matrix as a scalar recurrence is immediate, and the special cases are already given. No distinct valuable remainder is established in the frozen result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
