# Scientific review of the spatial excess-current spectral law

## Correctness — PASS

The proved object is specified explicitly by the boundary-value solution, the published complex mode response, and the spatial integral of squared excess current. The formula for the latter follows by integrating \(\lvert U'\rvert^2\) and using the fixed boundary increment. The factor \(3240\) makes the low-frequency ratio equal to one: the expansion \(J(s)=s^4/180+O(s^8)\) gives the normalization independently of numerical tests. The ratio factorization, strict single maximum of its limiting shape (polynomial \(z^6+30z^4+17z^2-108\)), compactness of maximizing scales, uniform derivative asymptotics, and the nondegenerate-maximizer argument establish the unique eventual optimizer and the two-term cubic law. The extracted ordinary Python checker performs 127 comparisons, including independent numerical integration of the current cost; those tests are not used as an infinite proof.

## Originality — PASS, with bounded priority risk

The direct source [1] supplies the weak-drive mode-response formula and a comparison using a different closed-form dissipation factor; its high-mode conclusions are qualitative or finite-mode numerical, with no sharp \(n^3\) optimum, unique asymptotically maximizing frequency, two-term expansion, or exact evaluation of the explicitly specified spatial-current integral as used in this theorem. The original SSEP large-deviation sources [2,3] concern stationary correlations and time-averaged fluctuation deviations, while [4] gives general thermodynamic decompositions, not this modewise variational limit. Searches of a published research index with the paper title, SSEP harmonic mode ratio, optimization and spectral aliases returned no directly overlapping claim. The accessible own prior claims had no match for this paper or theorem. The direct source's complete accessible HTML main text and relevant appendices were inspected. Some general antecedents were available only as abstracts; discovery cannot exclude an unindexed or differently formulated previous calculation.

## Value — PASS

The problem is motivated by a specific, physically measurable quadratic excess-current cost and the established failure of a common longest-mode response budget for shorter wavelengths. The new theorem quantifies the exact ultraviolet degradation as cubic in mode number, determines the unique limiting optimum frequency as a fixed multiple of the mode eigenvalue, and supplies the next-order coefficient. This is a useful sharp normalization and experimental spectral-resolution diagnostic, not a renaming of the published stationary covariance spectrum or a single computed mode.

## Scope and relationship to literature

The hydrodynamic/large-mode limits must be taken sequentially. Finite lattice ultraviolet scaling, strong modulation, nonharmonic protocols and any nonlinear entropy-production identity are outside the statement. No claim of independent review or publication-priority certification is made. The scientific comparison is based primarily on [1] in full HTML, with [2–4] inspected at the accessible abstract level.

References: [1] arXiv:2610.07964v1; [2] arXiv:cond-mat/0109346; [3] arXiv:2212.11561; [4] arXiv:2412.08432.

Self-review: passed. Independent audit: not yet performed.
