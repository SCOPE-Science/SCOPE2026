# Weakest-row stability frontier for smoothed-momentum randomized Kaczmarz

## Finding

Consider the randomized Kaczmarz algorithm with geometrically smoothed momentum, as defined by Alderman–Luikart–Marshall, on an invertible diagonal real system of dimension \(d\ge 2\). Write \(p_i=a_i^2/\sum_j a_j^2\) for its row-selection probabilities and \(p_* = \min_i p_i\). Fix momentum \(0\le M\le1\), smoothing \(0\le\beta<1\), and initialize the velocity at zero. Define
\[
F(p,\beta,M)=-2(1-\beta)^2M^2+igl(2p-1-2\beta+(3-2p)\beta^2\bigr)M+(1+\beta)(1-\beta+\beta p).
\]
For **every** deterministic initial error, the mean squared Euclidean error converges geometrically to zero **if and only if** \(F(p_*,\beta,M)>0\). If \(F(p_*,\beta,M)\le0\), every initial error having a nonzero component in a least-selected coordinate has nondecaying mean squared error; the corresponding component grows at least exponentially when the inequality is strict in the reverse direction and \(M>0\).

The scalar threshold for a coordinate selected with probability \(p\in(0,1)\) is the unique positive zero \(M_*(p,\beta)\) of \(F\), with \(F>0\) precisely for \(0\le M<M_*\). At every fixed \(\beta<1\),
\[
\lim_{p\downarrow0}M_*(p,\beta)=\frac12.
\]
Hence on equally scaled \(d\)-row orthogonal systems, the sharp admissible momentum tends to \(1/2\) as \(d\to\infty\), regardless of any fixed amount of smoothing. More sharply, full momentum \(M=1\) is mean-square stable precisely when
\[
\beta>\beta_c(p_*):=\frac{p_*+2-\sqrt{9p_*^2-4p_*+4}}{2p_*}.
\]
Here \(0<p_*\le1/2\) and \(\beta_c(p_*)\uparrow1\) as \(p_*\downarrow0\). By contrast, the signed expected iterate converges for all \(M<1\) and \(\beta<1\). Thus signed-mean convergence can conceal divergence of mean-square error, with a boundary governed by the **least** frequently sampled row rather than average conditioning.

## Assumptions and scope

Let \(d\ge2\), \(A=\operatorname{diag}(a_1,\ldots,a_d)\), all \(a_i\ne0\), and \(b=Ax_*\). Independently at each integer time \(t\ge0\), choose \(I_t=i\) with probability \(p_i=a_i^2/\|A\|_F^2\). With \(x_0\in\mathbb R^d\) deterministic and \(y_0=0\), the algorithm is
\[
x_{t+1}=x_t+\frac{b_{I_t}-a_{I_t}(x_t)_{I_t}}{a_{I_t}^2}a_{I_t}e_{I_t}+My_t,\qquad y_{t+1}=\beta y_t+(1-\beta)(x_{t+1}-x_t).
\]
All results refer to exact real arithmetic and fresh independent row draws. “Geometric mean-square convergence for every initial error” means, for each deterministic \(x_0\), there exist \(C<\infty\) and \(\rho<1\), possibly depending on the fixed parameters, such that \(\mathbb E\|x_t-x_*\|_2^2\le C\rho^t\). At the critical boundary the error is not asserted to converge or diverge along individual random trajectories; only its second moment is classified. The deterministic solution is unique because \(A\) is invertible. No claim is made for nonorthogonal rows, dependent selections, adaptive momentum, or nonzero initial velocity.

## Proof

Fix a coordinate \(i\), put \(p=p_i\), \(c=1-\beta>0\), \(g=\beta+cM\), \(e_t=(x_t-x_*)_i\), and \(v_t=(y_t)_i\). The indicator \(B_t=\mathbf1\{I_t=i\}\) is independent of the past and Bernoulli \(p\). The scalar state \(z_t=(e_t,v_t)^{\mathsf T}\) obeys
\[
z_{t+1}=K_{B_t}z_t,\quad K_0=\begin{pmatrix}1&M\\0&g\end{pmatrix},\quad K_1=\begin{pmatrix}0&M\\-c&g\end{pmatrix}.
\]
For the covariance entries \(u_t=(\mathbb E e_t^2,\mathbb E[e_tv_t],\mathbb E v_t^2)^{\mathsf T}\), independence gives \(u_{t+1}=Q(p,\beta,M)u_t\), where
\[
Q=\begin{pmatrix}
1-p&2(1-p)M&M^2\\
0&(1-p)g-pcM&Mg\\
pc^2&-2pcg&g^2
\end{pmatrix}.
\]
Direct polynomial calculation yields
\[
\det(I_3-Q)=p(1-\beta)F(p,\beta,M).
\]
The covariance transformation is \(\mathcal T(X)=(1-p)K_0XK_0^{\mathsf T}+pK_1XK_1^{\mathsf T}\), which preserves the closed cone of positive-semidefinite symmetric matrices. Standard finite-dimensional cone Perron–Frobenius theory makes its spectral radius \(r\) a nonnegative real eigenvalue with a nonzero positive-semidefinite eigenmatrix. At \(M=0\), its eigenvalues are \(1-p\), \((1-p)\beta\), and \(\beta^2\), each strictly below one. Consequently, as \(M\) varies, \(r\) can cross one only when \(\det(I_3-Q)=0\).

For any fixed \(p\in(0,1)\), \(\beta<1\), the quadratic \(F(p,\beta,M)=C+BM-2(1-\beta)^2M^2\), where \(C=(1+\beta)(1-\beta+\beta p)>0\), has exactly one positive zero. Continuity and the cone spectral-radius property therefore show \(r<1\) below that zero, \(r=1\) at the zero, and \(r>1\) above it. (The zero can exceed the permitted interval \([0,1]\).)

To prove sharp failure for the stipulated zero-velocity initialization, take \(e_0\ne0\). One step gives the strictly positive-definite covariance \(\mathbb E z_1z_1^{\mathsf T}=e_0^2\operatorname{diag}(1-p,pc^2)\). Let \(H\ne0\) be a positive-semidefinite eigenmatrix of \(\mathcal T\) with eigenvalue \(r\ge1\). For some \(\epsilon>0\), the first covariance dominates \(\epsilon H\). Hence \(\mathbb E z_tz_t^{\mathsf T}\succeq\epsilon r^{t-1}H\). Necessarily \(H_{11}>0\) when \(M>0\): otherwise positive semidefiniteness makes \(H_{12}=0\), and the first diagonal entry of \(\mathcal T(H)\) equals \(M^2H_{22}>0\), a contradiction. Thus \(\mathbb E e_t^2\ge\epsilon H_{11}r^{t-1}\). The case \(M=0\) is already stable. This proves the coordinatewise exact frontier for every nonzero initial coordinate error.

Finally,
\[
\partial_pF=2(1-\beta^2)M+\beta(1+\beta)\ge0,
\]
so the least selection probability determines the entire squared-norm boundary, since \(\mathbb E\|x_t-x_*\|_2^2=\sum_i\mathbb E e_{t,i}^2\). For the rare-row limit, substitute \(p=0\) into the polynomial to obtain
\[
F(0,\beta,M)=(1-\beta)(1-2M)((1-\beta)M+1+\beta),
\]
which has the sole positive root \(1/2\). Continuous dependence of the unique positive root gives the claimed limit. At \(M=1\), \(F=-p\beta^2+(p+2)\beta+2p-2\), strictly increasing on \([0,1]\) for \(p\le1/2\), with the displayed unique interior zero \(\beta_c(p)\).

The signed first-moment state matrix is
\[
\overline K=\begin{pmatrix}1-p&M\\-p(1-\beta)&\beta+(1-\beta)M\end{pmatrix}.
\]
Its determinant is \((1-p)\beta+(1-\beta)M\), and \(\det(I_2-\overline K)=p(1-\beta)>0\). For \(M<1\), all three second-order Jury inequalities hold (positive \(1-\det\), positive \(1-\operatorname{tr}+\det\), and positive \(1+\operatorname{tr}+\det\)); hence its eigenvalues lie in the open unit disk. This proves signed-mean convergence independently of the second-moment frontier.

## Verification

Run `python verify.py` with SymPy installed. The standalone program reconstructs both update matrices, derives the symmetric-square covariance action, checks the determinant identity, the monotonicity derivative, the rare-row factorization, the full-momentum polynomial, and the signed-mean determinant. It also compares the moment recurrence against direct, probability-weighted enumeration of **all** binary sequences through length five for 48 rational parameter triples, giving 240 exact path-moment equalities. This is finite algebraic evidence supporting the proof, not a substitute for its all-parameter cone argument.

## Relationship to prior work

Alderman, Luikart and Marshall (arXiv:2401.09415, first public 2024-01-17), introduce the exact smoothed-momentum update and characterize signed expected errors along singular vectors. Their discussion explicitly asks for critical momentum and mean-square/absolute-error understanding, but their theorem is not a second-moment criterion. Bollapragada, Chen and Ward (arXiv:2206.07553, first public 2022-06-15) analyze large-minibatch heavy-ball convergence via random matrix products; their sufficient batch conditions do not yield this exact one-row, heterogeneously sampled mean-square frontier. Lorenz and Winkler (arXiv:2307.15435) analyze *adaptively chosen* momentum, not the fixed smoothed-momentum recursion here.

A publicly indexed equal-probability two-coordinate result, identifier `2026/10/4/SCOPE-exact-mean-square-stability-frontier-and-a-signed-mean-blind-spo--e15c00248209`, already establishes the special case \(p=1/2\), where the present polynomial reduces to \(\beta+2(1-\beta)M<\sqrt{\beta+2}\). **That special case is not claimed as original.** The contribution here is the nonuniform, arbitrary-dimensional worst-row theorem and the singular rare-sampling/full-momentum smoothing transitions, which do not follow from the equal-probability statement without a new unequal-sampling covariance calculation. The complete text of that indexed result was unavailable for detailed implication comparison; its abstract-level coverage is a residual originality risk.

## Limitations

Only diagonal, full-rank real systems are considered, and independence of row draws is essential. The stability notion is second moment, not almost-sure divergence or convergence. The sharp rare-row limit assumes smoothing \(\beta<1\) is fixed as the sampling probability tends to zero; joint limits allowing \(\beta\to1\) are not classified here. The equal-probability two-coordinate special case is known. Literature overlap cannot be ruled out merely by unsuccessful searches, and the inaccessible full text of the indexed equal-probability result remains a specific risk. No independent audit has been performed.

## References

- S. J. Alderman, R. W. Luikart, N. F. Marshall, *Randomized Kaczmarz with geometrically smoothed momentum*, arXiv:2401.09415, first submitted 2024-01-17, https://arxiv.org/html/2401.09415v3.
- R. Bollapragada, T. Chen, R. Ward, *On the fast convergence of minibatch heavy ball momentum*, arXiv:2206.07553, first submitted 2022-06-15, https://arxiv.org/html/2206.07553v5.
- D. A. Lorenz, M. Winkler, *Minimal error momentum Bregman-Kaczmarz*, arXiv:2307.15435, first submitted 2023-07-28, https://arxiv.org/html/2307.15435v1.
- *Exact mean-square stability frontier and a signed-mean blind spot in KGSM*, published index 2026/10/4, identifier `2026/10/4/SCOPE-exact-mean-square-stability-frontier-and-a-signed-mean-blind-spo--e15c00248209` (summary available; full text not accessible).
