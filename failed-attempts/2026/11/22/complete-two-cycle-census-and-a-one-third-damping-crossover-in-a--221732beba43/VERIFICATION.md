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

For consecutive points (a,b,z),(b,a,w), eliminating z,w gives the reduced residuals K_1=b(m+z)-Aa and K_2=a(m+w)-Ab, with z=α(a²+rb²)/(1-r²) and w=α(b²+ra²)/(1-r²). A=1-n>0 makes zero coordinates yield the origin; a=b gives a fixed point and a=-b≠0 gives the unique symmetric cycle exactly under the first strict inequality. For Δ=a²-b²≠0, aK_1-bK_2=Δ(-A+αab/(1+r)) and bK_1-aK_2=-Δ(m+αr(a²+b²)/(1-r²)); the row transformation has determinant -Δ, so the sum/product constraints are necessary and sufficient. Positive distinct squared roots exist iff S>2|B|, with just two reflected orbits after quotient by phase. At equality the roots coincide. An independent derivative check: eliminate the third coordinate from F²-I by first using residual rows for the two second-coordinate equations and the third-coordinate return; subtract multiples of the first row to account for the intermediate second coordinate a+K_1 instead of a. The scalar Schur factor from the third-coordinate return is r²-1, giving det(P-I)=(r²-1)det DK. Differentiating the two factorizations at an asymmetric zero yields det DK=-2rΔ²/((1+r)(1-r²)), hence the asserted identity. The real monic characteristic polynomial is negative at 1 and positive at large arguments. The threshold difference for α=1 is A(1-3r)/(1-r), and for α=-1 the two thresholds are strictly ordered for every admissible r. The strict endpoints and the square-root discriminant onset both agree.

## originality

FAIL

The α=-1 global census, onset and collision type are explicitly covered by Resultary 6fdbde1ad9b7. Record d924c7a65241 gives the α=+1 census, determinant and damping crossover for negative n as stated, but the actual proof and the return-residual normalization transfer these results mechanically to positive n. Known second-iterate duality then transfers the off-symmetry determinant to α=-1. Thus there is material prior coverage and no distinct nonmechanical main claim left in the frozen finding. Inaccessible Gonchenko papers are not the reason for failure.

## value

FAIL

A global low-period census and a forced real multiplier would be mathematically useful for this normal form. But the frozen contribution beyond the directly covered negative-sign census is a homogeneous reparameterization of an existing complete return calculation plus a published second-iterate equivalence, not a further stability or bifurcation result; there is no independently useful distinct remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
