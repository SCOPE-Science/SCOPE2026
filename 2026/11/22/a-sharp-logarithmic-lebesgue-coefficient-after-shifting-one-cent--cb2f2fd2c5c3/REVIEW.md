# Mathematical review

## Correctness — PASS

The claimed object is the full-degree Lagrange projector on the precisely specified even Chebyshev–Lobatto grid after **one** central node is moved by a fixed fraction of an angular gap. The unperturbed nodal polynomial \((x^2-1)U_{n-1}(x)\), its exact nodal derivatives, and the one-node replacement identities are directly checked. These identities split the Lebesgue sum into a uniformly bounded moved-node term and the remaining nodes. Their two-sided harmonic tails have coefficient \((2/\pi)|\sin(\pi t)(1-\alpha/t)|\) near the changed node, uniformly over compact scaled coordinates. The away-from-center bound uses the classical unperturbed \((2/\pi)\log n+O(1)\) upper bound and an explicit weighted cardinal sum of negligible logarithmic size. This covers **all** maximizing-sequence possibilities, not only numerically sampled points. A strictly decreasing elementary root function proves uniqueness of the norming location and its claimed closed characterization. The standalone reproducibility code checks cardinal identities and finite-scale predictions independently of the infinite proof.

## Originality — PASS, subject to priority risk

The closest source, Wu (arXiv:2606.23409), proves a uniform sufficient small-angular-perturbation condition and constructs a **two-node** near-collision instability example. Neither is the present sharp fixed-fraction **single-node** asymptotic. Austin–Trefethen (arXiv:1612.04018) studies perturbed periodic trigonometric interpolation and provides different bounds. Piazzon–Vianello's small-perturbation norming-set inequalities require a perturbative hypothesis and do not calculate the exact coefficient here. A mathematical-record result on deleting one Lobatto sample changes the dimension and yields linear rather than logarithmic growth; its claim cannot imply the fixed-cardinality relocation theorem. Searches by names, geometric aliases, single-node displacement and asymptotic Lebesgue coefficients did not reveal an equivalent claim. This negative finding is not a proof of universal historical novelty; in particular, older specialized interpolation literature and non-indexed sources remain a risk.

## Value — PASS

The threshold question is motivated directly by the gap between general \(O((n\log n)^{-1})\) sufficient angular stability and specific perturbations at the larger physical mesh scale \(O(n^{-1})\). The result **exactly** quantifies a natural local sensor/node displacement: a fixed fractional change at one central node cannot destroy logarithmic stability, yet incurs a strict sharp logarithmic-coefficient penalty and displaces the worst interpolation location to the opposite side. This is a structural distinction with direct potential relevance to collocation-grid defect tolerance, not an arbitrary tabulated small case. No claim is made for arbitrary perturbations or algorithmic speedups.

## Literature and limitations

The primary text of Wu's paper was compared at its stability theorem, near-collision construction, and discussion of general perturbation inequalities; relevant Austin–Trefethen supplementary mathematical text and the Piazzon–Vianello opening and norming-set result were inspected. Other specialized full texts were not all available for exhaustive priority analysis. The result is restricted to fixed \(0<\alpha<1\), even degrees and a single central change. Computational checks do not certify the infinite quantifier; the proof does.

Self-review: passed. Independent audit: not yet performed.
