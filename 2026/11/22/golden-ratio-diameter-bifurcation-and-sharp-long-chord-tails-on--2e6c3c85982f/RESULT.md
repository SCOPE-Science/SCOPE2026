# Golden-ratio diameter bifurcation and sharp long-chord tails on a truncated parabola

## Finding
For each \(a>0\), let \(\Gamma_a=\{P(t)=(t,t^2):-a\le t\le a\}\), and let \(U,V\) be independent random variables uniformly distributed on \([-a,a]\). Define \(L_a=\|P(U)-P(V)\|_2\), \(D_a=\max_{u,v\in[-a,a]}\|P(u)-P(v)\|_2\), and
\[
 a_*=\sqrt{\frac{11+5\sqrt5}{8}},\qquad
 w_a=\frac{a+\sqrt{a^2-2}}2,\qquad x_a=w_a-a
\]
(the last two quantities are used only for \(a\ge a_*\)). There is one sharp change of diameter-realizing pairs:

* For \(0<a<a_*\), \(D_a=2a\), and the unique unordered diametral pair has parameters \(\{-a,a\}\).
* For \(a=a_*\), there are exactly three unordered diametral pairs, with parameters \(\{-a,a\}\), \(\{x_a,a\}\), and \(\{-a,-x_a\}\).
* For \(a>a_*\), the last two pairs are the only diametral pairs and
  \[
  D_a=(2a-w_a)\sqrt{1+w_a^2}>2a.
  \]

The two-point distance has sharply different upper-tail exponents on either side of this geometric transition. For fixed \(a<a_*\),
\[
 \Pr(L_a>D_a-\varepsilon)=\frac{\varepsilon^2}{4a^2}+o_a(\varepsilon^2).
\]
For fixed \(a\ge a_*\), write
\[
 A_a=2\sqrt{1+w_a^2},\quad B_a=\frac{2w_a^2-1}{2w_a\sqrt{1+w_a^2}}>0,\quad
 C_a=\frac{4}{3a^2 A_a\sqrt{B_a}}.
\]
Then
\[
 \Pr(L_a>D_a-\varepsilon)=C_a\varepsilon^{3/2}+o_a(\varepsilon^{3/2}).
\]
At the transition the endpoint-pair region has order \(\varepsilon^2\), so the two endpoint/interior contact regions of order \(\varepsilon^{3/2}\) determine the leading probability.

The localization is also exact in its limit. Below \(a_*\), conditional on the upper-tail event and after ordering \(U<V\), the pair \(((U+a)/\varepsilon,(a-V)/\varepsilon)\) converges in total variation to normalized Lebesgue measure on \(\{(s,t):s,t\ge0,\ s+t<1\}\). At or above \(a_*\), the two diametral endpoint/interior contact types have limiting conditional probabilities \(1/2\) each. On the branch near \((U,V)=(x_a,a)\), the normalized variables
\[
 X=\sqrt{B_a/\varepsilon}\,(U-x_a),\qquad Y=A_a(a-V)/\varepsilon
\]
converge in total variation, conditionally on that branch and the upper-tail event, to normalized Lebesgue measure on \(\{(x,y):y\ge0,\ x^2+y<1\}\). The other branch follows by reflection. The strict and weak upper-tail events have the same probability because the distance law has no atoms at any threshold.

## Assumptions and scope
The curve has the exact Euclidean embedding \(P(t)=(t,t^2)\); the two samples are independent and uniform in the parameter \(t\), **not uniform by Euclidean arclength**. The parameter \(a\) is held fixed as \(\varepsilon\downarrow0\). The geometric diameter is the Euclidean diameter of the compact arc (equivalently, of its convex hull). The two distributions in the conditional conclusion are with respect to ordinary planar Lebesgue measure and are independent of which reflected branch is chosen. No uniform-in-\(a\) transition-window estimate is claimed.

## Proof
**1. Exact distance and reduction to endpoint pairs.** For \(-a\le u<v\le a\),
\[
 F(u,v):=\|P(v)-P(u)\|_2=(v-u)\sqrt{1+(u+v)^2}.
\]
For every fixed \(u\) and distance threshold \(\ell\ge0\), the equation \((v-u)^2(1+(u+v)^2)=\ell^2\) is a nonzero quartic equation in \(v\). Its solution set is finite, so the original distance law is atomless by Fubini. Write \(d=v-u>0\), \(s=u+v\). At a point with both coordinates strictly inside the interval, stationarity of \(F^2=d^2(1+s^2)\) in \(u\) and \(v\) would require simultaneously \(ds=1+s^2\) and \(ds=-(1+s^2)\), an impossibility. Therefore every positive maximum has at least one boundary coordinate. Reflection \((u,v)\mapsto(-v,-u)\) reduces both boundary edges to \(v=a\). Set \(w=u+a\in[0,2a]\). Then
\[
 F(u,a)^2=(2a-w)^2(1+w^2).
\]
Apart from \(w=2a\), whose distance is zero, its nonzero stationary points solve \(2w^2-2aw+1=0\). There are none if \(a<\sqrt2\). For \(a>\sqrt2\), the smaller positive root is a local minimum and the larger root \(w=w_a\) is the only interior local maximum; at \(a=\sqrt2\) the double root does not create a new maximum. Thus only \(w=0\) and \(w=w_a\) can attain the diameter.

**2. Exact golden-ratio tie.** Along the interior stationary branch, \(a=w+1/(2w)\) and \(2a-w=w+1/w\). Hence
\[
 F(w-a,a)^2-4a^2
 =\frac{(1+w^2)^3-(1+2w^2)^2}{w^2}
 =w^4-w^2-1.
\]
The right side is strictly increasing for \(w>1/\sqrt2\), with its unique zero at \(w^2=(1+\sqrt5)/2\). Substituting into \(a=w+1/(2w)\) yields \(a_*^2=(11+5\sqrt5)/8\). There are precisely the pair configurations stated above; the reflection-fixed endpoint pair is counted once, whereas the other maximizing pair produces a distinct reflected pair.

**3. Local upper tail below the threshold.** Work on the ordered half-square \(u<v\), where the joint probability density is \(1/(2a^2)\). The sole maximizer is \((-a,a)\). With \(\xi=u+a\ge0\) and \(\eta=a-v\ge0\), Taylor expansion gives
\[
 D_a-F(u,v)=\xi+\eta+O_a((\xi+\eta)^2).
\]
Compactness excludes all points outside any sufficiently small fixed neighborhood. Scaling \((\xi,\eta)=\varepsilon(s,t)\) and applying dominated convergence gives an event area \(\varepsilon^2(1/2+o(1))\). Multiplication by the ordered-pair density proves \(1/(4a^2)\) and the simplex limit in total variation.

**4. Local upper tail at and above the threshold.** At \((u,v)=(x_a,a)\), put \(h=u-x_a\), \(\tau=a-v\ge0\). Direct differentiation of the exact distance gives
\[
 \partial_vF(x_a,a)=A_a=2\sqrt{1+w_a^2},\qquad
 -\tfrac12\partial_{uu}F(x_a,a)=B_a=\frac{2w_a^2-1}{2w_a\sqrt{1+w_a^2}}.
\]
Both are positive for \(a\ge a_*\), and the first derivative in \(u\) is zero. Consequently
\[
 D_a-F(x_a+h,a-\tau)
 =A_a\tau+B_a h^2+O_a(|h|^3+|h|\tau+\tau^2).
\]
The reflected maximizer has the same expansion. In a sufficiently small fixed neighborhood, the remainder is bounded in magnitude by \((A_a\tau+B_a h^2)/2\) since \(\tau\ge0\); hence the rescaled event lies in a fixed bounded set. After \(h=\sqrt{\varepsilon/B_a}\,x\), \(\tau=(\varepsilon/A_a)y\), the local event converges to \(y\ge0,\ x^2+y<1\), whose Lebesgue area is \(4/3\). Each branch therefore contributes probability
\[
 \frac1{2a^2}\frac{4}{3A_a\sqrt{B_a}}\varepsilon^{3/2}(1+o(1)).
\]
There are two disjoint reflected branches, yielding the stated \(C_a\). At \(a=a_*\), the third, corner-type maximizer contributes only order \(\varepsilon^2\), hence does not affect the leading \(\varepsilon^{3/2}\) term. Compactness and strict local maximality again exclude other contributions. Rescaled indicators converge almost everywhere on bounded sets to the limit-region indicators; normalization gives convergence of conditional densities in \(L^1\), i.e. total variation. The branch symmetry makes their weights equal.

## Verification
The standalone `check_parabolic_diameter.py` (Python 3, NumPy, SciPy) evaluates the golden-ratio tie and local critical equations, compares the exact diameter to a dense two-dimensional sample of chords, and computes independent one-dimensional numerical integrals for the near-diameter probabilities. For \(a=1.4\) and \(a=1.9\), respectively, the ratios of numerical probability to the two proved leading terms at \(\varepsilon=0.003\) are approximately \(1.0028\) and \(1.0005\). It prints `PARABOLIC_DIAMETER_GOLDEN_TRANSITION_CHECKS_OK` on success. The theorem is established by the analytic proof above; numerical grids or quadrature are **not** exhaustive proofs and do not address the parameter-uniform transition.

Run using `python check_parabolic_diameter.py` with `numpy` and `scipy` available. No external data files are necessary.

## Relationship to prior work
The study of random chord lengths and point distances in classical convex shapes is developed by U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707 (2012). Its objects are motion-invariant line chords and interior-uniform distances of regular polygons, not endpoint-parameter-uniform pairs on a parabolic arc. M. Mayer and I. Molchanov, *A limit theorem for the maximal interpoint distance of a random sample in the unit ball*, arXiv:math/0605289 (first public version 2006), develops broad extreme-distance context and covers random balls and spherical samples; its specific results do not supply the parabolic finite-arc diameter transition or these two coefficients. Published work on nondegenerate smooth convex closed curves and on polygonal boundary pairs has different endpoint contact geometries. Neither a generic near-diameter method nor a known chord-density formula is asserted to establish priority over specialized unlocated parabolic-arc calculations.

## Limitations
This is a two-point, fixed-width, parameter-uniform arc theorem. It is not an assertion about uniformly arclength-sampled points, motion-invariant random lines, full parabolas, or an arbitrary quadratic arc under a non-isometric affine mapping. The model does not yield a complete global chord-length density or a uniform double scaling with \(a-a_*\) comparable to \(\varepsilon\). Priority against potentially unindexed specialized arc calculations is not independently certified, and the mathematics has not undergone independent peer review.

## References
1. U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, first version 12 April 2012, https://arxiv.org/abs/1204.2707.
2. M. Mayer and I. Molchanov, *A limit theorem for the maximal interpoint distance of a random sample in the unit ball*, arXiv:math/0605289, first version 11 May 2006, https://arxiv.org/abs/math/0605289.
