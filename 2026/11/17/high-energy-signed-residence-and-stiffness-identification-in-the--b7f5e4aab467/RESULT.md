# High-energy signed residence and stiffness identification in the Helmholtz–Duffing oscillator

## Finding

For the conservative Helmholtz–Duffing oscillator with **positive cubic restoring coefficient** and arbitrary linear stiffness, quadratic stiffness and constant load, two high-energy observables reconstruct the cubic and quadratic stiffness coefficients uniquely. The ordinary period measures the dominant stiffness, while the signed fraction of time at positive versus negative position measures the subleading asymmetry. The full original-time position distribution also has a universal quartic-oscillator limit after centering at an identifiable displacement.

Let \(h>0\), \(k_1,k_2,F\in\mathbb R\), and consider
\[
\ddot x+k_1x+k_2x^2+hx^3+F=0.
\]
For each sufficiently large energy \(E\), let \(T(E)\) be the minimal physical-time period, \(T_+(E)\) and \(T_-(E)\) the durations with \(x>0\) and \(x<0\), and \(\bar x(E)\) the period-average position. Define
\[
I=\int_0^1\frac{du}{\sqrt{1-u^4}}=\tfrac14 B(\tfrac14,\tfrac12),\qquad
 a_h=(4/h)^{1/4},\qquad s=-\frac{k_2}{3h}.
\]
For fixed coefficients, as \(E\to\infty\),
\[
\begin{aligned}
T(E)&=2\sqrt2\,a_h I\,E^{-1/4}\bigl(1+O(E^{-1/2})\bigr),\\
\bar x(E)&=s+O(E^{-1/2}),\\
\frac{T_+(E)-T_-(E)}{T(E)}
 &=\frac{s}{a_h I}\,E^{-1/4}+O(E^{-3/4}).
\end{aligned}
\]
Consequently the finite limits
\[
L=\lim_{E\to\infty}E^{1/4}T(E)>0,\qquad
R=\lim_{E\to\infty}E^{1/4}\frac{T_+(E)-T_-(E)}{T(E)}
\]
uniquely recover **exactly the leading two stiffness coefficients**:
\[
\boxed{
 a_h=\frac{L}{2\sqrt2 I},\quad h=\frac4{a_h^4},\quad
 s=a_h I R,\quad k_2=-3ha_hIR.
}
\]
In particular, \(\operatorname{sgn}(R)=-\operatorname{sgn}(k_2)\) when \(k_2\ne0\). The lower stiffness \(k_1\) and load \(F\) may differ without changing these limits.

If a time is sampled uniformly on one high-energy period, then the centered and rescaled coordinate
\[
U_E=\frac{x(t)-s}{a_h E^{1/4}}
\]
converges weakly, with \(1\)-Wasserstein error \(O(E^{-1/2})\), to the probability density
\[
p(u)=\frac{\mathbf1_{(-1,1)}(u)}{2I\sqrt{1-u^4}}.
\]
This last statement concerns weak probability metrics, not uniform convergence of densities or total variation.

## Assumptions and scope

Take real fixed coefficients \(k_1,k_2,F\) and \(h>0\). Define the potential and energy by
\[
V(x)=\frac h4x^4+\frac{k_2}{3}x^3+\frac{k_1}{2}x^2+Fx,
\qquad E=\tfrac12\dot x^2+V(x).
\]
For all energies above the largest critical value of \(V\), the equation \(V(x)=E\) has exactly two simple real roots \(x_-<0<x_+\). Its closed energy level is one periodic oval, and every time statistic above is independent of the starting phase. Error constants can depend on the four fixed coefficients; no parameter-uniform claim is made at the coefficient boundary \(h=0\).

## Proof

**1. Canonical depressed quartic.** Set \(s=-k_2/(3h)\) and \(v=x-s\). Direct polynomial expansion gives
\[
V(v+s)=K_0+\frac h4v^4+\frac{K_2}{2}v^2+K_1v,
\]
where \(K_0=V(s)\), \(K_2=k_1-k_2^2/(3h)\), and \(K_1=F-k_1k_2/(3h)+2k_2^3/(27h^2)\). Let
\[
A=\left(\frac{4(E-K_0)}h\right)^{1/4},\quad
u=v/A,\quad \epsilon=\frac{2K_2}{hA^2},\quad
\eta=\frac{4K_1}{hA^3}.
\]
The allowed segment is \(1-u^4-\epsilon u^2-\eta u\ge0\). In particular \(\epsilon=O(A^{-2})\), \(\eta=O(A^{-3})\).

**2. Smooth quadrature through moving turning points.** By the implicit-function theorem there are analytic real turning roots \(u_-(\epsilon,\eta)\) and \(u_+(\epsilon,\eta)\) near \(-1\) and \(1\). Polynomial division gives
\[
1-u^4-\epsilon u^2-\eta u
=(u_+-u)(u-u_-)q_{\epsilon,\eta}(u),
\]
where \(q_{\epsilon,\eta}\) is a quadratic polynomial, positive on the interval for small parameters, and \(q_{0,0}(u)=1+u^2\). Put \(m=(u_++u_-)/2\) and \(d=(u_+-u_-)/2\). The substitution \(u=m+d\sin\theta\) reduces every Abel integral to a *regular analytic parameter-dependent integral*:
\[
J_g(\epsilon,\eta)
=\int_{-\pi/2}^{\pi/2}
\frac{g(m+d\sin\theta)}{\sqrt{q_{\epsilon,\eta}(m+d\sin\theta)}}\,d\theta.
\]
In particular \(J_1(0,0)=2I\). The exact full physical period is
\[
T(E)=\frac{\sqrt2 A}{\sqrt{E-K_0}}\,J_1(\epsilon,\eta).
\]
Analyticity implies \(J_1=2I+O(\epsilon)+O(\eta)\), yielding the asserted period expansion because \(A=a_hE^{1/4}(1+O(E^{-1}))\).

**3. Mean position.** For \(\eta=0\), the depressed energy profile is even: \(m=0\), the integration weight is even in \(u\), and \(J_u(\epsilon,0)=0\). Joint analyticity therefore gives \(J_u(\epsilon,\eta)/J_1(\epsilon,\eta)=O(\eta)\). Thus \(\bar x=s+A\,O(\eta)=s+O(A^{-2})\), which is \(s+O(E^{-1/2})\).

**4. Signed residence.** Let \(p_{\epsilon,\eta}(u)\) be the normalized period-sampling density in the coordinate \(u\), supported between its two moving turning roots. For \(\eta=0\) this density is even and analytic near the interior point \(u=0\); moreover
\[
p_{\epsilon,0}(0)=\frac1{2I}+O(\epsilon).
\]
The original sign threshold \(x=0\) is \(u=-s/A\). For symmetric \(\eta=0\), the signed occupation difference is twice the integral from \(0\) to \(s/A\), with the interval understood as oriented. Taylor expansion at the interior point gives
\[
2\int_0^{s/A}p_{\epsilon,0}(u)\,du
=\frac{s}{AI}+O(A^{-3}).
\]
Moving from \(\eta=0\) to \(\eta=O(A^{-3})\) perturbs the normalized signed integral by \(O(\eta)\): this follows from the regular \(\theta\)-integral above, where the sign threshold stays in the interior and moves analytically with the parameters. Therefore
\[
(T_+-T_-)/T=s/(AI)+O(A^{-3}),
\]
which is the claimed expansion in energy. Taking the two limits gives the explicitly stated inversion formulas.

**5. Universal sampling law.** At \((\epsilon,\eta)=(0,0)\), the period sampling density in \(u\) is exactly \(p(u)\). The regular \(\theta\)-integral provides a common bounded angular parameterization whose density, roots and map \(\theta\mapsto m+d\sin\theta\) change by \(O(|\epsilon|+|\eta|)\). Coupling their quantiles, or using a bounded-Lipschitz test function and the Kantorovich dual characterization on the common compact support, gives a \(1\)-Wasserstein error \(O(|\epsilon|+|\eta|)=O(A^{-2})\). Replacing \(A\) by \(a_hE^{1/4}\) only adds \(O(E^{-1})\).

## Verification

The attached `verify.py` recomputes the two real turning roots, divides the quartic exactly up to floating-point roundoff by their linear factors, and evaluates regularized original-time quadratures using numerical integration for three fixed parameter sets. It compares the scaled period, signed residence and average position with the independently derived limits, and tests the algebraic inverse identities. Run `python verify.py` with NumPy and SciPy. This is numerical corroboration; the infinite-energy statements are proved by the analytic estimates above rather than by finite sampling.

## Relationship to prior work

Big-Alabo and Alfred (first online 20 August 2024) give exact periodic solutions and elliptic-integral physical periods for the completely integrable loaded Helmholtz–Duffing family. Those results are the starting point; they do not state the present signed high-energy occupation coefficient, centered time-sampling distribution or two-observable stiffness inverse. Earlier approximation and elliptic-solution work cited therein also addresses the same oscillator, but not those specific identified high-energy statements in the material inspected. Published mathematical records for other cubic centers, switching centers and quartic oscillators were compared by their implications, not solely by their titles: their phase-space vector fields, time changes or potential structures differ, so their formulas do not imply the current theorem. The exact primary elliptic solution contains enough information in principle to derive our asymptotics; their extraction and coupled inverse identification are the claimed contribution, not the existence of a new exact solution.

## Limitations

The result only identifies the two highest stiffness coefficients. It requires \(h>0\), a fixed conservative undamped equation, and energy tending to infinity; it does not extend unchanged to damped, time-forced or finite-energy inverse estimation. Coefficients of the errors are not uniform over unbounded parameter families. A source presenting the equivalent asymptotic inverse under a different normalization might exist outside the inspected literature. No independent mathematical audit or publication-priority certification has been performed.

## References

1. A. Big-Alabo and P. B. Alfred, *Exact closed-form solution for the completely integrable helmholtz-duffing oscillator with applications to real-world problems*, first published online 20 August 2024, DOI: `10.1177/14613484241275526`, https://doi.org/10.1177/14613484241275526.
2. Y. O. El-Dib, *Insightful and comprehensive formularization of frequency–amplitude formula for strong or singular nonlinear oscillators*, DOI: `10.1177/14613484221118177`, https://doi.org/10.1177/14613484221118177. This discusses frequency–amplitude approximations rather than signed high-energy residence inversion.
