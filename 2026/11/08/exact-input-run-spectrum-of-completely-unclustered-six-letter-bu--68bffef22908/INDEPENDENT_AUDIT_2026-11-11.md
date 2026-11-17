# Independent mathematical audit

## correctness

PASS

The linear output-unclustered condition means the five neighboring pairs of the six-letter BWT last column are unequal; input runs are cyclic. Every primitive length-six necklace uses t<=6 distinct symbols, and unique increasing relabeling reduces to a surjective t-letter canonical necklace. Independently enumerated all t^6 length-six candidates, retained lexicographically minimal primitive rotations, computed actual sorted-rotation BWT, filtered consecutive output equality, and counted cyclic input boundaries. Complete eight histogram cells (t,r)=(3,4):5,(3,6):1,(4,4):14,(4,5):44,(4,6):20,(5,5):72,(5,6):108,(6,6):120 sum to 384. Each normalized object has exactly C(q,t) increasing lifts, giving all three displayed E_q,r polynomials for every q>=1; the 4-run fraction is 7/(2q^2)+O(q^-3). No finite-q extrapolation is used.

## originality

PASS

The complete input-run enumerator is not implied by the previously stated n=6 minimum, n=8 sharpness count, or all-length existence. Historical novelty is a qualified best-of-knowledge judgment because Kumallagov Appendix A on exactly n=6 was not accessible; no fabricated full-text noncoverage inference is made.

## value

PASS

Counting all primitive necklaces by BOTH BWT maximal fragmentation and original cyclic run count is a natural refined extremal statistic. The eight-cell classification resolves the exceptional length-six boundary uniformly in alphabet size, distinguishes input r=4/5/6, and exposes nontrivial support restrictions and q^-2 rarity beyond the already-known minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
