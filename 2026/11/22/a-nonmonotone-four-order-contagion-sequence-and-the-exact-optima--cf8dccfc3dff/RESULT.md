# A nonmonotone four-order contagion sequence and the exact optimal-seed census of the affine plane of order five

## Finding
For \(q\in\{2,3,4,5\}\), let \(G_q\) be the point–line incidence graph of the Desarguesian affine plane \(\operatorname{AG}(2,\mathbb F_q)\). In synchronous two-neighbour bootstrap percolation, an initially inactive vertex becomes active in the next round exactly when at least two adjacent vertices are active; activity is permanent. Write \(m(G_q,2)\) for the smallest number of initially active vertices that ultimately activate every vertex. Then
\[
\boxed{\bigl(m(G_2,2),m(G_3,2),m(G_4,2),m(G_5,2)\bigr)=(4,5,5,4).}
\]
Thus the minimum is not monotone over these first four prime-power orders: after rising from four to five, it drops back to four at order five.

The exact numbers of minimum seed sets for these orders are, respectively, \(8,4572,142176,70000\). At order five, the complete classification by *number of initially active point-vertices* is
\[
\begin{array}{c|rrrrr}
\text{point seeds}&0&1&2&3&4\\\hline
\text{optimal sets}&9000&32000&0&24000&5000.
\end{array}
\]
In particular no order-five optimal seed set has two points and two lines. Under the specified synchronous process, all \(70000\) optimal sets finish in between seven and eleven rounds, with exact completion-time counts
\[
\begin{array}{c|rrrrr}
\text{round}&7&8&9&10&11\\\hline
\text{sets}&5000&23000&18000&12000&12000.
\end{array}
\]
The counts are for actual labelled geometric vertices; seed sets are unordered and have no repetition. No assertion is made for unlisted affine-plane orders.

## Assumptions and scope
The affine points are pairs \((x,y)\in\mathbb F_q^2\). Lines are the \(q^2\) graphs \(y=ax+b\) and the \(q\) vertical lines \(x=b\), so \(G_q\) has \(q^2\) point vertices, \(q(q+1)\) line vertices, and \(q(2q+1)\) vertices in total. An edge joins a point to a line precisely at incidence. For \(q=4\), the field is \(\mathbb F_2[t]/(t^2+t+1)\); other fields in the statement are the prime fields.

Write \(A_0=S\subseteq V(G_q)\) and recursively
\[
A_{r+1}=A_r\cup\{v\in V(G_q):|N(v)\cap A_r|\ge2\}.
\]
The completion time is the smallest nonnegative \(r\) for which \(A_r=V(G_q)\). All enumeration bounds are exhaustive, not sampled.

## Proof
The finite theorem admits a complete, terminating exhaustive proof. The two included independent programs reconstruct the incidence graph from the displayed field definitions, enumerate *every* subset of the relevant cardinality, and perform the exact synchronous transition until it stops.

In the affine-coordinate verifier, points and lines are generated as above. Distinct vertices are numbered with points first, and the neighborhood of each vertex is stored as an arbitrary-precision integer bitmask. For every candidate seed set \(S\), its active-set mask \(a\) is updated simultaneously by computing the set of all inactive vertices whose neighbor mask intersects \(a\) in at least two set bits. The resulting operator is monotone, adds a vertex at most once, and stabilizes after at most \(|V(G_q)|\) rounds. Consequently the computed fixed point equals the mathematical closure defined in the preceding section. The program accepts a candidate precisely when the fixed-point bitmask contains every vertex.

The independent homogeneous-coordinate verifier instead enumerates the affine points as \((x,y,1)\), enumerates *normalized nonzero* projective line forms other than the line at infinity, and tests incidence by the dot-product equation. It uses a separately written synchronous closure routine. Both representations produce all \(q^2\) points and all \(q(q+1)\) lines with no repetitions. Exact integer arithmetic is used throughout, including polynomial-remainder arithmetic for \(\mathbb F_4\); no numerical tolerance or approximation enters.

The exhaustive outputs are:

| Order \(q\) | Checked seed size | Contagious sets | Point-count vector, from zero through the checked size |
|---|---:|---:|---|
| 2 | 3 | 0 | \((0,0,0,0)\) |
| 2 | 4 | 8 | \((3,4,0,0,1)\) |
| 3 | 4 | 0 | \((0,0,0,0,0)\) |
| 3 | 5 | 4572 | \((396,1224,1404,1080,396,72)\) |
| 4 | 4 | 0 | \((0,0,0,0,0)\) |
| 4 | 5 | 142176 | \((8448,32640,46080,36480,15840,2688)\) |
| 5 | 3 | 0 | \((0,0,0,0)\) |
| 5 | 4 | 70000 | \((9000,32000,0,24000,5000)\) |

For each \(q\), there is at least one contagious set at the claimed minimum size. If no set of size \(k-1\) percolates, no smaller set can: any smaller set extends to one of size \(k-1\), and bootstrap closure is monotone in the initial set. The zero counts immediately below each claimed minimum therefore prove minimality. The final order-five completion-time row follows from exactly the same exhaustive enumeration, retaining the first round in which the closure fills the entire graph. Both independent programs reproduce it.

The total four-set search spaces are \(\binom{10}{4}\), \(\binom{21}{4}\), \(\binom{36}{4}\), and \(\binom{55}{4}\); the five-set spaces for orders three and four are \(\binom{21}{5}\) and \(\binom{36}{5}\), respectively. Each of these spaces is enumerated in full by both provided implementations. This establishes the finite claims with no extrapolation.

## Verification
Run `python3 verify_affine_chart.py` and `python3 verify_homogeneous.py` using a Python interpreter supporting integer \(`bit_count`\). Both print their complete census, assert every coefficient and terminate with a success marker. No external dependencies or network connection are required. The two source files are standalone and embedded with this manuscript. Their exact output is recorded in `VERIFICATION.md`.

## Relationship to prior work
Freund, Poloczek and Reichman (2015) define ordinary graph bootstrap percolation and study small contagious sets via density conditions; they do not enumerate affine incidence-graph seeds. Gerbner, Keszegh, Mészáros, Patkós and Vizer (2016) treat a *different* projective-plane line-percolation rule: when a line contains enough active points, every point on that line becomes active. In the present model, that event activates the **line-vertex only**; its other point-vertices still require two active incident lines. Results for their model therefore do not imply these counts. A study of subfield-based colour refinement in projective incidence graphs and a prior exact projective-plane bootstrap-seed census concern different structures; neither determines the affine plane of order five with its line at infinity removed. The affine incidence graph is not obtained by merely restricting a projective contagious-set count, because closure changes when vertices and incidences are deleted.

## Limitations
This is an exact finite census at four specified orders, not a formula for all prime powers. In particular it does not prove that four seeds suffice for every prime order at least five, nor that five always suffice over a proper extension. The two enumerators are independent software checks of finite exhaustive spaces, not an external formal proof or independent scholarly audit. The assertions about the first return refer strictly to the listed orders two, three, four, five. Literature searches cannot rule out all earlier unpublished or unindexed enumerations.

## References
1. D. Freund, M. Poloczek and D. Reichman, *Contagious Sets in Dense Graphs*, arXiv:1503.00158, first made public 2015-02-28. https://arxiv.org/abs/1503.00158
2. D. Gerbner, B. Keszegh, G. Mészáros, B. Patkós and M. Vizer, *Line Percolation in Finite Projective Planes*, arXiv:1608.00531, first made public 2016-08-01. https://arxiv.org/abs/1608.00531
3. *A subfield criterion and five-point individualization threshold for projective-plane colour refinement* (2026). Used for comparison of projective join–meet closure only; the present theorem concerns a different graph process.
