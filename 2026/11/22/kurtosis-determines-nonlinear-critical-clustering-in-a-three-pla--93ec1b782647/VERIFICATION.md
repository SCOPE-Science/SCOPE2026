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

Differentiating the normalized Gaussian share gives the recorded flow. The mean mode has eigenvalue −4/(9v) at criticality, and the projected eigenvalue vanishes. I expanded all three shares on an arbitrary direction (p,q,−p−q), projected off the mean, and verified the cubic exactly as (13v²−12μ₄)/(27v⁴) times the squared Euclidean norm times the direction. Reflection permits a smooth odd equivariant center graph with no quadratic term. Its O(||z||³) mean contributes nothing to the transverse cubic since the linearization is block diagonal and there is no quadratic field. For a negative coefficient the radial derivative is strictly negative near zero and r⁻² has derivative tending to −2α; the stable mean mode gives full local asymptotic stability. For a positive coefficient the reflection-transposition fixed line (a,−a,0) yields outward trajectories, proving instability. Among finite symmetric laws, the law with total outer mass p on ±√(v/p) and remaining mass at zero has kurtosis 1/p, realizing both sides and equality. Equality itself is not classified. The symmetric Nash remark can also be verified at this critical reach: at a unilateral deviation a write t=a²/v, y=b²/v, r=e^(−t); the paired share is F(t,y)=(2r cosh(2√(ty))+r²)/(4+4r cosh(2√(ty))+r²). For 0<t≤3/2 it is concave in y: with w=2√(ty), the derivative test is (w cosh w−sinh w)(cosh w+k)≤2w sinh²w with k=e^t+e^(−t)/4<5. At k=5 the difference has nonnegative Taylor coefficients. Jensen gives F(t,1)<1/3, by cosh(2√t)<2e^t−e^(−t) (the first three nonconstant difference terms already form a strictly positive polynomial, and the rest are nonnegative). For t≥3/2, F(t,y)<(1+y)/6: for y≤3/2 use monotonic decrease for t≥y and the tangent at y=1 of F(3/2,y), whose value is below .29 and slope lies between .14 and .15; for 3/2≤y≤2 the two opposite-resource shares are below 4/5 and 1/30 respectively; for y≥2 the paired share is below 1/2. Taking the expectation with E[y]=1 proves the strict best response at zero. Every other symmetric profile has a nonzero payoff gradient toward the mean on each coordinate, an available direction even at a finite endpoint.

## originality

PASS

The model and linear threshold are Lovett–Fu’s. The inspected main paper gives a qualitative three-player pitchfork for a specific bimodal landscape, but not the arbitrary finite-law threshold in kurtosis, both signs at the same variance, or critical decay amplitude. In fact Theorem 4 and Corollary 9 of the inspected version literally state a nonlinear ‘if and only if’ stability claim in terms of strict linear stability; the independently checked stable critical example shows that necessity cannot extend to this nonhyperbolic regime under the stated dynamics. The contribution here is the explicit nonlinear computation and sign reversal at equality, not the model or the rate of an abstract cubic equation. Priority remains bounded by the inaccessible supplement.

## value

PASS

The two matched-variance witnesses show that a linear threshold plus variance is insufficient to classify the same model at criticality. The calculation gives one interpretable statistic that settles both stability outcomes away from the sharply specified boundary and fixes the relaxation amplitude in the original time units.

The dated certificate retains the supplied scientific assessment, sources and limitations.
