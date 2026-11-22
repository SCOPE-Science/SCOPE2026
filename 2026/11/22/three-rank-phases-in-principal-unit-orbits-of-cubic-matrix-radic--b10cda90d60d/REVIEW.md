# Scientific review — principal-unit matrix radical orbit trichotomy

## Correctness — PASS

The ring product is \((U,V)(C,D)=(0,UC)\). Hence the left action fixes \(C\) and translates \(D\) by the row-space-constrained \(mr\)-dimensional space \(\{UC\}\). The two-sided action translates by \(\{UC+CV\}\); after normalizing a rank-\(r\) leading matrix, its missing bottom-right square gives dimension \(2mr-r^2\). The corresponding affine coset counts and the ordinary finite-field rank formula imply the exact spectra. Rewriting the finite-field rank factor as \(P_m^2/(P_rP_{m-r}^2)\) proves the parity-sensitive theta law and the uniform two-sided law, with summable endpoint error. A Gaussian subspace-union bound proves full rank for a uniform point. The packaged `VERIFY.py` directly enumerates cosets over \(\mathbb F_2,\mathbb F_3\) at sizes at most two, checks all binary three-by-three leading matrices, and evaluates finite-size distribution distances; the general proof does not depend on finite experiments.

## Originality — PASS relative to inspected evidence

The 2023 Properzi–Van Antwerpen full-text preprint defines and studies \(\lambda\)-orbits and common-divisor graphs but not the two matrix-radical orbit spectra or asymptotic rank trichotomy. Childs (2019) provides a broader class-two brace framework (only its abstract was accessible in this comparison), not a verified enumeration. The full published result *Rank-stratified brace and group centralizers in three-block matrix radicals* deals with brace and group centralizers, commutator fibers and widths of a distinct three-block algebra; it does not entail the two-sided orbit-rank law for the diagonal-constrained cubic matrix radical. Related results on triangular-radical left orbits concern different multiplication and rank profiles. Searches of comparable statements and parameters did not identify a covering full statement, though they cannot prove historical uniqueness. The classical matrix-rank and theta ingredients are not claimed as novel.

## Value — PASS

Uniformly sampling algebra elements, the orbits of a brace's intrinsic action, and double principal-unit orbits are three natural but inequivalent symmetry measures on one canonical matrix radical. An exact all-dimensional classification demonstrates a sharp asymptotic trichotomy: point rank near \(m\), left-orbit rank near \(m/2\) with a discrete-Gaussian fluctuation, and two-sided-orbit rank asymptotically uniform across \(0,\ldots,m\). The continuum law and quantitative total-variation bounds have substantive use in understanding orbit-weighting bias and the geometry of class-two radical actions; the result is not merely a computation for a small dimension.

## Sources, comparison limits, and risks

Full preprint text: S. Properzi and A. Van Antwerpen, *Common divisor graphs for skew braces*, arXiv:2306.12415v1 (2023-06-21), https://arxiv.org/abs/2306.12415; full accessible transcription https://www.researchgate.net/publication/371758274_Common_divisor_graphs_for_skew_braces. Full published result: *Rank-stratified brace and group centralizers in three-block matrix radicals*, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-rank-stratified-brace-and-group-centralizers-in-three-block-matr--65007f7be362/RESULT.md. Abstract-level background: L. Childs, *Bi-skew braces and Hopf Galois structures*, arXiv:1904.08814 (2019-04-18). An unlocated earlier theorem about double actions on class-two matrix radicals remains a residual historical-priority risk; the checked papers do not imply the full rank-law trichotomy. No independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
