---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

For κ_i>0 the two-sided stationary stochastic convolution exists uniquely and is bounded in conditional variance by D/κ_min. At entry to phase i, fresh A_i is independent of inherited position. Ito conditional second moment gives b_{3-i}=q_i+(b_i-q_i) ℓ_i and the displayed solved b. The future attenuation integral after a fresh entry is H_i=h_i+g_iH_{3-i}, with unique solution since 0<g_1g_2<1. Conditional on age u and current holding length a, the conditional coordinate second moment is q_i+(b_i-q_i)e^{-2κ_i u}; integrated future response is (1-e^{-κ_i(a-u)})/κ_i+e^{-κ_i(a-u)}H_{3-i}. Campbell/alternating renewal reward averages their product over u∈[0,A_i] divided by T, yielding M_i and J_i and the exact I formula. Independence of future Brownian increments proves C(s)=E[X_0² exp(-∫_0^sκ_{J_v}dv)] and positivity allows Tonelli; κ_min>0 gives integrability. Stationary Itô balance yields potential energy D/2; two jump-work rewards give (κ_1-κ_2)(b_1-b_2)/(2T). Independent exact rational rederivation from P,Q shows equal τ,ℓ,b, M, occupations, static second moments and W, but g_2(P)=15/64≠19/80=g_2(Q); I_Q−I_P=341004/(919602257 log2)>0 and two-sided S_X(0) gap twice this. Independently recomputed assigned seven-entry Git tree 5de76a613c4639edbe85b3f7134985cfdc7e4208; 96 fresh random exponential-sojourn CTMC resolvent comparisons and 44 equal-stiffness controls passed. Numerical tests only corroborate the analytic all-distributions renewal argument.

## originality

PASS

Frydel (2026) covers the same arbitrary-residence two-state trap and all asserted static/energetic ingredients; these are acknowledged as known. The assessed nontrivial remainder is an explicit integrated lagged position covariance for arbitrary positive finite-mean holding laws, its dependence on additional first-rate transforms, and an exact atomic pair with equal birth/phase second moments and mean work but separated S_X(0). Behme et al. and earlier switching harmonic-trap covariance results require Markovian exponential dwell times; an on/off semi-Markov inverse theorem concerns static marginal inversion instead. Independent Resultary and primary searches found no broader theorem whose statement implies the remainder without a fresh weighted future-renewal computation. This is bounded best-of-knowledge originality, with residual risks.

## value

PASS

For a standard switched harmonic trap, occupations, state-conditioned variance, average potential energy and switching work are physical inverse observables. Their inability to identify low-frequency position fluctuations is a motivated, exact observability boundary. The same-mean, same second-rate-transform witness cleanly isolates a genuinely independent first-rate Laplace signature and shows a researcher why temporal spectra are needed in addition to static/energetic measurements. The explicit nonzero rational spectral gap is not a trivial normalization or a random arbitrary slice; it exhibits a structural difference between one-time second moments and two-time linear response. No general full-spectrum theorem or paper-sized contribution is required for this standalone exact counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
