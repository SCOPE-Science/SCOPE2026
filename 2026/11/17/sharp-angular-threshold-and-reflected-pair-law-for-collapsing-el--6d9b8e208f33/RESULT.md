# Sharp angular-threshold and reflected-pair law for collapsing-ellipse Steiner triples

## Finding

For fixed \(\beta\in(\pi/2,\pi)\), sample three independent parameters \(\Theta_1,\Theta_2,\Theta_3\) uniformly on \([0,2\pi)\). Put \(P_i=(\cos\Theta_i,\varepsilon\sin\Theta_i)\), where \(0<\varepsilon\le1\), and let \(E_{\varepsilon,\beta}\) mean that all three interior Euclidean triangle angles are strictly smaller than \(\beta\). As \(\varepsilon\downarrow0\),

\[
\Pr(E_{\varepsilon,\beta})=\frac{6(-\cot\beta)}{\pi}\,\varepsilon+o(\varepsilon).
\]

In particular, for \(\beta=2\pi/3\), the event is equivalent, up to a probability-zero boundary, to the three-terminal Euclidean Steiner minimal tree having an interior degree-three junction, and its probability is asymptotic to \(2\sqrt3\,\varepsilon/\pi\).

There is also a **marked total-variation limit**. On \(E_{\varepsilon,\beta}\), select the pair of indices \(i<j\) minimizing \(|\Theta_i+\Theta_j-2\pi|\), using lexicographic tie-breaking, let \(k\) be the remaining index, and define \(H_{\varepsilon}=(\Theta_i+\Theta_j-2\pi)/\varepsilon\). Conditionally on \(E_{\varepsilon,\beta}\), the joint law of \((\{i,j\},\Theta_i,H_{\varepsilon},\Theta_k)\) tends in total variation to four independent marks: a uniform choice among the three unordered pairs, a uniform \([0,2\pi)\) variable, a uniform \((-2\kappa,2\kappa)\) variable, and another uniform \([0,2\pi)\) variable, where \(\kappa=-\cot\beta>0\). Thus the rare event localizes two points near opposite eccentric anomalies with a universal, uniform scaled reflection mismatch. Their two limiting angles, as an unordered pair, are \(\{\pi/2-\arctan(H/2),\pi/2+\arctan(H/2)\}\), and the remaining angle tends to zero.

## Assumptions and scope

All points are independently sampled by **uniform eccentric anomaly**, equivalently normalized equiaffine arclength, not Euclidean arclength or area. The ellipse has semiaxes \(1\) and \(\varepsilon\). The threshold \(\beta\) is fixed strictly between \(\pi/2\) and \(\pi\); the asymptotic is not asserted uniformly as \(\beta\) approaches an endpoint. Ties, coincident points and exactly threshold angles have probability zero. Total variation refers to the joint marked law on the same measurable state space (three pair indices times the three real/angular marks), not to unscaled point configurations.

## Proof

**1. Exact chord-direction identity.** For distinct \(\theta,\phi\), the chord vector is

\[
P(\phi)-P(\theta)=2\sin\frac{\phi-\theta}{2}\left(-\sin\frac{\theta+\phi}{2},\varepsilon\cos\frac{\theta+\phi}{2}\right).
\]

Its absolute vertical-to-horizontal slope, with infinite value when horizontal displacement vanishes, is exactly \(\varepsilon|\cot((\theta+\phi)/2)|\).

**2. Uniform localization to reflected pairs.** Sort the three distinct first coordinates in increasing order. If both edges from the middle point have absolute slope at most \(q=\tan((\pi-\beta)/2)>0\), its angle is at least \(\pi-2\arctan q=\beta\); hence on \(E_{\varepsilon,\beta}\) some pair must have chord slope greater than \(q\). By the identity, \(|\tan((\Theta_i+\Theta_j)/2)|<\varepsilon/q\) for at least one pair. Since the parameter sum lies in \([0,4\pi)\), this means the sum is within \(2\arctan(\varepsilon/q)\le 2\varepsilon/q\) of \(0\), \(2\pi\), or \(4\pi\). The first and last cases require both angles to lie in intervals of length \(O_\beta(\varepsilon)\), so their joint probability is \(O_\beta(\varepsilon^2)\). Thus, except on a set of probability \(O_\beta(\varepsilon^2)\), the event is contained in the union of the three central bands

\[
B_{ij,\varepsilon}=\{|\Theta_i+\Theta_j-2\pi|\le 2\varepsilon/q\}.
\]

Intersections of two distinct central bands have probability \(O_\beta(\varepsilon^2)\), since their two independent linear sum restrictions each have width \(O_\beta(\varepsilon)\). This controls overcounting and the choice of marked pair.

**3. Local limit on each band.** For one fixed pair \(i<j\), change variables \(t=\Theta_i\), \(h=(\Theta_i+\Theta_j-2\pi)/\varepsilon\) and \(v=\Theta_k\). The Jacobian is \(\varepsilon\); the change is valid on the parameter domain whenever \(\Theta_j=2\pi-t+\varepsilon h\in[0,2\pi)\). Its excluded boundary strip has \(O_\beta(\varepsilon)\) measure in \(t\), hence contributes \(O_\beta(\varepsilon^2)\) to the original probability. Restrict \(h\) to the fixed compact interval \([-2/q,2/q]\).

For Lebesgue-almost every \((t,h,v)\) with \(\sin t\ne0\) and \(\cos v\ne\cos t\),

\[
P_j-P_i=\varepsilon\sin t\,(h,-2)+O(\varepsilon^2),
\qquad P_k-P_i=(\cos v-\cos t,O(\varepsilon)).
\]

It follows directly from unit direction vectors that the angle at \(k\) tends to zero and the two angles at \(i,j\) tend, as an unordered pair, to \(\{\pi/2-\arctan(h/2),\pi/2+\arctan(h/2)\}\). Therefore the indicator of \(E_{\varepsilon,\beta}\) converges pointwise almost everywhere to \(\mathbf1\{|h|<2\kappa\}\), with \(\kappa=-\cot\beta\). Note that \(2\kappa<2/q\) for every \(\beta\in(\pi/2,\pi)\), because \(\kappa=\cot(\pi-\beta)\) and \(q=\tan((\pi-\beta)/2)\).

**4. Probability and marked total variation.** In a central band the probability measure in \((t,h,v)\) is \(\varepsilon(2\pi)^{-3}\,dt\,dh\,dv\). Dominated convergence over the bounded box gives, for each one of the three pair labels,

\[
\Pr(E_{\varepsilon,\beta}\cap B_{ij,\varepsilon})
=\frac{\varepsilon}{(2\pi)^3}(2\pi)(4\kappa)(2\pi)+o(\varepsilon)
=\frac{2\kappa}{\pi}\varepsilon+o(\varepsilon).
\]

Summing the three pair contributions and using the \(O(\varepsilon^2)\) localization/overlap errors gives the stated constant. After dividing each band's absolutely continuous density by the event probability, the bounded densities converge almost everywhere to the product of the uniform limiting densities. Their integrals converge to one, so Scheffé's lemma gives convergence in \(L^1\), equivalently total variation. The mass of the excluded localization and overlap sets is \(o(\varepsilon)/\Pr(E_{\varepsilon,\beta})=o(1)\), completing the marked assertion.

The usual three-terminal Euclidean Steiner criterion says that an interior junction occurs exactly when every angle is strictly less than \(2\pi/3\); equality cases have zero probability here.

## Verification

The independent accompanying `verify.py` computes each Euclidean angle from the coordinates using dot products, checks the exact chord identity numerically, and estimates the normalized event probability by scrambled Sobol integration targeted at all three reflected-pair bands (with deterministic overlap tie-breaking). Its output tests three angle thresholds and three aspect ratios, with the smallest-aspect estimates close to the proved constants. These finite calculations corroborate the symbolic derivation but are neither exhaustive nor the proof of the limit. Reproduce with `python verify.py` after installing NumPy and SciPy.

## Relationship to prior work

Classical Fermat–Torricelli/Steiner theory supplies the \(120^\circ\) criterion, but not a probability for anisotropic boundary sampling. Romaskevich's 2013 elliptical billiard work treats incircle-center loci of deterministic periodic billiard triangles, not independent random vertices or angle-cap probabilities. Edelman and Strang (2015) analyze random triangle shape space and acute probabilities in Gaussian sampling, not the collapsing ellipse. Ivanov, Tropin and Tuzhilin (2016) study a different Hausdorff metric-space version of the Fermat–Steiner problem. Published exact acuteness laws for eccentric-anomaly-uniform ellipse triangles concern the critical endpoint \(\beta=\pi/2\), not any fixed threshold strictly above it; the known critical probability has a thinner \(\varepsilon^2\log(1/\varepsilon)\) scale. The reflected-pair linear law and its marked limit do not follow from that endpoint statement. A published spherical-latitude \(120^\circ\) result uses intrinsic spherical angles and a different sampling geometry.

## Limitations

No exact finite-\(\varepsilon\) closed-form probability is claimed, nor a second asymptotic coefficient or a threshold-dependent uniform remainder. The marked convergence holds for eccentric-anomaly sampling and fixed \(\beta\in(\pi/2,\pi)\); it is not asserted for perimeter-uniform ellipse samples or general oval collapse. Numerical checks cannot establish historical novelty. Historical priority remains open pending independent full-literature review, including public papers whose full text could not be fetched.

## References

1. O. Romaskevich, *On the incenters of triangular orbits in elliptic billiard*, arXiv:1304.7588 (first submitted 2013-04-29), https://arxiv.org/abs/1304.7588.
2. A. Edelman and G. Strang, *Random Triangle Theory with Geometry and Applications*, arXiv:1501.03053 (first submitted 2015-01-09), https://arxiv.org/abs/1501.03053.
3. A. Ivanov, A. Tropin and A. Tuzhilin, *Fermat–Steiner Problem in the Metric Space of Compact Sets endowed with Hausdorff Distance*, arXiv:1601.03852 (first submitted 2016-01-15), https://arxiv.org/abs/1601.03852.
4. Relevant public mathematical record: *Sharp dilogarithmic acuteness law for affine-uniform ellipse triangles*, published 2026; its record abstract establishes the \(90^\circ\) probability and not the fixed-above-right-angle law.
