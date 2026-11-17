# Parity-controlled diameters and ternary outer shells of Marion central polytopes

## Finding
For every integer \(N\ge3\), consider the Euclidean polytope
\[
Q_N=\left\{x\in\mathbb R^N:\ \sum_{i=1}^{N}x_i=1,\quad x_i\le 2x_j\text{ for all }i\ne j\right\}.
\]
This is the regular-simplex realization of the central polytope produced by trisecting every edge of a simplex and retaining the central halfspaces, as defined by Kazakov [1]. Its intrinsic dimension is \(N-1\); distances are the ordinary ambient Euclidean distances. Write \(m=\lfloor N/2\rfloor\). Its **exact Euclidean diameter** is
\[
\operatorname{diam}(Q_N)^2=
\begin{cases}
\dfrac4{9N},&N\text{ even},\\[4pt]
\dfrac{9N\,m(m+1)}{(N+m)^2(N+m+1)^2},&N\text{ odd}.
\end{cases}
\]
For each nonempty proper subset \(S\subset[N]\), define \(v_S\) by
\[
(v_S)_i=\frac{1+\mathbf 1_{\{i\in S\}}}{N+|S|}.
\]
The **only** diametral pairs are \(\{v_S,v_{S^c}\}\) with \(|S|\in\{\lfloor N/2\rfloor,\lceil N/2\rceil\}\). The number of *unordered* diametral pairs equals
\[
\begin{cases}
\tfrac12\binom N{N/2},&N\text{ even},\\
\binom N{(N-1)/2},&N\text{ odd}.
\end{cases}
\]

The unique smallest enclosing Euclidean ball has center \(u=N^{-1}(1,\ldots,1)\). Put \(s_*=\lfloor(N+1)/3\rfloor\). Its squared radius is
\[
R_N^2=\frac{s_*(N-s_*)}{N(N+s_*)^2},
\]
and its sphere meets the polytope precisely at the \(\binom N{s_*}\) vertices \(v_S\) with \(|S|=s_*\). In particular, the diameter is attained at almost-balanced complementary high-coordinate sets, while the enclosing sphere contacts a different layer whose high-coordinate proportion tends to one third. Their sharp constants are
\[
\lim_{N\to\infty}\sqrt N\,\operatorname{diam}(Q_N)=\frac23,\qquad
\lim_{N\to\infty}\sqrt N\,R_N=\frac1{2\sqrt2},\qquad
\lim_{N\to\infty}\frac{\operatorname{diam}(Q_N)}{R_N}=\frac{4\sqrt2}{3}.
\]

## Assumptions and scope
The regular simplex has vertices \(e_1,\ldots,e_N\in\mathbb R^N\), so an edge has length \(\sqrt2\). All metric formulas use this **particular Euclidean embedding**; the volume ratio from [1] is affine-invariant, but the diameters and enclosing radii here are not. No result is asserted for arbitrary scalene simplex embeddings or for division ratios other than \(1:2\). Every set \(S\) is nonempty and proper. The diameter is the largest Euclidean distance between **any two points** of \(Q_N\), not the graph-theoretic edge-walk diameter. The enclosing radius is the minimum over all possible Euclidean centers in the affine hull, not a prescribed-center quantity.

## Proof
**1. Exhaustive vertices.** From \(x_i\le2x_j\) for all distinct indices and \(\sum_i x_i=1\), every coordinate is positive. Let \(a=\min_i x_i\), \(b=\max_i x_i\). If \(b<2a\), the point is in the relative interior and cannot be a vertex. When \(b=2a\), the active inequalities relate a high coordinate \(b\) to a low coordinate \(a\). If any intermediate coordinate lies strictly between \(a\) and \(b\), it participates in no active inequality; after enforcing \(\sum x_i=1\), at least one degree of freedom remains, so the point is not a vertex. Consequently, all vertex coordinates must take the two values \(a,2a\). Conversely, for each nonempty proper set \(S\), all the equalities \(x_i=2x_j\) with \(i\in S\), \(j\notin S\), together with \(\sum x_i=1\), uniquely determine \(v_S\). Thus the \(v_S\)'s are precisely all vertices (this also recovers the structural description in [1]).

**2. Pair-distance reduction.** For two vertex sets \(S,T\), put \(s=|S|\), \(t=|T|\), and \(r=|S\cap T|\). With \(u=N^{-1}\mathbf1\),
\[
v_S-u=\frac{\mathbf1_S-(s/N)\mathbf1}{N+s},\qquad
\|v_S-u\|^2=\frac{s(N-s)}{N(N+s)^2}.
\]
Hence
\[
D_N(s,t,r):=\|v_S-v_T\|^2=
\frac{s(N-s)}{N(N+s)^2}+
\frac{t(N-t)}{N(N+t)^2}-
\frac{2(r-st/N)}{(N+s)(N+t)}.
\]
For fixed \(s,t\), this is strictly decreasing in \(r\). Since \(\max(0,s+t-N)\le r\le\min(s,t)\), the largest distance with those two cardinalities is achieved **only** at \(r_0=\max(0,s+t-N)\). If \(s+t\le N\), the two sets are disjoint; if \(s+t\ge N\), their union is all of \([N]\).

**3. Strict exchange toward complementary sets.** Extend \(s,t\) temporarily to positive real variables solely to prove the displayed rational inequalities between integer values. In the disjoint region, substitute \(r_0=0\), writing the resulting rational function as \(D_0(s,t)\). An exact differentiation gives
\[
\frac{\partial D_0}{\partial s}=
\frac{N^2-3Ns+3Nt-st}{(N+s)^3(N+t)}.
\]
This is strictly positive whenever \(0<s\le t<N\). Thus if \(s<t\) and \(s+t<N\), increasing the smaller cardinality by one strictly increases the maximum possible squared distance (while the sets remain disjoint). If \(s=t\) and \(2s<N\), direct subtraction gives
\[
D_0(s+1,s)-D_0(s,s)=\frac{N-s-1}{(N+s)(N+s+1)^2}>0.
\]
It follows that no maximum can have \(s+t<N\).

In the covering region substitute \(r_0=s+t-N\), obtaining \(D_1(s,t)\). Differentiation gives
\[
\frac{\partial D_1}{\partial s}=
\frac{-3N^2-7Ns+5Nt+st}{(N+s)^3(N+t)}<0
\qquad(s\ge t,\quad 0<t\le s<N),
\]
since the numerator is at most \(-3N^2-2Ns+st<0\). Hence if \(s>t\) and \(s+t>N\), reducing the larger cardinality by one strictly increases the maximum squared distance while staying in the covering region, possibly reaching its boundary. For \(s=t\) and \(2s>N\), the exact difference is
\[
D_1(s-1,s)-D_1(s,s)=
\frac{3N^2+2Ns-5N-s^2+s}{(N+s)^2(N+s-1)^2}>0.
\]
Indeed \(s\le N-1\) and \(N\ge3\) give a positive numerator, bounded below by \(2N^2-3N+1>0\). Thus no maximum has \(s+t>N\). Every step is strict, and all cardinalities in the finite process remain integers in \(\{1,\ldots,N-1\}\).

**4. Strict optimization on the boundary.** Necessarily \(s+t=N\) and \(r=0\), so \(T=S^c\). Writing \(z=s(N-s)\), direct simplification yields
\[
D_N(s,N-s,0)=\frac{9Nz}{(2N^2+z)^2}.
\]
The derivative with respect to \(z\) is \(9N(2N^2-z)/(2N^2+z)^3>0\) for \(0<z\le N^2/4\). Therefore the unique possible maximizing cardinalities are \(s=m\) and \(s=N-m\). Substitution yields the two stated diameter expressions. Strictness of the overlap comparison and exchange inequalities excludes every other pair. Counting complementary subsets without ordering gives the claimed multiplicities. Since \(\|x-y\|^2\) is strictly convex as a function of either endpoint, any pair globally attaining a positive diameter consists of vertices; consequently the classification exhausts all *points*, not merely vertex pairs.

**5. Smallest enclosing sphere and contact layer.** The minimum enclosing Euclidean ball of a compact set is unique: if two distinct centers had the same optimal radius, the squared-distance midpoint identity would yield a strictly smaller covering ball. Every coordinate permutation preserves \(Q_N\), so uniqueness forces the center to be fixed by all permutations. Its coordinates therefore coincide and, since it lies in the affine hyperplane \(\sum x_i=1\), it must equal \(u\). The squared vertex radii are \(f_N(s)=s(N-s)/[N(N+s)^2]\), and
\[
f_N'(s)=\frac{N-3s}{(N+s)^3}
\]
when \(s\) is a real variable (the factor \(1/N\) cancels). The discrete maximum is among the integers nearest \(N/3\). For \(N=3q\), \(s=q\) is uniquely optimal. For \(N=3q+1\), an exact comparison gives
\[
f_N(q+1)-f_N(q)=-\frac{q}{2(2q+1)^2(4q+1)^2}<0;
\]
for \(N=3q+2\), it gives
\[
f_N(q+1)-f_N(q)=\frac{q+1}{2(2q+1)^2(4q+3)^2}>0.
\]
Thus the unique maximizing cardinality for every \(N\ge3\) is \(s_*=\lfloor(N+1)/3\rfloor\). Every point on the enclosing sphere must be a vertex, by strict convexity of the squared distance to \(u\), establishing the stated contact multiplicity. Dividing the closed formulas by their powers of \(N\) gives the three limits.

## Verification
The standalone, standard-library-only file `verify.py` independently constructs every vertex \(v_S\) for \(3\le N\le10\), checks all pairs exactly using rational arithmetic, and checks the diameter equality cases and their number. It also checks all feasible triples of cardinalities and intersection sizes for \(3\le N\le44\), plus the radial contact-layer predictions. Run it using `python3 verify.py` in the directory containing this document and the code; the observed result was `PASS exact assertions: 1756025`. These finite tests verify calculations and boundary cases; the all-dimensional claim rests on the strict exchange proof above, not on finite enumeration.

## Relationship to prior work
Kazakov [1] introduced the central polytope by simplex-edge trisections, established its defining inequalities, volume fraction, and vertex enumeration. Its volume ratio is \(1/\binom{2N-1}{N-1}\). The new mathematical content here is the exact metric diameter, the complete classification and count of all diametral pairs, and the unique minimum enclosing sphere with its sharp contact layer. An abstract combinatorial resemblance to shard polytopes [2] does not determine the Euclidean distances of this particular normalization. Targeted searches also compared results for Euclidean radius shells of other polytope constructions; no implication covering these formulas was identified.

## Limitations
The conclusion is specific to a regular simplex with side length \(\sqrt2\) and ratio-two barycentric inequalities. Applying an arbitrary affine transformation generally changes the metric. No results are claimed for graph diameter, nonregular simplex realizations, generalized trisection ratios, mean width, or complete intrinsic volumes. Novelty is assessed against inspected and indexed material rather than certified against every possible earlier source; independent mathematical audit has not been performed.

## References
[1] Yu. V. Kazakov, *Generalization of Marion's Theorem: Volumes of Central Polytopes Obtained by Trisecting the Edges of Simplices*, arXiv:2606.02087 (first public version June 1, 2026). Full text: https://www.researchgate.net/publication/405683659_Generalization_of_Marion%27s_Theorem_Volumes_of_Central_Polytopes_Obtained_by_Trisecting_the_Edges_of_Simplices

[2] Arnau Padrol, Vincent Pilaud, and Julian Ritter, *Shard Polytopes*, arXiv:2007.01008 (2020); International Mathematics Research Notices, 2023. Cited for neighboring combinatorial realizations, not as proof of a Euclidean metric assertion here.
