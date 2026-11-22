# Scientific review

## Correctness — PASS

The universal optimizer follows by expressing the pulse matrix's Perron root through its trace and fixed determinant. Strict convexity of the trace gives the unique clipped square-root allocation, including both possible boundary optima. The exact example has a positive Metzler generator with positive natural mortality in both stages, a rational exponential obtained from the spectral projectors, and a precise two-policy spectral sign certificate. The budget crossing is unique by monotonicity in the fixed survival product. The released `verify.py` reproduces the algebra and finite comparisons without claiming that experiments prove the universal statements. Critical equality is unclassified.

## Originality — PASS, literature-bounded

The same ecological source is Long, Adjei and Patel, arXiv:2609.10581 (first public September 5, 2026). Its full-text Theorems 5–7 establish resistance fixation and classification by the full-resistance Floquet multiplier, but not optimal splitting of a prescribed log-kill budget. Patel and De Leenheer, arXiv:2310.07616, explicitly hold the survival matrix fixed and vary treatment period. Earlier Friedland/Nussbaum matrix log-convexity and generic Perron optimization are credited as prior; their existence does not by itself state the exact admissible allocation or constructed sharp budget interval. Relevant indexed results on fixed-strength pulse timing, stage-specific season ordering, and environment persistence have different decision variables. The accessible earlier related two-life-stage species-turnover claim concerns community stability, not treatment-dose allocation. Full historical priority remains uncertain, especially given older generic matrix-scaling literature and accessible summaries lacking complete texts.

## Value — PASS

The motivating paper raises practical questions about which stage-specific insecticide effects produce ecological control despite evolution of resistance. A common total logarithmic survival-reduction budget is a natural mathematical measure for combining independent multiplicative kill factors. The finding characterizes **all** feasible budget splits in a two-stage system and identifies an exact open interval of budgets in which equal allocation predicts unbounded population growth while another allocation guarantees extinction. This is a qualitative intervention-policy distinction, not a small parameter tuning or an empirical efficacy claim.

## Closest literature and limitations

- A. D'Ovidio Long, A. Adjei and S. Patel, https://arxiv.org/abs/2609.10581 — exact model and resistance-fixation prior, not fixed-product allocation.
- S. Patel and P. De Leenheer, https://arxiv.org/abs/2310.07616 — spectral criteria and treatment-period optimization at fixed survival matrix.
- S. Friedland, https://doi.org/10.1080/03081088108817381 — general convex spectral functions; possible special-case historical coverage risk.
- R. D. Nussbaum, https://doi.org/10.1016/0024-3795(86)90233-8 — strict matrix spectral log-convexity background.
- The model neglects density dependence, fitness costs, stochastic dynamics, and the empirical relation between dose and survival. The theorem makes no conclusion at neutral Floquet multiplier one.

Self-review: passed. Independent audit: not yet performed.
