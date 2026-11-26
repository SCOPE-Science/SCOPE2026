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

The strictly positive trace Hessian (positive divided differences of f' for f(s)=exp(-ts)) and injectivity of individual rates into the simple graph Laplacian give strict convexity even at disconnected supports. Compactness and scaling give a unique budget-saturating optimizer, hence invariance on the two edge orbits. The biadjacency has eigenvalues d and p-q on the constants and zero-sum vectors; taking symmetric and antisymmetric layers gives the four blocks including all zero modes. Differentiating after budget elimination gives (7). The normalized upper endpoint derivative r-(2-r)exp(-2Bt/(mr)) crosses once only for r<1; the lower endpoint is strictly negative for those prices. The lower endpoint sign for r>1 is the sign of F_m, strictly decreasing from 2m(r-1) to -A_m; at and above the ceiling it stays positive. Strict convexity handles exact equality at either activation time, and full edge transitivity settles r=1. For 1<r<2, fixed positive bracketing points yield the limiting scalar root; r=2 reduces to m exp(-2x)+exp(-mx)=1, giving x=(log m)/2+o(1); near the ceiling at fixed m, the second exponential divided by the first decays like exp(-(m-2)x). These apply with the stated fixed parameters. Independently assembled the 6-by-6 incidence-outer-product Laplacian and evaluated -tr(exp(-tL)(L_match-r L_off/(m-1))) at B=1, m=3. For r=1/2 at the matching-only boundary, t=.80,.85 gave signs -,+; for r=3/2 at the nonmatching-only boundary, t=2.19,2.20 gave +,-; r=4,t=10 gives + at the lower boundary. Scalar replay: solve 4.5 y^2+y^3=2.5 for y in (0,1), then T_b=-6 log y=2.19351865374148. These are bounded checks; the proof, not floating point, resolves every threshold. Inspected the frozen checker without running it.

## originality

PASS

Best of checked evidence: the priced-biclique gap ceiling overlaps exactly and must remain attributed. The supported new claim is the finite heat-trace support diagram and the activation-delay laws, not the ceiling as a spectral-gap result or the use of orbit averaging.

## value

PASS

This resolves all support changes for an unrestricted and natural finite-time diffusion loss. It distinguishes deliberate transient disconnection, delayed matching activation on already connected supports, and genuine permanent deletion, with different m, m^2 and m^2 log m laws at fixed budget. Those distinctions cannot be inferred from the known steady gap frontier.

The dated certificate retains the supplied scientific assessment, sources and limitations.
