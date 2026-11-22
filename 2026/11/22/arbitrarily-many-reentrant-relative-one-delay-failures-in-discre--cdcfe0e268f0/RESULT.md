# Arbitrarily many reentrant relative one-delay failures in discrete heat flow

## Finding

For every integer \(m\ge2\), a standard \(m\)-site Dirichlet discrete heat equation admits a nonzero, explicitly prescribed observation whose **best scalar one-delay relative forecast error** has at least \(m-1\) distinct strict local maxima as the integer burn-in time increases. At those maxima the relative defect tends to one, while at the two neighboring integer times it tends to zero, even though the corresponding *absolute* optimal defects decrease geometrically at every step.

The dimension-uniform construction is exact. The phenomenon is a separation between absolute contractive closure and **normalized** forecasting quality, not a contradiction to absolute-error heat-delay estimates.

## Assumptions and scope

Fix \(m\ge2\). Let \(A_m\in\mathbb R^{m\times m}\) be the symmetric tridiagonal matrix with diagonal entries \(2\), first upper/lower diagonals \(-1\), and all other entries zero. Its distinct eigenvalues are
\[
\nu_j=2-2\cos\frac{j\pi}{m+1},\qquad 1\le j\le m,
\]
with corresponding Euclidean-orthonormal eigenvectors \(v_1,\ldots,v_m\). For a positive lag \(L\), let \(\Phi_L=e^{-LA_m}\). This is the exact sampled semigroup, not a time-discretization approximation.

For an observation \(b_L\), define for all integers \(s\ge0\)
\[
E_L(s)=\min_{c\in\mathbb R}\|\Phi_L^{s+1}b_L-c\Phi_L^s b_L\|_2,\qquad
R_L(s)=\frac{E_L(s)}{\|\Phi_L^{s+1}b_L\|_2}.
\]
The quantity \(E_L(s)\) is the worst-case (over unit-norm initial states) absolute defect of an optimally chosen scalar one-delay observable closure. Its normalization \(R_L(s)\) is by the operator norm of the *next observation functional*, not by each trajectory's scalar output.

For \(1\le j<m\), put
\[
T_j=4(m-j)+\tfrac12,\quad \gamma_1=0,\quad
\gamma_{j+1}=\gamma_j+(\nu_{j+1}-\nu_j)T_j,
\quad b_L=\sum_{j=1}^m e^{L\gamma_j}v_j.
\]
This nonlocal vector depends on lag and has nonzero projection on every mode; a fixed single-coordinate point sensor is **not** claimed to realize the construction.

## Proof

**1. Unique dominant modes.** The modal coefficient of \(\Phi_L^s b_L\) in direction \(v_j\) is \(\exp[L(\gamma_j-s\nu_j)]\). Set \(\ell_j(s)=\gamma_j-s\nu_j\). Then
\[
\ell_{j+1}(s)-\ell_j(s)
=(\nu_{j+1}-\nu_j)(T_j-s).
\]
The crossing times satisfy \(T_1>T_2>\cdots>T_{m-1}>0\), spaced exactly four apart. Therefore, for every \(1\le j<m\) and \(T_{j+1}<s<T_j\) (with the convention \(T_m=-\infty\)), the unique maximizing affine exponent is \(\ell_{j+1}(s)\). For \(T_j<s<T_{j-1}\) (where \(T_0=+\infty\)), the unique maximum is \(\ell_j(s)\). This follows because the adjacent exponent differences are positive before their crossings and negative after.

**2. Relative peaks.** Let \(s_j=4(m-j)=T_j-\tfrac12\). Both \(s_j-1\) and \(s_j\) lie strictly inside the interval where mode \(j+1\) is uniquely dominant, whereas both \(s_j+1\) and \(s_j+2\) lie strictly inside the interval where mode \(j\) dominates. For fixed \(m\) and each of these finitely many integer times, dividing each heat snapshot by its own Euclidean norm and letting \(L\to\infty\) gives
\[
\frac{\Phi_L^s b_L}{\|\Phi_L^s b_L\|_2}\longrightarrow v_{j+1}
\quad(s=s_j-1,s_j),\qquad
\frac{\Phi_L^s b_L}{\|\Phi_L^s b_L\|_2}\longrightarrow v_j
\quad(s=s_j+1,s_j+2).
\]
The least-squares projection identity is
\[
R_L(s)^2=1-
\frac{\langle\Phi_L^s b_L,\Phi_L^{s+1}b_L\rangle^2}
{\|\Phi_L^s b_L\|_2^2\,\|\Phi_L^{s+1}b_L\|_2^2}.
\]
Consequently \(R_L(s_j)\to1\), and \(R_L(s_j-1),R_L(s_j+1)\to0\), because \(v_j\perp v_{j+1}\). The convergence holds simultaneously at finitely many indices for fixed \(m\). Thus, for all sufficiently large **finite** \(L\), each of the \(m-1\) separated indices \(s_j\) is a strict local maximum of the discrete-time sequence \(R_L(s)\).

**3. Absolute errors nevertheless decrease.** For each \(s\), let \(c_s\) be the scalar least-squares minimizer defining \(E_L(s)\). Then
\[
\begin{aligned}
E_L(s+1)&\le\|\Phi_L(\Phi_L^{s+1}b_L-c_s\Phi_L^s b_L)\|_2\\
&\le\|\Phi_L\|_2 E_L(s)
=e^{-L\nu_1}E_L(s).
\end{aligned}
\]
Because every mode of \(b_L\) is nonzero and the eigenvalues of \(\Phi_L\) are distinct, \(E_L(s)>0\); the factor \(e^{-L\nu_1}<1\) yields strict stepwise decrease. There is no limit/interchange issue: the inequality holds for every finite \(L>0\).

**4. Exact reproducibility identity.** With \(W_j(s)=e^{2L\ell_j(s)}\) and \(q_j=e^{-L\nu_j}\), the residual can also be evaluated without explicitly computing eigenvectors:
\[
R_L(s)^2=
\frac{\sum_{i<j}W_i(s)W_j(s)(q_i-q_j)^2}
{\big(\sum_i W_i(s)\big)\big(\sum_i W_i(s)q_i^2\big)}.
\]
This is the exact weighted-variance identity. It is nonnegative and has no cancellation against one; the standalone script rescales weights to prevent numerical overflow.

## Verification

Execute `python verify.py` with a standard Python installation. It independently computes the pairwise modal-variance residual and compares it with the direct least-squares angle identity at moderate lags. In dimensions two through eight, it checks strict local-maximizer inequalities at all prescribed indices for two positive lag values and checks every prescribed adjacent logarithmic crossing identity. The extracted checker completed **273 checks** with `VERIFY_OK`.

The proof, not the finite numerical checks, establishes all dimensions, existence of a sufficiently large lag, and the exact limiting values.

## Relationship to prior work

Han, Xiu and Zikatanov (2026) prove absolute approximation bounds for heat-semigroup delay closures, including an exponentially decreasing smoothed-Krylov error bound in their Theorem 7 (equation (34)) and an absolute observable-defect bound in Corollary 9 (equation (39)). Those statements involve unnormalized defects and do not imply monotonicity of the normalized optimally fitted *one-delay* angle for every observation.

The published result *Arbitrarily many Fourier-ratio peaks under periodic heat flow* establishes repeated maxima for a different statistic, the Fourier \(\ell^1/\ell^2\) ratio along periodic diffusion. Its full result was compared: that nonlinear ratio is not the projective best-fit residual of two successive heat observations and does not imply the present theorem without a new argument. Both use deliberately separated spectral crossing times, so the construction method itself is not claimed as novel.

The standard Kantorovich inequality can control a **single** angle between \(u\) and \(\Phi_Lu\) in terms of extreme eigenvalues but does not establish or exclude arbitrarily many distinct burn-in maxima on one fixed trajectory; the proof supplies that temporal structure explicitly.

## Limitations

The observation \(b_L\) is nonlocal, has exponentially unequal spectral coefficients, and changes with \(L\). The result does not establish this behavior for point sensors, bounded coefficient dynamic range, fixed \(b\) across varying lags, higher-memory closures, noisy observations, floating-point implementations, or prediction errors normalized by an individual trajectory's possibly vanishing scalar output. The heat matrix and relative-residual definition are fixed, but the dimension grows to obtain arbitrarily many peaks. Unindexed prior results about angles of successive normalized positive-semigroup iterates remain a historical-priority risk. No independent validation is asserted.

## References

1. X. Han, D. Xiu and L. T. Zikatanov, *Delay Closure of Observable Dynamics for the Heat Equation*, arXiv:2611.19040v1 (first public 2026-11-14), https://arxiv.org/html/2611.19040v1.
2. *Arbitrarily many Fourier-ratio peaks under periodic heat flow*, published research record (2026-10-18), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-arbitrarily-many-fourier-ratio-peaks-under-periodic-heat-flow--0d41ccdbf41d.
3. Kantorovich's inequality for positive-definite operators (standard spectral comparison; cited only as background, not as a claim of priority).
