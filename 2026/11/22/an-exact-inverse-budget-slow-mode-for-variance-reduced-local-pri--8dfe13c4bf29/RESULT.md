# An exact inverse-budget slow mode for variance-reduced local primal–dual quadratics

## Finding

For the local primal–dual variance-reduced finite-sum algorithm of Liu et al. [1] on one-dimensional, strictly convex component quadratics, fix a local gradient stepsize \(\alpha\) independently of the number \(\tau\) of local updates and use the algorithm's dual coefficient \(\beta=1/\tau\). If \(0<\alpha a_i<2\) at every agent, the exact linear map governing the **expectations** of the primal and dual errors has spectral radius

\[
\rho_\tau=1-\frac{\mu_*}{\tau}+o(\tau^{-1}),\qquad
\mu_* =\lambda_{\min}^{+}\!\left(T^{1/2}(I-W)T^{1/2}\right),\quad
T=\operatorname{diag}\left(\frac1{\alpha a_1},\ldots,\frac1{\alpha a_N}\right).
\]

Here \(\lambda_{\min}^{+}\) means the smallest strictly positive eigenvalue, and the spectral radius is taken on the invariant space in which the dual variables sum to zero. In particular, for all sufficiently large \(\tau\) the expectations converge, but their sharp worst-mode contraction per communication round approaches one.

This slowdown is **exact for every positive integer budget** in a genuinely stochastic two-agent, two-component example. For a mixing eigenvalue \(0<\lambda<1\), the nonzero mean primal disagreement after the first round is multiplied at each subsequent round by

\[
r_\tau=1-\frac{1-\lambda}{\tau}.
\]

Thus the communication rounds needed for any fixed relative mean-disagreement reduction scale as \(\Theta(\tau)\), and the corresponding local component-gradient evaluations per agent as \(\Theta(\tau^2)\). These are first-moment claims; no mean-square stability at a fixed \(\alpha\) is asserted.

## Assumptions and scope

Take integers \(N\ge2\), \(m_i\ge1\), and component functions \(f_{ij}(u)=\tfrac12a_{ij}(u-b_{ij})^2\) with \(a_{ij}>0\), \(b_{ij}\in\mathbb R\), and \(j=1,\ldots,m_i\). Set

\[
a_i=\frac1{m_i}\sum_j a_{ij},\qquad c_i=\frac{\sum_j a_{ij}b_{ij}}{\sum_j a_{ij}},\qquad
u_* =\frac{\sum_i a_ic_i}{\sum_i a_i}.
\]

The network mixing matrix \(W\in\mathbb R^{N\times N}\) is entrywise nonnegative, symmetric, positive definite, primitive, and doubly stochastic; its eigenvalue one is simple and the remaining eigenvalues lie strictly between zero and one. Write \(L=I-W\). Choose \(\alpha>0\) satisfying \(0<\alpha a_i<2\) for every agent, **independent of** \(\tau\in\mathbb N_+\).

At the start of each communication round \(t\), the algorithm initializes \(\phi_{i,0}=x_{i,t}\) and every gradient-table location \(z_{ij}=x_{i,t}\). For \(r=0,\ldots,\tau-1\), draw \(J_{i,r}\) conditionally uniformly from \(\{1,\ldots,m_i\}\), independently of the past given the current table, form

\[
g_{i,r}=\nabla f_{i,J_{i,r}}(\phi_{i,r})-\nabla f_{i,J_{i,r}}(z_{i,J_{i,r}})
 +\frac1{m_i}\sum_j\nabla f_{ij}(z_{ij}),
\quad \phi_{i,r+1}=\phi_{i,r}-\alpha g_{i,r}-\frac1\tau y_{i,t},
\]

and then replace \(z_{i,J_{i,r}}\) by \(\phi_{i,r+1}\). After all local steps, set \(x_{t+1}=W\phi_\tau\) and \(y_{t+1}=y_t+L\phi_\tau\), with deterministic initial \(x_0\in\mathbb R^N\) and \(y_0=0\). The randomness may be nontrivial for \(m_i\ge2\). All results concern exact arithmetic and finite matrices.

## Proof

**Conditional unbiasedness and exact mean recursion.** Conditional on the complete past immediately before sampling \(J_{i,r}\), the table-dependent negative and positive correction terms cancel in expectation. Consequently

\[
\mathbb E[g_{i,r}\mid\mathcal F_{i,r}]=a_i(\phi_{i,r}-c_i).
\]

The local gradient is affine, so taking conditional expectations given \((x_t,y_t)\) yields an *exact* scalar affine recursion, even though subsequent table entries and samples depend on past random draws. Define

\[
H_\tau=\operatorname{diag}(h_i),\quad h_i=(1-\alpha a_i)^\tau,\quad
K_\tau=\operatorname{diag}(k_i),\quad k_i=\frac{1-h_i}{\tau\alpha a_i}.
\]

Summing the geometric series of local steps gives

\[
\mathbb E[\phi_\tau\mid x_t,y_t]=H_\tau x_t+(I-H_\tau)c-K_\tau y_t.
\]

The updates of \(x_t\) and \(y_t\) are linear; therefore their unconditional means satisfy precisely the deterministic recurrence obtained by substituting this expression. The dual sum remains zero because \(\mathbf1^\top L=0\).

**Fixed point and error operator.** Let \(\bar x_* =\nu_*\mathbf1\) and \(\bar y_*=\tau\alpha\operatorname{diag}(a_i)(c-\nu_*\mathbf1)\). The latter has zero sum. Direct substitution into the conditional-mean formula gives \(\bar\phi_*=\nu_*\mathbf1\), hence \((\bar x_*,\bar y_*)\) is fixed. It is the unique fixed point with zero-sum dual: a fixed dual requires \(L\bar\phi=0\), hence \(\bar\phi\) is constant, and fixed primal then enforces the same constant. The local fixed-point equation and zero-sum dual determine that constant to be \(\nu_*\).

For centered expectation errors \(u_t=\mathbb E[x_t]-\bar x_*\) and \(v_t=\mathbb E[y_t]-\bar y_*\in\mathbf1^\perp\), the exact finite-\(\tau\) recurrence is

\[
\begin{pmatrix}u_{t+1}\\v_{t+1}\end{pmatrix}
= M_\tau\begin{pmatrix}u_t\\v_t\end{pmatrix},\qquad
M_\tau=\begin{pmatrix}
WH_\tau&-WK_\tau\\
LH_\tau&I-LK_\tau
\end{pmatrix}
\quad\text{on }\mathbb R^N\oplus\mathbf1^\perp.
\]

**Sharp slow spectrum.** Put \(q=\max_i|1-\alpha a_i|<1\), \(T=\operatorname{diag}((\alpha a_i)^{-1})\), and let \(Q\) have orthonormal columns spanning \(\mathbf1^\perp\). Uniformly in operator norm as \(\tau\to\infty\),

\[
H_\tau=O(q^\tau),\quad K_\tau=\frac{T}{\tau}+O(q^\tau/\tau),
\quad
M_\tau=\begin{pmatrix}0&0\\0&I\end{pmatrix}
+\frac1\tau\begin{pmatrix}0&-WT\\0&-LT\end{pmatrix}
+O(q^\tau)
\]

with the matrices restricted to \(\mathbb R^N\oplus\mathbf1^\perp\). The limiting matrix is a semisimple projector. Its eigenvalues near one have first-order corrections equal to the eigenvalues of \(-Q^\top LTQ\) on the dual space, while all remaining eigenvalues tend to zero. The operator \(LT\) preserves \(\mathbf1^\perp\) and is similar to the symmetric positive-semidefinite matrix \(T^{1/2}LT^{1/2}\). Its kernel is spanned by \(T^{-1}\mathbf1\), which is not in \(\mathbf1^\perp\); thus the restricted eigenvalues are precisely the strictly positive eigenvalues \(\mu_2,\ldots,\mu_N\) of \(T^{1/2}LT^{1/2}\). They are positive and real. Standard finite-dimensional perturbation of this semisimple eigenspace gives \(N-1\) slow eigenvalues \(1-\mu_j/\tau+o(\tau^{-1})\). Consequently

\[
\rho(M_\tau)=1-\mu_2/\tau+o(\tau^{-1}).
\]

In particular \(\rho(M_\tau)<1\) for sufficiently large \(\tau\). The coefficient \(\mu_2\) is exact, not merely a bound, because there is an eigenmode with that first-order rate. When the smallest positive eigenvalue is repeated, the same limit holds for the spectral radius.

**Genuinely stochastic exact witness.** Take \(N=2\), \(m_1=m_2=2\), \(\alpha=1\), \(\delta\in(0,1)\), and at each agent set

\[
f_{i,1}(u)=\frac{1+\delta}{2}(u-c_i)^2,\qquad
f_{i,2}(u)=\frac{1-\delta}{2}(u-c_i)^2,
\quad(c_1,c_2)=(1,-1).
\]

Thus \(a_1=a_2=1\) but component curvatures are unequal. Choose

\[
W=\frac12\begin{pmatrix}1+\lambda&1-\lambda\\1-\lambda&1+\lambda\end{pmatrix},
\qquad0<\lambda<1,\quad x_0=y_0=0.
\]

Because \(h_i=0\) and \(k_i=1/\tau\), the exact expected local endpoint is \(c-\mathbb E[y_t]/\tau\). The vector \(c=(1,-1)^\top\) is an eigenvector of \(W\) with eigenvalue \(\lambda\). Let \(r_\tau=1-(1-\lambda)/\tau\). Solving the resulting scalar dual recurrence gives, for every integer \(t\ge0\),

\[
\mathbb E[y_t]=\tau(1-r_\tau^t)c,\qquad
\mathbb E[x_{t+1}]=\lambda r_\tau^t c.
\]

The component sampling is not merely formal. For \(\tau=2\), starting at \(x_0=y_0=0\), the second local gradient estimator is a nonconstant signed variable conditional on the first sample, and direct enumeration yields

\[
\operatorname{Var}(\phi_{i,2})=\frac{1+\delta^2}{4}>0.
\]

Therefore the exact expectation law applies to a truly random variance-reduced method, not only an exact-gradient specialization. Since \(r_\tau\) increases strictly with \(\tau\), adding local steps strictly worsens this mean-disagreement contraction. To reduce \(\|\mathbb E[x_t]\|_2\) by a factor \(\varepsilon\in(0,1)\) relative to its value after round one requires precisely

\[
t\ge 1+\left\lceil\frac{\log\varepsilon}{\log r_\tau}\right\rceil,
\quad\text{and}\quad
\frac{\log\varepsilon}{\log r_\tau}\sim\frac{\tau}{1-\lambda}\log\frac1\varepsilon.
\]

Each round uses \(\tau\) sampled component-gradient evaluations per agent, giving the claimed quadratic local-work penalty. This finishes the proof.

## Verification

Run `python check.py` in a Python environment with NumPy. The script enumerates every stochastic sample path for two-component, within-round tables at budgets one through eight and verifies \(144\) exact-rational conditional-mean cases; it checks \(3{,}840\) exact-rational two-agent trajectory assertions; and it verifies \(960\) supplementary numerical assertions for the graph-Hessian spectral coefficient using positive-definite symmetric stochastic matrices of two, three, four and six nodes. The numerical tests do not replace the infinite-\(\tau\) proof. The proof itself uses exact algebra, affine conditional expectation and finite-dimensional eigenvalue perturbation.

## Relationship to prior work

Liu et al. [1] introduce the particular table-based variance-reduced method and analyze it at a stepsize scaling inversely with the local budget. Importantly, its exact-gradient specialization uses the same primal–dual local-update equations as Alghunaim's earlier Local Exact-Diffusion (LED) method [2] with \(\beta=1/\tau\); the basic iteration, graph mixing, zero-sum dual property and general convergence behavior are **not** claimed as new. LED's Appendix A diagonalizes a different graph-only comparison matrix, rather than deriving the exact mean error spectrum for quadratics with heterogeneous curvature and genuine SAGA-style samples. Yang, Yildirim and Feng [3] study a related but differently updated primal–dual algorithm with a different primal communication rule. Nguyen et al. [4] study local gradient tracking. The new claim is restricted to the sharp fixed-\(\alpha\) asymptotic coefficient and the exact stochastic example, not a generic assertion that local steps can be harmful.

## Limitations

The result concerns the **first moment** of a quadratic finite-sum method. It does not establish mean-square convergence, high-probability convergence, performance on nonquadratics, or a fixed-\(\alpha\) guarantee of the original stochastic convergence theorem. In particular, the quoted source's sufficient stepsizes shrink with \(\tau\); fixed \(\alpha\) does not satisfy those sufficient conditions uniformly as \(\tau\to\infty\). The exact \(\Theta(\tau^2)\) local-gradient statement is for a fixed relative reduction in the exhibited mean disagreement. Other choices of gradient and dual coefficients, accelerated consensus, and stopping criteria may have different behavior. Algebraic identities for this stochastic mean setting could have appeared in unindexed equivalent work.

## References

1. J. Liu, N. Bastianello, W. Xu and D. W. C. Ho, *Variance Reduction for Decentralized Stochastic Optimization with Multiple Local Updates*, arXiv:2610.41927, first posted 2026-10-30. https://arxiv.org/abs/2610.41927
2. S. A. Alghunaim, *Local Exact-Diffusion for Decentralized Optimization and Learning*, arXiv:2302.00620, first posted 2023-02-01. https://arxiv.org/abs/2302.00620
3. J. Yang, M. Yildirim and Q. Feng, *Accelerating Distributed Optimization: A Primal-Dual Perspective on Local Steps*, arXiv:2407.02689, first posted 2024-07-02. https://arxiv.org/abs/2407.02689
4. E. D. H. Nguyen, S. A. Alghunaim, K. Yuan and C. A. Uribe, *On the Performance of Gradient Tracking with Local Updates*, arXiv:2210.04757, first posted 2022-10-10. https://arxiv.org/abs/2210.04757
