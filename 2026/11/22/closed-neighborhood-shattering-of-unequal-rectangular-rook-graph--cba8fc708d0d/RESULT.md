# Closed-neighborhood shattering of unequal rectangular rook graphs

## Finding
Let \(R_{m,n}=K_m\square K_n\) be the labeled rook graph on cells of a full \(m\)-row, \(n\)-column rectangle, for positive integers \(m,n\). Each Boolean concept is a **closed** neighborhood, hence the union of the row and column through a chosen center cell. Let \(s_j(m,n)\) count the unordered \(j\)-cell supports shattered by these \(mn\) concepts. Write \(\mathbf1[P]\) for the indicator of a condition \(P\), and \(\binom ab=0\) for nonnegative integers \(a<b\). Then \(s_0=1\), \(s_j=0\) for every \(j\ge4\), and
\[
\begin{aligned}
s_1(m,n)&=mn\,\mathbf1[m,n\ge2],\\
s_2(m,n)&=m\binom n2\mathbf1[m\ge2,n\ge3]
 +n\binom m2\mathbf1[m\ge3,n\ge2]
 +2\binom m2\binom n2\mathbf1[m,n\ge3],\\
s_3(m,n)&=m(m-1)\binom n2(n-2)\mathbf1[m\ge3,n\ge4]\\
&\qquad+n(n-1)\binom m2(m-2)\mathbf1[m\ge4,n\ge3].
\end{aligned}
\]
These formulas count the complete labeled-support shattering polynomial \(\Phi_{m,n}(z)=\sum_{j\ge0}s_j(m,n)z^j\).

**Structural classification.** Identify a cell \((i,j)\) with the edge \(r_ic_j\) of the complete bipartite graph on row/column labels. A nonempty support is shattered precisely when it has an unused row and an unused column, and its selected-edge graph has one of the following shapes: a single edge; two adjacent edges; two disjoint edges; or a two-edge star plus one disjoint edge. The last shape requires three distinct used columns and two used rows when its center is a row, or the transpose. No support of four or more cells is shattered.

Consequently the VC dimension is zero if \(\min(m,n)=1\); one for \((m,n)=(2,2)\); two if \(\min(m,n)\ge2\) and either \(\min(m,n)=2\) with \(\max(m,n)\ge3\), or \((m,n)=(3,3)\); and three exactly if \(\min(m,n)\ge3\) and \(\max(m,n)\ge4\). This recovers known dimension data and the known equal-alphabet case as comparisons, not as novelty claims.

The substantive new scope is the **coefficientwise and support-level classification for unequal rectangles**. It distinguishes graphs whose vertex count, shattering of every pair, and VC dimension are identical. For instance,
\[
\Phi_{3,8}(z)=1+24z+276z^2+1008z^3,
\qquad
\Phi_{4,6}(z)=1+24z+276z^2+1080z^3.
\]
Both graphs have twenty-four vertices and VC dimension three, yet their shattered-triple counts differ by seventy-two.

## Assumptions and scope
The graph is the entire Cartesian product \(K_m\square K_n\), not a subgraph and not an open-neighborhood system. The center cell belongs to its own closed neighborhood. Explicitly,
\[
N[(a,b)]=\{(i,j):i=a\ \text{or}\ j=b\}.
\]
A support \(S\) is shattered if \(\{N[(a,b)]\cap S:(a,b)\in[m]\times[n]\}=2^S\). Each support is an unordered set of distinct labeled cells; isolated row and column vertices in its associated bipartite support graph are not treated as support edges. When one dimension is one, every closed neighborhood is the entire board, so no nonempty support is shattered.

## Proof
**Step 1: Empty trace and singleton necessity.** For any nonempty cell support \(S\), the empty trace occurs exactly when there exists a center with both its row and its column unused by \(S\). Equivalently, the selected-edge support graph \(H\subseteq K_{m,n}\) leaves at least one row vertex and at least one column vertex isolated. For a selected edge \(e=r_ic_j\) to appear by itself as a trace, the center must choose at least one of \(r_i,c_j\); if both endpoints have selected-edge degree at least two, choosing either endpoint also covers some other edge. Thus every edge of any shattered support has at least one degree-one endpoint.

A finite bipartite simple graph in which every edge has a degree-one endpoint is a star forest (its nontrivial components are stars, including isolated edges). Indeed, any connected component with two vertices of degree at least two would contain an edge joining vertices of degree at least two along a shortest path, contradicting the condition. Therefore every shattered support is a star forest; this argument uses only required singleton traces, not any finite enumeration.

**Step 2: One and two cells.** For \(m,n\ge2\), every singleton is shattered: the center at its cell realizes the positive label and a different row and column realize the negative. For two adjacent selected edges, the star center chooses their common row or column, while the leaf choices isolate either edge. An unused row and column exist precisely when \(m\ge2,n\ge3\) for a row-centered star, and conversely for a column-centered star. For two disjoint selected edges, a center choosing the row of one and the column of the other covers both, and choosing one endpoint together with an unused opposite-side label isolates either. The empty trace exists precisely when \(m,n\ge3\). These witnesses prove sufficiency, and the empty-trace condition proves necessity of the stated side-size bounds. Counts are respectively \(m\binom n2\), \(n\binom m2\), and \(2\binom m2\binom n2\).

**Step 3: Three cells.** The only three-edge star forests are a three-edge star, a two-edge star plus a disjoint edge, and three disjoint edges. Three disjoint edges cannot be covered by one row and one column, so the full positive trace fails. In a three-edge row star, selecting exactly two of its three edges without the third would require selecting the two corresponding column vertices, whereas a center selects only one column; the column-star case is symmetric. Therefore only a two-edge star plus a disjoint edge can be shattered.

For sufficiency, consider \(e_1=(r_1,c_1)\), \(e_2=(r_1,c_2)\), \(e_3=(r_2,c_3)\) with all displayed row labels and column labels distinct. The empty trace requires an additional unused row \(r_3\) and column \(c_4\), hence \(m\ge3,n\ge4\). With these spare labels, all eight traces are realized by the following centers:

| Desired trace | Center |
| --- | --- |
| \(\varnothing\) | \((r_3,c_4)\) |
| \(\{e_1\}\) | \((r_3,c_1)\) |
| \(\{e_2\}\) | \((r_3,c_2)\) |
| \(\{e_3\}\) | \((r_2,c_4)\) |
| \(\{e_1,e_2\}\) | \((r_1,c_4)\) |
| \(\{e_1,e_3\}\) | \((r_2,c_1)\) |
| \(\{e_2,e_3\}\) | \((r_2,c_2)\) |
| \(\{e_1,e_2,e_3\}\) | \((r_1,c_3)\) |

The transposed construction handles a column-centered star, and the empty-trace condition is again necessary. A row-centered two-edge star plus a disjoint edge has a unique repeated row. Choose that row in \(m\) ways, its two columns in \(\binom n2\) ways, and the disjoint edge in \((m-1)(n-2)\) ways. This proves the first summand of \(s_3\); transposition proves the second.

**Step 4: No shattered quartet.** If a four-edge support were shattered, every three-edge sub-support would be shattered. By Steps 1 and 3, it would have to be a star forest in which every choice of three edges is a two-edge star plus a disjoint edge. The partitions of four into component-edge sizes are \(4\), \(3+1\), \(2+2\), \(2+1+1\), and \(1+1+1+1\). All except \(2+2\) contain a three-edge sub-support that is a three-edge star or three disjoint edges. Hence its graph must consist of two disjoint two-edge stars. If both stars have centers on the same bipartition side, a trace selecting exactly one edge from each would require two leaves on the opposite side, which is impossible with only one selected vertex per side. If their centers lie on opposite sides, the trace selecting both edges from the first star and exactly one edge from the other would require choosing the first star center and one leaf of the other on that same side. This too is impossible. Thus no quartet is shattered. Shattering is hereditary under restricting supports, so no larger support is shattered.

The coefficient formulas follow from Steps 1–4. Positivity of the coefficients gives the stated dimension cases. The twenty-four-vertex example follows by direct substitution.

## Verification
The standalone standard-library script `VERIFY.py` directly builds row-column closed-neighborhood traces and independently applies the star-forest classifier. It compares every support of sizes one through four for all twenty-one rectangles \(1\le m\le n\le6\), including all boundary cases, then checks every predicted coefficient. The completed run passed \(144135\) individual support decisions (\(266\) singletons, \(2506\) pairs, \(19254\) triples, and \(122109\) quartets), and independently checked the \(4\times4\) published specialization \(1+16z+120z^2+288z^3\). Run from the package directory with `python3 VERIFY.py` and compare to `checks.txt`. The universal result is proved above; finite testing is a separate check, not an extrapolation.

## Relationship to prior work
Adler, Benediktsson and Macpherson [1] establish general VC bounds for **open** Hamming-graph neighborhoods and consequent boundedness for closed neighborhoods; that does not determine the exact closed-support coefficients for unequal alphabet sizes. Coudert, Csikós, Ducoffe and Viennot [2], first public on 2024-05-13, develop algorithms and general bounds for **closed** graph neighborhoods, not these two-parameter formulas. The prior complete rectangular-rook result [3] concerns **open** neighborhoods, represented as symmetric-difference rather than union of row/column incidence stars; its triple-support types are different. The prior complete **closed** homogeneous Hamming-graph result [4] determines every square-board specialization \(m=n=q\), which is credited and not claimed original. The earlier \(4\times4\) rook-versus-Shrikhande result [5] gives the closed polynomial on that square board; it is likewise subsumed in the credited specialization. The mixed-alphabet online-dimension result [6] gives the complete mixed rectangular **VC and Littlestone dimensions** but not the polynomial or all support structures.

The new claim is specifically the exact full shattering polynomial and star-forest support criterion for non-square rectangles, including side-size exceptions and the shape-sensitive triple coefficient. These claims do not follow from uniform-alphabet coefficients or the mixed-alphabet dimension table: restricting both the available centers and the support universe changes the realized traces. The equal-side formulas and all already known dimension conclusions are provided solely as checks and context.

## Limitations
Only complete rectangular rook graphs and their closed neighborhoods are studied. The result does not cover arbitrary induced subgraphs, radius-two balls, open neighborhoods, or adaptive dimensions. Although all parameter values are included for a unified theorem, the original contribution is the non-square extension; square cases and static VC dimension results are credited to prior work. The independent checker tests only finite boards and does not replace the proof for arbitrary sizes. Source-access limitations and potential differently indexed descriptions of row-column cross concept systems leave a historical-priority risk. No independent external mathematical audit has been conducted.

## References
[1] I. Adler, B. G. Benediktsson, D. Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042v1, 2020-07-31; accepted manuscript https://eprints.whiterose.ac.uk/id/eprint/178584/1/Adler_Benediktsson_Macpherson.pdf.

[2] D. Coudert, M. Csikós, G. Ducoffe, L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588v1, 2024-05-13; SEA 2024, DOI:10.4230/LIPIcs.SEA.2024.8, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SEA.2024.8.

[3] *Exact open-neighborhood shattering polynomials of rectangular rook graphs*, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-open-neighborhood-shattering-polynomials-of-rectangular-ro--ffaa2f7a2b1d/RESULT.md.

[4] *Closed-neighborhood shattering polynomials of all Hamming graphs*, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-closed-neighborhood-shattering-polynomials-of-all-hamming-graphs--6c82fc864f93/RESULT.md.

[5] *A closed-neighborhood shattering-polynomial separation of the Shrikhande and rook graphs*, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-closed-neighborhood-shattering-polynomial-separation-of-the-sh--670b6697d463/RESULT.md.

[6] *Exact online neighborhood dimensions of mixed-alphabet Hamming graphs*, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-online-neighborhood-dimensions-of-mixed-alphabet-hamming-g--4e24e4c568c0/RESULT.md.
