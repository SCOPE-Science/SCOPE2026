# Independent mathematical audit

## correctness

PASS

The real-space hypotheses and the actual norm agree exactly with equation (24). Appendix A defines Y on c0 by the closed convex hull of Gamma={+/-e1+/-en:n>=2} and D={y in B_c0:y1=0}; (1/2)B_c0 is contained in B_Y contained in B_c0, so the canonical coordinate vectors belong to Y. Taking the dual support function gives max(sum_{n>=2}|xn|,|x1|+max_{n>=2}|xn|). The strong-uniqueness premise is also verified from the source proof: (e1*+2en*)/3 exposes e1+en, with other generators bounded by 2/3, yielding ||z-(e1+en)||<=6(1-<x_n,z>); the signed variants span Y. Lemma 2.3 puts them in every concrete predual, and Fact 2.2 rules out proper nesting. For every nonempty I, deleting coordinates decreases both norm terms and P_I fixes a nonzero vector, hence ||P_I||=1. X_I is the intersection of kernels of the e_n in Y for n outside I, hence weak-star closed. For infinite I omitting 1 the restricted norm is exactly the l1 norm; for infinite I containing 1, a bijection of its infinite tail transports equation (24) isometrically. l1 has nonisometric isometric preduals c0 and c: their dual measures are countable l1, whereas c has extreme points in its unit ball and c0 does not. The continuum multiplicities follow from infinite subsets of a countable tail. Deleting {1,...,k} or {2,...,k+1} removes exactly k coordinates and gives the two codimension-k outcomes. The empty projection is excluded; no infinite-dimensional predual dichotomy is asserted for finite I or for non-coordinate subspaces. No numerical or exhaustive experiment is needed.

## originality

FAIL

The statement is not printed verbatim as an all-coordinate theorem in Appendix A, but its content is a routine implication of that source's stronger explicit data. Equation (24) specifies the norm for every vector and is invariant under every permutation of tail coordinates. The source itself deletes coordinate 1, proves weak-star closedness using e1 in Y, and derives both the l1 restriction and norm-one projection. Repeating the same deletion argument for an arbitrary subset and reindexing the remaining identical tail coordinates proves every proposed branch, without a new structural lemma. The every-finite-codimension corollary merely deletes k rather than one coordinates; the continuum assertion counts choices of an infinite subset. Comparing only Theorem A.1's stated codimension-one conclusion misses the implication of the displayed norm and proof. The actual corpus searches found the same-work entry; that entry is excluded as prior art, and unrelated similarity hits do not establish duplication. Rejection rests on the explicit primary implication, not unsuccessful search or an assertion that the all-coordinate wording had already been published.

## value

FAIL

The ambient example and predual-inheritance problem are mathematically motivated. However, the proposed restriction to canonical coordinate subspaces adds only coordinate deletion, permutation of the identical tail and counting of subsets to the source's explicit norm/codimension-one argument. It supplies no new norm analysis or classification of non-coordinate subspaces, projections, or predual structures. The two isometry types are immediately visible from the singled-out coordinate in equation (24); the finite-codimension and continuum versions introduce no further mechanism. This is a routine reindexing/parameter extension of the source example and does not meet the substantive-value requirement. This judgment concerns that actual implication; it does not require a downstream theorem or paper-sized result, and does not reject natural classifications simply for being narrow or having short proofs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
