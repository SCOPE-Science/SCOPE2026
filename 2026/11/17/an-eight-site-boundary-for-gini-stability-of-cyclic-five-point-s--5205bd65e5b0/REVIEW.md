# Self-review

## Correctness: PASS
The statement specifies the fixed five-tap periodic operator and complete-pair Gini seminorm for every real signal and every integer \(n\ge5\). Polynomial moments give the stencil exactly; a layer-cake decomposition proves that the seminorm is maximized on cuts. The short complete exact-integer certificate enumerates **every** nontrivial cut in the only four dimensions used for the finite sharp constants — \(L_5=6/7\), \(L_6=101/105\), \(L_7=69/70\), and \(L_8=251/245\) — with no probabilistic or partial extrapolation. For the unrestricted range, the singleton ratio follows from all 5 nonzero coefficients and their 10 mutual pairs; the \(47/35\) upper bound is the triangle inequality for five translated copies. Full proof and reproducible checker are in `RESULT.md` and `check_sg_gini.py`.

## Originality: PASS (historically qualified)
The original Savitzky–Golay article and two subsequent technical treatments establish local polynomial smoothing, coefficient construction, frequency behavior and implementations. The closest indexed record, *Seven points maximize the positivity defect of quadratic Savitzky–Golay smoothing*, concerns loss of positivity and an all-window bound, not Gini variation on periodic samples. In particular, knowing the absolute coefficient sum \(47/35\) does **not** give the small-cycle cut maximization or the sharp size-eight threshold. Searches for pairwise variation, signed cyclic convolution and the exact kernel found no covering primary assertion. One historical equivalence risk remains: related older time-domain studies might contain a reformulation not indexed under Gini or dispersion.

## Mathematical value: PASS
The five-point Savitzky–Golay smoother is a standard local quadratic smoothing filter, but its negative outer weights make claims of uniform dispersion reduction nontrivial. The sharp eight-vertex cutoff resolves exactly when smoothing is automatically Gini-nonexpansive on short periodic records; the all-size impulse witness and sharp uniform \(47/35\) amplification envelope quantify the price of polynomial reproduction. This is a natural complete stability classification, not an arbitrary subset computation or merely a rederivation of known coefficients.

## Boundaries and residual priority risk
The exact coefficients are supplied only through eight sites; all larger sites have a proven expansion witness and sharp family-wide envelope, not known exact per-site norms. Periodic wraparound and equal sample masses are essential. The result is not externally or independently validated.

Self-review: passed. Independent audit: not yet performed.
