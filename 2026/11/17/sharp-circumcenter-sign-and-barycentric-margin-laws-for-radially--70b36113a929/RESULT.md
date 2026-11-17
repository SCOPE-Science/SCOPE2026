# Sharp circumcenter sign and barycentric-margin laws for radially stretched regular simplices

## Finding
Let \(d\ge2\). Place the vertices of a nondegenerate Euclidean \(d\)-simplex at \(p_i=r_i v_i\), for arbitrary \(r_i>0\), where \(v_0,\ldots,v_d\) are the unit vertex directions of a regular \(d\)-simplex centered at the origin. Thus \(v_i\cdot v_j=-1/d\) for \(i\ne j\). Write \(c\) for the circumcenter and \(\lambda_i\) for its affine barycentric coordinates, \(c=\sum_i\lambda_i p_i\) and \(\sum_i\lambda_i=1\). Set \(n=d+1\), \(w_i=1/r_i\), \(U=\sum_iw_i\), \(V=\sum_iw_i^2\), \(B=\sum_i r_i\), \(\mu=B/U\), and \(\kappa=[n(2-d)+d\mu V]/U\). Then
\[
\lambda_i=\frac{d+\kappa w_i-d\mu w_i^2}{2n}.
\]
There is one positive threshold \(w_*\), specified exactly below, for which \(\lambda_i<0\) precisely when \(w_i>w_*\). Therefore, upon listing the radii in nondecreasing order, all negative circumcenter coordinates form an initial segment. Equality coordinates occur only at the threshold. In particular, the face(s) opposite vertices of the smallest radii are exactly those through which the circumcenter lies strictly outside the corresponding supporting halfspaces.

Moreover, write the radii in nonincreasing order \(r_{[1]}\ge r_{[2]}\ge\cdots\ge r_{[n]}\), retaining their corresponding barycentric coordinates, and put \(x=r_{[2]}/r_{[1]}\in(0,1]\). Then the **sharp fixed-ratio inequality** is
\[
\boxed{\lambda_{[2]}\ \ge\ \frac1{2d}+\frac{(d-1)(d+1)x^2}{2d(d+x)^2}.}
\]
Equality holds exactly when \(r_{[2]}=\cdots=r_{[n]}\) (up to possible relabelling of tied largest radii). Thus \(\lambda_{[2]}>1/(2d)\), and at least two barycentric coordinates of the circumcenter are strictly positive for every such simplex. The universal infimum \(1/(2d)\) is sharp but not attained: it is approached when one radius grows without bound and the others remain equal. For each \(k\in\{0,1,\ldots,d-1\}\), there exist radii for which precisely \(k\) barycentric coordinates are negative; no configuration has \(d\) or \(d+1\) negative coordinates.

## Assumptions and scope
The simplex is a full-dimensional Euclidean simplex, with a **fixed regular simplex of directions** and arbitrary strictly positive radial vertex scales. The circumcenter is the unique point equidistant from all vertices, not the center of the minimum enclosing ball. Its barycentric coordinates may be negative. This theorem does not assert the corresponding property for arbitrary simplices, arbitrary radial directions, or complete well-centeredness of all lower-dimensional faces. It applies in every integer dimension \(d\ge2\), including ties among radial lengths.

## Proof
**Nondegeneracy.** The only linear dependence among the regular directions is their sum \(\sum_iv_i=0\), and it spans the relation space. If \(\sum_i a_ip_i=0\) and \(\sum_ia_i=0\), then \(a_ir_i\) is independent of \(i\), say \(a_ir_i=t\). Consequently \(0=t\sum_i1/r_i=tU\), so every \(a_i=0\). The vertices are affinely independent.

**Exact barycentric coordinates.** Equidistance from all vertices gives a common value of \(r_i^2-2r_i(c\cdot v_i)\), say \(\tau\). Since \(\sum_iv_i=0\), summing \(2(c\cdot v_i)=r_i-\tau/r_i\) gives \(\tau=B/U=\mu\). Hence
\[
2(c\cdot v_i)=r_i-\mu/r_i.
\]
Put \(S=\sum_i\lambda_ir_i\). By the regular simplex Gram identity,
\[
c\cdot v_i=\frac{n\lambda_ir_i-S}{d},
\]
so \(2n\lambda_i=d+2S w_i-d\mu w_i^2\). Summing over \(i\) yields \(2n=nd+2SU-d\mu V\), hence \(2S=\kappa\), giving the formula.

**Initial-block sign classification.** The quadratic \(f(w)=d+\kappa w-d\mu w^2\) is strictly concave, has \(f(0)=d>0\), and tends to negative infinity as \(w\to\infty\), so it has exactly one positive root,
\[
w_* = \frac{\kappa+\sqrt{\kappa^2+4d^2\mu}}{2d\mu}.
\]
Since \(\lambda_i=f(w_i)/(2n)\), exactly the vertices with radius smaller than \(1/w_*\) have negative coordinates. The statement about opposite facets is the usual barycentric halfspace characterization.

**Sharp fixed-ratio bound.** Scale all radii so that \(r_{[2]}=1\), and denote the smallest reciprocal radius by \(x=w_{[1]}=r_{[2]}/r_{[1]}\). Thus \(w_{[2]}=1\) and the remaining \(d-1\) reciprocals are all at least \(1\). Consequently
\[
U\ge d+x,\qquad B\le d+1/x,\qquad V-U=\sum_i w_i(w_i-1)\ge -x(1-x).
\]
At the vertex with reciprocal radius \(1\), the barycentric formula becomes
\[
2n\lambda_{[2]}=d-\frac{n(d-2)}U+\frac{dB(V-U)}{U^2}.
\]
Since \(d\ge2\), all three displayed inequalities imply
\[
2n\lambda_{[2]}\ge d-\frac{n(d-2)}{d+x}-\frac{d(1+dx)(1-x)}{(d+x)^2}
=\frac nd+\frac{(d-1)n^2x^2}{d(d+x)^2}.
\]
Divide by \(2n\). Equality is possible exactly when every reciprocal other than the smallest equals \(1\), i.e. all radii but a potentially exceptional largest one are equal: these configurations make every step an equality. For \(x>0\) the extra term is positive. Letting \(x\downarrow0\) proves sharpness of the universal infimum.

**Number of negative coordinates.** The sign threshold and the strict positivity of the second-largest-radius vertex show at most \(d-1\) negative coordinates. All equal radii give none. For any \(1\le k\le d-1\), choose \(k\) radii equal to \(1\) and the remaining \(n-k\) radii equal to \(R\). As \(R\to\infty\), the barycentric coordinate at each short vertex tends to
\[
\frac{(d+2)k-d(d+1)}{2k^2}<0,
\]
while the long-vertex coordinates are positive by the previously proved positive-sign prefix and the fixed-ratio inequality. Choose a sufficiently large finite \(R\) to realize exactly \(k\) negative coordinates. This proves the complete signed-count spectrum.

## Verification
The accompanying `check_radial_simplex.py` reconstructs the regular directions numerically, solves directly for circumcenters and barycentric coordinates, and independently compares with the closed formulas. It tests dimensions \(2\) through \(8\), 10,500 random radial configurations, the exact fixed-ratio equality family, and all allowed negative-coordinate counts. It does not replace the analytic argument; the proof is valid for arbitrary dimension and positive radii.

## Relationship to prior work
VanderZee, Hirani, Guoy, Zharnitsky, and Ramos (2009), arXiv:0912.3097, develop general geometric and algebraic characterizations of well-centered simplices; in particular, their Proposition 11 gives a general determinant-based criterion. The present claim is **not** an independent general criterion for arbitrary simplices: it is a specialized and substantially sharper ordered-sign theorem, a sharp barycentric lower bound at a specified ratio, and a complete exterior-facet sign-count realization for the fixed regular-direction radial family. General circumcenter barycentric formulas, such as Westendorp's 2013 Cayley–Menger treatment, encompass computation of the individual coordinates but do not by themselves state these sharp inequalities or the attainable sign classification. Conventional triangle-angle classifications cover the planar case of positivity but not the all-dimensional quantitative inequality. No claim of independently certified historical priority is made.

## Limitations
The conclusion is specific to radial stretching about the centroid of a regular simplex of directions. The negative coordinates describe sidedness relative to individual facets; they do not assert that the circumcenter lies in a particular geometric cone. Existing general barycentric formulas can be specialized to produce the algebraic expression, so novelty is claimed for the sharp family-wide bound and sign structure, not merely for calculating a circumcenter. A relevant full 2010 dissertation by VanderZee could not be inspected during comparison; an equivalent earlier specialized theorem remains possible. Numerical testing is finite and independent expert verification has not been performed.

## References
1. E. VanderZee, A. N. Hirani, D. Guoy, V. Zharnitsky, E. Ramos, *Geometric and Combinatorial Properties of Well-Centered Triangulations in Three and Higher Dimensions*, arXiv:0912.3097, first submitted 2009-12-16. https://arxiv.org/abs/0912.3097
2. E. VanderZee, A. N. Hirani, D. Guoy, E. A. Ramos, *Well-Centered Triangulation*, SIAM Journal on Scientific Computing 31 (2010), 4497–4523, DOI 10.1137/090748214. https://doi.org/10.1137/090748214
3. G. Westendorp, *A formula for the N-circumsphere of an N-simplex*, April 2013. https://westy31.nl/Circumsphere/ncircumsphere.htm
4. E. B. VanderZee, *Well-centered meshing*, PhD dissertation, University of Illinois, 2010. https://www.ideals.illinois.edu/items/15648 (full text not inspected).
