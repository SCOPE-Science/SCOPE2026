# Opposite Hopf stabilities with simultaneous positive period drift in an invariant-line quadratic flow

## Finding
Consider the one-parameter quadratic flow
\[
\dot x=d x-y+\frac14x^2+\frac15xy-\frac13y^2,
\qquad \dot y=x(1+y).
\]
There are two nondegenerate small-cycle bifurcations, at the equilibria \(E_0=(0,0)\) when \(d=0\) and \(E_-=(0,-3)\) when \(d=3/5\). Write \(T_+(d)\) and \(T_-(d)\) for the minimal **original-time** periods of their nearby cycles. Their exact first-order period laws are
\[
\boxed{T_+(d)=2\pi+\frac{586\pi}{45}\,d+o(d)}\qquad(d\downarrow0),
\]
\[
\boxed{T_-(d)=\sqrt2\,\pi+\frac{793\sqrt2\,\pi}{225}
\left(\frac35-d\right)+o\left(\frac35-d\right)}
\qquad(d\uparrow3/5).
\]
Both physical periods therefore increase strictly above their limiting linear periods to first order on the respective cycle-bearing sides, **despite opposite orbital stabilities**. With the positive \(x\)-axis as the local Poincaré section, their unique small-cycle section radii are
\[
\boxed{x_+(d)=\sqrt{240d}+O(d)},\qquad
\boxed{x_-(d)=\sqrt{48(3/5-d)}+O(3/5-d)}.
\]
The orbit near \(E_0\) attracts and that near \(E_-\) repels. Their nontrivial Floquet multipliers \(M_\pm\) obey
\[
\log M_+(d)=-2\pi d+o(d),\qquad
\log M_-(d)=\sqrt2\,\pi(3/5-d)+o(3/5-d).
\]
The constants are for the actual vector-field time and the displayed Cartesian section; no freely rescaled normal-form clock is used.

## Assumptions and scope
The parameter \(d\) is real and sufficiently close to zero from above, or sufficiently close to \(3/5\) from below, respectively. Each section coordinate is \(x>0\): \(y=0\) for \(E_0\), and \(y=-3\) for \(E_-\). The cycles mentioned are the unique sufficiently small nonconstant periodic orbits near the indicated equilibrium. The unperturbed angular velocities are \(1\) and \(\sqrt2\), respectively. No assertion is made here about an arbitrary, distant limit cycle or monotonicity over the entire parameter windows.

## Proof
First, the only equilibria off the invariant line \(y=-1\) are \(E_0\) and \(E_-\). At \(E_0\) use \((u,v)=(x,y)\), set \(\mu=d\), \(\omega=1\), \(\sigma=1\). At \(E_-\) use \((u,v)=(x,-(y+3)/\sqrt2)\), set \(\mu=3/5-d\), \(\omega=\sqrt2\), \(\sigma=-1\). In either chart the equations become exactly
\[
\dot u=-\omega v+\sigma\mu u+P(u,v),\qquad
\dot v=\omega u+Q(u,v),
\]
where \(P,Q\) are homogeneous quadratic polynomials. Explicitly,
\[
(P,Q)=\left(\tfrac14u^2+\tfrac15uv-\tfrac13v^2,\;uv\right)
\quad\text{or}\quad
\left(\tfrac14u^2-\tfrac{\sqrt2}{5}uv-\tfrac23v^2,\;uv\right),
\]
respectively. Thus the opposite signs of \(\sigma\) measure the outward and inward eigenvalue crossings at the two centers.

Put \(u=r\cos\theta\), \(v=r\sin\theta\), and abbreviate \(c=\cos\theta\), \(s=\sin\theta\). Define the two cubic trigonometric polynomials
\[
C(\theta)=cP(c,s)+sQ(c,s),\qquad
D(\theta)=cQ(c,s)-sP(c,s),
\]
and set \(F(\theta)=\int_0^\theta C(t)\,dt\). The exact polar equations are
\[
\dot r=\sigma\mu r\cos^2\theta+r^2C(\theta),
\qquad
\dot\theta=\omega-\sigma\mu\sin\theta\cos\theta+rD(\theta).
\]
In each chart, \(\int_0^{2\pi}C=\int_0^{2\pi}D=0\), so \(F(2\pi)=0\). Direct integration, reproducible by the accompanying checker, gives the following exact values, with the rows ordered as \(E_0,E_-\):
\[
\begin{array}{c|cc}
 & I=\int_0^{2\pi}CD\,d\theta
 & J=\int_0^{2\pi}(D^2-FD)\,d\theta\\ \hline
E_0 & \pi/240 & 293\pi/5400\\
E_- & -\sqrt2\,\pi/48 & 793\pi/2700
\end{array}
\]
All integrals are elementary trigonometric-polynomial integrals; in the definition of \(J\), adding a constant to \(F\) would change nothing because \(\int D=0\).

For a sufficiently small positive section radius \(r\), expand \(dr/d\theta\) using the polar equations. Integrating over one positive angular turn yields the local return displacement
\[
\mathcal P_\mu(r)-r=
\frac{\sigma\pi}{\omega}\mu r-
\frac{I}{\omega^2}r^3+
O(\mu^2r+|\mu|r^2+r^4).
\]
The second-order effect of the quadratic radial term contributes \(\frac2{\omega^2}\int_0^{2\pi}FC\,d\theta=0\), since \(F'=C\), \(F(0)=F(2\pi)=0\). The coefficient of \(\mu r\) is \(\frac{\sigma}{\omega}\int_0^{2\pi}\cos^2\theta\,d\theta=\sigma\pi/\omega\).

Because \(\sigma I>0\) in both charts, the displacement is nondegenerate in the squared radius, giving one small positive-radius cycle for \(\mu>0\), with
\[
r^2=\frac{\sigma\pi\omega}{I}\mu+O(\mu^{3/2})=
\begin{cases}240\mu+O(\mu^{3/2})& E_0,\\48\mu+O(\mu^{3/2})& E_- .\end{cases}
\]
This conclusion follows, equivalently, by the standard nondegenerate Hopf theorem and the displayed first-return coefficient. The nontrivial multiplier, the derivative of \(\mathcal P_\mu\) at the cycle radius, is
\[
M=1-\frac{2\sigma\pi}{\omega}\mu+o(\mu).
\]
Thus the first branch is attracting, the second repelling; taking logarithms gives the stated Floquet laws.

To compute *physical time*, integrate \(dt/d\theta=1/\dot\theta\) along the cycle. Uniformly for one turn, its radial profile satisfies \(r(\theta)=r_0+(r_0^2/\omega)F(\theta)+O(r_0^3)\), where \(r_0\) is the section radius and \(\mu=O(r_0^2)\). The terms of first order in \(r_0\) and first order in \(\mu\) integrate to zero because \(\int D=0\) and \(\int\sin\theta\cos\theta=0\). Expansion to order \(r_0^2\) gives
\[
T=\frac{2\pi}{\omega}+\frac{r_0^2}{\omega^3}
\int_0^{2\pi}(D^2-FD)\,d\theta+O(r_0^3).
\]
Substitution of the exact values of \(J\), \(\omega\), and the squared-radius asymptotics yields
\[
\frac{240\cdot293\pi}{5400}=\frac{586\pi}{45},
\qquad
\frac{48\cdot793\pi}{2700(\sqrt2)^3}
=\frac{793\sqrt2\,\pi}{225}.
\]
These two strictly positive coefficients complete the proof.

## Verification
Run `python checker.py` in the same directory. With SymPy installed it directly recomputes the zero-mean trigonometric integrals, the exact \(I,J\) values, the squared-radius constants, and the original-time period coefficients in **both** coordinate charts. If SciPy is available, the checker additionally locates both small cycles by high-accuracy numerical Poincaré returns and compares measured radii and periods at \(\mu=2\cdot10^{-5}\); these finite checks confirm the derived leading coefficients but do not replace the analytical argument. The actual packaged checker was run successfully with both dependencies. The normal-form limit and error bounds are local, and are not asserted to be uniform on the full global existence windows.

## Relationship to prior work
Gasull and Giacomini's arXiv:2210.15803 (first publicly posted 2022-10-27), Section 6.5, equation (13), specifies this very vector field, its invariant line, and qualitative uniqueness/existence bounds for cycles near the two equilibria. Those results are treated as established background. Their statements and the corresponding 2023 journal text do not give the displayed numerical squared-radius constants, original-time first-order period derivatives, or local multiplier slopes. Standard Hopf theory supplies the framework but not the explicit coefficients, particularly the period coefficients that are sensitive to the physical clock and nonlinear angular modulation. Research on period functions of other quadratic centers and near-Hopf cycles in other flows uses different vector fields and does not imply these formulas by parameter substitution.

## Limitations
Only the two small-amplitude branches are analyzed, not the full period function at finite amplitude or global basin boundaries. The exact first-order period coefficients do not prove strict monotonicity throughout the complete cycle-bearing parameter windows. Numerical integration is confirmatory, not a proof. The 1988 related existence work of Holmes was not available in full text in the accessible sources; unindexed or inaccessible equivalent formulae remain a publication-priority risk. There has been no independent mathematical audit.

## References
- A. Gasull and H. Giacomini, *Number of limit cycles for planar systems with invariant algebraic curves*, arXiv:2210.15803 (public 2022-10-27), Section 6.5, equation (13), https://arxiv.org/abs/2210.15803 ; *Qualitative Theory of Dynamical Systems* **22**, 44 (2023), https://doi.org/10.1007/s12346-023-00746-7 .
- C. A. Holmes, *Some quadratic systems with a separatrix cycle surrounding a limit cycle*, *J. London Math. Soc.* s2-37 (1988), 545–551, https://doi.org/10.1112/jlms/s2-37.3.545 . (Full text not inspected.)
- Y. Zhao, *On the monotonicity of the period function of a quadratic system*, *Discrete Contin. Dyn. Syst.* **13** (2005), 795–810, https://doi.org/10.3934/dcds.2005.13.795 . (A distinct quadratic system.)
