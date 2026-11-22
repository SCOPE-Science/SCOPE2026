# Prime-field threshold and minimum-seed speed spectrum for two-neighbor bootstrap on projective-plane incidence graphs

## Finding
Let \(q=p^e\ge2\), with \(p\) prime and \(e\ge1\). Let \(G_q\) be the bipartite point–line incidence graph of the Desarguesian plane \(\operatorname{PG}(2,q)\). Under synchronous *two-neighbor bootstrap percolation*, an inactive vertex becomes permanently active in the next round exactly when at least two of its neighbors are active. The smallest initial set activating the entire graph has cardinality
\[
 m(G_q,2)=\begin{cases}4,&e=1,\\5,&e>1.\end{cases}
\]
When \(e=1\), the complete classification of minimum seed sets is: (i) four points in general position, or dually four lines in general position; (ii) three noncollinear points and a line incident with none of the three, or its dual. There are no minimum seeds containing two points and two lines. Writing \(v=q^2+q+1\) and
\[
 Q_q=\frac{v(v-1)q^2(q-1)^2}{24},
\]
there are exactly \(10Q_q\) minimum seed sets, with point-shore counts \(Q_q,4Q_q,0,4Q_q,Q_q\) at point counts \(0,1,2,3,4\), respectively.

At the first proper extension, \(q=4\), the exact five-seed census and synchronous completion-time spectrum are:

| Initially active points | Round 4 | Round 5 | Round 6 | All |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 1,008 | 10,080 | 0 | 11,088 |
| 1 | 0 | 35,280 | 20,160 | 55,440 |
| 2 | 10,080 | 60,480 | 30,240 | 100,800 |
| 3 | 10,080 | 60,480 | 30,240 | 100,800 |
| 4 | 0 | 35,280 | 20,160 | 55,440 |
| 5 | 1,008 | 10,080 | 0 | 11,088 |
| **All** | **22,176** | **211,680** | **100,800** | **334,656** |

Here one initial configuration is an unlabeled five-element *set* of distinct point/line vertices; the geometric points and lines themselves remain labeled. Every one of the \(334,656\) configurations is minimum, because no four-element set percolates. Every minimum configuration finishes in exactly four, five or six synchronous rounds.

## Assumptions and scope
Projective points are one-dimensional subspaces of \(\mathbb F_q^3\), and projective lines are kernels of nonzero linear forms, both represented by nonzero homogeneous triples up to nonzero scalar. Incidence is the zero dot product of their representatives. The graph has \(2(q^2+q+1)\) vertices. Seeds may freely mix point- and line-vertices; no initially active vertices are counted twice. Every round updates simultaneously from the preceding round's active set and keeps all previously active vertices. A seed *percolates* if every vertex eventually becomes active.

The theorem concerns finite **Desarguesian** projective planes, not arbitrary non-Desarguesian planes. The finite census concerns only \(q=4\), not arbitrary extension orders; its counts arise from complete computation, not a claimed closed formula for every \(q\).

## Proof
**Geometric closure equivalence.** Two active point-vertices force their unique joining line; two active line-vertices force their unique intersection point. The converse holds because a line-vertex has no point-neighbors other than incident points, and conversely for point-vertices. Thus the terminal active set is exactly the smallest point–line set closed under pairwise joins and meets. This is the \(P_3\)-convex hull of the initial set in the incidence graph.

**Coordinate-generation lemma.** Suppose a join–meet closed set contains a projective quadrangle \(Q\). Apply the unique projectivity sending the ordered quadrangle to the points \((1:0:0),(0:1:0),(0:0:1),(1:1:1)\). Let \(K\) be the smallest subfield of \(\mathbb F_q\) containing the coordinates of every other initially active normalized point or line. The closure is the incidence subplane \(\operatorname{PG}(2,K)\) whenever the extra seeds lie in that subplane.

For completeness, here is a constructive form of the elementary coordinate lemma. Use the affine chart \(z=1\), with origin \(O=(0,0)\), the two axis infinity points \(X_\infty=(1:0:0)\), \(Y_\infty=(0:1:0)\), and unit point \(I=(1,1)\). Joining and meeting these produces the affine axes and \((1,0),(0,1)\), hence the infinity direction \(D_\infty=(1:-1:0)\) of the line joining those last two points. Given the encoded scalar \(a\) as \((a,0)\), the line through \(D_\infty\) transports it to \((0,a)\). Horizontal/vertical lines make \((a,b)\) from the corresponding axis points; the line through \((a,b)\) and \(D_\infty\) meets the horizontal axis at \((a+b,0)\). To multiply \(a\) and \(b\), the line from \((1,0)\) to \((0,b)\) determines a direction, and its parallel through \((a,0)\) meets the vertical axis at \((0,ab)\). These are exclusively point joins and line intersections, valid in all characteristics. More explicitly, a marked affine point \((a,b)\) projects to \((a,0)\) and \((0,b)\) along the two coordinate infinity directions. A marked infinity point \((1:\alpha:0)\) is joined to the origin, intersects the constructible vertical line \(x=1\) in \((1,\alpha)\), and thereby reveals \(\alpha\) on the vertical axis; the other infinity point is already part of the frame. A marked line supplies its normalized coefficients through the intersections with the coordinate axes and with infinity, followed by the same projections. Therefore the coordinate set contains \(0,1\), is closed under addition and multiplication, and, being finite, contains inverses of its nonzero elements. It equals \(K\). Every \(K\)-rational point and line follows by intersections and joins; no operation leaves the \(K\)-rational subplane. The lemma follows.

**No seed of size at most three percolates.** Three initial points activate at most their three pairwise joining lines, and those lines meet only at the original points; if the points are collinear there is only one newly activated line. The dual statement holds for three initial lines. Two initial points and one initial line can create at most their joining line and its intersection with the initially active line: all resulting point-vertices lie on that joining line, so no further vertices activate. The one-point/two-line situation is dual. Fewer seeds cannot do more. Therefore every percolating set has at least four vertices.

**Four seeds cannot percolate except in the asserted prime-field types.** For four seeds all on one shore, a projective quadrangle is the only case whose closure is not a small degenerate point–line configuration: if at least three points are collinear, the points lie in a line together with at most one external point, and the joining lines and their intersections add nothing outside those points. Dually for four lines.

For two point seeds \(A,B\) and two line seeds \(L,M\), let \(N=AB\) and \(C=L\cap M\). If \(C\notin N\), set \(D=N\cap L\), \(E=N\cap M\). All subsequently activated points lie in \(\{A,B,C,D,E\}\), and all lines lie among \(N,CA,CB,CD,CE\): this set of at most ten vertices is join–meet closed. If \(C\in N\), the active points stay on \(N\) and the active lines stay in the pencil through \(C\); this is also proper. Therefore no two-plus-two four-seed set percolates.

Consider three point seeds. If collinear, joins give at most one new line, and an additional initial line creates at most its intersection with that line. If noncollinear and the initially selected line passes through one of the points, the closure consists of at most the triangle's three vertices, its opposite-side intersection with the selected line, and their joining lines. Neither arrangement percolates. In the remaining case the three points form a triangle and the initial line avoids all three. Normalize the triangle to the coordinate vertices; the line has all three coefficients nonzero and can be normalized to \(x+y+z=0\), an object over \(\mathbb F_p\). In the first round the three triangle-side lines activate. In the second round the line's intersection points with the sides activate; two such points together with two suitable original triangle vertices form a projective quadrangle. By the coordinate-generation lemma the closure is exactly \(\operatorname{PG}(2,p)\). Dually, the same applies to one-point/three-line configurations.

A four-point quadrangle likewise has closure exactly \(\operatorname{PG}(2,p)\), by its coordinate normalization. It percolates if and only if \(q=p\). This proves the lower bound of five when \(e>1\), and proves the precise prime-order classification once we observe that four-point quadrangles and the mixed nonincident triangle–line configurations do percolate when \(e=1\).

**Five seeds suffice for every proper extension.** Choose an element \(\alpha\in\mathbb F_q\) generating \(\mathbb F_q\) over its prime field. Such an element exists because the finite multiplicative group is cyclic. Initially activate the four points \((1:0:0),(0:1:0),(0:0:1),(1:1:1)\), and the fifth point \((1:\alpha:0)\). They include a quadrangle, and the coordinates generate the whole \(\mathbb F_q\). The coordinate-generation lemma forces every point and every line of the full plane. Hence five seeds suffice, completing the all-order minimum-size theorem.

**Prime-field counting.** The number of unordered projective quadrangles is
\[
 Q_q=\frac{v(v-1)q^2(q-1)^2}{4!}.
\]
Indeed choose an ordered pair of points, then a third point away from their line (\(q^2\) choices), then a fourth point away from the triangle's three sides (\((q-1)^2\) choices). Each unordered quadrangle has \(4!\) orderings. The number of unordered noncollinear point triples is \(v(v-1)q^2/3!\), and each has \((q-1)^2\) lines avoiding all three vertices. Their product is \(4Q_q\). Dualizing yields the remaining two classes, giving \(10Q_q\) in total.

**Complete finite count and completion times at \(q=4\).** The two standalone programs `verify_bootstrap.py` and `verify_bootstrap.cpp` construct all projective vectors and incidence edges directly from finite-field arithmetic. They enumerate all \(\binom{42}{4}=111,930\) four-seeds and all \(\binom{42}{5}=850,668\) five-seeds. For every candidate, they iteratively add precisely the previously inactive vertices with two or more active neighbors until no further changes occur. They test terminal equality with the full 42-vertex set, count by initial point-shore size, and count the exact number of nonempty synchronous update rounds. The outputs of both implementations agree with every entry of the displayed census. Since the loops traverse every combination exactly once, this exhaustive computation proves the finite census (not a non-exhaustive experiment); the separate symbolic reasoning proves the all-order part.

## Verification
Run `python3 verify_bootstrap.py`. Separately compile and run `g++ -std=c++17 -O2 verify_bootstrap.cpp -o verify_bootstrap && ./verify_bootstrap`. Each prints `VERIFY_OK` after reproducing the complete first-success threshold for \(q=2,3,4\), the point/line composition counts, and the complete completion-time table. The Python code uses polynomial reduction for \(\mathbb F_4\); the C++ code uses an explicit multiplication table for the same field and independently generates the normalized projective representatives and incidence matrix. They agree on \(70\) four-seeds for \(q=2\), \(2,340\) for \(q=3\), no four-seed for \(q=4\), and \(334,656\) five-seeds for \(q=4\). The all-order field-generation assertion rests on the geometric proof, not an extrapolation from those finite checks.

## Relationship to prior work
Morris (2009) gives the general two-neighbor graph bootstrap process and works on grid minimal percolating sets; it does not treat finite projective-plane incidence graphs. Gerbner–Keszegh–Mészáros–Patkós–Vizer (2016) study **line percolation**, which infects every point of a line after a threshold of infected points; their model is not the alternating point–line *vertex* bootstrap process here, and their paper explicitly regards line threshold two as an elementary case. The published 2026 subfield/colour-refinement note already establishes a join–meet coordinate-generation lemma and a five-point individualization threshold for a different color-refinement dynamics; this geometric ingredient, and its implications for all-point seed sufficiency, are credited as prior knowledge, not claimed original here. The 2026 classification of the Heawood graph's \(P_3\)-convexity lattice contains the \(q=2\) closure structure and is likewise credited.

The contribution advanced here is the **mixed point–line bootstrap classification and prime-order exact count**, together with the full **minimum-seed composition-by-time spectrum at \(q=4\)**. These do not follow merely by substituting a graph into the cited grid or line-percolation theorems, nor are the numerical tables stated in the inspected colour-refinement or Heawood convexity results. The related subfield lemma makes the threshold argument shorter, but does not determine how mixed seeds are classified or how rapidly they percolate.

## Limitations
Absolute historical priority is not certified: earlier unindexed work or unavailable source text could contain an equivalent census. The extensive finite computation is exhaustive only at orders two, three and four, not at arbitrary finite orders. No formula is asserted for the number or completion times of five-seeds at \(q>4\); the general theorem assumes a finite field and does not extend automatically to non-Desarguesian planes. No independent mathematical audit has been performed.

## References
1. R. Morris, *Minimal Percolating Sets in Bootstrap Percolation*, Electronic Journal of Combinatorics 16 (2009), #R2, published 7 January 2009, primary MSC 05D99. DOI: https://doi.org/10.37236/91 .
2. D. Gerbner, B. Keszegh, G. Mészáros, B. Patkós and M. Vizer, *Line Percolation in Finite Projective Planes*, preprint 1 August 2016, arXiv:1608.00531, https://arxiv.org/abs/1608.00531 .
3. *A subfield criterion and five-point individualization threshold for projective-plane colour refinement*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-subfield-criterion-and-five-point-individualization-threshold--f7ad48a4f739 .
4. *The \(P_3\)-convexity lattice of the Heawood graph*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-the-p-3-convexity-lattice-of-the-heawood-graph--87513bd35bd8 .
