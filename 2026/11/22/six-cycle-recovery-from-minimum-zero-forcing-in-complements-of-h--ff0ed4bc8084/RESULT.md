# Six-cycle recovery from minimum zero forcing in complements of high-girth graphs

## Finding
Let \(H\) be any finite simple graph on \(n\) vertices, with minimum degree at least two and girth at least five (the girth is infinite when there are no cycles). Let \(G=\overline H\). Write \(d(v)=\deg_H(v)\), let \(D(v)\) be the number of distinct vertices at distance exactly two from \(v\) in \(H\), and let \(c_6(H)\) count undirected simple cycles of length six, each counted once up to rotation and reversal. Put
\[
A(H)=\sum_{v\in V(H)}\binom{d(v)}2,\qquad B(H)=\sum_{v\in V(H)}\binom{D(v)}2.
\]
Then the minimum ordinary zero-forcing number of \(G\) is \(Z(G)=n-3\). Its minimum zero-forcing sets are precisely the complements of three-sets \(W=\{a,b,c\}\) for which some \(v\notin W\) is adjacent in \(H\) to exactly two vertices of \(W\). Their exact number is
\[
M(H)=(n-3)A(H)-B(H)+2c_6(H).
\]
Every set whose complement contains at most two vertices is zero forcing; none whose complement contains four or more vertices is zero forcing. Consequently the *complete* zero-forcing set polynomial is
\[
\mathcal Z_G(z)=M(H)z^{n-3}+\binom n2z^{n-2}+nz^{n-1}+z^n.
\]
In particular, the number of six-cycles can be recovered exactly from the number of minimum forcing sets and the local degree-two-neighborhood data:
\[
c_6(H)=\tfrac12\bigl(M(H)-(n-3)A(H)+B(H)\bigr).
\]
This is a single characterization-and-enumeration theorem. The scalar upper bound \(Z(G)\le n-3\) for connected complementary graph pairs, and the complement-of-cycle special case, are previously known; the new assertion is the general optimizer criterion and the six-cycle-sensitive enumeration, especially for graphs of degree at least three.

## Assumptions and scope
All graphs are undirected, finite and simple. The zero-forcing rule is *ordinary* (only an already-black vertex may force its sole white neighbor); a zero-forcing set is a black initial set from which a finite legal sequence colors every vertex black. For a disconnected graph \(H\), distance between different components is infinite, so \(D(v)\) includes only distance-two vertices in its own component. The condition on girth excludes triangles and quadrilaterals, but permits pentagons and hexagons. A cycle of length six is not required to be an induced cycle: under girth at least five, every six-cycle is automatically chordless. No regularity, connectedness or planarity is assumed. The finite verification examples below are illustrative and do not establish the unbounded-domain claim by enumeration.

## Proof
**1. At most three initially white vertices are possible.** As \(\delta(H)\ge2\) and \(H\) has no triangles, it has no universal vertex; hence every vertex of \(G\) has a neighbor. Suppose an initial set leaves four white vertices. A first force in \(G\) by a black vertex \(v\) can occur only if exactly three of those whites are neighbors of \(v\) in \(H\). Once the unique \(G\)-neighbor among the four is forced, the other three whites lie in \(N_H(v)\). The vertex \(v\) has zero \(G\)-neighbors among them. Every other vertex has at most one \(H\)-neighbor among them: two such neighbors would give a triangle if that vertex were also adjacent to \(v\), or a quadrilateral otherwise. Therefore every other black vertex has at least two white \(G\)-neighbors and cannot force. With no first force the process already stops. Thus no four-white configuration succeeds. By monotonicity in the initially black set, no configuration with more than four whites succeeds either.

**2. Three-white forcing criterion.** Suppose \(W=\{a,b,c\}\) is initially white. A first force is possible precisely when some black vertex \(v\notin W\) has exactly one \(G\)-neighbor in \(W\), equivalently exactly two \(H\)-neighbors, say \(a,b\), in \(W\). This force colors the third vertex \(c\). Choose \(u\in N_H(a)\setminus\{v\}\), which exists by minimum degree. Since \(a-v-b-u-a\) would be a quadrilateral, \(u\) cannot be adjacent to \(b\) in \(H\). It is black (possibly it is the just-forced vertex \(c\)), is nonadjacent to \(a\) in \(G\), and is adjacent to \(b\) in \(G\). Thus \(u\) forces \(b\). The remaining vertex \(a\) is forced by any of its black neighbors in \(G\), which exists by the absence of isolated vertices in \(G\). Hence any possible first force yields complete forcing, proving the criterion.

**3. Two or fewer whites always succeed.** For distinct whites \(a,b\), there is a vertex \(u\notin\{a,b\}\) adjacent in \(H\) to exactly one of \(a,b\). If \(a,b\) are adjacent in \(H\), take another neighbor of \(a\) and use triangle-freeness. If nonadjacent, otherwise all (at least two) neighbors of \(a\) would also neighbor \(b\), producing a quadrilateral. The vertex \(u\) sees exactly one of \(a,b\) in \(G\) and forces it; a remaining single white vertex has a black \(G\)-neighbor. The zero-white and one-white cases are immediate. Combining steps 1–3 gives \(Z(G)=n-3\) and the polynomial's top three coefficients.

**4. Enumerate all successful three-white sets.** Define \(J\) on \(V(H)\) by joining vertices at \(H\)-distance two. Distinct two-step paths from the same endpoint have distinct endpoints because \(H\) contains no triangles or quadrilaterals. Thus \(\deg_J(v)=D(v)\) and \(|E(J)|=A(H)\): every edge of \(J\) has a unique common neighbor in \(H\). Count three-sets containing at least one \(J\)-edge by inclusion-exclusion over their one, two or three induced \(J\)-edges:
\[
T=A(H)(n-2)-B(H)+t(J),
\]
where \(t(J)\) denotes the number of triangles of \(J\). A triangle \(\{a,b,c\}\) of \(J\) has three unique pairwise midpoint vertices in \(H\). Either all three midpoints coincide, making \(\{a,b,c\}\) a triple in one \(H\)-neighborhood, or they are all distinct, making a simple six-cycle alternating the three chosen vertices with their midpoints. Precisely two midpoints cannot coincide: if the midpoints of \(ab\) and \(ac\) agree but the midpoint of \(bc\) differs, the two midpoints together with \(b,c\) form a forbidden four-cycle. The two alternating vertex classes of every undirected six-cycle are distinct triangles of \(J\). Hence
\[
t(J)=\sum_v\binom{d(v)}3+2c_6(H).
\]
Not every three-set counted by \(T\) can force: the excluded sets are exactly (i) the three vertices of a two-edge \(H\)-path, with its only two-step midpoint initially white; and (ii) three neighbors of one \(H\)-vertex, so that their unique shared midpoint has zero white \(G\)-neighbors. Their numbers are, respectively, \(A(H)\) and \(\sum_v\binom{d(v)}3\). Each type is counted without duplication by the no-triangle/no-quadrilateral assumptions, and they are disjoint. No other three-set with a \(J\)-edge fails step 2. Thus
\[
M(H)=T-A(H)-\sum_v\binom{d(v)}3=(n-3)A(H)-B(H)+2c_6(H),
\]
as claimed.

For a \(d\)-regular graph this becomes
\[
M(H)=\frac{nd(d-1)}2\bigl(n-2-d(d-1)\bigr)+2c_6(H).
\]
The formula therefore distinguishes same-order, same-degree high-girth graphs by their six-cycle counts.

## Verification
Two different self-contained programs, `verify_python.py` (Python 3 standard library; sequential forcing) and `verify_cpp.cpp` (C++17; simultaneous forcing), independently enumerate **every** initially white set of cardinality two, three, and four on seven graphs. Both check the three-white structural criterion directly, count simple six-cycles independently and evaluate the formula from degree and distance-two data. Running `python3 verify_python.py` and `g++ -std=c++17 -O2 verify_cpp.cpp -o verify_cpp && ./verify_cpp` produces the figures in `TEST_OUTPUT.txt`.

| Underlying graph \(H\) | \(n\) | Minimum/maximum degree | Six-cycles | Minimum forcing sets of \(\overline H\) |
|---|---:|---:|---:|---:|
| Petersen | 10 | 3/3 | 10 | 80 |
| Heawood | 14 | 3/3 | 28 | 308 |
| Dodecahedral | 20 | 3/3 | 0 | 720 |
| Desargues | 20 | 3/3 | 20 | 760 |
| Projective-plane incidence graph, order three | 26 | 4/4 | 234 | 2340 |
| Eight-cycle with opposite-vertex chord | 8 | 2/3 | 0 | 34 |
| Five-cycle joined by a bridge to a six-cycle | 11 | 2/3 | 1 | 93 |

For example, the dodecahedral and Desargues graphs have the same \(n=20\) and degree three but yield 720 versus 760 minimum forcing sets in their complements, a difference of exactly twice the difference in six-cycle counts.

## Relationship to prior work
Eroh, Kang and Yi established in 2014 that when both a graph and its complement are connected, the zero-forcing number is at most three below the order; they also noted sharpness on complements of cycles. Their result is a scalar bound, not the present complete optimizer criterion, irregular-degree formula or six-cycle recovery. Work of Davila and Kenter concerns large girth in the graph **being forced**, rather than the complement of a large-girth graph. Earlier exact complement-of-path and complement-of-cycle enumerations constitute the degree-at-most-two boundary of the present formula. The 2026 study of forbidden induced configurations for small complementary zero-forcing number concerns a related scalar threshold; its accessible description does not itself supply the present enumeration. Its complete text was not available for direct inspection, so exact historical priority remains subject to that limitation.

## Limitations
The result requires minimum degree at least two and absence of triangles and quadrilaterals in the **underlying** graph \(H\), not in \(G\). It does not assert the formula for graphs with leaves or short cycles, or for skew/positive-semidefinite forcing. The exact count is for all labeled vertex subsets of each specified graph, not for symmetry orbits. Finite tests corroborate the all-order proof but cannot replace it. Historical priority is not independently certified; an inaccessible closely related 2026 preprint and unindexed work are residual overlap risks.

## References
1. L. Eroh, C. X. Kang, E. Yi, *On Zero Forcing Number of Graphs and Their Complements*, arXiv:1402.1962, first posted 9 February 2014; *Discrete Mathematics, Algorithms and Applications* 7 (2015), 1550002, DOI:10.1142/S1793830915500020.
2. R. Davila, F. Kenter, *Bounds for the Zero-Forcing Number of Graphs with Large Girth*, arXiv:1406.0482, first posted 2 June 2014; *Theory and Applications of Graphs* 2 (2015), article 1, DOI:10.20429/tag.2015.020201.
3. C. A. Alfaro and collaborators, *The forbidden structure for zero forcing number*, arXiv:2608.27972, first posted 28 August 2026 (abstract/secondary extraction checked; complete text inaccessible).
