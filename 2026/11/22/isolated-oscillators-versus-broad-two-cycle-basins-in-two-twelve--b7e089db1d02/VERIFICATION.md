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

Independently built the two graphs and indexed all 4096 states of each by bit masks. The update threshold on neighbor ones is floor(d/2)+1 at an incumbent zero and ceil(d/2) at an incumbent one, including degree-four ties. Computing every successor and flagging F²(s)=s identifies exactly the states with period dividing two, and following every initial state to its first flagged state proves the claimed cutoff and absence of other periods. On T, the fixed destination row is (16,238,468,720,216,72), the two-cycle destination row is (478,1264,528,96,0,0). Thus 239 primitive orbits attract 2366 states (1888 transient), sharp time three within that basin and five globally. The unanimous basins each contain 680 states. On benchmark C the rows are (146,1606,1200,1008,96,0) and (40,0,0,0,0,0); the unanimous basins each have 1032 states, and no oscillator has a transient predecessor. Witnesses 310 on T and 348 on C attain the global times. Independent adjacency-preserving bijection backtracking found groups of orders 24 and 48 and applying them gave respectively (5,26) and (14,3) fixed/two-cycle spatial counts. The structural symmetry arguments in the corrected result agree. Global sharpness of the iterate identity follows because F^(r+2)(x)=F^r(x) exactly when F^r(x) is already of period dividing two. All figures and claims in the corrected files were checked against this exhaustive replay or against the explicitly credited benchmark statement.

## originality

PASS

For the repaired claim only: the established cuboctahedron census is a reference point, including the no-transient-predecessor result itself. The distinct contribution is the exact truncated-tetrahedral binary-majority attraction and entry census, not eventual period-two theory, a recomputation of the cuboctahedron, or a general isolation claim. No inspected statement gives or implies the new truncated-tetrahedral census.

## value

PASS

The repaired contribution determines the exact distribution of recurrent destinations and times for a canonical twelve-vertex Archimedean majority network, motivated by comparison with the already established cuboctahedral isolation standard. The substantive contrast is that a uniformly random start usually oscillates on T, with 1888 nonperiodic starts converging to two-cycles, not simply that the graphs have different recurrent-state totals. The independent sharp times for reaching any attractor and for reaching an oscillator, plus symmetry-resolved counts, make the model a precise finite benchmark. This is not presented as the first existence of transients entering oscillations in general.

The dated certificate retains the supplied scientific assessment, sources and limitations.
