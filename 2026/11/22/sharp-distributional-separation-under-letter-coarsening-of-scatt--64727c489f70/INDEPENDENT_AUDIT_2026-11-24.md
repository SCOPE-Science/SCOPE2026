# Independent mathematical audit

## correctness

PASS

For every family of indexed embeddings, the joint indicator expectation is either zero on a letter conflict or q^(−union size) by independent uniform letters. Coarsening can only remove conflicts. This proves coefficientwise comparison of the generating polynomials expanded in t−1 and also raw integer-moment comparison, with equal means. If m≤n<m+d, ranks sharing a host site differ by at most n−m<d; coarsening cannot alter any family's compatibility, so the full polynomials, hence laws, agree. If n<m the laws are both zero counts. At length m+d the explicit pair of embeddings uses one shared site at ranks i,j realizing a shortest merge, all other shared sites at equal ranks, and d private sites on each side of the conflict. This pair gives strict PGF inequality at t>1 and, by repeating a member, strict comparison for every integer order r≥2. The witness persists with extra sites; equal means give the first variance separation as well. Every nonconstant pattern has an unequal adjacent pair, and a repeated-endpoints-only pattern shows sharpness of the uniform distinct-pattern threshold 2m−1 when q≥m. For the second moments the constant case has three site types, giving the multinomial, while equal-rank overlap in the injective case makes each of k+1 gaps an interleaving of equal-sized private runs, yielding the central-binomial generating factor. Independently enumerated the worked q=4 example using a prefix dynamic program on host words: equal laws for n=4,5,6 and exact second-moment gap 1/8192 at n=7 (python3 /workspace/branches/review_replay.py 5). Inspected the frozen script and recorded output, but did not execute the script.

## originality

PASS

The supported distinct content is the all-length coarsening order together with the exact first full-law and variance separation length, and the resulting sharp extremizer cutoffs. Overlap-based moment computation is existing hidden-word machinery; an earlier exact binary formula is recovered in one subcase. The evidence does not support calling the general overlap method, or every closed-form second-moment specialization, new.

## value

PASS

The equality partition of the pattern is a natural coarsening parameter for an indexed count whose mean cannot distinguish patterns. The smallest newly merged rank distance governs exactly when the entire law and the variance begin to detect the coarsening. That sharp cutoff provides a usable comparison even before evaluating any histogram, and explains the sharp ranges of uniqueness for the canonical maximal and minimal patterns. The conclusion is stronger than a known variance calculation at a single alphabet or length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
