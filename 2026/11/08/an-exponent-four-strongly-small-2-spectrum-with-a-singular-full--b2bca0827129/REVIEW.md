# Scientific review: an exponent-four strongly small-2 spectrum

## Correctness — PASS

The complete proof is in `RESULT.md`. Its only special finite input is the explicit six-point reversible set \(D\subset(\mathbb Z/4\mathbb Z)^2\), whose character sum is \(1+(-1)^{u+v}+2\cos(\pi u/2)+2\cos(\pi v/2)\). For all nonzero frequencies this is exactly \(\pm2\), giving a real, nonvanishing, flat Fourier transform of the associated sign. Tensorization gives the real-even signs needed to remove exactly one from each antipodal Fourier pair of local factors. Independent exact Gaussian-integer calculations verify all local Fourier coefficients at the first three levels, but the tensor identity proves the unbounded-level formula. All amplitude and normalization constants were checked: the perturbation is \(a/(2\cdot4^j)\); the two separating expectations are \(0\) and \(a^2/2\); the fourth-moment contribution is \(a^4/16^j\). The summable perturbations yield a finite complex measure dominated by a singular product probability; local antipodal exclusion forces the finite-intersection condition; a polar-decomposition approximation proves convolution absolute continuity for **all** measures with spectrum in \(E\).

## Originality — PASS relative to checked literature

The closest primary source is P. Ohrysko, arXiv:2609.12628, especially its Theorem 1.1 and Sections 2–6. That paper provides the finite-intersection/product-perturbation framework and constructs examples on products of groups of order six and of odd prime order. It neither states nor constructs the pure exponent-four case; its finite blocks contain either an odd-order coordinate or an odd-prime field. The present construction instead uses a real-even flat sign on the sixteen-element order-four square, with no odd-order factor, and verifies the indispensable local cancellation. An isomorphism or quotient from the cited groups cannot supply the same compact exponent-four group. The result does not claim originality of the general framework or of Hadamard difference sets.

The universal positive implication asserted by Lau and Ülger (arXiv:2606.30570) conflicts with Ohrysko's counterexamples; the present proof is self-contained on the decisive finite input and uses none of the asserted implication. Searches for equivalent exponent-four strong small-2 examples, reversible-difference-set constructions, and wider Fourier-support terminology did not uncover direct statement coverage. A published finite-group Fourier census on \((\mathbb Z/4\mathbb Z)^2\) concerns spectral subsets in the tiling sense, not strongly small-2 subsets of the dual of an infinite compact product. An older unindexed or differently named example remains a priority risk.

## Value — PASS

The ambient group is mathematically motivated: the exponent-two Walsh group cannot support nontrivial antipodal-free local spectra because every character is its own negative, while exponent four is the first pure two-primary case that allows opposite characters. The construction resolves existence on this first nontrivial pure two-primary product, including an exact convolution-square norm and full Fourier support of a singular witness. The reversible sixteen-point flat sign is a finite, checkable structural device; its use is not a cosmetic parameter substitution for the odd-prime examples. The claim is intentionally confined to existence and does not classify all small-2 sets or resolve the exponent-two case.

## Sources and residual risk

The relevant main text of Ohrysko's September 11, 2026 preprint (definition, finite-intersection criterion, product perturbation, explicit blocks, limitations) was inspected. Lau–Ülger's June 29, 2026 preprint was inspected for its abstract and opening main claim as contrary context. Published reversible difference-set literature was used only as background, with no dependence on inaccessible assertions. The largest remaining risk is equivalent priority in historical product-measure or reversible-design literature under an unrelated name. The mathematical result has not undergone independent auditing.

Self-review: passed. Independent audit: not yet performed.
