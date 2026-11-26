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

The full diameter forces any resolver of an antipodal pair to be one of the endpoints. Conversely every vertex belongs to the interval between a vertex and its antipode, so any antipodal transversal strongly resolves, and choosing a coordinate half-cube adds exact-distance-two domination. A minimum transversal fails the latter condition exactly if its omitted set contains D_2(v). The d=2 antipode is itself a hop witness; in d=3 each parity class is a distance-two clique, giving two bad transversals; in d=4 each parity contains only four omitted vertices, fewer than the size-seven obstruction. For d=5, write U for the omitted even words. Failure is equivalent to U or its relative complement lying in an open distance-four neighborhood on even words. Two such neighborhoods intersect in two vertices at center distance two and zero at center distance four: a weight-four support must meet a size-two center difference in one coordinate, or a size-four difference in two (the latter is impossible). This gives 353 faces including the empty face, and the two excluded types are disjoint. In d=6, distances in each same-parity antipodal pair sum to six; exactly one is 0 or 2, so each obstruction is a whole parity-side transversal, and the 32 choices are distinct. Bounded fresh exact enumeration corroborated d=5 and both d=6 parity-side counts; replay /workspace/branches/76e234e5-929b-405c-ada6-840c0c61a3c7/reproduce_counts.py, with reproduction_output.txt in that directory. Supplied scripts and recorded outputs were inspected rather than run. For the infinite result, D_2(v) fixes L=1+binom(d,2) distinct antipodal choices. At center distance two there are the two centers plus 2(d-2) common words; at distance four there are binom(4,2) common words; otherwise there are none. A distance-two pair has no antipodal conflict for odd d (same parity), or for even d>=8 (cross-neighborhood distances are at most six). Its contribution from 2^(d-1)binom(d,2) pairs is exactly the claimed positive correction to the no-obstruction probability. Other pair contributions are bounded by 2^(2d-1) times 2^(-2L+6). Triple unions fix at least 3L-3(2d-2) choices if consistent and are impossible otherwise; fewer than 2^(3d) triples give the stated second error bound. Bonferroni places the error between the remaining pair sum and that sum minus the triple sum. Both displayed errors divided by the positive correction vanish. This establishes the coefficient and the explicit bound for all d>=8 independently of enumeration.

## originality

PASS

Pass for the combined exact-distance-two obstruction count and especially the sharp second-order labeled cube asymptotic. The antipodal strong resolving basis reduction alone is not claimed original, and the dimension-five incidence census is covered by earlier Clebsch face data together with the elementary parity translation, as the finding expressly credits.

## value

PASS

The labeled cube is a natural product test case linking two graph constraints. The result detects exactly which local obstructions spoil a minimum strong resolving basis and identifies the dominant dependent pairs, with a proved smaller remainder. The finite exceptions put the asymptotic in context; the already-known Clebsch data are not the basis for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
