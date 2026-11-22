# Redundant identifying codes of the Heawood graph: the Fano deletion classification

## Finding

**Theorem.** Let \(H\) be the Heawood graph, the point-line incidence graph of the Fano plane, and call \(S\subseteq V(H)\) a *redundant identifying code* if \(S\setminus\{s\}\) is a closed-neighborhood identifying code for every \(s\in S\). For a set \(T=V(H)\setminus S\) of omitted detector locations, the redundant codes are characterized as follows:

1. Every \(T\) of size at most two is permitted.
2. A three-element \(T\) is permitted exactly when it is either a noncollinear triple of points, a nonconcurrent triple of lines, or a mixed triple with one point and two lines (or its dual) having **exactly one incidence** among the point and the two lines.
3. A four-element \(T\) is permitted exactly when it is either the four points outside a line, the four lines not incident with a point, or two points and two lines whose induced incidence relation is a perfect matching.
4. No \(T\) of size five or more is permitted.

Consequently, for labelled vertex subsets, the entire redundant-identifying-code cardinality polynomial is
\[
R_H(z)=98z^{10}+224z^{11}+91z^{12}+14z^{13}+z^{14}.
\]
Its minimum cardinality is \(10\), exactly \(98\) codes attain that minimum, **all inclusion-minimal redundant codes have cardinality ten**, and the minimum codes form exactly two orbits under the graph automorphism group of order \(336\), of respective sizes \(14\) and \(84\).

## Assumptions and scope

The fourteen labelled vertices are points \(p_i\) and lines \(\ell_j\), \(i,j\in\mathbb Z/7\mathbb Z\), where \(\ell_j\) is incident with \(p_j,p_{j+1},p_{j+3}\). For any vertex \(v\), \(N[v]\) denotes the closed neighborhood. A code \(C\) is identifying when the traces \(N[v]\cap C\), for all fourteen vertices \(v\), are nonempty and pairwise distinct. A *redundant* code remains identifying after removal of any one of its selected vertices. There is no requirement that two sensors fail simultaneously. Counts use the fixed fourteen labels; the symmetry-orbit statement alone uses graph automorphisms.

## Proof

**Step 1: exact failure conditions.** The one-failure condition is equivalent to
\[
|N[v]\cap S|\ge2\quad(v\in V(H)),\qquad
|(N[u]\mathbin\triangle N[v])\cap S|\ge2\quad(u\ne v).
\]
Indeed, a trace is nonempty after every single sensor removal precisely if it initially contains at least two sensors; similarly two traces remain different after any removal precisely if the symmetric difference contains at least two sensors. This is also the standard characterization of redundant identifying codes.

Every closed neighborhood in \(H\) has four vertices. Two distinct point vertices, or two distinct line vertices, have symmetric-difference neighborhoods of size six: they share the unique common incidence neighbor. A nonincident point and line have disjoint closed neighborhoods, hence symmetric difference of size eight. At an incident point-line pair \((p,\ell)\), the symmetric difference is a four-element set
\[
X(p,\ell)=\bigl(N(p)\setminus\{\ell\}\bigr)\ \cup\ \bigl(N(\ell)\setminus\{p\}\bigr),
\]
consisting of the other two lines through \(p\) and the other two points on \(\ell\). Therefore, for \(|T|\le4\), the exact redundant-code criterion becomes
\[
|T\cap N[v]|\le2\quad\text{for all }v,\qquad
|T\cap X(p,\ell)|\le2\quad\text{for all }p\in\ell.
\tag{1}
\]
The six- and eight-element symmetric differences automatically retain at least two selected elements when at most four vertices are omitted. For \(|T|\le2\), both inequalities in (1) always hold.

**Step 2: deleted triples.** For three omitted points, (1) fails exactly when some line contains all three, i.e. the points are collinear. Three omitted lines obey the dual nonconcurrency condition. For \(T=\{p,\ell,m\}\) with two lines, the closed-neighborhood test excludes \(p\in\ell\cap m\). If \(p\) lies on neither line, let \(q=\ell\cap m\) and take the unique line \(t\) through \(p,q\). Then \(t\ne\ell,m\) and \(X(q,t)\) contains all three omitted vertices, violating (1). If \(p\) lies on exactly one selected line, no \(X(q,t)\) can contain both selected lines and \(p\): the only intersection point \(q=\ell\cap m\) has its third incident line not through \(p\). Hence exactly one incidence is necessary and sufficient. Duality proves the analogous condition for two points and one line. There are \(2(\binom73-7)=56\) pure allowed triples and \(2\cdot7\cdot3\cdot4=168\) mixed ones, totaling \(224\).

**Step 3: deleted quadruples.** Four omitted points satisfy (1) if and only if no three are collinear. In the Fano plane a four-point cap is exactly the complement of a line: its six pairs determine six distinct lines, whose twelve point incidences leave the seventh line disjoint from the four-point set. There are seven such caps, and dually seven four-line configurations.

A split \(1+3\) (one point, three lines) cannot work. At most one of the three omitted lines may contain the omitted point \(p\); select two, \(\ell,m\), that do not. Their intersection \(q\) lies on a third line \(t\) through \(p\), so \(X(q,t)\) contains \(p,\ell,m\), contradicting (1). The dual split \(3+1\) also fails.

For a split \(2+2\), (1) implies that each omitted point lies on at most one omitted line and each omitted line contains at most one omitted point. Thus their incidence relation is a partial matching. If the matching has fewer than two edges, at least one omitted point \(p\) lies outside both omitted lines \(\ell,m\); with \(q=\ell\cap m\), the third line through \(q\), namely \(pq\), shows \(X(q,pq)\) contains \(p,\ell,m\), impossible. Conversely, a perfect matching meets the closed-neighborhood conditions. No four-element set \(X(q,t)\) contains three of its omissions: two omitted lines in \(X(q,t)\) force \(q=\ell\cap m\), and the third line through \(q\) contains neither omitted point; two omitted points in \(X(q,t)\) force \(t\) to be their joining line, and neither omitted line can pass through its remaining point \(q\) without violating the perfect-matching incidence condition. This proves sufficiency. There are \(\binom72\cdot2\cdot2=84\) such configurations: after choosing the two omitted points, each has two lines through it that avoid the other point. Hence the total is \(7+7+84=98\).

**Step 4: no larger deletions and minimality.** Redundancy is monotone under adding detectors, so every subset of a permitted omission set is permitted. A five-element omitted set with both points and lines contains a forbidden four-element split \(1+3\) or \(3+1\), except for a split \(2+3\) or \(3+2\), which also contains such a four-subset. A five-element monochromatic omission contains three collinear points or three concurrent lines because a Fano cap has at most four points. Thus no five omissions work, and none larger can work. Conversely every permitted omitted triple extends to a permitted quadruple: a pure noncollinear triple extends uniquely to a four-point cap, and a mixed triple with exactly one incidence extends by selecting a second point or line to make the \(2+2\) perfect matching. Every permitted zero-, one-, or two-element omission extends similarly (two same-type vertices fit in a cap; an incident or nonincident mixed pair fits in a matching). Therefore only the \(98\) ten-detector codes are inclusion-minimal. The polynomial follows by counts \(\binom{14}{k}\) for \(k\le2\) omitted vertices and the above triple/quadruple counts.

**Step 5: full symmetry.** The Fano collineation group has \(168\) elements, and adjoining a point-line duality gives the entire Heawood automorphism group of order \(336\). It acts transitively on the fourteen cap/dual-cap omissions and on the 84 perfect-matching omissions, as may also be verified by explicitly generating all incidences-preserving permutations (see checker). These are the only two minimum-code orbits.

## Verification

Two different exhaustive checks corroborate the entire finite theorem. `verify_fano.py` uses the cyclic seven-line incidence model and checks all \(2^{14}=16384\) possible deletion masks against both (1) and the independent geometric characterization; it verifies the full polynomial, extension-to-minimality property, and both orbits by constructing \(336\) automorphisms. `verify_direct.cpp` uses nonzero vectors and functionals in \(\mathbb F_2^3\), enumerates all \(16384\) detector subsets, and *directly* checks identifying traces after removing each individual detector, without relying on the symmetric-difference criterion or cyclic Fano model. Its independent results agree on all cardinality counts and all \(98\) inclusion-minimal sets. The checkers require standard Python 3 and a C++17 compiler and can be run with `python3 verify_fano.py` and `g++ -O2 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct`.

## Relationship to prior work

Jean and Seo (arXiv:2112.01685v1, first public 2021-12-03, Theorem 2) introduce and characterize redundant identifying codes and study cubic graphs in general. The general two-domination/two-distinguishing criterion used in Step 1 is credited to them; the specialized four-point Fano deletion classification, the complete polynomial, and two-orbit census are the result here. Their small-cubic-graph computations are a priority risk for the scalar minimum, not a documented matching configuration polynomial in the inspected text. Their distinct later error-correcting and error-detecting notions should not be conflated with one-detector removal.

Balbuena, Foucaud and Hansberg (arXiv:1407.7263, 2014) study identifying codes and locating domination in girth-at-least-five graphs, including the Heawood graph. Their Heawood locating-domination result has a different trace requirement and does not determine redundant identifying codes. A separately published Heawood result enumerates \(268\) *ordinary* minimum identifying codes of size seven and their token-slide graph; the full inspected statement expressly concerns ordinary codes and not the stronger one-failure condition. Another result classifies \(448\) *locating-dominating* sets, again a different condition. Neither known statement implies the count \(98\) or the above omitted-set structure.

## Limitations

The conclusion is an exact finite theorem for the 14-vertex Fano incidence graph, not an all-order theorem for projective-plane incidence graphs. A complete pairwise-trace test proves the finite claim, and two programs reproduce it; these do not constitute an independent scholarly audit. The new part beyond the 2021 general theorem is the particular Heawood/Fano structural classification, polynomial, minimality and orbit refinement. A possible unpublished or unindexed exact census, or a stronger theorem not located by the comparisons, remains a publication-priority risk.

## References

1. D. C. Jean and S. J. Seo, *Fault-tolerant Identifying Codes in Special Classes of Graphs*, arXiv:2112.01685v1 (2021-12-03); *Discussiones Mathematicae Graph Theory* 44 (2024), 591–611. https://arxiv.org/abs/2112.01685 ; https://arxiv.org/pdf/2112.01685
2. C. Balbuena, F. Foucaud and A. Hansberg, *Locating-dominating sets and identifying codes in graphs of girth at least 5*, arXiv:1407.7263 (2014). https://arxiv.org/abs/1407.7263
3. D. C. Jean and S. J. Seo, *Error-correcting Identifying Codes*, arXiv:2204.11362 (2022). https://arxiv.org/abs/2204.11362
4. *The token-slide graph of minimum identifying codes of the Heawood graph is a star forest*, publicly accessible exact graph-specific classification (2026): https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-token-slide-graph-of-minimum-identifying-codes-of-the-heawoo--f9533412f5d1
5. *Four symmetry types and 448 minimum locating-dominating codes of the Heawood graph*, publicly accessible related graph-specific record (2026): https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-four-symmetry-types-and-448-minimum-locating-dominating-codes-of--7539b3d3a7fb
