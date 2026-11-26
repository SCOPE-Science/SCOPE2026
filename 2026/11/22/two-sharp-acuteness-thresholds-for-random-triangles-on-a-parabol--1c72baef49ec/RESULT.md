# Two sharp acuteness thresholds for random triangles on a parabolic arc

## Finding

For each real \(a>0\), choose three independent uniform parameters on \([-a,a]\), and join their images under \(P(t)=(t,t^2)\) to make a Euclidean triangle. Let \(p(a)\) denote the probability that all its angles are strictly acute. Define
\[
S(a)=\sqrt{a^2-1},\qquad R(a)=\sqrt{a^2-2}.
\]
Then \(p(a)=0\) for \(0<a\le1\). For \(1<a\le\sqrt2\), the exact probability is
\[
p(a)=\frac{S(a)^3+3S(a)-3a\operatorname{arcosh}(a)}{a^3}.
\]
For \(a>\sqrt2\), the exact probability is
\[
p(a)=\frac{S(a)^3+3S(a)-3a\operatorname{arcosh}(a)
-R(a)^3-6R(a)+6a\operatorname{arcosh}(a/\sqrt2)}{a^3}.
\]
The two cutoffs have different geometric meanings. A strictly acute inscribed triangle is possible exactly for horizontal half-widths \(a>1\). A triangle with an obtuse angle at its leftmost or rightmost parameter vertex is possible exactly for \(a>\sqrt2\). Neither strict event is possible at its own cutoff. Both transitions are sharp, with nonanalytic exponent \(5/2\). Explicitly,
\[
p(1+\delta)=\frac{8\sqrt2}{5}\,\delta^{5/2}+O(\delta^{7/2})
\quad(\delta\downarrow0),
\]
and if \(F(a)=[S(a)^3+3S(a)-3a\operatorname{arcosh}(a)]/a^3\), then
\[
F(\sqrt2+\delta)-p(\sqrt2+\delta)
=\frac{4\,2^{1/4}}5\,\delta^{5/2}+O(\delta^{7/2}).
\]
At the opposite extreme,
\[
p(a)=\frac{3\log a-3/2}{a^2}+\frac9{8a^4}+O(a^{-6})
\qquad(a\longrightarrow\infty).
\]
In particular \(p(a)>0\) for every \(a>1\), and the long-arc probability tends to zero.

A joint conditional shape law also holds at the first transition. For ordered parameters \(U<V<W\), set \(\delta=a-1\) and, conditional on acuteness, define
\[
(X,Z,Y)=\left(\frac{U+a}{2\delta},\frac{V}{\sqrt{2\delta}},\frac{a-W}{2\delta}\right).
\]
As \(a\downarrow1\), this triple converges in total variation to the uniform probability law on
\[
\mathcal D=\{(x,z,y):x\ge0,\ y\ge0,\ x+y+z^2<1\},
\qquad\operatorname{vol}(\mathcal D)=\frac8{15}.
\]

## Assumptions and scope

The sampling density is uniform in the horizontal parabola parameter \(t\), **not** Euclidean arclength. The curve is the entire compact arc \(\{(t,t^2):-a\le t\le a\}\). Triangles are formed from three independent samples, with coincident parameters and exact right angles being probability-zero events; all angle inequalities are strict. The preceding formula applies for every \(a>0\), with inverse hyperbolic cosine on its real domain. The first public supporting sources date to 2014 and 2015; the result here is a separate mathematical claim, not a claim of publication in those sources.

## Proof

**1. Chord-angle factorization.** Order the distinct samples \(u<v<w\), a permutation that leaves their distribution symmetric. The directed chord from parameter \(r\) to parameter \(s\) is \((s-r)(1,r+s)\). Thus the strict acuteness conditions at the left, middle and right vertices are respectively
\[
1+(u+v)(u+w)>0,\quad
1+(u+v)(v+w)<0,\quad
1+(u+w)(v+w)>0.
\]
The middle condition reverses sign because its two directed chords have oppositely signed horizontal components. An ordered triple occupies a constant density \(6/(2a)^3=3/(4a^3)\) on the region \(u<v<w\).

**2. The positive-product rectangle integral.** For \(z>0\), define
\[
H(z)=\begin{cases}z-1-\log z,&z>1,\\0,&0<z\le1.\end{cases}
\]
If \(s\in(0,A)\) and \(t\in(0,B)\), the planar area for which \(st>1\) is \(H(AB)\). Indeed, for \(AB>1\), integrating \(B-1/s\) over \(1/B<s<A\) gives \(AB-1-\log(AB)\); otherwise the area vanishes.

**3. Middle-angle measure and the first threshold.** Fix the middle parameter \(v\), and let \(s=-(u+v)\), \(t=v+w\). The middle vertex is acute exactly when \(s,t>0\) and \(st>1\). In the formal rectangle \(0<s<a-v\), \(0<t<a+v\) the eligible area is \(H(a^2-v^2)\). But the ordering constraints remove the strip \(t<2v\) when \(v>0\), or \(s<-2v\) when \(v<0\). Each removal has area \(H(2|v|(a-|v|))\). Consequently the ordered-volume of middle-acute triples is
\[
I_m(a)-2I_e(a),
\quad I_m(a)=\int_{-a}^a H(a^2-v^2)\,dv,
\quad I_e(a)=\int_0^a H(2v(a-v))\,dv.
\]
Since \(a^2-v^2\le a^2\), the first integral is positive if and only if \(a>1\), and no middle-acute triple exists at \(a=1\). For any \(a>1\), the ordered parameters \((-b,0,b)\) with \(1<b<a\) give a strictly acute triangle and hence have an open acute neighborhood. The second integral is positive if and only if \(a>\sqrt2\), since \(\max_{0\le v\le a}2v(a-v)=a^2/2\).

**4. Endpoint-angle exclusion and the second threshold.** Suppose the angle at \(u\) is obtuse. Necessarily \(u=-p<0\), \(u+v<0\), and \(u+w>0\). Define \(s=-(u+v)\) and \(t=u+w\). For fixed \(p\in(0,a)\), the geometric ordering gives exactly \(0<s<2p\) and \(0<t<a-p\); the obtuseness inequality is \(st>1\). Its volume is precisely \(I_e(a)\). By the reflection symmetry \(t\mapsto-t\), the angle at \(w\) has the same obtuse-event volume. The two endpoint-obtuse events cannot overlap and both lie within the middle-acute event, since a nondegenerate Euclidean triangle has at most one nonacute angle. It follows that the volume of all-acute ordered triples is **exactly**
\[
I_m(a)-4I_e(a).
\]
This subtraction is essential: subtracting just two endpoint volumes from the formal rectangle ignores the two ordering strips and yields an incorrect full law.

**5. Exact integration.** When \(a>1\), write \(s_0=\sqrt{a^2-1}\). The first integral equals
\[
I_m(a)=\int_{-s_0}^{s_0}[a^2-v^2-1-\log(a^2-v^2)]\,dv
=\frac43s_0^3+4s_0-4a\operatorname{arcosh}(a).
\]
When \(a>\sqrt2\), write \(r_0=\sqrt{a^2-2}\). The second equals
\[
I_e(a)=\int_{(a-r_0)/2}^{(a+r_0)/2}
[2v(a-v)-1-\log(2v(a-v))]\,dv
=\frac13r_0^3+2r_0-2a\operatorname{arcosh}(a/\sqrt2).
\]
Multiplying \(I_m-4I_e\) by \(3/(4a^3)\) gives the stated piecewise probability formula.

**6. Critical and long-arc behavior.** Put \(a=1+\delta\). On the middle-acute event, \(a^2-v^2>1\), so \(|v|<S(a)=O(\sqrt\delta)\). Also \((a-v-(u+a))(a+v)>1\) and \((a-v)(a+v-(a-w))>1\), since the two actual positive factors of the middle-angle product are bounded by \(a-v\) and \(a+v\). These inequalities force \(u+a=O(\delta)\) and \(a-w=O(\delta)\). In the scaled coordinates, expanding \((a-v-2\delta X)(a+v-2\delta Y)-1\) and dividing by \(2\delta\) gives \(1-X-Y-Z^2+o(1)\) uniformly on bounded sets. Ordering and the endpoint-angle inequalities hold for all sufficiently small \(\delta\) on bounded scaled sets with \(X,Y\ge0\). The scaled support domains have uniformly bounded extent, and their indicators converge outside a measure-zero boundary. Their normalized uniform densities thus converge in \(L^1\) by dominated convergence. The limiting volume is \(\operatorname{vol}\mathcal D=\int_{-1}^1(1-z^2)^2/2\,dz=8/15\).

For the stated quantitative probability remainder, the endpoint and ordering exclusions are zero near \(a=1\). Use \(H(1+q)=q^2/2+O(q^3)\) in \(I_m\) with \(q=S(a)^2-v^2\) on \([-S(a),S(a)]\). Integrating gives \(I_m(a)=8S(a)^5/15+O(S(a)^7)\). Multiplication by \(3/(4a^3)\), with \(S(a)^2=2\delta+\delta^2\), yields \(8\sqrt2\,\delta^{5/2}/5+O(\delta^{7/2})\).

At \(a=\sqrt2+\delta\), the newly nonzero endpoint exclusion \(I_e\) has local form \(\int_0^{r_0}[(r_0^2-z^2)^2/8+O(r_0^6)]\,dz=r_0^5/15+O(r_0^7)\), where \(r_0^2=a^2-2\). Hence \(3I_e/a^3=(4\,2^{1/4}/5)\delta^{5/2}+O(\delta^{7/2})\). Finally, Taylor expansion of the radicals and \(\operatorname{arcosh}(a)=\log(a+\sqrt{a^2-1})\) in the exact formula gives \((3\log a-3/2)/a^2+9/(8a^4)+O(a^{-6})\).

## Verification

A standalone Python standard-library checker is supplied in `check_parabolic_acuteness.py`. It tests the exact angle factorization against Euclidean vector dot products, independently numerically integrates the two positive-product area formulas, compares the resulting probabilities to deterministic-seed Monte Carlo experiments at eight arc sizes, and checks both critical coefficients, the large-arc asymptotic, and the limiting-body volume. It prints `PARABOLIC_ARC_ACUTENESS_CHECKS_OK` upon success. The analytic integrations and domination arguments above, not the finite simulations, establish the theorem.

## Relationship to prior work

Kim–Kim–Kim–Park (2014), *Area of triangles associated with a curve II*, studies local areas and tangent-triangle identities characterizing parabolas; its triangle object and conic geometry motivate the setting, but its main theorems concern area ratios rather than random inscribed-triangle angles. Edelman–Strang (2015), *Random Triangle Theory with Geometry and Applications*, develops the probability of acuteness under Gaussian vertex/shape-space sampling, not three independent uniform parameters on a parabolic arc. The dated texts and the public comparison records listed below do not imply the exact two-threshold law. The separate affine-uniform ellipse result samples uniformly in eccentric anomaly on a closed curve. It does not give this parabolic law, and acuteness is not invariant under a general affine map. The same parabolic sampling model also appears in a study of circumradius tails, rather than of acute-angle events. Searches cannot establish absolute priority, and older unindexed treatments of parabola-inscribed triangles remain a material risk.

## Limitations

The law is Euclidean and uses independent uniform horizontal parameters. It is not an arclength-uniform result, does not cover higher polynomial graphs or arbitrary convex curves, and does not determine a maximizing arc size explicitly. The conditional limit is proved only at the onset \(a\downarrow1\), not at all transition windows. The supplied numerical tests are not a formal proof certificate, and the literature comparison is not exhaustive.

## References

1. D.-S. Kim, W. Kim, Y. H. Kim, D. H. Park, *Area of triangles associated with a curve II*, arXiv:1404.2969v1, first public 2014-04-10. https://arxiv.org/abs/1404.2969
2. A. Edelman, G. Strang, *Random Triangle Theory with Geometry and Applications*, arXiv:1501.03053v1, first public 2015-01-09. https://arxiv.org/abs/1501.03053
3. Public comparison finding, *Sharp dilogarithmic acuteness law for affine-uniform ellipse triangles*, identifier `2026/11/2/SCOPE-sharp-dilogarithmic-acuteness-law-for-affine-uniform-ellipse-tri--a5911e351b92`. Distinct curve, not a coverage claim.
4. Public comparison finding, *Endpoint-driven Gamma and interior Gaussian fluctuations for random parabolic hulls*, identifier `2026/11/2/SCOPE-endpoint-driven-gamma-and-interior-gaussian-fluctuations-for-ran--77a979074148`. Distinct invariant.
5. [Two distinct endpoint laws for circumradii of random parabolic triangles](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-two-distinct-endpoint-laws-for-circumradii-of-random-parabolic-t--cbedc9fbaebb/RESULT.md).
