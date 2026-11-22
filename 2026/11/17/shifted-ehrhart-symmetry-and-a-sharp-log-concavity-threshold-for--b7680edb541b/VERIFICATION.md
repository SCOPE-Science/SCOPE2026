---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For n>=3 and positive integral w_i with det M=1−(−1)^n Π_i w_i nonzero, v_i=e_i+w_{i+1}e_{i+1} form an (n−1)-simplex in affine hyperplane. If a barycentric coefficient vanishes on a lattice boundary point, integer coordinates propagate a 0/1 choice around the cycle forcing a vertex. The same propagation for half-open parallelepiped generator coefficients in [0,1) forces any nonzero lattice point to have all coefficients strictly between zero and one; complementing gives height j↔n−j, h_n=0. For n=5, uniform w>=2, all interior positive integer compositions of total w+1 lie in simplex (for w>=4 prove via M^{-1} lower coordinate bound), hence L(1)=5+binom(w,4). Affine normalized volume (w5+1)/(w+1), h0=1 and shifted symmetry yield h1=h4=A and h2=h3=B=w(w−1)(11w²+5w+6)/24. B>A, so log-concavity reduces to A²>=B; ratio B/A decreasing for w>3 and exact w6 failure vs w7 success proves cutoff 7. Independent first-two-dilate counts w2..6 verify coefficients, not full general case. Degenerate even all-unit case correctly excluded.

## originality

PASS

The full claim is a nondegenerate positive exponent-vector directed-cycle simplex with shifted Ehrhart reciprocity for all positive integral weights and a complete five-cycle polynomial with exact w>=7 log-concavity cutoff. Known toric-ideal setup and the later weighted-oriented-edge-polytope paper supply object and unit-dilate/IDP facts; general reciprocity is classical and unclaimed as methodological novelty. Bounded searches did not locate this exact numerator/cutoff or a stronger statement forcing it. A plausible unavailable full text is retained as real priority risk, not automatic scientific failure.

## value

PASS

It identifies a natural weighted oriented-graph lattice-polytope family with unexpectedly shifted Ehrhart symmetry and provides an exact explicit log-concavity threshold inside a persistent non-IDP family. The exact five-cycle h* polynomial and w=7 boundary are nontrivial finite-dimensional but infinite-parameter facts, useful beyond a numerical instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
