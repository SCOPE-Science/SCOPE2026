# General position polynomial and maximal-set structure of double stars
## Finding
Let \(D_{a,b}\), with \(a,b\ge2\), be the double star with adjacent centers \(u,v\), \(a\) leaves \(A\) adjacent to \(u\), and \(b\) leaves \(B\) adjacent to \(v\). Its general position polynomial is \[\psi(D_{a,b};x)=(1+x)^{a+b}+x(1+x)^a+x(1+x)^b+(a+b+1)x^2.\] The maximal general position sets are exactly \(A\cup B\), \({u}\cup B\), \({v}\cup A\), the \(a\) sets \({u,a_i}\), the \(b\) sets \({v,b_j}\), and \({u,v}\). Consequently \(\operatorname{gp}(D_{a,b})=a+b\), the leaf set \(A\cup B\) is the unique maximum general position set, there are exactly \(a+b+4\) maximal general position sets, and \(\psi(D_{a,b};1)=2^{a+b}+2^a+2^b+a+b+1\).

## Assumptions and scope
All graphs are finite, simple, and connected. For integers \(a,b\ge2\), let \(D_{a,b}\) be the tree with adjacent centers \(u,v\), leaf set \(A=\{a_1,\ldots,a_a\}\) adjacent to \(u\), and leaf set \(B=\{b_1,\ldots,b_b\}\) adjacent to \(v\).

A vertex set \(S\) is in general position when no three vertices of \(S\) lie on a common geodesic with one of them between the other two. The general position polynomial is
\[
\psi(G;x)=\sum_{S\text{ in general position}}x^{|S|}.
\]

## Proof
Because \(D_{a,b}\) is a tree, every pair of vertices has a unique geodesic. We classify general position sets according to their intersection with the two centers.

If neither \(u\) nor \(v\) belongs to \(S\), then \(S\subseteq A\cup B\). Any geodesic between two selected leaves has only centers as internal vertices, so none of its internal vertices lies in \(S\). Hence every subset of \(A\cup B\) is in general position. These sets contribute
\[
(1+x)^{a+b}.
\]

Suppose \(u\in S\) and \(v\notin S\). If \(S\) contains two leaves of \(A\), then \(u\) is the internal vertex on their length-two geodesic, so \(S\) is not in general position. If \(S\) contains one leaf of \(A\) and one leaf of \(B\), then \(u\) lies internally on the unique geodesic joining those leaves, again violating general position. Conversely, if \(S\cap A=\varnothing\), then \(u\) may be combined with an arbitrary subset of \(B\); and if \(S\cap B=\varnothing\), then \(u\) may be combined with at most one leaf of \(A\). Thus the sets containing \(u\) but not \(v\) contribute
\[
x(1+x)^b+a x^2.
\]
By symmetry, the sets containing \(v\) but not \(u\) contribute
\[
x(1+x)^a+b x^2.
\]

Finally, if both centers lie in \(S\), then no leaf can be added: for a leaf at either side, one of the selected centers lies internally on the geodesic from that leaf to the opposite center. Hence the only such set is \(\{u,v\}\), contributing \(x^2\).

Adding the four disjoint cases gives
\[
\psi(D_{a,b};x)=(1+x)^{a+b}+x(1+x)^a+x(1+x)^b+(a+b+1)x^2.
\]

The same classification identifies inclusion-maximal general position sets. In the center-free case, maximality forces all leaves, giving \(A\cup B\). In the \(u\)-only case, maximality gives either \(\{u\}\cup B\) or \(\{u,a_i\}\) for one leaf \(a_i\in A\); the symmetric alternatives are \(\{v\}\cup A\) and \(\{v,b_j\}\). With both centers selected, \(\{u,v\}\) is maximal. These are all maximal sets, so their number is \(a+b+4\).

Since \(a,b\ge2\), the all-leaf set has size \(a+b\), while every other maximal set has size at most \(\max\{a+1,b+1\}<a+b\). Therefore
\[
\operatorname{gp}(D_{a,b})=a+b,
\]
and the maximum set is unique. Evaluating the polynomial at \(x=1\) gives
\[
\psi(D_{a,b};1)=2^{a+b}+2^a+2^b+a+b+1.
\]

## Verification
The included checker constructs each double star directly for \(2\le a,b\le7\), computes all-pairs distances by breadth-first search, and tests every vertex subset against the defining three-vertex geodesic condition. It does not use the closed formula to decide whether a subset is in general position.

It independently compares the complete coefficient vector with the formula, enumerates all inclusion-maximal general position sets, and checks the general position number, uniqueness of the maximum set, and total count.

## Relationship to prior work
The 2024 paper introducing the general position polynomial develops exact formulas for several standard graph families and operations and shows that tree polynomials already exhibit nontrivial behavior through brooms and combs. Targeted full-text searches in that paper found no double-star or bistar treatment.

An earlier 2020 paper on general position numbers of complementary prisms uses a double star as an example in a complementary-prism argument, so double stars are not new objects in the general-position literature; however, that work concerns the extremal number rather than the all-set counting polynomial. A 2026 paper on explicit general position polynomial formulas treats complete multipartite graphs and coronas and likewise contains no double-star or bistar formula in targeted full-text searches.

The present theorem supplies the complete size enumerator and the full inclusion-maximal-set structure for the diameter-three double-star family.

## Limitations
The theorem concerns ordinary general position sets in double stars with at least two leaves at each center. The cases with one side of size one merge into spider-tree behavior and are intentionally excluded. The finite exhaustive checks are corroborative only; the all-parameter theorem follows from the case classification above. Literature search cannot rule out a differently named or non-indexed equivalent formula.

## References
1. V. Iršič, S. Klavžar, G. Rus, J. Tuite, “General position polynomials,” arXiv:2401.05696v1, 11 January 2024; Results in Mathematics 79 (2024), DOI 10.1007/s00025-024-02133-3.
2. P. K. Neethu, S. V. Ullas Chandran, M. Changat, S. Klavžar, “On the general position number of complementary prisms,” arXiv:2001.02189v1, 7 January 2020.
3. B. A. Rather, “Explicit Formulas and Unimodality Phenomena for General Position Polynomials,” arXiv:2603.06930v1, 6 March 2026.
