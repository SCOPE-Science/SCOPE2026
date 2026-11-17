# Scientific review

## Correctness — PASS

The calculation is made for one precisely specified bounded positive operator on complex \(\ell^1\), with fixed \(0<\delta<1\) and \(\alpha\ge1\). The exact binomial column formula includes the terminal \(k=n+1\) coefficient and handles cancellation before applying absolute values. The global Gaussian bound on the first-difference kernel justifies both the summable \(\alpha>1\) zeta limit and the critical harmonic cutoff at \(\alpha=1\); separate outer-region and off-central estimates justify global maximization, and the unique Gaussian peak locations are \(\pm1\). The proof is analytical. `python check.py` passed 87 finite rational/numerical diagnostic assertions. The finite checks are not substitutes for the limiting argument.

## Originality — PASS, with priority risk

Arnold's 2026 preprint introduces the weighted shift and lazy convex-average framework; these components are acknowledged. The complete closely matching *Gaussian sharp constants for lazy positive weighted shifts* result covers only \(0<\alpha<1\); the proof there explicitly requires local integrability of its fractional Gaussian kernel. Its boundary limit does not prove either the new logarithmic constant or the supercritical zeta constant. The published reflexive-space counterpart has \(1<p<\infty\), \(0<\alpha<1/p\), while Abbar–Arnold–Coine address ACB growth and weighted shifts without a corresponding endpoint difference formula. published-finding corpus and public-literature queries for exact equivalents, broader consequences, and possible tables did not identify direct coverage. An older rephrasing in weighted binomial convolution theory remains possible and independent priority checking is required.

## Mathematical value — PASS

The exact boundary is not a numerical curiosity: it is the divergence threshold of the already-motivated singular Gaussian kernel in the operator power regularity problem. The harmonic coefficient at \(\alpha=1\), the zeta coefficient above it, and the localization of extremal columns give a sharp new phase classification for every fixed supercritical exponent. These operators are not absolutely Cesàro bounded for \(\alpha\ge1\), so the result does not resolve the universal positive ACB version of Katznelson–Tzafriri; it delineates its boundary model. The statement is deliberately restricted to this sequence-space family, with no joint critical-window uniformity or exhaustive novelty certificate.

## Closest sources and limitations

L. Arnold, arXiv:2610.00271v1, Example 3.2 and Section 7; A. Abbar, L. Arnold, C. Coine, arXiv:2609.24601v1, Section 3; *Gaussian sharp constants for lazy positive weighted shifts* (2026), complete published RESULT.md; *Sharp power growth and power-difference decay for positive lazy backward shifts on reflexive sequence spaces* (2026), complete published RESULT.md; Katznelson–Tzafriri (1986). Independent mathematical validation and exhaustive priority determination have not occurred.

Self-review: passed. Independent audit: not yet performed.
