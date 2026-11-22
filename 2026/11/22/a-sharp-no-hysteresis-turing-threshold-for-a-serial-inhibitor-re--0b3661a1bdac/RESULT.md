# A sharp no-hysteresis Turing threshold for a serial-inhibitor reaction–diffusion triad

## Finding

For the three-component Neumann reaction–diffusion system below, the zero homogeneous state is linearly stable to every spatial mode **if and only if** it is the *only* stationary state. If a mode becomes linearly unstable, there are at least two distinct nonconstant smooth stationary solutions. Thus the entire stationary-pattern existence diagram is determined by the strict linear Turing criterion, with no hidden subcritical steady patterns, even at a neutral threshold.

More precisely, let \(0<a<1/2\), \(a<\zeta<2(1-a)^2\), \(d>0\), and \(L>0\). Define the Neumann eigenvalues \(q_j=(j\pi/L)^2\), \(j=0,1,\ldots\), and
\[
\ell_d(q)=a-q-\frac{\zeta}{(1+dq)^2}.
\]
There are nonconstant classical equilibria **exactly when** \(\ell_d(q_j)>0\) for at least one \(j\ge1\). In that case a pair of opposite equilibria minimizes an explicitly given stationary energy below its value at zero. If \(L\le\pi/\sqrt a\), no nonconstant equilibria exist for any \(d>0\). If \(L>\pi/\sqrt a\), define
\[
d_L=\min_{\substack{j\ge1\\q_j<a}}
\frac{\sqrt{\zeta/(a-q_j)}-1}{q_j}.
\]
Then nonconstant equilibria exist if and only if \(d>d_L\); at equality the only equilibrium is zero.

There is a unique continuum threshold \(d_*>1/(2a)\) satisfying
\[
\frac{4(1+a d_*)^3}{27d_*}=\zeta,
\qquad q_* = \frac{2ad_*-1}{3d_*}.
\]
For every finite \(L>\pi/\sqrt a\), one has \(d_L\ge d_*\), with equality exactly when \(L\sqrt{q_*}/\pi\) is a positive integer. As \(L\to\infty\), the sharp boundary shift is
\[
d_L-d_* = \frac{6\pi^2d_*^2}{(1+d_*q_*)L^2}
\operatorname{dist}\!\left(\frac{L\sqrt{q_*}}\pi,\mathbb Z\right)^2+O(L^{-3}).
\]
The remainder is uniform over all sufficiently large lengths. This term resolves the arithmetic mismatch between the continuum-preferred wavelength and discrete Neumann modes.

## Assumptions and scope

Let \(x\in(0,L)\), \(t\ge0\), with homogeneous Neumann boundary conditions on all three fields. The real-valued fields obey
\[
\begin{aligned}
\partial_t u&=\partial_{xx}u+a u-\zeta w-u^3,\\
\partial_t v&=d\partial_{xx}v-v+u,\\
\partial_t w&=d\partial_{xx}w-w+v.
\end{aligned}
\]
All three species diffuse strictly positively, and the two successive inhibitor stages have the same diffusivity \(d\). The nonlinear activator saturation is local and cubic. No positivity or mass-conservation condition on the signed deviation fields is assumed. An equilibrium means a real classical solution of the stationary Neumann equations. Pattern existence here does **not** assert dynamical stability of individual nonzero equilibria or global convergence of the time-dependent system.

The parameter inequalities guarantee a unique homogeneous equilibrium, strict homogeneous spectral stability, positivity of two of the Routh–Hurwitz coefficients, and exclusion of finite-frequency linear instabilities at all wavenumbers. No result is asserted outside this parameter region.

## Proof

**1. Linear spectrum and its sign.** The linearized matrix at Neumann squared wavenumber \(q\ge0\) is
\[
M(q)=\begin{pmatrix}a-q&0&-\zeta\\1&-1-dq&0\\0&1&-1-dq\end{pmatrix}.
\]
Write \(X=q-a\), \(Y=1+dq\). Its characteristic polynomial is
\[
P_q(\lambda)=(\lambda+X)(\lambda+Y)^2+\zeta
=\lambda^3+(X+2Y)\lambda^2+Y(2X+Y)\lambda+XY^2+\zeta.
\]
Since \(q\ge0\), \(0<a<1/2\) and \(Y\ge1\), the quadratic and linear coefficients are strictly positive. The last coefficient is \(-Y^2\ell_d(q)\). Moreover,
\[
(X+2Y)Y(2X+Y)-(XY^2+\zeta)
=2Y(X+Y)^2-\zeta\ge2(1-a)^2-\zeta>0.
\]
Hence the cubic Routh–Hurwitz criterion gives strictly negative real parts for every root exactly when \(\ell_d(q)<0\). At equality there is one simple root at zero and two roots in the strict left half-plane. If \(\ell_d(q)>0\), the constant term is negative and the polynomial has a positive real root. No oscillatory crossing can arise while \(\ell_d(q)\le0\). For \(q_0=0\), \(\ell_d(0)=a-\zeta<0\), proving strict homogeneous stability.

**2. Stationary reduction.** Let \(B_d=I-d\partial_{xx}\) with Neumann boundary conditions. This positive self-adjoint operator has eigenvalues \(1+dq_j\). Any stationary solution satisfies \(v=B_d^{-1}u\), \(w=B_d^{-2}u\). Substitution leaves
\[
\partial_{xx}u+a u-\zeta B_d^{-2}u-u^3=0.
\]
On the real Sobolev space \(H^1(0,L)\), define
\[
\mathcal E_d(u)=\frac12\int_0^L\left(|u'|^2-a u^2\right)dx
+\frac\zeta2\langle u,B_d^{-2}u\rangle_{L^2}
+\frac14\int_0^L u^4dx.
\]
The bounded nonnegative operator \(B_d^{-2}\) is self-adjoint. The functional is differentiable and its Euler–Lagrange equation is precisely the displayed scalar stationary equation. It is bounded below and coercive on \(H^1\): Young's inequality bounds \(a\|u\|_2^2/2\) by an arbitrary positive fraction of \(\|u\|_4^4\) plus a constant; the \(H^1\) derivative term is nonnegative. A bounded minimizing sequence has a weakly convergent subsequence in \(H^1\) and a strongly convergent subsequence in \(L^2\) and \(L^4\) in one dimension. These convergences give a global minimizer. Elliptic regularity for the Neumann elliptic cascade makes every minimizer classical.

**3. Exact nonlinear no-pattern criterion.** Expand \(u\) in the orthonormal Neumann cosine basis. Multiplying the stationary scalar equation by \(u\) and integrating yields
\[
\sum_{j\ge0}\ell_d(q_j)|\widehat u_j|^2=\int_0^L u^4dx.
\]
If all \(\ell_d(q_j)\le0\), the left side is nonpositive while the right side is nonnegative; therefore \(u=v=w=0\). This argument includes all neutral cases and does not presume small amplitudes. Conversely, if some \(\ell_d(q_j)>0\), choose a normalized cosine eigenfunction \(\varphi_j\). For small nonzero \(\varepsilon\),
\[
\mathcal E_d(\varepsilon\varphi_j)
=-\tfrac12\varepsilon^2\ell_d(q_j)
+\tfrac14\varepsilon^4\int_0^L\varphi_j^4dx<0=\mathcal E_d(0).
\]
Thus the energy minimizer is nonzero. Odd symmetry of the stationary equations supplies its distinct negative. Constant stationary solutions require \((a-\zeta)u-u^3=0\), so zero is the only constant equilibrium. Both nonzero minimizers are therefore nonconstant patterns.

**4. Sharp finite-length threshold.** If \(q\ge a\), then \(\ell_d(q)<0\) for every \(d>0\). If \(0<q<a\), the inequality \(\ell_d(q)>0\) is equivalent to
\[
d>\frac{\sqrt{\zeta/(a-q)}-1}{q}.
\]
The numerator is positive because \(\zeta>a\). The eligible Neumann set is finite, and it is nonempty precisely when \(q_1<a\), i.e. \(L>\pi/\sqrt a\). Minimizing over those modes proves the threshold formula and its strict endpoint.

**5. Continuum criticality and arithmetic shift.** The continuous squared-wavenumber instability criterion is \((a-q)(1+dq)^2>\zeta\) for some \(0<q<a\). Its maximum over \([0,a]\) is \(a\) if \(d\le1/(2a)\), and otherwise occurs uniquely at \(q=(2ad-1)/(3d)\), with value \(4(1+ad)^3/(27d)\). The latter increases strictly from \(a\) to infinity with \(d\), proving existence and uniqueness of \(d_*\) and \(q_*\). Hence the discrete threshold is at least \(d_*\), and strict uniqueness of the continuous minimizing wavenumber implies equality exactly at commensurate lengths.

Let \(D(q)=(\sqrt{\zeta/(a-q)}-1)/q\). It has its unique global minimum at \(q_*\), and direct differentiation at that minimum gives
\[
D''(q_*)=\frac{3d_*^2}{q_*(1+d_*q_*)}>0.
\]
For large \(L\), the optimizing integer is a nearest integer to \(L\sqrt{q_*}/\pi\), up to a possible choice between adjacent integers that changes the expansion only at order \(L^{-3}\). Taylor expansion, using \(q_j-q_*=2\sqrt{q_*}\pi(j-L\sqrt{q_*}/\pi)/L+O(L^{-2})\), gives the stated uniform correction.

For an exact calibration, \(a=1/4\) and \(\zeta=1/2\) yield \(d_*=8\), \(q_*=1/8\). On \(L=\pi\sqrt8\) the first positive Neumann mode reaches criticality at \(d=8\) exactly. At \(L=3\pi\), the threshold is \(9(\sqrt{18/5}-1)>8\). At \(L\le2\pi\), all stationary patterns are excluded for every positive \(d\).

## Verification

The accompanying standalone `checker.py` uses independent numerical matrix eigenvalues, exact rational determinant expansions, analytical threshold examples, and negative-energy witnesses. It passed 983 independent matrix-spectrum sign comparisons, plus all exact coefficient and threshold assertions and large-domain sampling tests. Run with Python 3 and NumPy: `python checker.py`. These finite calculations are diagnostics; the all-length, all-parameter statements follow from the analytic variational and spectral arguments above. The proof does not rely on an exhaustive parameter sweep or numerical detection of equilibria.

## Relationship to prior work

Haas and Goldstein (2020/2021) study diffusivity thresholds and show the importance of three diffusing components and two equal diffusion rates, but analyze sampled *linear* reaction Jacobians, not stationary nonlinear variational classification or finite-domain arithmetic. Villar-Sepúlveda and Champneys (2023) give broad linear Turing/wave criteria; their discussion explicitly separates nonlinear bifurcation type as work beyond their analysis. Diego and collaborators (2017/2018) classify Turing network topology and diffusion constraints, again without the present exact global nonzero-stationary-state equivalence and Neumann threshold shift for this serial-inhibitor cubic family. Published finite-domain Turing counterexamples concern discrete-mode selection for other kinetics; that familiar issue alone does not supply the explicit nonlinear if-and-only-if result, critical-length obstruction, or the commensurability coefficient.

The linear Routh–Hurwitz criterion, cosine mode quantization, and direct-method existence of minimizers are standard tools, not separately claimed as new. The assessed statement is their joint exact classification for the specified feedback cascade, including exclusion of *all* finite-amplitude stationary patterns below onset and the quantitative commensurability law.

## Limitations

The signed cubic fields need not remain positive and do not represent conserved species concentrations. The variational functional pertains to equilibria after eliminating the inhibitor stages; it is not asserted to decrease along the original three-field time evolution. Nonzero minimizing stationary solutions are not certified dynamically attracting. The one-dimensional Neumann geometry, equal inhibitor diffusivities, exact cubic saturation, and parameter inequalities are essential to the asserted theorem. The result does not rule out time-periodic or more general nonstationary attractors away from equilibrium. Literature priority beyond the inspected sources remains subject to independent checking, particularly possible implicit conclusions of general gradient-system results.

## References

1. P. A. Haas and R. E. Goldstein, “Turing's diffusive threshold in random reaction-diffusion systems,” arXiv:2011.04614, first publicly submitted 9 November 2020; *Physical Review Letters* 126, 238101 (2021). https://arxiv.org/abs/2011.04614
2. E. Villar-Sepúlveda and A. R. Champneys, “General conditions for Turing and wave instabilities in reaction-diffusion systems,” *Journal of Mathematical Biology* 86, 39 (2023). https://doi.org/10.1007/s00285-023-01870-3
3. X. Diego, L. Marcon, P. Müller and J. Sharpe, “Key features of Turing systems are determined purely by network topology,” arXiv:1708.09645, first submitted 31 August 2017; *Physical Review X* 8, 021071 (2018). https://arxiv.org/abs/1708.09645
