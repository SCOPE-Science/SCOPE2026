# Self-review

## Correctness — PASS

The normalized star entries are \(\sqrt{w_i/\sum_jw_j}\); differentiating these entries gives an exact absolute Jacobian-row-sum formula. A strictly negative derivative in the sum of the other spoke weights forces their common lower bound. The remaining scalar optimization has an exact eighteen-leaf positivity certificate and a strict nineteen-leaf counter-witness. Critical-point analysis gives the unique heavy-spoke optimizer for every larger star and its positive asymptotic limit. Integration along conductance segments and interior sharpness directions transfer the Jacobian norm to the global two-input Lipschitz coefficient. The standalone numerical and exact-rational checker passed 14,202 counted supplementary checks; finite tests do not replace the analytic quantifiers.

## Originality — PASS with residual priority risk

The directly relevant theorem in Levie–Isufi–Kutyniok (arXiv:1901.10524) bounds graph spectral-filter responses in operator norm as a function of the graph-shift perturbation. Gama–Bruna–Ribeiro (arXiv:1905.04497) gives related first-order graph-shift filter bounds with eigenvector-misalignment parameters. Neither bound supplies the sharp conductance-to-normalized-adjacency maximum-entry modulus, its optimizing conductance profiles, or the integer transition at nineteen leaves. The degree-normalization discussion in Geisler et al. (NeurIPS 2024) assumes upper and lower degree bounds and is not an exact calculation on the unbounded upper-weight star domain. Nearby published graph-heat and star-resolvent results study distinct operators and input norms. Earlier unindexed equivalent sensitivity laws remain a priority risk; the third source was only partially accessible in extracted text.

## Mathematical value — PASS

This is the complete sharp perturbation law for a natural family of symmetric normalized graph-shift matrices under directly controllable absolute edge-weight errors. It identifies an unexpected discrete switch in the extremal network geometry: the uniform lower-bound profile is sharp through eighteen spokes, while a single heavy spoke dominates thereafter. The limiting coefficient remains nonzero even as the number of leaves diverges, providing an exact baseline for stability studies of normalized graph filters rather than another generic upper inequality. The scope is limited to the base normalized adjacency operator on labelled weighted stars; no claim is made for arbitrary graphs or arbitrary spectral filters.

Self-review: passed. Independent audit: not yet performed.
