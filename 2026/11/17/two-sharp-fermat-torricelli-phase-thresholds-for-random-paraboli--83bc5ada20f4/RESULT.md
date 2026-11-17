# Two sharp Fermat–Torricelli phase thresholds for random parabolic triangles

## Finding

Let \(a>0\) and independently choose three parameters uniformly from \([-a,a]\). Put the corresponding points on the Euclidean parabola \(P(t)=(t,t^2)\), and sort the parameters as \(X<Y<Z\). The shortest Euclidean network connecting the three points is either a two-edge tree with hub at one sampled point or a three-edge tree with an interior 120-degree Steiner junction. Let \(p_{\rm int}(a)\) be the latter probability, and let \(p_{\rm end}(a)\) be the probability that the two-edge hub is \(P(X)\) or \(P(Z)\), rather than \(P(Y)\).

Define
\[
a_0=\frac1{\sqrt3},\qquad
a_1=\frac{\sqrt3}{2}+\frac{2\sqrt6}{3},\qquad
q=\frac{\frac12+\sqrt2}{\sqrt3}.
\]
Then the network has its hub at \(P(Y)\) almost surely for \(0<a\le a_0\). For \(a_0<a\le a_1\), only the middle-hub and interior-junction topologies have positive probability. For \(a>a_1\), all three possibilities (middle hub, endpoint hub, interior junction) have positive probability. Both thresholds are sharp, and
\[
\boxed{p_{\rm int}(a_0+\delta)\sim \frac{48\,3^{1/4}}5\,\delta^{5/2}},\qquad
\boxed{p_{\rm end}(a_1+\delta)\sim \frac{8}{5a_1^3(3/2)^{1/4}}\,\delta^{5/2}}
\]
as \(\delta\downarrow0\). These constants are approximately \(12.6343105243\) and \(0.09263790397\), respectively.

The rare configurations admit joint conditional total-variation limits. At the first threshold, conditional on an interior junction, the variables
\[
\left(\frac{X+a}{\delta},\frac{a-Z}{\delta},\frac{Y}{\sqrt\delta}\right)
\]
converge to the uniform law on
\[
D_0=\{(u,w,v):u,w\ge0,\ u+w+(\sqrt3/2)v^2<2\},
\qquad\operatorname{vol}(D_0)=\frac{64}{15\,3^{1/4}}.
\]
At the second threshold, conditional on an endpoint hub, the two hub labels become equiprobable. Reflect the parameter triple by \(t\mapsto-t\) if the hub is the right endpoint. In the resulting left-hub coordinates, the variables
\[
\left(\frac{X+q}{\sqrt\delta},\frac{Y-X}{\delta},\frac{a-Z}{\delta}\right)
\]
converge to the uniform law on
\[
D_1=\{(v,u,w):u,w\ge0,\ u/2+w+\sqrt{3/2}\,v^2<1\},
\qquad\operatorname{vol}(D_1)=\frac{16}{15(3/2)^{1/4}}.
\]
The reflected label is asymptotically independent of the limiting coordinates.

## Assumptions and scope

The three samples are independent and **uniform in the parabola parameter** \(t\), not uniform by Euclidean arclength. They are almost surely distinct. The parabola is exactly \((t,t^2)\); scaling to other parabolas requires transforming the parameter range. All angles are Euclidean interior angles, and strict 120-degree inequalities are used. Equality has probability zero.

## Proof

**1. Exact angle reduction.** A chord joining \(P(s)\) to \(P(t)\) has slope \(s+t\). For ordered parameters \(x<y<z\), set
\[
A=\arctan(x+y),\qquad B=\arctan(x+z),\qquad C=\arctan(y+z).
\]
Then \(A<B<C\) and the three triangle angles, at left, middle, right, respectively, are
\[
\theta_L=B-A,\qquad\theta_M=\pi-(C-A),\qquad\theta_R=C-B.
\]
The Euclidean Fermat–Torricelli criterion says that an interior Steiner junction occurs exactly when all three angles are less than \(2\pi/3\); otherwise the unique minimizing hub is the vertex with angle at least \(2\pi/3\). At most one angle can meet that threshold.

**2. First threshold.** The greatest possible slope-angle spread is
\[
C-A\le\arctan(y+a)-\arctan(y-a)\le2\arctan a,
\]
with equality in the closure of the ordered parameter simplex only at \((x,y,z)=(-a,0,a)\). Therefore \(\theta_M\ge2\pi/3\) for every triple whenever \(a\le a_0=\tan(\pi/6)\). For \(a>a_0\) the strict reverse inequality occurs on an open set. Every endpoint angle is less than \(2\pi/3\) at least until the second threshold (proved next), so the first such open set produces interior Steiner junctions.

**3. Second threshold.** For a leftmost hub, \(\theta_L\) is maximized, for fixed \(x\), by taking \(y\downarrow x\) and \(z\uparrow a\). For \(x=-r\), \(0\le r\le a\), this limiting angle is
\[
F(r,a)=\arctan(a-r)+\arctan(2r).
\]
An angle at least \(2\pi/3\) is possible in the closure exactly when, for some \(r>1/(2\sqrt3)\),
\[
a\ge\frac{2\sqrt3\,r^2+r+\sqrt3}{2\sqrt3\,r-1}.
\]
Set \(s=\sqrt3\,r\). The right-hand side becomes \(\sqrt3(2s^2+s+3)/(3(2s-1))\), and has its unique positive minimum at \(s=1/2+\sqrt2\), equal to \(a_1\). The limiting maximizer is \((x,y,z)=(-q,-q,a_1)\). The reflected case gives the right hub. Thus no endpoint hub occurs for \(a\le a_1\), while each is achieved on an open set when \(a>a_1\). Middle hubs exist on an open set for every finite \(a\) (three sufficiently close parameters), and interior junctions exist on an open set whenever \(a>a_0\) (parameters near \((-a,0,a)\), where endpoint angles remain less than \(\pi/2\)). This proves all topology assertions.

**4. First onset and its marked limit.** Put \(a=a_0+\delta\) and use \(x=-a+\delta u\), \(z=a-\delta w\), \(y=\sqrt\delta\,v\). Taylor expansion at the unique maximizing configuration gives, locally uniformly for bounded marks,
\[
(C-A)-\frac\pi3
=\frac{3\delta}{4}\left(2-u-w-\frac{\sqrt3}{2}v^2+o(1)\right).
\]
The maximizing configuration is unique and the quadratic term is strictly negative, so the qualifying region is confined, for small \(\delta\), to a fixed compact set in these scaled variables. The ordered triple has constant Lebesgue density \(6/(2a)^3=3/(4a^3)\); the Jacobian is \(\delta^{5/2}\). Integrating the limiting sublevel domain gives
\[
\operatorname{vol}(D_0)=\int_{-\sqrt{4/\sqrt3}}^{\sqrt{4/\sqrt3}}
\frac12\left(2-\frac{\sqrt3}{2}v^2\right)^2dv
=\frac{64}{15\,3^{1/4}}.
\]
Multiplication by \(3/(4a_0^3)\) gives the first probability constant. The indicator densities converge in \(L^1\), and their total masses converge to the positive domain volume. Normalizing them proves the conditional total-variation limit.

**5. Endpoint onset and its marked limit.** Write \(x_0=-q\), \(a=a_1+\delta\), and introduce
\[
x=x_0+\sqrt\delta\,v,\qquad y=x+\delta u,\qquad z=a-\delta w.
\]
At the unique left-hub boundary maximizer, direct differentiation of \(\arctan(x+z)-\arctan(x+y)\) yields
\[
\kappa=\frac1{1+(a_1-q)^2}>0,\qquad
\frac1{1+4q^2}=\frac\kappa2,
\]
and the negative second derivative divided by \(2\kappa\) is exactly \(\sqrt{3/2}\). Consequently
\[
\theta_L-\frac{2\pi}{3}
=\kappa\delta\left(1-\frac u2-w-\sqrt{3/2}\,v^2+o(1)\right).
\]
Uniqueness and strict nondegeneracy again confine the qualifying marks to a bounded region. The volume is
\[
\operatorname{vol}(D_1)=\int_{-(3/2)^{-1/4}}^{(3/2)^{-1/4}}
\left(1-\sqrt{3/2}\,v^2\right)^2dv
=\frac{16}{15(3/2)^{1/4}}.
\]
The left-hub probability is asymptotic to \(3\operatorname{vol}(D_1)\delta^{5/2}/(4a_1^3)\). Reflection doubles it for all endpoint hubs and makes the two labels equiprobable. The same normalized-indicator argument gives joint total-variation convergence of the reflected marks and the independent label.

## Verification

The companion pure-standard-library `verify.py` checks the two exact threshold identities, a critical derivative identity, normalization integrals, and both rare-event constants against deterministic quasi-Monte-Carlo integrals of **the exact triangle-angle inequalities**. For \(\delta=0.001\), the computed onset ratios are approximately \(12.585982\) and \(0.09249346\), converging to \(12.63431052\) and \(0.092637904\). Running `python3 verify.py` prints `PARABOLIC_FERMAT_TWO_ONSETS_CHECKS_OK`. These numerical tests corroborate, but do not replace, the analytic proof above.

## Relationship to prior work

The classical Fermat–Torricelli 120-degree criterion is not new. Zachos (2014), especially Corollaries 1–2, reviews the interior-versus-absorbed criterion and derives weighted geometric constructions. Jahn, Kupitz, Martini and Richter (2014) analyze more general minsum location problems. Neither inspected study supplies the random three-point parabolic-arc topology diagram, the exact two interval thresholds or their marked \(5/2\)-power onset laws. A 2015 geometry discussion of a 120-degree triangle with one parabola vertex considers a fixed symmetric degenerating configuration; it does not establish any of the reported sampling laws. Published related work on random parabolic hull areas and on different sampled curves was also compared at statement level. Historical priority has not been independently certified.

## Limitations

The law applies to parameter-uniform sampling on a single symmetric finite parabola arc and to exactly three terminals. It is not an arclength-uniform law. It gives **near-threshold** probability asymptotics and limiting marked laws, not a closed formula for the three topology probabilities at all \(a\). Independent mathematical audit and definitive historical-priority assessment have not been performed.

## References

1. A. N. Zachos, *Two new analytical solutions and two new geometrical solutions for the weighted Fermat–Torricelli problem in the Euclidean plane*, arXiv:1406.6230, first submitted 24 June 2014, https://arxiv.org/abs/1406.6230 .
2. T. Jahn, Y. S. Kupitz, H. Martini, C. Richter, *Minsum Location Extended to Gauges and to Convex Sets*, arXiv:1410.3690, first submitted 14 October 2014, https://arxiv.org/abs/1410.3690 .
3. *Triangle in parabola*, Math Stack Exchange, question dated 29 January 2015, https://math.stackexchange.com/questions/1125013/triangle-in-parabola .
