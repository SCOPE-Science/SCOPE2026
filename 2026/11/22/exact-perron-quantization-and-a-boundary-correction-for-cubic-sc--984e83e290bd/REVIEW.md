# Scientific review

## Correctness — PASS

The fully specified cubic Greville basis has an interior substochastic, irreducible, aperiodic collocation block. Exact Cox–de Boor evaluations yield the two non-Toeplitz endpoint rows and the constant tridiagonal interior. Elimination of the boundary unknowns gives the exact scalar tangent equation. Its right-hand side is decreasing and positive on the stated interval, while the left-hand side is increasing; the unique root yields a strictly positive symmetric eigenvector, so the eigenvalue is the simple Perron root. Reproduction of affine functions and the spectral-radius formula identify the operator-norm root limit. The Taylor calculation of the boundary phase verifies the nonzero fifth-order term. The provided checker reproduces each nonstandard collocation identity for 23 degrees with exact fractions and tests the scalar equation and asymptotics. These finite tests corroborate, not establish, the universal theorem.

## Originality — PASS, qualified

The closely relevant Nagler–Kähler 2013 preprint gives iteration estimates without this explicit cubic eigenvalue. Nagler–Cerejeiras–Forster 2014 develops general spectral theory, explicitly noting that the second-largest eigenvalue is unknown. Nagler 2014 studies the general peripheral spectrum; the 2015 thesis proves real and simple interior spectra but does not state this quantization, its boundary phase, or the fifth-order gap coefficient. Searches for cubic Greville collocation, Robin/tangent quantization and spline iteration rates found no governing stronger theorem among the materially inspected sources. A computation buried in other historical spline-collocation literature remains a residual risk; search absence alone does not establish originality.

## Value — PASS

The natural asymptotic contraction factor of an iterated variation-diminishing approximation operator is exactly its largest nontrivial eigenvalue, which the primary work explicitly left undetermined. The boundary-conditioned cosine formula supplies that rate for every mesh size n >= 6 and distinguishes the \(n^{-5}\) boundary effect from the \(n^{-2}\) diffusion and \(n^{-4}\) dispersion coefficients. This is a substantive all-size spectral classification of a motivated open parameter rather than a special-case numerical table.

## Closest primary literature and limitations

- J. Nagler and U. Kähler, arXiv:1312.5546v1, 2013, https://arxiv.org/abs/1312.5546.
- J. Nagler, P. Cerejeiras and B. Forster, arXiv:1402.2403v1, 2014, https://arxiv.org/abs/1402.2403.
- J. Nagler, arXiv:1403.4522v1, 2014, https://arxiv.org/abs/1403.4522.
- J. Nagler, 2015 dissertation, Section 3.2.3, https://d-nb.info/1078405816/34.

Nonuniform knots, spline degrees other than cubic, and the rest of the cubic spectrum are not covered. The asymptotic expansion holds as n tends to infinity; no finite-n error constant is asserted. An undiscovered equivalent quantization formula remains possible.

Self-review: passed. Independent audit: not yet performed.
