---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The polygon has at most one side per prism face, hence at most n+2. Away from planes through a vertex, with q=|U_z| and t=hq/√(1−q²), the top and bottom each contribute two crossed edges if t is below the maximum absolute horizontal vertex projection, and none above it. The n vertical edges occur in opposite pairs, a pair crossing exactly if its projection modulus is below t. Thus the n+2 event is exactly that t lies between the two largest moduli. Folding the azimuth onto (0,π/n) gives those moduli as cos φ and cos(2π/n−φ); Haar q is independent uniform on (0,1). The CDF b/√(h²+b²) and elementary antiderivative give exactly the stated probability, also for n=4. The derivative in z=(1+h²)^−1/2 has sign 1−3 cos²(π/n) z² after comparison of positive radicals; the unique zero is interior even at n=4. Substitution, the cubic Taylor term 2(π/n)^3/(3√3) in the arcsine difference, and the exact square and hexagon evaluations agree with the finding. The supplied Monte Carlo/quadrature code was inspected, not rerun, and is not needed for the proof.

## originality

FAIL

Actual earlier Resultary text b6d28d7c72f4 states and proves the same optimal probability and exact optimizer for every even n≥6, with identical plane law, normalization and maximal-count event, including the exact regular hexagon result. The added n=4 is a known cube consistency check and direct extension of the identical angular calculation to the endpoint; the large-n expansion is a direct Taylor consequence of the earlier exact formula. No substantive uncovered remainder is established.

## value

FAIL

The full height-design law answers a natural geometric question, but that contribution is already available. For this frozen record the only additions identified are the known square/cube endpoint, its immediate inclusion in the same proof, and the leading coefficient mechanically extractable from the earlier law. They do not supply an independently useful unknown mathematical result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
