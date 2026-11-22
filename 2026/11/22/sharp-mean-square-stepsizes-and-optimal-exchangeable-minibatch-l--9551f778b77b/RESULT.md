# Sharp mean-square stepsizes and optimal exchangeable minibatch laws for equicorrelated quadratic descent

## Finding

Consider synchronous parallel coordinate-gradient descent on the positive-definite equicorrelation quadratic, with a new independently drawn exchangeable random subset of active coordinates at every step. **At a fixed expected number of active coordinates, the exchangeable sampling law maximizing the admissible constant stepsize for convergence in mean square is unique: use the two integer batch sizes bracketing the prescribed mean, each followed by a uniform subset of that size.** Fixed-size batches are therefore uniquely optimal when the expected batch size is an integer. The exact optimal stepsize, as well as the threshold for every other exchangeable law, follows from a two-dimensional covariance transfer formula below.

For integer \(n\ge2\), parameters \(0<c<1\), \(0<p<1\), and an exchangeable subset \(S\subseteq\{1,\ldots,n\}\) with \(\mathbb P(i\in S)=p\), write
\[
q=\mathbb P(i,j\in S)\quad(i\ne j),\qquad L=1+(n-1)c,\quad G=1+(n-2)c,\quad K=(1-c)L.
\]
The mean-square stability interval is **exactly** \(0<\eta<\eta_*(p,q)\), where
\[
\boxed{\displaystyle
\eta_*(p,q)=\frac{4p}{p+qG+\sqrt{(p+qG)^2-4pqK}}.}
\]
The formula includes \(q=0\), for which \(\eta_*=2\). At and above the boundary, at least one nonzero deterministic initial vector fails to converge in mean square. For fixed \(n,c,p\), \(\eta_*(p,q)\) is **strictly decreasing** throughout the feasible range of \(q\). In particular, the unique maximizing exchangeable sampling law has
\[
\mu=np,\quad m=\lfloor\mu\rfloor,\quad\theta=\mu-m,\qquad
\boxed{\displaystyle q_{\min}=\frac{m(m-1)+2m\theta}{n(n-1)},}
\]
with \(\mathbb P(|S|=m)=1-\theta\) and \(\mathbb P(|S|=m+1)=\theta\), conditionally uniform given size. This optimal policy strictly improves the sharp stability threshold of independent Bernoulli activations, which have \(q=p^2\), at every \(n\ge2\), \(0<c,p<1\).

A further sharp distinction is that the ceiling for nonincrease of the **one-step expected quadratic objective for every initial state** is
\[
\eta_{\rm des}=\frac{2p}{p+(n-1)cq}.
\]
There is a strict stable-but-not-universally-descending window \(\eta_{\rm des}<\eta<\eta_*\) **if and only if** \(0<q<p\). Thus, for any fixed nontrivial batch size \(2\le b\le n-1\), the optimal fixed-size law permits steps beyond the all-state one-step expected-descent bound without forfeiting mean-square convergence. At \(q=0\) and \(q=p\), the two ceilings coincide.

## Assumptions and scope

Let \(H=(1-c)I+c\mathbf1\mathbf1^{\mathsf T}\), \(f(x)=\tfrac12x^{\mathsf T}Hx\), and \(x_0\in\mathbb R^n\) deterministic. For each nonnegative integer \(k\), choose \(S_k\) independently with a common exchangeable distribution on subsets of \(\{1,\ldots,n\}\), independent of the initial vector. The random diagonal matrix \(D_k\) has entries \((D_k)_{ii}=\mathbf1_{\{i\in S_k\}}\). Use **simultaneous gradients computed from the same pre-step vector**, not sequential Gauss–Seidel gradients:
\[
x_{k+1}=(I-\eta D_kH)x_k,\qquad \eta>0.
\]
Mean-square convergence means \(\lim_{k\to\infty}\mathbb E\|x_k\|_2^2=0\). The total expected update count per iteration is \(np\); the optimization of the sampling law holds at a fixed \(p\). Exchangeability means invariance under every coordinate permutation, not merely equal one-coordinate marginals. No claim is made for nonexchangeable distributions or for temporal dependence among the masks.

The matrix \(H\) has eigenvalue \(L=1+(n-1)c\) on the all-ones direction and eigenvalue \(a=1-c\) with multiplicity \(n-1\), so it is positive definite. The permissible pairs satisfy \(0\le q\le p\); the endpoint \(q=p\) is the all-or-no-coordinates lottery, and \(q=0\) is feasible only for sufficiently small \(p\).

## Proof

**1. Exact covariance reduction.** Put \(P=\mathbf1\mathbf1^{\mathsf T}/n\), \(Q=I-P\). On the two-dimensional space of permutation-invariant symmetric covariances write \(X=rP+sQ\). For a positive semidefinite \(X\), both \(r,s\ge0\), and \(\operatorname{tr}X=r+(n-1)s\). Write \(M=I-\eta DH\) for one random step. Because \(\mathbb E D=pI\), and since \(\mathbb E[DAD]\) multiplies the diagonal of an exchangeable matrix \(A\) by \(p\) and its off-diagonal by \(q\), direct expansion of \(\mathbb E[MXM^{\mathsf T}]\) yields
\[
\begin{pmatrix}r'\\s'\end{pmatrix}=
T_\eta\begin{pmatrix}r\\s\end{pmatrix},\quad
T_\eta=\begin{pmatrix}
1-2\eta pL+\dfrac{\eta^2L^2[p+(n-1)q]}n & \dfrac{\eta^2(n-1)a^2(p-q)}n\\[6pt]
\dfrac{\eta^2L^2(p-q)}n &1-2\eta pa+\dfrac{\eta^2a^2[(n-1)p+q]}n
\end{pmatrix}.
\]
Every entry of \(T_\eta\) is nonnegative: apply the covariance operator separately to \(P\) and \(Q\), both positive semidefinite. When \(q<p\) and \(\eta>0\), its off-diagonal entries are strictly positive. At \(q=p\), it is diagonal.

For an arbitrary deterministic \(x_0\), symmetrize \(x_0x_0^{\mathsf T}\) by averaging over coordinate permutations. The random covariance evolution commutes with every coordinate permutation; trace is invariant under these permutations. Hence its expected squared Euclidean norm after **every** step equals \(r_k+(n-1)s_k\), with \((r_k,s_k)^{\mathsf T}=T_\eta^k(r_0,s_0)^{\mathsf T}\) and both initial components nonnegative. Conversely, a nonnegative Perron eigenvector of \(T_\eta\) determines an exchangeable positive semidefinite covariance; as a mixture of deterministic rank-one covariances, failure of its second moment to decay implies failure for some deterministic initial vector. Therefore convergence for all deterministic initial vectors is equivalent to \(\rho(T_\eta)<1\), including the reducible case \(q=p\). Rank-one symmetric covariances linearly span all real symmetric matrices, so this all-initial-vector convergence also implies spectral stability of the full covariance operator on that finite-dimensional space. Equivalently, in the irreducible case \(q<p\), the deterministic all-ones initial vector already detects nondecay when \(\rho(T_\eta)\ge1\).

**2. Exact boundary and absence of reentry.** Direct multiplication, with \(K=(1-c)L>0\), gives the factorization
\[
\det(I-T_\eta)=p\eta^2K F(\eta),\qquad
F(\eta)=4p-2(p+qG)\eta+qK\eta^2.
\]
At small positive \(\eta\), mean-square convergence holds. Indeed,
\[
\mathbb E[M^{\mathsf T}HM]-H
=\eta H\bigl[-2pI+\eta((p-q)I+qH)\bigr]H,
\]
which is strictly negative definite for \(0<\eta<2p/[p+(n-1)cq]\). This supplies a uniform geometric expected-objective contraction.

If \(q>0\), then \(F(0)=4p>0\) and
\[
F(2)=-4q(n-1)c^2<0.
\]
Since \(F\) is an upward quadratic, it has exactly two positive simple roots, one in \((0,2)\) and the other in \((2,\infty)\). Its smaller root is exactly the displayed \(\eta_*(p,q)\), by rationalizing the quadratic formula. If \(q=0\), \(F(\eta)=2p(2-\eta)\) and the sole positive root is \(2\). Continuity of the spectral radius, positivity of \(T_\eta\), and the absence of earlier zeros of \(\det(I-T_\eta)\) show that \(\rho(T_\eta)<1\) below the first root and equals one at that root.

To rule out any spurious later stability window, let \(\mathcal L_\eta(X)=\mathbb E[(I-\eta DH)X(I-\eta HD)]\) on symmetric matrices. If \(\mathcal L_{\eta_0}\) is mean-square stable, its adjoint has a positive-definite Lyapunov certificate \(W\), e.g.
\[
W=\sum_{j=0}^{\infty}(\mathcal L_{\eta_0}^*)^j(I),\quad
\mathcal L_{\eta_0}^*(W)-W=-I.
\]
For every \(0<\eta<\eta_0\), expansion of the quadratic dependence on step size yields
\[
\mathcal L_\eta^*(W)-W=\frac{\eta}{\eta_0}[\mathcal L_{\eta_0}^*(W)-W]
-\eta(\eta_0-\eta)\,\mathbb E[(DH)^{\mathsf T}W(DH)]\prec0.
\]
Thus the stable step-size set is downward closed. No step above the first root is stable. This proves the complete sharp interval, including both boundaries, without mistaking the larger determinant root for renewed convergence.

**3. Optimize the sampling law.** For \(q>0\), its boundary lies strictly below \(2\). On \(0<\eta\le2\),
\[
\frac{\partial F}{\partial q}=-2G\eta+K\eta^2
\le-2\eta(G-K)=-2\eta(n-1)c^2<0.
\]
Increasing \(q\) therefore decreases the first positive root strictly; this also applies when comparing against \(q=0\), whose root is \(2\). Now let \(B=|S|\), an integer-valued random variable of mean \(\mu=np\). By exchangeability,
\[
q=\frac{\mathbb E[B(B-1)]}{n(n-1)}.
\]
Write \(m=\lfloor\mu\rfloor\) and \(\theta=\mu-m\). Since every integer \(b\) satisfies \((b-m)(b-m-1)\ge0\), taking expectation gives
\[
\mathbb E[B(B-1)]\ge m(m-1)+2m\theta.
\]
Equality is possible **only** when \(B\in\{m,m+1\}\) almost surely. The mean condition then forces probabilities \(1-\theta,\theta\), respectively. Exchangeability uniquely fixes the conditional distribution to be uniform among all subsets of each selected size. Hence the claimed optimizer is unique within the specified class. Independent Bernoulli masks have \(B\sim\mathrm{Binomial}(n,p)\), with support on at least three values for \(n\ge2\), \(0<p<1\), and thus strictly larger \(q=p^2>q_{\min}\). Strict gain improvement follows.

**4. Expected descent comparison.** Because \(\mathbb E[DHD]=(p-q)I+qH\), the matrix inequality in Step 2 is nonpositive exactly when \(\eta\le\eta_{\rm des}\). Along the all-ones eigendirection it becomes positive for any larger \(\eta\), proving sharpness. Substitution gives
\[
F(\eta_{\rm des})=
\frac{4c(1-c)(n-1)pq(p-q)}{[p+(n-1)cq]^2}.
\]
This is strictly positive exactly when \(0<q<p\). Since \(\eta_{\rm des}\le2\), it lies strictly before the first positive root precisely in that case. For \(q=0\) or \(q=p\), the numerator vanishes and the two limits agree. This establishes the exact stable-but-initially-nondescent criterion.

**5. A concrete and a sharp limiting separation.** With \(n=4\), \(c=p=1/2\), the uniquely optimal uniform two-coordinate batch has \(q=1/6\) and
\[
\eta_*=\frac{12}{5+\sqrt{10}}=1.470177871865\ldots,
\qquad\eta_{\rm des}=\frac43.
\]
Independent Bernoulli activation at the same marginal and expected work has \(q=1/4\) and \(\eta_*=1.240408205773\ldots\), a strictly smaller stability ceiling. More sharply, at \(p=1/n\), the unique optimum chooses exactly one coordinate per step and has \(\eta_*=2\) for every \(c<1\). As \(c\uparrow1\), the independent-Bernoulli ceiling tends to \(2n/(2n-1)\), giving a sharp optimal-to-Bernoulli gain ratio tending to \(2-1/n\); subsequently letting \(n\to\infty\) gives factor \(2\). These are ordered limiting statements; no assertion is made at singular \(c=1\).

## Verification

The standalone program `verify.py` (run with `python verify.py` after installing packages from `requirements.txt`) verifies the exact symbolic determinant and descent identities, independently reconstructs the expected covariance transfer by enumeration of **all subsets** for sizes \(n=2,3,4\), both selected rational correlation parameters and three rational step sizes, and tests the sharp roots, batch-size optimizer and Bernoulli comparison across a larger finite parameter grid. The successful execution produced `PASS 2241 exact symbolic / rational-mask / numerical assertions`. These checks validate the formulas and finite examples; the proof above, not finite enumeration, establishes the statements for all permitted dimensions and parameters.

## Relationship to prior work

The sampling-probability-matrix and ESO formalism for arbitrary-sampling coordinate descent is established in Hanzely and Richtárik (2018); their full HTML paper includes the standard uniformly fixed-size batch and a sufficient expected-descent-type stepsize/rate in Section 2 and the nonaccelerated analysis in Appendix B. That does **not** state the necessary-and-sufficient mean-square stability interval or optimize that interval over all exchangeable laws of a fixed expected size. The earlier synchronous arbitrary-subset NSync algorithm of Richtárik and Takáč (public since 2013, journal 2015/2016) also establishes sampling optimization of a **sufficient complexity bound**, not a necessary-and-sufficient mean-square stability ceiling. General expected-smoothness sampling bounds from Gower et al. (2019) are likewise sufficient convergence guarantees, not the exact spectral-radius boundary for synchronous coordinate masks on this equicorrelated Hessian.

The special case of independent Bernoulli masks, \(q=p^2\), has already been worked out as a sharp mean-square stability and descent-gap statement; its recovery here is a **consistency check and is not claimed as a new discovery**. A separate published four-coordinate, fixed-size-two coupling result discusses finite-horizon Euclidean risk and state-dependent objective optimization over balanced couplings. Its reported findings do not imply the all-dimensional sharp stability formula or the unique all-exchangeable fixed-work sampling optimizer. The complete full text of that particular record was not accessible for this comparison; see the specified residual risk in `AUDIT.json`. The new contribution assessed here is the exact **optimization over all exchangeable minibatch laws**, including random batch sizes, combined with the all-law sharp stability condition and the strict independent-sampling comparison.

## Limitations

This concerns the fixed equicorrelated strongly convex quadratic, uniform coordinate marginals, i.i.d. exchangeable sampling across steps, and simultaneous unnormalized coordinate-gradient updates. It does not cover nonsymmetric Hessians, nonexchangeable sampling, momentum, stale gradients, state-dependent sampling, nonquadratic losses, or finite-precision effects. The stability optimum maximizes the feasible stepsize, not necessarily the convergence rate at a prescribed stepsize or the wall-clock complexity. Prior-work searches cannot certify global historical priority; the nearest published fixed-size coupling record has only summary-level material accessible here. No independent mathematical audit was performed.

## References

1. F. Hanzely and P. Richtárik, *Accelerated Coordinate Descent with Arbitrary Sampling and Best Rates for Minibatches*, arXiv:1809.09354 (first public September 25, 2018), especially Section 2 and Appendix B. https://arxiv.org/html/1809.09354v2
2. R. M. Gower, N. Loizou, X. Qian, A. Sailanbayev, E. Shulgin and P. Richtárik, *SGD: General Analysis and Improved Rates*, PMLR 97, 2019, especially Sections 3.1–3.3. https://proceedings.mlr.press/v97/qian19b.html
3. *Exact coupling-invariant Euclidean risk and state-dependent batch-optimal objective in four-coordinate descent*, published-finding corpus record dated October 12, 2026, identifier `2026/10/12/SCOPE-exact-coupling-invariant-euclidean-risk-and-state-dependent-batc--da850d87df4f` (accessible abstract/summary only).
4. P. Richtárik and M. Takáč, *On optimal probabilities in stochastic coordinate descent methods*, *Optimization Letters* (first public preprint October 2013, article first online July 2, 2015). https://link.springer.com/article/10.1007/s11590-015-0916-1
5. *Sharp mean-square stability beyond expected descent for Bernoulli parallel coordinate updates*, prior specialized statement, identifier `ca6b551f-e80d-464d-b46e-ba6184a0bcfd` (independent-activation special case).
