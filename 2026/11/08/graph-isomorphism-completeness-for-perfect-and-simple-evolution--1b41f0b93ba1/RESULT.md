# Graph-isomorphism completeness for simple evolution algebras over a fixed finite field

## Finding

Fix a prime power \(q\ge2\). Graph isomorphism reduces in deterministic polynomial time to isomorphism of **simple** evolution algebras over \(\mathbb F_q\), supplied by their natural-basis structure matrices. For an \(n\)-vertex input graph with \(n\ge1\), the reduction constructs a \((4n+6)\)-dimensional algebra with all structure constants in \(\{0,1\}\). The construction gives simple algebras over every field, and over each field it preserves and reflects graph isomorphism. The known upper reduction for perfect evolution algebras applies to simple algebras, giving GI-completeness on this promise over each fixed finite field.

## Assumptions and scope

All graphs used as inputs are finite, undirected and simple. An evolution algebra over a field \(K\) has a natural basis \(e_i\) with \(e_ie_j=0\) for \(i\ne j\); its row structure matrix \(A=(a_{ij})\) satisfies \(e_i^2=\sum_j a_{ij}e_j\). Isomorphisms are \(K\)-linear. Perfect means \(E^2=E\), equivalently \(A\) is invertible. Simple means \(E^2\ne0\) and there are no nonzero proper ideals. The lower reduction does not require a finite field; the upper reduction is used only with a finite field fixed outside the input.

## Proof

**Monomial isomorphisms.** Suppose \(E(A)\cong E(B)\) are perfect and \(\varphi(e_i)=\sum_k p_{ik}f_k\). For distinct \(i,j\), multiplying their images gives \(\sum_k p_{ik}p_{jk} f_k^2=0\). The \(f_k^2\) are a basis, so each column of the invertible \(P=(p_{ik})\) has exactly one nonzero entry, as does each row. Therefore \(\varphi(e_i)=s_i f_{\sigma(i)}\) for a permutation \(\sigma\) and \(s_i\ne0\). Such a map is an isomorphism exactly when
\[
a_{ij}s_j=s_i^2 b_{\sigma(i),\sigma(j)} \qquad\text{for all }i,j.
\tag{1}
\]
In particular the directed support of the structure matrix, including its diagonal, is preserved and reflected.

**Faithful connected graph encoding.** From \(G\) on \(n\ge1\) vertices, form \(H(G)\) by adding a hub adjacent to all old vertices and to \(n+2\) new leaves, with no other new edges. This connected graph has \(m=2n+3\) vertices. Its unique hub has degree \(2n+2\), compared with at most \(n\) at any other vertex. The induced graph on the nonhub vertices of degree at least two is precisely \(G\) with its isolated vertices removed. The number of removed isolates is determined by \(n=(m-3)/2\) and the size of the recovered graph. Thus \(G\cong G'\) if and only if \(H(G)\cong H(G')\); forward isomorphisms are extended by mapping hubs to hubs and new leaves bijectively.

**Simple-algebra gadget.** Given a connected graph \(H\) on \(m\ge1\) vertices with adjacency matrix \(C\), take natural basis vectors \(x_v,y_v\) and products
\[
x_v^2=x_v+\sum_{w\sim v}x_w+y_v,\qquad y_v^2=x_v.
\]
The matrix in the order \(x\) then \(y\) is
\[
M_H=\begin{pmatrix}I_m+C&I_m\\ I_m&0\end{pmatrix}.
\]
Its kernel over any field is zero: the bottom equation forces the first coordinate block to vanish, and the top forces the second. Its multiplication digraph (arc \(i\to j\) for a nonzero \(a_{ij}\)) is strongly connected, since the \(x\)-vertices induce the bidirected connected graph \(H\) with loops and each pair \(x_v,y_v\) is joined in both directions. To see simplicity, take a nonzero element of an ideal and multiply by a basis vector at a nonzero coordinate. This puts the corresponding basis square into the ideal. Whenever the square of basis vector \(i\) lies in the ideal and \(i\to j\), multiplying that square by basis vector \(j\) gives a nonzero scalar times the square of \(j\). All basis squares lie in the ideal by strong connectivity, and span the algebra by perfection.

An isomorphism of graphs \(H\to H'\) induces the same permutation of \(x\)- and \(y\)-vectors and preserves all products. Conversely, any algebra isomorphism is monomial by (1). The \(x\)-vectors are exactly the vertices with a loop, and the off-diagonal arcs induced on them encode exactly the edges of \(H\). Consequently the induced permutation on the \(x\)-vectors is an isomorphism \(H\to H'\). Combining this with the hub encoding gives \(E_G=E_{H(G)}\) of dimension \(2m=4n+6\). If input graphs of order zero are allowed, map the empty graph separately to the one-dimensional algebra with \(e^2=e\), which is simple and is not isomorphic to any positive-order image. The construction of the structure matrix is polynomial in the size of the graph input.

**Upper bound over a fixed finite field.** For completeness, the finite-field reduction for the perfect case is as follows. Simplicity implies perfection since \(E^2\) is a nonzero ideal (the product of any vector with a vector in \(E^2\) is again a product of two vectors in \(E\)). Fix a generator \(g\) of \(\mathbb F_q^\times\). Use vertices \((i,t)\) with \(t\in\mathbb F_q^\times\) and two separate directed arc relations: one contains \((i,t)\to(i,gt)\); the other contains \((i,t)\to(j,t^2a_{ij})\) for each nonzero \(a_{ij}\). The first relation forces isomorphisms to take the form \((i,t)\mapsto(\sigma(i),ts_i)\), also when \(q=2\) and the cycles are singleton loops. The second relation enforces exactly (1): arcs at \(t=1\) enforce it on the nonzero coefficients and preservation of the relation enforces the zero pattern; (1) suffices at every \(t\). There are \(n(q-1)\) vertices and at most \((n+n^2)(q-1)\) arcs.

To remove colors and directions, replace each arc by a length-three path with two fresh vertices having distinct tail and head colors for that arc relation. Give the original vertices a fifth color. Loops become triangles with the two new colors; simultaneous arcs use distinct fresh vertices. This is a faithful encoding in vertex-colored undirected simple graphs. To remove the vertex colors, attach a distinct number of pendant leaves (at least two) for each color. The old vertices are exactly those of degree at least two in the final graph; the number of degree-one neighbors recovers their colors. This proves a polynomial upper bound for fixed \(q\).

## Verification

The proof establishes the result over the entire stated domain. The accompanying `checker.py` gives bounded corroboration: it tests the two-relation upper encoding against the monomial equations on all invertible \(2\)-by-\(2\) matrices over \(\mathbb F_2\) and \(\mathbb F_3\) and a fixed sample over \(\mathbb F_4\). On the lower side it checks invertibility in characteristics two and three, connectivity and graph recovery on the 75 labelled input graphs of orders one through four. The recorded output is in `verification_output.txt`. The checker does not prove the polynomial bound, all-characteristic simplicity, or the reductions for arbitrary dimensions.

## Relationship to prior work and limitations

The contribution is the lower reduction **under the algebraically simple promise**, not the perfect-algebra GI-completeness result, the finite-field upper encoding, or monomial rigidity. Costoya, Ligouras, Tocino and Viruel give a pairwise isomorphism-preserving reduction to regular (perfect) evolution algebras over every field, not just an automorphism-group construction. Their Definition 3.2 has vertex basis elements \(b_v\) with \(b_v^2=b_v\); whenever the dimension exceeds one, \(K b_v\) is a nonzero proper ideal, so that construction does not furnish the simple-algebra hardness reduction. The earlier perfect-algebra GI-completeness record gives the fixed-field upper reduction with two directed relations; its perfect lower-bound construction is not needed here. The survey's Question 50 concerns the perfect case. The total-colored graph construction of Falcón, Falcón and Núñez addresses isotopisms and uses vectors of the full algebra, not a polynomial-size isomorphism reduction of the form used for the upper bound. No priority assertion is made beyond these comparisons. The result does not treat fields varying with the input, semilinear isomorphisms or the problem of finding a natural basis from an arbitrary multiplication table.

## References

1. C. Costoya, P. Ligouras, A. Tocino and A. Viruel, *Regular evolution algebras are universally finite*, [arXiv:2002.03338v3](https://arxiv.org/abs/2002.03338v3), Definition 3.2, Theorem 3.1 and Lemma 3.6.
2. *Graph-isomorphism completeness of perfect evolution-algebra isomorphism*, [Resultary 58409c6864d5](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-graph-isomorphism-completeness-of-perfect-evolution-algebra-isom--58409c6864d5).
3. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, [arXiv:2610.22248v1](https://arxiv.org/abs/2610.22248v1), Theorems 4 and 6 and Question 50.
4. A. Elduque and A. Labra, *Evolution algebras and graphs*, [arXiv:1312.4685](https://arxiv.org/abs/1312.4685); *Evolution algebras, automorphisms, and graphs*, [arXiv:1902.02191](https://arxiv.org/abs/1902.02191).
5. R. M. Falcón, Ó. J. Falcón and J. Núñez, *An Application of Total-Colored Graphs to Describe Mutations in Non-Mendelian Genetics*, *Mathematics* 7 (2019), 1068, DOI:10.3390/math7111068.
