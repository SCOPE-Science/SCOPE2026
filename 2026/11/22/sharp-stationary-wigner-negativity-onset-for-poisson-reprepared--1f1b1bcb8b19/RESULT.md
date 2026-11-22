# Sharp stationary Wigner-negativity onset for Poisson-reprepared odd optical cats

## Finding
An odd optical Schrödinger cat continuously loses photons at zero temperature and is independently re-prepared at a Poisson rate. Its unique stationary Wigner function has the following complete positivity transition, independent of the initial nonzero coherent amplitude:

\[
W_{r/\gamma}(z)>0\quad(0<r<\gamma,\ z\in\mathbb C),\qquad
W_1(z)\geq0\text{ with equality only at }z=0,\qquad
W_{r/\gamma}(0)<0\quad(r>\gamma).
\]

Moreover the negative Wigner mass has a strictly positive *quadratic* onset immediately above the threshold, with an explicit amplitude-dependent coefficient. Thus the universal threshold holds for an unobserved random age mixture—not merely for an optical state exposed to one fixed attenuation time.

## Assumptions and scope
One bosonic oscillator, zero-temperature pure photon loss at rate \(\gamma>0\), no detuning in the rotating frame, and independent full-state re-preparation at rate \(r>0\). Each re-preparation initializes the normalized odd cat
\[
|\mathcal C^-_\alpha\rangle=\frac{|\alpha\rangle-|-\alpha\rangle}{\sqrt{2(1-e^{-2A})}},\qquad A=|\alpha|^2>0.
\]
A phase rotation lets \(\alpha=\sqrt A>0\). The loss Lindbladian is \(\mathcal L\rho=\gamma(a\rho a^\dagger-\tfrac12\{a^\dagger a,\rho\})\). The measured Wigner function averages over the unobserved reset age; no conditioning on the reset record is allowed. Phase-space coordinates are \(z=x+iy\), the vacuum Wigner function is \(2e^{-2|z|^2}/\pi\), and negative mass means \(\mathcal N=\int_{\mathbb C}(-W(z))_+\,d^2z\).

Set \(k=r/\gamma\). Define for each \(A>0\)
\[
B_x(A)=\int_0^1 t e^{-2At}\,dt=\frac{1-(1+2A)e^{-2A}}{4A^2},\qquad
B_y(A)=\int_0^1 t e^{-2A(1-t)}\,dt=\frac{2A-1+e^{-2A}}{4A^2},
\]
\[
h(A)=-\int_0^1\log t\,[e^{-2At}-e^{-2A(1-t)}]dt>0,
\qquad C(A)=\frac{h(A)^2}{8A(1-e^{-2A})\sqrt{B_x(A)B_y(A)}}>0.
\]
For each fixed \(A>0\), as \(\varepsilon=k-1\downarrow0\),
\[
\boxed{\mathcal N(1+\varepsilon,A)=C(A)\varepsilon^2+o(\varepsilon^2).}
\]
The negative set, rescaled by \(\sqrt\varepsilon\), converges to the interior of the ellipse \(8AB_x(A)X^2+8AB_y(A)Y^2<h(A)\). It has exactly one connected component for all sufficiently small positive \(\varepsilon\); no statement about the number of components at arbitrary larger rates is made.

## Proof
**Stationary mixture and exact phase-space formula.** The last-reset age is exponentially distributed with parameter \(r\). Pure loss with transmissivity \(t=e^{-\gamma T}\) maps coherent amplitudes to their square-root attenuations and multiplies the off-diagonal coherent-state dyads by the environmental overlap. Hence \(t\) has density \(kt^{k-1}\) on \((0,1)\). The Wigner function for a *fixed* attenuation \(t\) is
\[
W_t(x,y)=\frac{2e^{-2(x^2+y^2)}}{\pi(1-e^{-2A})}
\left[e^{-2At}\cosh(4x\sqrt{At})-e^{-2A(1-t)}\cos(4y\sqrt{At})\right].
\]
Its integral over phase space is one: Gaussian integration of the two bracketed terms gives \(1-e^{-2A}\). Averaging over the Beta density gives
\[
W_k(x,y)=\frac{2e^{-2(x^2+y^2)}}{\pi(1-e^{-2A})}\,F_k(x,y),\quad
F_k=k\int_0^1t^{k-1}\left[e^{-2At}\cosh(4x\sqrt{At})-e^{-2A(1-t)}\cos(4y\sqrt{At})\right]dt.
\]

**A global sign reduction.** Exactly decompose \(F_k(x,y)=I_k+X_k(x)+Y_k(y)\), where
\[
I_k=k\int_0^1t^{k-1}[e^{-2At}-e^{-2A(1-t)}]dt,
\]
\[
X_k(x)=k\int_0^1t^{k-1}e^{-2At}[\cosh(4x\sqrt{At})-1]dt\geq0,
\]
\[
Y_k(y)=k\int_0^1t^{k-1}e^{-2A(1-t)}[1-\cos(4y\sqrt{At})]dt\geq0.
\]
The last inequalities are strict for \(x\ne0\) and \(y\ne0\), respectively: each integrand is nonnegative and is positive on a set of positive measure. With \(f(t)=e^{-2At}-e^{-2A(1-t)}\), one has \(f(t)>0\) for \(0<t<1/2\) and \(f(1-t)=-f(t)\). Consequently,
\[
I_k=k\int_0^{1/2}[t^{k-1}-(1-t)^{k-1}]f(t)dt.
\]
This is strictly positive for \(0<k<1\), zero for \(k=1\), and strictly negative for \(k>1\). Since \(F_k\ge I_k\) with equality only at the origin, the claimed *entire-plane* positivity classification follows. At \(k>1\), the origin itself is negative.

**Onset coefficient and negative-region geometry.** Differentiation under the integral, valid for \(k\) in a compact neighborhood of one, yields \(I_{1+\varepsilon}=-h(A)\varepsilon+O(\varepsilon^2)\) because \(I_1=0\). Taylor expansion of the other two terms gives, uniformly near the origin,
\[
F_{1+\varepsilon}(x,y)=-h(A)\varepsilon+8AB_x(A)x^2+8AB_y(A)y^2
+O_A\big(\varepsilon^2+\varepsilon(x^2+y^2)+(x^2+y^2)^2\big).
\]
In particular \(B_x,B_y>0\), and \(h(A)>0\) follows from the same antisymmetric pairing with the increasing weight \(\log t\). To exclude remote negative islands, note \(F_1=X_1+Y_1>0\) off the origin. For \(k\) sufficiently near one, \(X_k\) has a uniform positive lower bound outside any fixed \(x\)-neighborhood of zero, while \(Y_k\) has a uniform positive lower bound outside any fixed \(y\)-neighborhood of zero: \(Y_k\) tends at large \(|y|\) to a positive constant by the Riemann–Lebesgue lemma, uniformly in \(k\) on a compact neighborhood of one by \(L^1\) continuity of its weighting density. Thus all negativity lies inside an arbitrarily small fixed ball for \(\varepsilon\) small. Inside that ball the Hessian of \(F_k\) is positive definite uniformly for nearby \(k\), by continuity of the Hessian and its positive-definite value at the origin. The negative set is therefore one strictly convex component. Rescaling \(x=\sqrt\varepsilon X\), \(y=\sqrt\varepsilon Y\) yields the limiting ellipse.

Finally the negative mass equals the integral of the leading quadratic bowl times \(2/[\pi(1-e^{-2A})]\), with area element \(\varepsilon\,dX\,dY\). Integrating \((h-8AB_xX^2-8AB_yY^2)_+\) over the plane gives \(\pi h^2/[16A\sqrt{B_xB_y}]\), and hence the displayed coefficient \(C(A)\). This uses a bounded support after rescaling; the exact exponential prefactor tends uniformly to one, so dominated convergence gives the claimed \(o(\varepsilon^2)\) remainder.

## Verification
The standalone `CHECK.py` reproduces numerical quadratures and independent odd-Fock parity checks, verifies signs for multiple positive amplitudes and rate ratios, tests the local derivative and Taylor coefficients, and numerically integrates the small negative region. In the completed source package it passes 136 numerical assertions. Finite checks confirm normalization and representative cases but cannot by themselves establish the global all-parameter theorem, which follows from the analytic proof above. For example, \(C(1)\approx0.11857243\), giving quadratic small-excess-rate Wigner-negative mass.

## Relationship to prior work
Nugmanov, Zunikov and Khalili (arXiv:2201.03257, first posted 2022-01-10) prove the well-known fixed-transmissivity \(50\%\) Wigner-negativity boundary for pure non-Gaussian states and display fixed-attenuation odd-cat formulas. That does not imply positivity of an *unconditioned mixture* of loss channels whose age distribution crosses both sides of \(1/2\). Rose, Touchette, Lesanovsky and Garrahan (arXiv:1806.01298) derive the general resolvent and stationary renewal construction for quantum resetting; it does not classify the Wigner sign of the odd-cat attenuation mixture or the resulting negative volume. Prior coherent-state cat and attenuation studies also treat fixed loss rather than this exact phase-space aging mixture. Standard Gaussian integration, parity generating functions, and renewal theory are not claimed as new. The claimed addition is the global reset/loss-rate positivity boundary, its single critical zero, and the amplitude-resolved quadratic negative-volume onset, for the precisely stated physical model.

## Limitations
The result assumes zero-temperature pure loss, complete renewal to the same odd cat, exponential reset times, no phase rotation relative to the preparation, and a single bosonic mode. The rate condition does not assert experimentally detectable negativity at finite counts. At arbitrary \(r>\gamma\), only existence of a negative region is proved, not its global topology. No independent audit or general literature priority certificate is claimed. A broader quantum-channel mixture theorem could imply part of the result and remains a priority risk.

## References
1. B. Nugmanov, N. Zunikov, F. Ya. Khalili, *Robustness of negativity of the Wigner function to dissipation*, arXiv:2201.03257, first posted 2022-01-10, https://arxiv.org/abs/2201.03257 .
2. D. C. Rose, H. Touchette, I. Lesanovsky, J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, arXiv:1806.01298 (2018), https://arxiv.org/abs/1806.01298 .
3. *Quantifying quantum coherence of optical cat states*, *Photonics Research* (2021), https://doi.org/10.1364/PRJ.418417 .
4. *Robustness of quantum cat-state coherence* (2026), arXiv:2604.20303, https://arxiv.org/abs/2604.20303 (later comparison only; not the selected primary date).
