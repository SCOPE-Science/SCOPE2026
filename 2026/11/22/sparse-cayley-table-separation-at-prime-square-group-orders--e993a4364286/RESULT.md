# Sparse Cayley-table separation at prime-square group orders

## Finding

Let \(m(n)\) be the minimum number of entries of a group multiplication table that, when the labels may be freely permuted, identifies **some** group of order \(n\) up to isomorphism among all groups of that order. For every prime \(p\), write \(\ell(p+1)\) for the minimum length of an addition chain from \(1\) to \(p+1\). Then

\[
\boxed{\lceil\log_2 p\rceil\le m(p^2)\le\ell(p+1).}
\]

The central statement is stronger: **if \(k\ge1\) and \(p>2^k\), every pattern of at most \(k\) multiplication entries that is realizable in either of the two groups of order \(p^2\) is also realizable in the other.** This is an exact indistinguishability result for arbitrary repeated labels and arbitrary placements of the entries, not merely multiplication chains.

Both bounds coincide for every Mersenne prime \(p=2^s-1\) with \(s\ge2\) and every Fermat prime \(p=2^s+1\) with \(s\ge1\). Consequently \(m(p^2)=\lceil\log_2 p\rceil\) for all such primes. They also coincide at \(p=11,19,23\). In particular,

\[
\boxed{m(25)=m(49)=3,\qquad m(121)=4.}
\]

For all primes \(p\ge11\), at least four entries are necessary, while exactly three suffice at \(p=5,7\). The known smaller cases are \(m(4)=m(9)=2\).

## Assumptions and scope

A partially filled table is a finite collection of constraints \(x_a x_b=x_c\) on named, pairwise distinct elements of a group. The names occurring in the constraints are distinct group elements, even when the same name occurs in several constraints; unused table labels may be assigned afterwards. Two tables of equal order count as the same group type after a simultaneous relabelling of rows, columns and entries. By the elementary classification of groups of prime-square order, the only two types are \(C_{p^2}\) and \(C_p\oplus C_p\).

The statement concerns identification **up to group isomorphism**, not unique completion of a fully labelled Latin square. The chain \(1=a_0<a_1<\cdots<a_h=p+1\) means each \(a_i\) is the sum of two preceding terms; its length is \(h\). No infinitude of Mersenne or Fermat primes is assumed.

## Proof

**1. Encode any sparse pattern linearly.** Suppose \(k\ge1\) cells involve \(t\le3k\) distinct labels. Over \(\mathbb Z\) let \(e_1,\ldots,e_t\) be the free basis. Build the \(k\times t\) integer matrix \(M\) whose row for \(x_a x_b=x_c\) is \(e_a+e_b-e_c\), and let \(L\) be its integer row lattice. Realizations in any abelian group \(G\) are exactly homomorphisms \(\mathbb Z^t/L\to G\) that send the classes of the \(e_i\) to pairwise distinct values.

**2. A universal minor bound.** Every equation row splits as

\[
e_a+e_b-e_c=e_a+(e_b-e_c).
\]

Each unit row \(e_a\) can be viewed as an oriented incidence row \(e_a-e_0\) after adjoining a ground vertex \(0\). Every row \(e_b-e_c\) is also a directed-graph incidence row. Matrices formed from such rows are totally unimodular (expand determinants along a vertex of degree at most one, or use the usual oriented-incidence argument). For any square minor of \(M\), expand multilinearly over the at most \(k\) equation rows; it is a sum of at most \(2^k\) determinants in \(\{-1,0,1\}\). The same is true for every square minor of the matrix obtained by appending any one difference row \(d=e_i-e_j\), since that extra row is already an incidence row. Thus

\[
|\det B|\le 2^k
\]

for **every** square minor \(B\) of either matrix, without restrictions on repeated indices in the original cells.

**3. No hidden prime torsion or accidental congruence.** Assume \(p>2^k\). Every nonzero minor described in Step 2 is then nonzero modulo \(p\), and conversely. Hence the ranks of \(M\) and each augmented matrix \([M;d]\) over \(\mathbb Q\) equal their ranks over \(\mathbb F_p\). If the rational rank of \(M\) is \(r\), a nonzero \(r\times r\) minor is a unit in \(\mathbb Z_{(p)}\); thus \(L\otimes\mathbb Z_{(p)}\) is a direct summand. In particular \((\mathbb Z^t/L)\otimes\mathbb Z/p^2\) is free over \(\mathbb Z/p^2\).

For any \(d=e_i-e_j\), if its class vanishes modulo \(p\), the augmented rank does not increase modulo \(p\), and therefore does not increase over \(\mathbb Q\). Thus \(d\) belongs to the rational row span. Invertibility of the chosen full-rank minor over \(\mathbb Z_{(p)}\) then puts \(d\) in the localized row lattice itself: it vanishes also modulo \(p^2\). Therefore a difference between two distinct labels is either forced to vanish in **both** target groups, or is nonzero modulo \(p\) in the free quotient.

**4. Simultaneous realizability.** Suppose the constraints can be embedded in either group. By Step 3, all \(\binom t2\) pairwise label differences are nonzero modulo \(p\). Choose uniformly a homomorphism from the quotient into \(C_{p^2}\). Each such difference maps to zero with probability exactly \(p^{-2}\), because it has a unit coordinate in a free \(\mathbb Z/p^2\)-module. Choose instead a uniform pair of linear forms into \(\mathbb F_p\), giving a map into \(C_p\oplus C_p\). Each difference likewise vanishes with probability exactly \(p^{-2}\). By the union bound the chance of **any** collision in either experiment is at most

\[
\binom{t}{2}p^{-2}\le\binom{3k}{2}p^{-2}<4^kp^{-2}<1.
\]

The elementary inequality \(\binom{3k}{2}<4^k\) holds for \(k=1,2\), and subsequently by induction. Hence a collision-free realization exists in each group. The remaining \(p^2-t\) unused names extend arbitrarily to bijective table labellings. This proves the asserted \(k\)-entry indistinguishability.

**5. Lower and upper bounds.** If \(k<\lceil\log_2p\rceil\), then \(p>2^k\), so no pattern of \(k\) cells can isolate one isomorphism type. This gives the lower bound; the zero-cell case is immediate. For the upper bound, choose a generator \(x\) of \(C_{p^2}\) and an addition chain for \(p+1\). For each chain step \(a_i=a_j+a_l\) fill the cell \(x^{a_j}x^{a_l}=x^{a_i}\). The distinct integers in the chain lie between \(1\) and \(p+1<p^2\) (also when \(p=2\)), hence name distinct elements in the cyclic group. In \(C_p\oplus C_p\), however, \(x^{p+1}=x\) for every \(x\), contradicting the distinct names \(x\) and \(x^{p+1}\). Thus the filled cells distinguish the cyclic group.

**6. Exact families and examples.** When \(p=2^s-1\) is prime, the doubling chain \(1,2,4,\ldots,2^s=p+1\) has \(s=\lceil\log_2 p\rceil\) steps. When \(p=2^s+1\) is prime, the chain \(1,2,4,\ldots,2^s,2^s+2=p+1\) has \(s+1=\lceil\log_2p\rceil\) steps. The chains \((1,2,3,6,12)\), \((1,2,4,5,10,20)\), and \((1,2,3,6,12,24)\) give equality for \(p=11,19,23\) respectively. The results for \(p=5,7\) follow from the Fermat and Mersenne cases.

## Verification

The proof is uniform in \(p\) and \(k\) and does not infer an infinite theorem from enumeration. The attached standalone C++17 checker enumerates every equality pattern on the \(3k\) input/output slots at \(k=1,2,3\), namely \(5\), \(203\), and \(21147\) set partitions, and verifies that the row rank and all label-difference-augmented ranks agree modulo representative primes below the universal minor threshold and modulo \(17\). It also checks concrete addition chains for primes \(3,5,7,11,17,19,23,31\). To reproduce, compile and run `cayley_sparse_check.cpp` with a C++17 compiler using the command in its first comment; the last line must be `SPARSE_CAYLEY_PRIME_SQUARE_CHECKS_OK`.

The finite checker is corroborative. The proof of the determinant bound uses total unimodularity, and the existence of both injections uses an exact union bound, so no finite search is extrapolated beyond its checked range.

## Relationship to prior work

The motivating public record is OEIS entry A387855, authored October 8, 2025, which defines the smallest filled-cell group-isomorphism identification invariant and lists its values only for orders through \(23\). The subsequent paper of Chernev and Chernev, first posted November 19, 2026, studies the same invariant and gives the small-order list and a general cyclic upper bound, but does not state this uniform prime-square indistinguishability theorem or the exact Mersenne/Fermat families. The newer paper is used only as a claim-level comparison, not as the dated motivating source.

Bean's October 2026 theorem on Latin-square critical sets requires uniqueness of the entire **labelled** Latin-square completion, an intrinsically stronger requirement; it supplies neither a lower bound on the number of cells needed merely to identify the underlying abstract group nor a classification of the two groups of order \(p^2\). General results on partial associativity and approximate group tables likewise concern dense or approximate patterns, not a sparse distinction between finite group isomorphism types.

## Limitations

The sandwich bounds need not coincide for an arbitrary prime, and the result does not claim a full formula for \(m(p^2)\) outside the specified prime families and examples. It does not classify groups of orders other than prime squares. The priority assessment is based on accessible published records and primary literature; an unindexed earlier argument could still exist. Independent mathematical audit has not been performed.

## References

1. Andrey Chernev, *Minimum number of filled Cayley table cells for unique identification of a group of order \(n\)*, OEIS A387855, author record dated 2025-10-08, https://oeis.org/A387855.
2. Andrey M. Chernev and Nikolay A. Chernev, *On the Smallest Cayley Table Fill That Uniquely Determines a Group*, arXiv:2611.25532v1, posted 2026-11-19, https://arxiv.org/html/2611.25532v1.
3. Richard Bean, *A counting proof for the smallest critical set in a Latin square*, arXiv:2610.18199, posted 2026-10-13, https://arxiv.org/abs/2610.18199.
4. W. T. Gowers and J. Long, *Partial associativity and rough approximate groups*, Geometric and Functional Analysis 30 (2020), 1583–1647, https://doi.org/10.1007/s00039-020-00553-1.
