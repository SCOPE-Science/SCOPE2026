# Scientific review

## Correctness — PASS

The centered two-residual ridge objective has the unique minimizer \(\gamma_\lambda=-WT/(T^2+\lambda)\) for \(\lambda>0\), and produces the exact error representation in `RESULT.md`. Normal orthogonal contrasts are independent. The moment threshold is proved from the exact tail coefficient for \(E_0=\theta+dW/T\); the ridge singularity follows from a normal-density local integral with coefficient \(\pi d^2 p_\sigma(0)m_2/2\). A Gaussian Taylor expansion with exponentially small exceptional-set control yields the exact fourth-order polynomial \(Q(c)\). Its strictly positive quadratic coefficient proves uniqueness when \(\theta\ne0\). The standalone symbolic-numeric verifier passed 155 deterministic checks, including symbolic coefficient equalities and direct noisy-update comparisons. Computation supports, but does not substitute for, the infinite-domain proof.

## Originality — PASS (qualified)

Scieur, d'Aspremont and Bach (arxiv:1706.07270) already introduce regularized nonlinear acceleration; two-coefficient ridge weights themselves are not new. Toth et al. (2017, doi:10.1137/16M1080677) study inaccurate Anderson evaluations under different coefficient and local-control conditions. Wei, Bao and Liu (arxiv:2110.01543) study adaptively regularized stochastic mixing, and Pollock and Rebholz (arxiv:2211.12953) study conditioning filters. None of the inspected primary statements gives this exact fixed-site Gaussian one-step risk law or its fourth-order coefficient minimizer. Deterministic scalar Aitken-Steffensen robustness in the published mathematical record is distinct from this noisy distributional question. Ordinary Gaussian-ratio tails are known and are credited, not claimed new. Specialist precedents under alternative names remain possible; the full source and query comparisons are in `AUDIT.json`.

## Value — PASS

Ridge selection in two-point stochastic extrapolation is a natural numerical question, because near cancellation of residual differences can induce huge random mixing weights. This result proves that the unregularized risk is mathematically infinite despite arbitrarily small Gaussian perturbations, determines the exact weak-ridge singularity, and specifies the sharp fixed-scale asymptotic tuning coefficient. Its usefulness is in calibration and cautionary stability benchmarking rather than a general solver guarantee.

## Residual limitations

Only scalar affine contractions and deterministic input sites are analyzed. Noise is independent, identically distributed Gaussian. The fourth-order ridge tuning applies to nonzero midpoint offsets and fixed positive \(c\) as \(\sigma\downarrow0\); global finite-\(\sigma\) optimality, nonlinear adaptive histories, and higher dimensions remain unproved. The closest algorithmic prior work introduces the method; this contribution is a new exact risk analysis under the stated model, conditional on unindexed-specialist precedence.

Self-review: passed. Independent audit: not yet performed.
