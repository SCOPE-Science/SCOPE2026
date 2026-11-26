# Fixed-point slack, shattering, and the top cycle of involution assignment complexes

## Finding

Let \(\mathcal I_n\) be all involutions of \([n]\), including fixed points. A Boolean query at an ordered cell \((i,j)\in[n]^2\) asks whether \(\pi(i)=j\). Let \(\Delta_n\) be the simplicial complex of VC-shattered supports, with \(\Delta_0=\{\varnothing\}\).

A support is shattered if and only if it consists of \(e\) vertex-disjoint two-cycle queries (one orientation per pair) and \(f\) distinct fixed-point queries disjoint from those pairs, with \(f=0\) or \(2e+f<n\). Its face polynomial and exponential generating function are
\[
\Phi_n(z)=\sum_{\substack{e,f\ge0,\ 2e+f\le n\\ f=0\ \mathrm{or}\ 2e+f<n}}
\frac{n!}{e!f!(n-2e-f)!}z^{e+f},\qquad
\sum_{n\ge0}\Phi_n(z)\frac{t^n}{n!}=e^{zt^2}(e^{(1+z)t}-e^{zt}+1).
\]
For \(n\ge2\), both VC dimension and Littlestone dimension are \(n-1\); for \(n=1\), both are zero.

For \(n\ge2\) the facets leave exactly one uncovered vertex or are loop-free oriented perfect matchings (the latter possible only for even \(n\)). Their attainable cardinalities are \(\lfloor n/2\rfloor,\ldots,n-1\), and the complex is nonpure for \(n\ge4\). The number of facets with \(e\) oriented edges and one uncovered vertex is \(n!/[e!(n-1-2e)!]\) for \(0\le e\le\lfloor(n-1)/2\rfloor\). For even \(n\), add \(n!/(n/2)!\) oriented perfect-matching facets. For \(n\ge3\), the only size-\((n-1)\) faces are the \(n\) ways to omit one diagonal query, and
\[
\widetilde H_{n-2}(\Delta_n;\mathbb Z)\cong\mathbb Z
\]
with generator the oriented boundary of the simplex on all diagonal queries. At \(n=2\), all four singleton queries are shattered and \(\Phi_2(z)=1+4z\).

If a uniform sample of \(m\) distinct ordered cells satisfies \(m/\sqrt n\to c\in[0,\infty)\), the probability of shattering tends to \(e^{-2c^2}\). In particular it tends to one for \(m=o(\sqrt n)\), and tends to zero for \(m/\sqrt n\to\infty\).

## Proof

**Criterion.** The all-positive labeling must describe disjoint cycles of length one or two. Opposite queries on one two-cycle are logically equal, so any support containing both fails to realize opposite answers on them. If a support with a loop query uses all vertices, make one loop negative and all other queries positive; the negative loop vertex is then the only vertex available, so cannot be paired to avoid the loop. Conversely, for any labeling of an admissible support, install the positive cycles. Let \(K\) be the vertices of negative loop queries. Pair the vertices of \(K\) among themselves if \(|K|\) is even; if odd, first pair one with a wholly unqueried vertex, which exists by the criterion. Fix all remaining vertices. Negative two-cycle endpoints were not used in these pairings and are fixed individually, so all negative answers occur as required.

**Enumeration.** For \(e\) pairs, \(f\) singletons and \(r=n-2e-f\) unused vertices, the count of supports is \(n!/(2^e e! f! r!)\) times \(2^e\) orientations. Remove the cases \(r=0, f>0\). In the EGF the unrestricted factor is \(e^{zt^2+(1+z)t}\), from oriented pairs, queried singletons and unused vertices; remove \(e^{zt^2}(e^{zt}-1)\) for the saturated loop cases. In particular, the polynomials for \(n=1,3,4,5\) are respectively \(1\), \(1+9z+3z^2\), \(1+16z+42z^2+4z^3\), and \(1+25z+130z^2+70z^3+5z^4\).

**Dimensions.** Leaving one diagonal unqueried gives a shattered support of size \(n-1\). Any support using at most \(n-1\) vertices has size at most \(n-1\); any allowed saturated support has size \(n/2\le n-1\) when \(n\ge2\). For adaptive shattering, a positive root answer pins a fixed point or a two-cycle, leaving an involution on \(n-1\) or \(n-2\) vertices. Coordinates involving the pinned vertices now have constant values and cannot split a full query subtree. The families on zero and one vertices each contain only one concept and have Littlestone dimension zero. Induction thus bounds the depth of the positive subtree by \(n-2\) for \(n\ge2\), and static shattering yields a complete adaptive tree of depth \(n-1\).

**Facets and top homology.** With two or more unused vertices, adding a diagonal on one of them preserves shattering. With one unused vertex, adding its diagonal would give a forbidden saturated loop support, and adding any edge would reuse a vertex. Saturated admissible supports are loop-free and maximal. The facet counts follow by substituting \(r=1\) or \(r=f=0\) in the enumeration and the size in the \(r=1\) case is \(n-1-e\). For \(n\ge3\), a support of size \(n-1\) cannot be a saturated perfect matching; in the unsaturated case \(2e+f=(n-1)+e\le n-1\), so \(e=0\). The top boundary matrix is the simplex-boundary matrix on the diagonal queries, with possible extra zero rows from other lower faces. Equivalently, orient these \(n\) facets with the boundary signs of the full simplex: each face that omits two diagonals forces the coefficients of its two incident facets in a cycle to agree. Thus the integer kernel is freely generated by their oriented sum, and no higher faces can make it a boundary.

**Sampling.** The probability that all sampled cells are off-diagonal and pairwise disjoint on underlying vertices is, for \(m\le\lfloor n/2\rfloor\),
\[
Q_n(m)=\prod_{j=0}^{m-1}\frac{(n-2j)(n-2j-1)}{n^2-j}.
\]
Such supports are shattered. Any other shattered support contains at least one diagonal, an event of probability at most \(m/n\). For \(m=O(\sqrt n)\), expanding the logarithm uniformly gives \(\log Q_n(m)=-2m(m-1)/n+O(m/n+m^3/n^2)\), which proves the finite-ratio limit. In the supercritical case, couple all sample sizes by an initial segment of a uniform ordering of the board. The shattering event decreases in size, so its limiting upper probability is at most \(e^{-2C^2}\) by comparing to \(\lfloor C\sqrt n\rfloor\) for every fixed \(C>0\); then send \(C\) to infinity.

## Verification and scope

`check_involution_shattering.py` enumerates involutions and checks traces, coefficients and facet counts of ordered supports of size at most \(n\) for \(1\le n\le5\). `CHECK_OUTPUT.txt` records its finite results, including all four singletons for \(n=2\). The proof, not the finite enumeration, establishes the all-order claims. Only ordinary reduced integral homology in top degree is asserted, not lower homology or full homotopy type. The criterion applies to unrestricted involutions and the full ordered query board, not subfamilies with forbidden edges, fixed-point restrictions or parity constraints. Sampling is uniform without replacement.

## Relationship to prior work

Fang, Hamaker and Troyka, [arXiv:2009.00079](https://arxiv.org/abs/2009.00079), study pattern avoidance and the enumeration of involutions; Bucić et al., [arXiv:1906.05908](https://arxiv.org/abs/1906.05908), study perfect matchings and derangement counts in graphs. Johnson and Wickes, [arXiv:2112.01946](https://arxiv.org/abs/2112.01946), use permutation shattering to mean realization of relative orders rather than Boolean traces of individual cells. The Resultary record [*Perfect-matching trace universality and the shattering polynomial of derangements*](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-perfect-matching-trace-universality-and-the-shattering-polynomia--d84d57a040aa/RESULT.md) studies derangements as bipartite assignments, with no diagonal queries or identification of opposite orientations; it has a different partial-matching support criterion and sampling limit \(e^{-c^2}\). The present classification concerns the loop-saturation obstruction specific to involutions. The classical decomposition into fixed points and two-cycles is not an originality claim, nor is the comparison a guarantee of historical priority.
