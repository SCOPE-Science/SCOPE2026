# A strict bias and false logarithmic relaxation in the semi-open Glauber scaling shortcut

## Finding

The normalized error-function similarity shortcut proposed for the continuum semi-open zero-temperature Glauber–Ising scaling correlation has a strict sign bias at every interior point and positive time. More significantly, it gives a *non-integrable* approach to the stationary correlation, although the exact theory has a finite, explicitly computable integrated relaxation. This is a quantitative obstruction to using that shortcut for time-integrated quench observables, not a correction to the exact solution itself.

Fix \(L>0\), \(0<x<L\), \(t>0\), and write \(u=x/L\). Let \(C\) solve the boundary/initial-value problem in the next section, and define the previously proposed shortcut \(\widehat C\). Then

\[
0<\widehat C(t,x)<C(t,x)<1-u,\qquad
0<C(t,x)-\widehat C(t,x)<\frac{\operatorname{erf}(x/\sqrt{2t})}{\operatorname{erf}(L/\sqrt{2t})}-u.
\]

For each fixed \(0<u<1\), the exact and shortcut relaxation deficits obey

\[
1-u-C(t,uL)\sim\frac{2}{\pi}\sin(\pi u)e^{-\pi^2t/(2L^2)},\qquad
1-u-\widehat C(t,uL)\sim \frac{L^2}{6t}u(1-u^2).
\]

Consequently, the exact integrated relaxation is finite and **algebraic in spatial position**, whereas the shortcut yields a logarithmically divergent time integral:

\[
\int_0^\infty [1-u-C(t,uL)]\,dt=\frac{L^2}{3}u(1-u)(2-u),
\]

\[
\int_0^T [1-u-\widehat C(t,uL)]\,dt
=\frac{L^2}{6}u(1-u^2)\log(T/L^2)+O_u(L^2),\qquad T\to\infty.
\]

The subtraction \(1-u\) is the *stationary equal-time spatial correlation*, not a time-lag autocorrelation. The second formula describes a quench-relaxation area and makes no claim about the stationary autocorrelation time.

## Assumptions and scope

Work entirely with the **continuum scaling boundary-value problem**, not the finite-spacing microscopic Markov chain. The dimensionless diffusion normalization agrees with Henkel's semi-open continuum equation (11):

\[
\partial_t C(t,x)=\tfrac12\partial_{xx}C(t,x),\quad
C(t,0)=1,\quad C(t,L)=0,\quad C(0,x)=0\ \ (0<x<L).
\]

The initial datum is understood in the interior mild-solution sense; incompatible boundary/initial corner values are allowed. For \(t>0\) the solution is classical and bounded. Its stationary profile is \(1-x/L\). The source's proposed similarity shortcut is

\[
\widehat C(t,x)=1-\frac{\operatorname{erf}(x/\sqrt{2t})}{\operatorname{erf}(L/\sqrt{2t})}.
\]

All inequalities are strict only when \(t>0\) and \(0<x<L\); both boundary values agree exactly, and limits at \(t=0\) require respecting the corner incompatibility. Scaling \(t\) by \(L^2\) reduces the formulas to a universal interval.

## Proof

**Step 1: exact spectral representation.** Subtract the stationary harmonic function \(1-u\). The Dirichlet heat equation for \(R(t,u)=1-u-C(t,uL)\) has initial profile \(1-u\), whose sine coefficients are \(2/(n\pi)\). Thus

\[
R(t,u)=\frac{2}{\pi}\sum_{n=1}^{\infty}\frac{\sin(n\pi u)}{n}
\exp\left(-\frac{n^2\pi^2t}{2L^2}\right),
\]

with absolute, uniform convergence for every \(t\ge\epsilon>0\). This coincides with Henkel's exact leading theta-function expression (17a). The positive first eigenmode dominates every fixed interior \(u\) as \(t\to\infty\), giving the stated exponential asymptotic. The strong maximum principle on the positive-initial-data Dirichlet heat problem gives \(R(t,u)>0\) for every interior point at positive time, hence \(C(t,x)<1-u\).

**Step 2: the strict signed approximation error.** Put

\[
F(t,x)=\operatorname{erf}(x/\sqrt{2t}),\qquad H(t)=F(t,L).
\]

For positive time, \(F_t=\frac12 F_{xx}\), \(F(t,x)>0\) for \(x>0\), \(H(t)>0\), and

\[
H'(t)=-\frac{L}{\sqrt{2\pi}\,t^{3/2}}e^{-L^2/(2t)}<0.
\]

Direct differentiation (the time dependence of \(H\) cannot be discarded) gives the signed residual

\[
\left(\partial_t-\tfrac12\partial_{xx}\right)\widehat C(t,x)
=\frac{F(t,x)H'(t)}{H(t)^2}<0.
\]

Both \(C\) and \(\widehat C\) have identical boundary values and vanish in the interior as \(t\downarrow0\). Their difference \(E=C-\widehat C\) is the Dirichlet heat solution forced by the strictly positive function \(-F H'/H^2\), so positivity of the killed interval heat kernel or the strong parabolic comparison principle implies \(E>0\) everywhere in the open space-time domain. Since \(F(t,x)<H(t)\) for \(0<x<L\), also \(\widehat C>0\). Finally, \(C<1-u\) implies \(E<1-u-\widehat C=F/H-u\), proving the strict envelope. One may apply comparison first on finite time strips bounded away from \(t=0\), then take the limit, using the common interior initial trace.

**Step 3: long-time shortcut tail.** Write \(y=L/\sqrt{2t}\). Taylor's theorem at the origin gives, for each fixed \(0<u<1\),

\[
\frac{\operatorname{erf}(uy)}{\operatorname{erf}(y)}
=u+\frac{u(1-u^2)}3y^2+O_u(y^4).
\]

Consequently,

\[
1-u-\widehat C(t,uL)
=\frac{L^2}{6t}u(1-u^2)+O_u(L^4/t^2).
\]

Combining this with the exponentially small exact \(R\), the difference \(C-\widehat C\) has the same positive \(t^{-1}\) leading coefficient. Integration from any fixed time to \(T\) proves the logarithmic divergence; the early-time integral is finite because the shortcut deficit is bounded by \(1-u\).

**Step 4: finite exact integral.** Define \(A(u)=\int_0^\infty R(t,u)\,dt\). The spectral gap justifies integrating the equation \(R_t=(2L^2)^{-1}R_{uu}\):

\[
\frac1{2L^2}A''(u)=R(\infty,u)-R(0,u)=-(1-u),
\qquad A(0)=A(1)=0.
\]

Two integrations give uniquely \(A(u)=\frac{L^2}{3}u(1-u)(2-u)\), as claimed. This result also follows by integrating the convergent sine-mode series and summing its cubic reciprocal coefficients. Neither argument relies on finite-grid experiments.

## Verification

The standalone `verify.py` reproduces the symbolic Poisson problem and its endpoint values, compares the exact Fourier solution with an independently diagonalized finite-difference Dirichlet heat semigroup at twenty points, checks the strict sign/envelope at interior parameter grids and the analytic large-time coefficient, and checks the area formula against independently summed spectral integrals. Execute using `python verify.py` with NumPy, SciPy, and SymPy. All tests passed on the supplied file. Finite numerical tests do not prove the all-time inequalities or the asymptotic quantifiers; those follow from the maximum-principle and Taylor arguments above.

## Relationship to prior work

Malte Henkel's June 15, 2026 arXiv manuscript derives the *exact* semi-open scaling correlation as a theta function in equation (17a), then proposes the one-variable normalized error-function shortcut in equation (20). Section 2.3 and Figure 3 explicitly show that the shortcut is only approximate and disagree around the finite-size crossover. That recognition is **prior work**, not claimed as a discovery here. The present additional claim is the **global strict sign**, an analytic leading \(t^{-1}\) bias, and a qualitative failure of the shortcut for the exact time-integrated relaxation, including its coefficient and the exact finite integrated area. The journal edition is the same work, not an independent source.

Henkel's 2025 finite-size ageing treatment addresses the periodically closed chain and does not analyze this semi-open normalized-error-function shortcut. Elementary Dirichlet heat-semigroup theory supplies the comparison tools, but does not itself specify the normalized shortcut, the physical finite-size normalization, or its divergent integrated-correlation consequence. Searches of the published mathematical-results record did not reveal this combined finding, although absence from an index is not a uniqueness guarantee.

## Limitations

The statement is restricted to the continuum leading scaling correlation and the explicit normalized error-function candidate; there is no assertion about generic similarity approximations, the fixed-microscopic-spacing lattice at arbitrary times, or finite-temperature Glauber chains. The earlier article already established that the shortcut is *not exact*; only the stated quantitative strengthening is claimed here. The integrated deficit concerns the relaxation after a quench, not a two-time Green–Kubo transport integral. An implicit consequence in prior mathematical heat-kernel literature or an unindexed treatment cannot be ruled out.

## References

1. Malte Henkel, *Exact solution of the Glauber-Ising model on the finite-length semi-open chain*, arXiv:2606.16848, first public 2026-06-15, especially equations (11), (17a), (20), (21), section 2.3 and Figure 3; journal version *Entropy* **28** (2026), 771, doi:10.3390/e28070771. Full text: https://www.preprints.org/manuscript/202606.1468 .
2. Malte Henkel, *Finite-size scaling in the ageing dynamics of the 1D Glauber-Ising model*, arXiv:2501.05912 (2025), periodic-boundary context.
