# Scientific assessment

## Correctness — PASS

The result is for explicitly defined independent-neighbor reorientation operators on the homogeneous orientation simplex, with no unproved spatial closure assumptions. The proof derives the two tangent Jacobian eigenvalues from complete multinomial coefficients for all seven possible occupied-neighborhood sizes; isolates the random-tie unique positive root by a monotone positive-coefficient transform; and establishes strictly positive zero-noise incumbent-tie growth using a uniform polynomial lower bound. The stability statements follow from the sign of the two-dimensional scalar Jacobian. `verify.py` independently enumerates the full four-state configuration space using exact fractions; results agree at thirty parameter/rule test cases. No numerical computation is substituted for a universal sign proof.

## Originality — PASS, with explicit priority risk

The primary 2026 Dias–Dickman–Rosembach manuscript was examined in the model, mean-field and numerical-results sections. Its particle rule explicitly randomizes ties, whereas its mean-field equation retains an incumbent-specific tie contribution proportional to \(\eta\). The published analysis does not state the sharp homogeneous tie-rule dichotomy, the exact \(\rho_*\) threshold or the vanishing-density incumbent instability. The 2024 predecessor uses an extended 19-site neighborhood and Monte Carlo analysis; a 2026 cubic-lattice majority-vote paper studies a fully occupied geometry. Search comparisons also considered the published *Exact finite-ring spinodal and a five-site barrier in active exclusion mean fields* and *Exact fixed-point entropy gap for majority tie-breaking on a width-three torus*. Neither implies the claim because their operators and tangent spectra are different. Residual risk: an unindexed equivalent annealed majority-stability calculation could exist; accessible literature search is not a uniqueness certificate.

## Value — PASS

A change in the response to a local tie reverses a qualitative stability conclusion: a nonzero-density obstacle to spontaneous homogeneous polarization exists in one physically natural update but disappears completely in the other. This is a motivated modeling distinction precisely because both tie conventions occur in distinct prescriptions in a recently published active-lattice-gas model. Exact polynomial boundaries and a quadratic low-density noise scale make the distinction operational. This is **not** merely a reparametrization, nor a claim that either local mean-field curve is a transition boundary of the full moving-particle model.

## Closest literature and limits

Dias, Dickman and Rosembach (2026), arXiv:2604.22536v2, Sec. II, provides the neighborhood and the differing tie/noise prescriptions; its numerical results focus on spatially structured bands. Rosembach, Dias and Dickman (2024), arXiv:2312.09492, concerns a 19-site simulation model. Kwak, Lee and Kim (2026), DOI:10.1103/6vh3-fx7f, treats fully occupied cubic-lattice majority voting; only its abstract was available for this comparison. The theorem excludes spatial perturbations, excluded-volume transport, global phase selection and marginal nonlinear classification. Publication priority and independent reproducibility have not been externally determined.

Self-review: passed. Independent audit: not yet performed.
