---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For orientation jumps j->j+1,j-1,j+2 at rates a,b,h and a+b=M>0, exact 4x4 tilted characteristic polynomial is λ(λ+2M)[(λ+L)^2+Ω^2]-k²v²(λ+M)(λ+L)+k⁴u²w² with L=M+2h,Ω=a-b. A simple principal eigenvalue near k=0 yields κ2/t=v²L/Q and κ4/t=-3v⁴[F+Q²sin²(2θ)]/(M Q³), Q=L²+Ω², F=L[(2M-L)L²-(L+2M)Ω²]. The inequality F+Q²>0 proves strictly negative diagonal rate. Algebra reduces the axial sign to χ² > (1+2q)²(1-2q)/(3+2q) for q<1/2, with q=h/M, χ=Ω/M; differentiation yields its unique maximum q*=sqrt(5)/2-1 and the positive/negative/positive reversal witness at χ²=7/20, q=0,1/8,1/2. Independent symbolic determinant and fourth-order cumulant coefficient comparisons returned exact difference zero. Finite-state spectral gap (including a=0 or b=0) justifies cumulant rate limits; not a claim about finite-time signs.

## originality

PASS

Published 2026-10-25 SCOPE result already fully covers the h=0 quarter-turn-only sign and angular sectors and is credited. Mallikarjun–Pal 2022 gives the exact three-rate generator and full forward transform but only reports leading t² raw fourth moment; the linear connected cumulant and sharp nonmonotone h-dependent axial phase are not explicitly covered in inspected text. Later Resultary arbitrary-angle tumbling envelopes concern a uniformly continuous initial orientation, not lab-frame fourfold anisotropy of this lattice-supported process.

## value

PASS

The nonmonotone reversal-controlled kurtosis phase distinguishes walks with identical isotropic diffusivity; a sharp parameter-space boundary, diagonal obstruction, and reentrance are mathematically motivated new classification beyond the known h=0 case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
