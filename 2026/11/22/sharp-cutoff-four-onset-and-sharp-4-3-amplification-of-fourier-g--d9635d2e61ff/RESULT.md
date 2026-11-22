# Sharp cutoff-four onset and sharp \(4/3\) amplification of Fourier–Galerkin leakage in two-harmonic diffusion

## Finding

**Theorem (optimal two-harmonic boundary leakage).** Let \(K\ge2\) be an integer and \(0<s<1/\sqrt2\). On the circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), use normalized Lebesgue measure and the positive diffusion coefficient
\[
a(x)=1+\beta\cos(x-\phi)+\gamma\cos(2(x-\psi)),\qquad
\beta,\gamma\ge0,\quad \beta^2+\gamma^2=s^2,
\]
with arbitrary real phases \(\phi,\psi\). Set \(\mathcal A f=\partial_x(a\,\partial_x f)\) on smooth periodic functions, and let \(P_K\) project orthogonally in \(L^2(\mathbb T)\) onto \(\mathcal V_K=\operatorname{span}\{e^{ikx}:|k|\le K\}\). Write
\[
\Theta_K(\beta,\gamma)=\big\|P_K\mathcal A(I-P_K)\mathcal A P_K\big\|_{\mathcal V_K\to\mathcal V_K}.
\]
Define the positive integers and their squares
\[
a_K=K^2-1,\quad b_K=K(K+1),\quad c_K=K(K+2),\qquad
A_K=a_K^2,\quad B_K=b_K^2,\quad C_K=c_K^2,
\]
and let \(d_K=A_K+C_K-B_K\), \(\Delta_K=4A_KC_K-d_K^2\). Then \(d_K,\Delta_K>0\), and the exact maximum is
\[
\max_{\substack{\beta,\gamma\ge0\\\beta^2+\gamma^2=s^2}}\Theta_K(\beta,\gamma)
=\frac{s^2}{4}\begin{cases}
C_K,&K=2,3,\\[2mm]
\displaystyle\frac{4A_KC_KB_K}{\Delta_K},&K\ge4.
\end{cases}
\]
For \(K=2,3\), the only optimal allocation is \(\beta=0,\gamma=s\). For each \(K\ge4\), the optimal squared proportions are uniquely
\[
\frac{\gamma^2}{s^2}=\frac{2B_Kd_K}{\Delta_K}\in(0,1),\qquad
\frac{\beta^2}{s^2}=1-\frac{2B_Kd_K}{\Delta_K}\in(0,1).
\]
All results are independent of both phases. In particular, as \(K\to\infty\),
\[
\frac{\beta^2}{s^2}\longrightarrow\frac13,\quad
\frac{\gamma^2}{s^2}\longrightarrow\frac23,\quad
\frac{4}{s^2K^4}\max\Theta_K\longrightarrow\frac43.
\]
The optimal mixture therefore exceeds the largest single-harmonic leakage by an asymptotically sharp factor \(4/3\); the improvement first becomes strict at cutoff \(K=4\).

## Assumptions and scope

All operators and norms use normalized periodic \(L^2\) and exact Fourier projection. Since \(\beta+\gamma\le\sqrt2s<1\), the coefficient satisfies \(a(x)\ge1-\sqrt2s>0\) for all phases, and \(\mathcal A\) is symmetric and nonpositive on smooth periodic functions. The comparison fixes the squared Euclidean amplitude \(\beta^2+\gamma^2=s^2\), not the maximum or minimum diffusivity, which may vary across choices. The theorem is about the projection defect at every finite cutoff, not about a global discretization error or an empirically sampled matrix.

## Proof

Set \(e_k(x)=e^{ikx}\). Writing \(a_j\) for the Fourier coefficients of \(a\), direct differentiation gives
\[
\langle e_m,\mathcal A e_k\rangle=-mk\,a_{m-k}.
\]
Only offsets \(0,\pm1,\pm2\) occur, and positive-frequency output outside \(\mathcal V_K\) is supported on \(e_{K+1},e_{K+2}\). Its input comes only from \(e_{K-1},e_K\); the corresponding matrix is
\[
-\frac12\begin{pmatrix}
\gamma a_K e^{-2i\psi}&\beta b_K e^{-i\phi}\\
0&\gamma c_K e^{-2i\psi}
\end{pmatrix}.
\]
The negative-frequency exterior block is the complex conjugate of the reflected positive block. The two input blocks are disjoint for \(K\ge2\), so the entire exterior map \(E_K=(I-P_K)\mathcal A P_K\) has the squared operator norm of this \(2\times2\) matrix. Symmetry gives \(P_K\mathcal A(I-P_K)\mathcal A P_K=E_K^*E_K\), so \(\Theta_K=\|E_K\|^2\). Both the trace and determinant of the block Gram matrix depend only on \(\beta^2,\gamma^2\); the phases disappear.

Put \(y=\gamma^2/s^2\in[0,1]\), and abbreviate \(A=A_K,B=B_K,C=C_K,d=A+C-B\). The top eigenvalue \(\lambda_K(y)=4\Theta_K/s^2\) is the larger root of
\[
\lambda^2-[B+dy]\lambda+ACy^2=0,
\]
namely
\[
\lambda_K(y)=\frac{B+dy+\sqrt{(B+dy)^2-4ACy^2}}2.
\]
The top root is simple throughout \([0,1]\) because at the endpoints the squared singular values are \(\{B,0\}\) and \(\{C,A\}\) with \(B>0\), \(C>A\), and in the interior the off-diagonal block coupling is nonzero. Moreover \(d>0\), since \(d=K^4+2K^3+K^2+1\). The factorization
\[
\Delta=4AC-d^2=[(a_K+c_K)^2-B][B-(c_K-a_K)^2]
\]
is strictly positive: \(a_K+c_K>b_K>c_K-a_K\) for all \(K\ge2\).

Implicit differentiation shows that at an interior stationary point
\[
\lambda=\frac{2ACy}{d}.
\]
Substitution into the characteristic polynomial yields exactly one possible stationary point and value,
\[
y_*=\frac{2Bd}{\Delta},\qquad
\lambda_*=\frac{4ACB}{\Delta}.
\]
Since \(\Delta-2Bd=B^2-(C-A)^2\) and \(B+C-A>0\), one has \(y_*<1\) if and only if \(B>C-A\). The latter is equivalent to
\[
K^4-2K^3-5K^2+1>0.
\]
This polynomial is negative at \(K=2,3\), positive at \(K=4\), and strictly increasing for real \(K\ge3\) because its derivative is \(2K(2K-5)(K+1)>0\). Also \(\lambda'_K(0)=d>0\). Therefore at cutoffs \(2,3\) no interior stationary point exists and the maximum is \(\lambda_K(1)=C\). At every \(K\ge4\), the unique interior stationary point exists, and
\[
\lambda'_K(1)=\frac{C(C-A-B)}{C-A}<0.
\]
It is consequently the unique global maximum. This proves the finite-cutoff classification and uniqueness of the amplitude ratios.

Finally \(A/K^4,B/K^4,C/K^4,d/K^4\to1\), and \(\Delta/K^8\to3\), giving \(y_*\to2/3\) and \(\lambda_*/K^4\to4/3\). In the pure-harmonic cases the larger leakage is the \(\gamma=s\) case, with \(\Theta_K=s^2C/4\sim s^2K^4/4\). Division establishes the sharp \(4/3\) ratio. \(\square\)

## Verification

The self-contained standard-library script `VERIFY.py` reconstructs the finite Fourier exterior blocks exactly using rational arithmetic, independently checks both Gram characteristic invariants and the stationary-point identities for cutoffs \(2\) through \(44\), and scans the candidate maximal eigenvalue against finite comparison grids. It additionally checks phase invariance for complex coefficients. Executing `python VERIFY.py` returned `VERIFY_OK 46262` and `PHASE_VERIFY_OK 46430`. The all-cutoff and asymptotic conclusions above are proved algebraically; the finite checks are consistency tests, not substitutes for the proof.

## Relationship to prior work

Yuanchao Xu, *A Second-Order Stochastic Dynamic Mode Decomposition by Richardson Extrapolation* (arXiv:2611.00793, publicly available October 31, 2026), Proposition 2.2 identifies the second-order Galerkin residual with \(E_K^*E_K\) for symmetric generators. Its Example 4.5 calculates \(\Theta_K=\beta^2K^2(K+1)^2/4\) for the **single** coefficient harmonic \(1+\beta\cos x\). Those are essential prior identities used here. They do not state the sharp two-harmonic amplitude-budget optimizer, the cutoff-\(4\) onset, or its \(4/3\) limiting gain. General Fourier–Galerkin boundary coupling and two-by-two singular values are established tools; the specific constrained extremal classification is the assessed added statement, not a claim to have invented those tools.

## Limitations

The maximum is over the specified two-harmonic family at fixed coefficient energy; no extremality is asserted over arbitrary diffusivities or other amplitude budgets. The residual is an operator quantity and is not automatically the observed finite-time or finite-sample error. The result does not establish that the source's convergence estimates fail or that a practical implementation is unstable. Existing general Fourier spectral analysis may subsume isolated calculations; exhaustive historical priority and independent verification are not established.

## References

1. Y. Xu, *A Second-Order Stochastic Dynamic Mode Decomposition by Richardson Extrapolation*, arXiv:2611.00793v1 (October 31, 2026), especially Proposition 2.2 and Example 4.5. https://arxiv.org/abs/2611.00793
2. J. S. Hesthaven, S. Gottlieb and D. Gottlieb, *Spectral Methods for Time-Dependent Problems*, Cambridge University Press, 2007, Chapter 3 (general Fourier–Galerkin residual and boundary-mode context). https://doi.org/10.1017/CBO9780511618352
