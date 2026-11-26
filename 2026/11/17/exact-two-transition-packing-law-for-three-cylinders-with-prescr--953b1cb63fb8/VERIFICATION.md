---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Analytically checked the normalized line-distance reduction: the foot of each axis has norm 1+r, and with nonparallel directions only the offset difference along the unit common normal controls distance. The given cone yields k=(1-3c^2)/(1+3c^2) for neighboring normals. Fixing the three gap signs and optimizing first over disks gives the simplex dual by bilinear minimax; each dual vector is already in the correct perpendicular plane. Cyclic or pair averaging is valid by convexity and reduces all eight patterns to the two reported values. In the mixed case f'(0)=q+2(k-2)<0; f'(1/2)=q+2(1-2k), whose zero in the required range is k*. The interior second derivative is positive for -1/2<k<1 and solving f'=0 with the negative sign before squaring gives the displayed minimizer. The identity comparing g/q with 1 changes sign precisely at k=0. The witnesses lie on the actual unit circles and the three signed gaps equal the dual optimum on the interior branch; on the boundary branch the third gap is 2k and exceeds 1+q/2 except at equality. At c=0 the coinciding normals allow gaps of absolute size (1,1,2) with the same mixed upper bound 1. In all cases q<sqrt(3), g<=1+q/2<2, so the conversion to radius is finite and increasing. The orthogonal and parallel-limit values follow by substitution and g'(0)=1/(3 sqrt(2)) (derivative in k at the interior minimizer a=1/3), checking the claimed one-sided orthogonal comparison. Contact assertions are about the explicit maximizers, not uniqueness. Inspected the archived numerical diagnostic; the proof, not that finite grid, gives the uniform law.

## originality

PASS

Best-of-knowledge pass for the fixed conical direction family with arbitrary offsets, its sharp radius and its two changes in optimum pattern or active contacts. No originality credit for the skew-line distance formula, minimax or the global unrestricted radius.

## value

PASS

The symmetric direction family interpolates between coplanar, orthogonal and nearly parallel regimes while leaving configurations themselves unrestricted in their offsets. The law gives exact achievable clearances where the unrestricted bound is too coarse, detects a genuine change of sign pattern and the onset of three-way contact, and shows orthogonality is not locally optimal. The explicit disk-to-circle equality witnesses are essential; this is not a substitution into a general unrestricted theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
