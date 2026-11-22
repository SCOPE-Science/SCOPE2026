# A six-label symplectic exception to skew-forcing matroidality of triangular graphs

## Finding

Let \(T_n=L(K_n)\) be the triangular graph, whose vertices are the \(\binom n2\) unordered pairs of \(\{0,\ldots,n-1\}\), with two distinct pairs adjacent when they intersect. In the *skew zero-forcing* closure \(\operatorname{scl}_{T_n}(S)\), initially fill exactly \(S\), and repeatedly fill the unique unfilled neighbor of any vertex, filled or unfilled, until no such neighbor exists.

**Theorem.** For every integer \(n\ge3\), \(\operatorname{scl}_{T_n}\) satisfies the matroid exchange axiom if and only if \(n\in\{3,4,6\}\). The resulting matroids are, respectively,

\[
\operatorname{SZF}(T_3)\cong U_{1,3},\qquad
\operatorname{SZF}(T_4)\cong P_{2,6}^{*},\qquad
\operatorname{SZF}(T_6)\cong\operatorname{PG}(3,2)^{*},
\]

where \(P_{2,6}\) is the rank-two partition matroid whose three parallel classes each contain two elements. In particular \(\operatorname{SZF}(T_6)\) has rank \(11\) on \(15\) elements and exactly \(840\) bases (minimum skew-forcing sets). The negative assertions have explicit exchange witnesses at \(n=5\) and \(n=7\), and a single double-star construction works for every \(n\ge8\).

## Assumptions and scope

Graphs are finite, simple and undirected; the triangular graph has no loops. For a filled subset \(S\subseteq E(K_n)\), call \(W=E(K_n)\setminus S\) its *unfilled edge graph*. The closure exchange axiom is: if \(x,y\notin S\), \(y\in\operatorname{scl}(S\cup\{x\})\setminus\operatorname{scl}(S)\), then \(x\in\operatorname{scl}(S\cup\{y\})\). A failure of this implication disproves matroidality. All statements concern this closure on the vertices of \(L(K_n)\), **not** the usual cycle matroid of \(K_n\).

For an unordered pair \(f=\{u,v\}\in E(K_n)\), the number of its unfilled neighbors in \(T_n\) is

\[
 d_W(u)+d_W(v)-2\mathbf1_{\{f\in W\}},
\]

where \(d_W\) is degree in the unfilled edge graph. This identity applies whether \(f\) is filled or unfilled, and is used below to verify stalled configurations.

## Proof

**Positive cases.** For \(n=3\), \(T_3=K_3\); the empty set is closed and every nonempty set fills all three vertices, giving \(U_{1,3}\). For \(n=4\), \(T_4\cong K_{2,2,2}\), with the three pairs of nonadjacent vertices corresponding to the three perfect matchings of \(K_4\). Each neighborhood in \(T_4\) is the complement of one such two-element class. These are precisely the three four-element circuits of the dual of the rank-two matroid having those classes as parallel classes. The unique-unfilled-neighbor rule is precisely closure by these circuits. Thus the skew closure equals the dual partition-matroid closure for every subset.

For \(n=6\), take the even-weight subspace \(H=\{v\in\mathbf F_2^6:\sum_i v_i=0\}\), and quotient by the all-one vector \(\mathbf1\in H\). The quotient \(U=H/\langle\mathbf1\rangle\) has dimension \(4\). Its \(15\) nonzero vectors are exactly the distinct classes \(p_{ij}=[e_i+e_j]\), one for each vertex \(\{i,j\}\) of \(T_6\). The dot product on \(H\) has radical precisely \(\langle\mathbf1\rangle\), so descends to a nondegenerate alternating form \(\omega\) on \(U\). For distinct pairs \(ij\) and \(kl\),

\[
 \omega(p_{ij},p_{kl})=1\quad\Longleftrightarrow\quad |\{i,j\}\cap\{k,l\}|=1.
\]

Consequently the open neighborhood of \(ij\) in \(T_6\) is the complement, among the fifteen nonzero projective points, of the hyperplane \(\{p:\omega(p_{ij},p)=0\}\). Nondegeneracy makes these the complete list of the fifteen hyperplanes of \(\operatorname{PG}(3,2)\). Their complements are exactly the cocircuits of that projective matroid, hence exactly the circuits of \(\operatorname{PG}(3,2)^*\). Standard matroid circuit closure fills a point precisely when a circuit has it as its unique unfilled member; iterating these steps gives the full matroid closure. Thus the two closure operators are identical for **every** initial subset. The dual has rank \(15-4=11\). Its bases are complements of bases in the four-dimensional binary projective geometry: counting ordered independent four-tuples \(15\cdot14\cdot12\cdot8\), then dividing by \(4!\), yields \(840\) bases.

**Failure at five labels.** Let \(W=\{04,14,23,24,34\}\), \(S=E(K_5)\setminus W\), \(x=24\), \(y=04\). The degree identity shows \(S\) is stalled: every possible forcing vertex has zero or at least two unfilled neighbors. After filling \(x\), the unfilled edge \(23\) forces \(34\), the unfilled edge \(14\) forces \(04\), and filled edges \(01\) and \(12\) then force \(14\) and \(23\), respectively. Thus \(\operatorname{scl}(S+x)=E(K_5)\). If instead one first fills \(y=04\), filled edge \(01\) forces \(14\) and the remaining triangle \(\{23,24,34\}\) is stalled. Therefore \(y\in\operatorname{scl}(S+x)\setminus\operatorname{scl}(S)\), while \(x\notin\operatorname{scl}(S+y)\), violating exchange.

**Failure at seven labels.** Take \(W=\{01,02,12,34,56\}\), \(S=E(K_7)\setminus W\), \(x=01\), \(y=34\). The original state is stalled. Filling \(x\) allows an unfilled edge \(02\) to force \(12\), the now-filled \(12\) to force \(02\), and filled edges \(03\) and \(05\) to force \(34\) and \(56\), respectively. Hence the entire graph fills. Filling \(y\) instead allows \(56\) to fill, but leaves the triangle \(\{01,02,12\}\) permanently unfilled. This again violates exchange.

**Failure for every \(n\ge8\).** On labels \(0,\ldots,n-1\), take the spanning double-star

\[
 W=\{01,02,03,04\}\cup\{1j:5\le j\le n-1\},\quad x=02,\quad y=01,
\]

and \(S=E(K_n)\setminus W\). Its centers have unfilled degrees \(4\) and \(n-4\ge4\); every other label has unfilled degree one. Every edge of \(K_n\) has at least two unfilled neighbors in \(T_n\) (for white leaf-edges the count is at least two), so \(S\) is stalled. Filling \(x\) leaves label \(2\) incident with no unfilled edge: for every remaining leaf edge \(av\), the filled vertex \(2v\) of \(T_n\) sees exactly that one unfilled neighbor, so all leaf edges can be filled successively; then the central edge \(01\) fills. In contrast, filling \(y=01\) leaves two disjoint stars of sizes three and \(n-5\ge3\), both centered at their original centers. Each remaining white leaf-edge has at least two white neighbors, and every filled edge has zero or at least two; the state remains stalled with \(x\) unfilled. Exchange fails for all \(n\ge8\).

Together, these cases exhaust the range \(n\ge3\).

## Verification

The accompanying standalone `verify.py` uses only Python 3's standard library. It constructs every triangular-graph neighborhood as a bit mask and independently computes the skew closure of **all** \(2^3\), \(2^6\), and \(2^{15}\) subsets for \(n=3,4,6\). These closures are compared, respectively, with the rank-one uniform matroid, dual partition-matroid circuit closure, and an independent binary-rank formula for \(\operatorname{PG}(3,2)^*\). The latter is \(r_{M^*}(S)=|S|-4+r_M(E\setminus S)\); rank in the quotient is calculated using binary Gaussian elimination. It separately tests the exchange-witness sets for \(n=5,7\) and the double-star witnesses for \(8\le n\le14\). The script returns `VERIFY_OK`; these finite calculations corroborate but do not replace the all-order proof.

## Relationship to prior work

Hall, Pfeil and Taylor introduce the systematic terminology *SZF-matroidal graph*, develop matroidal circuit/neighborhood constraints and prove, among other results, a characterization of when ordinary **cycle matroids** \(M(K_n)\) are SZF-realizable by some graph. The object here is different: the skew-zero-forcing closure on the specific line graph \(L(K_n)\). Their Theorem 2.3 supplies the standard matroid circuit-closure characterization used in the positive proof, but does not classify these triangular graphs or identify the six-label dual projective geometry. Cooper and Fickes investigate the skew closure and kernel matroids on trees, cycles and complete bipartite graphs; their analyzed classes do not imply this complete triangular-graph classification. The isomorphism between the fifteen-point symplectic graph and \(T_6\) is an underlying classical geometric fact, not itself asserted as novel.

## Limitations

This theorem concerns all \(n\ge3\) for the simple, unlooped triangular graphs and only the skew color-change rule. The exceptional \(\operatorname{PG}(3,2)^*\) is non-graphic as a matroid, and is not the usual cycle matroid \(M(K_6)\). The standalone checks are finite and not an independent mathematical audit. An unindexed or differently named source might still contain an equivalent characterization; mathematical priority is not independently certified.

## References

1. D. Hall, S. Pfeil and J. Taylor, *Skew Zero Forcing Matroids*, arXiv:2611.15741v1 (first public 2026-11-11). https://arxiv.org/pdf/2611.15741
2. J. Cooper and G. Fickes, *Zero loci of nullvectors and skew zero forcing in graphs and hypergraphs*, arXiv:2303.17419v1 (first public 2023-03-30). https://arxiv.org/pdf/2303.17419
3. L. DeAlba, *Some results on minimum skew zero forcing sets, and skew zero forcing number*, arXiv:1404.1618 (2014). https://arxiv.org/abs/1404.1618
