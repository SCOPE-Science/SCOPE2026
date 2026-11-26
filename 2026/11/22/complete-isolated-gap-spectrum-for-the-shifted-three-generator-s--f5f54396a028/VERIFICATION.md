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

I checked the formula by partitioning the integers into slices ta+r, 0≤r<a. In a t-coin band the offsets with exactly j nonzero summands form [3j,4j]; for j≥2 successive intervals touch, so the t≥2 band is {0,3,4} and [6,4t] in offsets. For t≥3 the previous terminal interval starts at (t−1)a+6≤ta. Therefore earlier-band coverage of the slice is exactly its prefix ending at E_(t−1)=(t−1)(a+4); older bands cannot extend it, and no later band begins inside the slice. In t=2 the previous band cannot reach 2a. Offsets 3,4 are covered, and offset 1 cannot stand by itself because earlier coverage of offset 2 also covers 1. A missing offset 2 has both neighbors precisely when E_(t−1)=ta+1; a missing offset 5 always has both neighbors for t≥2 and is missing iff E_(t−1)<ta+5. The remaining possible hole at the end of a slice is isolated only when E_t=(t+1)a−2. For a=6 the possible offset 5 is just before the next slice. For t=1, only the terminal boundary can furnish an isolated gap because its members are a, a+3, a+4; before a there is none. Solving the equations yields both residue exceptions and the stated range for t. The extra term has a residue distinct from 5 except for a=6, where it is 11, below the first main term 17. I also independently matched 158 complete gap sets for a=6..163 by minimizing y(a+3)+z(a+4) in each residue over 0≤y,z<a. Larger coefficients cannot be minimal because a copies can be subtracted.

## originality

PASS

The all-parameter formula for this exact triple survives comparison with explicit spectra for neighboring families, one covered quotient instance, and general perfect-closure methods. The contribution is the complete set for a≥6, not the definition, a general isolated-gap algorithm, or the a=7 case.

## value

PASS

Isolated gaps are the precise exceptions relevant to perfection and closure. This natural consecutive-offset triple is an infinite minimal three-generator family where fixed-coin bands have a persistent isolated hole at offset 5; the exact set separates these recurring holes from two arithmetic boundary mechanisms. This gives concrete inputs to closure calculations and a sharp test case for broader offset families, not just a few enumerated examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
