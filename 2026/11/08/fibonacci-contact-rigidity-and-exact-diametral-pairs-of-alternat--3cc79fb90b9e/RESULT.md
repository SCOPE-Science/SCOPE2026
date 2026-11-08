# Fibonacci contact rigidity and exact diametral pairs of alternating adjacent-sum polytopes

## Finding

For the alternating adjacent-sum lattice polytopes defined below, the smallest enclosing Euclidean ball and Euclidean diameter have closed formulas in every dimension and at every positive integer twist. For \(d\ge4\), their sphere contacts undergo a sharp, exact change at \(s=2\): in the nontrivial alternating regime the contacts are weighted independent sets of a path, so their number is \(F_{d+2}\). (For dimensions \(d=2,3\), the two contact-count formulas coincide.) The number of unordered diametral pairs simultaneously falls to one. At \(s=1\), the respective sphere-contact counts are \(3^r\) and \(5\cdot3^{r-1}\) in even and odd dimension, and the diametral-pair count is \(2^{r-1}\). Here \(r=\lfloor d/2\rfloor\) and \(F_0=0,F_1=1\) are Fibonacci numbers.

More precisely, the unique minimum enclosing ball has center and squared radius
\[
\begin{array}{c|c|c}
 d & c & R^2\\\hline
 2r &(s/2)\mathbf1_{2r} & rs^2/2\\
 2r+1 &(s/2)\mathbf1_{2r}\oplus((s+1)/2)&[2rs^2+(s+1)^2]/4
\end{array}
\]
and the exact squared diameter is \(4R^2\).

## Assumptions and scope

Let \(d\ge2\) and \(s\ge1\) be integers. The ambient inner product is the standard Euclidean one. Define
\[
P_d^{(s)}=\{x\in\mathbb R^d:x_i\ge0\ (1\le i\le d),\ x_i+x_{i+1}\le s+\delta_i\ (1\le i<d)\},
\qquad \delta_i=\begin{cases}0&i\text{ odd},\\1&i\text{ even}.\end{cases}
\]
The final inequality is at index \(d-1\); there is no cyclic wraparound. Write \(r=\lfloor d/2\rfloor\). A contact point means any point of the polytope lying on the minimum enclosing sphere; a diametral pair is an unordered pair of points realizing the Euclidean diameter. All counted contacts are actual polytope vertices. The Fibonacci numbers are initialized by \(F_0=0,F_1=1\) and \(F_{n+2}=F_{n+1}+F_n\).

## Proof

**1. A product circumball.** Let \(T_s=\{(u,v)\in\mathbb R^2:u,v\ge0,\ u+v\le s\}\). The odd-indexed adjacent-sum inequalities imply
\[
P_{2r}^{(s)}\subseteq T_s^r,\qquad P_{2r+1}^{(s)}\subseteq T_s^r\times[0,s+1].
\]
For the second inclusion, the last coordinate is at most \(s+1\), by the last (even-indexed) adjacent-sum inequality and nonnegativity. The three vertices of \(T_s\), namely \((0,0),(s,0),(0,s)\), all lie on the circle with center \((s/2,s/2)\) and squared radius \(s^2/2\). Every other point of \(T_s\) lies strictly inside this circle: strict convexity of the squared Euclidean norm implies that a nonvertex convex combination cannot maximize it. Similarly, \([0,s+1]\) lies in the closed interval-centered ball of squared radius \((s+1)^2/4\), with equality only at the two endpoints. Summing squared distances in independent coordinate blocks gives the asserted ball containment and formulas for \(c,R\).

**2. Sharpness and uniqueness.** Define two points by putting value \(s\) in every odd coordinate and zero in each even coordinate, and vice versa, with the final odd coordinate of the first point taking \(s+1\) when \(d\) is odd. These two points satisfy all alternating inequalities: at an odd index the adjacent sum is exactly \(s\); at every even index the sum is \(s\), except that the final index in odd dimension may sum to \(s+1\); in all cases the bound is respected. In the even case they are coordinatewise complementary around \(c\); in the odd case their final coordinates sum to \(s+1\). They therefore have Euclidean separation \(2R\) and are antipodal about \(c\). No point pair in the containing radius-\(R\) ball can be farther apart, and no enclosing ball can have radius less than half their separation. Thus the proposed ball is minimal and \(\operatorname{diam}(P)=2R\). Moreover, any radius-\(R\) ball containing an antipodal distance-\(2R\) pair must be centered at their midpoint \(c\), proving uniqueness.

**3. All contact vertices for \(s\ge2\).** Equality with the product ball in Step 1 holds exactly when every triangular block is at one of its three vertices and (for odd dimension) the terminal interval is at an endpoint. Thus each contact is a vector with entries zero or \(s\), except for the terminal odd coordinate, which may be zero or \(s+1\). Odd-index adjacent constraints rule out both coordinates of any triangular block being positive. At an even index, two positive neighboring coordinates have sum \(2s>s+1\), or, for the terminal pair, \(2s+1>s+1\). Hence the remaining inequalities hold if and only if the set of positive coordinates is an independent set in the path graph with vertices \(1,\ldots,d\). Every such indicator vector is feasible, and as an extreme point of the product container is also an extreme point of \(P\). The elementary recurrence for independent sets of a length-\(d\) path, splitting on whether its last vertex is selected, gives exactly \(F_{d+2}\) contacts.

**4. All contact vertices for \(s=1\).** When \(d=2r\), every triangular-block vertex is feasible: across two blocks, the intervening even-index bound is two, and each contributing coordinate is at most one. There are exactly \(3^r\) contact vertices. When \(d=2r+1\), the terminal coordinate may be zero or two. In the former case, all \(3^r\) triangle-vertex choices are feasible. In the latter case, the preceding coordinate must be zero, leaving two choices for the final triangle and three each for the other \(r-1\) triangles. Therefore the count is \(3^r+2\cdot3^{r-1}=5\cdot3^{r-1}\). The same product strict-convexity argument excludes every other point from the sphere.

**5. Diametral-pair enumeration.** Equality in the triangle inequality for two points in a Euclidean radius-\(R\) ball occurs precisely when the points are mutually antipodal around \(c\), both on the sphere. In every triangular block, antipodal contact corners must be \((s,0)\) and \((0,s)\); \((0,0)\) has no triangular-vertex antipode. For odd dimension the terminal endpoints must be \(0\) and \(s+1\). Thus an antipodal candidate pair corresponds to an orientation choice in each of the \(r\) triangular blocks. If \(s\ge2\), changing orientation between neighboring blocks places two selected positive coordinates across their even-index interface in one endpoint, violating the capacity \(s+1\); hence every orientation agrees, giving one unordered pair. In odd dimension, the terminal endpoint at \(s+1\) forces the orientation of the last triangular block as well, and again the unique pair survives. If \(s=1\), every orientation of the \(r\) blocks is possible in even dimension, and exchanging the two endpoints identifies opposite orientation words, giving \(2^{r-1}\) unordered pairs. For odd dimension, fixing which endpoint has terminal coordinate two forces the last triangle's orientation but leaves the other \(r-1\) orientations free; the count is also \(2^{r-1}\). This completes all cases.

## Verification

The included standalone `verify.py` enumerates feasible nonnegative integer points independently from the defining adjacent inequalities for each \(2\le d\le8\), \(1\le s\le4\). Exact integer arithmetic compares squared radius (scaled by four), the number of contact lattice points, and the number of complementary contact-point pairs with all formulas. All 28 parameter cases passed; a total of 74,364 feasible integer points were enumerated. These finite checks test the formulas and their boundary cases, but the preceding proof establishes the universal real-polytope theorem.

## Relationship to prior work

Jiang, Wen, and Zhong introduced and analyzed the alternating adjacent-sum family via transfer matrices, lattice-point counts, Ehrhart series, volumes and Gorenstein properties; in particular they identify the \(s=1\), even-dimensional product of triangles. Product containment and the elementary independent-set Fibonacci recurrence are known ingredients, **not themselves new claims**. The contribution here is the complete Euclidean minimum-enclosing-sphere contact classification, exact parity-dependent and parameter-dependent contact counts, and all diametral-pair configurations in this family. General literature on circuit diameter of combinatorial polytopes concerns graph/circuit paths rather than Euclidean distances. Full text of the motivating 2026 preprint could not be independently inspected for this comparison; originality is therefore subject to a residual source-coverage risk.

## Limitations

This does not classify intrinsic volumes, John ellipsoids, general cyclic variants, arbitrary real values of the twist parameter, or higher-dimensional projection behavior. The theorem applies only to the noncyclic system and positive integer \(s\). The simple enclosing radius is determined by a known product relaxation; the new result is the equality-case geometry and exact counts. Similar contact classifications could exist in unindexed or inaccessible literature. No independent mathematical audit has been performed.

## References

1. Xinru Jiang, Suzhen Wen, Yueming Zhong, *Alternating adjacent-sum polytopes: transfer matrices and Ehrhart series*, arXiv:2607.14887v1 (first public 2026-07-16), https://arxiv.org/abs/2607.14887.
2. Anna Kafer, Kanstantsin Pashkovich, Laura Sanità, *On the Circuit Diameter of Some Combinatorial Polytopes* (2017), https://arxiv.org/abs/1709.09642. Relevant only as a distinction between circuit/edge distances and Euclidean metric diameter.
3. E. W. Weisstein, *Independent Vertex Set*, MathWorld, https://mathworld.wolfram.com/IndependentVertexSet.html. Reference for the classical path-independent-set Fibonacci recurrence.
