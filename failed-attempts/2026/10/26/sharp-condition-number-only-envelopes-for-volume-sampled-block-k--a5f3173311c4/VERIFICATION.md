---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Verified the projector identity and reconstructed the extrema. The t-derivative of the z^k coefficient of det(I+zA(I+tyyᵀ)Aᵀ) sums w_S yᵀP_Sy over full-rank blocks; singular blocks have identically zero determinant. On the Gram eigenbasis this coefficient is the quadratic form with diagonal λ_i e_{k−1}(λ_{−i}), and the normalizer is e_k(λ). Pairwise subtraction gives p_j−p_i=(λ_j−λ_i)e_{k−1}(λ_{−i,−j})/e_k(λ), strictly reflecting ordering when k<N and the eigenvalues differ. At endpoints 1 and κ, μ=1/(1+e_k(κ,u)/e_{k−1}(κ,u)) decreases in the intermediate entries u. The condition ratio is κ(t+1)/(t+κ), with t=e_{k−1}(u)/e_{k−2}(u) increasing in u. For an exposed coordinate, the derivative of each consecutive symmetric ratio has numerator b²−ac for successive coefficients a,b,c; normalized Newton is strict when both neighbors are positive, and if one is zero the numerator is b²>0 in the interior k range. Evaluating u≡1 or u≡κ gives the four bounds and shows uniqueness of the interior spectral profiles, not of the matrices. For a prescribed rectangular m, pad the attaining diagonal A by zero rows, which have zero sampling weight. At k=1, F=B/tr B; at k=N, F=I; at κ=1, F=(k/N)I. The projection Pythagorean identity yields worst factor 1−μ, with the sharp ceiling threshold obtained by solving the monotone inequality in k, including δ=1.

## originality

FAIL

The distinct indexed record b4d8c12466a2 directly states the lower-μ/upper-χ half and the cutoff. Its proof also explicitly establishes the same formulas, strict Newton monotonicity and equality machinery needed for the other half. Holding the largest eigenvalue fixed at κ and plugging the lower endpoints of the proven coordinatewise comparisons gives the claimed upper μ, lower χ and unique alternate profile mechanically. This is demonstrable coverage by a stronger proof step, not an inference of historical priority from catalogue dates, and not a correctness objection.

## value

FAIL

Condition-only one-step geometry is a meaningful design question, but this record does not establish a substantive increment over the matched result. The cutoff already appears there, and the added opposite envelopes and extremizers are just the other endpoint evaluations of its explicit monotone formulas at fixed κ. The worked example and the proof of the known transform do not supply a surviving independent advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
