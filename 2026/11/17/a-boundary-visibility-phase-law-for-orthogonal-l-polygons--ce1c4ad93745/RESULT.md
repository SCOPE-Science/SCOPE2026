# A boundary-visibility phase law for orthogonal L-polygons

## Finding

For any four strictly positive real lengths \(A,B,C,D\), let
\[
\mathcal L_{A,B,C,D}=([0,A+C]\times[0,B])\cup([0,C]\times[0,B+D]).
\]
Choose \(P,Q\) independently and uniformly by **Euclidean arclength** on the entire polygon boundary. A pair is visible when its closed Euclidean segment is contained in \(\mathcal L_{A,B,C,D}\). Write \(\ell=2(A+B+C+D)\) for the perimeter and \(r=AD/(BC)\). Define the unnormalized blocking integral
\[
J(A,B,C,D)=\begin{cases}
4AD+2AC+2BD-\dfrac{BC^2}{2D}-\dfrac{B^2C}{2A}-BC\log r,&r\ge1,\\[2mm]
4AD+AC+BD+\dfrac{DA^2}{2B}+\dfrac{AD^2}{2C}+AD\log(1/r),&r\le1.
\end{cases}
\]
The branches agree at \(r=1\). The **exact finite-parameter probability** that \(P,Q\) cannot see each other is
\[
\boxed{\Pr([P,Q]\not\subseteq\mathcal L_{A,B,C,D})=\frac{2J(A,B,C,D)}{\ell^2}.}\tag{1}
\]
This probability is strictly between \(0\) and \(1/2\). Both endpoints of this interval are sharp limits within the class; in particular, along the square-notch family \(A=D=1-t\), \(B=C=t\), the blocking probability tends to \(1/2\) as \(t\downarrow0\) and tends to \(0\) as \(t\uparrow1\).

The equality \(AD=BC\) is a **regularity transition** for (1). The two analytic branches match through first order across this hypersurface. Holding \(B,C,D\) fixed and varying \(A\) through \(BC/D\), they generically have different second derivatives; specifically
\[
\left.\partial_A^2(J_{r>1}-J_{r<1})\right|_{A=BC/D}
=-\frac{D(C-D)^2}{BC^2}.\tag{2}
\]
Therefore the full four-parameter probability is \(C^1\), but is not \(C^2\) at any transition point with \(C\ne D\).

There is a higher-order cancellation on the canonical square-notch family. Define \(v(t)=\Pr([P,Q]\subseteq\mathcal L_{1-t,t,t,1-t})\) for \(0<t<1\). Then
\[
\boxed{v(t)=1-\frac18\begin{cases}
4(1-t)-\dfrac{t^3}{1-t}-2t^2\log\!\dfrac{1-t}{t},&0<t\le\frac12,\\[2mm]
2(1-t)(2-t)+\dfrac{(1-t)^3}{t}+2(1-t)^2\log\!\dfrac{t}{1-t},&\frac12\le t<1.
\end{cases}}\tag{3}
\]
In particular \(v(1/2)=25/32\), the function is exactly \(C^3\) but not \(C^4\) at \(t=1/2\), and its sharp fourth-derivative jump is
\[
\boxed{v^{(4)}(1/2+)-v^{(4)}(1/2-)=-128.}\tag{4}
\]
All statements concern this boundary sampling and **not** the usual area-uniform Beer index.

## Assumptions and scope

All four lengths are strictly positive; arbitrary common scaling leaves the probability unchanged. The polygon has one reflex vertex \((C,B)\), is simply connected, and is the union of two closed axis-aligned rectangles. Its six boundary edges are measured once each, including the two interior-facing edges of the notch. Endpoint coincidences and corner points have arclength measure zero. A chord lying on the boundary is visible. The probability law is for independent uniform **one-dimensional arclength** endpoints; no area-uniform, invariant-line, or arbitrary affine-deformation law is claimed.

## Proof

**1. Only opposite outer arms can obstruct.** Decompose the six boundary edges into three classes. The horizontal/right group \(H\), of total length \(2A+B\), consists of: the right \(A\)-portion of the bottom edge; the right outer vertical edge of length \(B\); and the horizontal inward notch edge of length \(A\). The upper/left group \(V\), of total length \(2D+C\), consists of: the upper \(D\)-portion of the left edge; the upper outer horizontal edge of length \(C\); and the inward notch vertical edge of length \(D\). The remaining left/bottom edges have total length \(B+C\). Any pair drawn from a common horizontal strip \(y\le B\), or a common vertical strip \(x\le C\), is visible by convexity of that strip. Thus an invisible pair must have one point in \(H\) and the other in \(V\), in either order. The two orders have equal arclength measure, so we calculate one order and double it.

**2. Exact crossing criterion.** Write a point of \(H\) as \((C+a,B-b)\), with \(0\le a\le A\), \(0\le b\le B\), and a point of \(V\) as \((C-c,B+d)\), with \(0\le c\le C\), \(0\le d\le D\). The segment crosses the horizontal line \(y=B\) at parameter \(b/(b+d)\) and the vertical line \(x=C\) at parameter \(a/(a+c)\). Away from a null set of degenerate edge endpoints, it enters the missing open northeast quadrant precisely when
\[
\frac{b}{b+d}<\frac{a}{a+c},\quad\text{equivalently}\quad ad>bc.\tag{5}
\]
It cannot leave the outer rectangle, since the latter is convex.

**3. Four edge-pair integrals and exact integration.** The inward-facing horizontal and vertical notch edges automatically obstruct every opposite-group partner, except for measure-zero endpoint coincidences. Together, these contributions have arclength-product measure \(3AD+AC+BD\). The other four edge pairings yield the following measures of \(ad>bc\), using Lebesgue measure along the corresponding two edge parameters:
\[
\begin{array}{c|c|c}
\text{edge pairing}&AD\ge BC&AD\le BC\\\hline
(b=B,c=C)&AD-BC[1+\log(AD/(BC))]&0\\[1mm]
(b=B,d=D)&AC-BC^2/(2D)&DA^2/(2B)\\[1mm]
(a=A,c=C)&BD-B^2C/(2A)&AD^2/(2C)\\[1mm]
(a=A,d=D)&BC&AD[1+\log(BC/(AD))]
\end{array}\tag{6}
\]
For instance, the first entry integrates \(\mathbf1_{ad>BC}\) over \(0<a<A,0<d<D\), yielding \(AD-BC-BC\log[AD/(BC)]\) when \(AD>BC\). The last entry is its product-complement counterpart on \(0<b<B,0<c<C\); the middle two entries are elementary triangle/clipped-triangle areas. Adding the four entries to \(3AD+AC+BD\) gives the displayed branches of \(J\). Since the ordered boundary-pair measure is \(\ell^2\), the doubling of opposite endpoint orderings proves (1).

**4. Strict universal half-bound and its sharpness.** Only points from opposite groups can be blocked, so
\[
0<\Pr(\text{blocked})<\frac{2(2A+B)(2D+C)}{\ell^2}<\frac12,
\]
where the latter strict inequality holds because the remaining edge length \(B+C\) is positive, and \(2xy\le(x+y)^2/2\). Positivity follows from the pair of two inward-facing notch edges, both of positive length, all of whose cross-group segments enter the missing quadrant. For \(A=D=1-t,B=C=t\) as \(t\downarrow0\), each group has length approaching \(2\), the remaining boundary length approaches zero, and almost every opposite-group chord is blocked, by (5); hence the half-bound is sharp. The \(t\uparrow1\) zero limit follows by substituting into (3); it reflects the disappearance of the open missing quadrant, not a vanishing length of the opposite groups.

**5. Generic phase singularity.** Set \(z=AD/(BC)-1\) and, for comparison, extend the two branch expressions analytically across \(z=0\), with \(B,C,D\) fixed and \(A=BC(1+z)/D\). Direct Taylor expansion of the elementary formulas gives
\[
J_{r>1}-J_{r<1}=
-\frac{B(C-D)^2}{2D}z^2-\frac{B(C-D)}2z^3
+\left(\frac{BC}{3}-\frac{BD}{2}\right)z^4+O_{B,C,D}(z^5).\tag{7}
\]
Thus the values and first derivatives agree. Differentiate (7) twice with \(\partial_A z=D/(BC)\) to obtain (2). This also proves the claimed lack of second-order smoothness where \(C\ne D\). The case \(C=D\) has higher cancellation along slices fixing these lengths; no global higher-order regularity is asserted for the whole parameter hypersurface.

**6. Square-notch fourth derivative.** Substituting \(A=D=1-t\), \(B=C=t\) into (1), noting \(\ell=4\) and that \(AD\ge BC\) precisely when \(t\le1/2\), gives (3). Write \(h=t-1/2\). The analytic continuations of the two expressions for \(J\), denoted by \(J_<\) (used on \(t<1/2\)) and \(J_>\) (used on \(t>1/2\)), satisfy
\[
J_>(1/2+h)-J_<(1/2+h)=\frac{128}{3}h^4+O(h^6).\tag{8}
\]
Both are real analytic near \(h=0\), and (8) makes their derivatives through order three coincide while the fourth derivative differs by \(24(128/3)=1024\). As \(v=1-J/8\), the fourth-derivative jump is \(-128\), establishing exactly \(C^3\) and not \(C^4\) at the transition. Substitution gives \(J(1/2)=7/4\) and \(v(1/2)=25/32\).

## Verification

Run `python3 checker.py` using Python 3 and its standard library. The checker samples arclength on all six edges and determines visibility by the independently implemented horizontal/vertical crossing-time test for a straight segment. It compares six parameter configurations with the formula under explicit binomial sampling tolerances, verifies several values and inequalities for the square-notch family, and numerically checks the fourth-order analytic-extension separation. A successful run prints `BOUNDARY_L_VISIBILITY_CUSP_CHECK_OK`. The symbolic exact manipulations in the proof, not the finite samples, establish the theorem; no finite experiment proves the global formulas.

## Relationship to prior work

The Beer index of convexity is ordinarily defined with **area-uniform** endpoints, notably in Balko, Jelínek, Valtr and Walczak (initial public preprint 2014-12-04). Exact polygon visibility computations in Buchin, Kostitsyna, Löffler and Silveira (first public preprint 2014-02-23) and Abrahamsen and Fredslund-Hansen (2022) also work with area distributions or finite point sets. An independently published exact four-parameter **area-sampled** notched-parallelogram law and fixed-area optimizer covers that sampling model, and is explicitly not claimed here. In contrast, the arclength measure supported on the boundary is singular with respect to area measure, so an area integral cannot yield (1) by parameter substitution. García-Pelayo (first public preprint 2015-01-01) treats **invariant-line** multichord sampling in nonconvex polygons, a different probability law. The checked treatments do not state (1)–(4) for independently perimeter-sampled endpoints. These differences support, but cannot conclusively establish, historical priority.

## Limitations

The polygon is axis-aligned with a single right-angle reflex corner; freely oriented, curved, multiply notched and general polygonal domains are not treated. The generic second-derivative jump is proved on transverse \(A\)-slices; it is not a classification of every possible smooth transverse path. The higher-order cancellation and coefficient \(-128\) pertain to the stated one-parameter square-notch family. Historical originality is not independently certified, and a specialized older boundary-visibility computation may have escaped the searches. The finite numerical checks do not certify the continuum calculations.

## References

1. K. Buchin, I. Kostitsyna, M. Löffler, R. I. Silveira, *Region-Based Approximation of Probability Distributions (for Visibility Between Imprecise Points Among Obstacles)*, first arXiv posting 2014-02-23, arXiv:1402.5681; subsequently Algorithmica 81 (2019), 2682–2715. https://arxiv.org/abs/1402.5681
2. M. Balko, V. Jelínek, P. Valtr, B. Walczak, *On the Beer Index of Convexity and Its Variants*, first arXiv posting 2014-12-04, arXiv:1412.1769. https://arxiv.org/abs/1412.1769
3. R. García-Pelayo, *Computation of the Multi-Chord Distribution of Convex and Concave Polygons*, first arXiv posting 2015-01-01, arXiv:1501.00292. https://arxiv.org/abs/1501.00292
4. M. Abrahamsen, V. Fredslund-Hansen, *Degree of Convexity and Expected Distances in Polygons*, arXiv:2208.07106 (2022). https://arxiv.org/abs/2208.07106
5. *Sharp fixed-area Beer-index law for notched parallelograms*, public exact area-sampled result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-fixed-area-beer-index-law-for-notched-parallelograms--529f7fcacd94
