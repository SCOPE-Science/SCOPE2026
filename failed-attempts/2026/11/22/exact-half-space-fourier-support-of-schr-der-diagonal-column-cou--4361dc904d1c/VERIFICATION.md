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

The signed transfer K_i(h,h′)=1_{h′≥h−1}+z_i 1_{h′≥h}, z_i=(−1)^ξ_i, counts the unique possible initial north run for each chosen east or diagonal step and pair of allowable heights. In the first column both indicators are one, so the factor is 1+z₀. A separate proof expands every Schröder diagonal into NE, giving a Dyck path with some of its peaks marked. If C(D) is the set of columns in which an NE peak of D starts, the character sum is exactly Σ_D ∏_{i∈C(D)}(1+z_i). The first east step is necessarily a peak from column 0; thus ξ₀=1 kills every term, while ξ₀=0 gives nonnegative even contributions. The one-peak path NⁿEⁿ contributes 2 in every surviving case. For 1≤i<n, NⁱEⁱNⁿ⁻ⁱEⁿ⁻ⁱ has peaks in precisely columns 0 and i, adding 4 if ξ_i=0. Thus only (0,1,…,1) minimizes over the nonzero spectrum. Every term is bounded by its value at ξ=0, and the zigzag (NE)ⁿ loses its strictly positive term if any ξ_i=1, proving uniqueness of the maximum R_n. At n=1 the same single coefficient realizes both extrema. The Walsh characters diagonalize unnormalized convolution; the surviving characters are exactly those independent of the first coordinate. Hence rank, nullity, range, and restricted condition number follow. Fourier inversion gives equal counts μ_n(0,w)=μ_n(1,w), so the first bit is fair and independent of the marginal, whose transform consists of the surviving coefficients and never vanishes. Marking any subset of the zigzag peaks also verifies full incidence-vector support.

## originality

FAIL

The exact theorem is a direct corollary of a published, position-preserving combinatorial construction. Drake's arbitrary-subset peak flattening in §1.1 provides the fibers and independent choices; assigning the sign of each peak's east-step column and summing independently proves the complete position-refined product. The extrema then follow by the one-peak, two-peak, and zigzag paths, and all operator properties are consequences of Fourier diagonalization. Drake does not state the Walsh theorem verbatim; it is the construction, not the univariate total alone, that implies it. The separate height-transfer proof is valid but does not avoid this prior implication.

## value

FAIL

The counting kernel and the question of its null space are natural, and the formulas are correct. But this exact invariant is mechanically forced by the known independent peak-subset construction: a forced first peak, an elementary two-peak witness in each other column, and the zigzag suffice. The remaining calculations are standard Walsh consequences, with no separately useful new structural result demonstrated in the frozen finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
