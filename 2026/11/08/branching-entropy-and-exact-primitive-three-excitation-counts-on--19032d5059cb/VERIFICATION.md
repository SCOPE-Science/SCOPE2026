---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For a connected graph, a nonzero state fixed by the cube of synchronous three-state threshold-one Greenberg–Hastings must have every vertex advance at every step: permanently resting vertices cannot neighbor an advancing one. This is equivalent to each initial vertex having a successor-color neighbor. On the binary triangular cactus, classify each rooted subtree with fixed root phase as A (internally supported) or B (root unsupported and needing parent). For the single triangle (A0,B0)=(2,1), and an explicit nine ordered phase-pair enumeration yields A_next=5A²+6AB+2B² and B_next=4A²+4AB+B². The full root needs A and cyclic recoloring gives P_h=3A_h. The normalized logarithmic recursion gives a convergent entropy series, r_h=B_h/A_h remains in [1/2,3/4], with q(r0)=17/2 and q(rh)>10 thereafter. Hence c>(log340)/4>log(2+sqrt5), rigorously compared to the known triangular-chain transfer eigenvalue. Direct enumeration of 3^7 states at height1 and recurrence identities match. Finite-state tests do not replace the all-height polynomial recursion.

## originality

PASS

Prior Greenberg–Hastings works characterize eventual excitation, winding and synchronization on arbitrary finite graphs, not initial primitive three-period population on a complete binary triangular cactus. A same-date published triangular cactus chain theorem gives linear transfer matrix with growth 2+sqrt5, not the quadratic branching recurrence. The same-date singly resonant cactus product law explicitly excludes graphs with two or more 3-divisible cycles, while the present graph has 2^(h+1)-1 triangles, all resonant. Hence no searched stronger statement implies the binary-branch entropy comparison.

## value

PASS

The exact two-terminal nonlinear recursion for a natural family of line graphs identifies how combinatorial branching changes the exponential population of persistent excitation configurations, with a strict, proved entropy gain over a linear chain at equal vertex-per-block normalization. It is not an arbitrary finite census or merely generic periodicity existence; the infinite family and entropy inequality are structurally meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
