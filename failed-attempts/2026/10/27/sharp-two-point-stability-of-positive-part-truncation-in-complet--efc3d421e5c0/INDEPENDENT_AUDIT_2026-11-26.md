# Independent mathematical audit

## correctness

PASS

The Gram matrix is A=(1+nγ)I−γ11ᵀ. Every segment is split into intervals with constant masks, assigning identically zero coordinates arbitrarily, so its increment quotient is bounded by the largest mask norm. Conversely a small step in any norming direction at an interior orthant point makes the local mask bound attainable. For a mixed mask with blocks of sizes k and ℓ=n−k, separate the within-block zero-sum subspaces and the span of the two normalized block indicators; these are A-orthogonal. On the latter span A has diagonal entries 1+γℓ and 1+γk, off-diagonal −γ√(kℓ), and determinant 1+nγ. Minimizing the input energy over the second coordinate gives squared projection norm (1+γℓ)(1+γk)/(1+nγ). The within-block ratios are at most 1 and the pure masks have norms 0 and 1. Exactly the most balanced k maximize kℓ; the witness has inactive step γk/(1+γk) times its common active step and can be scaled to remain inside the orthant. Scalar contractivity from zero and on each edge gives the one-point inequality, and the two limits follow from the floor formula. The uploaded numerical checker was inspected, not run; no numerical computation or formal certification is needed for this exact proof.

## originality

FAIL

The strongest indexed comparator gives the exact cut-by-cut nonlinear modulus and same-orthant attainment for every positively weighted finite graph with the same norm. On a unit-weight clique, its one rank-one singular value and the scalar integer maximization mechanically give the entire Finding, including its parity and equality statements.

## value

FAIL

The one-point versus two-point distinction is meaningful, but the complete-graph calculation is a routine rank-one specialization of the already indexed exact nonlinear cut theorem. The balanced support restriction and the odd-n correction follow from one scalar product k(n−k); there is no separate unresolved mathematical component to rescue by narrowing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
