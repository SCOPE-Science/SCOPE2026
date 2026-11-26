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

At unit rolling radius, z=e^{it}(n+1-e^{int}) is nonzero and winds once; the polar argument has nonnegative derivative, positive except at finitely many cusps, from the stated radial sweep. This gives a simple loop. The extrema of the cusp-direction projection occur at cusps or at odd multiples of pi/(n+2); their values are n cos t or (n+2)cos t, respectively. The global maximum is attained only at ±alpha, since (n+2)cos alpha>n for n>=1. Rotate to get the n chords. Other retained arcs and chord endpoints lie strictly inward of each corresponding support line except at its two own contacts, so replacing the disjoint cusp arcs makes a simple closed path without new crossings. The tangent matches at the endpoints, turns through 2pi/n along each retained arc and is constant on the chord. This is the convex boundary, whose arcs and chords all belong to the convex hull of the old curve. Direct speed integration retains 8(n+1)sin alpha of curved length; all chords add 2n² sin alpha. For a separate area computation, the signed area added at each cusp is half the cross product of the two endpoints minus half the integrated radial sweep on [-alpha,alpha]. This is n(n+2)sin alpha cos alpha -(n+1)(n+2)(alpha-sin(n alpha)/n). Use sin(n alpha)=sin(2 alpha) and n alpha+2 alpha=pi to recover the recorded total. Restoring r by homogeneity, the original integrals are 8(n+1)r and pi(n+1)(n+2)r², and the sine asymptotics give both ratios. Read the polygon-sampling script and recorded notes as finite corroboration, not as proof of the support set or continuum formulas.

## originality

PASS

Best-of-knowledge pass on the complete all-integer hull decomposition and its exact perimeter and area, not on classical epicycloid integrals, individual known bitangents or isolated hull-area computations. A material special-case calculation is apparent in Balmoral Software's indexed page, and a potentially relevant full-text cycloidal cap paper is unresolved; neither available statement establishes the whole integer family.

## value

PASS

The exact supporting contacts, retained arcs and intrinsic volumes are useful for convexification of a natural classical family. The formulas separate what is kept from what is flattened at every finite cusp count and quantify both geometric costs. The asymptotic contrast is useful interpretation but is not the intrinsic novelty or the sole justification for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
