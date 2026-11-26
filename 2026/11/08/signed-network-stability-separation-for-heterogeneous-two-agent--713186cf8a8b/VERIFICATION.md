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

On consistent initialization y_c=x_c+ηx_d is preserved. Eliminating it in unscaled coordinates (x_c,x_d,y_d) independently gives det(zI−A)=(z−1+β)[(z−ν)^2+βν(z−1)]−β²η²ν(z−1), agreeing with the scaled matrix and all cubic coefficients. The cubic Schur reduction with |c|<1 gives the two endpoint signs and D=1−b+ac−c²>0. At ν=−1+δ, β=kδ, the leading terms of −Q(−1), 1+c and D are 4kδ, 2δ and (8−4k)δ, establishing sufficiency for fixed 0<k<2. To control the supremum, c<1 bounds all stable steps because 1−η²>0 is fixed. At ν=−1 the exact D is −β[h²β³−4hβ+4] with h=1−η²; the bracket is positive by min_{u≥0}(u³−4u)=−16/(3 sqrt(3)). Thus every stable step tends to zero as δ→0, and the Taylor remainder in D=8δ−4β+O((δ+β)²) can be absorbed uniformly to give limsup B_-/δ≤2. The verified prior positive exact formula gives lim B_+=2/(1+η), also obtained by the frozen limiting factorization with roots 1 and 1−β(1±η). Independent bounded SymPy algebra formed the Jacobian of (x_c−β(x_c+ηx_d),ν(x_d−βy_d),νy_d+η(x_c^+−x_c)+(x_d^+−x_d)) and confirmed the determinant, limiting D, directional derivative 8−4k and rational witnesses D=15759/10000 and −1161/10000. For the latter a real root r∈(0,1/100) leaves a conjugate pair with squared modulus 1/(100r)>1, and the no-root-mod-seven check plus rational initial vector excludes confinement to the real eigenspace. The repair also shows the initialization plane K satisfies K+AK=R³ and, for ν≠0, tracker recovery from consecutive positions. This justifies the all-initial-positions interpretation. The frozen verification report and source script were read but not run; the proof, not the finite replay, establishes the limit over the entire stability set.

## originality

PASS

The frozen positive branch and its cubic/Jury specialization overlap exact earlier Resultary coverage, not merely a similar spectral-radius certificate. The corrected Finding explicitly narrows the contribution to the sharp fixed-heterogeneity near-negative-endpoint supremum and the resulting separation from the credited positive frontier. Neither the earlier fixed-step signed result, the homogeneous tuning result, nor the inspected general sufficient certificate gives a bound excluding all larger stable steps on the negative branch or its coefficient two. The finite pair illustrates the surviving claim rather than asserting priority for qualitative sign dependence.

## value

PASS

An exact order and leading coefficient for the largest negative-network step give a quantitative limitation on tuning from the unsigned descriptors; the positive ceiling stays bounded away from zero. Controlling all stable steps is essential because a small sufficient interval or one unstable example leaves room for distant stable intervals. This gives a sharp two-agent benchmark for stability safeguards under fixed heterogeneity, not a claim about general convergence rates or an exercise in re-deriving the known positive formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
