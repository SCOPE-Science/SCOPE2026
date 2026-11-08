# Seasonal synergy depresses cooperation with an exact frequency resonance

## Finding

Consider the four-player nonlinear public-goods game with adaptive cooperator reward defined below. Let the exogenous synergy vary as \(w(t)=1+\delta\cos(\omega t)\). For every fixed environmental-feedback speed \(\varepsilon>4/9\) and frequency \(\omega>0\), there is \(\delta_0(\varepsilon,\omega)>0\) such that for \(|\delta|<\delta_0\) the system has exactly one periodic solution near \((x,r)=(2/3,2)\). It has period \(2\pi/\omega\), is locally attracting, and stays strictly inside the physical state rectangle.

The mean cooperation on this solution is

\[
\overline x(\delta,\omega,\varepsilon)=\frac23-
\frac{256\omega^2(3\varepsilon+4)}
{9\bigl[(9\varepsilon-48\omega^2)^2+(18\varepsilon-8)^2\omega^2\bigr]}\,\delta^2+O_{\varepsilon,\omega}(\delta^4).
\]

The coefficient is **strictly negative at every positive frequency**. The largest leading-order reduction of mean cooperation occurs at the unique frequency

\[
\omega_*(\varepsilon)=\frac{\sqrt{3\varepsilon}}4,
\qquad
\mathcal K(\omega_*,\varepsilon)=-\frac{64(3\varepsilon+4)}{9(9\varepsilon-4)^2}.
\]

For \(\varepsilon=1\), this is \(\omega_*=\sqrt3/4\) and the exact leading mean reduction equals \(448\delta^2/225\). This is an asymptotic statement as \(\delta\to0\) with \(\varepsilon\) and \(\omega\) fixed, not a finite-amplitude global optimum.

## Assumptions and scope

We use the nonlinear public-goods payoff and adaptive reward equations of Jiang et al., with group size \(N=4\), cooperator contribution \(c=1\), defector multiplier \(r_d=1\), cooperator reward bounds \(\alpha=3/2\), \(\beta=7/2\), and payoff feedback ratio \(\theta=2\). The state \(x(t)\) is the cooperator fraction and \(r(t)\) the cooperator multiplier. The physical region is \(0\le x\le1\), \(3/2\le r\le7/2\), and \(\varepsilon>0\) is the ratio of reward to strategy response speeds. The positive exogenous synergy \(w(t)=1+\delta\cos(\omega t)\) has amplitude \(|\delta|<1\).

For these parameters the exact population payoffs, including the removable \(w=1\) singularity in the source formula, are

\[
f_d(x,w)=\frac{3x+3(w-1)x^2+(w-1)^2x^3}{4},
\]
\[
f_c(x,r,w)=\frac r4\{1+3wx+3w(w-1)x^2+w(w-1)^2x^3\}-1.
\]

The vector field \(\dot z=F(z,w(t))\), \(z=(x,r)^\mathsf T\), is

\[
F(z,w)=\begin{pmatrix}
x(1-x)(f_c-f_d)\\
\varepsilon(r-3/2)(7/2-r)[-xf_c+2(1-x)f_d]
\end{pmatrix}.
\]

The result concerns only the locally attracting forced response near the interior equilibrium; other attractors may exist elsewhere in the state rectangle. No uniform claim is made as \(\varepsilon\downarrow4/9\), \(\omega\downarrow0\), or \(|\delta|\) becomes large.

## Proof

**Step 1 (unforced stability and periodic continuation).** At \(w=1\), \(z_*=(2/3,2)^\mathsf T\) satisfies \(F(z_*,1)=0\). Its Jacobian and the forcing derivative are

\[
J=\begin{pmatrix}1/6&1/6\\-3\varepsilon/2&-3\varepsilon/8\end{pmatrix},\qquad
g=F_w(z_*,1)=\begin{pmatrix}8/27\\-2\varepsilon/3\end{pmatrix}.
\]

The trace is \((4-9\varepsilon)/24\) and the determinant is \(3\varepsilon/16\). Hence \(J\) is Hurwitz precisely when \(\varepsilon>4/9\). The time-\(T\) map, \(T=2\pi/\omega\), is real analytic in the initial state and \(\delta\). At \(\delta=0\), the derivative of its fixed-point equation is \(e^{TJ}-I\), which is invertible because all eigenvalues of \(e^{TJ}\) have modulus below one. The implicit-function theorem therefore supplies one real-analytic \(T\)-periodic solution in a neighborhood of \(z_*\); continuity of its Floquet multipliers proves local attraction. Smallness of \(|\delta|\) keeps this solution in the interior.

**Step 2 (first Fourier mode).** Expand the periodic solution for fixed positive \(\varepsilon\) and \(\omega\):

\[
z(t)=z_*+\delta u(t)+\delta^2v(t)+O(\delta^3).
\]

With \(u(t)=\operatorname{Re}(h e^{i\omega t})\), the linear equation \(\dot u=Ju+g\cos(\omega t)\) gives

\[
h=(i\omega I-J)^{-1}g
=\frac1{q}\begin{pmatrix}128i\omega/9\\-16\varepsilon(1+2i\omega)\end{pmatrix},\quad
q=9\varepsilon-48\omega^2+i(18\varepsilon-8)\omega.
\]

Because \(J\) is Hurwitz, \(q\ne0\) for every real positive \(\omega\).

**Step 3 (second-order average).** Write \(H^{(k)}=F^{(k)}_{zz}(z_*,1)\), \(C=F_{zw}(z_*,1)\) and \(d=F_{ww}(z_*,1)\). Direct differentiation of the exact payoffs gives

\[
H^{(1)}=\begin{pmatrix}-1/2&-1/12\\-1/12&0\end{pmatrix},\quad
H^{(2)}=\varepsilon\begin{pmatrix}-9/2&-47/16\\-47/16&-1\end{pmatrix},
\]
\[
C=\begin{pmatrix}1/9&5/27\\-3\varepsilon&-47\varepsilon/36\end{pmatrix},\qquad
d=\begin{pmatrix}80/243\\-20\varepsilon/27\end{pmatrix}.
\]

At order \(\delta^2\), the equation is

\[
\dot v=Jv+\frac12 F_{zz}[u,u]+F_{zw}u\cos(\omega t)+\frac12F_{ww}\cos^2(\omega t).
\]

For a full-period average \(\langle\cdot\rangle\), \(\langle u_i u_j\rangle=\frac12\operatorname{Re}(h_i\overline h_j)\), \(\langle u_i\cos\omega t\rangle=\frac12\operatorname{Re}h_i\), and \(\langle\cos^2\omega t\rangle=1/2\). Thus

\[
\langle v\rangle=-J^{-1}Q,\quad
Q_k=\frac14\sum_{i,j}H^{(k)}_{ij}\operatorname{Re}(h_i\overline h_j)
+\frac12\sum_i C_{ki}\operatorname{Re}h_i+\frac14d_k.
\]

Using the displayed exact derivatives and \(|q|^2=(9\varepsilon-48\omega^2)^2+(18\varepsilon-8)^2\omega^2\), direct rational simplification yields

\[
\langle v_x\rangle=-\frac{256\omega^2(3\varepsilon+4)}{9|q|^2}.
\]

The included standalone `verify.py` recomputes all derivatives and this identity using exact symbolic arithmetic. The mean of the first-order mode is zero. Replacing \(\delta\) by \(-\delta\) shifts the forcing by half a period, so uniqueness of the nearby periodic solution implies its time average is an even analytic function of \(\delta\). This improves the remainder after the quadratic term to \(O(\delta^4)\).

**Step 4 (sign and exact optimal frequency).** For \(\omega>0\) and \(\varepsilon>4/9\), \(|q|^2>0\) and \(3\varepsilon+4>0\), establishing a strict negative coefficient. Put \(s=\omega^2\). Its magnitude is a positive constant times

\[
\frac{s}{2304s^2+(324\varepsilon^2-1152\varepsilon+64)s+81\varepsilon^2}.
\]

The derivative has the sign of \(81\varepsilon^2-2304s^2\). Hence the unique global maximum over \(s>0\) is at \(s=3\varepsilon/16\); substitution yields the stated peak coefficient. The magnitude goes to zero both as \(\omega\downarrow0\) and \(\omega\to\infty\).

## Verification

Run `python verify.py` with Python 3 and SymPy. It verifies the equilibrium, Jacobian, forcing derivative, Fourier response, second-order mean, and sharp maximizer by exact polynomial identities, printing `VERIFY_OK`. An independent numerical period-map computation using adaptive ODE integration and quadrature also converged to the coefficient under amplitude halving, for example at \(\varepsilon=1\), \(\omega=\sqrt3/4\), yielding estimated coefficients \(-1.99888413\) at \(\delta=0.01\) and \(-1.99305173\) at \(\delta=0.005\), approaching the exact \(-448/225\approx-1.99111111\). Such numerical tests are diagnostic, not the proof of periodic existence or of the infinitesimal response formula.

## Relationship to prior work

Jiang et al. [1,2] introduce the precise nonlinear payoffs and two-way adaptive reward, calculate interior fixed-point stability thresholds, and numerically display cooperation–environment cycles under periodic global variations. The source's parameters \(N=4\), \(\alpha=1.5\), \(\beta=3.5\), \(\theta=2\), and \(r_d=1\) motivate the present continuous-speed family. Its published results do not provide the signed second-order **time-averaged** cooperation response for a small sinusoidal modulation or its exact frequency optimizer.

Liu, Cao and Wu [3] establish a mean-cooperation identity for autonomous nonlinear-imitation eco-evolutionary cycles. Their environmental coordinate satisfies a different state-only feedback law, and their cycles are unforced; their mean identity does not imply a vanishing or positive correction in the periodically driven reward model here. This paper neither claims discovery of forced oscillations nor a general theorem for every payoff parameterization.

## Limitations

The result is local to the branch issued from \((2/3,2)\), and is a small-amplitude asymptotic; it does not establish global attraction, finite-amplitude mean-sign rigidity, uniformity near the Hopf threshold, or generic sign under different payoff parameters. The full journal S2 supporting appendix could not be inspected through the available DOI route; its published description concerns numerical continuous forcing and four-segment forcing, but inaccessible supplementary content leaves residual literature-priority risk. Other unindexed equivalent perturbative results may exist. No independent external validation is asserted.

## References

1. Y. Jiang, X. Wang, L. Liu, M. Wei, J. Zhao, Z. Zheng and S. Tang, *Nonlinear eco-evolutionary games with global environmental fluctuations and local environmental feedbacks*, arXiv:2212.06497v1, first posted 2022-12-13. https://arxiv.org/abs/2212.06497
2. Y. Jiang et al., same-titled peer-reviewed version, *PLOS Computational Biology* 19 (2023), e1011269. https://doi.org/10.1371/journal.pcbi.1011269
3. Y. Liu, L. Cao and B. Wu, *General non-linear imitation leads to limit cycles in eco-evolutionary dynamics*, arXiv:2210.10552v1 (2022). https://arxiv.org/abs/2210.10552
