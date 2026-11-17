# The complete facet-transversal polynomial and a Poisson deletion window for even cyclic polytopes

## Finding

For integers \(k\ge1\) and \(n\ge2k+1\), let \(P=C(n,2k)\) be the cyclic \(2k\)-polytope whose \(n\) moment-curve vertices are numbered in their natural order. A **facet transversal** is a vertex subset meeting every facet. Write \(H_{n,k}(s)\) for the number of labeled facet transversals having exactly \(s\) vertices, and set \(\binom uv=0\) whenever \(v<0\) or \(v>u\), with \(u\) a nonnegative integer.

The complete transversal-size distribution is

\[
H_{n,k}(0)=0,\qquad
H_{n,k}(s)=\frac ns\sum_{a=0}^{k-1}
 \binom{s+a-1}{a}\binom{s}{n-s-2a}
\quad(1\le s\le n).
\]

Consequently, \(\sum_{s=0}^{n}H_{n,k}(s)z^s\) is the full facet-transversal polynomial, not merely its smallest-degree coefficient. For example, in the four-dimensional nine-vertex case,

\[
\sum_s H_{9,2}(s)z^s=36z^4+99z^5+84z^6+36z^7+9z^8+z^9.
\]

There is also a **sharp random-deletion window**. Fix \(k\) and retain each of the \(n\) vertices independently with probability \(1-q_n\). For the retained set \(T_n\),

\[
\Pr(T_n\text{ meets every facet})\longrightarrow
\begin{cases}
1,&q_n\sqrt n\to0,\\
\displaystyle e^{-c^2}\sum_{j=0}^{k-1}\frac{c^{2j}}{j!},&q_n\sqrt n\to c\in(0,\infty),\\
0,&q_n\sqrt n\to\infty.
\end{cases}
\]

Thus a typical transversal must retain all but order \(\sqrt n\) vertices when the dimension is fixed, whereas the established minimum-cardinality bound permits an optimally chosen transversal with only about half the vertices. The critical limiting law has Poisson parameter \(c^2\).

## Assumptions and scope

Here \(n,k,s\) are integers with \(k\ge1\), \(n\ge2k+1\), and \(0\le s\le n\). The cyclic polytope is the convex hull of \((t_i,t_i^2,\ldots,t_i^{2k})\) for arbitrary strictly increasing real \(t_1<\cdots<t_n\); the statements depend only on combinatorics. The labels are meaningful: transversals are distinct if their labeled vertex sets differ. For the probabilistic statement, \(k\) is fixed as \(n\to\infty\), and \(0\le q_n\le1\) is deterministic. The events refer to facets of the *original* polytope, not facets of the randomly retained convex hull.

## Proof

**1. Translate the facets into matchings.** By Gale's evenness criterion in even dimension, a \(2k\)-subset of the vertices is a facet exactly when its vertices can be paired into \(k\) disjoint consecutive edges of the cyclic adjacency graph on \(\{1,\ldots,n\}\), including the edge \(\{n,1\}\). Indeed, between consecutive omitted indices every selected run has even cardinality; the even number of selected vertices can be paired consecutively. The wraparound run is even because the total selected number is \(2k\). Conversely, pairing selected vertices into cyclic edges makes the number strictly between any two omitted indices even. For the simplex case \(n=2k+1\), a facet omits exactly one vertex and the remaining \(2k\) consecutive cycle vertices admit such a matching; thus the same statement holds.

Let \(T\) be a proposed transversal and let \(U=[n]\setminus T\). It misses some facet exactly when the induced cycle subgraph on \(U\) contains a matching of size \(k\). This is a statement about ordinary matchings, not induced matchings.

**2. Classify all transversals by circular gaps.** If \(s=|T|\ge1\), walk around the cyclic order beginning at a marked vertex of \(T\). Let \(g_1,\ldots,g_s\ge0\) count the omitted vertices between successive retained vertices; then \(\sum_i g_i=n-s\). The induced subgraph on \(U\) is a disjoint union of paths on \(g_i\) vertices, and its maximum matching cardinality is exactly \(\sum_i\lfloor g_i/2\rfloor\). Therefore

\[
T\text{ is a facet transversal}\iff\sum_{i=1}^{s}\lfloor g_i/2\rfloor\le k-1.
\]

Write \(g_i=2a_i+\varepsilon_i\), with \(a_i\ge0\) and \(\varepsilon_i\in\{0,1\}\). If \(a=\sum a_i\), there are \(\binom{s+a-1}{a}\) choices of the \(a_i\), and the number of ones among the \(\varepsilon_i\) must be \(n-s-2a\), yielding \(\binom{s}{n-s-2a}\) possibilities. Summing over \(a=0,\ldots,k-1\) counts valid circular gap sequences with a marked starting vertex. There are \(n\) positions for the mark but each labeled \(s\)-element set is counted exactly \(s\) times, proving the formula. If \(T=\varnothing\), the whole cycle contains \(k\) disjoint edges because \(n\ge2k+1\); hence \(H_{n,k}(0)=0\).

**3. Poisson critical window.** In the deletion model let \(X_i\) indicate that both cyclic neighbors \(i\) and \(i+1\) are deleted, with indices modulo \(n\), and put \(Z_n=\sum_iX_i\). If \(q_n\sqrt n\to c\in(0,\infty)\), then for each fixed integer \(r\ge1\), the factorial moment \(\mathbb E[(Z_n)_r]\) is the sum over ordered distinct \(r\)-tuples of cycle edges. Tuples of pairwise disjoint edges contribute \((n^r+O_r(n^{r-1}))q_n^{2r}\to c^{2r}\). An overlapping edge tuple whose union has \(b<r\) components uses \(r+b\) cycle vertices and has \(O_r(n^b)\) placements, so its contribution is \(O_r(n^b q_n^{r+b})=O_r(n^{(b-r)/2})=o(1)\). Consequently all factorial moments converge to those of \(\mathrm{Poisson}(c^2)\), and \(Z_n\) converges in law to that distribution.

Moreover, \(\Pr(\text{three consecutive vertices are all deleted})\le nq_n^3\to0\). Outside this event, the deleted adjacent pairs are vertex-disjoint, so their number is exactly the induced subgraph's matching number. Therefore, with probability tending to one, \(T_n\) meets all facets exactly when \(Z_n\le k-1\), proving the middle branch.

When \(q_n\sqrt n\to0\), the union bound \(\Pr(Z_n>0)\le nq_n^2\to0\) proves the first branch. When \(q_n\sqrt n\to\infty\), select \(\lfloor n/2\rfloor\) fixed disjoint cycle edges. The number with both endpoints deleted is \(\mathrm{Binomial}(\lfloor n/2\rfloor,q_n^2)\), whose mean tends to infinity; with probability tending to one it exceeds \(k-1\), giving a disjoint \(k\)-matching and disproving the transversal property. This proves the last branch.

## Verification

The standalone Python 3 verifier \(\texttt{verify.py}\) enumerates actual facets **directly using Gale evenness** rather than reusing the cycle-matching rule in the proof. It then enumerates all vertex subsets, checks their facet intersection property, and compares the entire size sequence with the formula for every admissible \(k\) in dimensions with \(3\le n\le12\). For \(3\le n\le8\), an additional independent recursive matching search checks that the facet condition agrees with the induced-subgraph matching obstruction. It also verifies the minimum layer against its already established formula. The verifier reports 295 size-coefficient comparisons and 1,368 additional matching checks. These finite checks do not prove the unbounded formula or the probabilistic limit; those follow from the proofs above.

Run with \(\texttt{python3 verify.py}\), using only the Python standard library.

## Relationship to prior work

Briggs, Dobbins and Lee established Gale's evenness framework and the **minimum** transversal cardinality for even cyclic polytopes (their Proposition 3.6). The previously established exact classification and count of *minimum* transversals is also not claimed anew. Novik and Zheng's broader 2024 preprint studies bounds, cyclic-polytope siblings, and new higher-ratio spheres; its relevant sections likewise do not give a complete size enumerator. Dobbins and Lee's 2026 work motivates the study of facet-transversal ratios but proves a different extremal construction. Neither of these results specifies the complete cardinality-by-cardinality count, the exact all-retention-probability law, or the sharp Poisson deletion window stated here. The \(k=1\) specialization is the familiar vertex-cover enumeration of a cycle and is not claimed as new. The Poisson approximation for rare adjacent successes is classical; the contribution is its exact geometric-facet interpretation and threshold for the entire cyclic-polytope family.

## Limitations

The complete enumerator is for even-dimensional cyclic polytopes, not arbitrary neighborly polytopes or odd dimensions. The probability window assumes fixed \(k\); no uniform result with growing dimension is claimed. The independent finite tests are diagnostic, not exhaustive for all parameters. Historical priority of the full polynomial is provisional: an earlier matching-number enumeration under different terminology could imply the formula. Independent mathematical review has not been performed.

## References

1. J. Briggs, M. G. Dobbins, S. Lee, *Transversals and colorings of simplicial spheres*, arXiv:2111.06560 (first public 2021-11-12), especially §3.3 and Proposition 3.6. https://arxiv.org/html/2111.06560v3
2. M. G. Dobbins, S. Lee, *Polytopes with large transversal ratio*, arXiv:2603.16298 (first public 2026-03-17). https://arxiv.org/abs/2603.16298
3. I. Novik, H. Zheng, *Transversal numbers of simplicial polytopes, spheres, and pure complexes*, arXiv:2407.19693 (first public 2024-07-29), relevant §§1–2, 4. https://sites.math.washington.edu/~novik/publications/transversal-final.pdf
4. Gale's evenness criterion as reproduced in Reference 1, Theorem 3.5.
