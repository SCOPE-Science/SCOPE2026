# Sharp critical Hopf ringdown and negative logarithmic phase drift in an Allee predator–prey flow

## Finding

At the critical coexistence boundary of the strong-Allee predator–prey system, local decay is oscillatory and algebraic, with an explicitly negative logarithmic drift of the unwrapped oscillation phase. For every \(a\in(0,1)\) and \(\varepsilon>0\), define
\[
\phi_H=\frac1{2-a},\quad V=(1-\phi_H)(1-a),\quad
\omega=\sqrt{\frac V\varepsilon},\quad q=\frac{\phi_H}{\varepsilon}.
\]
For all sufficiently close positive nonstationary initial conditions, the exact solution at \(\phi=\phi_H\) satisfies
\[
\lim_{t\to\infty}t\left[(u(t)-1)^2+\frac{(v(t)-V)^2}{\varepsilon^2\omega^2}\right]=\frac2q,
\]
and the unwrapped angle
\[
\Theta(t)=\operatorname{lift}\arg\left((u(t)-1)+i\frac{v(t)-V}{\varepsilon\omega}\right)
\]
obeys
\[
\Theta(t)=\omega t-\frac{\omega^2+4q^2+5q+1}{12\omega q}\log t+\Theta_\infty+o(1).
\]
In particular, the coefficient of \(\log t\) is strictly negative for all admissible parameters. The equilibrium is locally asymptotically stable at the zero-trace boundary. The Hopf bifurcation is supercritical: for fixed \(a,\varepsilon\), a locally attracting small cycle bifurcates for \(\phi<\phi_H\) near the boundary.

## Assumptions and scope

The autonomous (unramped) model is
\[
\varepsilon\dot u=u[(1-\phi u)(u-a)-v],\qquad \dot v=v(u-1),
\]
where \(0<a<1\), \(\varepsilon>0\), and \(0<\phi<1\). Time \(t\) is the dimensionless slow time in this equation. At \(\phi_H=(2-a)^{-1}\), the coexistence equilibrium \((u,v)=(1,V)\) lies strictly inside the positive quadrant. The theorem is local: it asserts the limits for every sufficiently near but distinct initial point, without asserting global attraction or behavior under environmental ramps. Because angular speed tends to \(\omega>0\), the angle lift is well-defined after entering the punctured neighborhood; changing its initial branch only changes \(\Theta_\infty\) by a multiple of \(2\pi\).

## Proof

**Exact polynomial reduction.** The coexistence Jacobian has trace \([1-(2-a)\phi]/\varepsilon\) and determinant \((1-\phi)(1-a)/\varepsilon\). At \(\phi=\phi_H\), the eigenvalues are \(\pm i\omega\). Put \(X=u-1\) and \(Y=(v-V)/(\varepsilon\omega)\). Direct substitution, without truncation, gives
\[
\dot X=-\omega Y-qX^2-\omega XY-qX^3,\qquad
\dot Y=\omega X+XY.
\]
Write \(X=R\cos\theta\), \(Y=R\sin\theta\), and abbreviate \(c=\cos\theta\), \(s=\sin\theta\). On \(R>0\), the exact equations are
\[
\dot R=R^2A(\theta)+R^3B(\theta),\qquad
\dot\theta=\omega+RC(\theta)+R^2D(\theta),
\]
where
\[
\begin{aligned}
A&=-qc^3-\omega c^2s+cs^2,&B&=-qc^4,\\
C&=(1+q)c^2s+\omega cs^2,&D&=qc^3s.
\end{aligned}
\]
The mean of each of \(A,C,D\) over one turn is zero. Choose periodic mean-zero primitives \(U'=A/\omega\) and \(Q'=-C/\omega\). The successive near-identity changes \(\rho=R-R^2U(\theta)+O(R^3)\) and \(\psi=\theta+RQ(\theta)+O(R^2)\) remove the nonresonant quadratic radial and linear angular oscillations. Removing the remaining zero-mean cubic radial and quadratic angular terms yields the classical averaged equations
\[
\dot\rho=\mu\rho^3+O(\rho^4),\qquad
\dot\psi=\omega+\nu\rho^2+O(\rho^3),
\]
with all remainders uniform in phase for sufficiently small \(\rho\). The coefficients are the *evaluated* averages
\[
\mu=\langle B\rangle-\frac{\langle AC\rangle}{\omega},\qquad
\nu=\langle UC\rangle-\frac{\langle C^2\rangle}{\omega},
\]
where \(\langle f\rangle=(2\pi)^{-1}\int_0^{2\pi}f(\theta)\,d\theta\). Integration by parts uses \(\langle AQ\rangle=\langle UC\rangle\). Exact trigonometric integration gives
\[
\begin{aligned}
\langle B\rangle&=-3q/8,&\langle AC\rangle&=-\omega q/8,\\
\langle UC\rangle&=(\omega^2-5q^2-4q+1)/(48\omega),&
\langle C^2\rangle&=(\omega^2+q^2+2q+1)/16.
\end{aligned}
\]
Therefore
\[
\boxed{\mu=-q/4<0,\qquad
\nu=-\frac{\omega^2+4q^2+5q+1}{24\omega}<0.}
\]

**Attraction and asymptotics.** For sufficiently small positive \(\rho\), the radial equation gives strictly decreasing \(\rho\) and convergence to zero. Because \(\dot\psi=\omega+O(\rho^2)>\omega/2\), nonstationary solutions spiral and never reach the equilibrium in finite time. Writing \(W=\rho^{-2}\), one obtains \(\dot W=q/2+O(\rho)\). The resulting comparison implies \(\rho(t)=O(t^{-1/2})\), then integration yields \(W(t)=(q/2)t+O(\sqrt t)\), hence
\[
\rho(t)^2=\frac2{qt}+O(t^{-3/2}).
\]
Since \(R=\rho+O(\rho^2)\), it follows that \(tR^2\to2/q\). Moreover, the phase equation gives
\[
\dot\psi-\omega=\frac{2\nu}{qt}+O(t^{-3/2}),
\]
so integration has a finite asymptotic integration constant and produces \(\psi(t)=\omega t+(2\nu/q)\log t+\psi_\infty+o(1)\). The near-identity angular transformation satisfies \(\theta-\psi=O(R)\to0\), so the same assertion holds for the original lifted angle \(\Theta\), with
\[
\chi=2\nu/q=-\frac{\omega^2+4q^2+5q+1}{12\omega q}<0.
\]
For parameter variation, the real eigenvalue part crosses zero with nonzero derivative \(-(2-a)/(2\varepsilon)\). The strict negative cubic radial coefficient establishes the supercritical direction by the planar Hopf theorem, yielding stable small-amplitude cycles on the \(\phi<\phi_H\) side.

## Verification

The accompanying standalone checker evaluates the trigonometric means exactly with symbolic arithmetic, reconstructs \(\mu\) and \(\nu\), and integrates two representative positive solutions. For \(a=1/2\) and \(\varepsilon=1\), the predicted constants are \(2/q=3\) and \(\chi\approx-1.922169034267355\). The checker tests convergence of both the scaled elliptic radius and the corrected unwrapped phase; these finite tests corroborate rather than prove the asymptotics. The analytical argument above applies to all \(0<a<1\) and \(\varepsilon>0\).

## Relationship to prior work

Hennessy, Popović and Sattar (2026) introduced the precise autonomous model and analyzed its slow-fast geometry, folded saddle and rate-induced extinction upon ramping \(\phi\); their standing bistability analysis works on the strict stable side \(\phi>\phi_H\), and their original study does not derive the exact critical ringdown or logarithmic phase coefficient. Wang, Shi and Wei (2011), for a much broader class of strong-Allee predator–prey systems, already gave the generic first Lyapunov coefficient and supercritical Hopf criterion, including linear predator functional response. Therefore the **Hopf direction itself is not claimed as novel**. Their Appendix introduces a symbolic cubic angular coefficient but does not evaluate the present model's negative phase-drift constant or establish the two explicit trajectory-wise limits. The new contribution is precisely the original-coordinate amplitude and strictly negative logarithmic phase drift at the excluded nonhyperbolic boundary, for arbitrary finite \(\varepsilon>0\). The 2007 Bazykin–Berezovskaya (BB) model analyzed by van Voorn and coauthors is in fact exactly equivalent to this autonomous system: set \(s=(\phi/\varepsilon)t\), \(x_1=u\), \(x_2=v/\phi\), and its BB parameters \(l=a\), \(k=1/\phi\), \(m=1\), \(c=\varepsilon/\phi\). That work already describes the Hopf curve and stable cycles, but the inspected full text does not evaluate the logarithmic critical phase drift. Earlier classical Hopf methods are acknowledged; historical priority for this particular explicit phase law remains provisional.

## Limitations

This is a local autonomous result for positive trajectories close to coexistence, not a global-basin theorem. It does not give a uniform neighborhood as \(\varepsilon\to0\), quantify the ramped critical rate, or classify large cycles and heteroclinic transitions. No independent scientific audit has been performed. The finite trajectory calculations cannot prove infinite-time asymptotics; the proof relies on exact normal-form averaging and summable errors. Other earlier sources might contain equivalent evaluated coefficients.

## References

1. B. Hennessy, N. Popović and Z. Sattar, *A minimal model for rate-induced tipping to extinction*, arXiv:2610.12319v1, first public October 8, 2026. https://arxiv.org/abs/2610.12319
2. J. Wang, J. Shi and J. Wei, *Predator–prey system with strong Allee effect in prey*, Journal of Mathematical Biology 62 (2011), 291–331. DOI: 10.1007/s00285-010-0332-1. Open author manuscript: https://jxshix.people.wm.edu/shi/11-wang-shi-wei-JMB.pdf
3. G. A. K. van Voorn, L. Hemerik, M. P. Boer and B. W. Kooi, *Heteroclinic orbits indicate overexploitation in predator–prey systems with a strong Allee effect*, Mathematical Biosciences 209 (2007), 451–469. DOI: 10.1016/j.mbs.2007.02.006.
