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

For each received triple reverse the channel by inserting each symbol in each position and retaining a set of parents. This gives the distinct-source incidence, not a count of positions. My exact check covers all 81 inputs and 27 outputs and confirms the ten symmetry orbits: in units of one eighth, the left sides of (1) are 8 on 51 inputs, 9 on 12, and 10 on 18. The total output and input weights are 75/8 and 21/8. Summing (1) over any valid code counts nonnegative output weights at most twice and nonnegative input corrections at most once, giving size at most floor(171/8)=21. The displayed 21 distinct parents hit each received word exactly twice. Pairwise intersections for the triangle on 0120, 0121, 0210 are {012}, {010,020}, and {021} in pair order (first/second, first/third, second/third). No output hits all three, and the resulting odd cycle cannot lie in a union of two independent sets in the conflict graph. Zero deletions give a unique parent and do not change the maximum.

## originality

PASS

In the sources checked, the directly applicable run-counting converse gives only 30, and related exact records have different list bounds or block lengths. No examined exact optimization or stronger applicable theorem settles the stated capacity. The supported distinct result is the sharp list-two optimum for q=3,n=4 with an exactly two-fold and non-bipartite witness, not the general deletion-hypergraph method.

## value

PASS

A standard fixed-list channel has a meaningful exact finite benchmark here. A checkable rational converse closes the one-codeword gap below twice the unique-list optimum. The attaining code saturates all received words yet cannot be partitioned into two uniquely decodable codes, separating these two ways to use the list allowance at optimum size. The result is not merely a numerical feasible example or an asymptotic-rate claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
