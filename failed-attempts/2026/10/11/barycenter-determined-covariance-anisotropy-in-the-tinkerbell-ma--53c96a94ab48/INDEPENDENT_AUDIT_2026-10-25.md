# Independent mathematical audit

## correctness

PASS

For each compactly supported invariant probability µ, ∫x dµ=∫F_1 dµ and ∫y dµ=∫F_2 dµ are valid. Substitution of the displayed quadratic coordinate map gives E[x²−y²]=(1−a)u−bv and 2E[xy]=−cu+(1−d)v. By definitions p=E[x²]−u², r=E[y²]−v², q=E[xy]−uv, the claimed A=p−r and B=2q follow exactly. A real symmetric 2×2 covariance has spectral gap sqrt((p−r)²+4q²), eigenvalues (T±D)/2, and PSD forces T≥D. Equality iff detΣ=0; a zero-variance linear functional forces µ onto an affine line, including a point atom. u=v=0 forces isotropic Σ; complex pseudocovariance is A+iB. The checker in the package merely verifies some rational substitutions; independently recreated general symbolic proof and exact specialization. A full symbolic test and a pure-squaring invariant three-point probability example corroborate the boundaries. No existence, uniqueness or nontrivial sharpness at arbitrary prescribed barycenter follows.

## originality

FAIL

The mathematical content is exactly a two-coordinate specialization of established invariant-moment equations for all compactly supported invariant measures of arbitrary polynomial maps. Korda–Henrion–Mezić (arXiv:1807.08956, §2 eqs.3–6) and Magron–Forets–Henrion (arXiv:1807.00754, p.7) explicitly give ∫F^αdµ=∫x^αdµ for every multiindex α. Choosing α=(1,0),(0,1) on the already published Tinkerbell equations yields both raw second-moment identities verbatim; centering and applying the textbook 2×2 PSD eigenvalue identity yields every other claimed conclusion. This is positive stronger prior implication, not an absence-of-search inference. Exact Tinkerbell-specific typography is not required for coverage. Separate same-object chaos and time-series papers do not independently state these relations, but that does not restore novelty.

## value

FAIL

For this well-known quadratic map, the submission only writes the two degree-one cases of standard invariant-measure moment balance, subtracts mean squares, and applies universally known 2×2 covariance spectral/PSD identities. The centered isotropy is substitution u=v=0, and the “sharp” trace inequality is not shown to be an attainable nontrivial constraint for any prescribed barycenter; equality at the always-present origin point atom is trivial. No new invariant-state existence, exclusion, support restriction beyond rank-one PSD, sharp parameter region, difficult boundary, extremal classification, or empirically nontrivial dynamical prediction is established. A covariance consistency identity is potentially useful for teaching and checking simulations, but this routine algebraic repackaging without a substantive new mathematical constraint does not pass the research-value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
