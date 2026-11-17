---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Uniform barycentric simplex coordinates have Dirichlet(1,...,1) moments E prod lambda_i^ki=prod ki!/(m)_(sum ki). For sum z_i=0 the exact complex moment identity gives E|Y|²=P/[m(m+1)] and E|Y|^4=(2P²+|Q|²+6R)/(m)_4, P=sum|z|²,Q=sum z²,R=sum|z|⁴. Lower deficit equals [m(m+1)/((m+2)(m+3))]*(|Q|²+6 sum(|z_i|²-P/m)²)/P²; all mth roots unity attain equality for m>=3. For the upper end, the zero-sum fourth-power extremum R/P²=(m²-3m+3)/(m(m-1)) follows by real Lagrange/second variation and extends to complex by x,y Cauchy–Schwarz; |Q|<=P is sharp only for common phase. Classifies real outlier upper equality for m>=4 and all real zero-sum for m=3. Averaging any Hermitian comparison form over S_m reduces it to a scalar P, proving exact Banach–Mazur distance^4=3(3m²-7m+6)/(2(m-1)(m+3)). Independently expanded all 4-index barycentric moments for four complex coefficient tuples in dimensions m=3,4 and obtained exact formula. Finite checks corroborate but do not prove all m.

## originality

PASS

Published October 11 zero-sum ℓ4 hyperplane result gives the needed sharp coordinate quartic bound and permutation symmetrization, but its norm is sum|z|^4 and its B-M distortion grows with m. Here the natural *integrated simplex affine L4 norm* has additional |sum z²|² term, a different lower equality phase condition, and bounded optimal distortion approaching (9/2)^(1/4). General simplex-integration papers provide Dirichlet-moment formula but not the analyzed all-complex extremizers and B-M optimization. The distinct evaluated norm supplies a surviving original result; historical specialized literature remains possible.

## value

PASS

Centered affine functions with uniform simplex volume are canonical finite-element and convex geometry function spaces. The all-dimensional exact complex fourth-moment interval, full equality geometry and sum-of-squares lower defect give natural sharp norm-comparison constants. The exact complex-linear Banach–Mazur distance has a bounded limit while the related coordinate ℓ4 distance diverges, a substantive structural distinction. This is a complete family invariant, not a single unmotivated numerical sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
