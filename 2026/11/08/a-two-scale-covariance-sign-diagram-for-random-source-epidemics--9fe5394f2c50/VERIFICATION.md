---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Conditioning on source at hub, designated leaves, or other leaves yields exact marginal P(H)=(1+kp)/(k+1), P(L)=(1+p+(k-1)p²)/(k+1) and pair probabilities (2p+(k-1)p²)/(k+1) and (3p²+(k-2)p³)/(k+1). Subtract products and factor the two stated polynomials. A_k increases from -1 to positive for k>=2; B_k for k>=3 is strictly convex on p>=0, initially decreases, and crosses exactly once before 1. Exact identity B_k-(k-1)pA_k/k=2p²-(2+1/k)p-1<0 on [0,1] orders roots. k=2 factor (p-1)(p²+4p+1), k=1 simple two-point result. p=c k^{-2/3} gives B_k=c³-1+O(k^{-1/3}); r_k formula yields (sqrt5-1)/(2k). Independently checked polynomial identity symbolically and exact seed/edge enumeration k=2..6 at p=1/4,1/2,3/4.

## originality

PASS

The inspected Kenah–Robins full SIR-percolation article and Sharkey–Kiss–Wilkinson–Simon full tree-moment-equations paper analyze more general dynamical settings, but do not state or directly imply the two exact random-single-source final-infection pair covariance sign thresholds and distinct degree exponents. Relevant fixed-time SIS/SIR correlation work is a different observable. This is a defensible best-of-knowledge new exact benchmark; comprehensive historical uniqueness not proved.

## value

PASS

Uniformly random index location induces negative dependence at low transmissibility despite independently successful contacts, then two distinct pair types reverse at parametrically different scales. This is a natural finite-network dependence classification and provides exact test cases for epidemic correlation conjectures, not merely a minor numerical coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
