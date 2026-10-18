# Zero forcing polynomial of the subgroup-intersection pineapple for \(C_{p^2}\times C_p\)

## Finding

Let \(p\) be a prime and let
\[
H=C_{p^2}\times C_p.
\]
For the intersection graph \(\Gamma(H)\) on the proper nontrivial subgroups of \(H\), two vertices being adjacent exactly when their intersection is nontrivial, one has
\[
\mathcal Z(\Gamma(H);u)
=
u^{2p-1}(u+p)(u+p+1)(u+1).
\]
Equivalently, a vertex set is zero forcing exactly when its white complement contains at most one pendant order-\(p\) subgroup and at most one noncentral clique vertex; the center may independently be white or blue. Hence
\[
Z(\Gamma(H))=2p-1,
\]
and there are exactly
\[
p(p+1)
\]
minimum zero forcing sets.

The graph itself is the \((p+2,p)\)-pineapple. A known theorem for pineapple graphs therefore also gives, over every field,
\[
\operatorname{mr}(\Gamma(H))=3,
\qquad
M(\Gamma(H))=2p-1.
\]
The minimum-rank statement is prior coverage; the new content here is the subgroup-lattice identification together with the complete zero forcing set classification and polynomial.

## Assumptions and scope

The intersection graph used here has all proper nontrivial subgroups as vertices, and distinct subgroups are adjacent when their intersection is not the trivial subgroup.

Put
\[
E=H[p]=\{x\in H:px=0\}
\]
and
\[
P=pC_{p^2}\times\{0\}.
\]
Then \(E\cong C_p^2\) and \(P\) is a line in \(E\).

## Proof

Every proper nontrivial subgroup of a group of order \(p^3\) has order \(p\) or \(p^2\).

The order-\(p\) subgroups are exactly the one-dimensional subspaces of
\[
E\cong \mathbb F_p^2,
\]
so there are \(p+1\) of them.

There is exactly one elementary abelian subgroup of order \(p^2\), namely \(E\). The remaining order-\(p^2\) subgroups are cyclic. The number of elements of order \(p^2\) in \(H\) is
\[
p^2(p-1).
\]
Each cyclic subgroup of order \(p^2\) contributes
\[
\varphi(p^2)=p(p-1)
\]
generators, so there are exactly \(p\) cyclic subgroups of order \(p^2\). Every one of them has the same unique order-\(p\) subgroup \(P\).

Thus \(\Gamma(H)\) has
\[
(p+1)+(p+1)=2p+2
\]
vertices. The vertices
\[
E,\quad P,\quad\text{and the \(p\) cyclic order-\(p^2\) subgroups}
\]
form a clique of size \(p+2\): \(E\) meets every one of them nontrivially, and all cyclic order-\(p^2\) subgroups contain \(P\).

Each of the remaining \(p\) order-\(p\) subgroups \(L\ne P\) lies in \(E\), so it is adjacent to \(E\). It intersects \(P\), every cyclic order-\(p^2\) subgroup, and every other such line trivially. Hence these \(p\) vertices are pendant leaves at \(E\). Therefore
\[
\Gamma(H)\cong P_{p+2,p},
\]
the pineapple formed by attaching \(p\) leaves to one vertex of \(K_{p+2}\).

Write \(c=E\), let \(Q\) be the \(p+1\) clique vertices other than \(c\), and let \(L\) be the \(p\) leaves.

Suppose a coloring leaves two vertices of \(L\) white. Only \(c\) is adjacent to either leaf, so neither of those two white leaves can ever be the unique white neighbor of a blue vertex. Thus no zero forcing set can leave two leaves white.

Likewise, suppose at least two vertices of \(Q\) are white. Every vertex of \(Q\) has the same clique neighborhood \(Q\cup\{c\}\) after deleting itself, and \(c\) is adjacent to all of \(Q\). No force can reduce two white vertices of \(Q\) to one. Thus a zero forcing set leaves at most one member of \(Q\) white.

Conversely, assume the white set \(W\) satisfies
\[
|W\cap L|\le1,
\qquad
|W\cap Q|\le1.
\]
If \(c\) is white, then because \(p\ge2\), at least one leaf is blue and immediately forces \(c\). Once \(c\) is blue, if a member of \(Q\) is white, any blue member of \(Q\) forces it. Finally, if one leaf is white, \(c\) forces that leaf. If \(c\) starts blue, the same last two steps apply. Hence these two inequalities are also sufficient.

Therefore the white-complement enumerator is
\[
(1+pt)(1+(p+1)t)(1+t).
\]
Since \(|V(\Gamma(H))|=2p+2\), reversing white size to blue size yields
\[
\mathcal Z(\Gamma(H);u)
=
u^{2p+2}
\left(1+\frac p u\right)
\left(1+\frac{p+1}{u}\right)
\left(1+\frac1u\right),
\]
which is
\[
\mathcal Z(\Gamma(H);u)
=
u^{2p-1}(u+p)(u+p+1)(u+1).
\]

The least exponent is \(2p-1\). A minimum zero forcing set therefore leaves exactly three white vertices: \(c\), one of the \(p\) leaves, and one of the \(p+1\) vertices of \(Q\). Hence there are exactly
\[
p(p+1)
\]
minimum zero forcing sets.

DeAlba, Grout, Hogben, Mikkelson, and Rasmussen proved that every pineapple \(P_{m,k}\), with \(m\ge3\) and \(k\ge2\), has field-independent minimum rank \(3\). Applying that prior theorem to \(P_{p+2,p}\) gives
\[
\operatorname{mr}(\Gamma(H))=3
\]
over every field. Since the graph has \(2p+2\) vertices,
\[
M(\Gamma(H))=2p-1=Z(\Gamma(H)).
\]

## Verification

The accompanying `verify.py` was read from its packaged path before replay.

For
\[
p\in\{2,3,5,7\},
\]
it constructs the abstract pineapple graph, enumerates every vertex subset, verifies the stated necessary-and-sufficient white-complement criterion, reproduces the complete polynomial, and counts exactly \(p(p+1)\) minimum zero forcing sets.

For \(p=2\) and \(p=3\), it separately constructs \(C_{p^2}\times C_p\) as an additive group, generates all subgroups from pairs of generators, removes the trivial and whole subgroups, and verifies directly that there are \(p+1\) order-\(p\) and \(p+1\) order-\(p^2\) vertices with the pineapple degree/intersection pattern.

Exact replay output:

```text
p=2: abstract polynomial {3: 6, 4: 11, 5: 6, 6: 1}; minimum sets=6
p=3: abstract polynomial {5: 12, 6: 19, 7: 8, 8: 1}; minimum sets=12
p=5: abstract polynomial {9: 30, 10: 41, 11: 12, 12: 1}; minimum sets=30
p=7: abstract polynomial {13: 56, 14: 71, 15: 16, 16: 1}; minimum sets=56
p=2: actual subgroup census {2: 3, 4: 3}; degrees=[1, 1, 3, 3, 3, 5]
p=3: actual subgroup census {9: 4, 3: 4}; degrees=[1, 1, 1, 4, 4, 4, 4, 7]
VERIFY_OK
```

The finite computations corroborate, but do not replace, the arbitrary-prime subgroup count and the all-set forcing proof.

## Relationship to prior work

The standard subgroup intersection graph was established before the present calculation. A 2013 public preprint by Yaraneri uses this graph and lists primary classification \(20K99\); that preprint was later withdrawn because of an error in its main theorem, so it is used here only as a dated definition/classification anchor, not as evidence for any substantive theorem. The corrected finite-abelian-group isomorphism study by Kayacan and Yaraneri appeared online in 2015 and uses the same graph.

The abstract graph obtained here is a pineapple. DeAlba, Grout, Hogben, Mikkelson, and Rasmussen already proved in 2009 that every pineapple \(P_{m,k}\) has minimum rank \(3\) over every field. A later dom-forcing paper also records the standard zero forcing number \(m+k-3\) for pineapples. These prior statements cover the scalar zero forcing number and the minimum-rank corollary, so neither is used as the originality basis.

Boyer and coauthors introduced the zero forcing polynomial and derived closed forms for several graph families. Targeted searches for the subgroup-intersection formulation, the pineapple formulation, the exact factorization, and the coefficient sequence did not locate a complete standard zero forcing polynomial or an all-zero-forcing-set classification for pineapples.

The present statement is stronger than the known scalar parameter: it characterizes every zero forcing set and therefore determines every coefficient of the polynomial, then identifies that enumerator with a natural finite abelian subgroup lattice.

## Limitations

The result concerns \(C_{p^2}\times C_p\), not arbitrary finite abelian \(p\)-groups.

The zero forcing number and field-independent minimum rank of the underlying pineapple graph are already covered by prior graph-theoretic results; only the complete zero forcing classification and polynomial, together with this subgroup-intersection realization, are asserted as new.

A source under an unrelated graph-family name could contain the same pineapple polynomial; this is the principal residual originality risk.

No claim is made that the polynomial determines the prime among arbitrary graph families, although within this subgroup-intersection family its degree \(2p+2\) recovers \(p\).

## References

1. E. Yaraneri, “Abelian Groups With Isomorphic Intersection Graphs,” arXiv:1310.5343, submitted 20 October 2013. The preprint is withdrawn; it is cited only for the public date, graph definition, and classification metadata.
2. S. Kayacan and E. Yaraneri, “Abelian groups with isomorphic intersection graphs,” *Acta Mathematica Hungarica* 146 (2015), 107–127. DOI: 10.1007/s10474-015-0486-9.
3. L. M. DeAlba, J. Grout, L. Hogben, R. Mikkelson, and K. Rasmussen, “Universally Optimal Matrices and Field Independence of the Minimum Rank of a Graph,” *Electronic Journal of Linear Algebra* 18 (2009), 403–419.
4. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” *Discrete Applied Mathematics* 258 (2019), 35–48. DOI: 10.1016/j.dam.2018.11.033; arXiv:1801.08910.
