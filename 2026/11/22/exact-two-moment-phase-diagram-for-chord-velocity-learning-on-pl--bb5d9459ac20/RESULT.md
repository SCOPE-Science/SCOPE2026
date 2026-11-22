# Exact two-moment phase diagram for chord-velocity learning on planar rotations

## Finding

Consider a planar rotation sampled once every \(h>0\). A linear velocity field is fitted to a chord interpolant at a random offset. The **entire population optimum, minimum residual, false damping or growth, sub-Nyquist frequency fold, and small-step order** are determined by only the first two moments of the offset law.

Write \(J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\), \(R_\theta=\cos\theta\,I+\sin\theta\,J\), with \(0<\theta<\pi\), and let the independent random offset \(S\in[0,1]\) have \(\mu=\mathbb E S\), \(v=\operatorname{Var} S\), and
\[
q=\mathbb E[S(1-S)]=\mu(1-\mu)-v,\qquad D=1-2q(1-\cos\theta).
\]
For a uniform phase \(x\) on the circle of radius \(r>0\), fit **all** real \(2\times2\) matrices \(B\) by minimizing the exact, unregularized population loss
\[
\mathcal L_h(B)=\mathbb E_{x,S}\left\|B\big((1-S)x+S R_\theta x\big)-\frac{R_\theta x-x}{h}\right\|^2.
\]
The minimizer is unique and is
\[
\boxed{B_*=\frac{(1-2\mu)(\cos\theta-1)I+\sin\theta\,J}{hD}},
\qquad
\boxed{\min_B\mathcal L_h(B)=\frac{4r^2v(1-\cos\theta)^2}{h^2D}}.
\]
In particular, the learned flow is exactly conservative (skew-symmetric generator) if and only if \(\mu=1/2\); offset means below or above \(1/2\) respectively create spurious radial damping or growth. A zero training residual occurs exactly for a deterministic offset, not necessarily for a faithful generator.

The learned angular frequency is \(\widehat\omega_h(\theta)=\sin\theta/(hD)\). For \(q<1/4\) it has a **unique maximum** at
\[
\boxed{\theta_q=\arccos\left(-\frac{2q}{1-2q}\right)},\qquad \pi/2\le\theta_q<\pi,
\]
and strictly decreases on \((\theta_q,\pi)\), despite all angles being below the Nyquist angle \(\pi\). For \(q=1/4\), necessarily \(S=1/2\) almost surely; then \(\widehat\omega_h=2\tan(\theta/2)/h\), strictly increasing and unbounded as \(\theta\uparrow\pi\).

For true frequency \(\omega>0\) and \(\theta=\omega h\to0\), the **full learned generator** satisfies \(B_*-\omega J=O(h^4)\) if and only if
\[
\boxed{\mu=\tfrac12,\quad v=\tfrac1{12}}.
\]
Then
\[
B_*=\left(\omega-\frac{\omega^5h^4}{180}+O(h^6)\right)J,
\qquad \min_B\mathcal L_h(B)=\frac{r^2\omega^4h^2}{12}+O(h^4).
\]
Thus fourth-order recovery can coexist with a positive second-order training residual. Moreover every fourth-order offset distribution has \(q=1/6\), hence the same frequency fold \(\theta_q=2\pi/3\). This combination of exact loss, generator order and unavoidable fold is the assessed result; the known fourth-order compact-difference frequency symbol appearing in the uniform-offset special case is **not** asserted to be new.

## Assumptions and scope

The noiseless observations satisfy \(x_1=R_\theta x_0\), independently of the offset. The phase of \(x_0\) is uniformly distributed and its radius is fixed at \(r>0\); independent isotropic initial data with \(\mathbb E[xx^\top]=(r^2/2)I\) also suffice. The offset can be continuous, discrete, degenerate, or asymmetric, but is supported on \([0,1]\) and independent of the phase. The loss is a population expectation, not an empirical finite-sample loss. Matrices \(B\) are unrestricted and time-independent. The true continuous generator is \(\omega J\) when \(\theta=\omega h\); the sampling restriction \(0<\theta<\pi\) removes integer aliasing and the singular midpoint endpoint \(\theta=\pi\).

Because \(0\le q\le1/4\), \(D>0\) on this open angular interval, including at deterministic midpoint offsets. Neither the field-fitting result nor the phase diagram asserts global accuracy for nonlinear systems or noisy observations.

## Proof

Put \(c=\cos\theta\), \(s=\sin\theta\), \(K_S=(1-S)I+S R_\theta\), and \(C=(R_\theta-I)/h\). Since \(R_\theta R_\theta^\top=I\) and \(J^\top=-J\), straightforward multiplication gives
\[
K_SK_S^\top=\big(1-2S(1-S)(1-c)\big)I,
\]
so, by isotropy and independence,
\[
\mathbb E[(K_Sx)(K_Sx)^\top]=\frac{r^2D}{2}I.
\]
Similarly,
\[
\mathbb E[(Cx)(K_Sx)^\top]
=\frac{r^2}{2}\,C\,\mathbb E K_S^\top
=\frac{r^2}{2h}\big((1-2\mu)(c-1)I+sJ\big).
\]
The normal equations of unconstrained matrix least squares give the displayed unique \(B_*\), because the feature covariance is positive definite for \(0<\theta<\pi\). The exact target energy is \(\mathbb E\|Cx\|^2=2r^2(1-c)/h^2\). Subtracting the explained energy yields
\[
\mathcal L_h(B_*)=\frac{r^2}{h^2}\left[2(1-c)-\frac{(1-2\mu)^2(1-c)^2+s^2}{D}\right].
\]
The identity
\[
2(1-c)D-\big((1-2\mu)^2(1-c)^2+s^2\big)=4v(1-c)^2
\]
follows on substituting \(s^2=1-c^2\) and \(q=\mu(1-\mu)-v\). This proves the minimum risk. Since \(1-c>0\), its vanishing is equivalent to \(v=0\). Since \((1-2\mu)(c-1)\) is the symmetric coefficient of \(B_*\), skew-symmetry is equivalent to \(\mu=1/2\), with the stated sign of the radial coefficient.

Differentiation of the angular coefficient gives the exact sign identity
\[
\frac{d}{d\theta}\big(h\widehat\omega_h(\theta)\big)
=\frac{(1-2q)\cos\theta+2q}{D^2}.
\]
For \(0\le q<1/4\), the numerator strictly decreases from \(1\) to \(4q-1<0\), so it has precisely one zero, yielding the claimed fold and its monotonicity intervals. If \(q=1/4\), equality in \(\mathbb E S(1-S)\le1/4\) forces \(S=1/2\) almost surely. Substitution gives the tangent formula, which is strictly increasing on \((0,\pi)\).

Finally, Taylor series at \(\theta=\omega h\) yield
\[
\frac{(1-2\mu)(\cos\theta-1)}{hD}=(\mu-\tfrac12)\omega^2h+O(h^3),
\]
\[
\widehat\omega_h=\omega+(q-\tfrac16)\omega^3h^2
+\left(q^2-\tfrac14q+\tfrac1{120}\right)\omega^5h^4+O(h^6).
\]
Because \(\omega>0\), fourth-order convergence of the **whole matrix** forces both \(\mu=1/2\) and \(q=1/6\). Conversely those conditions suffice, and they are equivalent to \(\mu=1/2,v=1/12\). Substituting gives coefficient \(-1/180\), and the risk formula gives the residual expansion. At \(q=1/6\), the fold is \(2\pi/3\). This proves the entire statement.

## Verification

`verify.py` uses Python 3 and only the standard library. It checks exact-rational regression normal equations and risks for 55 discrete offset laws, seven rationally parameterized rotation angles and three rational steps; it additionally checks the derivative and fold phases on dense angle grids. It confirms the fourth-order coefficient, the midpoint formula and the uniform-moment fold. Execute `python3 verify.py` in the directory containing the extracted script. The finite checks are diagnostics, **not substitutes for the algebraic proof**. The continuous uniform law \(S\sim\operatorname{Uniform}[0,1]\) has moments \(\mu=1/2,v=1/12\); the unequal-to-uniform three-point law with masses \(1/6,2/3,1/6\) on \(0,1/2,1\) has the same moments, hence the same optimum and risk exactly.

## Relationship to prior work

Farenga and Manzoni (2026), sections 4.1–4.4 and Appendix C, introduce piecewise-linear velocity matching, its uniform stochastic collocation, its general bias–variance decomposition and its relation to an implicit average-vector-field residual. Those constructions and general insights are prior. The precise all-matrix population optimizer for a planar rotation under arbitrary offset laws, the minimum loss and its exact mean–variance constraints, and the joint fourth-order/aliasing classification are the additional statements investigated here.

Lele (1992), sections 2.1 and 3.1, already studies the classical fourth-order compact Padé first derivative and its modified wavenumber. As Li, Li and Liao (2023), equation (2.3), also writes, the symbol is \(3\sin\theta/(2+\cos\theta)\). Hence **the uniform-offset frequency formula, its fourth-order expansion and the fold obtainable directly from that formula are algebraically covered as a compact-differencing symbol**. They are not independently claimed as discoveries; the content here is their precise characterization as part of a full statistical regression/risk and arbitrary-collocation moment theorem.

Lu and Tsai (2025/2026), sections 1–3, analyze biased dynamics learned through a numerical-integrator rollout objective and advocate implicit midpoint for conservative dynamics. That objective is different from least-squares chord velocity matching at random offsets, even though its midpoint stability function is relevant to the deterministic-middle special case. The distinction is between rollout-based identification and the exact off-trajectory interpolation loss studied here.

## Limitations

The law of the offset matters here only through its first two moments because the learned field is linear and the predictor depends affinely on the offset; this reduction need not persist in nonlinear models. The model assumes rotationally isotropic, noiseless population data; anisotropic initial distributions, finite training sets, observation noise, regularization, nonlinearity, and mixed frequencies can change the optimizer. The fold measures noninjectivity of the **imaginary part of the fitted generator**, not nonidentifiability from all possible raw data or all entries of \(B_*\). The maximum at \(2\pi/3\) for fourth-order laws is a property of this learning statistic, and the uniform-offset formula is already familiar from compact finite differencing. This result is not a claim of a novel finite-difference stencil.

## References

1. N. Farenga and A. Manzoni, *Learning to evolve by matching velocities*, arXiv:2611.00448, first made public 2026-10-30, https://arxiv.org/abs/2611.00448 . Full text sections 4.1–4.4, Appendix C.
2. S. K. Lele, *Compact finite difference schemes with spectral-like resolution*, Journal of Computational Physics 103 (1992), 16–42, https://www.math.uakron.edu/~kreider/anpde/Lele_JCP_1992.pdf . See sections 2.1 and 3.1.
3. D. Li, K. Li and W. Liao, *A combined compact finite difference scheme for solving the acoustic wave equation in heterogeneous media*, Numerical Methods for Partial Differential Equations 39 (2023), 4062–4086, https://doi.org/10.1002/num.23036 . See equation (2.3).
4. B.-Z. Lu and R. Tsai, *Artifacts of Numerical Integration in Learning Dynamical Systems*, arXiv:2507.14491, first made public 2025-07-19, https://arxiv.org/abs/2507.14491 . See sections 1–3.
