# The one-induced-edge shattering law for degree-two graphs and its exact path enumerator

## Finding

Let \(G=(V,E)\) be any finite simple graph of maximum degree at most two, and define the Boolean concept family
\[
\mathcal H(G)=\{U\subseteq V:|E(G[U])|=1\}.
\]
The queries are individual vertices, returning whether they belong to \(U\). **Exact support criterion:** a subset \(S\subseteq V\) is shattered if and only if
\[
\boxed{|E(G[S])|\le1\quad\text{and}\quad |E(G[V\setminus S])|\ge1.}\tag{1}
\]
Thus the shattering complex is the intersection of the complex of vertex sets inducing at most one edge with the complements of the sets covering every graph edge. This statement includes disjoint unions of paths, cycles, and isolated vertices; when \(G\) has no edges the concept class is empty and has no shattered support (including the empty support).

For the path \(P_n\), let \(b(S)\in\{0,1\}^n\) indicate a queried coordinate by one. Criterion (1) becomes: \(b(S)\) has at most one consecutive factor `11` and at least one consecutive factor `00`. Write \(\Phi_n(z)=\sum_{S\text{ shattered}}z^{|S|}\). The complete bivariate generating function is
\[
\boxed{\sum_{n\ge0}\Phi_n(z)t^n=A(t,z)-B(t,z),}
\]
where
\[
A(t,z)=\frac{1-t+tz-2t^2z+t^2z^2-t^3z^2}{(1-t-t^2z)^2},\qquad
B(t,z)=\frac{(1+t)(1+tz-t^2z+t^2z^2)}{(1-t^2z)^2}.
\tag{2}
\]
The first coefficients are \(\Phi_0=\Phi_1=0\), \(\Phi_2=1\), \(\Phi_3=1+2z\), \(\Phi_4=1+4z+3z^2\), and \(\Phi_5=1+5z+9z^2+2z^3\). In particular,
\[
\boxed{\operatorname{VCdim}(\mathcal H(P_n))=
\begin{cases}0,&n\le2,\\1,&n=3,\\\lfloor(n+1)/2\rfloor,&n\ge4.\end{cases}}
\tag{3}
\]
At \(n=0,1\) the concept class is empty; we use the nonnegative VC-dimension convention for its empty support system. For each fixed \(k\ge1\) and \(n\ge2k+2\), the exact coefficient stabilizes to the familiar gap-binomial expression
\[
\boxed{[z^k]\Phi_n(z)=\binom{n-k+1}{k}+(k-1)\binom{n-k+1}{k-1}.}\tag{4}
\]
The maximum-degree assumption is a genuine boundary: equation (1) fails for the diamond graph \(K_4\) with one edge removed.

## Assumptions and scope

Graphs are finite, undirected and simple. Vertex queries are Boolean membership tests; every labeling of a fixed support must extend to some selected vertex set inducing **exactly one** edge. Shattering permits a different completion for each labeling. The path is labeled linearly, not cyclically. The variables \(t,z\) respectively mark path length and number of queries. Empty supports count when and only when the concept class is nonempty.

## Proof

**Necessary conditions.** If \(S\) is shattered, the all-positive trace is realized by some \(U\supseteq S\); since \(G[U]\) has exactly one edge, \(G[S]\) has at most one edge. The all-negative trace is realized by some \(U\subseteq V\setminus S\); therefore the complement induces at least one edge.

**Sufficiency under the degree bound.** Assume both conditions, and prescribe a positive subset \(A\subseteq S\). Because \(E(G[A])\subseteq E(G[S])\), either \(A\) induces exactly one edge, in which case choosing \(U=A\) realizes the trace, or \(A\) is independent. In the second case choose any edge \(uv\in E(G[V\setminus S])\). If \(u\) has a neighbor in \(A\), it has **exactly one**: one of its at most two neighbors is \(v\notin A\). Thus \(U=A\cup\{u\}\) induces precisely the one edge joining \(u\) to \(A\). If \(u\) has no neighbor in \(A\) but \(v\) does, use \(U=A\cup\{v\}\). If neither endpoint has a neighbor in \(A\), use \(U=A\cup\{u,v\}\), which induces precisely \(uv\). No completion selects a forbidden queried vertex. Since \(A\) was arbitrary, \(S\) is shattered. This proves (1).

**Exact weighted enumeration.** On \(P_n\), the internal-edge count of \(S\) is the number of adjacent factors `11` in \(b(S)\); the complement-edge count is the number of adjacent factors `00`. Let \(A\) enumerate words with at most one `11` and \(B\) enumerate those with at most one `11` and no `00`, weighting every selected position by \(z\). The desired series is exactly \(A-B\).

For either language use four states ordered \((0,0),(1,0),(0,1),(1,1)\), recording the last bit and whether a factor `11` has already appeared. The row vector of length-one word weights is \(u=(1,z,0,0)\), and the column of accepting continuations is \(\mathbf1\). The unrestricted and no-`00` transition matrices, whose entries include the weight \(z\) for an appended `1`, are
\[
T_A=\begin{pmatrix}1&z&0&0\\1&0&0&z\\0&0&1&z\\0&0&1&0\end{pmatrix},\qquad
T_B=\begin{pmatrix}0&z&0&0\\1&0&0&z\\0&0&0&z\\0&0&1&0\end{pmatrix}.
\]
These matrices allow precisely the indicated transitions. For either matrix \(T\), the generating function is \(1+t\,u(I-tT)^{-1}\mathbf1\), including the unique length-zero word. Direct inversion of the two four-by-four matrices gives precisely (2); their constant terms cancel in \(A-B\). These are formal power-series identities, so (2) counts every support at every length without an asymptotic restriction.

**Sharp dimension.** For any length-\(n\) indicator \(b\), let \(r\) be its count of `11` factors, \(s\) its count of `00` factors, and \(k\) its count of ones. Counting adjacent bit pairs gives the identity
\[
r-s=2k-n+1-b_1-b_n.\]
For a shattered support, \(r\le1\), \(s\ge1\), and \(b_1+b_n\le2\), so \(2k\le n+1\). For \(n=2m\ge4\), the indicator `1100(10)` repeated after its initial four letters exactly \(m-2\) times has length \(2m\), contains \(m\) ones, exactly one `11`, and a `00`. For \(n=2m+1\ge5\), append one `1` to that indicator, obtaining \(m+1\) ones with the same two properties. These witnesses attain the upper bound. At \(n=3\), only the first and last singleton supports are shattered; at \(n=2\), only the empty support is shattered. At \(n\le1\) there are no concepts. This proves (3).

**Stable binomial coefficients.** If \(n\ge2k+2\) and an indicator has \(k\) ones, then its \(n-k\ge k+2\) zeros cannot all be isolated between the at most \(k+1\) zero-runs permitted by the ones; hence a `00` exists automatically. The \(k\)-element supports with no `11` number \(\binom{n-k+1}{k}\). The supports with exactly one `11` consist of one run of two ones and \(k-2\) single ones, separated by at least one zero; compressing the run structure gives exactly \((k-1)\binom{n-k+1}{k-1}\) choices. This establishes (4). For example, \(\Phi_8(z)=1+8z+28z^2+50z^3+30z^4\). Its \(z^3\) coefficient is \(20+30=50\),.

**Sharpness of maximum degree.** Let \(G\) be the diamond \(K_4\) minus edge \(ab\). Its other two vertices \(u,v\) are adjacent and each is adjacent to both \(a,b\). With \(S=\{a,b\}\), the two conditions of (1) hold: \(G[S]\) has no edges and \(G[V\setminus S]\) has edge \(uv\). Yet the trace selecting both \(a,b\) cannot be extended to any set inducing one edge. Adding \(u\) or \(v\) creates at least two edges, while adding neither creates none. Thus (1) is false for this degree-three graph.

## Verification

The standalone Python 3 checker `verify.py` independently enumerates every maximum-degree-two simple graph on at most five vertices (304 graph instances, 8,824 support tests) and compares its true trace-shattering decisions to (1). It then enumerates every binary hypothesis and support for each path of two through twelve vertices (8,188 support tests), compares the support law and the exact polynomial with an independent weighted-state dynamic program, tests the sharp VC formula and the stable binomial coefficients, and separately verifies the diamond counterexample. Run `python3 verify.py`; a successful run prints `SINGLE_INDUCED_EDGE_SHATTERING_PASS`. The finite checks corroborate but do not substitute for the unrestricted proofs above.

## Relationship to prior work

Johnson's *Binary strings of finite VC dimension* (arXiv:2101.06490, publicly posted January 16, 2021; primary MSC 03C45) studies translate/subword families arising from **one** infinite binary sequence. It does not study all words satisfying an exact local induced-edge quota, so its results do not imply (1)--(4). The published no-monochromatic-triple shattering theorem classifies the language avoiding `000` and `111`; this is a distinct constraint from exactly one `11`, with different support indicators and generating function. The exact-transition binary-word theorem fixes the number of adjacent bit *switches* rather than the number of `11` factors, and its endpoint-parallel matroid characterization has different implications. Likewise, the published induced-edge concept theorem on cycles queries **edges** and allows arbitrary vertex subsets, whereas (1) queries **vertices** and restricts induced-edge count to exactly one. The separate graph-structure criterion and path coefficient enumerator are the contributions assessed here; no complete historical priority certification is claimed.

## Limitations

The support criterion is only asserted for maximum degree at most two; the diamond is a counterexample above this threshold, not a classification of all higher-degree graphs. The path series counts coordinate supports, not hypothesis words or Littlestone dimensions. Other exact induced-edge counts, cycles' explicit closed enumerators, and general graph classes are left open. The comparison with unindexed or earlier equivalent literature is incomplete; independent mathematical audit has not been performed.

## References

1. H. R. Johnson, *Binary strings of finite VC dimension*, arXiv:2101.06490v1, first posted 2021-01-16, https://arxiv.org/abs/2101.06490.
2. *VC-dimensions of nondeterministic finite automata for words of equal length*, arXiv:2001.02309v1, first posted 2020-01-07, https://arxiv.org/abs/2001.02309 (automata-as-concepts and words-as-queries, rather than the dual point-query setup here).
3. *A regular shattering complex for binary words with no monochromatic triple*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-regular-shattering-complex-for-binary-words-with-no-monochroma--a86c7bc37664.
4. *Endpoint-parallel shattering matroids of exact-transition binary words*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-endpoint-parallel-shattering-matroids-of-exact-transition-binary--0961bfcd9d1b.
5. *Shattering and a periodic online gap for induced-edge concepts on cycles*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-shattering-and-a-periodic-online-gap-for-induced-edge-concepts-o--13bcb5cc23b0.
