# Scientific review: three-chord crossing-count tomography

## Correctness (PASS)

The object is a fixed nondegenerate Euclidean triangle. Proper crossing is defined in its open interior, excluding same-edge boundary chords; this qualification is essential because such chords have positive sampling probability. For a chord connecting two distinct sides, the conditional crossing probability is a bivariate polynomial in its independently uniform edge coordinates. Its first moment gives \(q=2e_2^2\); summing its square over the three edge-pair types gives \(\mathbb E[g^2]=(20/9)e_2^3-(4/3)e_3^2\). Every pair of crossing indicators among three chords shares exactly one chord, so total covariance gives the stated variance. Viète's relations and positivity of \(e_3\) prove uniqueness of the recovered side multiset. An exact rational two-chord ambiguity pair proves the sharp minimum of three chords.

A standalone verification script reproduced ten bivariate quadratures, five exact-rational cases and inversions, the nonidentifiability pair, and independent empirical three-chord moment checks (360,000 trials). Simulations are not used as proof. Potential boundaries—degenerate triangles, arbitrary endpoint laws, and scale recovery—are excluded in the theorem.

## Originality (PASS, historical priority provisional)

Acan (arXiv:1501.01489v1, Sections 1–2) studies uniformly paired *distinct* circle points; neither triangular flat-edge atoms in the chord-type partition nor crossing-count inverses are present in the inspected introduction and degree results. Bortolotto–Ramos (DOI:10.1112/mtk.70024, Theorem 1.2) studies endpoint laws on a circle and therefore the invariant circular alternation count, which does not retain same-edge proper-intersection exclusions. Gates (1982, DOI:10.2307/3213487) studies circle chords under an invariant-line model; its accessible abstract does not describe triangle boundary endpoint sampling. Exact-claim and stronger-coverage literature and research-record searches identified no theorem implying both the shape-dependent variance and three-chord inverse.

Residual risks include older unindexed geometric probability literature and unavailable full text of Gates (1982). The absence of a matching search hit is not itself a proof of originality; the assessment rests on the distinctions in sampling models and the explicit new inverse statistic.

## Value (PASS)

The crossing count is a natural observable of a random segment intersection graph and needs no Euclidean distance or angle measurements. The finding establishes exact, nontrivial shape recovery from just its mean and variance for three segments, and proves two segments are inadequate even with their complete crossing-count law. This is a small complete inverse problem with sharp data complexity, not merely a recomputation of the classical probability that two circular chords alternate.

## Limits and sources

Only similarity is identified without perimeter data. No robustness or confidence theory for empirical moments is claimed. The main relevant full-text evidence examined was Acan (2015) and Bortolotto–Ramos (2025); Gates (1982) was available only through its abstract. References and source comparisons are detailed in `RESULT.md` and `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
