# Self-review

## Correctness — PASS

The asserted claim is one theorem with exact finite joint survival (1), its two point-process limits, and the macroscopic threshold. For the model with replacement, the product over independent new-vertex parent choices gives the multivariate probability exactly. The all-order product upper bound controls every coefficient in the Laplace functional, so the fixed-fan-in Poisson limit is not an extrapolation from finite enumeration. In the logarithmic window the centering \(b_n\) is chosen by the cumulative first moment, and a uniform power-sum integral estimate, a negligible joint-probability ratio, and the same dominated Laplace expansion prove the \(e^y\,dy\) Poisson limit. An explicit small-left-tail bound closes the void-probability argument for the minimum. The two outer birth-fraction regimes use Markov's inequality, negative pair covariances, and Chebyshev's inequality. Boundary conditions: \(n\ge2\), fixed \(k\ge2\) in the Weibull limit; integer \(k_n\ge2\) in the logarithmic and outer regimes. No finite checker is treated as proof of a limit.

The actual `verify.py` executed from the complete candidate package and passed 497 exact joint-moment and related checks including twelve exhaustive small ensembles, plus deterministic first-intensity scaling checks. The analytic proof, not this finite test, carries the infinite assertions.

## Originality — PASS, with residual priority risk

The closest research record establishes an oldest-leaf Poisson point process only for *single-parent* recursive trees; its statement does not imply the \(k\ge2\) intensity exponent or the logarithmic-fan-in Gumbel birth-fraction crossover. Devroye and Janson (arXiv:0906.0152, 2009) provide the *same* multi-parent random graph, but prove root-path depth laws. Javanian and Vahidi-Asl (2011) prove a global-output-count Gaussian law for a different distinct-parent model, not earliest childless birth labels. Janson (2023) obtains descendant set sizes in this model, a different statistic. Research-record comparisons for oldest outputs, leaf-sparsity, Weibull and Gumbel aliases found no covering multi-parent birth-label point process or varying-fan-in frontier. The inaccessible Tsukiji–Mahmoud binary-circuit article is a named residual historical risk, not represented as fully excluded. No independence or worldwide priority has been externally certified.

## Value — PASS

The location of the *oldest* childless vertex determines how far back a live output persists in a growing recursive circuit, unlike a global count of outputs. The theorem identifies two distinct natural extreme-value universality classes and a sharp parameter scale: fixed fan-in yields a \(n^{k/(k+1)}\) age with a Weibull tail, while fan-in proportional to \(\log n\) moves the first childless vertex to a deterministic positive birth fraction and produces a reversed-Gumbel window. This crossover and its finite multivariate input are mathematically motivated, not an arbitrary slice of small cases. The fixed \(k=1\) theorem is acknowledged as previous work and is not included as a newly claimed finding.

## Scope and unresolved limitations

The theorem requires independent uniform parent choices with replacement. It does not assert results for distinct-parent sampling, general variable-weight attachment, quantitative convergence rates, or logarithmic-scale Gumbel normalization outside the stated positive finite ratio regime. Earlier circuit-output literature may contain an equivalent birth-age statement not located in the inspected sources; the oldest relevant full article could not be accessed.

Self-review: passed. Independent audit: not yet performed.
