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

Summing updates gives a Laplacian kernel vector, so connectedness forces one common number of firings per vertex in three steps. Zero and three firings yield fixed states; one and two are interchanged by x↦5−x. This complement is valid throughout each orbit: each vertex has a waiting time with at most two chips, the next value is at most five, and any firing step cannot increase its own value. For frequency one, a vertex at its unique firing time has 3+u, and the two subsequent values are u+b_own and 3+u−a, with a its predecessor-phase count. Both are legal waiting values exactly for 0≤u<a, using a+b_own≤3. The local choices are independent, reconstruct each phase and height from the states, and force least period three. Hence the phase-weight sum is multiplied by 2/3, not by a spatial orbit factor. The 81 states are consecutive-rung pairs; in a twisted closure the terminal pair is the initial pair with both rows swapped, giving the predecessor weights across the seam at both ends. The row involution commutes with the transfer and fixes nine pair states, so the sectors have dimensions 45 and 36. Independent exact characteristic-polynomial computation matched the two displayed factorizations; traces add for the prism and subtract for the Möbius closure, regardless of Jordan blocks. A is strictly positive on the real axis since its remaining quadratic after subtracting (z²+z)² has negative discriminant. The two conjugate moduli are reciprocal, not both one, since otherwise A would be reciprocal. The dominant cosine has subsequences bounded away from zero on both sides whether its angle is rational or irrational in turns (indeed even n suffices, as the doubled angle is nontrivial). This gives sign reversals. For C the three rational brackets give distinct positive roots, Descartes excludes additional positive roots and C(−x)<0 for x≥0. Their product exceeds one so the remaining conjugate pair has modulus below one. The stated triangle bounds for A and for B=(z+1)^4−3z give radii below 4.8 and 3, so the C root above 4.88 uniquely dominates, giving the claimed growth and relative error bound.

## originality

PASS

The graph-general phase count and activity complement are prior and are not credited as new. The exact sector factors for the weighted chip-firing transfer and their consequence for the signed response to twisting are distinct from the closest same-family chip-firing and excitable-wave results.

## value

PASS

The exact counts distinguish two natural seam closures for the same local dynamics. Twisting leaves the dominant growth unchanged yet changes the counts in both directions infinitely often, including within one parity class; this shows precisely where the corresponding period-two parity intuition fails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
