# Sharp tetrahedron-volume and normalized-volume transition in cube–octahedron hulls

## Finding
For every real \(h>0\), define the three-dimensional convex body
\[
P_h=\operatorname{conv}\bigl([-1,1]^3\cup\{\pm he_1,\pm he_2,\pm he_3\}\bigr),
\]
where \(e_i\) are the standard coordinate unit vectors. The largest determinant of a tetrahedron with **arbitrary four points of \(P_h\)** is exactly
\[
D(h):=6\max_{T\subset P_h}\operatorname{vol}_3(T)=
\begin{cases}
16,&0<h\le r,\\
h^2(h+3),&r\le h\le3,\\
2h^3,&h\ge3,
\end{cases}
\]
where \(r\in(1,2)\) is the unique positive root of \(r^2(r+3)=16\) (approximately \(1.821640164404\)). The volume of the body is
\[
\operatorname{vol}_3(P_h)=
\begin{cases}
8,&0<h\le1,\\
8h,&1\le h\le2,\\
4h^2,&2\le h\le3,\\
4h^3/3,&h\ge3.
\end{cases}
\]
Consequently, the *normalized* largest tetrahedron volume is
\[
\frac{\max_{T\subset P_h}\operatorname{vol}_3(T)}{\operatorname{vol}_3(P_h)}=
\begin{cases}
1/3,&0<h\le1,\\
1/(3h),&1\le h\le r,\\
h(h+3)/48,&r\le h\le2,\\
(h+3)/24,&2\le h\le3,\\
1/4,&h\ge3.
\end{cases}
\]
Its **unique global minimum** is \(1/(3r)\approx0.182985278787\), attained only at \(h=r\). Thus the minimizing parameter is strictly below \(h=2\), where \(P_h\) is a regular rhombic dodecahedron.

Every maximizing tetrahedron is vertex-supported when \(1<h<3\). In fact, for \(1<h<r\) there are exactly two, namely the two complementary regular cube tetrahedra with all four corners satisfying \(x_1x_2x_3=1\) or all four satisfying \(x_1x_2x_3=-1\). For \(r<h<3\) there are exactly eight, indexed by sign triples \(\varepsilon=(\varepsilon_1,\varepsilon_2,\varepsilon_3)\in\{-1,1\}^3\):
\[
\operatorname{conv}\{h\varepsilon_1e_1,h\varepsilon_2e_2,h\varepsilon_3e_3,(-\varepsilon_1,-\varepsilon_2,-\varepsilon_3)\}.
\]
At \(h=r\) precisely those ten vertex-supported tetrahedra maximize. This enumeration includes all nonvertex choices by exclusion, not just all quadruples of extreme points.

## Assumptions and scope
The Euclidean metric and volume are in ordinary three-dimensional Cartesian coordinates. The cube has side length two. The six axial points have distance \(h\) from the origin. For \(0<h\le1\) the body is the cube; for \(h\ge3\) it is the octahedron \(hB_1^3\); throughout \(1<h<3\) the body has exactly fourteen distinct vertices, comprising all eight cube corners and all six axial points. The maximal volume ranges over all tetrahedra contained in \(P_h\), including ones with vertices in faces or the interior. Equality classification is asserted only for \(1<h<3\), while maximal volume and normalized ratio cover all \(h>0\).

## Proof
**1. Vertex set and reduction to finitely many signed determinants.** When \(1<h<3\), the eight cube corners and six axial points are all extreme: an axial point is uniquely exposed by a corresponding coordinate functional, and a corner is uniquely exposed by its signed coordinate sum because \(3>h\). The converse is immediate from the convex-hull definition. For four points \(p_0,p_1,p_2,p_3\), write \(\Delta=\det(p_1-p_0,p_2-p_0,p_3-p_0)\). This signed determinant is affine in each argument separately. Decomposing arbitrary points into convex combinations of extreme points expresses \(\Delta\) as a convex combination of vertex-tetrahedron determinants. Hence the largest possible absolute value is attained at a four-vertex subset, and any global upper bound for every such subset also applies to arbitrary contained tetrahedra.

**2. An all-parameter exact polynomial certificate.** There are \(\binom{14}{4}=1001\) unordered vertex quadruples. Classify them by \(k\), the number of axial points (\(0\le k\le4\)). The following **sharp bounds hold for every real \(1\le h\le3\)**:
\[
\begin{array}{c|c|c}
k&|\Delta|\text{ bound }E_k(h)&\text{number of vertex quadruples attaining }E_k\text{ identically}\\\hline
0&16&2\\
1&4(h+1)&48\\
2&2h(h+2)&12\\
3&h^2(h+3)&8\\
4&2h^3&12
\end{array}
\]
Here "identically" means equality as polynomials throughout \([1,3]\), not merely equality at a selected point. The attached standalone `check_hull_tetra.py` constructs all \(1001\) determinant polynomials \(p(h)\) using integer arithmetic: each has degree at most three. For both signs and for the class-appropriate bound it forms \(q_\pm(h)=E_k(h)\pm p(h)\), substitutes \(h=1+2s\), and exactly converts \(q_\pm(1+2s)\) to degree-three Bernstein form
\[
q_\pm(1+2s)=\sum_{i=0}^3b_i^\pm\binom3i s^i(1-s)^{3-i},\quad0\le s\le1.
\]
It verifies \(b_i^\pm\ge0\) for every coefficient, using rational arithmetic, a total of \(1001\cdot2\cdot4=8008\) exact sign assertions. Since all basis functions are nonnegative on \([0,1]\), these finite symbolic inequalities certify the bound for **all** real \(h\in[1,3]\); no grid extrapolation occurs. The checker separately identifies all polynomials equal identically to a signed envelope. If a nonnegative Bernstein representation vanishes at an *interior* parameter \(0<s<1\), all its nonnegative coefficients must vanish, so accidental interior equality cases are impossible. Thus the displayed classwise attaining counts hold everywhere in \(1<h<3\).

**3. Comparison and explicit sharp maximizers.** The bounds \(E_1(h)<16\) throughout \(1<h<3\). For \(1<h\le2\), \(E_2(h)\le16\); for \(2\le h<3\), \(E_2(h)<E_3(h)\). For \(1<h<3\), \(E_4(h)<E_3(h)\). Hence the global determinant bound is \(\max\{16,h^2(h+3)\}\). The two cube tetrahedra attain the former bound, and the eight specified three-axis-plus-opposite-corner configurations attain the latter bound. The increasing function \(h^2(h+3)\) crosses \(16\) once, at \(h=r\), establishing the first two branches and all vertex-supported equality counts. For \(h\ge3\), the convex hull is the scaled coordinate octahedron, whose maximum tetrahedral determinant is \(2h^3\), attained by the four axial vertices with one antipodal pair and the other two points on distinct remaining axes. For \(0<h\le1\) the cube's maximum determinant is \(16\), as established by the \(k=0\) case or a direct cube-vertex enumeration.

**4. Why no nonvertex tetrahedron maximizes in the fourteen-vertex regime.** Among the two maximizing cube tetrahedra and the eight maximizing three-axis-plus-corner tetrahedra, no two distinct tetrahedra share three vertices; the checker tests every pair of their vertex index sets. Suppose a tetrahedron with at least one nonvertex point were maximizing. Express each of its four points as a convex combination of extreme points, including a decomposition with at least two distinct positive-weight vertices for the nonvertex point. Multiaffinity expresses its signed determinant as a positive-weight average of vertex-tetrahedron determinants. To attain maximal absolute value, every contributing term must have the same maximal signed determinant. Fixing contributing choices for the other three points gives two different maximal vertex tetrahedra sharing the same three vertices, a contradiction. A contributing repeated-vertex tuple would give determinant zero and likewise obstruct maximality. Thus all maximizing tetrahedra are precisely the enumerated vertex-supported ones.

**5. Polytope volume and normalized minimizer.** For \(1\le h\le2\), the cube plus six outward square pyramids decomposes \(P_h\) into disjoint interiors; each pyramid has base area \(4\) and altitude \(h-1\), yielding \(8+6\cdot4(h-1)/3=8h\). For \(2\le h\le3\), the octahedron \(hB_1^3\) plus eight disjoint corner pyramids decomposes \(P_h\); each corner triangle lies in a signed coordinate plane with intercept \(h\), and the total added volume is \(4h^2-4h^3/3\), giving \(4h^2\). These decompositions are consistent at \(h=2\) and the two extreme regimes \(h\le1\), \(h\ge3\). Dividing \(D(h)/6\) by these volumes yields the claimed five branches. They are constant, strictly decreasing, then strictly increasing, strictly increasing, and constant respectively. Hence \(h=r\) uniquely minimizes the ratio, at \(1/(3r)\).

## Verification
Run `python3 check_hull_tetra.py` with the Python standard library. It prints `CUBE_OCTAHEDRON_HULL_TETRAHEDRA_EXACT_PASS vertex_quadruples=1001 bernstein_nonnegative=8008 class_tight_counts=2,48,12,8,12 cube_maxima=2 axis_corner_maxima=8 three_vertex_overlap_pairs=0`. The enumeration, signed determinants, polynomial bounds, and pairwise overlap checks all occur in exact integer/rational arithmetic. Unlike numerical parameter sampling, the nonnegative Bernstein coefficients constitute a finite proof of each required polynomial inequality over the entire interval. The analytical convex-combination and volume-decomposition arguments are necessary steps beyond the finite check. No formal proof assistant or external certification is claimed.

## Relationship to prior work
A published analysis of the cube–octahedron **intersection** family \(K_c=[-1,1]^3\cap c B_1^3\) determines its maximum tetrahedral volume and a different sharp normalized minimum. That calculation is not the present convex-hull family: the bodies are related by polarity, \(K_h=h(P_h)^\circ\), but polar duality does not preserve volumes of largest contained tetrahedra or their volume fractions. Akopyan and Glazyrin establish general structural properties of maximal simplices in centrally symmetric polytopes, not this sharp family profile. Han, Yang, Sriamorn and Zong place the rhombic dodecahedron in the classification of three-dimensional parallelohedra. The exact determinant switching parameter, five-piece normalized profile, and equality classification are not stated in the inspected relevant materials. Historical priority beyond the checked sources is not guaranteed.

## Limitations
This is an exact result only for the specified three-dimensional cube–octahedron hull family. No classification is asserted for maximizing tetrahedra at \(h=1\) or \(h=3\); the formula for their maximal volume does cover those endpoints. The all-parameter determinant certificate relies on a standalone checker enumerating 1001 formal quadruples and checking 8008 exact coefficient inequalities. A separate full audit of that finite computation has not been performed. A general study of largest simplices in polytopes by Gritzmann, Klee and Larman could not be inspected in full, so historical priority remains provisional.

## References
1. M. Han, Q. Yang, K. Sriamorn and C. Zong, *Twofold Translative Tiles in Three-Dimensional Space*, first public arXiv submission 29 June 2021, arXiv:2106.15388. https://arxiv.org/abs/2106.15388 .
2. A. V. Akopyan and A. A. Glazyrin, *On maximum volume simplices in polytopes*, Periodica Mathematica Hungarica 69 (2014), 251–256. Author open-access text: https://users.mccme.ru/akopyan/papers/Akopyan-Glazyrin-Maximum-Volume.pdf .
3. *Sharp tetrahedral-volume profile in the cube–octahedron intersection family*, published mathematical record, 11 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-tetrahedral-volume-profile-in-the-cube-octahedron-intersec--9ba1a511dacf .
4. P. Gritzmann, V. Klee and D. Larman, *Largest j-simplices in n-polytopes*, Discrete & Computational Geometry (1995), DOI:10.1007/BF02574058. Historical-priority comparison limited to bibliographic records and abstract.
