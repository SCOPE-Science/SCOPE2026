# Minimum total and paired dominating sets in ideal-intersection graphs of products of fields

## Finding

Let \(R\cong\prod_{i=1}^{r}F_i\) be a direct product of \(r\ge2\) fields, and let \(\Gamma(R)\) be the intersection graph whose vertices are the nonzero proper ideals and whose edges join ideals with nonzero intersection. If \(r=2\), then \(\Gamma(R)\) has no total dominating set and no paired dominating set. If \(r\ge3\), then \[\gamma_t(\Gamma(R))=\gamma_{\mathrm{pr}}(\Gamma(R))=2.\] More precisely, writing \(I_A\) for the ideal supported on a nonempty proper subset \(A\subset[r]\), the minimum total dominating sets and the minimum paired dominating sets coincide: they are exactly the unordered pairs \(\{I_A,I_B\}\) satisfying \(A\cap B\ne\varnothing\) and \(A\cup B=[r]\). Consequently the number of minimum sets of either kind is \[\frac{3^r-3\cdot2^r+3}{2}.\]

For \(r\ge3\), the result therefore classifies every smallest strengthened dominating set, rather than only determining its cardinality.

## Assumptions and scope

Let
\[
R\cong F_1\times\cdots\times F_r,
\qquad r\ge2,
\]
where each \(F_i\) is a field. The intersection graph \(\Gamma(R)\) has the nonzero proper ideals of \(R\) as vertices; two distinct vertices are adjacent exactly when their ideal intersection is nonzero.

For each nonempty proper subset \(A\subset[r]\), define
\[
I_A=J_1\times\cdots\times J_r,
\qquad
J_i=
\begin{cases}
F_i,&i\in A,\\
0,&i\notin A.
\end{cases}
\]
Every nonzero proper ideal is uniquely of this form. Moreover,
\[
I_A\cap I_B=I_{A\cap B},
\]
so distinct vertices are adjacent exactly when \(A\cap B\ne\varnothing\).

A total dominating set requires every vertex, including every selected vertex, to have a selected neighbor. A paired dominating set is a dominating set whose induced subgraph has a perfect matching.

## Proof

If \(r=2\), the only nonzero proper ideals are \(I_{\{1\}}\) and \(I_{\{2\}}\). Their supports are disjoint, so \(\Gamma(R)\cong2K_1\). Hence neither total nor paired domination exists.

Assume \(r\ge3\). Let \(A,B\) be nonempty proper subsets of \([r]\). We first characterize when the pair \(\{I_A,I_B\}\) is a total dominating set.

Necessity of adjacency gives
\[
A\cap B\ne\varnothing.
\tag{1}
\]
If \(A\cup B\ne[r]\), choose \(j\notin A\cup B\). Then the singleton-support vertex \(I_{\{j\}}\) intersects neither selected ideal, so it is undominated. Thus
\[
A\cup B=[r].
\tag{2}
\]

Conversely, suppose (1) and (2) hold. The two selected vertices dominate one another by (1). If \(C\subset[r]\) is any nonempty proper support and \(C\) were disjoint from both \(A\) and \(B\), then it would be disjoint from \(A\cup B=[r]\), impossible. Hence \(I_C\) is adjacent to at least one of \(I_A,I_B\). Therefore the pair is total dominating.

For \(r\ge3\) such pairs exist, for example
\[
A=[r]\setminus\{1\},
\qquad
B=[r]\setminus\{2\}.
\]
Their intersection is nonempty. Since a total dominating set in a simple graph cannot have one vertex,
\[
\gamma_t(\Gamma(R))=2.
\]

Every paired dominating set is total dominating. A two-vertex total dominating set induces one edge, hence already has a perfect matching. Thus the minimum total and paired dominating sets coincide, and
\[
\gamma_{\mathrm{pr}}(\Gamma(R))=2.
\]

It remains to count the minimum sets. For an ordered pair \(A,B\) satisfying (1) and (2), every coordinate lies in exactly one of
\[
A\setminus B,
\qquad
B\setminus A,
\qquad
A\cap B.
\]
All three classes are nonempty: the third by (1), while either of the first two being empty would force the other selected support to equal \([r]\), contradicting properness together with (2). Hence ordered admissible pairs are exactly surjections from \([r]\) onto three labeled classes. Inclusion-exclusion gives
\[
3^r-3\cdot2^r+3
\]
such ordered pairs. Swapping \(A\) and \(B\) is a fixed-point-free involution, so the number of unordered minimum sets is
\[
\frac{3^r-3\cdot2^r+3}{2}.
\]

## Verification

The standalone `verify.py` artifact represents supports as nonzero, non-full bit masks. It builds adjacency from nonempty intersection and exhaustively enumerates all two-vertex total and paired dominating sets for
\[
2\le r\le7.
\]
For every checked rank it verifies equality with the structural criterion and with the closed counting formula.

Exact output:

```text
r=2 vertices=2 minimum_total_pairs=0 minimum_paired_pairs=0 formula=0
r=3 vertices=6 minimum_total_pairs=3 minimum_paired_pairs=3 formula=3
r=4 vertices=14 minimum_total_pairs=18 minimum_paired_pairs=18 formula=18
r=5 vertices=30 minimum_total_pairs=75 minimum_paired_pairs=75 formula=75
r=6 vertices=62 minimum_total_pairs=270 minimum_paired_pairs=270 formula=270
r=7 vertices=126 minimum_total_pairs=903 minimum_paired_pairs=903 formula=903
VERIFY_OK
```

The computation is corroborative only. The arbitrary-rank theorem is established by the support-intersection proof above.

## Relationship to prior work

Jafari and Jafari Rad determine ordinary domination in intersection graphs of ideals. Their Theorem 2.6 proves that an Artinian commutative ring has ordinary domination number two precisely in the product-of-fields case considered here. Their paper defines ordinary domination only and contains no statement of total or paired domination.

Abu Osba, Al-Addasi, and Abughneim later recover ordinary domination number two for finite principal ideal rings that are products of fields and develop radius, center, geodetic, hull, independence, and chordality information. Their full article likewise contains no total- or paired-domination theorem.

The present result sharpens the ordinary-domination picture in two directions that are not implied by the value \(\gamma=2\): the two-factor product has no total or paired dominating set at all, while every product with at least three factors has strengthened domination number two; and all minimum strengthened dominating pairs are classified and counted exactly.

## Limitations

The theorem concerns direct products of fields. Products with nonfield local factors have additional ideals and need not have the same support-only intersection graph.

The result uses the standard ideal-intersection graph on nonzero proper ideals. Altering the vertex convention changes the graph.

The field cardinalities do not enter the answer; only the number of factors is detected by the minimum-set count.

## References

1. S. H. Jafari and N. Jafari Rad, “Domination in the intersection graphs of rings and modules,” *Italian Journal of Pure and Applied Mathematics* 28 (2011), 17–20.
2. Z. S. Pucanović, M. Radovanović, and A. Lj. Erić, “On the genus of the intersection graph of ideals of a commutative ring,” *Journal of Algebra and Its Applications* 13 (2014), 1350155. DOI: 10.1142/S0219498813501557.
3. E. Abu Osba, S. Al-Addasi, and O. Abughneim, “Some Properties of the Intersection Graph for Finite Commutative Principal Ideal Rings,” *International Journal of Combinatorics* 2014, 952371. DOI: 10.1155/2014/952371.
