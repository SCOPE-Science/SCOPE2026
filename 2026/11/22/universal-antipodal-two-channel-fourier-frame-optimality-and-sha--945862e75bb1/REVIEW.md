# Scientific review

## Correctness — PASS

All assumptions are quantified: even cyclic order including the doubled-edge two-vertex boundary; arbitrary positive radially decreasing Fourier-energy sequence; every translation; two different modulation channels with fixed total positive power. The unitary-DFT normalization gives the exact frame spectrum. Reflection averaging proves balanced powers weakly improve both extremes. The explicit short-arc and long-arc distance-pair construction gives *strict* upper and lower inequalities for each nonantipodal gap. A reflected antipodal extremal pair proves equal-power uniqueness. Cyclic Laplacian Fourier eigenvalues yield the sharp heat cosh bounds, parity split and nonzero quantitative design margins. Supplementary standalone numerical checks of constructed matrices, spectra, bounds, finite profiles and heat parameters passed 161085 assertions. No finite test is taken as an infinite proof.

## Originality — PASS relative to inspected published evidence

The source arXiv:2605.16139v2 (Section 5.2, full HTML material inspected) gives the general full-translation Gabor frame diagonalization and the finite frame criterion, not the radial spectral two-extreme optimization, power uniqueness or the exact heat-window bound. A distinct public three-tap two-channel result (full RESULT.md inspected) optimizes *frame potential* over tap phases and modulation gaps, not the frame-condition-number extremes for arbitrary radial Fourier energy. The arXiv:2608.04992 totally-positive-window work concerns existence on continuous Gabor lattices, and other retrieved heat-sampling and Poisson-Gabor results use different observation operators/windows. Search comparisons included equivalent formulations (cyclic circular polarization, two translated unimodal sequences), broader coverage (full-translation frame criteria), exact tables (no applicable tabulated design was found), and whether the closest source statements imply this theorem (they do not). A classical unindexed rearrangement lemma could imply the strict two-arc lemma; this remains an explicit priority risk rather than a novelty guarantee.

## Value — PASS

Worst-case frame conditioning and worst-energy amplification are materially different from average frame potential. The universal result simultaneously optimizes both sharp frame bounds over channel positions and powers for *every* strictly radial decreasing Fourier spectrum, giving a robust design rule without tuning to the window. Its graph heat instance provides exact finite-order, parity-sensitive conditioning constants and explicit strict loss margins for all competing designs; these are usable for finite diffusion-based cyclic acquisition and do not follow from the general frame-spectrum identity alone. The domain includes a broad natural class rather than a contrived isolated test case.

## Literature, limits and audit status

Relevant sources: https://arxiv.org/abs/2605.16139 ; https://arxiv.org/abs/2608.04992 ; https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-phase-frequency-design-and-tightness-transition-for-three--9d47ac973e0f . Earlier circle-rearrangement or polarization results may subsume part of the proof, despite the absence of a covering implication in the material inspected. The proof has not been independently audited.

Self-review: passed. Independent audit: not yet performed.
