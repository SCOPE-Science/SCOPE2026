# Scientific review

## Correctness — PASS

The source's global-feedback replicator is transformed by \(p=x+z\), \(q=z/p\), and exposure time \(s=\int_0^t(1-p(\tau))\,d\tau\). Direct differentiation produces a logistic equation for \(q\) and an integrating factor for \(1/p\). The resulting scalar function has at most one interior maximum; its exact height gives an exhaustive three-way basin classification. A double first-contact root gives \(1-p\sim K(s_*-s)^2\) and hence the claimed \(t^{-2}\) coefficient. The provided checker verifies derivative and integrating-factor identities and exact rational example. The theorem is limited to strictly interior initial data and positive parameters in its statement.

## Originality — PASS, subject to independent priority assessment

The source paper [1] supplies the model, local equilibrium analysis and numerical phase portraits but not the exact full interior basin boundary or critical universal asymptotic law. The earlier punishment-transition paper [2] uses a distinct game and stochastic evolutionary framework. Searches for exact separatrices, Riccati reductions, and algebraic critical decay did not identify a stronger covering result. Standard integrating-factor and replicator techniques are acknowledged, and the residual risk of an older equivalent unpublished or incompletely indexed global analysis remains.

## Value — PASS

The exact initial-condition boundary partitions *all* strictly interior states for a natural, published three-strategy game and determines whether initially present defectors disappear or ultimately dominate. The knife-edge has a distinct, explicitly quantified \(t^{-2}\) decay law and universal coefficient, refining local linear stability and numerical basin visualizations. The result is not a parameter renaming, arbitrary sampled subcase, or mere computational verification.

## Scope and independence

The theorem concerns deterministic infinite-population frequencies with global feedback only. Its parameters and all admitted boundary cases are explicit. No empirical prediction or finite-population fixation is established. Independent external validation and historical-priority assessment have not occurred.

Self-review: passed. Independent audit: not yet performed.

## Sources

[1] Q. Wang, X. Chen, A. Szolnoki, *Evolutionary dynamics in state-feedback public goods games with peer punishment*, arXiv:2504.16659v1, April 23, 2025, https://arxiv.org/pdf/2504.16659.

[2] A. Hintze, C. Adami, *Punishment in public goods games leads to meta-stable phase transitions and hysteresis*, *Physical Biology* 12 (2015), 046005, https://arxiv.org/pdf/1210.5233.
