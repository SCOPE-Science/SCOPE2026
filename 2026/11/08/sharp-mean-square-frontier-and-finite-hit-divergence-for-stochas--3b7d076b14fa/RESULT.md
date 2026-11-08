# Sharp mean-square frontier and finite-hit divergence for stochastic reflected gradients

## Finding

The fixed-step, one-oracle reflected-gradient iteration on a scalar strongly convex quadratic has an exact, distribution-independent **second-moment stability frontier**. Let \(U_n\) be independent, identically distributed, square-integrable real random variables with \(m=\mathbb E U_n>0\) and \(v=\mathbb E U_n^2\). For deterministic finite initial values \(x_{-1},x_0\), set
\[
x_{n+1}=x_n-hU_n(2x_n-x_{n-1}),\qquad h>0.
\]
Convergence \(\mathbb E(x_n^2+x_{n-1}^2)\to0\) for **every** deterministic initialization holds if and only if
\[
\boxed{v h(1+3mh)<2m.}
\]
At equality there is a deterministic initialization with non-decaying second moment; above equality there is an initialization with unbounded second moment. Equivalently, writing \(t=hm\) and \(\nu=v/m^2\), the exact stability domain is \(\nu(t+3t^2)<2\), with step ceiling
\[
\boxed{h_*=\frac{\sqrt{1+24/\nu}-1}{6m}.}
\]
Only the first two oracle moments enter this criterion, with no assumption on higher moments.

The same scheme can **terminate exactly in finite time almost surely while its mean squared error diverges exponentially**. Specifically, choose \(\mathbb P(U_n=0)=\mathbb P(U_n=2m)=1/2\), \(h=1/(2m)\), and \((x_{-1},x_0)=(0,1)\). Then, with \(\lambda_\pm=(1\pm\sqrt3)/2\),
\[
\boxed{\mathbb E x_n^2=\frac{\lambda_+^{\,n+1}-\lambda_-^{\,n+1}}{\sqrt3}\longrightarrow+\infty,\qquad x_n=0\text{ eventually almost surely}.}
\]
The almost-sure hitting time \(T=\inf\{n\ge0:(x_n,x_{n-1})=(0,0)\}\) satisfies
\[
\mathbb P(T>3k)\le(7/8)^k\quad(k\ge0).
\]
In contrast, ordinary one-oracle stochastic gradient descent on the **same quadratic, oracle, and step size**, initialized at \(y_0=1\), has \(\mathbb E y_n^2=2^{-n}\) and reaches zero almost surely as soon as it sees its first nonzero oracle slope.

## Assumptions and scope

All random variables are defined on a common probability space; \(U_0,U_1,\ldots\) are independent and identically distributed, independent of deterministic \(x_{-1},x_0\), with \(\mathbb E U_n=m>0\) and \(\mathbb E U_n^2=v<\infty\). Since \(v\ge m^2\), the dimensionless variance ratio \(\nu=v/m^2\) lies in \([1,\infty)\). No almost-sure sign restriction is necessary for the frontier. The explicit finite-hit example uses **nonnegative** oracle slopes \(0\) and \(2m\), so each sampled linear gradient is individually monotone.

The target is the strongly convex function \(f(x)=mx^2/2\) with exact gradient \(B(x)=mx\), and each oracle returns \(r_n=U_n(2x_n-x_{n-1})\). This is unbiased conditional on the iterate history. It is the reflected forward-backward scheme with the backward operator set to zero. The stability statement quantifies the **entire augmented iterate state** in expected square norm, and explicitly means stability for every deterministic initial pair. The borderline is excluded.

## Proof

**1. Exact second-moment transfer.** Put \(S_n=\mathbb E x_n^2\), \(P_n=\mathbb E x_{n-1}^2\), and \(C_n=\mathbb E(x_nx_{n-1})\). Conditioning on the iterates and using independence of \(U_n\), their vector obeys the exact deterministic recurrence
\[
\begin{pmatrix}S_{n+1}\\P_{n+1}\\C_{n+1}\end{pmatrix}
=K(h)\begin{pmatrix}S_n\\P_n\\C_n\end{pmatrix},\quad
K(h)=\begin{pmatrix}
1-4hm+4h^2v & h^2v & 2hm-4h^2v\\
1&0&0\\
1-2hm&0&hm
\end{pmatrix}.
\]
Direct expansion gives the exact determinant identity
\[
\boxed{\det(I-K(h))=h\big(2m-hv-3h^2mv\big).}
\]

**2. Necessity and sufficiency at the sharp boundary.** The matrix \(K(h)\) represents the linear map \(Q\mapsto\mathbb E[H(U_n)QH(U_n)^\mathsf T]\) on symmetric \(2\times2\) matrices, where
\[
H(u)=\begin{pmatrix}1-2hu&hu\\1&0\end{pmatrix},
\qquad Q=\begin{pmatrix}S&C\\C&P\end{pmatrix}.
\]
This linear map preserves the closed, pointed, generating cone of positive semidefinite matrices. The finite-dimensional Perron theorem for a cone-preserving linear map therefore ensures its spectral radius \(\rho(K(h))\) is a **nonnegative real eigenvalue** with a nonzero positive semidefinite eigenmatrix. At \(h=0\), the eigenvalues are \(1,0,0\); the simple eigenvalue \(1\) has derivative \(-2m\) as \(h\downarrow0\). Hence \(\rho(K(h))<1\) for sufficiently small positive \(h\).

The function \(2m-hv-3h^2mv\) decreases strictly from \(2m\) and vanishes at exactly one positive \(h_*\). If the spectral radius crossed \(1\) earlier, its real Perron eigenvalue would equal \(1\) somewhere earlier, contradicting the determinant identity. Thus \(\rho(K(h))<1\) throughout \(0<h<h_*\), and \(\rho(K(h_*))=1\) by continuity. If \(h>h_*\), then \(\det(I-K(h))<0\); the real monic characteristic polynomial is negative at \(1\) and tends to \(+\infty\) for large positive argument, so it has an eigenvalue larger than \(1\). Consequently \(\rho(K(h))>1\).

When the spectral radius is below one, every second-moment vector tends to zero. When it is at least one, take a nonzero positive semidefinite eigenmatrix \(Q\) and decompose it into at most two rank-one positive semidefinite matrices. These rank-one matrices are covariance matrices of deterministic initial pairs. Since the sum of their propagated nonnegative expected squared norms equals \(\rho(K)^n\operatorname{tr}Q\), at least one deterministic pair has a second moment that fails to tend to zero (and has unbounded limsup when \(\rho(K)>1\)). This establishes the exact *for-all-initializations* criterion and boundary behavior.

**3. Finite-hit versus exploding expectation.** At the stated binary oracle and step, write \(Z_n=hU_n\in\{0,1\}\). The update becomes
\[
(x_{n+1},x_n)=
\begin{cases}
(x_n,x_n),&Z_n=0,\\
(x_{n-1}-x_n,x_n),&Z_n=1.
\end{cases}
\]
Regardless of the incoming pair, the three-symbol block \((Z_n,Z_{n+1},Z_{n+2})=(0,1,0)\) sends the augmented state to \((0,0)\). Each disjoint block of three independently realizes this word with probability \(1/8\); hence \(\mathbb P(T>3k)\le(7/8)^k\), so \(T<\infty\) almost surely and the state remains zero thereafter.

For the initial pair \((x_{-1},x_0)=(0,1)\), the cross moment satisfies \(C_{n+1}=C_n/2\), so \(C_n=0\). The squared moment then satisfies \(S_{n+1}=S_n+S_{n-1}/2\), with \(S_0=S_1=1\). Solving this linear recurrence yields the displayed closed form with characteristic roots \(\lambda_\pm=(1\pm\sqrt3)/2\). Since \(\lambda_+>1\) and \(|\lambda_-|<1\), \(S_n\) grows exponentially even though paths are eventually identically zero almost surely. This is an explicit failure of uniform integrability, not a contradiction in probability theory.

For the comparison gradient method \(y_{n+1}=y_n-hU_n y_n\), the random multiplier is \(1\) or \(0\), each with probability \(1/2\). Therefore \(\mathbb E y_n^2=2^{-n}y_0^2\), using precisely one oracle call per update.

## Verification

Run `python3 verify.py` using only the Python standard library. The standalone exact-rational verifier checks the determinant identity over a grid of admissible rational moments, matches moment propagation against exhaustive binary path enumeration for several initial pairs through nine steps, verifies the special second-moment recurrence through 45 steps, checks exact annihilation by the reset word for 225 rational initial pairs, and confirms the Fibonacci all-active lower bound. `verification_output.txt` records a replay result of `VERIFY_OK` with 578 checks.

Finite enumeration is auxiliary: the universal frontier is established by the cone-preserving spectral argument, and almost-sure absorption follows from the independent disjoint-block bound; neither infinite claim is inferred from the finite tests.

## Relationship to prior work

Dung and Vũ (arXiv:2102.08906, first public version 17 February 2021), Algorithm 3.1, explicitly introduce a one-oracle stochastic reflected forward-backward update. Their constant-step convergence corollary assumes summability of oracle noise, while their bounded-noise convergence rate uses decreasing steps; neither supplies this fixed-step, state-dependent-multiplicative-noise second-moment frontier. Cui and Shanbhag (arXiv:1904.11076) study the same reflected evaluation in stochastic projected gradient methods but analyze variable batch sizes and projected gap convergence, rather than this sharp scalar moment classification. The finite-sum variance-reduced forward-reflected-backward algorithm of Alacaoglu, Malitsky and Cevher (2021) is a distinct stored-estimator method, not the independent single-oracle recursion here.

The well-known general criterion for mean-square stability of random linear recurrences, based on the spectral radius of an expected Kronecker product, supplies a framework but does not itself state the simplified universal inequality or the finite-hit/divergent-risk example. The distinction between almost-sure and mean-square convergence is classical; what is established here is its exact realization in this specific reflected-gradient method together with its all-oracle two-moment frontier. Prior deterministic reflected-gradient step boundaries include the zero-noise special case \(\nu=1\), yielding \(hm<2/3\); these do not imply the \(\nu>1\) criterion or the binary-oracle result.

## Limitations

The frontier is exact only for a **scalar linear**, fixed-step, independent and identically distributed multiplicative oracle with a finite second moment and zero backward operator. It is not a guarantee for general constrained, nonlinear, additive-noise, correlated-oracle or multidimensional problems. Only the worst-case-over-initializations second-moment statement is classified. The special finite-hit example is not claimed to be a generic property of other oracle distributions. Prior-art identification is bounded by the literature inspected; a differently phrased older treatment of this exact recursion could exist. No independent scientific audit has been performed.

## References

- N. V. Dung and B. C. Vũ, *Convergence analysis of the stochastic reflected forward-backward splitting algorithm*, arXiv:2102.08906, initial public version 17 February 2021, https://arxiv.org/abs/2102.08906.
- S. Cui and U. V. Shanbhag, *On the analysis of variance-reduced and randomized projection variants of single projection schemes for monotone stochastic variational inequality problems*, arXiv:1904.11076, initial public version 24 April 2019, https://arxiv.org/abs/1904.11076.
- A. Alacaoglu, Y. Malitsky and V. Cevher, *Forward-reflected-backward method with variance reduction*, Comput. Optim. Appl. 80 (2021), 321–346, https://doi.org/10.1007/s10589-021-00305-3.
- Y. Malitsky, *Projected reflected gradient methods for monotone variational inequalities*, SIAM J. Optim. 25 (2015), 502–520, https://doi.org/10.1137/14097238X.
