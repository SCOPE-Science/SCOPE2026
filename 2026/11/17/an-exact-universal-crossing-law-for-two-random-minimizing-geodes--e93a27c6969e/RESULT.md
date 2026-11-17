# An exact universal crossing law for two random minimizing geodesics on a flat cylinder

## Finding

For arbitrary \(L,H>0\), equip the flat cylinder
\[
C_{L,H}=(\mathbb R/L\mathbb Z)\times[0,H]
\]
with its intrinsic product metric and its normalized two-dimensional area measure. Choose four independent area-uniform points \(P_1,P_2,P_3,P_4\), connect \(P_1\) to \(P_2\) and \(P_3\) to \(P_4\) by their shortest geodesic segments, and let \(E\) denote transverse intersection of their relative interiors. Then
\[
\boxed{\Pr(E)=\frac{65}{216}-\frac{2\log 2}{9}
 =0.146893219134826968\ldots .}
\]
The value is independent of the circumference and height, **even as their ratio becomes arbitrarily extreme**. These two independently sampled minimizing arcs intersect at most once almost surely.

## Assumptions and scope

The cylinder has positive finite height and circumference, includes both boundary circles, and is intrinsically flat. All four endpoints are sampled independently from uniform area, not perimeter. Almost every endpoint pair has a unique minimizing arc; the exceptional diametrically opposite angular displacements have probability zero. Collinear, tangent, or coincident segments also occur with probability zero. The claim concerns intersections of intrinsic surface geodesics, not Euclidean straight-line chords through the ambient solid cylinder.

## Proof

**1. Unwrap the independent shortest arcs.** Write cylinder coordinates as \((x,y)\in(\mathbb R/L\mathbb Z)\times[0,H]\). For a pair of independent uniform endpoints, the unique shortest lift has horizontal increment \(U\), the nearest modulo-\(L\) representative of the endpoint angle difference. Translation invariance makes \(U\sim\operatorname{Unif}(-L/2,L/2)\), independent of the starting horizontal coordinate and the two vertical endpoints. The latter are independent \(\operatorname{Unif}(0,H)\). The two arcs provide independent copies of these variables.

Orient both arcs according to their labelled endpoints. Write their vertical increments as \(a=y_1-y_0\) and \(b=z_1-z_0\). Almost surely \(a,b\ne0\). The corresponding horizontal slopes with respect to \(y\) are \(U/a\) and \(V/b\). Let \(h\) be the overlap length of the two closed vertical-coordinate ranges, and set \(h=0\) when those ranges are disjoint. Relative horizontal position at the lower end of the overlap is uniform modulo \(L\) and independent of everything determining the slope difference. Along the overlap, that relative coordinate traverses an ordinary interval of length
\[
\ell=h\left|\frac Ua-\frac Vb\right|.
\]
Because \(h\le |a|\) and \(h\le |b|\),
\[
\ell\le |U|+|V|\le L.
\]
Consequently the relative coordinate hits a multiple of \(L\) at most once except on null events, and the conditional probability of transverse crossing is exactly \(\ell/L\). Thus
\[
\Pr(E)=\mathbb E\left[\frac hL\left|\frac Ua-\frac Vb\right|\right].\tag{1}
\]
This step also proves the almost-sure intersection multiplicity bound.

**2. Average horizontal increments.** Put \(A=|a|\), \(B=|b|\), and \(m=\min(A,B)\), \(M=\max(A,B)\). The two random slopes are independent centered uniform variables with respective half-ranges \(L/(2A)\), \(L/(2B)\). For independent centered uniform variables of half-ranges \(\alpha\ge\beta>0\), elementary conditioning gives
\[
\mathbb E|X-Y|=\frac\alpha2+\frac{\beta^2}{6\alpha}.
\]
Indeed, for fixed \(|Y|\le\alpha\), \(\mathbb E_X|X-Y|=(\alpha^2+Y^2)/(2\alpha)\), followed by \(\mathbb E Y^2=\beta^2/3\). Therefore
\[
\frac1L\mathbb E_{U,V}\left|\frac Ua-\frac Vb\right|=
\frac1{4m}+\frac{m}{12M^2}.\tag{2}
\]
The product \(h/m\le1\) keeps the apparently singular expression integrable.

**3. Compute the expected vertical overlap.** Rescale \(y\) by \(H\); crossing is unchanged under the resulting separate horizontal and vertical affine coordinate scalings, because minimizing arcs unwrap to straight segments with the same nearest horizontal lift and the same segment intersection topology. We henceforth take \(L=H=1\) without claiming the anisotropic map is an isometry. For a vertical interval of prescribed length \(A\in(0,1)\), the lower endpoint is uniform on \([0,1-A]\); in the joint density of the independent uniform original endpoints, the oriented/unoriented interval change of variables contributes \(2\,dA\,dl\). The two intervals together contribute \(4\,dA\,dB\,dl\,dk\).

For fixed lengths \(A,B\), integrate their overlap \(h\) over all valid lower endpoints and call the resulting quantity \(J(A,B)\):
\[
J(A,B)=\int_0^{1-A}\int_0^{1-B}
|[l,l+A]\cap[k,k+B]|\,dk\,dl.
\]
By Fubini, the allowable placement length for an interval of length \(A\) containing a given \(y\in[0,1]\) is
\[
g_A(y)=\min\{y,1-y,A,1-A\}.
\]
It follows that \(J(A,B)=\int_0^1g_A(y)g_B(y)\,dy\). If \(r=\min(A,1-A,B,1-B)\) and \(s=\max(\min(A,1-A),\min(B,1-B))\), elementary integration of the two trapezoidal profiles gives
\[
\boxed{J(A,B)=rs(1-s)-\frac{r^3}{3}.}\tag{3}
\]
In particular, \(J\) is symmetric in its arguments.

**4. Four-region exact evaluation.** Combining (1)–(3), changing from oriented intervals and using symmetry under \(A\leftrightarrow B\),
\[
\Pr(E)=8\int_0^1\int_A^1J(A,B)
\left(\frac1{4A}+\frac{A}{12B^2}\right)\,dB\,dA.\tag{4}
\]
Split its triangular integration domain into the four disjoint regions listed below (boundary lines have measure zero). On the first two regions \(J=AB(1-B)-A^3/3\); on the others use the expressions in the table. Integrate the rational polynomial integrands first in \(B\), then in \(A\). The resulting exact contributions, already including the outer factor \(8\), are:

| Region for \((A,B)\) | \(J(A,B)\) | Contribution |
|---|---|---|
| \(0<A<B<1/2\) | \(AB(1-B)-A^3/3\) | \(29/540\) |
| \(0<A<1/2,\ 1/2<B<1-A\) | \(AB(1-B)-A^3/3\) | \(-139/540+4\log(2)/9\) |
| \(0<A<1/2,\ 1-A<B<1\) | \(A(1-A)(1-B)-(1-B)^3/3\) | \(47/144-125\log(2)/288\) |
| \(1/2<A<B<1\) | \(A(1-A)(1-B)-(1-B)^3/3\) | \(77/432-67\log(2)/288\) |

Summing the four rows yields
\[
\frac{65}{216}-\frac{2\log 2}{9},
\]
proving the claimed exact value and universality. \(\square\)

## Verification

The accompanying self-contained script `verification/check_crossing.py` reproduces the four exact iterated integrals symbolically using SymPy, asserts their sum, verifies the elementary uniform-slope identity and tests an independent sample of actual geodesic intersections. The latter samples four independent points and two independent nearest horizontal lifts, compares relative horizontal lifts throughout the overlapping vertical ranges, and checks whether an integer multiple of the circumference is crossed. It tests several strongly different aspect ratios and checks observed crossing frequencies against the sharp exact value using a prespecified Monte Carlo tolerance. These finite experiments corroborate, but do not replace, the exact proof.

## Relationship to prior work

Artzrouni (2007, arXiv:0712.1477v1) studied crossings of independent fixed-length, random-direction agent steps in large planar domains and on spheres. The result \(2d_1d_2/(\pi A)\) is an approximation in a different sampling model, and does not supply the present exact finite-cylinder shortest-geodesic crossing law. Glorieux and Yarmola (2020, arXiv:2003.08190v1) computed the probability that a random **three-edge geodesic triangle** on a closed flat torus is null-homotopic. The published published-finding corpus result *Sharp crossing probability for independently sampled shortest geodesics on flat two-tori* concerns the genuinely closer two-segment crossing problem on a surface periodic in **both** coordinates. Its exact probability ranges between \(22/243\) and \(5/54\), unlike this finite cylinder's \(65/216-2\log(2)/9\); its torus-area determinant identity cannot be applied unchanged to a cylinder whose vertical coordinate has boundary and nonuniform displacement. A 2014 MathOverflow discussion addresses shortest geodesic intersection on the round sphere, where antipodal symmetry yields \(1/8\), again a different metric space and mechanism.

## Limitations

The result assumes a flat, finite, two-dimensional cylinder and four independent area-uniform endpoints. It does not cover nonuniform sampling, geodesics allowed to wind nonminimally, curved cylinders, vertical reflecting geodesics, or correlations involving three or more arcs. Priority is provisional: search coverage cannot exclude an unindexed equivalent formulation. No independent mathematical audit has been performed.

## References

1. M. Artzrouni, *Crossing paths in 2D random walks*, arXiv:0712.1477v1, first public December 10, 2007, https://arxiv.org/abs/0712.1477.
2. O. Glorieux and A. Yarmola, *Random triangles on flat tori*, arXiv:2003.08190v1, March 18, 2020, https://arxiv.org/html/2003.08190v1.
3. *Sharp crossing probability for independently sampled shortest geodesics on flat two-tori*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-crossing-probability-for-independently-sampled-shortest-ge--72270b2f5a6b.
4. *Probability of random geodesics on the round sphere intersecting*, MathOverflow, January 6, 2014, https://mathoverflow.net/questions/153700/probability-of-random-geodesics-on-the-round-sphere-intersecting.
