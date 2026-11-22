# Seventy-two minimum edge guards and a four-swap mobility threshold in the ternary affine-plane incidence graph

## Finding

Let \(H\) be the point-line incidence (Levi) graph of \(\operatorname{AG}(2,3)\). Its vertices are the nine points and twelve lines, and its edges are the 36 incident point-line pairs (flags). An edge set \(M\) *edge-dominates* if every flag shares its point or line with at least one flag of \(M\).

**Theorem.** The minimum size of an edge-dominating set of \(H\) is \(\gamma_e(H)=7\), and there are exactly \(72\) minimum sets. Every minimum is a matching. More precisely, select any two distinct points \(a,b\) and let \(c\) be the third point of the line \(\ell_{ab}\). The unique flag at \(\ell_{ab}\) in a minimum leaving \(a,b\) uncovered is \((c,\ell_{ab})\); the six remaining selected flags form one of two alternating perfect matchings in a twelve-cycle. Every minimum arises exactly once this way.

For \(1\le d\le7\), define the *\(d\)-exchange graph* of minimum edge-dominating sets: two different minima \(M,N\) are adjacent precisely when \(7-|M\cap N|\le d\). The \(d\)-exchange graph is edgeless for \(d\le3\). At \(d=4\), it is connected and eight-regular, with \(72\) vertices, \(288\) edges and diameter \(4\). Every vertex has distance-level sizes \((1,8,32,28,3)\) at levels \(0,1,2,3,4\).

## Assumptions and scope

All points and lines are those of the unique order-three affine plane, with points \(\mathbb F_3^2\) and twelve lines \(x=c\) or \(y=mx+b\), where \(m,b,c\in\mathbb F_3\). The flag graph is undirected and simple. The term minimum means *minimum cardinality* (not merely inclusion minimality). Batch exchange is between minimum feasible configurations only; every intermediate state in a path is minimum feasible.

## Proof

**1. Incidence-free lower bound.** Let \(M\) be any edge-dominating set of size \(k\), not assumed to be a matching. Let \(X\) be its uncovered point vertices and \(Y\) its uncovered line vertices. Since each chosen flag covers at most one point and one line, \(|X|\ge9-k\) and \(|Y|\ge12-k\). Edge domination implies no point of \(X\) lies on a line of \(Y\).

Every point of \(\operatorname{AG}(2,3)\) lies on four lines; each pair of points lies on precisely one line. If three points are collinear, exactly ten lines meet at least one of them (one common line and three additional lines through each point). If three points are noncollinear, exactly nine lines meet at least one of them by inclusion-exclusion. Thus at most three of the twelve lines avoid any chosen three points. If \(k\le6\), then \(|X|\ge3\) and \(|Y|\ge6\), a contradiction. Hence \(k\ge7\).

**2. Complete optimum classification.** If \(k=7\), then \(|X|\ge2\) and \(|Y|\ge5\). The preceding three-point bound rules out \(|X|\ge3\). Thus \(X=\{a,b\}\), and all other seven points are covered; the seven chosen flags have distinct point endpoints. Exactly seven lines meet \(a\) or \(b\), since \(4+4-1=7\), leaving precisely five lines disjoint from \(\{a,b\}\). All five must be uncovered, as no uncovered line can meet an uncovered point and \(|Y|\ge5\). Therefore every one of the seven lines through \(a\) or \(b\) occurs exactly once among the seven flags. Consequently \(M\) is a matching between the other seven points and these seven lines.

The line \(\ell_{ab}\) contains \(a,b,c\), so its flag is forced to be \((c,\ell_{ab})\). Among the six off-line points, each belongs to exactly one of the three other lines through \(a\) and exactly one of the three other lines through \(b\). For each direction except that of \(\ell_{ab}\), the two lines of that direction (one through each of \(a,b\)) are parallel. Every other cross-family pair intersects at an off-line point. Hence the bipartite incidence pattern between these two line triples is \(K_{3,3}\) with a perfect matching deleted, which is a six-cycle. Subdividing its six edges by the off-line points gives a twelve-cycle between the six remaining lines and six remaining points. A cycle of even length has exactly two perfect matchings. For each of the \(\binom92=36\) uncovered point pairs this yields precisely two seven-flag matchings; each is edge-dominating because its five uncovered lines avoid its two uncovered points. Distinct pairs have different uncovered point sets. This proves \(\gamma_e(H)=7\) and the exact count \(72\).

**3. Sharp batch-exchange geometry.** The remaining finite statement concerns exactly the 72 explicitly classified sets. We give a complete finite certificate, not an extrapolation from sample cases. The accompanying `verify_geometry.py` enumerates all \(\binom92\) unordered point pairs and both exact residual perfect matchings. It computes the intersection cardinality of each of the \(\binom{72}{2}=2556\) distinct pairs, obtaining respectively \(612,900,756,288\) pairs with intersection sizes \(0,1,2,3\), and none with larger intersection. Thus changing three or fewer flags never connects two distinct optima; exactly the 288 pairs sharing three flags are legal four-exchanges.

The verifier constructs all 288 adjacencies and performs breadth-first search from **each** of the 72 minima. Every vertex has eight neighbors and full distance-level vector \((1,8,32,28,3)\), proving connectedness and diameter four. A second checker, `verify_all_edge_sets.cpp`, enumerates every subset of the 36 flags of size one through seven independently of the point-pair construction, checks the edge-dominating condition, and repeats the intersection and breadth-first search checks for its 72 seven-flag solutions. The exhaustive algorithms, termination ranges and assertions are contained in the included complete source files, so no unstated enumeration is required.

## Verification

Run from a directory containing the supplied standalone sources:

```sh
python3 verify_geometry.py
g++ -O3 -std=c++17 -o verify_all_edge_sets verify_all_edge_sets.cpp
./verify_all_edge_sets
```

The geometric checker reports `GEOMETRY_CERTIFICATE_OK`; the direct independent exhaustive checker reports `CERTIFICATE_OK`. It checks all \(\sum_{j=1}^{7}\binom{36}{j}\) edge subsets in the stated range, not merely matchings. Both confirm 72 minima, intersection multiplicities, eight-regular four-exchange graph, diameter four. The analytic proof, not the code, establishes the lower bound and geometric parametrization.

## Relationship to prior work

Spiro, Adriaensen and Mattheus (first public preprint 2022-11-25) develop the incidence-free-pair method for edge domination of incidence graphs. Their general lower bound for a \((v,b,k,r,\lambda)=(9,12,3,4,1)\) design already yields \(\gamma_e(H)\ge\lceil 2(7-\sqrt{13})\rceil=7\). This lower bound **is not claimed to be new**. Their article focuses on general bounds and principally symmetric designs; its inspected full text does not give the order-three affine-plane optimum construction, count or batch-exchange classification. Caro, Davila, Henning and Pepper (2021 preprint, 2022 journal article) give general bounds relating edge domination to matching, but not this incidence-plane enumeration.

Published results on affine-space *vertex* total/paired domination, on matchings of the projective-plane Levi graph, and on ordinary edge domination in crown graphs concern different objects or invariants and do not imply the 72-set or four-exchange assertions. Prior-art review is necessarily provisional for unindexed historical calculations.

## Limitations

This is an exact finite theorem for the 21-vertex incidence graph of the order-three affine plane; it does not assert a formula for all affine planes. The four-exchange diameter is verified by complete, independently implemented finite enumeration; no symbolic formula in larger order is claimed. An independent human audit has not been performed, and exhaustive historical priority cannot be guaranteed.

## References

- S. Spiro, S. Adriaensen and S. Mattheus, *Incidence-free sets and edge domination in incidence graphs*, arXiv:2211.14339, first publicly submitted 2022-11-25, https://arxiv.org/abs/2211.14339 ; Journal of Combinatorial Designs 32 (2024), 55–87, DOI:10.1002/jcd.21925.
- Y. Caro, R. Davila, M. A. Henning and R. Pepper, *Conjectures of TxGraffiti: Independence, domination, and matchings*, arXiv:2104.01092, first submitted 2021-04-02; Australasian Journal of Combinatorics 84 (2022), 258–274, https://arxiv.org/abs/2104.01092.
