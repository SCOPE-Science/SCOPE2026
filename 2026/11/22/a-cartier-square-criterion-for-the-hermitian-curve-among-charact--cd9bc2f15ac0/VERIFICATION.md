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

The homogeneous plane quintic is smooth: at infinity F_Z=1, and at finite points a potential singularity would have y=0 and be a repeated root of f. Adjunction gives the six differentials. Independently, x is separating and the Cartier rule on (A²+xB²)dx returns B dx. Write f=f_e²+xf_o² with f_e=x²+√b x+√d and f_o=√a x+√c; use y=f/y⁴ and factor the square denominators out of Cartier. This reproduces the six images; three are independent as (a,c) is not zero, the second image is spanned by a^(1/4)ω02 and b^(1/4)ω02, and the third is zero. Stable rank and first rank give 2-rank zero and a-number three. On a=b=0, c≠0, take a root β and α³=c, so x=αu+β and y-rescaling yield the Hermitian model. The converse uses invariance of Cartier and uniqueness of the equal-exponent cover (the divisor difference is five-divisible and Pic(P¹) has no 5-torsion). Trace and norm fibers over F16 give 4(1+3·5)+1=65. The finite-field script is corroboration only; it was inspected, not run.

## originality

PASS

Best-of-knowledge PASS for the explicit full-family two-stratum characterization, not the known Hermitian member or the general computational machinery.

## value

PASS

This identifies a distinguished branch configuration by an intrinsic invariant that separates it from every other member despite constant a-number and p-rank. The all-parameter rank profile and geometric converse are useful; the known Hermitian point count is not the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
