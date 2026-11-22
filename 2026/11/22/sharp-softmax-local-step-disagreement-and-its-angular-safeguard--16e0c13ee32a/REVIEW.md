# Review: sharp softmax local-step disagreement and its angular safeguard

## Correctness — PASS
The two local minimizers follow from exact differentiation. The cosine identity is Cauchy--Schwarz with its equality condition; the ternary rational formula, derivative factor, unique optimizer and small-probability constant have analytic proofs in `RESULT.md`. The standalone checker confirms symbolic identities and 34,581 diagnostic statements using exact rational arithmetic where applicable. Tests do not substitute for the quantified proof.

## Originality — PASS, qualified
The motivating source [1] introduces the estimators and pruning; the comparison theorem and sharp ternary extremum are new deductions from those definitions, not established claims of [1]. The closest full-text related paper [2] decomposes multiclass Gauss--Newton curvature without comparing closest-softmax steps. The other inspected paper [3] addresses Taylor convergence radii rather than ratios of local surrogate minimizers. Record and literature searches did not identify a covering theorem. Historical priority may be affected by uncatalogued equivalents, especially an independently derived Cauchy--Schwarz reformulation.

## Value — PASS
The result precisely quantifies how two contemporaneous learning-rate heuristics can differ on low-probability labels, and shows that the source's angular pruning has an exact upper-bound interpretation in the same limiting model. The sharp constrained frontier and 1/12 coefficient are not consequences of merely knowing that two formulas exist.

## Limitations
Only one example, identity logits, logit-gradient direction, and zero-probe limits are treated. Large raw-estimator disagreement is not actual optimization instability; the extreme displayed example is excluded by the source's filter. No claim is made about minibatches or the final learning-rate schedule. Independent validation is outstanding.

## Closest sources
[1] Bauwens--Krivodub--Zhang, arXiv:2611.05191v1 (estimators and pruning); [2] Korbit--Zanon, arXiv:2605.06081 (multiclass curvature); [3] Sao, arXiv:2603.13552v1 (complex Taylor radius).

Self-review: passed. Independent audit: not yet performed.
