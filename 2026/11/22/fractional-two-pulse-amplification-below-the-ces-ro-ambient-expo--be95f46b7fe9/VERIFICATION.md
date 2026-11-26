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

For 1≤p<∞, 0<q<p and 0<α<1/p, write r=αp, d=αq, b=r−d, θ=q/p. For j≥N the single-coordinate average is maximal at j=N and is N^(d−1)Σ h^(−d), bounded above by the corresponding integral and converging to 1/(1−d). For the p-orbit average, interchange the sum over time and the nonnegative coordinate sum; a coordinate j<N contributes at most j/[N(1−r)], and j≥N contributes at most 1/(1−r). Jensen gives the stated upper bound for C, which is not defined with a q-th root. Weighted p-masses ε and 1−ε at floor(sN) and N yield the stated Riemann limit: split at the two singularities and use subadditivity of the θ-power and summable h^(−d) tail bounds. The right derivative is dominated by a multiple of (A_s+A_1)A_1^(θ−1) and is θ[I(s)−1/(1−d)]. With η=(1−s)/s the substitution t=s(1−u) gives I(s)=s^(1+b)[1/(1−d)+J(η)]; by the fundamental theorem of calculus, Tonelli, and u=vw, J(η)=b∫_0^η v^(−d)∫_0^(1/v)w^(−r)(1+w)^(b−1)dw dv. The inner integral tends to B(1−r,d), and the prefactor correction is O(1−s)=o((1−s)^(1−d)). The positive derivative first fixes s, then ε, then gives a genuinely finite two-coordinate witness at large N. Independently summing the orbit norms for (p,q,α)=(2,1,0.4), N=200000, j=190000 and p-masses 1/4,3/4 gave 1.68995648807005 against 1.66666666666667. This is a diagnostic, not the universal proof; no exact unrestricted optimum is asserted.

## originality

PASS

The supported distinct claim is universal strict amplification over the one-coordinate test below p, with a two-coordinate mechanism and quantitative first-variation law. The power-weight regime, boundedness results, and rigidity of the basis test for q≥p are prior, not credited as new.

## value

PASS

Basis testing is an exact norm-constant principle above and at the ambient exponent. Establishing its universal strict failure below that exponent in the canonical power-weight family, with a minimal-support witness and an explicit positive coalescence scale even for q<1, resolves a natural extremal question rather than just giving a numerical improvement in a single example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
