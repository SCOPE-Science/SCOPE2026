# Universal logarithmic phase drift and an elliptical scaling limit in a critical business-cycle map

## Finding

Consider the real planar multiplier-accelerator map
\[
 F_\alpha(x,y)=\left(x+y,\;-2(1-\alpha)x+(2\alpha-1)y-2\alpha y^3\right),\qquad \frac12<\alpha<1.
\]
Define
\[
 s=\sqrt{1-\alpha^2},\quad c=\sqrt{\frac{1-\alpha}{1+\alpha}},\quad
 \theta=\arccos\alpha,\quad \tau=\frac c2,\quad R=\sqrt{\frac{1+\alpha}{3\alpha}},
\]
and write \(z_n=(1-\alpha)x_n+y_n+i s x_n\). For each fixed \(\alpha\) there is \(\varepsilon_\alpha>0\) such that every **nonzero** real initial state \(\|(x_0,y_0)\|<\varepsilon_\alpha\) has a real phase \(\Phi\), depending on the state, with
\[
 z_n=\frac R{\sqrt n}\exp\left(i[n\theta+\tau\log n+\Phi]\right)
 +O_{\alpha,x_0,y_0}\left(\frac{\log n}{n^{3/2}}\right),\qquad n\longrightarrow\infty.
\]
Equivalently, the set of **all subsequential limits** of \(\sqrt n(x_n,y_n)\) is precisely the nondegenerate ellipse
\[
 \mathcal E_\alpha=\left\{(X,Y)\in\mathbb R^2:
  \big((1-\alpha)X+Y\big)^2+(1-\alpha^2)X^2
  =\frac{1+\alpha}{3\alpha}\right\}.
\]
The entire ellipse is attained as an accumulation set even if \(\theta/(2\pi)\) is rational. This is a limit-set assertion, not a claim of uniform phase distribution for rational \(\theta/(2\pi)\).

## Assumptions and scope

The parameter range is the entire open interval \(1/2<\alpha<1\); no Diophantine or irrationality assumption is imposed. Initial data lie in a sufficiently small punctured neighborhood of the origin, whose radius may depend on \(\alpha\). The statement concerns the unforced, exactly specified real-valued map and forward integer iterations \(n\ge0\). The origin itself remains fixed and is excluded from the asymptotic formula. The estimate is pointwise in fixed \(\alpha\) and initial data, not uniform near either endpoint of the parameter interval.

The map is the neutral-parameter specialization \(a=1-b\), \(\alpha=(2-b)/2\) of the Puu--Sushko cubic multiplier-accelerator system, as analyzed in Section 4.1 of Grushkovskaya (first public 16 October 2024). This is the **same dynamical map**, not an alternative model with a fitted correction.

## Proof

**1. Complex linear coordinate and cubic coefficient.** Put \(s=\sqrt{1-\alpha^2}\), \(c=(1-\alpha)/s\), \(\omega=\alpha+i s=e^{i\theta}\), and \(z=(1-\alpha)x+y+i s x\). Its inverse is
\[
 x=\frac{\operatorname{Im}z}{s},\qquad y=\operatorname{Re}z-c\operatorname{Im}z.
\]
Direct substitution into the original recurrence (not into a truncated model) gives the exact identity
\[
 z'=\omega z-2\alpha\left(\operatorname{Re}z-c\operatorname{Im}z\right)^3.
\]
Writing \(d=(1+i c)/2\), one has \(y=dz+\bar d\bar z\). Thus the coefficient of the resonant monomial \(z^2\bar z\) in the cubic part is exactly
\[
 C=-6\alpha d^2\bar d=-\frac{3\alpha}{2(1+\alpha)}(1+i c).
\]
The useful identities \(1+c^2=2/(1+\alpha)\) and \(\bar\omega(1+i c)=1-i c\) give
\[
 \bar\omega C=-a_\alpha+i b_\alpha,\qquad
 a_\alpha=\frac{3\alpha}{2(1+\alpha)}>0,\quad
 b_\alpha=a_\alpha c>0.
\]

**2. Legitimate nonresonant cubic normalization.** For the cubic monomials \(z^3\), \(z\bar z^2\), \(\bar z^3\), the homological denominators are \(\omega-\omega^3\), \(\omega-\omega\bar\omega^2\), and \(\omega-\bar\omega^3\), respectively. They are nonzero because \(0<\theta<\pi/3\) (in particular \(\omega^2\ne1\) and \(\omega^4\ne1\)). A real-analytic near-identity odd cubic coordinate transformation \(u=z+H_3(z,\bar z)\), locally invertible near zero, therefore eliminates exactly these nonresonant cubic terms. The coefficient \(C\) of the resonant term is unchanged. Because the original polynomial map is odd and contains no even-degree terms, the remaining error is fifth order:
\[
 u'=\omega u+C u^2\bar u+O_\alpha(|u|^5)
 =\omega u\big[1+(-a_\alpha+i b_\alpha)|u|^2+O_\alpha(|u|^4)\big].
\]
All remainder bounds hold uniformly on a fixed sufficiently small neighborhood for each fixed parameter.

**3. Attraction and sharp radius.** If \(\rho_n=|u_n|^2\), the normal form gives
\[
 \rho_{n+1}=\rho_n-2a_\alpha\rho_n^2+O_\alpha(\rho_n^3).
\]
Choose the neighborhood sufficiently small that \(\rho_{n+1}\le \rho_n-a_\alpha\rho_n^2\), and sufficiently small that the coordinate map and its inverse are diffeomorphisms there. Every nonzero small initial state then stays in the neighborhood, never reaches zero (local invertibility), and satisfies \(\rho_n\downarrow0\). Reciprocation yields
\[
 \rho_{n+1}^{-1}-\rho_n^{-1}=2a_\alpha+O_\alpha(\rho_n).
\]
Initially this implies \(\rho_n\asymp n^{-1}\). Summing again, using \(\sum_{j\le n}\rho_j=O(\log n)\), yields
\[
 \rho_n^{-1}=2a_\alpha n+O_{\alpha,u_0}(\log n),\qquad
 |u_n|=\frac{1}{\sqrt{2a_\alpha n}}+O\!\left(\frac{\log n}{n^{3/2}}\right).
\]
Here \(1/\sqrt{2a_\alpha}=R\).

**4. Actual phase, not a frozen-angle approximation.** Choose a continuous lift \(\varphi_n\) of the argument of the nonzero \(u_n\) along consecutive iterates, with increments near \(\theta\). The multiplicative normal form yields
\[
 \varphi_{n+1}-\varphi_n=\theta+b_\alpha\rho_n+O_\alpha(\rho_n^2).
\]
The radial estimate implies \(\rho_n=(2a_\alpha n)^{-1}+O(\log n/n^2)\). Therefore both \(\sum_n\rho_n^2\) and \(\sum_n[\rho_n-(2a_\alpha n)^{-1}]\) converge absolutely. The harmonic-number asymptotic then shows that
\[
 \varphi_n-n\theta-\frac{b_\alpha}{2a_\alpha}\log n
 =\Phi+O\!\left(\frac{\log n}{n}\right)
\]
for some finite \(\Phi\) (modulo \(2\pi\)). Since \(b_\alpha/(2a_\alpha)=c/2=\tau\), combining radius and angle gives the asserted formula for \(u_n\). Finally \(z_n=u_n+O(|u_n|^3)\) transfers the formula to the **original** physical coordinate with the same leading amplitude and phase.

**5. Why the entire ellipse is the limit set, including rational rotation.** Set \(\psi_n=n\theta+\tau\log n+\Phi\). If \(\theta/(2\pi)\) is irrational, for any integer \(k\ne0\), summation by parts applied to \(\sum_{n\le N}e^{ikn\theta}n^{ik\tau}\) gives \(O_k(1+\log N)\): partial sums of \(e^{ikn\theta}\) are bounded and the total variation of \(n^{ik\tau}\) is \(O_k(\log N)\). Weyl's criterion therefore gives equidistribution of \(\psi_n\) modulo \(2\pi\).

If \(\theta/(2\pi)=p/q\) is rational in lowest terms, restrict to \(n=qj+r\) for any fixed residue \(r\). Modulo \(2\pi\), the linear part is constant, while the remaining \(\tau\log(qj+r)\) increases without bound with consecutive increments tending to zero; because \(\tau>0\), it accumulates at every angle. Thus in both cases the angular accumulation set is the full circle. The inverse real-linear map \((\operatorname{Re}z,\operatorname{Im}z)\mapsto(x,y)\) sends the circle of radius \(R\) precisely onto \(\mathcal E_\alpha\). The vanishing scaled error does not alter the limit set.

## Verification

The accompanying standalone script `verify_phase.py` checks, using only the Python standard library: the exact complex-coordinate identity and the resonant coefficient at representative parameter values; the expected \(n|z_n|^2\) limit; and convergence of the corrected physical phase at both an irrational rotation angle and a rational rotation angle \(\theta=\pi/5\). All checks have been run against the packaged script. These finite checks support, but do not replace, the analytic proof in the preceding section.

## Relationship to prior work

Grushkovskaya, *Asymptotic behavior of solutions of nonlinear discrete systems in critical cases* (16 October 2024), proves local asymptotic stability and polynomial upper decay bounds for broad neutral maps and explicitly treats this same business-cycle map in Section 4.1. That article computes the leading real radial normal-form coefficient but neither a finite asymptotic **angular phase** after subtracting \(n\theta+\tau\log n\) nor the exact complete elliptical subsequential limit set. The present argument requires the imaginary resonant coefficient and a summability argument beyond the published upper-bound theorem.

Puu and Sushko, *A business cycle model with cubic nonlinearity* (2004), study the same underlying map's fixed-point stability frontier, invariant-circle bifurcations and global basin geometry, rather than critical-orbit phase asymptotics at the frontier. The elliptical limit set here concerns rescaled trajectories approaching the fixed point, **not** an invariant circle of the original unscaled dynamics beyond bifurcation.

Generic nonresonant Neimark--Sacker normal forms are established background. The specific physical-coordinate coefficient \(\tau\), its strict positivity throughout the economic parameter interval, and the rational-angle full-ellipse consequence are the model-specific claims; no novelty of the normal-form method is asserted.

## Limitations

Only sufficiently small nonzero initial conditions are covered, not all real initial conditions. The radius of that neighborhood and the asymptotic-error constants need not be uniform in \(\alpha\), particularly at the excluded endpoints. For rational rotation angles, the sequence of phases need not be equidistributed despite having the full circle as accumulation set. The theorem is a deterministic exact-real statement; it does not forecast observed macroeconomic cycles. Unindexed equivalent treatments of this exact neutral boundary remain a publication-priority risk. No independent mathematical validation is claimed.

## References

1. V. Grushkovskaya, *Asymptotic behavior of solutions of nonlinear discrete systems in critical cases*, **Nonlinear Dynamics** 113 (2025), 1227–1244; first published 16 October 2024. https://doi.org/10.1007/s11071-024-10295-6 ; Section 4.1, equations (42)–(53).
2. T. Puu and I. Sushko, *A business cycle model with cubic nonlinearity*, **Chaos, Solitons & Fractals** 19 (2004), 597–612. https://doi.org/10.1016/S0960-0779(03)00132-2 ; Sections 1–2, especially fixed-point bifurcation.
3. G. Iooss, *Bifurcation of Maps and Applications*, North-Holland (1979); background nonresonant cubic normal forms, not a source for the asserted model-specific phase formula.
