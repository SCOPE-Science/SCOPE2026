# Self-review

## Correctness — PASS

The proof is a complete complex Fourier diagonalization with four Galois frequency sectors, including the nonzero trivial frequency for odd-order sign words. Prime-order vanishing is equivalent to equal integer row/column sums; mixed-frequency vanishing plus binary entry constraints forces identical rows or columns. The disjoint weight-divisibility alternatives produce all exact rank and count formulas; no numerical tolerance is used. Exact independent enumeration over all 32,768 length-15 and 2,097,152 length-21 sign words, using polynomial divisibility rather than row-balance logic, matches all formulas at all weights. The infinite-prime assertion is proved structurally rather than inferred from enumeration.

## Originality — PASS, with explicit prior implication boundary

Lam–Leung's vanishing-root theory and Miller's 2024 preprint directly cover the cyclotomic machinery. Miller's Lemma 2(3) **already gives the complete aggregate Bernoulli-circulant singularity probability** at semiprime orders, and therefore the total number singular at every weight by polynomial coefficient comparison; Chen's nonsingularity special cases and Yang's general Fourier-rank identity and weight-wise invertibility criterion are also covered. Those facts are not treated as new. The precise candidate is the six-stratum **complex-rank refinement**, its support-geometric necessary-and-sufficient criteria, and full rank-by-Hamming-weight count table, which are not supplied or implied by an aggregate determinant-zero count without the additional structural analysis of which primitive orbits vanish. The closest accessible full primary text was compared at the theorem and proof level. Historical-priority risk remains for a possible unindexed rank table or the inaccessible Ingleton paper.

## Value — PASS

The exact rank and fixed-weight census answers a natural, complete Fourier question: not merely whether random structured masks are singular, but how many independent convolution measurements survive, for every support weight and every mask. In particular it separates the four nontrivial positive-nullity classes which are merged in a single determinant-zero event and identifies the geometries producing each. Its formulas are directly usable for finite-length rank-controlled mask design, and include all orders given by two distinct odd primes. It makes no unsupported numerical conditioning or broader finite-group claims.

## Limitations

The result is a narrowly scoped structural refinement of established circulant singularity work. An unindexed earlier all-rank classification could eliminate priority. No independent scientific audit was conducted; the provided proof and exact checkers were examined only in the self-review.

Self-review: passed. Independent audit: not yet performed.
