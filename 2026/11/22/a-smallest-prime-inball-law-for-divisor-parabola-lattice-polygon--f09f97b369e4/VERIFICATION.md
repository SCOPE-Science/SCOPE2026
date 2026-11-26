---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For h≥2 the predecessor d=h/p is at most h/2. The signed distances from (0,h²−r) to the top and both terminal chord lines equal r=h(h+d)/(1+√(1+(h+d)²)). For any other lower line with endpoint parameters (u,v), including (1,1) for the bottom lines, both parameters are at most d. The sign of the first partial derivative of R_h(u,v) is that of (v²−h²)(u+v)+v(1+√(1+(u+v)²)); since u+v≥2 and v≤h/2 this is bounded above strictly by (u+v)(v²+2v−h²)<0. By symmetry R_h(u,v)≥R_h(d,d)>R_h(d,h), which gives strict slack; it includes the case d=1. Any center (x,y) and feasible radius ρ obey ρ≤h²−y and ρ√(1+(h+d)²)+(h+d)|x|≤y+dh. Adding proves optimality, and equality forces the proposed center. All three contacts are in the relative interiors because all other lines are slack. Retaining 1,d,h after symmetric deletion preserves these constraints and keeps every new nonterminal chord below the same parameter bound. Strict convexity makes each retained parabola point extreme, so the deletion count is exact. Rationalization gives the positive error from p/(p+1) of less than 1/(2h); isolation of finite prime values and the sole accumulation point 1 give both sequence equivalences and the full spectrum, realized by prime powers and increasing primes. The frozen decimal checker was inspected, not run, and its finite scope is not needed for the proof.

## originality

PASS

The credited facet description and earlier arithmetic invariants of B_h are prior results. In the inspected sources the unique three-contact Euclidean inball, deletion invariance and prime-indexed metric defect are distinct, not established by the earlier lattice area computations or the general formulation of the center optimization problem. This is a bounded priority assessment.

## value

PASS

The polygon is an established arithmetic building block and the free Euclidean inball is a natural shape invariant. Identifying three universally active facets among 2τ(h)+1, and proving that the disk persists in every specified deletion, gives useful structural compression beyond a numerical center solver. The uniform defect estimate recovers a precise least-prime signal, with all accumulation values and their rigidity characterized. The value is planar and family-specific, not a claim about inballs of the higher-dimensional reflexive constructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
