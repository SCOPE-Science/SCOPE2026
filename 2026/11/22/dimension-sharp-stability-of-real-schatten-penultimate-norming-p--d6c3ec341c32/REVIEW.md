# Review: dimension-sharp stability of real Schatten norming planes

## Correctness — PASS

All quantifiers are fixed: real two-dimensional subspaces of \(N\)-by-\(N\) matrices, even \(N\ge4\), and \(\varepsilon\le1/(100N)\). For every Hilbert--Schmidt orthogonal basis of squared norm \(N\), normalizing an arbitrary pencil element forces its largest singular value below \(1+\varepsilon\). Its fixed squared singular-value sum then forces every singular value into \([1-3N\varepsilon,1+\varepsilon]\). The polar factors of three normalized pencil elements supply a symmetric-product error; the skew part of an orthogonal cross-product admits a *real exact skew-orthogonal polar correction* while the symmetric defect has norm at most \(0.15\). These steps yield the stated \(3N\varepsilon\) and \(33N\varepsilon\) bounds, and Cauchy--Schwarz gives the directed \(34N\varepsilon\) plane estimate. Equality at zero deficit and the converse are both proved.

The explicit block family has only two singular levels in each pencil member. Their ratio is maximized when the scalar identity component vanishes, giving exactly \(\varepsilon=t/(m-1)\). The chosen Hilbert--Schmidt-normalized member has singular spread \(tm/((m-1)\sqrt{1+t^2/(m-1)})\); every member of any conformal plane has flat singular values. The singular-value Lipschitz inequality gives the displayed lower bound. No compactness, unverified computational optimizer, or unproved classification is required. Standalone standard-library diagnostics passed 42 finite cases; they support but do not replace the analytic argument.

## Originality — PASS, with residual priority risk

The exact **scalar** penultimate real Gelfand width and its parity law are already known from the published-finding corpus finding *A parity law for the penultimate Gelfand number of real Schatten embeddings* (2026-11-17). The scalar value and elementary existence of conformal planes are not new claims. The published published-finding corpus theorem *Exact Grassmannian landscape and endpoint stability for real two-by-two Schatten widths* (2026-11-17) has a full planar profile for **order two**, and is credited. The new claim starts in order four and proves a quantified near-minimizer theorem in every even order, with sharp dimension-dependent excess scale rather than the planar exact profile. Prochno's arXiv:2611.08448 (2026-11-05), Prochno--Strzelecki arXiv:2103.13050, and Hinrichs--Prochno--Vybíral arXiv:2011.06554 analyze width values/bounds, not the specific global correction with its sharp order. The accessible primary full texts and matched database claims were compared on statements rather than title similarity. A differently named older stability theorem could still exist.

## Value — PASS

The first two-parameter test subspace is the smallest nontrivial subspace determining a penultimate Gelfand number. Knowing its optimal scalar width alone does not determine which test planes remain useful after perturbations. The result supplies a constructive basis-level rigidity theorem and a dimension-dependent, **order-optimal** stability modulus; the explicit extremizing family proves that the factor \(N\) cannot be removed, even in arbitrarily small neighborhoods of the optimal family. These facts are useful for quantitative geometry of Schatten embeddings and robustness of structured matrix pencils. They are not a renaming, a finite numerical table, or a trivial corollary of the scalar optimal value. The numerical leading constant \(34\) is explicitly not claimed sharp.

## Closest literature and limits

- Prochno, *Gelfand numbers of Schatten class embeddings in the quasi-Banach range*, arXiv:2611.08448 (2026-11-05).
- *A parity law for the penultimate Gelfand number of real Schatten embeddings*, published-finding corpus (2026-11-17).
- *Exact Grassmannian landscape and endpoint stability for real two-by-two Schatten widths*, published-finding corpus (2026-11-17).
- Prochno--Strzelecki, arXiv:2103.13050; Hinrichs--Prochno--Vybíral, arXiv:2011.06554.

Only real even-order square matrix two-planes and the \(\mathcal S_1\)-to-\(\mathcal S_\infty\) endpoint are treated. The proof is analytic; finite tests are supplemental, and independent mathematical validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
