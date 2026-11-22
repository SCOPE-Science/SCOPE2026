# Exact three-size random greedy adsorption law on the sixteen-vertex Boolean four-cube

## Finding

For the four-dimensional binary hypercube \(Q_4\), a uniform random ordering of its sixteen vertices followed by nearest-neighbor-blocked acceptance produces a maximal independent set \(I\) with exactly the distribution
\[
\Pr(|I|=4)=\frac16,\quad \Pr(|I|=5)=\frac{64}{165},\quad \Pr(|I|=8)=\frac{49}{110}.
\]
There are exactly 24, 16, and 2 labeled maximal independent sets at these three sizes; no other sizes occur. All maximal independent sets of a given size have the same greedy output probability, namely \(1/144\), \(4/165\), and \(49/220\), respectively. The size of the greedy set strictly first-order stochastically dominates that of a maximal independent set chosen uniformly among the total of 42 sets. For the optimal eight-site packing, the respective probabilities are \(49/110\) and \(1/21\), a ratio \(1029/110\). The exact greedy mean is \(1018/165\) versus \(32/7\) for uniform maximal-set sampling.

## Assumptions and scope

The vertices of \(Q_d\) are the binary words of length \(d\); an edge connects words at Hamming distance one. The graph \(Q_4\) is also the nearest-neighbor square torus \(C_4\square C_4\). Each vertex receives a distinct uniformly random arrival rank. An arriving vertex is accepted exactly when none of its neighboring vertices was previously accepted. Rejected vertices are never reconsidered. No continuum or infinite-volume limiting claim is made. The comparison law is uniform among *maximal* independent sets, not among all independent sets and not among optimal sets.

## Proof

**1. Complete finite structural classification.** For any binary subset mask \(m\) of the sixteen labeled vertices, test independence by checking every accepted vertex against all its Hamming-distance-one neighbors. Test maximality by ensuring each unselected vertex has at least one selected neighbor. The exhaustive scan of all \(2^{16}=65536\) masks, implemented in the attached standalone checker, gives precisely 24 maximal independent masks of size four, 16 of size five, and two of size eight. It excludes every other size. The automorphisms \(v\mapsto \pi(v)\oplus t\), where \(\pi\) runs over the 24 coordinate permutations and \(t\) over the 16 translations, form a group of 384 maps preserving edges. Exhaustively applying all 384 maps to one representative of each size class yields the entire class (orbits of sizes 24, 16, and 2). Hence each class is one orbit and all individual greedy output probabilities within it coincide.

**2. Exact random-order recurrence.** If \(S\) is the mask of currently available vertices and \(N[v]\) is the closed neighborhood of \(v\), write \(F_S(z)\) for the generating polynomial of the number of additional accepted vertices. The next vertex among currently available vertices is uniformly selected from \(S\), irrespective of already rejected vertices, by exchangeability of random ranks. Therefore
\[
F_\varnothing(z)=1,\qquad F_S(z)=\frac z{|S|}\sum_{v\in S}F_{S\setminus N[v]}(z)\quad(S\ne\varnothing).
\]
Each argument on the right is a strict subset, making this a terminating exact rational recurrence. Applying it to the full mask returns
\[
F_{V(Q_4)}(z)=\frac16z^4+\frac{64}{165}z^5+\frac{49}{110}z^8.
\]
An independently organized target-set recursion gives the probability of every one of the 42 individual maximal independent sets, then sums them by size to check the same coefficients. Orbit transitivity from Step 1 gives the stated exact individual probabilities.

**3. Stochastic comparison.** For a uniformly selected maximal independent set, the size probabilities are \(24/42=4/7\), \(16/42=8/21\), and \(2/42=1/21\). At the two proper cutoffs \(4\) and \(5\), the greedy lower tails are respectively \(1/6\) and \(61/110\), strictly less than the uniform lower tails \(4/7\) and \(20/21\); at and above 8 both cumulative probabilities are one. This proves first-order stochastic domination with strict inequality at both nontrivial thresholds. The pointwise optimum amplification and expected values follow by exact arithmetic.

**4. Small-dimensional boundary.** Running the same exhaustive classification and rational recurrence on \(Q_2\) gives terminal size two with probability one; on \(Q_3\) the possible sizes are two and four with probabilities \(1/4\) and \(3/4\). Thus dimension four is the first dimension at least two with odd terminal occupancy. Dimension one is explicitly excluded because its terminal size is one.

## Verification

Run `python3 q4_exact_checker.py` using the Python standard library. The checker independently (i) scans every subset of the full labeled sixteen-vertex cube for maximal independence; (ii) performs exact rational recursion over every reachable available-vertex mask; (iii) performs a separate target-specific rational recursion for all maximal independent sets; (iv) enumerates all 384 coordinate/translation automorphisms and certifies their orbits; and (v) checks both strict cumulative inequalities and every individual output probability. It also checks the claimed smaller-dimensional boundary. Every assertion must pass; the program reports exact state counts and the final PASS line. The exhaustive finite checks are the proof certificates for the finite assertions, not empirical samples.

## Relationship to prior work

Random sequential adsorption and greedy maximal independent sets are classical. Pippenger (1989) studies asymptotic occupancy under girth and related graph conditions; those results do not give this complete finite-cube output law, and the full paper was not accessible for comparison. Dhara, van Leeuwaarden, and Mukherjee (first arXiv release 2016-04-13) analyze generalized adsorption on Erdős–Rényi random graphs via limiting jamming densities, not the exact random-order law on a sixteen-site Boolean cube. A recent exact adsorption census for the truncated-octahedral skeleton concerns a different graph and cannot imply the four-cube probabilities or automorphism classes. The present calculation is deliberately finite, and no unrestricted-in-dimension formula is asserted.

## Limitations

The result is restricted to \(Q_4\) with supporting exact checks on \(Q_1,Q_2,Q_3\). The recursive certificate is exhaustive only for these finite dimensions. Larger hypercubes and infinite-lattice jamming are outside the claim. A negative literature search cannot certify historical uniqueness; the 1989 full text and any unindexed finite-volume computations remain residual priority risks. Independent validation has not been performed.

## References

- N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM J. Discrete Math. 2 (1989), 393–401, DOI: https://doi.org/10.1137/0402034 (primary MSC 60K35).
- S. Dhara, J. S. H. van Leeuwaarden, D. Mukherjee, *Generalized Random Sequential Adsorption on Erdős–Rényi Random Graphs*, arXiv:1604.03918, first submitted 2016-04-13, https://arxiv.org/abs/1604.03918.
- P. Bennett and T. Bohman, *A note on the random greedy independent set algorithm*, Random Structures & Algorithms 49 (2016), 479–502, https://doi.org/10.1002/rsa.20667.
