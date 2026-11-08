# Exact ordinary and fractional illumination of type-\(D_d\) root polytopes

## Finding
For every integer \(d\ge4\), define
\[
P_d=\operatorname{conv}\{\sigma e_i+\tau e_j:1\le i<j\le d,\ \sigma,\tau\in\{-1,1\}\}\subset\mathbb R^d.
\]
Its ordinary directional illumination number and fractional directional illumination number satisfy
\[
\boxed{I(P_d)=I^*(P_d)=2d.}
\]
Furthermore, a concrete family of \(2d\) directions exactly partitions all \(2d(d-1)\) vertices into illumination classes of \(d-1\) vertices. The theorem includes the regular \(24\)-cell in dimension four, for which both numbers are \(8\).

## Assumptions and scope
A nonzero direction \(u\in\mathbb R^d\) illuminates \(x\in\partial P_d\) if \(x+tu\in\operatorname{int}P_d\) for some \(t>0\). The least size of a finite family illuminating the entire boundary is \(I(P_d)\). The fractional number \(I^*(P_d)\) is the infimum of \(\sum_r\lambda_r\) over finite families of directions \(u_r\) with nonnegative weights \(\lambda_r\), for which the weights of directions illuminating every boundary point sum to at least one. Directions need not be normalized because positive scaling leaves illumination unchanged. All claims concern real dimension \(d\ge4\) and ordinary strict illumination; no claim is made about other root-system polytopes or a quantitative cost involving distances to light sources.

The halfspace representation is
\[
P_d=\{x:\ |x_i|\le1\ (1\le i\le d),\quad \sum_i|x_i|\le2\}.
\]
To see this, the listed roots satisfy the inequalities. In any fixed orthant, the intersection is the signed image of the polytope \(0\le y_i\le1\), \(\sum_i y_i\le2\), whose vertices have zero-one coordinates and at most two ones. Points with at most one nonzero coordinate lie in the convex hull of the displayed roots, proving the reverse inclusion. Each displayed root is exposed by its two signed coordinate supporting hyperplanes. Thus there are exactly \(4\binom d2=2d(d-1)\) vertices.

## Proof
**1. An exact vertex-direction criterion.** At the vertex \(v=\sigma e_i+\tau e_j\), the active inequalities are \(\sigma x_i\le1\), \(\tau x_j\le1\), and
\[
\sigma x_i+\tau x_j+\sum_{k\notin\{i,j\}}\varepsilon_k x_k\le2
\qquad(\varepsilon_k\in\{-1,1\}).
\]
Strict inward motion along \(u\) requires all active normals to have negative pairing with \(u\). Thus illumination is equivalent to
\[
\sigma u_i<0,\quad\tau u_j<0,\quad
|u_i|+|u_j|>\sum_{k\notin\{i,j\}}|u_k|. \tag{1}
\]
Indeed, the last condition is the maximum over all active sign-sum normals after the first two force the signs. For a fixed unordered pair \(\{i,j\}\), at most one of the four vertices supported there can be illuminated by a given \(u\).

**2. No direction illuminates more than \(d-1\) vertices.** Set \(a_i=|u_i|\) and \(S=\sum_i a_i\). An unordered pair is *heavy* if \(2(a_i+a_j)>S\). Equation (1) shows that each illuminated vertex uses a heavy pair. Two disjoint pairs cannot both be heavy, since summing their strict inequalities gives \(a_i+a_j+a_k+a_\ell>S\), contradicting the definition of \(S\). Therefore all heavy pairs are pairwise intersecting edges of a complete graph. Every pairwise intersecting family of two-element sets is either a star or a triangle: if edges \(\{a,b\}\), \(\{a,c\}\) occur and another edge omits \(a\), it must be \(\{b,c\}\), after which no fourth different edge can intersect all three. Accordingly, the heavy pairs number at most \(\max\{d-1,3\}=d-1\) for \(d\ge4\). Hence every direction illuminates at most \(d-1\) vertices.

**3. An explicit exact partition by \(2d\) directions.** For \(1\le i\le d\) let
\[
(w_i)_j=\begin{cases}-1,&j<i,\\d,&j=i,\\1,&j>i.\end{cases}
\]
Use the \(2d\) nonzero directions \(w_i,-w_i\). For either direction centered at \(i\), the only heavy pairs are \(\{i,j\}\) with \(j\ne i\): the corresponding two-coordinate magnitude is \(d+1\), exceeding the remaining magnitude sum \(d-2\); a pair avoiding \(i\) has magnitude sum \(2\), smaller than its complement \(2d-3\). By (1), each direction illuminates exactly one vertex over each of its \(d-1\) heavy pairs.

For a fixed pair \(i<j\), only the directions \(w_i,-w_i,w_j,-w_j\) can illuminate vertices supported there. Their signs in coordinates \((i,j)\) are respectively \((+,+),(-,-),(-,+),(+,-)\). The four sign pairs occur exactly once. By (1), each of the four vertices \(\sigma e_i+\tau e_j\) is therefore illuminated by exactly one of these directions. This proves the asserted exact partition.

**4. Boundary coverage and fractional sharpness.** Illuminating every vertex illuminates the whole polytope boundary. Indeed, for \(x\) in the relative interior of its minimal face, pick a vertex \(v\) of that face; every facet inequality active at \(x\) is active at \(v\), so a direction strictly inward at \(v\) is strictly inward at \(x\). The construction consequently gives \(I(P_d)\le2d\) and, with unit weights, \(I^*(P_d)\le2d\).

On the other hand, summing the coverage condition of any fractional illumination over the \(2d(d-1)\) vertices gives
\[
2d(d-1)\le\sum_r\lambda_r\,N(u_r)\le(d-1)\sum_r\lambda_r,
\]
where \(N(u_r)\le d-1\) is the number of vertices illuminated by \(u_r\). Hence \(I^*(P_d)\ge2d\). Since \(I(P_d)\ge I^*(P_d)\), both equal \(2d\). An invertible affine transformation preserves the illuminated-face incidence structure, so the equality also holds for every affine image of \(P_d\).

## Verification
The standalone `verify_root_family.py` independently implements the active-facet criterion (1), enumerates the \(2d(d-1)\) vertices and the \(2d\) specified directions, and checks both that every direction illuminates exactly \(d-1\) vertices and that every vertex is illuminated exactly once. The program executes exact integer arithmetic for all dimensions from \(4\) through \(15\), with the supplementary dimension-three comparison, and prints `ROOT_FAMILY_EXACT_OK`. This finite check corroborates the calculation but is not an infinite-dimensional proof; Steps 1–4 give the proof for every integer \(d\ge4\).

## Relationship to prior work
Naszódi (2009) introduced finite-weight fractional illumination and proved general upper estimates, including \(I^*(K)\le2^d\) for centrally symmetric convex bodies. Gorodzha (2026) establishes the general \(2^d\) bound with its equality case. Neither result gives the exact \(2d\) value for this family. Kiss and de Wet (2012) distinguish ordinary illumination from the more costly quantitative illumination parameter and study chiefly three-dimensional Platonic and Archimedean solids.

A separate publicly available 2026 note, *Exact quantitative illumination of type-D root polytopes*, treats exactly these polytopes but a **different** invariant: the total gauge cost of finite exterior light sources. Its proof already establishes the heavy-pair intersecting-edge mechanism used for the lower bound, so that mechanism is not asserted to be new. The present contribution is the simultaneous exact value of the **ordinary and fractional directional invariants for all dimensions \(d\ge4\)**, with an explicit family of \(2d\) directions partitioning all vertices. The older quantitative cost evaluation and the general fractional upper bounds do not supply that construction or imply the exact ordinary value.

## Limitations
This statement does not address all convex bodies, all root systems, or quantitative light-source costs. The historical priority assessment is necessarily limited to the examined literature and public mathematical records; an earlier equivalent construction not indexed by the searches remains possible. Independent mathematical verification has not been performed.

## References
1. M. Naszódi, *Fractional illumination of convex bodies*, Contributions to Discrete Mathematics 4 (2009), 83–88. DOI: 10.55016/ojs/cdm.v4i2.62022. https://cdm.ucalgary.ca/article/view/62022
2. Y. Gorodzha, *Fractional illumination and the optimal exponential rate in Hadwiger's covering conjecture*, first posted 2026-09-20, arXiv:2609.23913. https://arxiv.org/abs/2609.23913
3. G. Kiss and P. O. de Wet, *Notes on the illumination parameters of convex polytopes*, Contributions to Discrete Mathematics 7 (2012), 58–67. DOI: 10.55016/ojs/cdm.v7i1.62108. https://cdm.ucalgary.ca/article/view/62108
4. *Exact quantitative illumination of type-D root polytopes* (public mathematical note, 2026), concerning a gauge-weighted source-cost parameter rather than directional illumination.
