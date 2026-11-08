# Sharp annealed–quenched memory suppression at a skew Brownian junction

## Finding

Consider \(N\ge1\) independent skew Brownian particles initially placed independently and uniformly in \([0,L]\). All particles have diffusivity \(D>0\), and the skew junction at \(0\) has parameter \(-1\le\beta\le1\) (positive-excursion probability \((1+\beta)/2\)). At time \(t>0\), count the particles **currently outside** \([0,L]\), not the number that have ever exited. Denote the variance of this count with initial positions re-randomized by \(V_{\mathrm{an}}(t,\beta)\); denote the initial-position average of its variance conditional on the initial positions by \(V_{\mathrm{qu}}(t,\beta)\). Let \(\Delta_\beta=V_{\mathrm{an}}-V_{\mathrm{qu}}\).

**Theorem.** For every \(N\ge1\), \(L,D,t>0\) and \(\beta\in[-1,1]\), define \(g_t(z)=(4\pi Dt)^{-1/2}\exp[-z^2/(4Dt)]\),
\[
A_t(x)=\int_0^L g_t(y-x)\,dy,\qquad B_t(x)=\int_0^L g_t(y+x)\,dy,
\]
and use a bar for expectation under uniform \(x\in[0,L]\). Then
\[
\Delta_\beta(t)=N\operatorname{Var}_x(A_t+\beta B_t)
=N\bigl[\operatorname{Var}(A_t)+2\beta\operatorname{Cov}(A_t,B_t)+\beta^2\operatorname{Var}(B_t)\bigr]>0.
\]
This is strictly convex in \(\beta\), with the **unique** minimizing junction at any finite positive time
\[
\beta_{\mathrm{opt}}(t)=\operatorname{clip}_{[-1,1]}
\left(-\frac{\operatorname{Cov}(A_t,B_t)}{\operatorname{Var}(B_t)}\right).
\]
Its boundary-control limits are
\[
\lim_{t\downarrow0}\beta_{\mathrm{opt}}(t)=1,
\qquad\lim_{t\to\infty}\beta_{\mathrm{opt}}(t)=-\frac1{61}.
\]
Thus at least one finite-time reversal from \(\beta>0\) to \(\beta<0\) occurs. No uniqueness of the reversal time is asserted. Uniformly over all \(\beta\in[-1,1]\),
\[
\Delta_\beta(t)=\frac{NL^6}{11520\pi D^3t^3}
\bigl(61\beta^2+2\beta+1\bigr)
+O_{N,L,D}(t^{-4}),\qquad t\to\infty.
\]
The asymptotic minimizer suppresses the leading memory coefficient by exactly \(60/61\) relative to the freely crossing junction \(\beta=0\), whereas the reflecting junction \(\beta=1\) has \(64\) times the free-junction coefficient. The positive-excursion probability at the long-time optimum is \(30/61\).

## Assumptions and scope

The transition density is that of standard skew Brownian motion at one point on the **whole line**, with generator \(D\partial_{xx}\) off the origin. Its density for \(x>0\) is
\[
p_\beta(t;x,y)=\begin{cases}
g_t(y-x)+\beta g_t(y+x),&y>0,\\
(1-\beta)g_t(|y|+x),&y<0.
\end{cases}
\]
The two limits are ordinary unconstrained Brownian motion (\(\beta=0\)) and reflection into the positive half-line (\(\beta=1\)); \(\beta=-1\) makes the origin one-way from the positive to the negative half-line. The right endpoint \(L\) is **not** a physical wall: it is only a counting-window boundary. The junction is a scale-invariant local-time skew mechanism, not a finite-permeability Robin membrane with a fixed length or time scale. This distinction is necessary in interpreting the result. All particles use independent Brownian noises and independent initial positions. The total particle number \(N\) is fixed.

## Proof

**1. Conditional counting probabilities.** Integrating the transition density over the counting interval gives
\[
S_\beta(x,t)=\mathbb P_x(X_t\in[0,L])=A_t(x)+\beta B_t(x),
\quad U_\beta(x,t)=1-S_\beta(x,t).
\]
The integrals are explicitly
\[
A_t(x)=\Phi\!\left(\frac{L-x}{\sqrt{2Dt}}\right)
-\Phi\!\left(\frac{-x}{\sqrt{2Dt}}\right),\quad
B_t(x)=\Phi\!\left(\frac{L+x}{\sqrt{2Dt}}\right)
-\Phi\!\left(\frac{x}{\sqrt{2Dt}}\right),
\]
where \(\Phi\) is the standard normal distribution function. Given initial positions, the indicators of being outside are independent Bernoulli variables of probabilities \(U_\beta(x_i,t)\). Consequently
\[
V_{\mathrm{an}}=N\overline U_\beta(1-\overline U_\beta),\qquad
V_{\mathrm{qu}}=N\overline{U_\beta(1-U_\beta)}.
\]
Their difference equals \(N\operatorname{Var}_x(U_\beta)=N\operatorname{Var}_x(S_\beta)\), establishing the exact quadratic.

**2. Strictness and uniqueness.** For each \(t>0\), \(B_t'(x)=g_t(L+x)-g_t(x)<0\) on \([0,L]\) (including \(x=0\)); hence \(\operatorname{Var}(B_t)>0\) and the quadratic in \(\beta\) is strictly convex. If \(S_\beta\) were constant in \(x\), differentiating at \(x=0\) would give
\[
0=S_\beta'(0)=(1-\beta)\bigl[g_t(0)-g_t(L)\bigr],
\]
which forces \(\beta=1\). But then
\[
S_1'(L)=g_t(2L)-g_t(0)<0,
\]
a contradiction. This proves strict positivity for every finite time and every admissible skew parameter, including both endpoints, and the unique clipped-quadratic minimizer.

**3. Short-time optimum.** Write \(h=\sqrt{2Dt}\) and \(H_0(x)=\Phi(-x/h)\), \(H_L(x)=\Phi(-(L-x)/h)\), and \(H_+(x)=\Phi(-(L+x)/h)\). Direct Gaussian integration gives
\[
B_t=H_0-H_+,
\qquad A_t+B_t=1-H_L-H_+.
\]
The boundary layers of \(H_0\) and \(H_L\) have width \(O(h)\) around opposite ends. Gaussian tail bounds give \(\operatorname{Var}(B_t)=\Theta(h/L)\) and \(\operatorname{Cov}(A_t+B_t,B_t)=O((h/L)^2)+O(e^{-cL^2/h^2})\) for a positive constant \(c\). Therefore the unconstrained minimizer satisfies
\[
-\frac{\operatorname{Cov}(A_t,B_t)}{\operatorname{Var}(B_t)}
=1-\frac{\operatorname{Cov}(A_t+B_t,B_t)}{\operatorname{Var}(B_t)}\longrightarrow1.
\]
Clipping to \([-1,1]\) preserves this limit. In addition, \(B_t\) and \(A_t+B_t\) are both strictly decreasing in \(x\), so their covariance is positive, and the unconstrained optimizer always lies strictly below \(1\).

**4. Long-time coefficient.** Put \(u=x/L\) and \(\epsilon=L^2/(4Dt)\). Expanding the Gaussian kernel on the compact square \([0,L]^2\), uniformly in \(\beta\in[-1,1]\), yields
\[
S_\beta(x,t)=\frac{L}{\sqrt{4\pi Dt}}
\left[(1+\beta)-\epsilon\left((1+\beta)\left(u^2+\frac13\right)+(\beta-1)u\right)+O(\epsilon^2)\right].
\]
The remainder is differentiable in \(\beta\), with uniformly bounded coefficients for bounded \(\beta\). For uniform \(u\in[0,1]\),
\[
\operatorname{Var}(u)=\frac1{12},\quad
\operatorname{Var}(u^2)=\frac4{45},\quad
\operatorname{Cov}(u,u^2)=\frac1{12}.
\]
It follows by direct algebra that
\[
\operatorname{Var}\bigl((1+\beta)u^2+(\beta-1)u\bigr)
=\frac{61\beta^2+2\beta+1}{180}.
\]
Multiplying by the squared Gaussian prefactor and \(\epsilon^2\) yields the displayed \(t^{-3}\) coefficient and \(O(t^{-4})\) remainder, uniformly in the compact skew range. The unique minimizer of the positive limiting quadratic is \(\beta=-1/61\), an interior point. Its convergence follows from strict convexity and uniform convergence of the rescaled objectives (or of their derivatives). The optimized coefficient is \(60/61\) times the \(\beta=0\) value, while the \(\beta=1\) coefficient is \(64\) times that value.

**5. Existence of a reversal.** The numerator and denominator defining the unconstrained minimizer depend continuously on \(t>0\), and the denominator is strictly positive. Therefore \(\beta_{\mathrm{opt}}(t)\) is continuous. Its two opposite-sign limits give at least one finite-time zero by the intermediate value theorem. No monotonicity or uniqueness of that zero is needed or claimed.

## Verification

Run `python verify.py` with Python 3 and `mpmath`. The checker compares the positive-halfline skew transition density integrated in space against the Gaussian-CDF formulas; reconstructs the annealed–quenched difference independently from Bernoulli variances; verifies the exact rational covariance polynomial with `fractions.Fraction`; tests finite-time positivity and optimization; and checks the large-time coefficient for three skew parameters. The checked computations are finite diagnostics only. The proof above establishes all universal and asymptotic claims.

## Relationship to prior work

Biswas, Jose, Pal and Ramola (arXiv:2404.13988, first posted 22 April 2024) derive the general annealed and quenched generating functions and study the two endpoint geometries: a reflecting boundary or two open boundaries, including leading \(t^{-1/2}\) convergence of both variances. Their Eq. (13) and Eq. (21) imply the general variance-of-conditional-escape-probability identity. Here that identity is **not** claimed as new. The new analysis selects the scale-invariant continuous skew-Brownian family, derives the strict exact variance-gap and its full \(t^{-3}\) coefficient, and proves a unique optimal bias with opposite short- and long-time limits. For the skew-Brownian transition kernel see Lejay's review and Gairat–Shcherbakov. Bressloff (arXiv:2211.12460) studies a distinct finite-permeability snapping-out Brownian interface, including asymmetric directions; it does not imply the claimed optimum for the scale-invariant skew junction.

## Limitations

The result is only for **independent** finite-number particles, exact uniform initial positions, constant diffusivity, a single fixed skew point at one end, and one-time outside-count variances. It does not treat absorbing/reflecting **walls at both ends**, cumulative first-exit counts, interacting particles, a finite-permeability semipermeable membrane, or statistically noisy estimation. No uniqueness of the crossing time is proved. The kernel and general annealed–quenched decomposition are established literature; originality is claimed solely for the exact skew-family optimization and its sharp asymptotics. Independent literature-priority review has not been performed.

## References

1. A. Biswas, S. Jose, A. Pal and K. Ramola, *Current fluctuations in finite-sized one-dimensional non-interacting passive and active systems*, arXiv:2404.13988v1 (22 April 2024), https://arxiv.org/html/2404.13988v1 .
2. A. Lejay, *On the constructions of the skew Brownian motion*, Probability Surveys 3 (2006), 413–466, doi:10.1214/154957807000000013.
3. A. Gairat and V. Shcherbakov, *Density of skew Brownian motion and its functionals with application in finance*, Mathematical Finance 27 (2017), 1069–1088, arXiv:1407.1715, https://arxiv.org/abs/1407.1715 .
4. P. C. Bressloff, *Renewal equations for single-particle diffusion through a semipermeable interface*, arXiv:2211.12460v1 (22 November 2022), https://arxiv.org/html/2211.12460v1 .
