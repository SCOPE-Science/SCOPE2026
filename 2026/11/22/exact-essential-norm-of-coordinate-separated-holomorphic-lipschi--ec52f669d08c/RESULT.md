# Exact essential norm of coordinate-separated holomorphic-Lipschitz linearizations

## Finding

Let \(1\le p<\infty\), \(X=\ell_p(\mathbb C)\), and \(B_X=\{x\in X:\|x\|_p<1\}\). For every integer \(j\ge1\), take a holomorphic function \(\varphi_j:\mathbb D\to\mathbb C\) satisfying \(\varphi_j(0)=0\), and put
\[
c_j=\sup_{z\in\mathbb D}|\varphi_j'(z)|,\qquad C=\sup_{j\ge1}c_j<\infty.
\]
Assume that the coordinate-separated map \(f:B_X\to X\), defined by \(f(x)=(\varphi_j(x_j))_{j\ge1}\), satisfies both \(r:=\sup_{x\in B_X}\|f(x)\|_p<1\) and relative norm compactness of \(f(B_X)\). Let \(\mathcal G_0(B_X)\) be the holomorphic-Lipschitz-free space, and \(T=\widehat f:\mathcal G_0(B_X)\to\mathcal G_0(B_X)\) the operator determined by \(T\delta(x)=\delta(f(x))\).

Then
\[
\boxed{\ \|T\|=C,\qquad \|T\|_{\mathrm e}=\limsup_{j\to\infty}c_j\ },
\]
where \(\|T\|_{\mathrm e}=\inf\{\|T-K\|:K\text{ compact}\}\). In particular \(T\) is compact exactly when \(c_j\to0\). For \(1<p<\infty\), \(T\) is always weakly compact under the stated hypotheses. For \(p=1\), it is weakly compact exactly when it is compact.

For every \(1\le p<\infty\) and \(t\in[0,1]\), there is such a symbol with \(\|T\|=1\) and \(\|T\|_{\mathrm e}=t\). For \(p>1\) these are all weakly compact, including the noncompact examples \(t>0\).

## Assumptions and scope

The scalar functions are holomorphic on the open disk and need only have bounded first derivatives, not continuous extensions to the closed disk. The uniform strict-interior requirement \(r<1\) is essential to the argument, as is relative compactness of the symbol image. The coordinate norm is the standard complex \(\ell_p\) norm for finite \(p\). No assertion is made for \(p=\infty\), arbitrary non-coordinate-separated maps, or images touching the target unit sphere.

For the compactness assumption one may equivalently require
\[
\eta_N:=\sup_{x\in B_X}\|(I-P_N)f(x)\|_p\longrightarrow0,
\]
where \(P_N\) truncates to the first \(N\) coordinates. This follows from the standard relative-compactness criterion in \(\ell_p\): boundedness plus uniform smallness of coordinate tails.

## Proof

**1. Basic regularity and norm.** By integration on the disk segment, \(|\varphi_j(z)-\varphi_j(w)|\le c_j|z-w|\). Therefore \(f\) is \(C\)-Lipschitz on the ball. Each finite-coordinate truncation \(f_N=P_Nf\) is holomorphic; the compact-image hypothesis gives \(\|f-f_N\|_\infty\le\eta_N\to0\), hence \(f\) is Fréchet holomorphic. For each \(j\) and \(z\in\mathbb D\), evaluation at \(x=ze_j\) and differentiation in direction \(e_j\) show \(\|Df(x)\|\ge|\varphi_j'(z)|\). Thus \(\|f\|_{\mathrm{Lip}}=C\). The universal linearization property of the holomorphic-Lipschitz-free space proves \(\|T\|=C\).

**2. Compact upper approximants.** Put \(F=\delta\circ f\) and \(F_N=\delta\circ f_N\), where \(\delta:B_X\to\mathcal G_0(B_X)\) is the canonical holomorphic isometric evaluation embedding. Each \(f_N(B_X)\) is bounded in a finite-dimensional subspace, and its set of normalized Lipschitz slopes is also contained in that finite-dimensional subspace and bounded. Since \(\|f_N\|_\infty\le r<1\), Theorem 4.1 of Bayart--Lemay--Petitjean implies that \(T_N=\widehat {f_N}\) is compact.

The canonical embedding \(\delta\) is a bounded holomorphic map on the target unit ball, with \(\|\delta(y)\|=\|y\|\le1\). Banach-space Cauchy estimates give a finite constant \(K_r\) such that
\[
\|D\delta(y)-D\delta(z)\|\le K_r\|y-z\|
\quad\text{whenever }\|y\|,\|z\|\le r.
\]
Also \(\|D\delta(y)\|\le1\), as \(\delta\) is an isometry. Write \(C_N=\sup_{j>N}c_j\). The chain rule, inserting and subtracting \(D\delta(f(x))Df_N(x)\), gives
\[
\begin{aligned}
\|D(F-F_N)(x)\|
&\le\|D\delta(f(x))\|\,\|D(f-f_N)(x)\|\\
&\quad+\|D\delta(f(x))-D\delta(f_N(x))\|\,\|Df_N(x)\|\\
&\le C_N+K_r C\eta_N.
\end{aligned}
\]
The open ball is convex, so the Lipschitz constant of \(F-F_N\) is bounded by the supremum of this derivative. The linearization isometric property now gives
\[
\|T-T_N\|\le C_N+K_rC\eta_N.
\]
Since \(T_N\) is compact and \(\eta_N\to0\), this proves \(\|T\|_{\mathrm e}\le\limsup_jc_j\).

**3. Lower bound against every compact operator.** Write \(L=\limsup_jc_j\) and choose distinct indices \(j_k\to\infty\) and points \(z_k\in\mathbb D\) with \(|\varphi_{j_k}'(z_k)|\to L\). Define
\[
u_k=D\delta(z_ke_{j_k})e_{j_k}\in\mathcal G_0(B_X).
\]
Because \(\delta\) is an isometry, \(\|u_k\|=1\). The canonical barycenter \(\beta:\mathcal G_0(B_X)\to X\) satisfies \(\|\beta\|=1\) and \(\beta\delta(y)=y\). Differentiating \(T\delta(x)=\delta(f(x))\) and then applying \(\beta\) yields
\[
\beta Tu_k=\varphi_{j_k}'(z_k)e_{j_k}.
\]
Fix an arbitrary compact \(K:\mathcal G_0(B_X)\to\mathcal G_0(B_X)\). Along a subsequence \(\beta Ku_k\) converges in norm to some \(v\in X\). The \(j_k\)-th coordinates of this subsequence tend to zero, since \(\|\beta Ku_k-v\|\to0\) and \(v_{j_k}\to0\). Consequently
\[
\|T-K\|\ge\limsup_k\|\beta(T-K)u_k\|_p
\ge\lim_k\big|\varphi_{j_k}'(z_k)-(\beta Ku_k)_{j_k}\big|=L.
\]
This is true for every compact \(K\), proving the opposite inequality and the exact formula.

**4. Weak compactness and sharp continuum.** For \(1<p<\infty\), \(X=\ell_p\) is reflexive, and Theorem 4.10 of Bayart--Lemay--Petitjean applies to the relatively compact, strictly interior image. At \(p=1\), their Theorem 3.9 identifies weak compactness with compactness.

To obtain every ratio, set \(\varphi_1=0\), and for \(j\ge2\) let
\[
\varphi_j(z)=\frac{b_j}{j^2}z^{j^2},\qquad
b_2=1,\quad b_j=t\ (j\ge3).
\]
The derivative suprema are \(c_j=b_j\), hence \(C=1\) and \(L=t\). Uniformly for \(x\in B_X\),
\[
\|f(x)\|_p\le\left(\sum_{j=2}^\infty j^{-2p}\right)^{1/p}
\le\sum_{j=2}^\infty j^{-2}<1.
\]
The coordinate tails are bounded by the corresponding convergent series, so the image is relatively compact and the strict-interior condition holds. The formula follows.

## Verification

The proof separates four nonfinite steps: the standard free-space linearization, compactness of finite-coordinate approximants under a strict interior condition, a uniform interior derivative bound for the evaluation embedding, and a barycenter/coordinate-escape lower bound against every compact operator. Each is explicit above. The finite diagnostic in `check_diag.py` checks the concrete power-family input bounds, derivative suprema and tail behavior at several parameters; it does not certify the general infinite-dimensional theorem.

## Relationship to prior work

Bayart--Lemay--Petitjean (arXiv:2610.26047, first public 2026-10-19) establish qualitative compactness and weak-compactness criteria and construct diagonal monomial examples with compact image but noncompact linearization (Examples 4.11 and 4.14). Those results are used, not claimed new. The distinction here is an *exact quantitative distance to compact operators* for all coordinate-separated symbols satisfying the two geometric hypotheses. Their qualitative criteria determine the zero/nonzero status but do not, as stated, yield this sharp Calkin norm or the full range of normalized essential norms.

Dimant--García-Lirola--Guerrero-Viu--Procházka (arXiv:2605.21279, first public 2026-05-20) study adjoint composition operators on holomorphic Lipschitz functions, including related weakly compact/noncompact monomial examples. Their results do not state this diagonal essential-norm formula. Classical essential-norm estimates on scalar analytic Lipschitz/Bergman/Hardy function spaces concern different operators and do not imply the asserted holomorphic-free-space identity.

## Limitations

This is a theorem for coordinate-separated maps into \(\ell_p\) with finite \(p\), strict interior range and norm-precompact image; it does not generalize merely from qualitative weak compactness. The proof relies on the published compactness/weak-compactness theorems cited below. While targeted searches of accessible literature and mathematical research records did not reveal an equivalent quantitative formula, absence from those searches does not prove priority; terminology and unindexed publications remain residual risks. No independent mathematical audit has been performed.

## References

1. F. Bayart, M. Lemay, C. Petitjean, *Compactness and weak compactness of linearized Holomorphic-Lipschitz maps*, arXiv:2610.26047 (2026), https://arxiv.org/abs/2610.26047, especially Theorems 3.9, 4.1, 4.10; Lemma 4.3; Examples 4.11, 4.14.
2. V. Dimant, L. C. García-Lirola, J. Guerrero-Viu, A. Procházka, *Composition operators for holomorphic Lipschitz functions*, arXiv:2605.21279 (2026), https://arxiv.org/abs/2605.21279, especially Example 4.13.
3. R. Aron, V. Dimant, L. C. García-Lirola, M. Maestre, *Linearization of holomorphic Lipschitz functions*, arXiv:2304.07149 (2023), https://arxiv.org/abs/2304.07149, for the canonical linearization and evaluation embedding.
