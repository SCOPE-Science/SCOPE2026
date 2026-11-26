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

Pavlík's interval description gives one vertex per cube face and one edge per cover; the cube realization supplies the required existence. A nonempty face is a ternary word, so without the empty-face pole the graph is a product of three-vertex paths with distance 2a+b. The pole is adjacent precisely to the zero-free words, at distance f(u)+1 from u. Any geodesic either avoids it or uses it once, giving the minimum of the two stated costs. Equivalently the nonempty-pair metric is n+1−e−|a−c−1|, so equality with n+1 requires e=0 and a=c+1. Every nonpole with a fixed coordinate has a partner made by reversing one sign, freeing every other fixed coordinate, and fixing all free coordinates; the two poles partner each other. This proves all eccentricities, including n=1. The four ordered coordinate multiplicities are 2,4,1,2; deleting the 3^n diagonal pairs, halving the ordered count and adding the empty-face shells gives the enumerator, and degree-one coefficients agree with the edge count. The mean correction is 2E[(C−A+1)_+]. Only A−C≤0 contributes, and the single-coordinate exponential moment at (log 2)/2 is (6+2√2)/9, establishing the stated bound for sampling with replacement. An independently written vertex-set-inclusion graph and exhaustive BFS reproduced the metrics and all six listed diametral counts in dimensions 1–6 (/workspace/branches/independent_replay.py, cube()). The packaged checker was read but not run. The finite reproduction is not the all-n proof.

## originality

PASS

The underlying cover graph and realization, the induced path product, and the regular-grid distance before adding the pole are antecedent or elementary. The distinct finding is the analysis of distances in the augmented graph, including all diametral pairs, full enumerator, and exponential accuracy of the pole-route mean. No separate matching statement was found in the bounded comparison.

## value

PASS

A single additional face vertex changes typical distances by a term linear in dimension relative to the coordinatewise product, yet every vertex has the same maximal eccentricity. Exact all-distance and diametral-pair data for this natural combinatorial polytope family, together with a quantitative mean estimate, make the metric useful beyond face counting or a small-dimensional observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
