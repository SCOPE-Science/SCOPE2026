# A three-point distance moment resolves every nine-vertex unit metric-tree collision

## Finding

For each finite tree with between two and nine vertices, replace every combinatorial edge by a closed interval of length one and give the resulting intrinsic metric tree its normalized arclength probability measure. Let \(X,Y,Z\) be three independent samples, \(D=d(X,Y)\), and
\[
Q(T)=\mathbb E[d(X,Y)d(X,Z)].
\]
Then the **pair** consisting of the full distribution of \(D\) and the one real number \(Q(T)\) determines the unit-edge metric tree up to isometry. The two-point distance distribution alone already distinguishes every such tree on at most eight vertices; at nine vertices it has exactly two nontrivial collision classes, each containing two nonisometric trees. The new three-point moment separates both classes, with exact differences \(3/64\) and \(1/16\), respectively.

The same statement holds without supplying the vertex count: for a unit-edge tree of total length \(m\), the right derivative of its two-point CDF at zero is \(2/m\), hence its edge count and vertex count are recoverable.

## Assumptions and scope

All combinatorial trees are finite, connected, simple and unlabeled; all edges have length exactly one. The probability measure is the one-dimensional Hausdorff measure divided by the total length. In particular, samples may lie anywhere along an edge, not only at vertices. We consider exactly the finite class of trees with \(2\le |V|\le9\). No arbitrary positive edge lengths or larger trees are covered.

For a tree with \(m\) edges, let \(h_k\) be the number of unordered pairs of distinct edges for which the shortest endpoint-to-endpoint graph distance is \(k\). Define
\[
B(r)=\begin{cases}0,&r\le0,\\2r-r^2,&0<r<1,\\1,&r\ge1,\end{cases}\qquad
J(r)=\begin{cases}0,&r\le0,\\r^2/2,&0<r<1,\\1-(2-r)^2/2,&1\le r<2,\\1,&r\ge2.\end{cases}
\]
Then the complete two-point CDF is
\[
\Pr(D\le r)=\frac{B(r)}m+\frac2{m^2}\sum_{k\ge0}h_kJ(r-k).
\]
This is a sampling identity, not itself claimed to be new: for trees the edge-distance histogram is an equivalent form of the classical vertex Hosoya polynomial.

## Proof

**Reduction to the discrete edge histogram.** Condition on the two sampled edges. With probability \(1/m\), both points are in the same edge and their distance has CDF \(B\). Conditional on distinct edges separated by \(k\) intervening complete edges, the distance is \(k+U+V\) for independent \(U,V\sim\operatorname{Uniform}(0,1)\), and its CDF is \(J(r-k)\). Each unordered edge pair corresponds to two ordered possibilities, yielding the displayed formula. For \(r\downarrow0\), the distinct-edge contributions are \(O(r^2)\), so the right CDF derivative is \(2/m\). Moreover, the Laplace transform of the distinct-edge part factors as the strictly positive square of \((1-e^{-t})/t\), times \(\sum_k h_ke^{-kt}\). Thus, for fixed \(m\), equality of the two-point distance laws is equivalent to equality of the complete integer histogram \((h_k)\). The 2016 edge-Hosoya identity identifies \(h_k\) with the vertex-pair distance count at distance \(k+2\), excluding the \(m\) coincident-edge terms.

**An exact formula for the new statistic.** Fix an oriented edge \(e=(u,v)\), and use \(s\in[0,1]\) as its coordinate measured from \(u\). Cutting its interior leaves two components with \(a_e\) and \(b_e\) other unit edges. Put
\[
A_e=\int_{T_u}d(u,y)\,d\ell(y),\quad
C_e=\int_{T_v}d(v,y)\,d\ell(y),
\]
where \(T_u,T_v\) are the components **excluding the open edge** \(e\). The unnormalized distance mean from \(x\in e\) is the exact quadratic
\[
I_e(s):=\int_T d(x,y)\,d\ell(y)
=s^2+p_es+q_e,
\quad p_e=a_e-b_e-1,\qquad q_e=b_e+A_e+C_e+\tfrac12.
\]
Indeed, the contributions of \(T_u\) and \(T_v\) are \(a_es+A_e\) and \(b_e(1-s)+C_e\), and the same-edge contribution is \(\int_0^1|s-t|dt=s^2-s+1/2\). Conditional independence of \(Y,Z\) given \(X\) gives
\[
Q(T)=\frac{1}{m^3}\sum_{e}\int_0^1I_e(s)^2\,ds
=\frac{1}{m^3}\sum_e\left(\frac15+\frac{p_e}{2}+\frac{p_e^2+2q_e}{3}+p_eq_e+q_e^2\right).
\]
All quantities are rational and can be calculated by finite vertex-distance sums: for a unit edge \((p,q)\) contained in \(T_u\), its contribution to \(A_e\) is \(\min\{d(u,p),d(u,q)\}+1/2\), and similarly on \(T_v\). This provides a reproducible, exact, independent-from-the-CDF computation of \(Q\).

**Exhaustive isometry classification and separation.** Every tree with at least two vertices has a leaf. Repeatedly deleting a leaf reduces it to a smaller tree, so the procedure that attaches one new leaf at every vertex of every previously generated unlabeled tree generates **all** trees at the next order. At each order, canonical strings obtained by recursively sorting the branch strings rooted at a vertex, and then taking the lexicographically least string over all roots, identify exactly graph-isomorphic trees. This standard canonical representation gives distinct counts \(1,1,1,2,3,6,11,23,47\) in orders \(1\) through \(9\), agreeing with the classical enumeration.

The checker computes every \((h_k)\) directly by edge-endpoint breadth-first search, cross-checks each against all-pairs vertex distances, and groups trees by two-point law. Every group is a singleton through eight vertices. Among the 47 nine-vertex trees exactly two groups have size two; the other 43 are singletons. The following table supplies explicit edge lists for both colliding pairs, their common histograms, and the exact three-point moments. Vertices are labeled \(0,\ldots,8\) solely to specify these edge lists.

| Pair | Edges of first tree | Edges of second tree | Common \((h_0,h_1,h_2,h_3)\) | \(Q\) first | \(Q\) second |
|---|---|---|---|---|---|
| A | `(0,1) (0,2) (0,3) (0,4) (0,5) (1,6) (2,7) (3,8)` | `(0,1) (0,2) (0,3) (0,4) (1,5) (1,6) (1,7) (2,8)` | \((13,12,3,0)\) | \(2263/960\) | \(1109/480\) |
| B | `(0,1) (0,2) (0,3) (0,4) (1,5) (2,6) (3,7) (5,8)` | `(0,1) (0,2) (0,3) (1,4) (1,5) (2,6) (2,7) (4,8)` | \((10,10,6,2)\) | \(1649/480\) | \(1619/480\) |

All omitted histogram entries are zero. The pair-A moment difference is \(3/64\), and pair B is \(1/16\). Within each pair, the degree sequences differ, so the resulting unit-edge metric trees are nonisometric. Equal two-point histograms and unequal \(Q\) therefore establish the asserted classification. Since every maximal arc between leaves or branch points has integral length, intrinsic isometry within this unit-edge class is equivalent to isomorphism of its canonical unit subdivisions; thus the exhaustive graph enumeration is also an exhaustive metric-isometry enumeration.

## Verification

Run `python verify.py` with Python 3; no third-party packages or network access are required. The executable constructs every unlabeled tree of orders at most nine without relying on a stored graph list, uses exact integer edge/vertex distance histograms and `fractions.Fraction` integrals, and verifies every alleged collision. Independently of the branch-component formula for \(Q\), it computes each mean-distance quadratic from exact direct integrals at \(s=0,1/2,1\) and compares all moments for every tree. The script also checks exact probabilities at twelve sample radii for both collision pairs. Its success marker is `THREE_POINT_VERIFY_OK`.

## Relationship to prior work

Stevanović and Gutman's 1999 table already enumerates **every** Hosoya polynomial on up to eleven vertices and visually displays the nonisomorphic trees realizing the duplicated nine-vertex polynomials. Together with Tratnik and Žigert Pleteršek's 2016 edge-Hosoya theorem, this covers the **two-point collision classification**, whose priority is expressly acknowledged. The new assertion is the exact **third-sample cross-distance moment** and the fact that adding this single moment resolves every such collision up through nine vertices; the old polynomial contains no third-sample correlation data. The new distinction is not a re-tabulation of the two-point polynomials.

Mémoli and Needham's work on distance distributions and inverse problems for metric measure spaces establishes much broader nonidentifiability phenomena, including nonisometric larger metric trees sharing even local one-point distance distributions. It does not assert the above sharp small-tree reconstruction result from a global two-point distribution plus one third-order moment. This finite theorem does not contradict the broader counterexamples.

## Limitations

This is an exact natural finite classification, not an infinite theorem. It makes no assertion for trees with ten or more vertices, arbitrary edge lengths, sampling laws other than uniform arclength, or full identification from only the first three moments of a **single** two-point distance. The two-point isodistribution at nine vertices was known through the old Hosoya table; only the third-point resolution and specific combined inverse claim are asserted as additional. An independently performed historical-priority audit could uncover an earlier three-point census. The result does not imply that every tree is identifiable from a three-point distance matrix distribution.

## References

1. D. Stevanović and I. Gutman, *Hosoya Polynomials of Trees with up to 11 Vertices*, Collection of Scientific Papers, Faculty of Science Kragujevac **21** (1999), 111–119. Public author-hosted full text: https://draganstevanovic.wordpress.com/wp-content/uploads/2012/09/hosdraw.pdf .
2. N. Tratnik and P. Žigert Pleteršek, *Relationship Between the Hosoya Polynomial and the Edge-Hosoya Polynomial of Trees*, first arXiv version 2016-09-14, https://arxiv.org/abs/1609.04182 , Theorem 3.2.
3. F. Mémoli and T. Needham, *Distance Distributions and Inverse Problems for Metric Measure Spaces*, https://arxiv.org/abs/1810.09646 , Section 4.1 and Example 4.3.
