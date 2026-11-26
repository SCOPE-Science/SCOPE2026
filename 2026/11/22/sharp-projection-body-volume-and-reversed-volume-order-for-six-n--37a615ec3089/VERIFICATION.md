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

The balanced tight-frame Gram projection and the all-ones direction leave a rank-two projection with diagonal 1/3. Its six Gram representatives, scaled to unit complex numbers, have vanishing first and second power sums. Newton identities kill the coefficients of degrees 5 and 4, and unit-root conjugate reciprocity kills degrees 1 and 2. The polynomial in z³ splits the representatives, with multiplicity, into equilateral triples and the corresponding original normals into orthonormal bases with opposite sums. Aligning the sums gives the two latitude rings; permutations and reflection reduce the twist to [0,π/3]. Conversely these rings have the required moments and six distinct nodes. Cauchy's formula and the segment volume identity give 8(π/3)^3 times the sum of the twenty absolute minors. The two pure minors contribute 2; either mixed type gives the entrywise absolute sum of the cross Gram matrix. Each of (2 cos(φ+2πj/3)−1)/3 occurs three times, with only the j=0 entry potentially positive; the cross sum is 1+4 cos φ. This gives 32π³(1+2 cos φ)/27; its strict injectivity on the reduced interval also rules out accidental congruences between different twists. I checked the quoted ordinary-volume formula independently: intersect the six halfspaces at unit support, with a=√(2/3), b=1/√3. All facets are congruent by cyclic rotations and by the reflection interchanging the rings and reversing z. On the upper facet z=(1−ax)/b, use s=y/x∈[−√3,√3]. The radial bound is x≤2/(a D(s)), where D=max over lower azimuths γ of 1+cos γ+s sin γ. There are two affine pieces from γ=φ−2π/3 and γ=φ, split at s=tan(φ−π/3) (one interval may degenerate). For t=2 cos(π/3−φ), D at either outer endpoint is 1+t and at the breakpoint is (1+t)/t. The integral of D⁻² over an affine piece equals its length divided by the product of its endpoint D values; including the Jacobian gives area (2/(a²b))·2√3 t/(1+t)²=18t/(1+t)². Scale to area 2π/3 and apply the pyramid volume formula to recover 4π^(3/2)(1+t)/(9√(3t)). It strictly increases, while the projection volume, hence also its ratio to the squared ordinary volume, strictly decreases. Both endpoint evaluations and the projection-body covariance under invertible maps check; the endpoints are the aligned triangular bipyramid and the three antipodal pairs of the cube. The 20-minor and hull scripts were inspected as supplementary evidence, not executed or used for continuum claims.

## originality

PASS

Credit the prior six-node twist and ordinary-volume result and general Cauchy/zonotope machinery. The distinct supported result is the six-node all-twist projection determinant sum and consequent sharp affine quotient and reversal of volume order. The strongest retrieved statements treat a different invariant on the same family, or the same invariant on different families. The primary comparison is bounded, with an explicit directional-kernel access risk.

## value

PASS

This solves a natural exact affine-geometric comparison on all six-node designs, the first size with a continuous strength-two family (four nodes force the regular simplex and five would leave a rank-one balanced complementary projection with five entries of equal nonzero modulus). It pinpoints a reversal between ordinary and projection-body volumes on the entire interval, not just endpoints, and gives sharp equality and quotient benchmarks in a canonical equal-area realization. The previous ordinary-volume or variance result alone cannot provide this comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
