# Shifted harmonic-mean rigidity for recurrent prey density in a chemostat
## Finding
Consider the nutrient–prey–predator chemostat
\[
\dot N=D(\mu-N)-P f_1(N),\qquad
\dot P=\gamma_1P f_1(N)-D_1P-Zf_2(P),\qquad
\dot Z=Z(\gamma_2f_2(P)-D_2).
\]
Under the source assumptions on \(f_1\), specialize the predator response to the Holling-II law
\[
f_2(P)=\frac{m_2P}{\alpha_2+P},
\]
with positive parameters and \(\gamma_2m_2>D_2\). Define the predator break-even prey density
\[
p_*=\frac{D_2\alpha_2}{\gamma_2m_2-D_2},
\]
so that \(f_2(p_*)=D_2/\gamma_2\).

Every compactly supported invariant Borel probability measure \(\nu\) whose support lies in \(N>0\), \(P>0\), \(Z>0\) obeys the exact shifted harmonic-mean law
\[
\int \frac{1}{\alpha_2+P}\,d\nu=\frac{1}{\alpha_2+p_*}.
\]
If \(\bar P=\int P\,d\nu\), then it also obeys the exact finite-amplitude defect identity
\[
\bar P-p_*=\frac{\alpha_2+p_*}{\alpha_2+\bar P}
\int\frac{(P-\bar P)^2}{\alpha_2+P}\,d\nu.
\]
Consequently \(\bar P\ge p_*\), and equality holds only for the coexistence-equilibrium measure. Thus every non-equilibrium compact interior recurrent statistical state has \(\bar P>p_*\). For every positive nonconstant periodic orbit, the time harmonic mean of \(\alpha_2+P(t)\) is exactly \(\alpha_2+p_*\), its ordinary time mean satisfies \(\overline P>p_*\), and the orbit strictly straddles the plane \(P=p_*\).

## Assumptions and scope
The invariant measure is assumed compactly supported in the strict positive octant, so \(\log Z\) and all displayed observables are bounded and smooth on a neighborhood of the support. The result uses only flow invariance, the Holling-II formula for \(f_2\), positivity of the parameters, \(\gamma_2m_2>D_2\), and the source's strict monotonicity assumption for \(f_1\) in the equality case. It does not assume that the invariant measure is ergodic.

The statement is conditional: it constrains any compact interior recurrent state that exists. It does not assert existence, uniqueness, stability, or period of a limit cycle. Boundary invariant measures are excluded because \(\log Z\) is not defined at \(Z=0\).

## Proof
Flow invariance gives \(\int L\phi\,d\nu=0\) for every smooth observable \(\phi\) defined on a neighborhood of the compact support. Taking \(\phi=\log Z\) yields
\[
0=\int(\gamma_2f_2(P)-D_2)\,d\nu,
\]
so
\[
\int f_2(P)\,d\nu=\frac{D_2}{\gamma_2}=f_2(p_*).
\]
Since
\[
f_2(P)=m_2\left(1-\frac{\alpha_2}{\alpha_2+P}\right),
\]
we obtain
\[
\int\frac{1}{\alpha_2+P}\,d\nu=\frac{1}{\alpha_2+p_*}.
\]
This is the shifted harmonic-mean rigidity.

For \(m=\bar P\), the pointwise algebraic identity
\[
\frac{1}{\alpha_2+P}
=\frac{1}{\alpha_2+m}
-\frac{P-m}{(\alpha_2+m)^2}
+\frac{(P-m)^2}{(\alpha_2+P)(\alpha_2+m)^2}
\]
has zero mean in its middle term. Averaging it and substituting the harmonic-mean law gives
\[
\frac{1}{\alpha_2+p_*}-\frac{1}{\alpha_2+m}
=\frac{1}{(\alpha_2+m)^2}
\int\frac{(P-m)^2}{\alpha_2+P}\,d\nu.
\]
Multiplication by \( (\alpha_2+p_*)(\alpha_2+m)\) gives
\[
m-p_*=\frac{\alpha_2+p_*}{\alpha_2+m}
\int\frac{(P-m)^2}{\alpha_2+P}\,d\nu.
\]
The right-hand side is nonnegative. Equality forces \(P=m\) almost surely. The harmonic-mean law then gives \(m=p_*\). Invariance of the support implies \(\dot P=0\) and \(\dot Z=0\) there. Because \(f_2(p_*)=D_2/\gamma_2\), \(Z\) is constant along each supported trajectory; then \(\dot P=0\) makes \(f_1(N)\) constant. Strict monotonicity of \(f_1\) makes \(N\) constant. Finally \(\dot N=0\) has at most one positive solution for fixed \(P=p_*\), because \(D(\mu-N)-p_*f_1(N)\) is strictly decreasing. Thus equality is the coexistence-equilibrium measure.

For a positive nonconstant periodic orbit, use normalized time measure. If \(P(t)\ge p_*\) for all \(t\), with strict inequality somewhere, then \(1/(\alpha_2+P(t))\) has time average strictly below \(1/(\alpha_2+p_*)\), contradicting the exact law. The analogous contradiction occurs if \(P(t)\le p_*\) for all \(t\). Therefore every positive nonconstant periodic orbit strictly crosses \(P=p_*\).

## Verification
The proof is analytic and does not rely on a finite numerical experiment. The critical steps were checked directly: the generator identity for \(\log Z\), the Holling-II reciprocal rewrite, the pointwise Jensen-defect decomposition, the equality case, and the periodic-orbit straddling argument.

At the source's Holling-II values \(\alpha_2=1/2\), \(\gamma_2=3/2\), and \(m_2=2\), the equal-removal example \(D_2=1\) has \(p_*=1/4\), so every positive cycle has harmonic mean \(H(1/2+P)=3/4\). For the distinct-removal example \(D_2=13/10\), one obtains \(p_*=13/34\) and \(H(1/2+P)=15/17\). These exact fractions are illustrations of the theorem, not evidence for it.

## Relationship to prior work
Ballyk, Jawarneh, and Staffeldt formulate the three-dimensional chemostat with general response functions, define the predator break-even concentration, specialize to Holling-II responses, and analyze Hopf bifurcations and limit cycles. Their full text was inspected for average, mean, harmonic-mean, and integral formulations; it does not state the shifted harmonic-mean rigidity or the exact arithmetic-mean defect above.

The closest earlier same-system literature was also compared at statement level. Li and Kuang analyze the same three-dimensional chemostat with distinct removal rates, including persistence and numerically observed oscillations. Kuang analyzes the equal-removal planar reduction, proves invariant-set location and uniqueness results for limit cycles, and explicitly notes that exact geometric location remained difficult. Those results bound where cycles lie but do not imply an equality for the reciprocal observable \(1/(\alpha_2+P)\), nor the exact finite-amplitude arithmetic-mean defect. Rana's later bifurcation analysis likewise studies Hopf and periodic behavior for distinct removal rates without such a time-average identity.

A standard general observation for positive Kolmogorov populations is that the time average of per-capita growth vanishes on a periodic orbit. The present claim is more specific: the Holling-II form converts that balance into an exact source-parameter harmonic mean, and the reciprocal identity then gives a closed nonnegative defect formula showing a strict arithmetic-mean shift for every non-equilibrium compact interior invariant measure.

## Limitations
The result is specific to the deterministic continuous-time model and the Holling-II predator response. It does not cover stochastic forcing, delays, boundary measures, or arbitrary functional responses. The strict equality classification uses the source's monotonicity assumption for \(f_1\). The literature on chemostat oscillations is extensive; the closest same-model and limit-cycle papers were inspected, but an older source could conceivably contain an equivalent observation under different terminology. No claim is made about independent validation.

## References
1. M. Ballyk, I. Jawarneh, and R. Staffeldt, “A Nutrient-Prey-Predator Model: Stability and Bifurcations,” arXiv:1812.09964, first public version 2018-12-24; Discrete and Continuous Dynamical Systems - S, DOI 10.3934/dcdss.2020192.
2. B. Li and Y. Kuang, “Simple Food Chain in a Chemostat with Distinct Removal Rates,” Journal of Mathematical Analysis and Applications 242 (2000), 75–92, DOI 10.1006/jmaa.1999.6655.
3. Y. Kuang, “Limit Cycles in a Chemostat-Related Model,” SIAM Journal on Applied Mathematics 49 (1989), 1759–1767, DOI 10.1137/0149107.
4. S. M. S. Rana, “Bifurcation Analysis of a Food Chain in a Chemostat with Distinct Removal Rates,” International Journal of Applied Science and Engineering 13 (2015), 217–232, DOI 10.6703/IJASE.2015.13(3).217.
