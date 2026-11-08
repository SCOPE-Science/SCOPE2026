# Scientific review

## Correctness — PASS

The conditional Itô-integral representation gives the exact mean and conditional variance. Brownian self-similarity turns the rescaled variance into a deterministic singular-endpoint Laplace integral, and a pathwise dominated-convergence argument applies whenever the Brownian endpoint is nonzero, an almost-sure event. The independent Gaussian mixture gives the full joint limit, and a separate dominated-convergence calculation proves the two-sided tail constant and moment threshold. The 16 deterministic numerical checks independently confirm the integral scaling and Gaussian-mixture constants. Finite experiments are not a proof; the analytical argument is the proof.

## Originality — PASS, qualified

The closest same-object source, Gupta and Klapp (arXiv:2609.33751v1), obtains finite-time conditional representations and moment asymptotics, and notes that averaging the thermal positional law is difficult. Its identifiable distributional calculation concerns the zero-temperature model, not the rescaled positive-temperature law. The earlier Gupta–Klapp stationary OU-stiffness paper (arXiv:2507.20915) concerns a stationary, sign-changing environment and has no direct implication for the growing positive Brownian-power stiffness. The Cauchy distribution of a Gaussian ratio is classical (Pillai, arXiv:1602.08181), but the reduction of this time-dependent stochastic trap to that ratio in the long-time limit is not furnished by the cited ratio theorem. Searches of published mathematical claim summaries did not reveal a covering assertion. Absence from a search is not proof of absolute novelty.

Residual priority risk: a more general, unindexed stochastic-averaging theorem could imply the entire family. Not all sections of every potentially relevant article were accessible at full-text level. The prior literature's moment formulas are stronger in a *different* direction (finite-time moments), not in the distributional scaling direction.

## Mathematical value — PASS

The source leaves the positive-temperature position density unaveraged, while its moment asymptotics decay anomalously. The exact weak limit identifies what a typical rescaled particle sees: a heavy-tailed Gaussian scale mixture, and at the physically studied quadratic stiffness a Cauchy distribution. Its sharp tail exponent and moment threshold explain why a typical scaling limit cannot be recovered by rescaling the source's low-order moments. Extending to all positive Brownian powers also resolves the natural higher-power direction explicitly identified in the motivating paper, with a single structural theorem rather than arbitrary parameter examples.

## Scientific limits and verification status

The result does not establish convergence of unbounded prelimit moments, convergence rates, multitime limits, or claims about heat and work. Independent validation has not been performed. The numerical checker is supplementary to the proof, not a substitute for it.

Self-review: passed. Independent audit: not yet performed.
