# Sharp mean-square stability beyond expected descent for Bernoulli parallel coordinate updates

## Finding
For every integer \(n\ge2\), every \(0<c<1\) and every activation probability \(0<p<1\), consider the positive-definite equicorrelation Hessian
\[
H=(1-c)I_n+c\mathbf1\mathbf1^{\mathsf T},\qquad f(x)=\frac12x^{\mathsf T}Hx.
\]
A common positive stepsize \(\eta\) is used for independent, simultaneously active coordinates, with every partial gradient evaluated at the *same pre-update vector*:
\[
x_{k+1}=\bigl(I_n-\eta D_kH\bigr)x_k,\qquad D_k=\operatorname{diag}(B_{k1},\ldots,B_{kn}),
\]
where the \(B_{ki}\) are all independent Bernoulli random variables with \(\mathbb P(B_{ki}=1)=p\). Empty updates are permitted. The following are equivalent:

1. \(\mathbb E\lVert x_k\rVert_2^2\to0\) for *every* deterministic \(x_0\in\mathbb R^n\).
2. The convergence in item 1 is exponentially fast for every deterministic \(x_0\).
3. The stepsize satisfies \(0<\eta<\eta_*\), where
\[
\boxed{\eta_*=\frac4{S+\sqrt{S^2-4pK}},\qquad S=1+p+p(n-2)c,\quad K=(1-c)(1+(n-1)c).}
\]

At \(\eta\ge\eta_*\) there exists a deterministic coordinate-vector initial state whose expected squared error fails to tend to zero. Let \(W=1+p(n-1)c\). The exact ceiling for *one-step expected objective nonincrease for all deterministic states* is \(\eta_{\mathrm{des}}=2/W\); the strict separation
\[
\boxed{\frac2W<\eta_*<2}
\]
holds throughout the displayed domain. Above \(2/W\), the all-ones starting state has strictly larger expected objective after one step, even when the entire process is mean-square convergent. The critical \(\eta_*\) strictly decreases when \(p\) or \(c\) increases, and strictly decreases on increasing integer dimension \(n\).

For instance, with \(n=3\), \(p=c=1/2\), the descent ceiling is \(4/3\), whereas the mean-square ceiling is \((7-\sqrt{17})/2=1.43844718719\ldots\). At \(\eta=7/5\), the two-moment spectral radius is \(0.93669165305\ldots<1\), but the expected objective after one update from \(x_0=\mathbf1\) is \(57/50\) times the initial objective.

## Assumptions and scope
The domain is exactly \(n\in\{2,3,\ldots\}\), \(0<c<1\), \(0<p<1\), \(\eta>0\). Coordinates are sampled independently both across coordinates and across steps, with common probability \(p\). All selected gradients use the pre-update iterate; this is a Jacobi-style parallel update, not a sequential or stale-read scheme. The Hessian's diagonal entries are one. Its two positive eigenvalues are \(a=1-c\) (multiplicity \(n-1\)) and \(L=1+(n-1)c\) (multiplicity one). The criterion is for unconditional expected squared Euclidean error from *every deterministic initial vector*; it is not a one-step monotonicity condition.

## Proof
Write \(J=\mathbf1\mathbf1^{\mathsf T}\), \(U=J/n\), and \(T=I-U\). These are orthogonal projectors. The covariance transfer \(\mathcal T(C)=\mathbb E[(I-\eta DH)C(I-\eta HD)]\) preserves the two-dimensional permutation-invariant subspace \(C=uT+vU\). Directly using \(\mathbb E B_i=p\) and \(\mathbb E B_iB_j=p^2\) for \(i\ne j\) yields
\[
\binom{u'}{v'}=A\binom uv,\quad
A=\begin{pmatrix}
1-2\eta pa+\eta^2pa^2(n-1+p)/n &\eta^2L^2p(1-p)/n\\
\eta^2a^2(n-1)p(1-p)/n &(1-\eta pL)^2+\eta^2L^2p(1-p)/n
\end{pmatrix}.
\]
Both off-diagonal entries are strictly positive. Both diagonal entries are nonnegative, since they are variances of projected random updates. Thus \(A\) is an irreducible nonnegative matrix, and its Perron root controls all positive invariant covariances.

For a deterministic state \(x_0\), its initial covariance satisfies \(x_0x_0^{\mathsf T}\preceq\lVert x_0\rVert_2^2 I\). Since \(\mathcal T\) preserves the positive semidefinite cone, \(\mathbb E\lVert x_k\rVert_2^2\le\lVert x_0\rVert_2^2\operatorname{tr}\mathcal T^k(I)\). Hence \(\rho(A)<1\) suffices for universal mean-square convergence. Conversely, if \(\rho(A)\ge1\), the strictly positive Perron covector and \(I=(n-1)T+U\) imply \(\operatorname{tr}\mathcal T^k(I)\not\to0\). But this trace equals the sum of the expected squared norms from the deterministic coordinate basis starts. By permutation invariance all those summands are equal; therefore each coordinate basis start fails to converge in mean square. This establishes necessity.

An exact two-by-two determinant factorization is
\[
\det(I_2-A)=p^2\eta^2K F(\eta),\qquad F(\eta)=4-2S\eta+pK\eta^2.
\]
Here \(S^2>4pK\), as follows from \(F(0)>0\) and \(F(2)<0\). More explicitly,
\[
F(0)=4,\qquad F(2)=-4p(n-1)c^2<0.
\]
Consequently the first positive root \(\eta_*\) of \(F\) lies in \((0,2)\), and the second lies strictly above two. At small positive \(\eta\), the Perron root of \(A\) is below one: indeed the mean drift at first order is the positive-definite operator \(-2pH\). At the first root of \(F\), Perron continuity gives \(\rho(A)=1\). Between the two roots, \(\det(I-A)<0\), so the two real eigenvalues straddle one and \(\rho(A)>1\). To exclude any larger reentrant stable interval: for each diagonal entry of \(A\), its quadratic dependence on \(\eta\) begins at one with a strictly negative derivative and subsequently crosses one exactly once on the positive axis. At its first such crossing, \(\det(I-A)=-A_{12}A_{21}<0\), so that crossing must occur strictly between the first and second roots of \(F\). Beyond it, this diagonal entry is at least one, implying \(\rho(A)\ge1\) by nonnegative-matrix comparison. This proves the complete sharp interval and its endpoints.

For expected *one-step* objective descent, the Bernoulli identities imply
\[
\mathbb E[DHD]=p(1-p)I+p^2H.
\]
Writing \(g=Hx\), direct expansion gives
\[
\mathbb E[f(x_{k+1})\mid x_k=x]-f(x)
=\frac{\eta p}{2}g^{\mathsf T}\bigl[\eta((1-p)I+pH)-2I\bigr]g.
\]
As \(H\) is invertible, this expression is nonpositive for every state exactly when \(\eta\le2/W\), where \(W=1+p(n-1)c\). Strict separation follows algebraically from
\[
F(2/W)=\frac{4(n-1)c(1-c)p(1-p)}{W^2}>0,
\]
because the other positive root of \(F\) lies above two and \(2/W<2\). For \(\eta>2/W\), choosing \(x=\mathbf1\) makes the displayed expected objective difference strictly positive.

Finally, for \(0<\eta<2\), the parameter derivatives of \(F\) satisfy
\[
\partial_p F=\eta[-2(1+(n-2)c)+\eta K]<0,
\]
\[
\partial_c F=p\eta[(n-2)(\eta-2)-2\eta(n-1)c]<0,
\]
\[
\partial_n F=p\eta c[\eta(1-c)-2]<0.
\]
The first inequality uses \(K=1+(n-2)c-(n-1)c^2\). At the smaller simple positive root, \(\partial_\eta F<0\). Implicit differentiation therefore shows strict decrease of \(\eta_*\) in each parameter, treating \(n\) as real temporarily and then restricting back to integers. All inequalities are strict on the stated open domain.

## Verification
Run `python verify.py` with Python 3 and SymPy installed, using `requirements.txt` if dependency setup is needed. It checks the determinant factorization, the boundary and separation identities, and monotonicity derivatives symbolically. It then enumerates all \(2^n\) update masks with exact rational arithmetic for \(72\) parameter cases with \(n\in\{2,3,4,5\}\) and compares the complete covariance transfer against the analytic matrix. An additional \(360\) parameter/stepsize cases independently recompute the Perron root on each side of the claimed threshold. These finite checks corroborate, but do not replace, the all-dimension analytic argument above.

## Relationship to prior work
Salzo and Villa (2019, arXiv:1906.07392) analyze parallel random block-coordinate forward-backward optimization, use expected separable overapproximation, and prove convergence under sufficient stepsize hypotheses. Their specified sampling excludes an empty block, unlike the unconditioned Bernoulli model here; conditioning out empty masks only rescales the nontrivial update probability and does not change this model's stability boundary. Hanzely and Richtárik (2018, arXiv:1809.09354) study arbitrary-sampling accelerated and minibatch coordinate descent using ESO bounds, without the exact two-moment all-initialization threshold established here. Di Giovacchino, Higham and Zygalakis (2023, arXiv:2309.02082), Theorem 4.8, establish sufficient mean-square conditions for a **modified continuous-time SDE** with single-coordinate sampling, rather than a necessary-and-sufficient discrete parallel-mask criterion. The stochastic-matrix second-moment spectral-radius method is standard and is not asserted as new. The contribution is the sharp closed-form global threshold and its strict separation from one-step expected objective descent across all dimensions and parameters in this natural family.

## Limitations
The result does not address general correlated Hessians, unequal activation probabilities, varying gain, gradient noise, gradient staleness, finite-budget optimization, or almost-sure convergence thresholds. The strict inequalities assume \(0<c,p<1\); limiting parameter cases may have reduced irreducibility or non-unique modes. The proof gives a sharp asymptotic mean-square criterion, not monotonicity or finite-horizon superiority. Historical priority remains provisional pending independent literature review.

## References
1. S. Salzo and S. Villa, *Parallel Random Block-Coordinate Forward-Backward Algorithm: A Unified Convergence Analysis*, first arXiv posting 2019-06-18, https://arxiv.org/abs/1906.07392.
2. F. Hanzely and P. Richtárik, *Accelerated Coordinate Descent with Arbitrary Sampling and Best Rates for Minibatches*, first arXiv posting 2018-09-25, https://arxiv.org/abs/1809.09354.
3. S. Di Giovacchino, D. J. Higham and K. Zygalakis, *Backward error analysis and the qualitative behaviour of stochastic optimization algorithms: Application to stochastic coordinate descent*, first arXiv posting 2023-09-05, https://arxiv.org/abs/2309.02082.
