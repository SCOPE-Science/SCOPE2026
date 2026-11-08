# A quarter-delay phase transition for sharp mean-square stability of momentum with stale gradients

## Finding

Consider a scalar strongly convex quadratic and classical constant-step heavy-ball updates where the gradient used at each iteration is independently either current or one step stale. For a delayed-gradient probability \(p\in(0,1)\), nonnegative momentum \(\beta\in[0,1)\), and normalized stepsize \(h>0\), **mean-square convergence for every deterministic pair of starting errors holds exactly when**
\[
F_p(h,\beta):=ph^2+[1+(4p-1)\beta]h+2\beta^2-2<0.
\]
For every fixed \(p,\beta\), the stability interval is \(0<h<H_p(\beta)\), with its exact endpoint
\[
H_p(\beta)=\frac{4(1-\beta^2)}{1+(4p-1)\beta+\sqrt{[1+(4p-1)\beta]^2+8p(1-\beta^2)}}.
\]
The **unique momentum maximizing the admissible stepsize supremum** is
\[
\beta_*(p)=\begin{cases}
\dfrac{1-4p}{1+4\sqrt{p(1-p)}},&0<p<1/4,\\
0,&1/4\le p<1,
\end{cases}
\]
and the corresponding sharp ceiling is
\[
H_*(p)=\sup_{0\le\beta<1}H_p(\beta)
=\begin{cases}
\dfrac{4}{1+4\sqrt{p(1-p)}},&0<p<1/4,\\
\dfrac{4}{1+\sqrt{1+8p}},&1/4\le p<1.
\end{cases}
\]
Thus positive momentum strictly enlarges the maximum stable stepsize precisely when the probability of a stale gradient is below \(1/4\); at or above this probability zero momentum is uniquely optimal for this criterion. The endpoint is a supremum, never a stable stepsize.

For example, with \(p=1/10\) and \(h=7/4\), no-momentum updates are mean-square unstable, while momentum \(\beta=3/11\) is mean-square stable. The exact signs are \(F_{1/10}(7/4,0)=9/160>0\) and \(F_{1/10}(7/4,3/11)=-315/3872<0\).

## Assumptions and scope

Fix a curvature \(a>0\), and set \(f(x)=ax^2/2\), with minimizer zero. Let \(D_k\in\{0,1\}\) be independent identically distributed random variables, independent of deterministic starting values, with \(\Pr(D_k=1)=p\in(0,1)\). Let \(\eta>0\), \(h=\eta a\), and \(0\le\beta<1\). The iteration is exactly
\[
x_{k+1}=x_k+\beta(x_k-x_{k-1})-\eta f'(x_{k-D_k})
=(1+\beta)x_k-\beta x_{k-1}-h x_{k-D_k},\quad k\ge0.
\]
The two initial values \(x_{-1},x_0\in\mathbb R\) are arbitrary and deterministic. Mean-square stability means \(\mathbb E x_k^2\to0\) as \(k\to\infty\) for **every** such initial pair. No additive gradient noise, varying learning rate, correlation across delays, or multivariate Hessian is assumed. The comparison optimizes the stepsize stability **ceiling**, not the spectral convergence rate at a fixed step.

## Proof

**1. Exact second-moment recurrence.** Introduce \(z_k=(x_k,x_{k-1})^{\mathsf T}\) and two real matrices
\[
A_0=\begin{pmatrix}1+\beta-h&-\beta\\1&0\end{pmatrix},\qquad
A_1=\begin{pmatrix}1+\beta&-\beta-h\\1&0\end{pmatrix}.
\]
Independence of \(D_k\) from the past gives the positive linear map on real symmetric matrices
\[
\Phi(X)=(1-p)A_0XA_0^{\mathsf T}+pA_1XA_1^{\mathsf T},\quad
\mathbb E[z_{k+1}z_{k+1}^{\mathsf T}]=\Phi(\mathbb E[z_kz_k^{\mathsf T}]).
\]
In coordinates \(X=\begin{psmallmatrix}u&v\\v&w\end{psmallmatrix}\), the matrix of \(\Phi\) is
\[
L=\begin{pmatrix}
(1-p)(1+\beta-h)^2+p(1+\beta)^2&
-2(1-p)\beta(1+\beta-h)-2p(1+\beta)(\beta+h)&
(1-p)\beta^2+p(\beta+h)^2\\
1+\beta-(1-p)h&-\beta-ph&0\\
1&0&0
\end{pmatrix}.
\]
Direct expansion gives the exact determinant factorization
\[
\det(I_3-L)=-h\{ph^2+[1+(4p-1)\beta]h+2\beta^2-2\}=-hF_p(h,\beta).
\]
These identities can be independently reconstructed using the embedded symbolic checker.

**2. This determinant gives the complete stability boundary, not merely a necessary condition.** A positive linear map preserving the finite-dimensional cone of positive-semidefinite matrices has a real nonnegative eigenvalue equal to its spectral radius, with an eigenmatrix in that cone (the elementary finite-dimensional Perron theorem for proper cones). Consequently \(\rho(L)=1\) implies \(\det(I_3-L)=0\). At \(h=0\), the moment eigenvalues are \(1,\beta,\beta^2\); the first is simple, with right eigenvector \(r=(1,1,1)^{\mathsf T}\) and left eigenvector \(\ell=(1,-2\beta,\beta^2)^{\mathsf T}/(1-\beta)^2\) normalized so that \(\ell^{\mathsf T}r=1\). Direct differentiation gives \(L_h(0)r=(-2,-1,0)^{\mathsf T}\). Thus the derivative of this simple eigenvalue is \(\ell^{\mathsf T}L_h(0)r=-2/(1-\beta)\). The other eigenvalues have modulus below one at zero, so \(\rho(L)<1\) for all sufficiently small positive \(h\).

For sufficiently large \(h\), \(\rho(L)>1\). Indeed, with probability \((1-p)^k\) the next \(k\) updates all choose \(A_0\). Choosing a real eigenvector of \(A_0\) for its large-modulus real eigenvalue yields an expected squared norm at least \((1-p)^k|\lambda_{\max}(A_0)|^{2k}\) times the starting norm; the base exceeds one when \(h\) is large. Thus the moment operator cannot be stable for all positive \(h\).

For \(0<p<1\), \(0\le\beta<1\), the polynomial \(F_p(h,\beta)\) satisfies \(F_p(0,\beta)=2\beta^2-2<0\) and
\[
\frac{\partial F_p}{\partial h}=1+(4p-1)\beta+2ph>0.
\]
Therefore it has exactly one positive root \(H_p(\beta)\), given above by the quadratic formula. By continuity of \(\rho(L)\), the preceding small- and large-stepsize facts, and the implication \(\rho(L)=1\Rightarrow F_p=0\), the spectral radius lies below one exactly before this root, equals one at the root, and exceeds one afterward. Finally, \(\rho(L)<1\) is equivalent to second-moment convergence for all deterministic starts. For the reverse direction, every positive-semidefinite initial covariance is a finite nonnegative sum of rank-one deterministic-start covariances; hence if all such starts decayed, every power of \(\Phi\) would tend to zero. This rules out a Perron eigenvalue of magnitude at least one.

**3. Optimize over momentum.** At a fixed positive \(h\), the function \(F_p(h,\beta)\) is strictly convex in \(\beta\), with
\[
\frac{\partial F_p}{\partial\beta}=4\beta+(4p-1)h.
\]
If \(p\ge1/4\), the unique minimum over \(\beta\in[0,1)\) occurs at \(\beta=0\). Its zero gives the claimed \(H_*(p)=4/(1+\sqrt{1+8p})\). If \(0<p<1/4\), take
\[
\widehat h=\frac4{1+4\sqrt{p(1-p)}},\qquad
\widehat\beta=\frac{1-4p}{1+4\sqrt{p(1-p)}}\in(0,1).
\]
Substitution shows \(F_p(\widehat h,\widehat\beta)=0\) and \(\partial_\beta F_p(\widehat h,\widehat\beta)=0\). Strict convexity then implies \(F_p(\widehat h,\beta)\ge0\), with equality only at \(\widehat\beta\). As \(F_p\) is strictly increasing in \(h\) at every admissible momentum, no momentum stabilizes any \(h\ge\widehat h\); every smaller positive step is stable at \(\widehat\beta\). This proves the sharp ceiling and its unique maximizing momentum. The strict phase transition at \(p=1/4\) follows.

## Verification

Run `python verify.py` with Python 3, SymPy and NumPy. It reconstructs both update matrices and the exact moment lift, checks \(\det(I_3-L)=-hF_p\) symbolically, verifies boundary specializations and optimizing substitutions, checks the exact rational example, and compares numeric moment spectral radii against the predicted phase boundary for a deterministic parameter grid. All executable assertions passed. The proof above, rather than finite tests, establishes the theorem for the full continuum of parameters.

## Relationship to prior work

Arjevani, Shamir and Srebro (2018) analyze SGD with **fixed** delayed gradients on quadratics and derive finite-time convergence bounds using generating functions, without this randomly fresh/stale momentum phase diagram. Cohen and collaborators (2021) address arbitrary delays with a **skip-if-stale** algorithm and general nonconvex guarantees, rather than this fixed heavy-ball recurrence. Pan and collaborators (2023) analyze heavy-ball momentum with **step-decay schedules and anisotropic noise**, not independently Bernoulli-selected one-step stale gradients. Su, Li and Lu (2021) give a general networked-control mean-square criterion for random **packet arrival times** where each message is received at most once; that transmission model differs from independently choosing a fresh or stale stored iterate at each update. These contrasts are comparisons of actual update rules and guarantees, not assertions that a keyword search proves novelty.

The \(\beta=0\) subcase is the familiar scalar two-choice stale-gradient frontier \(h+ph^2<2\); the claim of interest is the joint \((p,\beta,h)\) exact classification and the unique, sharp momentum phase transition. General lifted-moment spectral-radius criteria are classical and not claimed as original.

## Limitations

Only scalar deterministic quadratic curvature, iid Bernoulli one-step **read staleness**, standard unscaled heavy-ball momentum and mean-square convergence from all deterministic initial pairs are covered. A larger allowable stable stepsize is not the same thing as a faster actual rate. The result neither extends to packet-arrival queues nor to all asynchronous implementations without further argument. Independent mathematical checking and a fully exhaustive publication-precedence review have not been performed; earlier equivalent formulations in stochastic linear-system stability literature remain a risk.

## References

1. Y. Arjevani, O. Shamir and N. Srebro, *A Tight Convergence Analysis for Stochastic Gradient Descent with Delayed Updates*, first public arXiv posting 2018-06-26, https://arxiv.org/abs/1806.10188.
2. A. Cohen, A. Daniely, Y. Drori, T. Koren and M. Schain, *Asynchronous Stochastic Optimization Robust to Arbitrary Delays*, first public arXiv posting 2021-06-22, https://arxiv.org/abs/2106.11879.
3. W. Su, J. Li and J. Lu, *Mean-Square Input-Output Stability and Stabilizability of a Networked Control System with Random Channel Induced Delays*, arXiv posting 2021-08-29, https://arxiv.org/abs/2108.12795.
4. R. Pan, Y. Liu, X. Wang and T. Zhang, *Accelerated Convergence of Stochastic Heavy Ball Method under Anisotropic Gradient Noise*, first public arXiv posting 2023-12-22, https://arxiv.org/abs/2312.14567.
