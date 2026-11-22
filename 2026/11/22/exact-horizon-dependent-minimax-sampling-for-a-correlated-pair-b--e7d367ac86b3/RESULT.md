# Exact horizon-dependent minimax sampling for a correlated-pair block least-squares system

## Finding

For every integer \(n\ge3\), every horizon \(K\ge1\), and every \(0<\rho<1\), consider the full-rank least-squares objective
\[
f(x)=\tfrac12\|Ax\|_2^2,\qquad
A=[e_1,\ \rho e_1+\sqrt{1-\rho^2}\,e_2,\ e_3,\ldots,e_n].
\]
At each iteration, omit a single coordinate \(J\) with a fixed probability vector \(p\), independently across iterations, and exactly minimize \(f\) over all the other \(n-1\) coordinates. Define the sharp worst-initial-state expected objective retention after \(K\) updates by
\[
\mathcal R_K(p)=\sup_{x_0\ne0}\frac{\mathbb E_p f(x_K)}{f(x_0)}.
\]
Put
\[
C_K=\big[(1+\rho)(1+\rho^2)^{K-1}\big]^{1/K}.
\]
The **unique** minimizer over the entire closed probability simplex is
\[
\boxed{p_1^*=p_2^*=\frac1{2+(n-2)C_K},\qquad
p_j^*=\frac{C_K}{2+(n-2)C_K}\ (3\le j\le n),}
\]
with exact sharp minimax value
\[
\boxed{\min_p\mathcal R_K(p)=\left(\frac{C_K}{2+(n-2)C_K}\right)^K.}
\]
Thus the optimal fixed sampling law is genuinely horizon-dependent: \(C_1=1+\rho\), while \(C_K\) decreases strictly to \(1+\rho^2\) as \(K\to\infty\). In particular the optimal one-step distribution is strictly suboptimal for every \(K\ge2\), and its \(K\)-step worst-case objective retention divided by the optimum grows exponentially with \(K\).

## Assumptions and scope

The vectors \(e_j\) form the canonical basis of \(\mathbb R^n\), and the displayed \(A\) is invertible. The minimizer is \(x_*=0\); the same statement applies after translating to any exactly consistent right-hand side \(b=Ax_*\). Every candidate block has the same size \(n-1\) and is solved **exactly**. The omitted coordinate is drawn independently and identically at every step, using one distribution \(p\) that may depend on the prescribed horizon but does not adapt to current iterates. All \(p_j\ge0\) with \(\sum_jp_j=1\) are admitted. The objective ratio is the supremum of the *expected terminal loss divided by the initial loss*, not the expectation of a pathwise ratio maximized with information about the realized samples. There are no stochastic measurement errors, approximate solves, or claims about per-iteration computational work.

## Proof

**1. Exact block projections.** Work in the residual coordinate \(y=Ax\). When coordinate \(j\) is omitted, minimizing over the other coordinates orthogonally projects \(y\) onto the orthogonal complement of the span of the retained columns. These lines have unit directions
\[
v_1=-\sqrt{1-\rho^2}\,e_1+\rho e_2,\qquad
v_2=e_2,\qquad v_j=e_j\ (j\ge3).
\]
Write \(P_j=v_jv_j^{\mathsf T}\). The update is exactly \(y^+=P_jy\). Their only nonzero off-diagonal inner product is \(v_1^{\mathsf T}v_2=\rho\). Since \(A\) is invertible, taking the worst nonzero \(x_0\) is equivalent to taking the worst nonzero \(y_0\).

For a fixed sequence \((j_1,\ldots,j_K)\), the final squared norm is
\[
\|P_{j_K}\cdots P_{j_1}y_0\|_2^2
=\left[\prod_{s=1}^{K-1}(v_{j_s}^{\mathsf T}v_{j_{s+1}})^2\right](v_{j_1}^{\mathsf T}y_0)^2.
\]
Consequently \(\mathbb E\|y_K\|_2^2=y_0^{\mathsf T}M_K(p)y_0\), where \(M_K\) is positive semidefinite. Thus \(\mathcal R_K(p)=\lambda_{\max}(M_K(p))\). A sample sequence that visits both a label in \(\{1,2\}\) and a label in \(\{3,\ldots,n\}\), or visits two distinct labels at least three, contributes zero. It follows that
\[
M_K(p)=h_1P_1+h_2P_2+\sum_{j=3}^n p_j^K P_j,
\]
where, setting \(c=\rho^2\),
\[
\begin{pmatrix}h_1\\h_2\end{pmatrix}
=\operatorname{diag}(p_1,p_2)
\begin{pmatrix}p_1&cp_2\\cp_1&p_2\end{pmatrix}^{K-1}
\begin{pmatrix}1\\1\end{pmatrix}.
\]
This also holds for \(K=1\), with the zeroth matrix power interpreted as the identity. The two-dimensional correlated subspace is orthogonal to every other residual direction, so
\[
\mathcal R_K(p)=\max\left\{\lambda_{\max}(h_1P_1+h_2P_2),\ p_3^K,\ldots,p_n^K\right\}.
\]

**2. Balanced pair is globally optimal at fixed pair mass.** Fix \(t=p_1+p_2>0\), put \(q=t/2\), and write \(p_1=q(1+\delta)\), \(p_2=q(1-\delta)\) for \(-1\le\delta\le1\). The normalized bisector \(w=(v_1+v_2)/\sqrt{2(1+\rho)}\) satisfies
\[
w^{\mathsf T}(h_1P_1+h_2P_2)w=\frac{1+\rho}{2}(h_1+h_2).
\]
The sum \(h_1+h_2\) is the path partition function
\[
S_K(\delta)=q^K\sum_{\sigma\in\{-1,1\}^K}
\prod_{s=1}^K(1+\delta\sigma_s)
\prod_{s=1}^{K-1}\left[\frac{1+c}{2}\big(1+u\sigma_s\sigma_{s+1}\big)\right],
\quad u=\frac{1-c}{1+c}>0.
\]
For \(K\ge2\), expand both products and sum over all signs. Each surviving term has *even total degree in* \(\delta\) (a consequence of the sum of vertex degrees being even), with a nonnegative coefficient: a summand survives exactly when every spin has even combined incidence from selected edges and selected vertex factors. In particular, selecting the first edge and its two endpoints produces a **strictly positive** \(\delta^2u\) term. Therefore
\[
S_K(\delta)>S_K(0)=2q^K(1+c)^{K-1}\quad\text{for }\delta\ne0,\quad K\ge2.
\]
For a balanced pair, \(h_1=h_2=q^K(1+c)^{K-1}\); the largest eigenvalue of \(P_1+P_2\) is \(1+\rho\), attained at \(w\). Hence, for all \(K\ge2\), the top pair-block eigenvalue is uniquely minimized at \(p_1=p_2=q\), with value
\[
B_K(t)=(1+\rho)(1+\rho^2)^{K-1}(t/2)^K.
\]
For \(K=1\), the pair-block trace is \(t\) and determinant is \((1-\rho^2)p_1p_2\). Therefore its larger eigenvalue \(\big(t+\sqrt{t^2-4(1-\rho^2)p_1p_2}\big)/2\) is uniquely minimized by maximizing \(p_1p_2\), again at \(p_1=p_2=t/2\), giving the same displayed \(B_1(t)\). If \(t=0\), the pair block is zero and balancing is automatic.

**3. Balance the orthogonal labels and solve the scalar minimax problem.** Holding the total orthogonal probability \(1-t\) fixed, its largest individual \(K\)-step retention is at least \(((1-t)/(n-2))^K\), with equality exactly when \(p_3=\cdots=p_n=(1-t)/(n-2)\). By the preceding step the sharp global objective is bounded below by
\[
\max\left\{\big(C_Kt/2\big)^K,\ \big((1-t)/(n-2)\big)^K\right\}.
\]
The first argument increases strictly with \(t\), and the second decreases strictly. Their unique intersection is
\[
t_* = \frac{2}{2+(n-2)C_K}.
\]
The fully balanced distribution specified in the finding attains both arguments simultaneously. This proves existence, the exact optimum, and uniqueness: moving \(t\) strictly increases one of the two bounds, and at \(t=t_*\) any pair imbalance or orthogonal imbalance strictly increases the corresponding active block. No boundary distribution can give another optimum.

**4. Horizon dependence and sharp gap.** Because
\[
C_K=(1+\rho^2)\left(\frac{1+\rho}{1+\rho^2}\right)^{1/K},
\]
the sequence \(C_K\) decreases strictly from \(1+\rho\) to \(1+\rho^2\). The mapping \(C\mapsto C/[2+(n-2)C]\) is strictly increasing. Thus the optimum distribution changes strictly for every consecutive horizon, and its optimum per-step root decreases. Let \(r_1=(1+\rho)/[2+(n-2)(1+\rho)]\) and \(r_\infty=(1+\rho^2)/[2+(n-2)(1+\rho^2)]\). Under the one-step-optimal sampler, the orthogonal-mode retention is \(r_1^K\), and the pair-block retention is \(r_1^K((1+\rho^2)/(1+\rho))^{K-1}\), so the exact worst retention is \(r_1^K\). The optimal \(K\)-step retention has \(K\)-th root tending to \(r_\infty<r_1\); hence the ratio grows exponentially with base \(r_1/r_\infty>1\). This completes the proof.

## Verification

The proof covers all integer dimensions \(n\ge3\), all integer horizons \(K\ge1\), and all real \(\rho\in(0,1)\), including boundary probability vectors. The standalone `verify.py` compares explicit enumeration of the rank-one projection sequences with the independent two-by-two transfer recurrence, checks the optimizer against randomly chosen simplex distributions, directly compares projection updates with exact block least-squares solves, and checks strict suboptimality of the one-step law at later horizons. Run `python verify.py` with NumPy installed; the observed output was `VERIFY_OK 864 finite checks`. These finite computations do not substitute for the Ising-expansion positivity argument or the global minimax proof.

## Relationship to prior work

Xie and Yang, *On randomized batch-sampling coordinate descent methods for solving linear least-squares problems* (arXiv:2610.04685v1), establish the general fixed-distribution block-descent framework and upper bounds with learned sampling; their Theorem 4.1 and Remarks 4.1–4.2 optimize a convergence-bound surrogate rather than the exact terminal \(K\)-step worst-direction risk on this family. Rodomanov and Kropotov, *A Randomized Coordinate Descent Method with Volume Sampling* (arXiv:1904.04587), establish general determinant-weighted block-sampling convergence bounds, not this exact horizon-specific minimax law. Gower and Richtárik, *Randomized Iterative Methods for Linear Systems* (arXiv:1506.03296), give a general sketch-and-project framework and expected-error bounds, not this optimized finite-horizon distribution.

The previously published finding *A sharp volume-versus-uniform reversal for two-coordinate sampling on SPD stars* (identifier `e118fcf8fe26`) gives a general **one-step** minimax law when the normalized inverse Gram admits a positive sign conjugation; its general formula also recovers the \(K=1\) case here. The published finding *Exact two-regime convergence of maximal-block volume-sampled quadratic coordinate descent* (identifier `2ce7f475bd9c`) gives exact transfer dynamics under the **fixed volume law**, which motivates the present transfer matrix but does not solve the finite-horizon optimization over all fixed laws. *Exact minimax omission sampling for a frustrated three-coordinate quadratic* (identifier `aa6191d1adb5`) likewise optimizes only a one-step objective in a different signed-correlation geometry. No priority claim is made for the one-step formula or the transfer-matrix technique by themselves; the contribution is the complete all-horizon global optimizer, its uniqueness, and the horizon-induced reversal.

## Limitations

The theorem uses a canonical matrix with exactly one correlated column pair, orthogonal remaining columns, full-rank consistent least squares, exact updates over all but one coordinate, identical independent sampling, and worst-initial-direction terminal *expected objective*. It does not determine optimum laws on arbitrary dense column systems, under adaptive/nonstationary sampling, for other block sizes, for noisy systems, or for a wall-clock cost model. The asymptotic comparison concerns fixed per-step costs and the stated worst-case objective metric, not every initial state. Searches and material comparisons limit but do not eliminate historical-priority uncertainty.

## References

1. Dong-Yue Xie and Xi Yang, *On randomized batch-sampling coordinate descent methods for solving linear least-squares problems*, arXiv:2610.04685v1 (first public 2026-10-03). https://arxiv.org/abs/2610.04685
2. Anton Rodomanov and Dmitry Kropotov, *A Randomized Coordinate Descent Method with Volume Sampling*, arXiv:1904.04587 (first public 2019-04-09). https://arxiv.org/abs/1904.04587
3. Robert M. Gower and Peter Richtárik, *Randomized Iterative Methods for Linear Systems*, arXiv:1506.03296 (2015). https://arxiv.org/abs/1506.03296
4. *A sharp volume-versus-uniform reversal for two-coordinate sampling on SPD stars*, published mathematical finding `e118fcf8fe26`. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-volume-versus-uniform-reversal-for-two-coordinate-sampli--e118fcf8fe26
5. *Exact two-regime convergence of maximal-block volume-sampled quadratic coordinate descent*, published mathematical finding `2ce7f475bd9c`. https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-exact-two-regime-convergence-of-maximal-block-volume-sampled-qua--2ce7f475bd9c
6. *Exact minimax omission sampling for a frustrated three-coordinate quadratic*, published mathematical finding `aa6191d1adb5`. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-minimax-omission-sampling-for-a-frustrated-three-coordinat--aa6191d1adb5
