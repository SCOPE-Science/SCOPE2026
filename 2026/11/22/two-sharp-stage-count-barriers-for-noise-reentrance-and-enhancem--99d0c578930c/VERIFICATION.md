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

The invariant law of the phase chain is proportional to 1/d_i, d_0=s and d_i=1 otherwise; weighting the drift δd_i therefore gives nδ/(n+a). The unwrapped corrector increments solve p g_i−q g_{i−1}=v(1+a 1_{i=0}), and the periodic geometric Green function has sums 1/δ and (p^n+q^n)/[(p^n−q^n)δΣ] for its first and second powers. These give the stated bracket rate. I additionally checked D by a tilted-generator calculation independent of solving the corrector. Write the Fourier eigenvalues of the periodic homogeneous tilted matrix as μ_j(k)=p e^k ω_j+q e^(−k)/ω_j−Σ, ω_j=exp(2πij/n). The speed defect changes the eigenvalue equation to the homogeneous tilted matrix minus λ(I+aE_00). The rank-one determinant identity, isolating the j=0 term, yields (μ_0−λ)(1−(aλ/n)∑_{j≠0}(μ_j−λ)^−1)=aλ/n. At k=0 the sum is Σ(1−y_n)/(2δ²): by partial fractions it is (1/δ)∑_{j≠0}[1/(ω_j−1)−ρ/(ω_j−ρ)], ρ=q/p, whose two sums are −(n−1)/2 and nρ^n/(1−ρ^n)−ρ/(1−ρ). Expanding λ=v k+D k² gives D=Σ/2 [n/(n+a)+n a²(y_n−1)/(n+a)^3], precisely the announced expression. The eigenvalue at zero is simple and the finite tilted semigroup has a spectral gap at k=0, so its first two derivatives give long-time cumulant rates for each initial phase. The derivative has sign of −B_n a²+(2y_n−4)a−n. For y_n∈(1,4) its discriminant is negative; for y_n≥4 any real roots are positive, and at 4 the positive zero is double and monotonicity remains strict. This also checks all accelerated defects. The baseline difference has sign of −a[a²+n(3−y_n)a+n²]; for a>0 this yields a single positive enhancement interval precisely at y_n>5, with equality alone at a=n when y_n=5. Finally y_n=n tanh(t)coth(nt), t=log(p/q)/2, strictly increases from 1 to n since sinh(2nt)>n sinh(2t). This proves the sharp stage counts, equality cases and uniqueness/order of both finite bias thresholds. At n=6, a=6 the ratio equals (3+y_6)/8, confirming the quoted example to its stated precision. The source script CHECKER.py was inspected, not executed.

## originality

PASS

The drift and diffusivity themselves are not credited as new. In addition to the acknowledged general periodic formula, the actual all-profile kinetic corrector in the balanced-defects catalogue record directly specializes to this D. Pass the distinct complete reentrance-versus-baseline classification: the competing thresholds 4 and 5 in the bias variable, stage cutoffs, equality cases and exact windows of a strength scan. The strongest inspected comparisons neither state nor establish these features as a specialization of a general shape theorem. The judgment is bounded and does not establish priority.

## value

PASS

The two thresholds separate a genuine noise-design question into two independently meaningful effects: a slowed site can first increase D locally as its slowness grows without ever improving on homogeneous noise. The exact minimum periods, sharp bias boundaries, and single enhancement window tell when these effects can occur while drift always worsens. This is a natural complete classification of the simplest one-defect slice, not a recomputation of an exact diffusion entry or a claim about experimental motors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
