# A sharp noise-energy reversal in a stochastic three-vehicle ring

## Finding

For the quadratic stochastic port-Hamiltonian car-following model with zero velocity-alignment coefficient, increasing headway-coupling stiffness always **reduces** stationary speed variance and headway variance. Nevertheless the mean **fluctuation Hamiltonian energy** can strictly **increase**. For the smallest ring allowed by the originating model, three vehicles, the exact boundary is the dimensionless relation \(\gamma T=1\): mean energy increases at every stable stiffness when \(\gamma T>1\), is independent of stiffness when \(\gamma T=1\), and decreases when \(\gamma T<1\). The statement concerns a stationary Gaussian linear model, not collision-free car motion.

More precisely, for \(N\ge3\) and \(\gamma,T,\sigma>0\), \(\alpha\ge0\), consider the periodic-index stochastic equations
\[
\begin{aligned}
 dQ_n&=(p_{n+1}-p_n)\,dt,\\
 dp_n&=\left\{\gamma\left[\frac{Q_n-\ell}{T}-p_n\right]
          +\alpha(Q_n-Q_{n-1})\right\}\,dt+\sigma\,dW_n.
\end{aligned}
\]
Here \(\sum_{n=1}^NQ_n=L\) is constant, and \(W_n\) are independent standard Brownian motions. Write \(\bar Q=L/N\), \(g_n=Q_n-\bar Q\), \(v_*=(\bar Q-\ell)/T\), and \(y_n=p_n-v_*\). The centered energy and variances per vehicle are
\[
\mathcal H_N=\frac1{2N}\sum_{n=1}^N(y_n^2+\alpha g_n^2),\qquad
 K_N=\frac1{2N}\sum_{n=1}^N\mathbb E[y_n^2],\qquad
 G_N=\frac1N\sum_{n=1}^N\mathbb E[g_n^2].
\]
Stationary expectations in these definitions exist exactly in the stable range specified below.

For the Fourier modes \(q_j=2\pi j/N\), \(j=1,\dots,N-1\), put
\[
 d_j=\alpha+\frac{\gamma}{2T}-\frac{1+\cos q_j}{2T^2},
 \qquad C=\frac{\sigma^2}{2\gamma}.
\]
The centered process has a unique stationary Gaussian law **if and only if** every \(d_j>0\). With unitary discrete Fourier transforms \(\widehat g_j\) and \(\widehat y_j\), the exact stationary power per nonzero mode is
\[
 \mathbb E|\widehat g_j|^2=\frac{C}{d_j},\qquad
 \mathbb E|\widehat y_j|^2=C\left[1+\frac{1+\cos q_j}{2T^2d_j}\right].
\]
The zero speed mode has variance \(C\). The mode contribution to the unnormalized quadratic energy is
\[
 E_j(\alpha)=\frac C2\frac{2\alpha+\gamma/(2T)}{d_j},\qquad
 \frac{dE_j}{d\alpha}
 =\frac{C\,[\gamma T-2(1+\cos q_j)]}{4T^2d_j^2}.
\]
Thus individual modes can contribute opposite energy trends, although all nonzero headway powers and all speed powers except the Nyquist speed mode decrease with stiffness.

For the **three-vehicle ring**, set
\[
 d=\alpha+\frac\gamma{2T}-\frac1{4T^2}>0.
\]
At stationarity,
\[
 \boxed{G_3=\frac{\sigma^2}{3\gamma d}},\qquad
 \boxed{K_3=\frac{\sigma^2}{4\gamma}+\frac{\sigma^2}{24\gamma T^2d}},
\]
and
\[
 \boxed{\mathbb E\mathcal H_3
   =\frac{\sigma^2}{12\gamma}
    +\frac{\sigma^2}{6\gamma}\frac{2\alpha+\gamma/(2T)}{d}},
 \qquad
 \boxed{\frac{d}{d\alpha}\mathbb E\mathcal H_3
   =\frac{\sigma^2(\gamma T-1)}{12\gamma T^2d^2}}.
\]
The sign is sharp for all stable \(\alpha\), with equality at \(\gamma T=1\) for **every** stable stiffness. The stability restriction is \(\alpha>1/(4T^2)-\gamma/(2T)\), together with \(\alpha\ge0\).

As a rational witness, with \((N,\gamma,T,\sigma)=(3,2,1,1)\), increasing \(\alpha\) from \(0\) to \(1\) changes stationary mean energy from \(11/72\) to \(31/168\), even though mean kinetic energy decreases from \(11/72\) to \(23/168\) and mean squared headway fluctuation decreases from \(2/9\) to \(2/21\).

## Assumptions and scope

The time gap \(T\), damping \(\gamma\), and independent noise amplitude \(\sigma\) are strictly positive. The stiffness \(\alpha\) is nonnegative and the velocity-alignment coefficient is exactly zero. Vehicle indices are cyclic and the total gap \(L\) is fixed. Centering by the uniform flow eliminates the translation mode. The deterministic stability criterion and the finite stationary second moments require every \(d_j>0\). At the boundary \(d_j=0\) the corresponding forced mode is nondecaying and these stationary formulas do not apply.

These are the exact quadratic-potential, affine-optimal-velocity terms of Rüdiger–Tordeux–Ugurcan with their alignment coefficient specialized to zero; their quadratic energy of perturbations equals \(N\mathcal H_N\). The stationary law is on the affine headway hyperplane, not restricted to physically ordered or collision-avoiding configurations.

## Proof

**1. Fourier reduction and the stability boundary.** Center the equations as above and write \(g_n=x_{n+1}-x_n\), so the perturbation positions satisfy \(dx_n=y_n\,dt\). For a Fourier frequency \(q\ne0\), put \(\kappa=2(1-\cos q)\). The complex Fourier dynamics obey
\[
 dX=Y\,dt,\qquad
 dY=-a_qX\,dt-\gamma Y\,dt+\sigma\,dB_q,
 \quad a_q=\alpha\kappa+\frac\gamma T(1-e^{iq}).
\]
The characteristic polynomial is \(\lambda^2+\gamma\lambda+a_q\). At a spectral crossing of the imaginary axis, the imaginary part of \(\lambda=i\omega\) forces \(\omega=(\sin q)/T\); the real part then gives \(\kappa d_q=0\), where \(d_q=\alpha+\gamma/(2T)-(1+\cos q)/(2T^2)\). For sufficiently large \(\alpha\), both roots have strictly negative real part (their leading imaginary parts are \(\pm\sqrt{\alpha\kappa}\), and the damping correction is \(-\gamma/2\)). Continuity and the uniqueness of the crossing imply that both roots have negative real part exactly when \(d_q>0\). At the critical value an eigenvalue has zero real part; independent velocity noise excites it. The zero Fourier speed mode is a scalar Ornstein–Uhlenbeck process with decay rate \(\gamma\); its headway mode vanishes identically. Therefore a unique Gaussian invariant law exists exactly under the asserted conditions.

**2. Exact stationary complex-mode moments.** Fix \(q\ne0\), write \(U=\mathbb E|X|^2\), \(V=\mathbb E|Y|^2\), and \(Z=\mathbb E(\overline X Y)\), and set \(a_q=a_r+i a_i\). Applying the stationary Itô product identities, with the unitary Fourier-noise normalization, gives
\[
 \Re Z=0,\qquad V-a_qU-\gamma Z=0,\qquad
 2\gamma V+2\Re(a_q\overline Z)=\sigma^2.
\]
The first two equations imply \(Z=i(\sin q/T)U\) and
\[
 V=\kappa\left(\alpha+\frac\gamma{2T}\right)U.
\]
Inserting these into the third equation yields \(V=\sigma^2/(2\gamma)+(\sin^2q/T^2)U\). Since \(\sin^2q/\kappa=(1+\cos q)/2\), elimination gives
\[
 U=\frac{C}{\kappa d_q},\quad
 V=C\frac{\alpha+\gamma/(2T)}{d_q},\quad
 \mathbb E|\widehat g_q|^2=\kappa U=\frac C{d_q}.
\]
This also proves the stated expression for \(\mathbb E|\widehat y_q|^2\), since \(\alpha+\gamma/(2T)=d_q+(1+\cos q)/(2T^2)\).

**3. Hamiltonian differentiation.** The modal energy is \((V+\alpha\kappa U)/2=C[2\alpha+\gamma/(2T)]/(2d_q)\). Differentiating gives the displayed \(E_j'\), which has a numerator independent of \(\alpha\). Each nonzero gap variance is strictly decreasing, as is each speed-mode variance whenever \(1+\cos q>0\); at the Nyquist mode the speed-mode variance is constant.

**4. Three-vehicle specialization.** The two nonzero Fourier modes have \(\cos q=-1/2\), so both denominators are \(d\). The zero speed mode contributes \(C\). Parseval's identity gives
\[
 G_3=\frac{2C}{3d},\qquad
 K_3=\frac16\left[C+2C\frac{\alpha+\gamma/(2T)}d\right],\qquad
 \mathbb E\mathcal H_3=K_3+\frac\alpha2G_3.
\]
Elementary simplification yields the boxed three-vehicle formulas and their exact derivative. The derivative has the sign of \(\gamma T-1\) at every stable stiffness, proving the trichotomy. The rational witness is direct substitution. \(\square\)

## Verification

The standalone standard-library script `checks/check_stationary.py` independently builds the real five-dimensional centered three-vehicle drift, solves its complete stationary continuous-time Lyapunov system using **exact rational arithmetic** (25 linear equations), and checks the derived formulas in ten parameter combinations, including decreasing, constant, and increasing-energy regimes. It also checks the exact rational witness and the derivative-sign trichotomy. Run with `python3 checks/check_stationary.py`; it prints a `PASS` line when all assertions succeed. The matrix method is independent of the Fourier derivation. This computation validates selected finite exact instances, not the general \(N\)-vehicle theorem, whose proof is analytic.

## Relationship to prior work

Rüdiger, Tordeux and Ugurcan, *Stability analysis of a stochastic port-Hamiltonian car-following model*, arXiv:2212.05139 (first posted December 9, 2022), define the same quadratic-potential model, derive stability and Gaussian convergence, and give a covariance-integral representation. Their Section 4 reports decreased simulated Hamiltonian energy as the coupling grows for one model-parameter choice. The present theorem does **not** claim a new stochastic process or a new Gaussian existence result: it evaluates the stationary modes and classifies the energy response exactly, revealing an opposing regime and an exact neutral surface not established in that work.

Ackermann, Ehrhardt, Kruse and Tordeux, *Modelling car-following dynamics with stochastic input-state-output port-Hamiltonian systems*, arXiv:2502.00370 (February 1, 2025), treat a related controlled model and obtain spectral stability and Gaussian asymptotics. Their quadratic parameter is scaled differently, and their stated results do not provide the stiffness-dependent invariant energy classification here. General Ornstein–Uhlenbeck Lyapunov covariance theory supplies a standard method but does not by itself state the model-specific critical value or the reversed energy trend.

## Limitations

The theorem requires zero velocity-alignment coupling, independent equal-intensity Brownian accelerations, homogeneous vehicles, a quadratic potential, and stationary stable linear dynamics. Other alignment choices can change the critical boundary. A Gaussian linear model does not preserve nonnegative physical headways or speeds, so the result should not be read as a safety statement. The energy is the **centered fluctuation** Hamiltonian, not an uncentered deterministic baseline. The result does not address collisions, nonlinear car-following, feedback optimization, non-Gaussian stationary noise or infinite-vehicle limits. Formal publication-priority uncertainty remains for literature not located or independently audited.

## References

1. B. Rüdiger, A. Tordeux, and B. Ugurcan, *Stability analysis of a stochastic port-Hamiltonian car-following model*, arXiv:2212.05139, first version December 9, 2022, https://arxiv.org/abs/2212.05139 (especially model equation (23), covariance equation (47), and simulation discussion surrounding equation (73)).
2. J. Ackermann, M. Ehrhardt, T. Kruse, and A. Tordeux, *Modelling car-following dynamics with stochastic input-state-output port-Hamiltonian systems*, arXiv:2502.00370, first version February 1, 2025, https://arxiv.org/html/2502.00370v1 (especially Sections 3.3 and 4).
3. M. Bouadi, B. Jia, R. Jiang, X. Li and Z.-Y. Gao, *Stochastic factors and string stability of traffic flow: Analytical investigation and numerical study based on car-following models*, arXiv:2203.04877, https://arxiv.org/abs/2203.04877 (different car-following noise/string-stability setting).
