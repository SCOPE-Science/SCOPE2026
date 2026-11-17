# Two-term rare-area law and a marked boundary shape for three random great circles

## Finding

For three independent isotropic great circles on the unit sphere, the eight generic spherical triangular cells occur in four antipodal congruent pairs. Write \(A_1,A_2,A_3,A_4\) for the respective areas (one from each pair), so \(A_i>0\) and \(\sum_i A_i=2\pi\). Let \(M=\max_i A_i\). The sharp two-term near-hemisphere expansion is
\[\Pr\{M>2\pi-\varepsilon\}=\frac{\varepsilon^4}{168}\left(1-\frac{7\varepsilon^2}{330}+O(\varepsilon^4)\right),\qquad \varepsilon\downarrow0.\]
On this rare event the largest pair is unique. Put \(\eta=2\pi-M\), and call the other three areas \(B_1,B_2,B_3\) in a fixed sign-consistent ordering. Conditional on this event,
\[\left(\frac{\eta}{\varepsilon},\frac{B_1}{\eta},\frac{B_2}{\eta},\frac{B_3}{\eta}\right)\ \xrightarrow{\mathrm{TV}}\ (U,T_1,T_2,T_3),\]
with total-variation error \(O(\varepsilon^2)\). Here \(U\) is independent of \(T\), \(U\) has density \(4u^3\) for \(0<u<1\), and \(T\) has planar-simplex density
\[h(t_1,t_2,t_3)=\frac{21}{8\pi}\frac{(1-t_1)(1-t_2)(1-t_3)}{\sqrt{t_1t_2t_3}},\quad t_i>0,\quad t_1+t_2+t_3=1.\]
The density is with respect to \(dt_1dt_2\) with \(t_3=1-t_1-t_2\). These conditional marks describe the partition of the tiny total area outside the almost-hemispherical cell; the limit is not a symmetric Dirichlet distribution.

## Assumptions and scope

The great circles are independent and Haar-isotropic; equivalently their unit normal vectors are independent and uniform on \(S^2\), modulo independent sign choices. The sphere has curvature \(+1\), hence area \(4\pi\). Cell boundaries and nongeneric triple intersections are null events. The conditional law is on the ordinary finite-dimensional coordinate space \((0,1)\times\{t_1,t_2,t_3>0:\sum t_i=1\}\). Any fixed sign-consistent ordering of the three small cells is admissible, because their limiting joint law is symmetric. No assertion is made for nonisotropic normals, many circles, or non-spherical surfaces.

## Proof

**1. Joint density.** Choose oriented normals \(n_1,n_2,n_3\in S^2\) independently. Let \(x=n_1\cdot n_2\), \(y=n_1\cdot n_3\), \(z=n_2\cdot n_3\), and set \(a=\arcsin x\), \(b=\arcsin y\), \(c=\arcsin z\). In the positive-definite Gram region \(D=1+2xyz-x^2-y^2-z^2>0\), the Gram-correlation density is \((4\pi\sqrt D)^{-1}\). The eight cells come in antipodal pairs, and the four representative sign-sector areas are
\[A_1=\pi/2+a+b+c,\quad A_2=\pi/2+a-b-c,\quad A_3=\pi/2-a+b-c,\quad A_4=\pi/2-a-b+c.\]
These follow either by spherical orthant integration or by inclusion-exclusion for three signed hemispheres. They are positive and sum to \(2\pi\). The Jacobian from \((a,b,c)\) to \((A_1,A_2,A_3)\) has absolute determinant \(4\), and direct trigonometric factorization gives
\[D=4\prod_{i=1}^4\sin(A_i/2).\]
As \(\cos a=\sin((A_1+A_2)/2)\) and similarly for \(b,c\), the exact joint density on \(A_i>0,\sum_iA_i=2\pi\), relative to \(dA_1dA_2dA_3\), is
\[f(A)=\frac{\sin((A_1+A_2)/2)\sin((A_1+A_3)/2)\sin((A_1+A_4)/2)}{32\pi\sqrt{\prod_{i=1}^4\sin(A_i/2)}}.\]
This is a coordinate formulation of the classical joint angular distribution, not an independent novelty claim.

**2. Boundary expansion.** In the event \(A_1=2\pi-\eta\), put \(A_{j+1}=\eta t_j\) for \(j=1,2,3\), where \(t_j>0\), \(\sum_j t_j=1\). The Jacobian is \(\eta^2\). Using \(\operatorname{sinc}(v)=\sin(v)/v\), uniformly for all simplex marks as \(\eta\downarrow0\), one obtains
\[f(2\pi-\eta,\eta t_1,\eta t_2,\eta t_3)\eta^2=\frac{\eta^3}{64\pi}\,g(t)\left[1-\frac{\eta^2}{48}\left(1+\sum_jt_j^2\right)+O(\eta^4)\right],\]
where \(g(t)=\prod_j(1-t_j)/\sqrt{t_1t_2t_3}\). Uniformity follows from \(\operatorname{sinc}(v)=1-v^2/6+O(v^4)\) uniformly for \(0\le v\le\eta/2\); this remains valid near all simplex faces, since the factored singularity is explicit.

**3. Exact beta-integrals.** Relative to the symmetric \(\operatorname{Dirichlet}(1/2,1/2,1/2)\) law, \(g\) has weight \(\prod_j(1-t_j)\), and \(\int(t_1t_2t_3)^{-1/2}dt_1dt_2=2\pi\). Dirichlet rising-factorial identities give
\[\mathbb E\prod_j(1-T_j)=\frac4{21},\qquad
\frac{\mathbb E\left[\sum_jT_j^2\prod_j(1-T_j)\right]}{\mathbb E\prod_j(1-T_j)}=\frac{29}{55}.\]
Consequently \(\int g(t)dt=8\pi/21\) and the marginal deficit density is
\[p_\eta(\eta)=\frac{\eta^3}{168}\left(1-\frac{7\eta^2}{220}+O(\eta^4)\right).\]
Integrating from \(0\) to \(\varepsilon\) yields
\[\Pr\{A_1>2\pi-\varepsilon\}=\frac{\varepsilon^4}{672}\left(1-\frac{7\varepsilon^2}{330}+O(\varepsilon^4)\right).\]
For \(0<\varepsilon<\pi\), the four events \(\{A_i>2\pi-\varepsilon\}\) are disjoint, since the areas sum to \(2\pi\). Sign symmetry makes their probabilities equal. Multiplication by four proves the asserted law for \(M\).

**4. Marked convergence.** The leading joint measure in \((\eta,t)\) is proportional to \(\eta^3g(t)d\eta\,dt\). On \(0<\eta<\varepsilon\), set \(u=\eta/\varepsilon\) and normalize. The limiting density factors into \(4u^3du\) and \(h(t)dt\). The uniform relative \(1+O(\varepsilon^2)\) comparison from Step 2, including the normalizing constants, bounds the total-variation distance by \(O(\varepsilon^2)\). Conditioning on the union of four disjoint, sign-symmetric largest-cell events does not change this limit.

## Verification

The independent standard-library script `verify.py` checks the exact rational Dirichlet moments and both tail coefficients. It also samples generic triples of unit normals to test positivity and the Gram-to-area trigonometric identity, and checks the integrated exact-density-to-leading-density ratio by importance sampling at two small thresholds. The expected terminal message is `SPHERICAL_MAX_CELL_MARKED_TAIL_CHECKS_OK`. The code is a numerical/algebraic consistency check; the uniform analytic expansion and limit proof are in the preceding section.

## Relationship to prior work

Finch and Jones (2010 initial preprint; updated 2015) give integral descriptions of primal spherical-triangle perimeter and polar dual area; Philip (2015 manuscript) establishes general spherical-triangle area/perimeter distributions and their polarity relation. The exact joint angular distribution and its Gram-density reparametrizations are acknowledged as prior tools. The specific two-term largest-of-four antipodal-cell tail, its rational sixth-order correction, and the independent beta/simplex conditional area-partition limit with total-variation rate are not asserted in the inspected primary texts. The distinction is **not** simply the complete perimeter or area distribution, which was already studied. Other earlier work on small-perimeter or boundary-layer expansions might imply parts of this claim; publication priority has not been independently established.

## Limitations

The result requires exactly three independent isotropic great circles. Its asymptotic coefficients apply only at the rare-event endpoint \(M\uparrow2\pi\). It does not imply absolute-continuity or total-variation convergence for a larger number of circles, and it does not classify the full finite-threshold distribution of the maximal area. The argument relies on analytic asymptotics; numerical tests are supplementary. Full historical priority remains subject to expert review.

## References

1. S. R. Finch and A. J. Jones, *Random Spherical Triangles*, arXiv:1009.5329 (initial public preprint, September 27, 2010; later version December 21, 2015), https://arxiv.org/abs/1009.5329.
2. J. Philip, *The Area and Perimeter of a Random Spherical Triangle*, manuscript dated May 7, 2015, https://people.kth.se/~johanph/spherical.pdf.
3. R. E. Miles, *Random points, sets and tessellations on the surface of a sphere*, Sankhyā Ser. A 33 (1971), 145–174, cited in the above primary works; not independently inspected in full.
