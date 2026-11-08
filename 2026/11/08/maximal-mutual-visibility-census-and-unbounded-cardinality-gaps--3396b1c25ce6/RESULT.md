# Maximal mutual-visibility census and unbounded cardinality gaps in near-crown graphs

## Finding
For every integer \(n\ge4\), define \(G_n=K_{n+1,n+1}-M_n\), where a matching of \(n\) edges has been removed, leaving one unmatched vertex in each bipartition class. A mutual-visibility set \(S\) is a set for which every two vertices of \(S\) have a geodesic with internal vertices outside \(S\). A maximal set is inclusion-maximal, not necessarily maximum in cardinality.

Let \(\mathcal M_n(z)=\sum_{S\text{ maximal mutual-visible}}z^{|S|}\). Then
\[
\boxed{\mathcal M_n(z)=2nz^{n+1}+2z^{n+2}+20\binom n6z^{2n-4}+2\binom n3z^{2n-2}+2n^2z^{2n-1}+z^{2n}.}
\]
Here \(\binom n6=0\) when \(n<6\), and coefficients at coinciding exponents are added. In particular \(\mu^-(G_n)=n+1\), \(\mu(G_n)=2n\), and the unique maximum set comprises the \(2n\) endpoints of removed matching edges. For \(n\ge8\), the precise maximal-set cardinality support is \(\{n+1,n+2,2n-4,2n-2,2n-1,2n\}\); thus \(n+3,\ldots,2n-5\) is a missing interval of length \(n-7\), and \(2n-3\) is never a maximal-set cardinality.

## Assumptions and scope
Use disjoint classes \(A=\{a_0,a_1,\ldots,a_n\}\) and \(B=\{b_0,b_1,\ldots,b_n\}\), with the only missing cross-edges \(a_i b_i\) for \(1\le i\le n\). For a proposed set \(S\), partition matched indices into counts: \(c\) (neither endpoint selected), \(d\) (only \(b_i\) selected), \(e\) (only \(a_i\) selected), and \(h\) (both endpoints selected). Write \(n=c+d+e+h\). Let omission flags \(u=1\) when \(a_0\notin S\), \(v=1\) when \(b_0\notin S\), and zero otherwise. Exactly \(c+d\) matched left endpoints and \(c+e\) matched right endpoints are omitted. The selected left and right counts are \(e+h+1-u\) and \(d+h+1-v\), respectively.

## Proof
**Geodesic criterion.** For \(n\ge4\), every same-side pair has distance two, a cross-side adjacent pair has distance one, and every removed matched pair \(a_i,b_i\) has distance three. A selected same-left-side pair is mutually visible precisely when at least one of its common right neighbors is omitted. This fails only if every right vertex outside their two potentially excluded matched partners is selected. If there are \(b=c+e\) omitted matched right vertices, the criterion, applicable simultaneously to *every* selected left pair, is
\[
L:\quad e+h+1-u\le1\quad\lor\quad v=1\quad\lor\quad b\ge3\quad\lor\quad(1\le b\le2\land c\ge1).
\]
Indeed if \(b\in\{1,2\}\) and no fully omitted matched pair occurs, one can choose the selected matched left partner(s) of all omitted right vertices, giving an obstructed pair; conversely a fully omitted matched pair or at least three omitted right vertices leaves a common omitted neighbor for every left pair. The symmetric condition for selected right pairs is
\[
R:\quad d+h+1-v\le1\quad\lor\quad u=1\quad\lor\quad c+d\ge3\quad\lor\quad(1\le c+d\le2\land c\ge1).
\]
For every selected deleted pair \(a_i,b_i\), a geodesic of length three must have two omitted internal vertices joined by an edge. Such a pair exists exactly when there is at least one omitted vertex on each side and those omissions are not a single matched nonedge. Hence its condition is
\[
P:\quad h=0\quad\lor\quad[(c+d+u>0)\land(c+e+v>0)\land\neg(c=1,d=e=u=v=0)].
\]
Every selected pair belongs to one of the three types above, so \(S\) is mutually visible *if and only if* \(L\land R\land P\).

**Maximality test.** A mutually visible set is maximal if adding any omitted vertex makes it fail \(L\land R\land P\). Exactly six possible occupancy updates exhaust all single additions: when \(c>0\), \((c,d,e,h)\mapsto(c-1,d,e+1,h)\) or \((c-1,d+1,e,h)\); when \(d>0\), \((c,d,e,h)\mapsto(c,d-1,e,h+1)\); when \(e>0\), \((c,d,e,h)\mapsto(c,d,e-1,h+1)\); and the flags \(u=1\mapsto0\), \(v=1\mapsto0\). In each case all selected-pair tests are recomputed after adding the vertex.

**Exhaustive finite reduction with a proof of infinite scope.** All atomic comparisons in \(L,R,P\) and in the six one-addition tests compare nonnegative sums of the four occupancy counts and the two binary flags with constants at most three, together with zero/equality tests of occupancy counts at most one. Each addition changes one occupancy count by at most one, never more. Replacing each original occupancy count larger than four by four therefore preserves *all* such comparisons both before and after every one-addition update: an originally large count, even if decremented, remains at least three after truncation; sums containing it remain above all relevant thresholds. Zero and one tests also remain unchanged. Thus maximality is invariant under componentwise truncation \(x\mapsto\min(x,4)\). For \(n\ge4\), the truncated four-count sum remains at least four. Conversely, every truncated state with count sum at least four represents a valid graph in the asserted domain.

A complete finite case check is therefore a rigorous all-\(n\) proof. The standalone program `verify.py`, function `finite_reduction`, evaluates all \(2360\) states \((c,d,e,h,u,v)\) with counts in \(\{0,1,2,3,4\}\), count sum at least four, and binary flags, and asserts that precisely these seven symmetric families pass maximality:

| Family | Occupancy and flags, with indicated symmetry | Number of sets | Cardinality |
| --- | --- | --- | --- |
| I | \((c,d,e;u,v)=(0,0,0;1,1)\) | \(1\) | \(2n\) |
| II | \((0,0,n;0,0)\) or \((0,n,0;0,0)\) | \(2\) | \(n+2\) |
| III | \((0,1,n-1;0,1)\) or \((0,n-1,1;1,0)\) | \(2n\) | \(n+1\) |
| IV | \((0,0,3;1,0)\) or \((0,3,0;0,1)\) | \(2\binom n3\) | \(2n-2\) |
| V | \((1,0,0;0,1)\) or \((1,0,0;1,0)\) | \(2n\) | \(2n-1\) |
| VI | \((1,0,1;0,0)\) or \((1,1,0;0,0)\) | \(2n(n-1)\) | \(2n-1\) |
| VII | \((0,3,3;0,0)\), if \(n\ge6\) | \(20\binom n6\) | \(2n-4\) |

Here unlisted \(h\) is uniquely determined by \(n\); for family I, \(h=n\). In family VII choose ordered disjoint three-subsets of the matched-index labels, so the count is \(\binom n3\binom{n-3}3=20\binom n6\). All families consist of mutually different occupancy patterns, so the counts do not overlap. The row counts sum to the claimed polynomial. Family I gives the unique largest set; family III gives the smallest maximal-set cardinality; and for \(n\ge8\) the six distinct exponents are precisely those stated. This proves the theorem.

## Verification
Run `python3 verify.py` with Python 3 standard library only. Its first test checks all \(2360\) reduced states, which is an exhaustive formal consequence of the truncation argument. Separately it constructs each graph of orders \(n=4,\ldots,9\), computes all shortest-path distances with breadth-first search, and directly checks the geodesic definition on every vertex subset. This exhaustive small-graph test examines \(1,397,760\) subsets; \(1,351,121\) are mutually visible and \(3,456\) are maximal. All exact coefficients agree. A finite check alone would not establish an unrestricted result; the truncation lemma supplies the necessary reduction.

## Relationship to prior work
Brešar and Yero introduced the lower mutual-visibility parameter and general theorems in a public July 2023 preprint. Their results motivate, but do not determine, the present exact family profile. Bujtás, Klavžar and Tian later established the general visibility-polynomial framework and studied complete bipartite graphs, not the matching-deleted near-crown subclass. Tonny and Shikhi derived visibility polynomials for other named graph classes and studied maximal configurations in cycles. The January 2026 OEIS sequence A390404 explicitly gives the visibility polynomial for the *perfect* crown graph \(K_{n,n}-M_n\), a related but different graph; that known polynomial is not claimed as new here and does not imply the maximal near-crown classification. Related results on matching-deleted bicliques concern resolving sets and other distinct graph invariants, without an implication to mutual visibility.

## Limitations
The claim concerns inclusion-maximal **mutual** visibility and only \(n\ge4\), not total, dual or connected mutual visibility. It does not classify all mutual-visibility subsets, only maximal ones. Publication priority is provisional because unindexed equivalent results remain possible. Computation gives a complete reduced decision table justified by a mathematical truncation lemma; it is not an independently audited or formally verified theorem. Coefficients at coinciding powers in the small cases are added.

## References
1. Boštjan Brešar and Ismael G. Yero, *Lower (total) mutual-visibility number in graphs*, first publicly posted 2023-07-06, arXiv:2307.02951v1, later *Applied Mathematics and Computation* 465 (2024), 128411, doi:10.1016/j.amc.2023.128411.
2. Csilla Bujtás, Sandi Klavžar and Jing Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, arXiv:2412.03066v1, *Aequationes Mathematicae* 99 (2025), 1883–1901, doi:10.1007/s00010-025-01197-y.
3. Tonny K. B. and Shikhi M., *On the Visibility Polynomial of Graphs*, arXiv:2507.01851 (2025).
4. Tonny K. B. and Shikhi M., *Visibility Polynomial of Some Graph Classes*, arXiv:2509.22571 (2025).
5. Andrew Howroyd and Eric W. Weisstein, *Number of mutual-visibility sets in the n-crown graph*, OEIS A390404, including January 2026 crown visibility-polynomial formula, https://oeis.org/A390404.
