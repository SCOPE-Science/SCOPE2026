# Scientific review: exact node-averaged friendship-gap envelope

## Correctness — PASS

The mathematical setting is a fixed finite connected simple nonregular graph; all node degrees are positive. The centered reciprocal-degree neighbor vector \(w=\delta-\mathbf 1\) is nonzero because its inner product with the nonzero centered degree vector \(u\) is the strictly positive edge sum \(\sum_{\{i,j\}\in E}(d_i-d_j)^2/(d_id_j)\). The gap is exactly \(w\cdot a/n\), which makes its standardization the Pearson correlation of \(\delta\) and \(a\). Orthogonal decomposition in the centered Euclidean space yields both sharp extremal values and explicit attaining attributes; a second residual direction gives all intermediate values when the centered space has dimension at least three. The strict inequality at the failure threshold, including the \(s=1\) boundary, follows from the exact lower envelope rather than an approximation. Positive-affine rescaling realizes bounded nonnegative attribute values without changing any correlation or gap sign. The paw certificate is an independent exact rational instance.

The reproduction script checked the algebraic identities on every connected nonregular labeled graph of orders three through five, plus the exact paw invariants. Its finite checks support but do not replace the all-orders proof. No inference about random or empirical network outcomes is made.

## Originality — PASS with residual literature-priority uncertainty

**Closest exact object.** Evtushenko and Kleinberg (arXiv:2110.11821, sections “Each path to 1 goes to infinity in the number of nodes”, “Differentiating between pro- and anti-SGFP graphs”, “Pro-SGFP topologies aren’t common”, and “Finding high SGFP-failing correlations for real networks”) define \(\varrho_G\) abstractly as the infimum of correlations above which negative SGFP gaps are impossible. They prove existence below one and characterize the zero-threshold pro topologies. Their reported \(r_G^{(\mathrm{high})}\), however, is a **finite-margin numerical lower bound**, explicitly not the exact maximum/supremum. Their text does not exhibit the formula \(\varrho_G=\sqrt{1-\operatorname{Corr}(d,\delta)^2}\), a sharp fixed-correlation envelope, or strict boundary witnesses. The present theorem directly evaluates their named open numerical quantity; it does not reassert their graph classification as new.

**Broader theory.** Evtushenko and Kleinberg (arXiv:2406.10423, main sections on attribute-based and singular friendship-paradox extensions) give the sign rule for a **specified** attribute vector in terms of its correlation with \(\delta\). That broader weighted/unweighted framework contains the definitions and the criterion for individual signs but not the constrained optimization that determines exactly which signs are possible at each separately fixed degree–attribute correlation. The new two-vector geometric minimization is required to pass from one correlation rule to a sharp feasible region involving two correlations and an exact topology supremum. Its presence as a potential easy deduction is openly acknowledged and does not imply it has already been explicitly established in the inspected source.

**Other related material.** Jo, Lee and Eom (arXiv:2107.05838) treat model ensembles with correlated neighboring attributes and approximate mean-/median-/fraction-based GFP behaviors. That is a different quantification of the attribute space. Available mathematical-record searches returned only unrelated rank-correlation inequalities, graph degree-distance correlations, and the different friendship-graph metric problem; none states or dominates the fixed-graph SGFP threshold.

**Remaining risk.** The supplementary PDF to arXiv:2110.11821 / Scientific Reports 2023 was not fully readable, and an unindexed proof of the same sharp threshold remains possible. The conclusion is a self-review, not priority certification or independent referee validation.

## Value — PASS

The sharp boundary \(\varrho_G\) was explicitly introduced in the initiating paper to answer how close degree–attribute correlation can be to one while the singular paradox still fails, but its simulation replaces strict failure by a fixed negative-gap cutoff and returns merely a lower bound. Determining the **exact** all-graph threshold without optimization is a directly motivated, natural missing invariant. The full envelope adds information: given an observed degree–attribute correlation, it tells exactly the best and worst normalized singular gaps that topology permits and constructs attaining assignments. The strict endpoint and the paw's exact \(\sqrt{2/27}\) make a concrete mathematical distinction between a supremum and an attainable negative-gap maximum. This is a focused structural resolution rather than a claim to a new grand theory of social networks.

## Scope and limitations

The proof is confined to fixed connected simple undirected graphs with nonconstant degree and vertex attributes. It makes no statistical or empirical prediction and does not treat weighted or directed extensions. The graph's full joint degree/neighborhood structure enters via \(\delta\), not through the degree histogram alone. Literature-priority uncertainty remains where the relevant supplementary material could not be fully inspected.

Self-review: passed. Independent audit: not yet performed.
