# Scientific review: near-maximal boundary triangles of parallelograms

## Correctness — PASS

For a fixed nondegenerate parallelogram, the normalized boundary sampling law is exactly a four-side mixture with masses \(u,v,u,v\). The four exhaustive occupancy probabilities sum to one. Their exact sublevel integrals are derived independently: three distinct sides give the explicitly integrated kernel \(x(1-y)+yz\); an opposite singleton gives the triangular-law tail \(\varepsilon^2\); and an adjacent singleton gives the product tail by the exact density of the separation of two uniforms. These yield the exact formula for every \(0<\varepsilon<1/2\). The positive log-series follows coefficient by coefficient, including cancellation of the cubic term, and yields the strict extremal statement.

The conditional limit rests on an **exact**, not approximate, factorization in the central range: the rescaled two area contributions are uniform on a two-simplex and independent of the middle-side coordinate. The logarithmic coordinate's transformed density converges in \(L^1\), and noncentral configurations carry only \(O(\varepsilon^2)\) probability versus the dominant \(\varepsilon^2\log(1/\varepsilon)\), yielding total-variation convergence. No finite simulation is mistaken for an infinite proof.

The standalone test compares nine parameter/threshold pairs against independent quadrature and checks 1.6 million directly constructed boundary triples for each of three aspect ratios and shears; all tested discrepancies stayed within the declared tolerance. The proof itself supplies quantifiers and boundary restrictions.

## Originality — PASS, provisional priority

The most closely related public full texts inspected concern (i) the **interior-area-uniform** triangle-area distribution and its six-defect conditional shape law for a square, (ii) the **expectation** of convex-hull area for boundary-uniform samples in a parallelogram, and (iii) rectangle-boundary **acute-triangle probabilities**. None of those theorems determines the full high-area distribution under the boundary measure, the exact strict tail ordering for each high threshold, or the three-simplex/log-uniform marked limit. Koroleva–Nikitin's original work analyzes unit-circle samples and differs in both the sampling domain and regularity of maximum configurations. The related older Henze paper specifies interior-uniform points in its accessible abstract and is not treated as a whole-document negative priority certificate.

Historical priority is not exhaustively established: older literature on polygonal-boundary random triangles may use different terminology, and the published-index search is finite. The relevant source inspections, mathematical implication checks, and remaining risks are recorded in `AUDIT.json`.

## Value — PASS

The event probes a natural extremal invariant (inscribed-triangle area) under the canonical arclength distribution on polygonal boundaries. The maximum is achieved along continuous side-base families; their corner endpoints generate logarithmic rare-event enhancement. Formula (1) is exact throughout an interval, not merely a fitted leading term, and supplies a sharp rhombus-versus-thin-parallelogram ordering that is stronger than mean-area extremality. The universal quadratic correction and missing cubic power reveal a cancellation across geometrically distinct side-occupancy configurations. The joint marked law identifies where and how the rare triangles form, including a Dirichlet area budget and a log-uniform position mark. These properties offer precise geometric probability benchmarks beyond elementary expectation calculations.

## Closest literature and limitations

Koroleva and Nikitin, arXiv:1301.1360 (2013), give circle-inscribed polygon extremal laws; Henze, *J. Appl. Probab.* 20 (1983), addresses interior sampling; MathWorld's *Square Triangle Picking* catalogs interior-uniform area distributions. Three publicly available results dated 2026-10-25 and 2026-11-02 separately treat interior-square rare shapes, boundary-parallelogram means, and rectangle-boundary acuteness; their statements and mechanisms were compared, not merely their titles. The new theorem is limited to fixed nondegenerate parallelograms and normalized area thresholds above one quarter of the parallelogram area. General quadrilaterals, simultaneous shape degeneration, and external independent validation remain outside scope.

Self-review: passed. Independent audit: not yet performed.
