# Two sharp Euclidean chord shells in alternating type-C Gale-interval polytopes

## Finding

For each integer \(r\ge 2\), set \(n=2r\), \(T_r=\{2,4,\ldots,2r\}\), and let \(P_r\subset\mathbb R^{2r}\) be the canonical feasible polytope of the type-C Gale interval \([\varnothing,T_r]\), with its native orthonormal zero-one coordinates. Then \(P_r\) has \(\binom{2r+1}{r}\) vertices and full affine dimension \(2r\). Its exact squared Euclidean diameter is \(2r\). The number of unordered vertex pairs at the **largest** squared distance \(2r\) is
\[
N_r(2r)=2^{r-1},
\]
while the number at the **next** squared distance \(2r-1\) is
\[
N_r(2r-1)=2(3^r-2^r).
\]
Every diametral pair is a complementary zero-one pair, with exactly one selected coordinate from each successive two-position block \(\{2j-1,2j\}\) in one endpoint. Thus the diameter graph consists of \(2^{r-1}\) disjoint edges and \(\binom{2r+1}{r}-2^r\) isolated vertices. No nonvertex point of \(P_r\) can belong to a diametral pair.

In particular the ratio of near-diametral to diametral pairs is \(4((3/2)^r-1)\), so the second-longest chord shell grows exponentially faster than the longest shell. The conclusion concerns ordinary ambient Euclidean distances, not edge-graph distances.

## Assumptions and scope

The type-C Gale partial order on subsets of \([n]\) satisfies \(A\preceq B\) if and only if \(|A\cap[i,n]|\le |B\cap[i,n]|\) for every \(i\in[n]\). The vertices of \(P_r\) are exactly the characteristic vectors \(\mathbf1_A\) with \(A\preceq T_r\). Equivalently the defining inequalities are
\[
0\le x_i\le1,\qquad \sum_{j=i}^{2r}x_j\le |T_r\cap[i,2r]|\quad(1\le i\le2r).
\]
This is the alternating upper Gale interval, not an arbitrary type-C interval or its affine image in another metric. Every feasible zero-one point is a vertex because a zero-one vector cannot be a strict convex combination of distinct zero-one vectors. The unit coordinate basis fixes the metric normalization.

## Proof

**1. Vertex walk encoding and vertex count.** Read a feasible binary vector backwards, from coordinate \(2r\) down to coordinate \(1\). At each step record \(+1\) for bit zero and \(-1\) for bit one. For a reversed prefix of length \(k\), the upper Gale bound permits at most \(\lceil k/2\rceil\) ones, since the final \(k\) positions contain exactly \(\lceil k/2\rceil\) elements of \(T_r\). Equivalently its walk height \(h(k)\) is at least \(-1\). The number of length-\(2r\) walks with these steps and lower barrier \(-1\) is \(\binom{2r+1}{r}\), by the standard reflection argument (or by subtracting from \(2^{2r}\) all paths whose first visit to \(-2\) is reflected). The polytope is full-dimensional: all feasible singleton vectors, together with the origin, are affinely independent, since each singleton is \(\preceq T_r\).

**2. Diameter and complete contact graph.** For two zero-one vertices, the squared distance is the number of differing coordinates, hence at most \(2r\). Equality requires two complementary binary words. For a complementary feasible pair, let their reversed walk heights be \(h\) and \(-h\). Both must stay at least \(-1\), so their heights lie in \(\{-1,0,1\}\). At each even time the height is even, hence zero; every pair of successive steps must therefore be opposite. There are exactly two choices for each of the \(r\) two-step blocks, producing \(2^r\) ordered first endpoints and thus \(2^{r-1}\) unordered complementary pairs. Such pairs exist, proving the diameter. Each feasible endpoint has exactly one complement; hence these edges are disjoint and use exactly \(2^r\) vertices. Strict convexity of squared Euclidean distance in either endpoint excludes nonvertices from diameter-realizing pairs.

**3. Penultimate chord shell.** A pair at squared distance \(2r-1\) has exactly one agreeing coordinate. Before that coordinate, the two reversed walks are opposite and return to height \((0,0)\) after every even step. If their sole equal step is \((-1,-1)\) (both original bits one), their height sum becomes \(-2\). Both heights would then have to remain \(-1\), making any subsequent opposite step impossible. Since \(2r\) is even, the equal step cannot be at the final time either: the preceding odd-time opposite heights are \((1,-1)\) or \((-1,1)\), so subtracting one from both violates the barrier. Thus the sole common bit must be zero, corresponding to a simultaneous step \((+1,+1)\).

After this simultaneous step the sum of the two heights is \(2\). If the first height is \(s\), barrier feasibility for both is precisely \(-1\le s\le3\). The remaining opposite steps move \(s\) by \(+1\) or \(-1\), and therefore form walks on the five-vertex path with states \(-1,0,1,2,3\). Let \(f_L(s)\) count allowed length-\(L\) continuations starting at \(s\). The two-step adjacency operator on the two states \(0,2\) has constant row sum \(3\), so
\[
f_{2m}(0)=f_{2m}(2)=3^m,\qquad f_{2m+1}(1)=2\cdot3^m
\]
for all integers \(m\ge0\). These identities also follow by multiplication of the five-state path adjacency matrix.

If the sole agreeing coordinate is step \(t=2k+1\), with \(0\le k\le r-1\), the preceding \(2k\) opposite steps have \(2^k\) choices; the simultaneous zero bits place the height at central state \(1\). There remain \(2(r-k)-1\) steps, so this position contributes \(2^{k+1}3^{r-k-1}\) **ordered** pairs. Summing over \(k\) gives \(2(3^r-2^r)\) ordered pairs.

If the equal coordinate is step \(t=2k\), with \(1\le k\le r\), there are \(2^k\) preceding opposite-step strings, equally split between heights \((+1,-1)\) and \((-1,+1)\). After the simultaneous zero bits these give states \(2\) and \(0\), respectively. The remaining \(2(r-k)\) steps contribute \(3^{r-k}\) continuations per preceding string. Summing \(2^k3^{r-k}\) over \(k\) again gives \(2(3^r-2^r)\) ordered pairs. Every distinct unordered pair is represented twice, establishing \(N_r(2r-1)=2(3^r-2^r)\).

**4. Geometric interpretation.** The complete classification follows from the two combinatorial counts and the fact that Euclidean distances between binary vertices are Hamming distances. In particular, there can be no squared chord length strictly between \(2r-1\) and \(2r\).

## Verification

The standalone `check_chords.py` independently constructs all zero-one vertices from the suffix inequalities and enumerates every unordered vertex pair in dimensions \(2,4,6,8,10,12\) using exact integer arithmetic. It checks the vertex-count formula, both top squared-distance multiplicities, and the complete disjoint-edge structure of the diameter graph. A separate ordered-pair suffix-walk dynamic program independently verifies both shell formulas through \(r=15\). The run produced:

```text
r=1 vertices=3 diameter_pairs=1 near_pairs=2
r=2 vertices=10 diameter_pairs=2 near_pairs=10
r=3 vertices=35 diameter_pairs=4 near_pairs=38
r=4 vertices=126 diameter_pairs=8 near_pairs=130
r=5 vertices=462 diameter_pairs=16 near_pairs=422
r=6 vertices=1716 diameter_pairs=32 near_pairs=1330
ALTERNATING_GALE_TOP_SHELL_PASS brute_r=1..6 walk_dp_r=1..15 unordered_pairs=1586479
```

The case \(r=1\) is included as a small boundary calibration; the main theorem is asserted for \(r\ge2\). Both finite checks corroborate the all-dimensional proof and are not used to infer it.

## Relationship to prior work

Chen, Sanchez, Veliz and Ying introduced lattice-path delta matroids and proved the suffix-inequality description of their feasible polytopes in *Lattice Path Delta Matroids*, arXiv:2311.15441 (initial public upload 2023-11-26), especially their type-C Gale-order lemma and Theorem A. Their stated results concern descriptions, dimensions, faces, triangulations and volumes, not the two Euclidean outer chord shells determined here.

Eur, Fink, Larson and Spink, *Signed permutohedra, delta-matroids, and beyond*, arXiv:2209.06752, develop the general delta-matroid polytope framework and volume/lattice-point theory. A separate published result, *Four-state Euclidean distance spectrum and antipodal rigidity of linked type-C snake polytopes*, proves a metric transfer formula for linked **toric snake** intervals \([S,S\cup\{n\}]\). Our intervals have \(S=\varnothing\) and \(T_r\) with \(r\ge2\) elements, and hence cannot be members of that family: for \(S=\varnothing\), its linked toric form would require \(T=\{2r\}\). The published snake formula does not enumerate cross-cell pairs in a general non-snake interval and does not imply the present two-shell identities. The comparison is substantive rather than a claim that lack of a keyword match proves priority.

## Limitations

The explicit formulas are for the specified alternating upper type-C Gale interval and native Euclidean metric, not all lattice-path delta matroids. Only the largest two distinct **squared** vertex-distance shells are classified; no formula is asserted for every intermediate shell, facet metric or graph-theoretic geodesic distance. The independent mathematical validation of the claim has not been performed. Literature searches and accessible source text cannot rule out every unindexed equivalent statement.

## References

1. D. M. Chen, M. Sanchez, J. Veliz and Z. Ying, *Lattice Path Delta Matroids*, arXiv:2311.15441, first public version 2023-11-26. https://arxiv.org/abs/2311.15441
2. C. Eur, A. Fink, M. Larson and H. Spink, *Signed permutohedra, delta-matroids, and beyond*, arXiv:2209.06752. https://arxiv.org/abs/2209.06752
3. *Four-state Euclidean distance spectrum and antipodal rigidity of linked type-C snake polytopes*, published mathematical record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-four-state-euclidean-distance-spectrum-and-antipodal-rigidity-of--0acaa0ef9409
