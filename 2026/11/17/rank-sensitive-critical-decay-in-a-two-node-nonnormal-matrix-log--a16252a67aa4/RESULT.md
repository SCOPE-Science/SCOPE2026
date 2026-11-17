# Rank-sensitive critical decay in a two-node nonnormal matrix logistic map

## Finding
Let \(0<c<3/2\), \(B_c=\begin{pmatrix}1&c\\0&1\end{pmatrix}\), and let \(H_{n+1}=B_cH_n(I-H_n)B_c^{*}\) on complex Hermitian \(2\times2\) matrices. For every initial state \(0\le H_0<I\) (the latter means \(I-H_0\) is positive definite), \(H_n\to0\). More precisely, writing \(H_n=(h_{ij,n})\):

* If \(H_0\) is positive definite, then
  \[
  \lim_{n\to\infty}nh_{11,n}=4,\qquad
  \lim_{n\to\infty}c n^2h_{12,n}=6,\qquad
  \lim_{n\to\infty}c^2n^3h_{22,n}=12.
  \]
  In particular \(n^4\det H_n\to12/c^2\), and its eigenvalues, in decreasing order, are asymptotic to \(4/n\) and \(3/(c^2n^3)\).
* If \(H_0\) has rank one and its range is not \(\operatorname{span}(e_1)\), the respective scaled limits are \(3,3,3\). Its determinant is always zero.
* If \(H_0\) has rank one with range \(\operatorname{span}(e_1)\), the only nonzero entry is \(h_{11,n}\), and \(nh_{11,n}\to1\).
* If \(H_0=0\), the orbit is zero.

Thus the same neutral nonnormal coupling has three different universal leading amplitudes \(4,3,1\), distinguished exactly by initial rank and alignment. Moreover for \(H_0=\varepsilon I\) with \(0<\varepsilon<c^2/(2+c^2)\), one has \(\operatorname{tr} H_1>\operatorname{tr} H_0\) although \(H_n\to0\): transient amplification coexists with global extinction.

## Assumptions and scope
The state space is \(\mathcal D=\{H=H^*:0\le H\le I\}\), where \(H\ge0\) is the Hermitian positive-semidefinite order. The strict hypothesis \(H_0<I\) avoids possible boundary eigenvalue-one rank changes. The parameter condition \(c<3/2\) ensures \(\|B_c\|_2<2\); \(c=0\) is a diagonalizable limiting case, excluded. We use discrete generation time \(n=0,1,2,\ldots\). All limits hold separately for each fixed \(c\) and every permitted initial matrix; no rate uniform as \(c\downarrow0\) is claimed.

The three scaled limits for rank-one matrices mean that \(n h_{11,n}\to3\), \(c n^2 h_{12,n}\to3\) and \(c^2n^3h_{22,n}\to3\), including complex initial rank-one matrices: the normalized off-diagonal has a real positive limit. The two eigenvalue limits are asserted only in the positive-definite case.

## Proof
**1. State invariance and rank.** For every \(H\in\mathcal D\), functional calculus gives \(0\le H(I-H)\le I/4\). Since the two singular values of \(B_c\) are \((\sqrt{c^2+4}\pm c)/2\), \(0<c<3/2\) implies \(\|B_c\|_2<2\). Hence \(0\le B_cH(I-H)B_c^*<I\). The invertibility of \(B_c\) and the equality of ranks of \(H\) and \(H(I-H)\) for \(0\le H<I\) show that the rank is preserved for all iterations.

**2. Positive-definite data and an inverse-Gramian identity.** Suppose \(0<H_0<I\), and set \(Q_n=H_n^{-1}\), \(S=B_c^{-1}=\begin{pmatrix}1&-c\\0&1\end{pmatrix}\), and \(R_n=(I-H_n)^{-1}\). The exact matrix identity
\[
 [H_n(I-H_n)]^{-1}=H_n^{-1}+(I-H_n)^{-1}
\]
 follows because \(H_n\) commutes with \(I-H_n\). Consequently
\[
 Q_{n+1}=S^*(Q_n+R_n)S,
 \quad Q_n=(S^n)^*Q_0S^n+\sum_{k=1}^n(S^k)^*R_{n-k}S^k.
\]
 Since \(R_j\ge I\), this implies \(Q_n\ge G_n=\sum_{k=1}^n(S^k)^*S^k\). Direct summation, using \(S^k=\begin{pmatrix}1&-kc\\0&1\end{pmatrix}\), gives
\[
 G_n=\begin{pmatrix}
 n&-c n(n+1)/2\\
 -c n(n+1)/2&n+c^2n(n+1)(2n+1)/6
 \end{pmatrix},
 \quad\det G_n=n^2+\frac{c^2n^2(n^2-1)}{12}.
\]
 Therefore \(\lambda_{\min}(G_n)\sim n/4\) and \(\|H_n\|_2\le\|G_n^{-1}\|_2=O(1/n)\). In particular \(R_n-I=(I-H_n)^{-1}H_n=O(1/(n+1))\) in operator norm (increase the constant to cover finitely many initial indices).

Write \(Q_n=(q_{ij,n})\). In the inverse-Gramian expansion, the initial term \((S^n)^*Q_0S^n\) has entries of orders at most \(1,n,n^2\), in positions \((11),(12),(22)\). The correction to \(G_n\) coming from \(R_{n-k}-I\) has corresponding entries bounded by constant multiples of
\[
 \sum_{k=1}^n\frac{1}{n-k+1}=O(\log(n+1)),\quad
 \sum_{k=1}^n\frac{k+1}{n-k+1}=O(n\log(n+1)),\quad
 \sum_{k=1}^n\frac{(k+1)^2}{n-k+1}=O(n^2\log(n+1)).
\]
 Thus, also for complex off-diagonal initial entries,
\[
 q_{11,n}=n+o(n),\qquad q_{12,n}=-\frac c2n^2+o(n^2),\qquad q_{22,n}=\frac{c^2}{3}n^3+o(n^3).
\]
 Their determinant satisfies \(\det Q_n=(c^2/12)n^4+o(n^4)\). Inverting the Hermitian \(2\times2\) matrix yields the three claimed limits. It also gives \(\det H_n\sim12/(c^2n^4)\). Since \(\operatorname{tr}H_n\sim4/n\), the product and sum of its eigenvalues yield the asserted eigenvalue scales.

**3. Rank-one data transverse to the eigenline.** Write \(H_0=\lambda ww^*\), with \(\|w\|=1\), \(0<\lambda<1\), and \(w_2\ne0\). Put \(v_n=B_c^nw=(w_1+ncw_2,w_2)^T\). Every iterate has the form \(H_n=\theta_n v_nv_n^*\), with \(\theta_0=\lambda\) and
\[
 \theta_{n+1}=\theta_n(1-\theta_n\|v_n\|^2).
\]
 Let \(u_n=\theta_n^{-1}\) and \(\rho_n=\theta_n\|v_n\|^2=\operatorname{tr}H_n\in(0,1)\). Then
\[
 u_{n+1}-u_n=\frac{\|v_n\|^2}{1-\rho_n}\ge\|v_n\|^2,
\]
 hence \(u_n\ge\lambda^{-1}+\sum_{j=0}^{n-1}\|v_j\|^2\sim(c^2|w_2|^2/3)n^3\). Since \(\|v_n\|^2=c^2|w_2|^2n^2+O(n)\), this lower bound implies \(\rho_n=O(1/n)\). Returning to the exact increment now gives
\[
 u_n=\lambda^{-1}+\sum_{j=0}^{n-1}\|v_j\|^2[1+O(1/(j+1))]
 =\frac{c^2|w_2|^2}{3}n^3+O(n^2\log(n+1)).
\]
 Thus \(\theta_n\sim3/(c^2|w_2|^2n^3)\). The entries of \(\theta_nv_nv_n^*\) give the three scaled limits \(3,3,3\). The rank remains one.

**4. Eigenline rank one and zero.** If \(H_0=\lambda e_1e_1^*\), then \(B_ce_1=e_1\) and \(\lambda_{n+1}=\lambda_n(1-\lambda_n)\), with \(0<\lambda_0<1\). It decreases to zero; \(\lambda_{n+1}^{-1}-\lambda_n^{-1}=1/(1-\lambda_n)\to1\), whence \(n\lambda_n\to1\) by Cesàro summation. Zero is fixed. These cases, with the preceding two, exhaust \(0\le H_0<I\), proving global convergence.

**5. Transient amplification.** For \(H_0=\varepsilon I\), \(H_1=\varepsilon(1-\varepsilon)B_cB_c^*\). Therefore \(\operatorname{tr}H_1=\varepsilon(1-\varepsilon)(2+c^2)>2\varepsilon=\operatorname{tr}H_0\) exactly when \(0<\varepsilon<c^2/(2+c^2)\). This does not contradict global convergence.

## Verification
Run the standalone standard-library checker with `python3 checker.py`. It checks the exact inverse-matrix recurrence with rational arithmetic for five steps at each of two couplings, rank preservation of two rational rank-one sample orbits for nine steps each, and the exact transient identity. Separately, 20,000-step 50-digit-decimal diagnostics for three rank classes at two couplings support the six asymptotic triples. The general \(n\to\infty\) assertions are proved by the inverse-Gramian and scalar-quotient arguments above; the finite checks are not substitutes for that proof.

## Relationship to prior work
Pawela and Życzkowski, *Matrix logistic map: fractal spectral distributions and transfer of chaos*, arXiv:2303.06176 (v1 public March 10, 2023), introduced \(H\mapsto BH(I-H)B^*\) and studied chaotic eigenvalue densities and graph-directed coupling. Their paper's graph section and two-node appendix provide the relevant self-review but do not derive the neutral Jordan extinction asymptotics or their rank-dependent amplitudes. Published results on logistic threshold networks and transverse fluctuations in another matrix-logistic regime concern different models or parameters and do not imply these constants. The proof uses the standard Gramian method, but its application to this nonlinear iteration uses a state-dependent inverse remainder and separate rank-one dynamics.

## Limitations
This is the two-node size-two Jordan slice, not a classification of arbitrary coupling matrices, higher Jordan chains, or chaotic graph networks. The constants do not claim a uniform \(c\downarrow0\) limit, and the boundary \(\|B_c\|_2=2\) is excluded. The existence of similar asymptotics in literature not located by the targeted searches remains possible. No independent audit has been performed.

## References
1. Ł. Pawela and K. Życzkowski, *Matrix logistic map: fractal spectral distributions and transfer of chaos*, arXiv:2303.06176v1, March 10, 2023, https://arxiv.org/abs/2303.06176 (original map and graph-coupled examples, especially Eq. (6), Eq. (7), and Appendix A).
2. P. Lancaster, A. C. M. Ran and L. Rodman, *An existence and monotonicity theorem for the discrete algebraic matrix Riccati equation*, Linear and Multilinear Algebra 20 (1987), 353–361, https://doi.org/10.1080/03081088708817768 (background on other matrix Riccati problems, not an asserted proof of the result above).
