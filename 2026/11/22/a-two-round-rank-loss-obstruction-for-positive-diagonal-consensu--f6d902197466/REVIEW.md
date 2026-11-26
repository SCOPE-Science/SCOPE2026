# Independent mathematical audit

## correctness

PASS

The positive diagonal block on the m leaf rows has rank m, including when some spoke weights vanish, so each factor loses at most one dimension on any input subspace. For singular A and B the left null line of A and the right null line of B are obtained by solving at the leaf coordinates. Normalize each hub coordinate to 1 (if it were zero the entire vector would vanish); the pairing is 1+sum_i (b_i/a_i)(e_i/d_i)≥1. Thus the latter line is outside im(A), so B is injective on im(A). If a rank drop occurs, its factor is singular and the resulting product image is inside that factor's image; the next factor cannot drop rank, whether it is singular or invertible. Rank cannot increase under continued left multiplication. Starting from m+1 dimensions and reaching one requires m separated drops, so T≥2m-1. Rank one here means all rows agree because their row sums are one. As an independent exact check of the m=2 witness, the rows of A2 A1 are (1/4,1/4,1/2), (1/2,1/2,0), (5/12,5/12,1/6); applying A3 sends each to (1/3,1/3,1/3). Each factor is admissible with zeros allowed on some spokes. I inspected the frozen verification notes and verify_star.py without executing it. Its 25 finite tests are diagnostics, not the universal argument. The record proves a lower bound on exact consensus, not an all-sizes attaining construction of its own.

## originality

PASS

The distinct result is the unrestricted positive-diagonal star lower bound and the two-factor transversality that enforces it. Three-round average achievability on three vertices is already implied by Hendrickx–Shi–Johansson; their proof in fact supplies a matching upper bound for every star. Neither is credited as a distinct novelty of this record. The inspected unrestricted existence and restricted rank-count results do not imply the new lower bound.

## value

PASS

The admissible factor class is natural in finite-time consensus, and the question concerns the minimum number of rounds, not just finite-time existence. The null-space geometry proves a strict improvement over counting individual singular factors and shows exactly why the intervening rounds are necessary. Together with the already available star construction from the tree recurrence this determines the minimum over the stated unrestricted class. The value is in the universal obstruction, not the rational three-node witness by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
