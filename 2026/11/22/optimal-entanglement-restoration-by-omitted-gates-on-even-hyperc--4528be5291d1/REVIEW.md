# Independent mathematical audit

## correctness

PASS

For the graph-state amplitude matrix, summing the binary cross-cut phases over the odd-side words leaves reduced-state entries 2^(-|even side|) precisely when the difference of the row labels lies in ker(B^T). Ordering those labels by cosets gives identical all-ones blocks, hence a flat nonzero spectrum with multiplicity 2^rank(B), and all claimed entropy orders follow. Over GF(2), A(Q_m)^2=mI by commuting coordinate flips; when n is even the two-layer adjacency maps (u,v) to (w,A(Q_(n-1))w) and every w occurs. Its full rank is half the number of vertices, so its parity cut rank is 2^(n-2). The specified deleted edge is disjoint from the others and occurs exactly once in each square fiber, turning it into P4. A(P4) is invertible (its path has a unique perfect matching), and factoring the Cartesian-product adjacency gives the identity plus a square-zero correction from the even Q_(n-2); this is invertible, including n=2 where Q_0 contributes zero. Since the color classes stay balanced, the cut block gains full rank. Each binary cut entry change has rank at most one, so comparing any partial subset with both the unmodified and fully omitted endpoints gives matching lower and upper bounds of 2^(n-2)+|D|. Comparing an arbitrary omission set just with the baseline gives the global lower bound, not merely a matching-restricted bound. Odd baseline maximality follows from A(Q_n)^2=I. Inspected VERIFY.py and the recorded exact finite run (65,794 subsets), which was not rerun; it checks sampled/exhausted finite cases, while the algebra proves the infinite law.

## originality

PASS

The cut-rank lemma, one-edge perturbation bound and unmodified parity baseline are established. The distinct contribution supported here is the explicit rank-restoring matching on every even cube, which attains the lower bound and gives the exact gain for every subset. The inspected analogous constructions and literature do not give this location-constrained deletion pattern, whether expressed as an entanglement statement or a binary-matrix rank statement.

## value

PASS

The perturbation bound alone leaves open whether the graph even admits that many effective deletions. The explicit uniform choice makes the bound attainable on a natural infinite family using gates actually present, and guarantees the exact spectrum after any partial adoption. This is a sharp ideal graph-state design result; it neither asserts random omissions are beneficial nor claims to optimize a noisy device.

The dated certificate retains the supplied scientific assessment, sources and limitations.
