# Exact covariance phase locking and stroboscopic weak-order recovery for a drift-preserving oscillator integrator

## Finding

The drift-preserving stochastic Hamiltonian integrator of Chen, Cohen, D'Ambrosio and Lang, when applied to a harmonic oscillator with additive momentum noise, has an exact finite-step covariance formula. Its noise covariance becomes isotropic at an explicit, exhaustive set of phase-locked stepsizes, despite the method preserving the expected energy trace at *all* stepsizes. At fixed terminal time, its centered covariance error has a nonzero first-order limit except at integer half-periods of the physical oscillator, where the order increases sharply to two and the leading second-order covariance tensor is explicit. At a fixed number of steps tending to the large-stepsize regime, the normalized numerical covariance becomes rank one while the exact normalized covariance becomes isotropic.

Precisely, let \(\omega,\sigma,h>0\), \(N\ge 1\), and let the deterministic initial state be \((q_0,p_0)\). In normalized coordinates \(z=(\omega q,p)^\mathsf{T}\), write \(\theta=2\arctan(\omega h/2)\). For the numerical state covariance \(C_N\),

\[
C_N=\frac{\sigma^2h}{2}\begin{pmatrix}N-c_N&s_N\\s_N&N+c_N\end{pmatrix},\qquad
c_N+\mathrm{i}s_N=\sum_{j=1}^{N}e^{2\mathrm{i}j\theta}
=e^{\mathrm{i}(N+1)\theta}\frac{\sin(N\theta)}{\sin\theta}.
\]

Its two eigenvalues are
\[
\lambda_\pm(C_N)=\frac{\sigma^2h}{2}\left(N\pm\left|\frac{\sin(N\theta)}{\sin\theta}\right|\right),
\qquad \operatorname{tr}C_N=\sigma^2Nh.
\]
For \(N\ge2\), \(C_N\) is a scalar multiple of the identity **if and only if**
\[
h=\frac2\omega\tan\left(\frac{m\pi}{2N}\right),\qquad m=1,\ldots,N-1.
\]
There is no positive isotropizing stepsize for \(N=1\). The exact expected Hamiltonian energy nevertheless obeys the correct trace law for every \(h>0\):
\[
\mathbb E H(q_N,p_N)=H(q_0,p_0)+\frac{\sigma^2Nh}{2},\qquad
H(q,p)=\frac{p^2+\omega^2q^2}{2}.
\]

For any fixed physical time \(T>0\), use \(h=T/N\) and let \(C(T)\) be the exact state covariance at time \(T\). Define
\[
f_\omega(t)=\begin{pmatrix}\sin^2(\omega t)&\sin(\omega t)\cos(\omega t)\\\sin(\omega t)\cos(\omega t)&\cos^2(\omega t)\end{pmatrix}.
\]
Then
\[
\lim_{N\to\infty}\frac{C_N-C(T)}h
=\frac{\sigma^2}{2}\bigl(f_\omega(T)-f_\omega(0)\bigr),
\quad
\left\|\frac{\sigma^2}{2}\bigl(f_\omega(T)-f_\omega(0)\bigr)\right\|_2
=\frac{\sigma^2}{2}|\sin(\omega T)|.
\]
Thus the centered covariance error is sharply of first order exactly when \(\omega T\notin\pi\mathbb Z\). If \(\omega T=m\pi\) for any positive integer \(m\), then
\[
\lim_{N\to\infty}\frac{C_N-C(T)}{h^2}
=\frac{\sigma^2\omega^2T}{24}\begin{pmatrix}1&0\\0&-1\end{pmatrix}\ne0.
\]
At these half-periods, all polynomial test observables in \((q,p)\) of degree at most two have weak error \(O(h^2)\); the centered covariance convergence is genuinely second order. For deterministic \(z_0=0\), the quadratic observable \(G(q,p)=\omega^2q^2\) exhibits the displayed nonzero second-order constant.

Finally, for fixed \(N\ge1\) and \(h\to\infty\), with \(T=Nh\),
\[
\frac{C_N}{\sigma^2Nh}\longrightarrow\begin{pmatrix}0&0\\0&1\end{pmatrix},\qquad
\frac{C(T)}{\sigma^2Nh}\longrightarrow\frac{I_2}{2},\qquad
\left\|\frac{C_N-C(T)}{\sigma^2Nh}\right\|_2\longrightarrow\frac12.
\]

## Assumptions and scope

The scalar Brownian-driven Itô oscillator is
\[
\mathrm dq(t)=p(t)\,\mathrm dt,\qquad
\mathrm dp(t)=-\omega^2q(t)\,\mathrm dt+\sigma\,\mathrm dW(t),
\]
with fixed \(\omega>0\), \(\sigma>0\), deterministic \((q_0,p_0)\in\mathbb R^2\), and independent centered Wiener increments of variance \(h\). The Chen--Cohen--D'Ambrosio--Lang drift-preserving update is defined by
\[
\Psi_{k+1}=p_k+\sigma\Delta W_k-
\frac{h\omega^2}{2}\left(q_k+\frac h2\Psi_{k+1}\right),\quad
q_{k+1}=q_k+h\Psi_{k+1},\quad
p_{k+1}=p_k+\sigma\Delta W_k-h\omega^2\left(q_k+\frac h2\Psi_{k+1}\right).
\]
This is the exact specialization of the published integral formula to the quadratic potential, which is unconditionally uniquely solvable for all \(h>0\). Here covariance refers to randomness from the noise with the initial state held deterministic; the covariance formula is independent of the initial state. Physical half-periods are those for which \(\omega T\in\pi\mathbb Z\), not arbitrary numerical phase-locked stepsizes.

## Proof

**1. The numerical Cayley rotation.** Write
\[
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad e_2=\begin{pmatrix}0\\1\end{pmatrix},\quad R_\alpha=e^{\alpha J}=\begin{pmatrix}\cos\alpha&\sin\alpha\\-\sin\alpha&\cos\alpha\end{pmatrix}.
\]
Solving the displayed implicit update and using \(z_k=(\omega q_k,p_k)^\mathsf T\) gives exactly
\[
z_{k+1}=R_\theta\bigl(z_k+\sigma e_2\Delta W_k\bigr),\quad
\cos\theta=\frac{1-(\omega h/2)^2}{1+(\omega h/2)^2},\quad
\sin\theta=\frac{\omega h}{1+(\omega h/2)^2}.
\]
The resulting rotation is orthogonal, so \(\mathbb E\|z_{k+1}\|^2=\mathbb E\|z_k\|^2+\sigma^2h\). This proves the expected-energy identity at every step.

**2. Covariance and its spectrum.** Independent centered increments give
\[
C_N=\sigma^2h\sum_{j=1}^N R_{j\theta}e_2e_2^\mathsf TR_{j\theta}^\mathsf T.
\]
Since \(R_{j\theta}e_2=(\sin j\theta,\cos j\theta)^\mathsf T\), the double-angle identities yield the explicit covariance matrix and \(\operatorname{tr}C_N=\sigma^2Nh\). Its traceless part has squared eigenvalue \((\sigma^2h/2)^2(c_N^2+s_N^2)\). For \(0<\theta<\pi\), the finite geometric-series identity yields the stated expression for \(c_N+\mathrm is_N\), hence \(|c_N+\mathrm is_N|=|\sin(N\theta)/\sin\theta|\). The covariance is isotropic exactly when \(\sin(N\theta)=0\). Because \(\theta\in(0,\pi)\), the only possibilities are \(\theta=m\pi/N\) with \(1\le m\le N-1\); solving for \(h\) gives the claimed complete list.

**3. Exact covariance and the generic first-order coefficient.** The exact propagator is \(R_{\omega t}\), so stochastic convolution gives
\[
C(T)=\sigma^2\int_0^Tf_\omega(t)\,\mathrm dt
=\sigma^2\begin{pmatrix}
T/2-\sin(2\omega T)/(4\omega)&(1-\cos(2\omega T))/(4\omega)\\
(1-\cos(2\omega T))/(4\omega)&T/2+\sin(2\omega T)/(4\omega)
\end{pmatrix}.
\]
Set \(\omega_h=\theta/h\). For \(h=T/N\), the numerical covariance is the right-endpoint rule \(C_N=\sigma^2h\sum_{j=1}^N f_{\omega_h}(jh)\). Taylor expansion of arctangent gives \(\omega_h=\omega-\omega^3h^2/12+O(h^4)\). The classical smooth right-endpoint quadrature expansion, uniform for \(\omega_h\) in a neighborhood of \(\omega\), therefore gives
\[
C_N-C(T)=\frac{\sigma^2h}{2}\bigl(f_\omega(T)-f_\omega(0)\bigr)+O(h^2).
\]
The difference of the two unit-rank orthogonal projectors \(f_\omega(T)\) and \(f_\omega(0)\) has eigenvalues \(\pm|\sin(\omega T)|\). This gives the exact first-order norm and its vanishing condition.

**4. The sharp stroboscopic coefficient.** At \(\omega T=m\pi\), both \(f_\omega(T)=f_\omega(0)\) and \(\partial_tf_\omega(T)=\partial_tf_\omega(0)\). The Euler--Maclaurin expansion
\[
h\sum_{j=1}^Nf_{\omega_h}(jh)=\int_0^Tf_{\omega_h}(t)\,\mathrm dt+\frac h2(f_{\omega_h}(T)-f_{\omega_h}(0))
+\frac{h^2}{12}(\partial_tf_{\omega_h}(T)-\partial_tf_{\omega_h}(0))+O(h^4)
\]
has no first- or second-order boundary contribution at the limiting physical frequency. Because \(\omega_h-\omega=O(h^2)\), the remaining boundary terms are \(O(h^3)\) or smaller. Differentiating the exact covariance integral at the fixed time \(T=m\pi/\omega\) shows
\[
\left.\partial_\nu\int_0^T f_\nu(t)\,\mathrm dt\right|_{\nu=\omega}
=\frac{T}{2\omega}\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
\]
Multiplying by the frequency shift \(-\omega^3h^2/12\) proves the stated nonzero second-order tensor. The numerical mean is \(R_{N\theta}z_0\) and the true mean is \(R_{\omega T}z_0\). Since \(N\theta=\omega T-\omega^3Th^2/12+O(h^4)\), their difference is \(O(h^2)\). Every polynomial of degree at most two depends only on the first two moments, so its weak error is \(O(h^2)\) at physical half-periods.

**5. Large-step anisotropy.** At fixed \(N\), \(h\to\infty\) implies \(\theta\to\pi\). Every summand in the numerical covariance formula, normalized by \(\sigma^2Nh\), tends to \(e_2e_2^\mathsf T/N\). The exact covariance formula gives \(C(T)/(\sigma^2T)\to I_2/2\) as \(T=Nh\to\infty\). The operator-norm limit is \(\|\operatorname{diag}(-1/2,1/2)\|_2=1/2\).

## Verification

Run `python3 verify.py` using only the Python standard library. The supplied `verification_output.txt` records `VERIFY_OK checks=1042`. Exact-rational tests recompute the Cayley map, noise covariance recurrence, explicit sine-sum covariance, spectral gap, and exact isotropy for seven rational stepsizes and \(1\le N\le20\). Separate numerical convergence tests at \(T=1\), \(T=\pi\), and at a large fixed-\(N\) step check the derived limiting constants. These checks complement, rather than replace, the analytic arguments above; finite tests do not certify the universal quantifiers.

## Relationship to prior work

Chen, Cohen, D'Ambrosio and Lang (2019/2020) introduced the drift-preserving method, proved exact energy-trace preservation and general weak order one, and numerically tested first- and second-moment errors at \(T=1\) for a linear oscillator. Neither their trace theorem nor their generic weak-order estimate gives the finite-step isotropy classification, the sharp time-dependent leading covariance error tensor, the half-period order-two recovery, or the large-step rank-one limit. The current theorem is a specialized analysis of their existing integrator, not a new integration algorithm.

Strømmen Melbø and Higham (2004) analyze energy growth and oscillations for other stochastic-oscillator discretizations. Senosiain and Tocino (2014/2015) derive trigonometric moment sums for partitioned Euler--Maruyama and discuss scalar second-moment growth, rather than this method's normalized covariance phase locking and half-period weak-error transition. Hong, Scherer and Wang (2006) treat a stochastic midpoint rule on the same physical oscillator; its full manuscript was not obtainable during the comparison. Its potentially relevant detailed covariance analysis therefore remains an explicit precedence risk, and no assertion of noncoverage of that inaccessible full text is made. The subject also borders on stochastic-trigonometric integration and time-dependent superconvergence theory; a broader literature may contain related implications.

## Limitations

The findings require a scalar, undamped, constant-frequency harmonic oscillator, additive scalar Brownian momentum noise, deterministic initial state, and the precise published drift-preserving update. Exact finite-step isotropy is a property of the **numerical covariance**, not equality to the exact covariance at the corresponding physical time. The stroboscopic weak-order statement covers polynomial observables of degree at most two; it is not a general weak-order-two theorem for all smooth observables or nonlinear potentials. The large-step limit fixes the number of steps while increasing physical terminal time. There is no claim of independent scientific review, an exhaustive historical novelty search, or validity for other integrators without a fresh proof.

## References

1. C. Chen, D. Cohen, R. D'Ambrosio, A. Lang, *Drift-preserving numerical integrators for stochastic Hamiltonian systems*, initial public preprint 2019-07-20, arXiv:1907.08804, https://arxiv.org/abs/1907.08804; *Advances in Computational Mathematics* 46, 27 (2020), https://doi.org/10.1007/s10444-020-09771-5.
2. A. H. Strømmen Melbø, D. J. Higham, *Numerical simulation of a linear stochastic oscillator with additive noise*, *Applied Numerical Mathematics* 51 (2004), 89–99, https://doi.org/10.1016/j.apnum.2004.02.003; accessible manuscript https://strathprints.strath.ac.uk/164/.
3. M. J. Senosiain, A. Tocino, *A review on numerical schemes for solving a linear stochastic oscillator*, *BIT Numerical Mathematics* 55 (2015), 515–529, first online 2014-07-18, https://doi.org/10.1007/s10543-014-0507-z (accessible abstract and appendix).
4. J. Hong, R. Scherer, L. Wang, *Midpoint rule for a linear stochastic oscillator with additive noise*, *Neural, Parallel and Scientific Computations* 14 (2006), 1–12, https://www.researchgate.net/publication/265336686_Midpoint_Rule_for_a_Linear_Stochastic_Oscillator_with_Additive_Noise (abstract accessible; full text unavailable).
