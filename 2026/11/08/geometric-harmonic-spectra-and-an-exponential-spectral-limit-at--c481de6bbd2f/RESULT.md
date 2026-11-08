# Geometric harmonic spectra and an exponential spectral limit at a cubic invariant-circle degeneration

## Finding

Consider the cubic planar flow
\[
\dot x=ax+y-\bigl(a(x^2+y^2)+xy\bigr)(x+y),\qquad
\dot y=ay-\bigl(a(x^2+y^2)+xy\bigr)(y-x).
\]
For each real \(a<(1-\sqrt2)/2\) or \(a>(1+\sqrt2)/2\), its invariant unit circle is a genuine periodic orbit. Write
\[
b=|a-1/2|,\quad \varepsilon=\operatorname{sgn}(a-1/2),\quad
R=1/\sqrt2,\quad \Delta=\sqrt{b^2-R^2},\quad
k=\frac{R}{b+\Delta},\quad\phi=\pi/4.
\]
Choose the initial point uniformly in **original physical time** over the circle's minimal period \(T=2\pi/\Delta\), and let \(U(t)=(x(t)+iy(t))^2\). Its mean is \(m=-\varepsilon e^{i\phi}k\); for every \(t\in\mathbb R\), its exact centered autocorrelation is
\[
C_a(t)=\mathbb E\bigl[(U(t)-m)\overline{(U(0)-m)}\bigr]
=\frac{(1-k^2)^2e^{2i\varepsilon\Delta t}}{1-k^2e^{2i\varepsilon\Delta t}}.
\]
In the convention \(C_a(t)=\int e^{i\omega t}\,d\mathcal S_a(\omega)\), the full centered power spectral measure is
\[
\mathcal S_a=\sum_{j=1}^{\infty}(1-k^2)^2k^{2(j-1)}\,\delta_{2\varepsilon j\Delta},
\qquad \mathcal S_a(\mathbb R)=1-k^2.
\]
As the corresponding periodic regime approaches either endpoint \(a_\pm=(1\pm\sqrt2)/2\), with \(\varepsilon\) fixed, the **variance-normalized** spectral measure has the nondegenerate weak limit
\[
\frac{\mathcal S_a}{1-k^2}\ \Longrightarrow\ \operatorname{Law}(\varepsilon R E),
\qquad E\sim\operatorname{Exp}(1).
\]
Equivalently \(C_a(t)/C_a(0)\to(1-i\varepsilon Rt)^{-1}\) for every fixed physical lag \(t\). The limit is an exponential *frequency distribution* of normalized fluctuations, not an assertion of an absolutely continuous spectrum at any fixed parameter.

## Assumptions and scope

The parameter is real and in either of the two stated open ranges. The original-time sampling measure is the unique invariant probability for the smooth periodic motion on the unit circle; it is not uniform in polar angle. Correlations refer to the stationary ensemble obtained by uniform random original-time phase. The exponential variable has unit mean. Weak convergence is on the real frequency line and the endpoint limits are one-sided within the periodic parameter regions.

## Proof

**Invariant circle and original-time angular equation.** With \(x=r\cos\theta\), \(y=r\sin\theta\), direct differentiation gives \(\dot\theta=(x\dot y-y\dot x)/r^2\). On \(r=1\) the resulting identity is
\[
\dot\theta=a-\frac12+\frac{\cos 2\theta+\sin 2\theta}{2}
=(a-1/2)+R\cos(2\theta-\phi).
\]
The circle itself is invariant since \(d(r^2-1)/dt=-2\bigl(a r^2+xy\bigr)(r^2-1)\). Since \(b>R\), angular velocity is nowhere zero; every point traverses the full circle with minimal period
\[
T=\int_0^{2\pi}\frac{d\theta}{|\dot\theta|}=rac{2\pi}{\Delta}.
\]
The period integral follows by splitting into two identical half-turns and using \(\int_0^{2\pi}(b+R\cos v)^{-1}dv=2\pi/\Delta\).

**Exact phase conjugacy.** Put \(v=2\theta-\phi\) for \(\varepsilon=-1\), or \(v=2\theta-\phi-\pi\) for \(\varepsilon=1\). Then \(\dot v=2\varepsilon(b-R\cos v)\). Set \(r_0=\tan(v/2)\), \(\beta=\sqrt{(b-R)/(b+R)}\), and \(w=\arctan(r_0/\beta)\) modulo \(\pi\). Direct differentiation, including continuous chart changes, gives \(\dot w=\varepsilon\Delta\). Hence \(\zeta=e^{2iw}\) is uniformly distributed on the unit circle under normalized physical-time sampling, and \(\zeta(t)=\zeta(0)e^{2i\varepsilon\Delta t}\). Elementary tangent-half-angle algebra gives
\[
e^{iv}=\frac{\zeta+k}{1+k\zeta},\qquad
k=\frac{1-\beta}{1+\beta}=\frac{R}{b+\Delta},\qquad
U=-\varepsilon e^{i\phi}\frac{\zeta+k}{1+k\zeta}.
\]

**Exact spectrum.** Since \(0<k<1\), the Blaschke factor has the absolutely convergent boundary Fourier expansion
\[
\frac{\zeta+k}{1+k\zeta}=k+(1-k^2)\sum_{j=1}^{\infty}(-k)^{j-1}\zeta^j.
\]
Orthogonality of circle characters under uniform \(\zeta(0)\) establishes the mean and shows that the complex stationary autocorrelation is the sum of harmonic powers \((1-k^2)^2k^{2(j-1)}e^{2i\varepsilon j\Delta t}\). Summing the geometric series yields the stated rational correlation and the positive discrete spectral measure. The spectral mass is \((1-k^2)^2/(1-k^2)=1-k^2\), in agreement with \(\mathbb E|U|^2-|m|^2\).

**Critical weak spectral limit.** The parameter relation is
\[
1-k^2=\frac{2\Delta}{b+\Delta}\longrightarrow0.
\]
After normalizing by \(1-k^2\), the frequency is \(2\varepsilon\Delta J\), where \(J\) is geometric with \(\Pr(J=j)=(1-k^2)k^{2(j-1)}\), \(j\ge1\). Standard geometric-to-exponential convergence follows directly from
\[
\Pr((1-k^2)J>u)=k^{2\lfloor u/(1-k^2)\rfloor}\longrightarrow e^{-u}
\quad(u>0),
\]
with the immaterial integer boundary convention. Because \(2\Delta/(1-k^2)=b+\Delta\to R\), the continuous mapping theorem yields the exponential spectral limit. Its characteristic function gives the normalized correlation limit. This proves each claim with its original-time normalization.

## Verification

The standalone `check_spectrum.py` numerically integrates the explicit Möbius circle profile over uniformly sampled physical-time phase and compares it with the exact covariance for both rotation orientations and for parameters close to each critical endpoint. Its checks are finite corroborations of the displayed analytic identities, not a substitute for the proof.

## Relationship to prior work

Gasull and Giacomini (2022 preprint; 2023 journal), Section 7.1, equation (15), treat exactly this cubic polynomial family, the invariant circle, its periodicity parameter intervals and limit-cycle multiplicity; those structural facts are not new here. Giacomini and Grau (2005) study general cofactor and transverse-stability identities for invariant algebraic cycles. The present result instead obtains the **full temporal harmonic power measure** of the natural second-angular-harmonic observable and the weak limit of its variance-normalized frequencies at both infinite-period thresholds. The angular equation is conjugate to the classical saddle-node-on-invariant-circle phase normal form; no new normal-form classification is claimed.

## Limitations

The spectrum belongs to one specified complex observable and one stationary phase ensemble on the invariant circle; no claims are made about radial perturbations, global attractors, stochastic forcing, or nonstationary trajectories. The limiting exponential measure is obtained only after dividing by a variance tending to zero. The underlying Riccati phase mechanism is classical, and publication-priority risk remains for unindexed spectral calculations or specialized treatments of this exact cubic family. No independent audit has been undertaken.

## References

1. A. Gasull and H. Giacomini, *Number of Limit Cycles for Planar Systems with Invariant Algebraic Curves*, arXiv:2210.15803v1 (publicly posted 2022-10-27), Section 7.1, equation (15); journal DOI 10.1007/s12346-023-00746-7.
2. H. Giacomini and M. Grau, *On the Stability of Limit Cycles for Planar Differential Systems*, arXiv:math/0505027v1 (2005), general invariant-curve cofactor stability theory.
3. B. Ermentrout, *Ermentrout–Kopell Canonical Model*, Scholarpedia 3(3):1398 (2008), overview of the saddle-node-on-invariant-circle angular normal form.
