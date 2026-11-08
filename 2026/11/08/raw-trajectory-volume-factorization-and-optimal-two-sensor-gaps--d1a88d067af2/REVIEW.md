# Scientific review: raw-trajectory cycle-sampling determinant

## Correctness — PASS

The finding concerns every integer \(N\ge5\), all cutoffs \(1\le r<N/2\), every pair of distinct sensors \(0,d\), and every real spectrally separating evolution \(T\) on the prescribed Fourier band. The displayed formula is reconstructed from: (1) a real orthonormal constant/cosine/sine eigenbasis; (2) exact Vandermonde demixing at both sensors; (3) the codimension-one maximal-minor identity \(\det(B^*R^*RB)=|\det R|^2\det(B^*B)\|R^{-*}w\|^2\); and (4) the Lagrange-interpolation coefficient vector. The rank condition is exactly \(N/\gcd(N,2d)>r\). The five-mode lattice rule follows from strict one-peak monotonicity, and the metric-separation assertion uses a uniform second-derivative bound. Neither an experimental sample nor a search result is used as an infinite proof.

The actual standalone `CHECK.py` generated the result `CHECK_OK raw_volume_cases=801 five_mode_grid_sizes=496 demixed_vs_raw_checks=78`. Its brute minor computations and grid scans are independent checks, not certificates of universal quantifiers. Risks are conventional normalization, numerical sensitivity near singular sensors, and the need for spectral separation; the proof explicitly handles the normalization and singular cases.

## Originality — PASS relative to inspected literature

The closest published record is *Sharp spectral-demixed two-sensor frame bounds on finite cycles*, whose **complete** `RESULT.md` was materially read. It gives exact frame bounds for a blockwise **spectrally demixed** output norm and the Vandermonde invertibility of ordinary time samples. It explicitly excludes untreated time-trajectory noise conditioning. Its theorem does not state the raw Gram determinant, the codimension-one rectangular transport law, or the exhaustive two-candidate raw D-optimal classification. The new proof establishes those claims and proves a strict separation of raw volume and the earlier demixed-condition-number optimal locations for all multiples of six at least \(42\). The result on normalized paths proves a determinant theorem for a distinct one-sensor full-path spectrum, rather than the two-sensor degenerate cycle spectrum.

The graph Paley–Wiener source (arXiv:2609.25472, first posted 2026-09-21) was inspected at abstract and available metadata level, and its emphasis on the lattice and finite-path experiments was noted. The complete preprint was not accessible via available public PDF/HTML routes, and institutional retrieval was unavailable; possible hidden coverage remains a declared risk. A 2024 general dynamical-sampling paper and a 2021 graph local-aggregation paper were checked at abstract level, not certified as absent from their full texts. Searches of the published research index under raw trajectory, D-optimality, cycle, sine product, five-mode, and Vandermonde synonyms did not identify a fully covering result. Nonretrieval does not establish absolute novelty.

## Value — PASS

This is an analytically complete structural law for the untreated information volume, not a sample-size increment or a generic frame-existence restatement. The codimension-one transport identity eliminates nonunitary time-mixing dependence from **sensor placement for every bandwidth**, and the five-mode theorem turns a nonlinear discrete D-optimal search into an exact two-candidate selection for every graph order. The strict disagreement with optimal demixed conditioning exposes a substantive distinction between two natural sampling criteria and prevents substituting one for the other. This has concrete interpretive value for two-vertex graph sensor design even without a broader multi-sensor theorem.

## Scope and remaining risk

The determinant objective does not imply an optimal smallest singular value, raw condition number, or optimal noise mean-square error. Spectral-value collisions and the Nyquist singleton are excluded. Publication priority remains conditional on incomplete access to some relevant primary full texts. No independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
