# Scientific review: one-nodal quartic chamber census

## Correctness — PASS
The geometric exhaustion starts from nef and big anticanonical class and uses adjunction and Cauchy--Schwarz to restrict all negative curves to five exceptionals, seven strict transforms of ordinary pair-lines, and the unique strict transform of the collinear triple. The complete intersection matrix determines negative definiteness: selected \((-1)\)-curves must be pairwise disjoint, and at most one selected curve may meet the \((-2)\)-curve. The combinatorial generating functions count these configurations without omissions. Exact rational enumeration checks all \(8192\) subsets, and separately evaluates the counting expressions. The Bauer--Schmitz finiteness dichotomy applies because the anticanonical class is big. The computation is an independent consistency check, not a proof of completeness of negative curves.

## Originality — PASS, qualified
The closest earlier work is Bauer--Funke--Neumann (2009), which establishes the general negative-support correspondence and \(393\) chambers for the smooth degree-four case, and Bauer--Schmitz (2012), which establishes the general volume dichotomy and counting algorithms. The new contribution claimed is solely the explicit one-nodal quartic support polynomial and its finite/infinite-volume split \(178/107\). Neither relevant inspected primary text gives this specific one-collinear-triple census. An analogous one-nodal **cubic** geometry has different Picard rank and negative-curve incidence, so it does not cover this quartic invariant. Search coverage cannot rule out every unindexed table or alternate enumeration.

## Mathematical value — PASS
A single collinear triple is the smallest degeneration of a five-point general-position quartic del Pezzo model and creates exactly one effective \((-2)\)-curve. The result quantifies the structural change from the known \(393\)-chamber smooth surface to \(285\) chambers and separates the previously finite smooth-volume phenomenon into \(178\) finite and \(107\) infinite anticanonical slices. The full support polynomial is a natural stable-base-locus invariant and a useful test case for singular anticanonical degenerations. These quantities are not implied by the smooth \(393\) total or the general finite/infinite criterion without doing the geometric and incidence census.

## Risks and scope
The number and volume classification have only received self-review; independent audit has not yet been performed. The theorem is over \(\mathbb C\), and historical priority could be changed by an undiscovered specialist table or equivalent computation. Source dates are the earliest verified arXiv postings, not journal dates. The full computation is reproducible with Python's standard library.

Self-review: passed. Independent audit: not yet performed.
