# Three-rate passive-sampler pulse recovery and a universal short-pulse sensitivity law

## Finding

For a single rectangular water-contaminant episode and three simultaneously retrieved, calibrated first-order passive samplers with elimination rates \(k,2k,3k\), exactly three terminal readings uniquely recover the episode's concentration and its two endpoints. Two such terminal readings do not identify these three unknowns, even with noiseless data. More importantly, the exact local relative sensitivity of the inferred episode concentration to a relative perturbation of the third normalized reading, with the first two readings fixed, depends **only** on the duration \(h\), not on the episode amplitude or position:

\[
\mathcal S(h)=\frac{2(1+e^{-kh}+e^{-2kh})}{(1-e^{-kh})^2},\qquad
\lim_{h\downarrow0}(kh)^2\mathcal S(h)=6.
\]

Thus the same nominally identifiable experiment becomes locally unstable with the sharp quadratic factor \(6/(kh)^2\) for a short episode. This is a statement about differential conditioning of a precise idealized inverse, **not** a finite-noise error bound or a minimax claim.

## Assumptions and scope

Fix an observation horizon \(T>0\), a calibrated rate unit \(k>0\), and three known uptake coefficients \(\beta_j>0\) for \(j\in\{1,2,3\}\). The aqueous concentration is \(c(t)=C\mathbf1_{[t_0,t_1]}(t)\) for \(0\le t\le T\), with unknown \(C>0\) and \(0<t_0<t_1<T\). Each initially empty, nondepleting sampler follows the linear one-compartment equation

\[
\dot S_j(t)=\beta_j c(t)-jk S_j(t),\quad S_j(0)=0.
\]

Only the three exact terminal observations \(S_j(T)\) are supplied. The normalized readings are \(Q_j=jk S_j(T)/\beta_j\). Define \(h=t_1-t_0\). The quantities referred to as sensitivities below are derivatives along physically admissible local variations of the data triple, keeping \(Q_1,Q_2\) fixed.

## Proof

**Forward map.** Solving the linear equation, then integrating over the nonzero input interval, yields

\[
Q_j=C(X^j-Z^j),\quad
X=e^{-k(T-t_1)},\quad Z=e^{-k(T-t_0)},\quad 0<e^{-kT}<Z<X<1.
\]

Put \(s=Q_2/Q_1\) and \(v=Q_3/Q_1\). Dividing the power differences by \(X-Z\) gives

\[
s=X+Z,\quad v=X^2+XZ+Z^2,\quad 4v-3s^2=(X-Z)^2.
\]

Consequently the **complete necessary-and-sufficient positive interior data criterion** is

\[
Q_1>0,\quad \delta=\sqrt{4Q_3/Q_1-3(Q_2/Q_1)^2}>0,
\quad e^{-kT}<\frac{s-\delta}{2}<\frac{s+\delta}{2}<1.
\]

Here real square-root existence is included in \(\delta>0\). Whenever these conditions hold, the unique physical parameters are

\[
X=(s+\delta)/2,\quad Z=(s-\delta)/2,\quad
C=Q_1/\delta,\quad
t_0=T+k^{-1}\log Z,\quad t_1=T+k^{-1}\log X.
\]

Substitution reconstructs all three observations, so the conditions also prove existence, not merely injectivity.

**Sharp minimality for this terminal-reading design.** For any interior physical triple and only \(Q_1,Q_2\) supplied, \(s=X+Z\) is fixed. For every sufficiently small real \(\varepsilon\), the changed nodes \(X+\varepsilon\) and \(Z-\varepsilon\) remain strictly within the allowed bounds. Choosing the changed amplitude \(Q_1/(X-Z+2\varepsilon)\) preserves both observed readings, while changing the pulse parameters. Thus two channels have a genuine local continuum of aliases, not merely a parameter-counting argument.

**Exact inverse sensitivity.** At fixed \(Q_1,Q_2\), differentiating \(\delta^2=4Q_3/Q_1-3s^2\) and \(C=Q_1/\delta\) gives

\[
\frac{\partial C}{\partial Q_3}\bigg|_{Q_1,Q_2}=-\frac{2}{(X-Z)^3},\qquad
\mathcal S=\left|\frac{Q_3}{C}\frac{\partial C}{\partial Q_3}\bigg|_{Q_1,Q_2}\right|
=\frac{2(X^2+XZ+Z^2)}{(X-Z)^2}.
\]

Because \(Z/X=e^{-kh}\), this is exactly the displayed duration-only law. Let \(r=e^{-kh}\); the derivative of \((1+r+r^2)/(1-r)^2\) with respect to \(r\) is \(3(1+r)/(1-r)^3>0\). Hence \(\mathcal S\) strictly decreases with duration and the short-duration coefficient \(6\) follows from \(1-e^{-kh}\sim kh\).

**Jacobian cross-check.** Differentiating the three power differences shows

\[
\det\!\frac{\partial(Q_1,Q_2,Q_3)}{\partial(C,X,Z)}=-C^2(X-Z)^4,\qquad
\det\!\frac{\partial(Q_1,Q_2,Q_3)}{\partial(C,t_0,t_1)}=C^2k^2XZ(X-Z)^4>0.
\]

This confirms local invertibility for every interior pulse and fourth-order determinant collapse as its duration shrinks with its amplitude and final endpoint fixed. The determinant statement is separate from the sharper, coordinate-specified relative sensitivity identity above.

## Verification

An exact witness takes \(T=3\), \(k=\log 2\), \(t_0=1\), \(t_1=2\), and \(C=4\). Then \((X,Z)=(1/2,1/4)\) and the three normalized observations are \((Q_1,Q_2,Q_3)=(1,3/4,7/16)\). The inverse returns the exact original parameters, and \(\mathcal S=14\). A distinct two-channel alias is \((X,Z,C)=(9/16,3/16,8/3)\), which preserves \((Q_1,Q_2)=(1,3/4)\) but changes \(Q_3\).

The accompanying standard-library Python script `check.py`, run with `python3 check.py`, verifies these rational identities, the rational Jacobian determinant, 15,000 further interior reconstructions, 1,000 duration-only sensitivity comparisons, and short-duration asymptotics. It reports 47,013 assertions. Symbolic proof above, not finite sampling, establishes the universal quantifiers.

## Relationship to prior work

Becker et al. (2024) model calibrated passive-sampler accumulation under time-varying water concentrations and identify uncertainty about the timing and duration of intermittent exposure as an important limitation. Their published equations provide the underlying first-order convolution model but do not state the present minimal three-rate terminal inversion or exact duration-only sensitivity formula. Hawker (2009, published online) models pulse responses and discusses reconstructing temporal exposure from a **time series** of sampler readings, which is a different observation design from three rate-diverse samplers read once at a common end time.

The algebraic inverse is related to classical Prony reconstruction of exponential sums (Plonka and Tasche, 2014), particularly constrained opposite-sign two-node powers. General unconstrained two-node Prony schemes provide wider reconstruction methods, and collision-induced ill-conditioning is known. This finding does **not** claim those ideas as new: its scope is the three-terminal-channel, physical-feasibility, and exact local relative-sensitivity classification for a rectangular aqueous pulse. The availability of a stronger, previously published specialization in the broader inverse-moment literature remains a historical priority risk.

## Limitations

Rates exactly in the ratio \(1:2:3\), correct uptake calibration, zero initial sampler content, one rectangular pulse, constant rate coefficients, nondepleting ambient concentration and noiseless observations are required. A diffuse, multiple, or nonrectangular input may produce another interpretation; neither three readings nor this theorem validate the one-pulse assumption. The sensitivity law is a local derivative at fixed first two readings: it is **not** a confidence interval, noise distribution, instrument design optimum or claim of practical recovery for narrow pulses. Interior inequalities deliberately exclude pulses touching deployment or retrieval boundaries. No empirical model fit or independent verification is claimed.

## References

1. Becker, B., Kochleus, C., Spira, D., Bachtin, J., König, F., Meinecke, S., Möhlenkamp, C., and Booij, K. “Modelling passive sampling of hydrophilic compounds under time-variable aqueous concentrations.” *Environmental Science and Pollution Research* 31 (2024), 51844–51857. First published online 2024-08-12. https://doi.org/10.1007/s11356-024-34460-x
2. Hawker, D. W. “Modeling the response of passive samplers to varying ambient fluid concentrations of organic contaminants.” *Environmental Toxicology and Chemistry* 29 (2010), 591–596. First published online 2009-12-02. https://doi.org/10.1002/etc.69
3. Plonka, G., and Tasche, M. “Prony methods for recovery of structured functions.” *GAMM-Mitteilungen* 37 (2014), 239–258. https://doi.org/10.1002/gamm.201410011
