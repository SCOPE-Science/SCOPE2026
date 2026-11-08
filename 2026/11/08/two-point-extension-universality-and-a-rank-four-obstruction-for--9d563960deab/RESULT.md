# Two-point extension universality and a rank-four obstruction for \(q\)-Kneser graphs

## Finding

Let \(Q(n,k,q)\) be the simple, undirected graph of all \(k\)-dimensional subspaces of \(\mathbb F_q^n\), with an edge between distinct \(U,V\) exactly when \(U\cap V=\{0\}\). Here \(q\) is any prime power at least two and \(1\le k\le n\). In the edge-and-equality language, **exactly four elementary-equivalence classes at quantifier rank at most three** occur:

1. \(k=n\): a singleton.
2. \(k=1<n\): a complete graph with at least three vertices.
3. \(1<k<n<2k\): an edgeless graph with at least three vertices.
4. \(k\ge2\) and \(n\ge2k\): the rank-three theory of the countable Rado graph \(R\).

In case 4, every pair of distinct vertices has a third vertex in each of the four possible adjacency patterns. Nevertheless **no graph in case 4 is three-existentially closed**: a pencil of three subspaces supplies a uniform three-point obstruction. Consequently,

\[
Q(n,k,q)\equiv_3R\quad\text{but}\quad Q(n,k,q)\not\equiv_4R
\]

for all \(k\ge2\) and \(n\ge2k\). The smallest member of this case, ordered by vertex count, is \(Q(4,2,2)\), with \(\genfrac{[}{]}{0pt}{}{4}{2}_2=35\) vertices. Here \(\equiv_r\) means equality of truth values of all first-order sentences of quantifier rank at most \(r\), **not** unrestricted elementary equivalence.

## Assumptions and scope

The field is arbitrary of cardinality a prime power \(q\ge2\). Subspaces are distinct labelled vertices; the edge relation is irreflexive. A graph is **two-existentially closed** if for every two distinct vertices \(u,v\) and every \((\epsilon,\delta)\in\{0,1\}^2\), some third vertex is adjacent to \(u\) precisely when \(\epsilon=1\), and to \(v\) precisely when \(\delta=1\). Three-existential closure makes the analogous demand for triples and every prescribed pattern. The countable Rado graph realizes every finite adjacency pattern.

For \(k=n\), only the full space occurs. For \(k=1<n\), different lines intersect trivially, and there are at least \(q+1\ge3\) lines. If \(1<k<n<2k\), two distinct \(k\)-subspaces always intersect nontrivially since \(\dim(U\cap V)\ge2k-n>0\). There are at least three distinct such subspaces (already at \(n=k+1\), the number of hyperplanes is at least seven). These observations classify the three degenerate cases.

## Proof

**Two-point extension in the disjointness regime.** Fix \(k\ge2\), \(n\ge2k\), and distinct \(k\)-subspaces \(U,V\). Let \(X=U\cap V\) have dimension \(t\), where \(0\le t<k\). Choose complementary subspaces \(A\subset U\), \(B\subset V\) so \(U=X\oplus A\), \(V=X\oplus B\) and \(U+V=X\oplus A\oplus B\). An ambient complement to \(U+V\) has dimension \(n-2k+t\ge t\).

For the pattern adjacent to **both**, select a \(t\)-space \(Y\) in that ambient complement and linear isomorphisms \(f:X\to Y\), \(g:A\to B\). The \(k\)-space

\[
C=\{x+f(x):x\in X\}\oplus\{a+g(a):a\in A\}
\]

has trivial intersection with both \(U\) and \(V\), by comparing components in the displayed direct-sum decomposition. When \(t=0\), the first summand is zero and the construction remains valid.

For the pattern adjacent to \(U\) but **not** to \(V\), choose \(0\ne v\in V\setminus U\). As \(\dim(\mathbb F_q^n/U)=n-k\ge k\), extend \(v+U\) to an independent \(k\)-tuple of quotient vectors and lift it to a \(k\)-space \(C\) containing \(v\). Linear independence modulo \(U\) yields \(C\cap U=0\); containment of \(v\) gives \(C\cap V\ne0\). If \(U\cap V\ne0\), then automatically \(C\ne V\). If \(U\cap V=0\) and the chosen lifts happened to span \(V\), modify one of the other \(k-1\) lifts by adding a nonzero vector of \(U\). This preserves independence modulo \(U\) and inclusion of \(v\), but makes \(C\ne V\); it is possible since \(k\ge2\). The reverse pattern follows by interchanging \(U,V\).

For the pattern adjacent to **neither**, when \(t>0\) choose nonzero \(x\in X\) and \(z\notin U+V\); such \(z\) exists because \(n\ge2k>2k-t=\dim(U+V)\). Extend \(\operatorname{span}(x,z)\) to a \(k\)-space \(C\). It intersects both \(U,V\) and differs from each by containing \(z\). If \(t=0\), choose nonzero \(u\in U\) and \(v\in V\); extend \(\operatorname{span}(u,v)\) to a \(k\)-space. It intersects both and is distinct from both. Thus all four patterns have proper witnesses, establishing two-existential closure.

**Logical consequences.** In a three-move Ehrenfeucht–Fraïssé game on any two graphs satisfying the two-point extension property, Duplicator preserves the equality and adjacency pattern of the selected vertices: at each move, choose a fresh vertex with the required adjacency to the at most two previously selected distinct vertices. For zero or one previous vertex, either complete a pair first or note that the two-point property supplies both a neighbor and a nonneighbor. Hence all such graphs are \(\equiv_3\), including \(R\). Each of the other three cases has a different rank-three theory: a singleton is distinguishable by the existence of two distinct vertices; complete and edgeless graphs of size at least three are distinguished by the existence of an edge; the fourth case contains both edges and nonedges. This also shows there are exactly four classes.

**Uniform three-point obstruction.** Take a \((k-1)\)-subspace \(L\) lying in a \((k+1)\)-subspace \(H\), and select three distinct intermediate \(k\)-spaces \(U,V,W\) with \(L\subset U,V,W\subset H\). There are \(q+1\ge3\) such spaces, and their pairwise intersections equal \(L\), so they form a nonadjacent triple. Suppose a \(k\)-space \(C\) were disjoint from \(U\) while meeting both \(V\) and \(W\) nontrivially. Pick nonzero \(v\in C\cap V\), \(w\in C\cap W\). Both are outside \(U\), since \(C\cap U=0\). In the one-dimensional quotient \(H/U\), their nonzero images are dependent, so a nontrivial linear combination \(av+bw\) lies in \(U\). The vectors \(v,w\) are linearly independent: dependence would put them both in \(V\cap W=L\subset U\), impossible. Thus \(0\ne av+bw\in C\cap U\), a contradiction. Therefore the demanded adjacency pattern cannot be realized.

An explicit rank-four separator, true in \(R\) but false in every graph in case 4, is the assertion that every three pairwise distinct, pairwise nonadjacent vertices \(x,y,z\) have a fourth, distinct vertex \(w\) satisfying \(E(w,x)\), \(\neg E(w,y)\), \(\neg E(w,z)\). Its prenex prefix is \(\forall x\forall y\forall z\exists w\), so its quantifier rank is four. The Rado graph satisfies it by the full finite extension property; the displayed pencil refutes it in \(Q(n,k,q)\).

**Smallest witness.** In the case-4 parameter range, \(k\ge2\), \(n\ge2k\), \(q\ge2\). The number of vertices is the Gaussian binomial coefficient \(\genfrac{[}{]}{0pt}{}{n}{k}_q\), minimized at \((n,k,q)=(4,2,2)\). Indeed increasing \(n\) or \(q\) increases the number of \(k\)-subspaces, and at \(n=2k\) the Gaussian binomial count increases with \(k\ge2\), as follows directly by injection of \(k\)-subspaces into the \((k+1)\)-subspaces of an extended \((2k+2)\)-space with a new fixed point plus a strict additional family. The boundary value is \((15\cdot7)/(3\cdot1)=35\).

## Verification

The bundled standalone `checker.py` independently constructs all subspaces over the prime fields of orders two and three, checks the four extension patterns for every pair in \(Q(4,2,2)\), \(Q(5,2,2)\), and \(Q(4,2,3)\), and checks explicit pencil obstructions. It additionally checks 40 deterministically chosen pairs and an explicit pencil in \(Q(6,3,2)\). Run `python checker.py` from the extracted package; the terminating marker is `Q_KNESER_FINITE_CHECKS_OK`. The first three cases inspect every pair, but the fourth is a sample and none of these finite checks replaces the field-uniform proof above.

## Relationship to prior work

Benediktsson, Macpherson and Adler [1] study the model theory of Johnson adjacency graphs and discuss the analogous Grassmannian structures as a direction. Blokhuis, Brouwer and Szőnyi [2] treat the same \(q\)-Kneser disjointness graph, mainly its chromatic number and maximal cocliques. Chowdhury, Godsil and Royle [4] study all parameters and note explicitly that the common-neighbor set of several subspaces does not depend only on their join; their emphasis remains proper colorings and homomorphisms. Glasby, Niemeyer and Praeger [3] study a bipartite \(q\)-Kneser construction and its closed-walk probabilities, rather than local first-order extension types. These inspected texts do not state the all-rank two-extension law or the rank-four pencil obstruction.

The rank-three case \(k=2\) is **not claimed as separately novel**: the disjointness graph of two-dimensional subspaces is the graph complement of the Grassmann adjacency graph on the same vertices, and an earlier bounded-depth classification of Grassmann adjacency implies its rank-three classification. The substantive additional scope here is all \(k\ge3\) with sharp \(n=2k\) threshold and the uniform rank-four failure. The analogous ordinary (set-based) Kneser extension threshold follows different set-union inequalities. The present argument uses subspace quotients and pencils, not simple replacement of set cardinalities with vector dimensions.

## Limitations

This is a rank-three classification plus a rank-four obstruction, not a classification of all rank-four theories or the full elementary theories. The checker covers prime fields of order two or three and finitely many parameters; the proof is independent of these experiments and applies to every finite field. Literature comparisons cannot establish global historical priority; specialist finite-geometry or existential-closure papers may contain equivalent results. The work has undergone self-review only, not independent mathematical audit.

## References

[1] B. G. Benediktsson, D. Macpherson, I. Adler, *Model Theory of Johnson Graphs*, arXiv:2610.40054v1, first public 2026-10-29, https://arxiv.org/abs/2610.40054.

[2] A. Blokhuis, A. E. Brouwer, T. Szőnyi, *On the chromatic number of q-Kneser graphs*, *Designs, Codes and Cryptography* **65** (2012), 187–197, first online 2011-05-10, DOI 10.1007/s10623-011-9513-1.

[3] S. P. Glasby, A. C. Niemeyer, C. E. Praeger, *Bipartite q-Kneser graphs and two-generated irreducible linear groups*, arXiv:2312.05529, first public 2023-12-09, https://arxiv.org/abs/2312.05529.

[4] A. Chowdhury, C. Godsil, G. Royle, *Colouring Lines in Projective Space*, arXiv:math/0507319v1, first public 2005-07-15, https://arxiv.org/abs/math/0507319.
