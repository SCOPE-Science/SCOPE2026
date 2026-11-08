# Scientific assessment

## Correctness — PASS
The precise graph law follows by independent Poisson thinning and the age distribution \(\mu_u=e^{-x}dx+e^{-u}\delta_u\). The standard inhomogeneous-graph giant criterion [2, Theorem 3.1] applies because the fixed-time kernel is bounded and irreducible. The proof explicitly establishes the exact moment identities, positivity and injectivity of the minimum kernel, the strict spectral quotient inequality, and the endpoint-atom Robin condition. The stationary Bessel limit and monotonicity follow from a common-space kernel coupling. Numerical and symbolic checks replay in `verify.py`; they do not replace the analytic proof.

## Originality — PASS, with priority risk
Artime [1, Eq. (16)] gives the degree-only threshold that is strictly larger than the actual positive-time threshold established here; the paper's finite-time calculation does not incorporate correlations due to the simultaneous reset-history requirement at both endpoints. The general spectral criterion was already proved by Bollobás--Janson--Riordan [2], and their Turova example has exactly the same **stationary** minimum-age kernel and Bessel zero; this earlier coverage is explicitly credited. Crane--Ráth--Yeo [3] employ the same conditional-age graph mechanism in a different component-reset process. Neither inspected source supplies the specific truncated-exponential-with-atom finite-time eigenboundary for [1], nor the strict all-positive-time comparison with [1, Eq. (16)]. This is a model-specific analytical correction, not a claim that the generic kernel spectral theorem or stationary Bessel result is new. Undiscovered published applications and implicit derivations remain a residual priority risk.

## Mathematical value — PASS
The boundary overturns a published time-dependent percolation criterion in a natural, exactly defined resetting graph model, and produces a nonempty regime of qualitatively misclassified macroscopic connectivity at every positive time. The endpoint atom yields a nontrivial Robin eigenboundary. The strict spectral comparison is global, not a numerical or single-parameter counterexample; the same proof also gives monotonicity and the stationary correction. Its sharp scope is the thermodynamic limit with the specified homogeneous Poisson dynamics.

The main supporting literature is Artime [1], Bollobás--Janson--Riordan [2], and Crane--Ráth--Yeo [3]. No claim is made about finite-size critical windows or a new universal inhomogeneous-graph theorem.

Self-review: passed. Independent audit: not yet performed.
