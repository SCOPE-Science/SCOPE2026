# Scientific review: harmonic positivity of mixed circle Poisson kernels

## Correctness — PASS

The all-frequency moment-ratio proof explicitly treats the ranges below, at, and above the modulation frequency. Strictness is controlled by whether the mixing law is a point mass; the Vandermonde argument converts cofinite positive Fourier support into finite-site strict positive definiteness. The two-rate formula was obtained by direct algebra and checked exactly from the packaged `proof_check.py`. The summability hypothesis ensures a continuous covariance and justifies rearranging the Fourier series. The 79,922 exact-rational checks are not used in place of the infinite proof.

## Originality — PASS (best knowledge)

The closest recoverable companion statement (e14b214a-4013-43a6-a1dd-428a2ff46af4) covers fractional-power Fourier spectra, including the pure exponential case; these are special choices of a positive moment law and do not imply the arbitrary mixing result or the exact two-point reopening identity. The related mixed-Poisson curvature work treats spatial inflections, while the related single-Poisson nonstationary cosine modulation acts on a sum-coordinate rather than a difference-coordinate. Bissiri–Menegatto–Porcu, Emonds–Führ and Kato–Pewsey–Jones had their relevant full-text sections inspected via lawful open sources; they provide spectral foundations, strictness criteria and circular Fourier modeling but not this all-mixture sharp harmonic cutoff. Public full texts of two indexed closest prior findings could not be accessed; classical equivalent moment inequalities and unseen papers remain priority risks. The scientific comparisons and searched identifiers are recorded in `AUDIT.json`.

## Mathematical value — PASS

For a full class of completely monotone, summable Fourier coefficient sequences the positivity cone collapses from infinitely many spectral inequalities to one explicit constraint at the modulation frequency. More significantly, arbitrarily weak mixing changes the critical kernel from finite rank to strictly positive definite on every finite distinct-site configuration, and every restored high-mode coefficient is quantified. A log-convex but non-moment counterexample demonstrates why the special structure is necessary. This is a natural exact covariance-admissibility and spectral-support classification, not a recalculation of an isolated table.

## Limits and sources

The finding assumes positive mixing on \((0,1)\) and \(\int(1-r)^{-1}d\mu<\infty\); it does not establish results for nonsummable mixtures, multidimensional groups, signed mixing laws or general trigonometric modulations. The priority claim remains best-knowledge and there has been no independent mathematical audit.

Primary and relevant literature: https://arxiv.org/abs/1807.08184 (first public 21 July 2018); https://arxiv.org/abs/1002.3017; https://doi.org/10.1007/s11749-021-00790-y; https://dlmf.nist.gov/1.15.E12.

Self-review: passed. Independent audit: not yet performed.
