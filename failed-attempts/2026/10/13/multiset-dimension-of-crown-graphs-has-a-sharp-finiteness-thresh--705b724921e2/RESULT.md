# Multiset dimension of crown graphs has a sharp finiteness threshold
## Finding
Let
\[
\operatorname{Cr}_n=K_{n,n}-M,\qquad n\ge3,
\]
be the crown graph with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
where
\[
M=\{a_i b_i:1\le i\le n\}
\]
is the deleted perfect matching. Then
\[
\operatorname{md}(\operatorname{Cr}_n)=
\begin{cases}
3,&n=3,\\
\infty,&n\ge4.
\end{cases}
\]

The finite boundary is completely classified. For
\[
\operatorname{Cr}_3\cong C_6,
\]
there are exactly twelve multiset resolving sets, and every one has size \(3\).

For \(W\subseteq V(\operatorname{Cr}_3)\), put
\[
x_i=\mathbf 1_{\{a_i\in W\}},\qquad
y_i=\mathbf 1_{\{b_i\in W\}}.
\]
Then \(W\) is multiset resolving exactly when the three pairs \((x_i,y_i)\) are one of
\[
\{(0,0),(1,0),(1,1)\},
\qquad
\{(0,0),(0,1),(1,1)\}.
\]
Each pattern collection can be assigned to the three indices in \(3!\) ways, giving exactly
\[
12
\]
resolving sets.

## Assumptions and scope
Graphs are finite, simple, connected, and undirected. For \(W\subseteq V(G)\), the multiset representation of \(v\) is
\[
r_m(v\mid W)=\{\!\{d(v,w):w\in W\}\!\}.
\]
A set \(W\) is multiset resolving when all vertex representations are pairwise distinct. If no such set exists, the multiset dimension is infinite.

The connected crown family begins at \(n=3\); \(\operatorname{Cr}_2\) is disconnected and is outside the claim.

## Proof
Fix \(W\subseteq V(\operatorname{Cr}_n)\). Let
\[
p=|W\cap A|,\qquad q=|W\cap B|,
\]
and define
\[
x_i=\mathbf 1_{\{a_i\in W\}},\qquad y_i=\mathbf 1_{\{b_i\in W\}}.
\]

Crown distances are
\[
d(a_i,a_j)=2\quad(i\ne j),\qquad
d(b_i,b_j)=2\quad(i\ne j),
\]
\[
d(a_i,b_j)=1\quad(i\ne j),\qquad
d(a_i,b_i)=3.
\]

Hence \(r_m(a_i\mid W)\) contains \(x_i\) zeros, \(q-y_i\) ones, \(p-x_i\) twos, and \(y_i\) threes. Thus, for fixed \(p,q\),
\[
r_m(a_i\mid W)=r_m(a_j\mid W)
\quad\Longleftrightarrow\quad
(x_i,y_i)=(x_j,y_j).
\tag{1}
\]
The analogous statement holds among the \(B\)-vertices. Therefore all \(n\) membership pairs must be distinct. Since only four binary pairs exist,
\[
n\le4
\]
for any multiset resolving crown graph. Thus every \(\operatorname{Cr}_n\) with \(n\ge5\) has infinite multiset dimension.

Now let \(n=4\). A hypothetical resolving set would have to use all four patterns
\[
(0,0),(0,1),(1,0),(1,1),
\]
so \(p=q=2\). At the unique \((0,0)\) index \(i\), neither \(a_i\) nor \(b_i\) lies in \(W\), and both have representation
\[
\{\!\{1,1,2,2\}\!\}.
\]
This contradiction proves
\[
\operatorname{md}(\operatorname{Cr}_4)=\infty.
\]

Finally let \(n=3\). Three distinct membership patterns must be chosen from the four binary pairs. The collection
\[
\{(0,0),(0,1),(1,0)\}
\]
has size \(2\), and the matched vertices at the \((0,0)\) index have equal representation. The collection
\[
\{(0,1),(1,0),(1,1)\}
\]
has size \(4\), and the matched vertices at the \((1,1)\) index have equal representation.

The remaining two collections both have size \(3\). For
\[
\{(0,0),(1,0),(1,1)\},
\]
we have \(p=2\), \(q=1\). The three \(A\)-representations are
\[
\{\!\{1,2,2\}\!\},\quad
\{\!\{0,1,2\}\!\},\quad
\{\!\{0,2,3\}\!\},
\]
and the three \(B\)-representations are
\[
\{\!\{1,1,2\}\!\},\quad
\{\!\{1,2,3\}\!\},\quad
\{\!\{0,1,3\}\!\}.
\]
All six are distinct. Interchanging the bipartition classes proves the same for
\[
\{(0,0),(0,1),(1,1)\}.
\]
Thus exactly these two pattern collections work. Each has \(3!\) assignments to the index set, yielding twelve resolving sets.

## Verification
The included checker constructs every crown graph with
\[
3\le n\le8,
\]
computes all-pairs shortest-path distances by breadth-first search, enumerates every vertex subset, and compares the direct multiset-resolving test with the membership-pattern theorem.

It confirms exactly twelve resolving sets for \(\operatorname{Cr}_3\), all of size \(3\), and no resolving set for every tested \(\operatorname{Cr}_n\) with \(4\le n\le8\).

## Relationship to prior work
Multiset dimension was introduced in 2017. The foundational paper proves \(\operatorname{md}(C_n)=3\) for cycles of length at least \(6\), so the scalar value
\[
\operatorname{md}(\operatorname{Cr}_3)=3
\]
is already known through \(\operatorname{Cr}_3\cong C_6\). The same paper gives general infinite-dimension obstructions for diameter at most \(2\) and for large twin classes, neither of which applies to crown graphs with \(n\ge3\).

A 2024 primary paper proves that multiset resolving sets are exactly ID-colorings, establishes NP-completeness, and studies king grids and strong products. Its searchable full text contains no crown or complete-bipartite occurrence.

A 2026 preprint reports a large finite census and new king-grid results. Its accessible abstract does not state a crown theorem; its full text was not available in the comparison. Its finite census may include small crown instances, but this does not imply the arbitrary-\(n\) structural result above.

The new content here is the sharp crown-family threshold
\[
n=3\text{ finite},\qquad n\ge4\text{ infinite},
\]
together with the complete classification of the twelve resolving sets in the finite boundary case.

## Limitations
The result concerns ordinary multiset dimension, not outer, local, edge, or ordered metric variants.

The scalar value at \(n=3\) is prior work and is not claimed as new. The new contribution is the arbitrary-\(n\) finiteness threshold and the complete boundary classification.

The finite computation through \(n=8\) is corroborative only. The all-\(n\) proof is the four-pattern argument plus the \(n=4\) cross-part collision.

A differently phrased or non-indexed crown theorem may exist. The unavailable full text of the 2026 census remains a residual literature-comparison risk.

## References
1. R. Simanjuntak, P. Siagian, T. Vetrík, “The multiset dimension of graphs,” arXiv:1711.00225v1, 1 November 2017.
2. N. H. Bong, Y. Lin, “Some properties of the multiset dimension of graphs,” Electronic Journal of Graph Theory and Applications 9 (2021), DOI 10.5614/ejgta.2021.9.1.19.
3. A. Hakanen, I. G. Yero, “Complexity and Equivalency of Multiset Dimension and ID-colorings,” Fundamenta Informaticae 191 (2024), 315–330, DOI 10.3233/FI-242185.
4. J. Allikvere, “The Multiset Dimension of Graphs: Extremal Values and King Grids,” arXiv:2607.28813v1, 30 July 2026.
