---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The active affine equilibrium gives p,q and the stated open feasibility interval. After shifting to this equilibrium and rescaling the second neuron's deviations by 1/σ, the symmetric and antisymmetric modes decouple. The symmetric 2×2 block has negative trace and positive determinant; the antisymmetric block has trace zero and determinant ω²>0. A nonzero stable component cannot return after a positive period, and this argument applies even when a nonnegative periodic orbit touches the thresholds, where the affine and rectified vector fields agree. On the center plane u=v+τ_y v̇, with v harmonic of amplitude ρ, so max |u|=Kρ. Both firing inequalities hold iff Kρ<=min(p,q/σ), which excludes nonconstant orbits at either endpoint or outside the interval. The projected map from harmonic coordinates has constant Jacobian ωτ_y, and the two orthogonal embedding columns give intrinsic area multiplier 1+σ². The two positive affine bounds increase and decrease respectively, crossing only at r=σ, so radius and area have a unique maximum there; both threshold contacts occur at opposite phases. The exact primitive period follows from any nonzero harmonic component. Independent rational block/threshold checks at (τ_x,τ_y,b,σ,s_1)=(2,3,2,3/2,7/5) give R²=3/400,3/100,3/400 for r=7/6,3/2,21/10 and the predicted graze multiplicities (python /workspace/branches/independent_replay.py 1). Those checks supplement the argument; the frozen SymPy script was inspected but not executed.

## originality

FAIL

The distinct indexed grazing-circle result b24f77cdacfa establishes the identical active-center invariant and exact two-threshold cutoff under the same assumptions, with the stable complementary block and the period explicit. The frozen radius and area are its direct affine-coordinate rewrite and Jacobian, and maximizing that area is mechanically the intersection of the two affine thresholds already specified there. This is demonstrable equivalent coverage, not an assertion of chronological priority: the matching record carries a later catalogue date than the frozen record. Muramatsu–Kori provides earlier center and qualitative-grazing coverage, but is not needed to infer priority for the exact formulas. The inaccessible 2011 full text is not the reason for failure.

## value

FAIL

The active excursion envelope is a natural quantity for models of firing-threshold contact. However the same envelope, period and contact multiplicity are already supplied by the exact indexed center family. The remaining area and optimum simply measure that known ellipsoid by a fixed Jacobian and maximize the square of its known piecewise-affine cutoff. They do not supply an independently unknown invariant or a substantive residual boundary classification under the scientific value criterion. No repair is proposed; a different switching or optimization problem would require a new result, not an edit to this one.

The dated certificate retains the supplied scientific assessment, sources and limitations.
