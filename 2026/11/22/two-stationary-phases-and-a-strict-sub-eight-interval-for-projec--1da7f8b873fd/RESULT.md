# Two stationary phases and a strict sub-eight interval for projection volumes of truncated cubes

## Finding
For every real \(1\le t\le3\), let
\[
K_t=[-1,1]^3\cap\{x\in\mathbb R^3:|x_1|+|x_2|+|x_3|\le t\},
\qquad
P(t)=\frac{\operatorname{vol}_3(\Pi K_t)}{\operatorname{vol}_3(K_t)^2},
\]
where the projection body is defined by \(h_{\Pi K_t}(u)=\operatorname{area}_2(K_t|u^\perp)\) for unit \(u\). Put
\[
(a(t),b(t),V(t))=\begin{cases}
\bigl(2(t-1)^2,\ \frac12[t^2-3(t-1)^2],\ \frac43[t^3-3(t-1)^3]\bigr),&1\le t\le2,\\
\bigl(4-2(3-t)^2,\ \frac12(3-t)^2,\ 8-\frac43(3-t)^3\bigr),&2\le t\le3.
\end{cases}
\]
Then the entire affine-invariant projection-volume profile is
\[
\boxed{P(t)=\frac{8\bigl(a(t)^3+12a(t)^2b(t)+24a(t)b(t)^2+16b(t)^3\bigr)}{V(t)^2}.}\tag{1}
\]
It has **exactly two stationary points in the open interval** \((1,3)\), which are a strict global minimum and a strict secondary local maximum:
\[
\begin{split}
t_-&=1.574113325170236\ldots,& P(t_-)&=7.917189532562040\ldots,\\
t_+&=2.141041397857023\ldots,& P(t_+)&=8.336138645560756\ldots.
\end{split}\tag{2}
\]
The first point is the unique zero in \((1,2)\) of
\[
Q_-(t)=4t^5-16t^4+16t^3+4t^2-10t+3,
\]
and the second is the unique zero in \((2,3)\) of
\[
Q_+(t)=2t^4-15t^3+27t^2+3t-25.
\]
In particular, the strict global maximum is \(P(1)=9\), and the canonical intermediate values are
\[
P(3/2)=\frac{127}{16},\qquad P(2)=\frac{207}{25},\qquad P(3)=8.
\]
There are **exactly two values** \(c_1,c_2\in(1,2)\), satisfying
\[
c_1=1.427976889505496\ldots<3/2<c_2=1.740468392507064\ldots,
\]
such that \(P(c_1)=P(c_2)=8\). Precisely on \((c_1,c_2)\) the normalized projection volume is strictly **less** than \(8\); on \([1,c_1)\cup(c_2,3)\) it is strictly greater than \(8\), and at \(t=3\) it equals \(8\). The interval of sub-eight values contains an open family of non-zonohedral truncated cubes, not only the regular truncated octahedron.

## Assumptions and scope
All geometric quantities are Euclidean; \(K_t\) is a full-dimensional centrally symmetric polytope for the full closed parameter interval. The volume of a centered zonotope with symmetric generators \(g_j\) means the volume of \(\sum_j[-g_j,g_j]\). The ratio \(P(t)\) is invariant under invertible affine changes of the original body, so the fixed cube normalization entails no loss when comparing affinely equivalent family members. The term *stationary point* means an interior zero of the first derivative, which exists and is continuous at \(t=2\). Endpoint \(t=3\) is not counted among interior stationary points.

## Proof
**1. Exact seven-generator projection body.** By symmetry \(K_t\) has six axial facets and eight facets with outward normals \(\sigma/\sqrt3\), \(\sigma\in\{-1,1\}^3\), except where some facet areas vanish at an endpoint. For \(1\le t\le2\), an axial facet such as \(x_1=1\) is the diamond \(|x_2|+|x_3|\le t-1\) of area \(2(t-1)^2=a(t)\). For \(2\le t\le3\), the corresponding axial facet is \([-1,1]^2\) less four disjoint isosceles right corner triangles of leg length \(3-t\); its area is \(4-2(3-t)^2=a(t)\).

A positive-octant diagonal facet lies in \(x_1+x_2+x_3=t\) and has area \(\sqrt3 b(t)\). For \(1\le t\le2\), subtract the three disjoint corner triangles at \(x_i>1\) from the full positive-octant triangle of side-coordinate \(t\), giving \(\sqrt3[t^2-3(t-1)^2]/2\). For \(2\le t\le3\), it is the triangle at the cut-off cube corner with coordinate leg length \(3-t\), of area \(\sqrt3(3-t)^2/2\). All areas match at \(t=2\).

Cauchy's projection formula gives
\[
 h_{\Pi K_t}(u)=\frac12\sum_{F}\operatorname{area}_2(F)|u\cdot\nu_F|
 =a(t)\sum_{i=1}^3|u_i|+b(t)\sum_{\sigma\in E}|\sigma\cdot u|,
\]
where \(E=\{(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)\}\) represents the four antipodal pairs of diagonal normals. Therefore
\[
 \Pi K_t=\sum_{i=1}^3[-a(t)e_i,a(t)e_i]+
 \sum_{\sigma\in E}[-b(t)\sigma,b(t)\sigma].\tag{3}
\]

**2. Exact zonotope determinant sum.** For any centered three-dimensional zonotope with generators \(g_1,\ldots,g_m\),
\[
\operatorname{vol}_3\Bigl(\sum_{j=1}^m[-g_j,g_j]\Bigr)
=8\sum_{1\le i<j<k\le m}|\det(g_i,g_j,g_k)|.
\]
For the seven vectors in (3), unordered triples with three, two, one, or zero axial generators contribute respectively \(a^3\), \(12a^2b\), \(12(2ab^2)\), and \(4(4b^3)\). Six remaining one-axial/two-diagonal determinants vanish. These \(1+12+12+4+6=35\) triples exhaust all possibilities and prove the numerator of (1), including endpoints by continuity.

**3. Denominator and exact rational profile.** On \([1,2]\), start from the octahedron \(\|x\|_1\le t\), volume \(4t^3/3\), and discard six disjoint portions outside the cube, of total volume \(4(t-1)^3\). On \([2,3]\), start from the cube, volume \(8\), and discard eight disjoint corner tetrahedra with combined volume \(4(3-t)^3/3\). This establishes \(V(t)\).

Expanding (1) yields two rational expressions (both denominators are strictly positive squares throughout the respective parameter intervals):
\[
 P_-(t)=-9\frac{4t^6-24t^5+60t^4-88t^3+72t^2-30t+5}{(2t^3-9t^2+9t-3)^2},\quad1\le t\le2,
\]
\[
 P_+(t)=9\frac{3t^6-54t^5+393t^4-1476t^3+2997t^2-3078t+1247}{(t^3-9t^2+27t-21)^2},\quad2\le t\le3.
\]
Their exact derivatives factor as
\[
 P_-'(t)=\frac{54t(t-1)Q_-(t)}{(2t^3-9t^2+9t-3)^3},\qquad
 P_+'(t)=\frac{108(t-3)^2Q_+(t)}{(t^3-9t^2+27t-21)^3}.\tag{4}
\]
The first cubic in the denominators is \(-3V(t)/4<0\); the second is \(3V(t)/4>0\). At the junction both expressions and their first derivatives agree, with \(P(2)=207/25\) and \(P'(2)=108/125\). Thus the junction introduces no third stationary point.

**4. Exactly one critical point per combinatorial regime.** The substitutions \(t=(1+2u)/(1+u)\) and \(t=(2+3u)/(1+u)\), respectively, biject \(u>0\) with the intervals \((1,2)\) and \((2,3)\). Direct expansion gives
\[
(1+u)^5Q_-\!\left(\frac{1+2u}{1+u}\right)
=-u^5-11u^4+2u^3+14u^2+7u+1,
\]
\[
(1+u)^4Q_+\!\left(\frac{2+3u}{1+u}\right)
=-16u^4-40u^3-24u^2-u+1.
\]
In descending powers, each polynomial has exactly one sign change. Descartes' rule of signs therefore gives **at most one** positive root in each case. Since \(Q_-(1)=1>0\), \(Q_-(2)=-1<0\), \(Q_+(2)=1>0\), and \(Q_+(3)=-16<0\), the intermediate-value theorem gives **exactly one** root in each interval. Formula (4) shows that \(P\) strictly decreases on \((1,t_-)\), increases on \((t_-,t_+)\), and decreases on \((t_+,3)\). Rational sign brackets are \(1.574<t_-<1.575\) and \(2.141<t_+<2.142\). The numerical values in (2) are evaluated from the uniquely specified algebraic roots and are not used to prove uniqueness.

**5. Sharp global extremes and the threshold interval.** The exact values are \(P(1)=9\), \(P(3/2)=127/16<8\), \(P(2)=207/25>8\), and \(P(3)=8\). Strict monotonicity implies precisely two crossings of \(8\), both in \((1,2)\), and that \(t_-\) is strictly below every parameter outside its minimizing branch. For a direct global upper-bound certificate on \([2,3]\), write \(u=t-2\in[0,1]\). The numerator of \(9-P_+(t)\), in the positive denominator \((t^3-9t^2+27t-21)^2\), has degree-six Bernstein coefficients
\[
18,\quad18,\quad\frac{108}{5},\quad\frac{153}{5},\quad36,\quad36,\quad36.
\]
All are positive, so \(P_+(t)<9\) on the whole closed interval. On \([1,2]\), the single-minimum shape gives \(P(t)\le\max\{P(1),P(2)\}=9\), with equality only at \(t=1\). Hence the global maximum is uniquely at the octahedron and the global minimum uniquely at \(t_-\). The two roots of \(P(t)=8\) are uniquely specified by the rational expressions above; their displayed decimal approximations are auxiliary.

The diagonal facets are noncentrally symmetric for every \(1<t<2\) except \(t=3/2\): their vertices are permutations of \((1,t-1,0)\), and central reflection about \((t/3,t/3,t/3)\) preserves the vertex set only when \(t=3/2\). Since a three-dimensional zonotope must have centrally symmetric faces, all these other \(K_t\) are nonzonotopes. Thus the sub-eight interval contains non-zonotopes as claimed.

## Verification
Run `python3 verify_profile.py` with SymPy; if NumPy and SciPy are installed, the same file additionally constructs the complete \(2^7\)-point signed-generator clouds at five representative rational parameters and computes their independent three-dimensional convex-hull volumes. The exact checks verify the full \(35\)-triple determinant partition, both rational and derivative identities as polynomial equalities, both Descartes transformations and endpoint signs, critical-root rational isolations, Bernstein positivity, and the known \(8128\) projection-body volume after doubling the regular truncated octahedron's coordinates. The actual output was `EXACT_ALGEBRA_AND_NUMERIC_HULL_PASS` followed by `DESCARTES_CERTIFIED_UNIQUE_CRITICAL_POINTS`. These finite exact identities, together with the geometric arguments and the analytic Descartes theorem, establish the continuum statement; finite hull sampling alone would not.

## Relationship to prior work
Saroglou's 2011 research (primary MSC 52A40) establishes sharp class-level bounds for the same normalized affine projection-body-volume invariant, including the three-dimensional zonoid upper bound \(8\). Its class bound does not provide the piecewise exact profile, non-zonoidal sub-eight interval, stationary-root equations, or exact cuboctahedron value. The 2014 paper by Gantapara, de Graaf, van Roij and Dijkstra introduces the equivalent interpolating family but studies thermodynamic phase behavior and asphericity, not projection-body volumes.

The published record *Two sharp brightness transitions and an exact anisotropy plateau in cube–octahedron intersections* determines directional extreme brightness in \(1<t<2\), but not the volume of the whole projection body; its brightness formula agrees with Step 1. *Exact random-silhouette law along the cube–octahedron interpolation* determines projected vertex counts, not projected-area-body volumes. *Sharp tetrahedral-volume profile in the cube–octahedron intersection family* concerns maximal contained tetrahedra, not the present invariant. *Sharp shadow-area extrema and projection-body volume of the regular truncated octahedron* already evaluates \(\operatorname{vol}_3(\Pi K_{3/2})=127\) in the present normalization (\(8128\) after doubling), and that value is used here as a cross-check, not offered as new. The contribution is the full parameter-wide projection-volume law and its two sharp stationary phases, including the strict sub-eight interval and the nonregular global minimum.

## Limitations
This theorem concerns exactly the cubic-symmetric three-dimensional polytope family and this one affine invariant. It does not optimize the invariant over all convex bodies, settle Petty's conjecture, or extend the two-critical-point classification to arbitrary truncations or higher dimensions. The 2011 Saroglou paper was available through its full bibliographic abstract and theorem descriptions but not through an accessible full manuscript during the comparison; an older unindexed exact family profile remains a residual historical-priority risk. A broad 2026 brightness manuscript was likewise accessible by its abstract, not full text. These access gaps do not supply evidence of noncoverage; the numerical and algebraic calculations require independent mathematical scrutiny before external certification.

## References
1. Christos Saroglou, *Volumes of projection bodies of some classes of convex bodies*, Mathematika 57 (2011), 329–353, first public 2011-06-20, DOI: https://doi.org/10.1112/S0025579311001860. Primary classification 52A40.
2. Christos Saroglou, *On the shape of a convex body with respect to its second projection body*, arXiv:1409.4347v1 (first public 2014-09-15), https://arxiv.org/abs/1409.4347.
3. Anjan P. Gantapara, Joost de Graaf, René van Roij and Marjolein Dijkstra, *Phase behavior of a family of truncated hard cubes*, arXiv:1412.2597v1 (first public 2014-12-08), https://arxiv.org/abs/1412.2597. Author-hosted complete text: https://web.science.uu.nl/scm/Articles/2015/Gantapara_JChemPhys_2015.pdf.
4. Noah Samuel Brannen, *Volumes of projection bodies*, Mathematika 43 (1996), 255–264, DOI: https://doi.org/10.1112/S002557930001175X.
5. Published research record (2026-11-17), *Two sharp brightness transitions and an exact anisotropy plateau in cube–octahedron intersections*, identifier `f41e9f8b3783`.
6. Published research record (2026-10-18), *Exact random-silhouette law along the cube–octahedron interpolation*, identifier `23b7c8205147`.
7. Published research record (2026-10-11), *Sharp tetrahedral-volume profile in the cube–octahedron intersection family*, identifier `9ba1a511dacf`.
8. Published research record (2026-11-08), *Sharp shadow-area extrema and projection-body volume of the regular truncated octahedron*, identifier `ef8f8ba8bf3f`.
