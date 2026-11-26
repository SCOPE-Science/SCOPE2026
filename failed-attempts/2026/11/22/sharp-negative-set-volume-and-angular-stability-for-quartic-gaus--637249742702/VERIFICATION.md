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

For the specified Fourier convention, applying Q(i∂/(2π)) to the Gaussian gives Q−ΔQ/(4π)+Δ²Q/(32π²); applying a homogeneous quadratic R similarly gives −R+ΔR/(4π). Hence the quadratic term forced by self-duality is −ΔQ/(8π), with exact cancellation of the constant terms; the only free constant is zero at the origin. Polar differentiation gives ΔQ(rω)=r²[4(d+2)A+Δ_SA]. Because A>0, the negative radii satisfy 0<r²<h with h=(d+2)/(2π)+Δ_SA/(8πA), giving exactly v_d E[(h_+)^(d/2)]. The polynomial zero set is null. Integration by parts on the sphere gives E[Δ_SA/A]=E[|∇_S log A|²]; Jensen for the positive-part power proves the bound. The angular term vanishes only for constant A, establishing the sharp radial minimum; in d=2 h_+=h+(-h)_+ gives the additional exact clipping term without assuming h≥0. The inequality is not an equality formula at every nonradial profile in higher dimension. The accompanying symbolic/finite numerical checker was inspected, not executed; the recorded assertions are not needed for the proof.

## originality

FAIL

Demonstrable statement coverage by the distinct indexed record e978760b78fd, not by this record's own search hit. That record has the same sharp bound and angular penalty on every strictly positive leading quartic, plus a broader full-shell minimum and equality theorem. Its exact polar formula and spherical identity also yield the d=2 clipping formula by h_+=h+(-h)_+; the earlier 7fbca0facafa catalog summary expressly includes that planar angular-plus-clipping decomposition. No distinct scientific claim remains here. The two all-dimensional records share a catalog date, so neither order nor historical priority is inferred.

## value

PASS

The mathematical content addresses a natural definite-set problem: it rules out a nonradial minimizer in a genuine finite-dimensional Fourier shell and gives a useful scale-invariant energy penalty. This is valuable as a result, but the equivalent coverage prevents this narrower record from counting as a separate contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
