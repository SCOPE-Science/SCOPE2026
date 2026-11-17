# A sharp moving-boundary target law for endpoint-uniform circular chords

## Finding

Let \(X,Y\) be independent arclength-uniform points on the unit circle, and let \(C=[X,Y]\). For \(0<\varepsilon<1\) and \(0\le r\le 1-\varepsilon\), write
\[
H(r,\varepsilon)=\Pr\bigl(C\cap\overline B((r,0),\varepsilon)\ne\varnothing\bigr).
\]
For every fixed \(r\in[0,1)\), with \(K(k)=\int_0^{\pi/2}(1-k^2\sin^2t)^{-1/2}\,dt\),
\[
H(r,\varepsilon)=\frac{4K(r)}{\pi^2}\varepsilon+O_r(\varepsilon^3).
\]
The intensity \(4K(r)/\pi^2\) is strictly increasing in \(r\), and it diverges logarithmically at the unit-circle boundary. More sharply, for \(r=1-\lambda\varepsilon\) with any \(1\le\lambda\le\Lambda<\infty\), uniformly in \(\lambda\),
\[
\boxed{H(1-\lambda\varepsilon,\varepsilon)=\frac{2\varepsilon}{\pi^2}\left[\log\frac1\varepsilon+\log8+1-\frac{G(\lambda)}2\right]+O_\Lambda\!\left(\varepsilon^2\log\frac1\varepsilon\right),}
\]
where
\[
G(\lambda)=(\lambda+1)\log(\lambda+1)-(\lambda-1)\log(\lambda-1),
\]
with \(0\log0=0\). In particular, a disk internally tangent to the sampling circle (\(\lambda=1\)) satisfies
\[
H(1-\varepsilon,\varepsilon)=\frac{2\varepsilon}{\pi^2}\left[\log\frac1\varepsilon+1+\log4\right]+O\!\left(\varepsilon^2\log\frac1\varepsilon\right).
\]

There is also a conditional *marked* law. Represent the supporting line of \(C\) by its normal \((\cos\theta,\sin\theta)\), \(0\le\theta<\pi\), and its signed displacement \(s\), so the line is \(x\cos\theta+y\sin\theta=s\). Set
\[
\alpha=\min(\theta,\pi-\theta),\quad B={\bf1}_{\{\theta>\pi/2\}},\quad W_\varepsilon=\frac{2\log(1/\alpha)}{\log(1/\varepsilon)},\quad U_\varepsilon=\frac{s-(1-\lambda\varepsilon)\cos\theta}{\varepsilon}.
\]
Conditional on interception, the joint distribution of \((B,W_\varepsilon,U_\varepsilon)\) converges **in total variation** to the product of a fair Bernoulli variable, a uniform variable on \((0,1)\), and a uniform variable on \((-1,1)\). This is for each fixed \(\lambda\ge1\); the same statement is valid uniformly over any compact \(\lambda\)-interval within \([1,\infty)\).

## Assumptions and scope

The two endpoints are independent with normalized circular arclength measure. The target is a closed Euclidean disk entirely inside the unit disk; tangency is permitted. Equalities at the measure-zero boundary of the interception event do not affect the probability. The endpoint labels do not affect the unoriented chord. \(\varepsilon\downarrow0\) means a sequence of strictly positive radii tending to zero; in the moving-boundary regime \(\lambda\) is a fixed constant or varies in a bounded interval of \([1,\infty)\). No result is asserted here for targets protruding outside the sampling circle, or for \(\lambda\to\infty\) simultaneously with \(\varepsilon\to0\) without further hypotheses.

## Proof

**1. Exact chord-line measure.** A sum-and-difference change of angular endpoint variables shows that \(\theta\) is uniform on \([0,\pi)\), independent of \(s\), and that \(s\) has the signed arcsine density \(\pi^{-1}(1-s^2)^{-1/2}\), \(-1<s<1\). Because the entire target disk lies in the unit disk, its interception by the chord segment is equivalent to interception by the supporting infinite line. Consequently, the exact identity is
\[
H(r,\varepsilon)=\frac1{\pi^2}\int_0^\pi\left[\arcsin(r\cos\theta+\varepsilon)-\arcsin(r\cos\theta-\varepsilon)\right]d\theta.
\tag{1}
\]
Equivalently, using the symmetry \((\theta,u)\mapsto(\pi-\theta,-u)\),
\[
H(r,\varepsilon)=\frac{2\varepsilon}{\pi^2}\int_{-1}^1\int_0^{\pi/2}\frac{d\theta\,du}{\sqrt{1-(r\cos\theta+\varepsilon u)^2}}.
\tag{2}
\]

**2. Fixed interior target.** For fixed \(r<1\), the inverse-square-root integrand and its first two \(u\)-derivatives are uniformly bounded for sufficiently small \(\varepsilon\). Taylor expansion in \(\varepsilon u\), followed by the symmetric integral in \(u\), yields the leading term and \(O_r(\varepsilon^3)\). The angular integral is \(K(r)\). Differentiation under the integral shows \(K'(r)>0\) for \(0<r<1\), establishing strict off-center enhancement. The standard endpoint estimate \(K(r)=\log(4/\sqrt{1-r^2})+O((1-r^2)|\log(1-r^2)|)\) gives its logarithmic divergence.

**3. A uniform moving-target comparison.** Fix \(\Lambda\ge1\). Put \(r=1-\lambda\varepsilon\), \(\delta=\lambda-u\) and \(k=1-\varepsilon\delta\). For sufficiently small \(\varepsilon\), \(1\le\lambda\le\Lambda\), and \(-1\le u<\lambda\), we have
\[
r\cos\theta+\varepsilon u=k\cos\theta+\varepsilon u(1-\cos\theta).
\]
Since \(1-\cos\theta\le\sin^2\theta\) on \([0,\pi/2]\), the squared denominators obey
\[
1-(r\cos\theta+\varepsilon u)^2=\bigl(1-k^2\cos^2\theta\bigr)(1+O_\Lambda(\varepsilon))
\]
uniformly in \(\theta\). Thus, after integrating in \(\theta\), the integral in (2) equals
\[
\int_{-1}^1 K(1-\varepsilon(\lambda-u))\,du+O_\Lambda\!\left(\varepsilon\log(1/\varepsilon)\right).
\tag{3}
\]
Here the endpoint \(u=\lambda=1\) may have an infinite integrand, but it is a single measure-zero endpoint; the dominating logarithm is integrable in \(u\). The error estimate follows by bounding the integrated relative error with \(O_\Lambda(\varepsilon)\int_{-1}^1 K(1-\varepsilon(\lambda-u))du\).

Uniform elliptic-integral endpoint asymptotics for \(0<\delta\le\Lambda+1\) give
\[
K(1-\varepsilon\delta)=\frac12\log\frac1\varepsilon+\log(2\sqrt2)-\frac12\log\delta+O_\Lambda\!\left(\varepsilon\delta\,[1+|\log(\varepsilon\delta)|]\right).
\tag{4}
\]
The error integrates to \(O_\Lambda(\varepsilon\log(1/\varepsilon))\), because \(\delta|\log\delta|\) is integrable at zero. Finally,
\[
\int_{-1}^1\log(\lambda-u)du=G(\lambda)-2.
\]
Substitution of (4) into (3), then (2), proves the displayed two-term moving-boundary law with its stated uniform remainder, including the tangency case \(\lambda=1\).

**4. Total-variation marks.** On the interception event, \(-1\le U_\varepsilon\le1\). The joint density of \((\theta,U_\varepsilon)\), before conditioning, is
\[
\frac{\varepsilon}{\pi^2\sqrt{1-((1-\lambda\varepsilon)\cos\theta+\varepsilon U_\varepsilon)^2}}.
\]
For either branch \(B\in\{0,1\}\), set \(\alpha=\varepsilon^{w/2}\), so \(|d\theta/dw|=\alpha\log(1/\varepsilon)/2\). At every fixed \(0<w<1\) and \(-1<u<1\), \(\alpha\gg\sqrt\varepsilon\), and the denominator is asymptotic to \(\alpha\). Dividing by the interception probability from part 3 gives the pointwise limiting joint density \(1/4\) for each \(B\) on \((w,u)\in(0,1)\times(-1,1)\). That proposed limiting density has total mass \(2\cdot1\cdot2\cdot(1/4)=1\). Scheffé's lemma therefore yields convergence in \(L^1\), equivalently total variation, including disappearance of mass outside \(0<w<1\). Uniformity over \(\lambda\) in a fixed compact interval follows by uniformly bounding the density ratio on each strip \(\eta\le w\le1-\eta\) and observing that the total probability outside this strip is bounded by its limiting mass \(2\eta\) plus an error tending uniformly to zero. Letting \(\eta\downarrow0\) completes the uniform total-variation argument. This proves the product law.

## Verification

The accompanying `check_offcenter_chord.py` independently recomputes (1) by one-dimensional quadrature, checks the interior coefficient against a library implementation of \(K\), checks three successive shrinking scales in the moving-target expansion, and compares (1) with direct Cartesian endpoint simulations. Execute `python check_offcenter_chord.py` with NumPy and SciPy installed. On the tested inputs all assertions passed. These finite checks are supportive diagnostics; the limiting theorems follow from the proof, not from simulation.

## Relationship to prior work

Bertrand's chord paradox and classical line-measure geometry distinguish independently uniform endpoints from motion-invariant lines; the distinction is essential here. Bäsel (arXiv:1204.2707, first submitted 2012-04-12) treats motion-invariant random chords of regular polygons and point distances. Bortolotto and Souza (arXiv:2504.12866, first submitted 2025-04-17) derive radial laws for intersections of **two** independently sampled chord lines, not the interception of a **moving off-center target by one** endpoint-uniform chord. Bortolotto and Ramos (arXiv:2406.06771, first submitted 2024-06-10) study extremization of chord intersections in **concentric** disks, with a single-chord reduction, not the two-term moving-target intensity and its conditional angular law. The present claim is the explicit boundary-scale constant and marked total-variation law; the classical signed-arcsine chord measure and its elementary center-interception corollary are not asserted to be new.

## Limitations

Novelty is based on the identified literature and research-record comparisons, not a proof of priority across all historical texts. An early published account of the endpoint-uniform chord-distance distribution (Garwood and Holroyd, 1966) was available only as a publisher abstract, not in full. Informal discussions of shifted small targets also exist; therefore the elementary fixed-interior intensity by itself is not claimed as a priority discovery. No external mathematical audit is implied. The uniform remainder is only for bounded \(\lambda\ge1\), and a disk extending beyond the unit circle is outside the theorem. Endpoint sampling must be independent and arclength-uniform; the invariant-line chord model gives a different result.

## References

- U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707 (first public submission 2012-04-12); https://arxiv.org/abs/1204.2707.
- C. Bortolotto and V. Souza, *Intersections of random chords of a circle*, arXiv:2504.12866 (first public submission 2025-04-17); https://arxiv.org/abs/2504.12866.
- C. Bortolotto and J. P. G. Ramos, *On extremal problems associated with random chords on a circle*, arXiv:2406.06771 (first public submission 2024-06-10); https://arxiv.org/abs/2406.06771.
- F. Garwood and E. M. Holroyd, *The Distance of a “Random Chord” of a Circle from the Centre*, Mathematical Gazette 50 (1966), 283–286; https://doi.org/10.2307/3614676 (abstract inspected; full text unavailable).
- NIST Digital Library of Mathematical Functions, §19.12, asymptotics of complete elliptic integrals: https://dlmf.nist.gov/19.12.
