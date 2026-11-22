# Four sharp spacing regimes for a symmetric three-monitor smoke-plume transect

## Finding

A localized smoke plume is displaced laterally by uncertain wind. A three-monitor transect is constrained to have monitoring positions \((-d,0,d)\), with freely chosen half-spacing \(d\geq0\). Each monitor has the same threshold half-footprint \(r>0\), Gaussian center uncertainty with standard deviation \(\sigma>0\), and conditionally independent probability \(p\in(0,1)\) of issuing an alarm when the plume center lies in its footprint. A monitoring configuration succeeds when at least one instrument alarms.

Define \(q=1-p\) and \(\ell=-\sigma^2\log(q)/r\). The **unique** half-spacing maximizing the true-alarm probability over every \(d\geq0\) within this symmetric three-monitor design class is

\[
d_* = \begin{cases}
\ell, & 0<\ell\leq r,\\
r, & r\leq\ell\leq2r,\\
\ell/2, & 2r\leq\ell\leq4r,\\
2r, & \ell\geq4r.
\end{cases}
\]

All formulas agree at common boundaries. Consequently, as monitor reliability increases, the best spacing initially grows, remains **exactly pinned** at \(d=r\) over the nonzero interval \(1-e^{-r^2/\sigma^2}\leq p\leq1-e^{-2r^2/\sigma^2}\), grows again, and is finally pinned at \(d=2r\) for \(p\geq1-e^{-4r^2/\sigma^2}\). At \(r=\sigma\) the three change points are approximately \(0.63212056\), \(0.86466472\), and \(0.98168436\).

The first fixed-spacing plateau corresponds to the two outer footprints *just meeting each other at the middle instrument* while each still overlaps the middle footprint; the final plateau corresponds to three adjacent, nonoverlapping footprints. These are alternative layout regimes under one common true-detection objective, not claims about absolute field sensor calibration.

## Assumptions and scope

An illustrative Gaussian crosswind concentration profile at a fixed transport time \(t>0\) is \(C(x,t)=C_0(t)\exp[-(x-Z)^2/(4Kt)]\), with turbulent diffusivity \(K>0\), peak \(C_0(t)>0\), and uncertain center \(Z\sim N(0,\sigma^2)\). A threshold \(0<C_*<C_0(t)\) produces the half-footprint \(r=\sqrt{4Kt\log(C_0(t)/C_*)}\). The result also applies directly when the half-footprint \(r>0\) is specified without this physical parameterization. Three threshold monitors are located at \(-d,0,d\). Instrument \(j\) has footprint \([s_j-r,s_j+r]\), with \(r>0\). If \(Z\) lies in that footprint, its binary report is positive with probability \(p\), independent of the other instruments conditional on \(Z\); outside its footprint a positive report is impossible. The layout maximizes \(\Pr(\text{at least one true positive report})\), with no cost penalty for spatial separation, no false-positive penalty and no model for plume dispersion or time evolution. Positions are restricted *a priori* to a symmetric equally spaced transect; the result does **not** claim unrestricted three-location optimality.

Write \(\varphi_\sigma(x)=e^{-x^2/(2\sigma^2)}/(\sqrt{2\pi}\sigma)\), \(\Phi_\sigma(x)=\int_{-\infty}^{x}\varphi_\sigma(u)\,du\), and \(M(a)=\Phi_\sigma(a)-\Phi_\sigma(-a)\) for \(a\geq0\).

## Proof

Conditional on \(Z=z\), if exactly \(k\) of the three footprints contain \(z\), the probability of at least one report equals \(1-q^k\). For the three equally spaced footprints, integrate that probability against \(\varphi_\sigma\). For \(0\leq d\leq r\), their union is \([-r-d,r+d]\), their twofold-or-more coverage region is the center footprint \([-r,r]\), and their threefold intersection is \([-r+d,r-d]\). The layer-cake identity \(1-q^k=p\sum_{i=0}^{k-1}q^i\) yields the exact objective

\[
F(d)=p\{M(r+d)+qM(r)+q^2M(r-d)\},\qquad 0\leq d\leq r.
\]

For \(r\leq d\leq2r\), the outer footprints no longer overlap. The union is still \([-r-d,r+d]\), while the twofold-covered region consists of disjoint intervals \([-r,r-d]\) and \([d-r,r]\). Therefore

\[
F(d)=p\left\{M(r+d)+2q[\Phi_\sigma(r)-\Phi_\sigma(d-r)]\right\},\qquad r\leq d\leq2r.
\]

For \(d\geq2r\), the three intervals are pairwise disjoint, giving

\[
F(d)=p\{M(r)+2[\Phi_\sigma(d+r)-\Phi_\sigma(d-r)]\}.
\]

These expressions are continuous at \(d=r\) and \(d=2r\). Differentiation on the three open intervals gives, respectively,

\[
\begin{aligned}
F'(d)&=2p\{\varphi_\sigma(r+d)-q^2\varphi_\sigma(r-d)\},&&0<d<r,\\
F'(d)&=2p\{\varphi_\sigma(r+d)-q\varphi_\sigma(r-d)\},&&r<d<2r,\\
F'(d)&=2p\{\varphi_\sigma(d+r)-\varphi_\sigma(d-r)\},&&d>2r.
\end{aligned}
\]

The last derivative is strictly negative. For \(0\leq d\leq2r\), the Gaussian density ratio is

\[
\frac{\varphi_\sigma(r+d)}{\varphi_\sigma(r-d)}=\exp(-2rd/\sigma^2),
\]

strictly decreasing in \(d\). Hence the first derivative changes sign from positive to negative precisely at \(d=\ell\) when this lies in \((0,r)\); the second changes sign precisely at \(d=\ell/2\) when this lies in \((r,2r)\). At \(d=r\), the left and right slopes are proportional to \(e^{-2r^2/\sigma^2}-q^2\) and \(e^{-2r^2/\sigma^2}-q\), respectively. The first is nonnegative and second nonpositive exactly when \(r\leq\ell\leq2r\). At \(d=2r\), the left slope is nonnegative precisely when \(\ell\geq4r\), while the right slope is always negative. Consequently \(F\) increases strictly before the stated maximizer and decreases strictly after it, apart from zero one-sided slopes exactly at transition values. In every case the stated maximizer is unique. This also proves the endpoint claims and all three reliability thresholds.

## Verification

Run the standalone standard-library Python file `checker.py` with `python checker.py`. It independently computes the probability by partitioning the line at all six footprint endpoints and integrating the appropriate Gaussian mass with weights \(1-q^k\), compares that computation with the three closed formulas, and checks the prescribed optimum against 201 candidate spacings for each of 240 seeded parameter tuples. It also checks the four different formula regimes. The execution returned `PASS: 97444 finite numerical assertions; four analytic regimes sampled`. These finite calculations do not prove an infinite-domain optimizer; the exact derivative and sign argument above supplies that proof.

## Relationship to prior work

Bittner et al. (2024) motivate the atmospheric monitoring question by documenting steep smoke concentration gradients and mobile monitoring complementary to fixed instruments. Their study does not supply the assumptions of this idealized Gaussian-position, hard-footprint model and is not used as mathematical evidence for the spacing theorem.

Litvak et al., *Increasing Detection Performance of Surveillance Sensor Networks*, §5.2.1, study the tradeoff between coverage and overlap with **two** fallible finite-footprint sensors and derive a no-overlap condition for an arbitrary target-location density. Their same underlying probability-of-at-least-one-alarm objective is acknowledged. The present statement concerns a fixed **three-device symmetric transect**: two separate contact geometries lead to the powers \(q^2\) and \(q\) and create the intermediate reliability interval where \(d=r\) is uniquely optimal. The two-device condition does not assert that four-regime three-device conclusion. The elementary coverage probability principle is not claimed new.

Wettergren and Costa (2013) formulate numerical layout optimization for collaborative surveillance of moving targets with Poisson distributed detection opportunities, rather than a fixed three-instrument Gaussian-center true-alarm probability. Frasca, Garin, Gerencsér and Hendrickx (2015) optimize a different loss, the expected worst-case distance from the domain to the nearest operating sensor. That problem neither has a Gaussian-distributed single plume center nor maximizes the probability of at least one footprint detection. A publicly indexed research finding on three Poisson sensors for Gaussian-plume Fisher-information design concerns estimation rather than binary detection, and does not imply this reliability phase diagram. Priority relative to other spatial facility-location and monitoring literature remains provisional.

## Limitations

The symmetric equal-spacing constraint is essential: the theorem says nothing about unconstrained layouts or an arbitrary number of sensors. Detection footprints and conditional independence are idealizations; the Gaussian law is for uncertain **plume-center displacement**, not a claim that the whole atmospheric concentration field is Gaussian in space. Unknown wind distributions, uneven footprints, smoke false alarms, correlated instrument failures, temporal movement, access restrictions and deployment costs could change the optimum. Any empirical application requires separate estimation and validation of \(r\), \(\sigma\), and \(p\). Independent external validation of this mathematical claim has not been performed.

## References

1. A. S. Bittner, A. L. Holder, A. P. Grieshop, G. S. W. Hagler and W. Mitchell (2024), *Performance of Vehicle Add-on Mobile Monitoring System PM2.5 measurements during wildland fire episodes*, Environmental Science: Atmospheres 4, 306–320. First published 2024-02-26. https://doi.org/10.1039/D3EA00170A
2. N. Litvak et al., *Increasing Detection Performance of Surveillance Sensor Networks*, §5.2.1, pp. 89–90, publicly accessible report: https://miis.maths.ox.ac.uk/268/2/thales-report.pdf
3. P. Frasca, F. Garin, B. Gerencsér and J. M. Hendrickx (2015), *Optimal One-Dimensional Coverage by Unreliable Sensors*, SIAM Journal on Control and Optimization 53(5), 3120–3140. https://doi.org/10.1137/140968094
4. T. A. Wettergren and R. Costa (2013), *Optimal Planning of Distributed Sensor Layouts for Collaborative Surveillance*, International Journal of Distributed Sensor Networks. https://doi.org/10.1155/2013/145496
