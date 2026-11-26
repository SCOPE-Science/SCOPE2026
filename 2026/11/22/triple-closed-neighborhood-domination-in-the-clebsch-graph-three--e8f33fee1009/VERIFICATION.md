---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Independently enumerated all 65,536 labelled masks against the 16 closed neighborhoods, giving counts 312,1872,1580,560,120,16,1 at sizes 10–16 and none smaller. The even-word model is equivalent because its four chosen weight-four generators are a basis and their sum is the fifth; distance four is exactly one of these five XOR differences. A separate loop in that model tested all 8,008 six-hole sets, including every subset having a claimed degree sequence, confirming the if-and-only-if type classification with counts 40,192,80; triangle-freeness converts those sequences to 3K2, C5 plus an isolate, and C6. The action by translations and permutations gives three respective orbits of those exact sizes. Indexing pairs of distinct optimum hole sets by overlap at least 6−t gives zero edges at t=1 and, at t=2, 5,220 edges, degrees 39 on 120 and 30 on 192 vertices, one component and eccentricity 3 at every vertex. There is also an independent short check of the lower bound: two distinct closed neighborhoods intersect in two vertices. For a feasible seven-hole set, the first two incidence moments of its intersection sizes with closed neighborhoods are ∑i=42 and ∑binom(i,2)=42. As i≤3, equality forces 14 neighborhoods meeting in three holes and two meeting in none. The union of the latter two contains ten vertices, leaving only six possible holes, a contradiction. Larger feasible holes would contain feasible seven-hole sets. The frozen scripts and outputs were inspected but not executed; the separate reproduction also verifies the converse shape test not expressly asserted by the submitted scripts.

## originality

PASS

The object and the selection constraint are standard, but no compared source establishes the joint classification of minimum closed triple covers, their counts and reconfiguration graph. A narrower exact claim about ordinary covering-code minima, if found, would not by itself give this incidence and exchange structure. This is a bounded statement-level decision and does not rely on the zero-result literature query.

## value

PASS

The five-regular Clebsch graph is a standard highly symmetric test object for neighborhood covering. The exact type/orbit structure and sharp jump from a wholly isolated optimum space to a connected space at radius and diameter three are the main value, beyond just computing a minimum on 16 vertices. They give a precise benchmark for minimum closed-neighborhood cover enumeration and for how simultaneous replacements change reachability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
