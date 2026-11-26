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

Independently reconstructed the killed excursion by reflecting with the ghost value u_{L+1}=u_L in the Laplace recurrence, and obtaining τ_r(L)=(sinh θ/r)tanh((L+1/2)θ)−1/2, with 2(cosh θ−1)=r. Subtraction gives exactly the quoted δ_n. Each tooth mass equals its entrance flux times τ_r, and flux cancellation leaves the unique constant stationary weight on the finite periodic backbone. The strong law applies at fixed r>0; at zero, truncation proves divergence of the sample mean when the first moment is infinite. In the open tail ranges, δ_n on n√r=x tends to sech²x, and 1−δ_n to tanh²x; the bounds by Ce^(−2nθ) and min(1,rn²) control the discarded tails of the scaled integrals. At α=1 the error in replacing δ_n by the hard cutoff at r^(−1/2) in the weighted sum is O(1). At α=3, for nθ≤ε the relative error in 1−δ_n≈rn² is O(ε²+r) uniformly, while the omitted tail is O_ε(r); the truncated sum of n²s_n contributes (c/2)log(1/r). Above three, dominated convergence gives the cubic moment exactly. Substitution proves the five drift equivalents and extended right-slope classification; monotonicity follows directly from exponential truncation. Independently solved a heterogeneous four-junction rational generator and the first two tooth-moment systems (L=1,2,4,7); an α=3 numerical sum with a bounded omitted tail gave ratio ≈1.077 at r=10⁻⁸, consistent with slow logarithmic convergence, not used as proof. The supplied checker was read, not run: its 'exact' tests include floating-point comparisons to the hyperbolic formula, and the tail limits are not checked by it. Scope is sequential stationary-ring, volume and weak-return limits, with unit vertical rate and a survival tail, not a mass tail or a pathwise infinite-comb speed.

## originality

PASS

The reset excursion and stationary normalization are established methods. The audited contribution is the five-regime weak-return law with constants for independently biased backbone and symmetric reflecting teeth of regularly varying lengths. Prior local-returns work uses outward-biased trapping, with different moment requirements and, in the closest indexed result, geometric lengths and log-periodic behavior. Even an extension of its current identity to independent vertical parameters does not transfer its weak-rate expansion to these unbounded tails. General Laplace-transform asymptotics need the appropriate mixed excursion-time tail and amplitude as inputs.

## value

PASS

Stationary transport restoration and linear susceptibility test two different divergence mechanisms, not merely two names for a trapping transition. The exact α=1 and α=3 log laws distinguish arbitrarily slow restoration from divergent first-order response, and the coefficients specify what a finite-rate measurement should approach. These results are useful for the natural whole power-tail family without extrapolating to different tooth bias, trajectory limits, or concurrent volume/rate scaling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
