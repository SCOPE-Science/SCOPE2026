# Universal critical gap law and four-dimensional onset of nonreal sketched Ritz pairs

## Finding
For a real symmetric positive-definite eigenproblem, the two-dimensional sketched Rayleigh–Ritz procedure has a universal transition for the appearance of a nonreal conjugate Ritz pair. A gap of size comparable to the sketch-induced off-subspace coupling, divided by the square root of the sketch dimension, produces a nontrivial probability law. In particular, at a repeated projected eigenvalue the limiting probability of a complex pair is \(1-1/\sqrt{2}\), even as the subspace residual and embedding distortion vanish. A four-dimensional ambient space is the smallest possible for this phenomenon at an exactly repeated two-dimensional ordinary Ritz value.

Let \(t\geq0\). The critical-window probability is
\[
 p(t)=\frac{\sqrt2}{\pi}e^{-t^2/8}\int_0^1\frac{\sqrt{1-z^2}}{1+z^2}e^{-t^2z^2/8}\,dz.
\]
It is continuous and strictly decreasing, with
\[
 p(0)=1-\frac1{\sqrt2},\qquad
 p(t)\sim\frac{2}{\sqrt\pi\,t}e^{-t^2/8}\quad(t\to\infty).
\]
The formula holds for independent Gaussian or Rademacher sketch entries, and more generally for independent identically distributed real entries with mean zero and variance one.

## Assumptions and scope
For each integer \(s\ge2\), set \(m_s=s^2+4\), \(X_s=[e_1,e_2]\in\mathbb R^{m_s\times2}\), \(Y_s=[e_3,e_4]\), and parameters \(0<\rho_s\le1/2\), \(0\le g_s\le1\). Define the symmetric matrix
\[
 A_s=\begin{pmatrix}
 2-g_s/2&0&\rho_s&0\\
 0&2+g_s/2&0&\rho_s\\
 \rho_s&0&2&0\\
 0&\rho_s&0&2
 \end{pmatrix}\oplus2I_{m_s-4}.
\]
It is positive definite: each Gershgorin lower endpoint is at least \(2-g_s/2-\rho_s\ge1\). The ordinary Ritz matrix on \(X_s\) is \(H_s=\operatorname{diag}(2-g_s/2,2+g_s/2)\); its gap is \(g_s\), and \(\|(I-X_sX_s^\mathsf T)A_sX_s\|_2=\rho_s\).

Let \(S_s\in\mathbb R^{s\times m_s}\) have mutually independent entries \(\xi_{ij}/\sqrt{s}\), with identical real \(\xi_{ij}\), \(\mathbb E\xi_{ij}=0\) and \(\mathbb E\xi_{ij}^2=1\). Whenever \(S_sX_s\) has rank two, define the two-dimensional unwhitened sketched Ritz matrix
\[
 M_s=((S_sX_s)^\mathsf T(S_sX_s))^{-1}(S_sX_s)^\mathsf TS_sA_sX_s.
\]
The event of rank deficiency may be assigned an arbitrary outcome; its probability tends to zero under the stated assumptions. The spectrum of \(M_s\) agrees with that of the sketched Ritz matrix after basis whitening because the two matrices are similar. Put \(t_s=g_s\sqrt{s}/\rho_s\).

**Critical-window theorem.** If \(t_s\to t\in[0,\infty)\), then
\[
 \lim_{s\to\infty}\Pr(M_s\text{ has a nonreal eigenpair})=p(t).
\]
If \(t_s\to\infty\), the probability tends to zero. For \(g_s=0\), \(\rho_s=1/s\), both the residual and the active-four-dimensional subspace embedding error tend to zero (the latter in probability), but the nonreal-pair probability tends to \(1-1/\sqrt2\). This refers only to the four-dimensional span \(\operatorname{span}\{e_1,e_2,e_3,e_4\}\), not to an embedding of the full growing ambient space.

**Sharp minimal ambient dimension.** For any real symmetric \(A\in\mathbb R^{m\times m}\), any orthonormal \(X\in\mathbb R^{m\times2}\) satisfying \(X^\mathsf TAX=\mu I_2\), any real sketch \(S\) with \(SX\) of full rank, and \(m\le3\), every sketched Ritz eigenvalue is real. This is no longer true at \(m=4\), even when the sketch acts as an arbitrarily accurate subspace embedding.

**Deterministic four-dimensional threshold.** For \(0<\varepsilon<1\), set
\[
 J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
 W=\begin{pmatrix}I_2&\varepsilon J\\-\varepsilon J&I_2\end{pmatrix},\qquad S=W^{1/2}.
\]
With \(m=4\), \(X=[e_1,e_2]\) and the above \(A\), the sketch has Gram matrix \(W\), hence distorts every squared norm by at most \(\varepsilon\), and the exact sketched Ritz matrix is \(M=H+\rho\varepsilon J\). It has a nonreal conjugate pair if and only if \(g<2\rho\varepsilon\). At equality the eigenvalues coalesce, remaining real. This is a sharp criterion for this explicit family, not a universal embedding-error bound.

## Proof
**1. Similarity and the active block.** Let \(P=S_sX_s\) and \(Q=S_sY_s\). Since \(A_sX_s=X_sH_s+\rho_sY_s\), direct least-squares algebra gives
\[
 M_s=H_s+\rho_s(P^\mathsf TP)^{-1}P^\mathsf TQ.
\]
If \(P=UR\) is its reduced QR factorization, then \(B=X_sR^{-1}\) is sketch-orthonormal and the matrix actually formed after whitening is
\[
 U^\mathsf TS_sA_sB=RM_sR^{-1}.
\]
Thus eigenvalues, including whether they are nonreal, do not depend on the representation.

**2. The universal Gaussian limit.** Let \(U_s\) and \(V_s\) denote the first and next two unscaled columns of the sketch, respectively. The law of large numbers and the multivariate central limit theorem give
\[
 \frac{U_s^\mathsf TU_s}{s}\xrightarrow{\Pr}I_2,
 \qquad
 \frac{U_s^\mathsf TV_s}{\sqrt{s}}\xRightarrow{}G,
\]
where the four entries of \(G\) are independent standard normals. The cross-product covariance is exactly \(\mathbb E(\xi_a\xi_c\xi_b'\xi_d')=\delta_{ac}\delta_{bd}\); finite second moments suffice because the two column pairs are independent. Slutsky's theorem yields
\[
 \frac{\sqrt{s}}{\rho_s}(M_s-2I_2)
 \xRightarrow{}G+\operatorname{diag}(-t/2,t/2)
 \quad\text{when }t_s\to t.
\]
The real \(2\times2\) discriminant is a continuous polynomial; its zero set has zero probability under the continuous limiting Gaussian density. Hence the nonreal-event probabilities converge. If \(t_s\to\infty\), the noise matrices \(\sqrt{s}(P^\mathsf TP)^{-1}P^\mathsf TQ\) are tight, whereas the diagonal separation \(t_s\) diverges. Their discriminants are eventually nonnegative with probability tending to one.

**3. Exact cone integral.** Write the independent entries of \(G\) as \(G_{ij}\), and let
\[
 Z=\frac{G_{11}-G_{22}}{\sqrt2},\quad
 U=\frac{G_{12}+G_{21}}{\sqrt2},\quad
 V=\frac{G_{12}-G_{21}}{\sqrt2}.
\]
They are independent standard normals. The limiting matrix has a nonreal conjugate pair precisely when
\[
 V^2>U^2+(Z-t/\sqrt2)^2.
\]
In polar coordinates \((V,U)=(r\cos\theta,r\sin\theta)\), the inequality requires \(\cos(2\theta)>0\) and \(r^2>(Z-t/\sqrt2)^2/\cos(2\theta)\). Integrating the Rayleigh radial density and then the shifted Gaussian variable gives
\[
 p(t)=\frac2\pi\int_0^{\pi/4}
 \sqrt{\frac{\cos(2\theta)}{1+\cos(2\theta)}}
 \exp\left(-\frac{t^2}{4(1+\cos(2\theta))}\right)\,d\theta.
\]
The substitution \(z=\tan\theta\) gives the displayed formula. At \(t=0\), using \(z=\sin\theta\) evaluates its integral as \(\pi/\sqrt2-\pi/2\). The expression is positive and strictly decreasing in every positive \(t\); a Laplace expansion at \(z=0\) gives \(p(t)\sim2e^{-t^2/8}/(\sqrt\pi\,t)\).

**4. Minimal dimension and deterministic exactness.** For any orthonormal \(X\) with \(X^\mathsf TAX=\mu I_2\), the residual is \(R=(I-XX^\mathsf T)AX\), of rank at most \(m-2\). The sketched Ritz matrix satisfies \(M-\mu I_2=(SX)^\dagger SR\), so when \(m\le3\) this difference has rank at most one. A real scalar matrix plus a real rank-one matrix has only real eigenvalues. Conversely, in four dimensions the given \(W\) has eigenvalues \(1\pm\varepsilon\), each twice, and \(X^\mathsf TWX=I_2\), \(X^\mathsf TWY=\varepsilon J\). Hence \(M=H+\rho\varepsilon J\) has discriminant exactly \(g^2-4\rho^2\varepsilon^2\), giving the claimed sharp complex/real boundary.

## Verification
The standalone `check_collisions.py` evaluates the exact integral, tests the whitening similarity identities and four-dimensional embedding construction, verifies rank-one reality in ambient dimension three, compares the Gaussian limit against simulations of a real shifted-Ginibre matrix, and checks finite Gaussian/Rademacher sketch examples at several sample sizes. It returned `VERIFY_OK`. Its tests are finite corroboration only: the all-dimension, all-distribution and limiting claims follow from the proof above. Reproduce with Python 3, NumPy and SciPy by running `python check_collisions.py`.

## Relationship to prior work
Liu and Liu (2026), Section 3.1 and Sections 5.2–5.3, formulate whitening and real-Schur sketched Rayleigh–Ritz, explicitly recognizing that symmetric positive-definite input can produce nonreal projected eigenpairs. Nakatsukasa and Tropp (2021), Section 6.8, previously identify nonreal sketched Ritz estimates and discuss why small residuals can make eigenvalues nearly real. Those statements do not yield this probability profile, the universal critical gap scale or the minimal-four-dimensional exact embedding example. Forrester and Nagao (2007) analyze real Ginibre eigenvalues; the unshifted two-by-two Gaussian matrix's real/complex counts are established random-matrix facts, not a novelty claim here. The object here is the explicit connection between a sketched symmetric numerical eigenproblem, iid-entry universality, clustered Ritz gaps and the limiting nonreal block probability. A broad shifted-Ginibre matrix distribution may overlap with the integral formula independently of this numerical-method application.

## Limitations
Only a single two-column sketched Ritz extraction for the specified sparse positive-definite block family is analyzed; no iteration-wise law for full sSI or sTraceMIN is proved. The sketch has independent identically distributed real entries with zero mean and unit variance; structured or dependent sketches are not covered. The critical-window limit holds for fixed limiting \(t\) and the large-gap conclusion is qualitative; the fixed-profile asymptotic as \(t\to\infty\) does not assert a uniform relative error when \(t_s\) itself grows with \(s\). The number of complex pairs need not be stable under finite-precision roundoff when their imaginary parts vanish. No claim is made that the real-Schur remedy in the source paper fails. Priority against general shifted random-matrix formulae and earlier perturbation theory remains a residual literature risk. Independent audit has not been performed.

## References
1. J. Liu and Y. Liu, *Real-Arithmetic Sketched Eigensolvers for Symmetric Matrices*, arXiv:2610.22261v1 (15 October 2026), Sections 3.1 and 5; https://arxiv.org/html/2610.22261v1.
2. Y. Nakatsukasa and J. A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, arXiv:2111.00113 (2021), especially Section 6.8; https://arxiv.org/abs/2111.00113.
3. P. J. Forrester and T. Nagao, *Eigenvalue statistics of the real Ginibre ensemble*, arXiv:0706.2020 (2007); https://arxiv.org/abs/0706.2020.
4. N. Shao, *Stabilizing the Rayleigh–Ritz Procedure by Randomization*, arXiv:2604.01037 (2026); https://arxiv.org/abs/2604.01037. A different randomized projection and simple-eigenpair setting.
