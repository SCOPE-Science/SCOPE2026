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

A cut pair identifies a state bijectively and all legal switches are single-cut steps. For n>2s, the strip s≤y−x≤n−s has positive width: if a needed monotone coordinate move exits, a move of the other coordinate toward the target must enter the strip, by feasibility of the endpoint lift. Conversely every path lifts, giving the minimum of the two cyclic-order lift families. For source gaps d and n−d, alternate cuts give complementary admissible path lengths summing to n; targets on one arc can be paired via its exterior gaps, giving at most d on the short arc and n−d−s on the long arc. The T1 witness has distance m=floor(n/2) by two lift pairings (m and n−m), and its two gaps are feasible even at n=2s+1. For T2 write L=n−s−d and α=floor(L/2); the other candidate lengths d+s+2α and 2n−d−s−2α are both at least L. Radius occurs at d=m and diameter at d=s. Each of the n boundary states for n>2s has two moves, all others have four; n=2s gives n/2 isolates and no connected-case metric is claimed. Independently generated partitions as vertex bitmasks modulo complement and toggled a vertex directly; BFS verified counts, connectivity and all eccentricities for n=3 through 13.

## originality

PASS

The actual claimed contribution is the extremal evaluation in the size-constrained cycle, not cut-pair encoding, transport-optimality, the all-pairs distance formula, or connectivity. Two general token results already cover the latter exactly, and a prior eccentricity theorem is an actual subfamily overlap. The inspected sources do not evaluate the maximum for every d,n,s or give a stronger extremal theorem implying it.

## value

PASS

The exact eccentricity describes worst-case reconfiguration effort state by state in a natural constrained districting problem, showing the change between the floor(n/2) regime and a linear long-arc regime. It diagnoses how a minimum-size rule changes global geometry despite leaving transport distances intact for surviving states. Exact radius and diameter are useful consequences; the elementary counts alone would not justify value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
