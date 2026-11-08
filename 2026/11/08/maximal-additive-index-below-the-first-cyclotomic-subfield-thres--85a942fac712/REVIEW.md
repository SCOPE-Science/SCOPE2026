# Scientific review of maximal additive index below the cyclotomic subfield threshold

## Correctness: PASS

For any map, the affine-difference period set is an additive subspace, and it is exactly the largest subspace admissible in the additive-index definition; extension of an additive function on that subspace supplies the needed global linearized map. On a cyclotomic map of index at most the characteristic, the defining scalar subgroup has more than \(p^{n-1}\) elements. The affine period subspace is invariant under those scalars, so it is either zero or the whole field. The latter alternative makes the function affine-additive; a root count on the scalar subgroup forces a single Frobenius monomial. The odd-characteristic index-\(p+1\) example is an invertible two-term linearized map because its coefficient has nonunit norm. These are exact and unconditional arguments, not extrapolations from enumeration. The included checker replays complete finite tests over \(\mathbb F_9\).

## Originality: PASS, with residual historical-priority risk

Bienvenu and Winterhof's *Additive index and Carlitz rank*, arXiv:2604.25414v1, specifically §6.2, concludes only the lower bound \(\operatorname{AddInd}(f)\ge p\) for non-Frobenius maps of multiplicative index at most \(p\), not the maximal \(\operatorname{AddInd}(f)=p^n\). The exact dichotomy and sharp \(p+1\) boundary are not stated there and are not implied by that lower bound when \(n>1\). The earlier work of Işık and Winterhof treats Carlitz rank instead of additive index. Search comparisons of relevant mathematical research records for monomial additive index, low cyclotomic index, and affine periods found no result asserting the same maximal-index conclusion. Reis and Wang's 2022 foundational article was located bibliographically, but a full text was not available through open-access routes; it remains a risk for equivalent prior work.

## Mathematical value: PASS

The 2026 paper explicitly asks how far low multiplicative index forces high additive index, proposing a general index tradeoff and proving only a characteristic-sized lower bound. The exact maximal-index result resolves the whole first cyclotomic-index regime uniformly over all finite extension degrees, and the example at the next index proves its range is sharp. This is a structural separation with a genuine boundary, not a numerical increment. It does not settle higher cyclotomic indices or all instances of the paper's broader conjecture.

## Boundaries and checks

The exact domain is the zero-free-on-nonzero-input cyclotomic mapping class where the customary multiplicative index is defined; constants and maps with additional zeros are not covered by this formulation. The proof includes prime fields and characteristic two. It does not claim the sharpness construction in characteristic two. Finite tests are separate from the algebraic proof. Historical priority depends on the accessible sources stated in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
