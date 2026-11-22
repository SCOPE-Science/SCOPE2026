# Self-review of the logarithmic stable-clock comparison

## Correctness — PASS

The new claim is a one-time marginal statement for two independent standardized stable/inverse-stable compositions with strict parameters \(0<\alpha,\beta<1\) and \(t>0\). Self-similarity reduces the two marginal laws to different products of a positive stable and an inverse-stable variable. Their complex moments have a common, nonempty strip around zero, and the gamma reflection identity gives the ratio of the log-characteristic functions as a quotient of logistic characteristic functions. The nonstandard step is the **global positivity** of the proposed four-term Lévy density; this is proved by strict convexity of a reciprocal-exponential function in its logarithmic scale argument, not by finite sampling. Near-zero and infinity estimates verify the Lévy measure integrability requirements. Characteristic-function uniqueness then yields an independent symmetric-noise factor and Jensen gives the logarithmic convex ordering. Differentiation gives both the equal log means and strict positive variance gap. The supplied independent numerical checker reproduced 750 finite tests. No process-level or raw-clock convex order is inferred.

## Originality — PASS on examined evidence

Tathe–Ghosh (arXiv:2611.16676v1), Definition 3.2, defines the reversed subordinator/inverse-subordinator time change but does not compare the two marginal logarithms; the paper then primarily studies one composition. Kataria–Vellaisamy (arXiv:1608.06564) and Gupta–Kumar (arXiv:2108.09170) derive product and inverse-subordinator densities and Mellin expressions. Those established identities are used as inputs; they do not establish positivity of the ratio of the two **different** composition laws as a characteristic function, still less its symmetric infinitely divisible factor or convex ordering. Simon (arXiv:1310.1888v2, Theorems A–C) proves convex orders between different inverse-stable parameters, not between the two compositions at fixed indices. Searches for equivalent or dominating published results found nearby theorems about different stochastic orders and product distributions, without establishing the reversed-composition result. Absence of an exact match is not a proof of universal priority; the residual risk is an unnoticed general factorization/order theorem in the probability literature.

## Value — PASS

Subordinators and inverse subordinators are distinct and commonly composable time changes, and changing composition order is a natural modeling decision. Both orders have **identical time-homogeneity** and equal expected logarithmic time, so scaling alone does not reveal a direction of variability. A strict ordering for **every convex loss on log time** is substantially stronger than an isolated moment or tail comparison. The proof gives an explicit positive Lévy measure for the additional noise, allowing both qualitative and quantitative comparisons. The result is not a rephrased classical density or a tiny numerical improvement. Its importance is limited to independent untempered stable clocks at fixed observation time; no downstream process theorem is claimed.

## Closest literature and limitations

- K. Tathe and S. Ghosh, *Time-changed Compound Poisson Process* (2026), arXiv:2611.16676v1, Section 3, Definitions 3.1–3.2.
- K. K. Kataria and P. Vellaisamy, *On Densities of the Product, Quotient and Power of Independent Subordinators* (2016/2018), arXiv:1608.06564, Mellin and inverse-stable product sections.
- N. Gupta and A. Kumar, *Densities of Inverse Tempered Stable Subordinators and Related Processes With Mellin Transforrm* (2021), arXiv:2108.09170v1, Sections 2–3.
- T. Simon, *Comparing Fréchet and positive stable laws* (2014), arXiv:1310.1888v2, Theorems A–C.

The comparison has not been independently audited or checked against every historical source. The paper giving the motivating two-order definition assumes finite moments in parts of its analysis, whereas the stable subordinator in this theorem has infinite mean: the new proof is self-contained and does not import that paper's moment theorems. Numerical tests are diagnostic only and are not used to establish the global result.

Self-review: passed. Independent audit: not yet performed.
