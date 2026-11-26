---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

A fixed geometric point has an invariant nonempty support simplex, and conversely its barycenter is fixed. For prime p a nonidentity rotation generates the whole cyclic group and every complete orbit of an edge is a spanning cycle; containing it guarantees connectivity even after any one vertex is removed. For composite n a proper divisor d≥2 gives a nonempty rotation-invariant union of d disconnected step-d components (single edges when n/d=2). Babson et al., Theorem 3.1, gives a wedge of (n−2)! spheres of dimension 2n−5 for exactly this spanning non-2-connected graph complex. For p≥5 it is simply connected; freeness makes the quotient a regular covering with deck group C_p. Writing m=2p−5, the fibration over BC_p has no positive fibre (co)homology below m; differentials with the first possibly nonzero fibre row cannot affect the base row in degrees ≤m−1. The cyclic two-periodic resolution yields the odd integral homology Z/p and vanishing positive even homology there, and the integral polynomial generator of degree two with relation pu=0. Natural pullback yields the claimed products through degree 2p−6 and the unnormalized category bound p−2. No claim is made for p=3 about that range or the universal cover. Independent finite replay `python3 /workspace/review_calculations/small_cases.py graphs` obtains face counts 6,53,785,21399 and Euler characteristics 0,−1,−5,−23, with no fixed nonempty faces at 3,5 and fixed faces at 4,6. It checks boundary cases, not the integral cup products.

## originality

FAIL

Distinct Resultary record a63dad38c812 explicitly covers the whole frozen finding, at k=2 for the same spanning graph complex and regular cyclic relabeling. Its normalized category bound p−3 is the same as unnormalized p−2. This is demonstrable statement coverage, not an inference about authorship or provenance from dates.

## value

FAIL

There is real mathematical interest in the natural cyclic graph quotient and unbounded integral cup-length, but the frozen record adds no quotient invariant or free-action case beyond the stronger checked result. Changing category conventions and checking the small carrier-face counts do not constitute a standalone additional contribution. No valuable surviving claim to repair was identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
