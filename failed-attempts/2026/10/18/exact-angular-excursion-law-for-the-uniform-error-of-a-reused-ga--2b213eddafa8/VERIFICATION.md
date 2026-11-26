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

For a nonzero probe the residual is rank one: applying diag(1,ε) to the normalized perpendicular to (cos φ, ε sin φ) gives the norm ε/(cos²φ+ε² sin²φ)^(1/2). The Gaussian direction is uniform on the projective circle; continuity makes the swept angle a full interval. The distance d to the interval shifted by the orthogonality angle has mass α/π at zero and density 2/π on (0,(π−α)/2) for α<π. For α≥π the distance is identically zero. Inverting the decreasing residual as a function of d gives the stated tail, including the atom at 1 and the saturated part near ε. Averaging over d gives the stated mean. For b=(π−α)/2>0, subtracting (u²+ε²)^(−1/2) from the mean integrand gives a difference bounded by O(u) near zero and converging in integral to ∫₀ᵇ(csc u−1/u)du=log(2 tan(b/2)/b), even for b=π/2. Adding arsinh(b/ε) gives the claimed constant in the logarithm. A tangent substitution gives the one-point squared mean ε; Tonelli gives Tε. The probe zero has Gaussian measure zero, and the best rank-one error is the trailing singular value in both norms.

## originality

FAIL

The central exact distribution is substantively covered in distinct indexed records: one gives it in a stronger power-iteration setting and the other in relative squared error with refresh. Their catalogue dates are later than this frozen record's date. This is a judgment of demonstrated coverage now, not evidence that the indexed matches had historical priority or that this record was derived from them. Kressner–Lam's earlier uniform theorem is not equivalent. The explicit first mean and logarithmic term are direct consequences of the already covered distance law and the standard incomplete elliptic integral reduction, rather than an independent surviving finding.

## value

FAIL

The unoversampled rotating example is a useful concrete witness distinguishing integrated from worst-parameter error. Its full-error probability and exact profile are already available in the broader indexed treatments, however. The extra display of the first moment is a routine integration of their exact law; extracting the logarithmic endpoint does not establish an independent gap beyond the covered model-specific diagnostic. No substantive repair is supported.

The dated certificate retains the supplied scientific assessment, sources and limitations.
