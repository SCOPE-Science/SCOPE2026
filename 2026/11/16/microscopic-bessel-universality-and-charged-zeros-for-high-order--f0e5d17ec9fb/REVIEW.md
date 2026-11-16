# Scientific review of microscopic Hermite spectrogram universality

## Correctness — PASS
The main statement has three parts: the two-term \(C^s\) expansion for the exact pure Fock covariance, the \(C^s_{\mathrm{loc}}\) convergence of the associated proper Gaussian fields, and the joint vague limit of their positively and negatively charged zeros. The exact normalized kernel is \(e^{i\omega/n-t/(2n)}L_n(t/n)\). The falling-factorial/Bonferroni inequality gives a uniform \(O(n^{-2})\) series remainder after any fixed number of derivatives; the Bessel differential equation simplifies the first-order coefficient. Gaussian covariance convergence plus uniform high-derivative increment bounds yield tightness. The bounded smooth one-point densities allow the vector Bulinskaya lemma to exclude critical zeros; the inverse function theorem ensures continuity of charged zero measures. Kac--Rice with two independent exponential gradient squares supplies the exact finite-order charges and their equal limit. The standalone checker passed 457 finite assertions, but the infinite and probabilistic claims are supported by the proof, not by those checks.

## Originality — PASS relative to inspected primary evidence
The 2020/2022 Haimi--Koliander--Romero work provides the Hermite covariance and finite-order one-point formulas; the 2026 Abreu--Shirai work studies cross-order zero correlations and averaged fields; the October 2026 Bellourak--Meignen--Polisano--Nahon paper studies fixed-order charged and pair intensities. None of the inspected statements or directly relevant sections provides the simultaneous single-order high-\(n\) microscopic limit \(J_0\), its first magnetic \(n^{-1}\) correction, or convergence of the charged zero point processes. The classical Mehler--Heine and general Gaussian regular-zero machinery are treated as antecedents. The 2016 Canzani--Hanin local-universality paper concerns a distinct random-eigenfunction ensemble on manifolds; it provides an analogy, not an implication for Hermite spectrograms.

The claim is not certified new against every older Landau-level or time-frequency source. A possible equivalent random-wave limit under quantum-Hall terminology remains a specifically identified priority risk. Literature-index absence alone was not treated as novelty proof.

## Value — PASS
The covariance limit alone is a standard special-function degeneration, but the combined theorem identifies the zero-process scaling limit and its persistent topological charges for a natural high-order time-frequency family, not merely a scalar Bessel approximation. The first correction separates the scalar radial effect from magnetic phase geometry and displays the sharp \(n^{-1}\) charge imbalance. These give a mathematically motivated universality law relevant to comparing different Hermite orders and interpreting spectrogram zero patterns. The result makes no claim about finite-\(n\) two-point rates or an optimal detection algorithm.

## Main references and limitations
- Haimi--Koliander--Romero, arXiv:2012.12298v1, especially Sections 1.1 and 5.4.
- Abreu--Shirai, arXiv:2605.17296v1, especially Sections 1, 2 and 4.1--4.4.
- Bellourak--Meignen--Polisano--Nahon, arXiv:2610.13531v1, especially Sections 2.3, 3 and 5.
- Canzani--Hanin, arXiv:1610.09438, as a non-implicating analogy for zero-set local limits.

The theorem is local after scaling, proves no stochastic rate of point-process convergence, and has not been independently audited or publication-priority certified.

Self-review: passed. Independent audit: not yet performed.
