# Scientific review: sharp one-impulse repair of prime-power cubic Gabor chirps

## Correctness
**PASS.** The argument expands the self-ambiguity of the perturbed cubic chirp and separates the original cubic Gauss coefficients into exact zero and nonzero branches. The underlying imprimitive quadratic Gauss sums have magnitude \(p^{(a+t)/2}\) in their nonzero branch, so a positive impulse \(0<\varepsilon\le1\) cannot cancel them for \(p\ge5\). On the zero branch the perturbation equals two unit-circle terms; the sharp smallest modulus follows from the odd-order roots nearest to \(-1\), with an explicit attaining delay/modulation pair. A phase-space Fourier diagonalization of Gabor projector analysis gives all singular values in terms of ambiguity moduli. Finally the unperturbed kernel count follows by summing over \(p\)-adic valuations of translation indices. The proof covers every stated prime and exponent. The included independent finite-sum checker successfully corroborates selected dimensions; it is not substituted for the proof. No full-spark assertion is made.

## Originality
**PASS relative to inspected sources, with residual priority risk.** Li [1, Proposition 5.1] already proves the prime-power cubic chirp's unperturbed ambiguity zeros, so those zeros alone are not a new claim. Li's Theorem 2.1 perturbs a different root-of-unity quadratic phase by an algebraic parameter to get simultaneous full spark and phase retrieval; Li's universal stable construction also uses a different seed. Neither yields this quantitative, real single-site *cubic* repair. Bojarovska and Flinth [2] supply a general nonzero-ambiguity sufficient criterion and lifting framework, not a cubic-specific minimum or nullity. The closest published one-impulse *quadratic* chirp [3] obtains a different phase-space Gauss structure and a different sine scale, so its formula does not imply the prime-power cubic result. Searches for equivalent impulse-corrected Alltop/power-phase laws, for stronger all-dimensional covered variants, and for exact lifting rank tables returned no decisive prior equivalent. Older radar-sequence literature could still contain an equivalent formula; independent priority validation remains open.

## Value
**PASS.** A 2026 prime-power chirp obstruction raises a concrete mathematical question about whether a small, explicit modification can remove all Gabor ambiguity zeros. This theorem gives an elementary one-site remedy for every odd prime power \(p^a\), an exact worst-case all-mode margin (rather than nonvanishing alone), and the exact missing operator dimension before repair. The sharp margin determines the condition number of full matrix inversion for this natural design family, while the nullity shows that a positive perturbation repairs a macroscopic rank defect. The result does not claim global optimization over all windows or superior asymptotic conditioning to competing constructions.

## Closest literature and limitations
[1] D. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614, full primary text, especially Section 5 and Proposition 5.1.

[2] I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800, full primary text and Theorem 2.2.

[3] *Single-impulse quadratic chirps: exact cyclic Gabor tomography spectrum and arithmetic rank obstruction*, published result, identifier `2026/10/11/SCOPE-single-impulse-quadratic-chirps-exact-cyclic-gabor-tomography-sp--03361b3cff9c`; full primary result read.

Only full, noiseless Gabor intensity data and complex-linear lifting are addressed. Publication priority requires independent scrutiny; no global nonlinear inverse stability or full-spark property is asserted.

Self-review: passed. Independent audit: not yet performed.
