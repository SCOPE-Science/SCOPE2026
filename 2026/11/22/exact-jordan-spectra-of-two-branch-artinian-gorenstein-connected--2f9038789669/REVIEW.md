# Mathematical review: exact Jordan spectra of two-branch connected sums

## Correctness — PASS

In the displayed algebra, mixed monomials vanish, the two branch socles are identified, and the regular module has basis consisting of the unit, the proper powers along the two branches, and their common socle. For an element with leading branch degrees \(i,j\), the image dimension of its \(t\)-th multiplication power follows by triangular elimination of the two higher-order branch tails. Before either terminal degree, both surviving tails and the leading combination give rank \(a+b-ti-tj\); at and after a terminal degree the surviving branch gives \(a+1-ti\) or \(b+1-tj\); when both terminate only the scalar socle coefficient matters. At the only possible simultaneous terminal power \(k=a/i=b/j\), cancellation is equivalent to \(u^k+v^k=0\). The rank sequence determines the full Jordan partition by second differences. Counting leading coefficients and free higher terms yields the stated all-field weighted double sum and total mass \(q^{a+b-1}\). The balanced count is exclusive because first-power rank forces both leading degrees to be one. The attached checker independently constructs multiplication matrices and exhaustively tests all elements for thirteen finite configurations; no finite experiment is used as a substitute for the general proof.

## Originality — PASS, with historical priority qualification

The 2010 construction paper by Ananthnarayan–Avramov–Moore establishes connected sums of Gorenstein rings, but not a finite-field Jordan multiplicity census. The 2014 decomposition paper by Ananthnarayan–Celikbas–Laxmi–Yang studies decomposability and algebraic structure, not the distributions of multiplication operators. Iarrobino–McDaniel–Seceleanu (2019) investigates Lefschetz properties and Jordan types of graded connected sums; its quadratic example detects sensitivity to the base field, which is already known, but its inspected results do not state the exact all-parameter finite-field multiplicity polynomial or the higher radical element strata. Altafi–Iarrobino–Macias Marques (2023) surveys generic Jordan-type theory without that exact census. The arithmetic root equation and the complete count for every pair of branch lengths are the new assertions, not connected sums or the Jordan invariant themselves. A general but currently unlocated special-case identity, or a less readily indexed historical census, could cover the formula; these are residual priority risks.

## Value — PASS

Jordan type refines the weak/strong Lefschetz invariants for Artinian Gorenstein algebras. The complete count of each Jordan type for a canonical unbounded two-branch family is a natural exact invariant, rather than an arbitrary finite slice. It distinguishes the effect of all nonlinear radical coefficients and reveals a field-dependent jump in the balanced generic Jordan partition at the solvability of an \(n\)-th root of minus one. The outcome is computable without any field-element enumeration and applies to every prime-power field, even characteristics dividing the branch lengths.

## Closest literature and limitations

- H. Ananthnarayan, L. L. Avramov, W. F. Moore, *Connected sums of Gorenstein local rings*, https://arxiv.org/abs/1005.1304 (first posted 2010-05-07).
- H. Ananthnarayan, E. Celikbas, J. Laxmi, Z. Yang, *Decomposing Gorenstein Rings as Connected Sums*, https://arxiv.org/abs/1406.7600 (first posted 2014-06-30).
- A. Iarrobino, C. McDaniel, A. Seceleanu, *Connected Sums of Graded Artinian Gorenstein Algebras and Lefschetz Properties*, https://arxiv.org/abs/1904.06297 (first posted 2019-04-12; especially Sections 5.1–5.2).
- N. Altafi, A. Iarrobino, P. Macias Marques, *Jordan type of an Artinian algebra, a survey*, https://arxiv.org/abs/2307.00957 (first posted 2023-07-03).

The claim concerns only the specified ring and its regular module; it does not claim a general classification of connected sums. Historical originality is qualified, and no external independent mathematical audit is claimed.

Self-review: passed. Independent audit: not yet performed.
