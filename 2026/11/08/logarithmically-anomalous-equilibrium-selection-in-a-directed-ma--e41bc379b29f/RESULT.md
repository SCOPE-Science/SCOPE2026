# Logarithmically anomalous equilibrium selection in a directed many-loci recombination cycle

## Finding
For every integer \(m\ge3\), consider a directed, cyclic nearest-neighbor instance of the quadratic stochastic many-loci operator introduced by Omirov and Rozikov [1]. On a strictly positive invariant fiber it converges to a common allele ratio \(\beta_m\), with the exact formula
\[
\beta_m=\frac{\sum_{i=1}^m q_i/c_{i+1}}{\sum_{i=1}^m1/c_{i+1}},
\qquad c_i=x_{i,+}+x_{i,-},\quad q_i=x_{i,+}/c_i.
\]
All subscripts are cyclic. If the \(2m\) initial coordinates have the symmetric Dirichlet law with common shape \(a\ge1\), then \(\beta_m\to1/2\) in probability, with the **two regimes**
\[
\boxed{\sqrt m\,(\beta_m-\tfrac12)\ \Longrightarrow\
N\!\left(0,\frac{2a-1}{4(2a+1)(2a-2)}\right),\quad a>1,}
\]
\[
\boxed{\sqrt{\frac{m}{\log m}}\,(\beta_m-\tfrac12)\ \Longrightarrow\ N(0,1/24),\quad a=1.}
\]
The \(a=1\) case is uniform sampling from the \((2m-1)\)-simplex. Its square-root logarithmic enlargement is intrinsic: it comes from random inverse fiber masses with an infinite second moment.

For comparison, the all-to-all version of the same many-loci operator reaches common allele ratio after one iteration, and, under the same Dirichlet initialization, its selected ratio has exactly the \(\operatorname{Beta}(ma,ma)\) law. Thus its centered fluctuations always have square-root \(m\) scale, including at \(a=1\), with limiting normal variance \(1/(8a)\).

## Assumptions and scope
Let \(m\ge3\). Work on the simplex of \(2m\) nonnegative real coordinates \(x_{i,+},x_{i,-}\), indexed by \(i=1,\ldots,m\), summing to one. Write \(i+1\) modulo \(m\) and set
\[
\begin{aligned}
x'_{i,+}&=x_{i,+}+x_{i,-}x_{i+1,+}-x_{i,+}x_{i+1,-},\\
x'_{i,-}&=x_{i,-}-x_{i,-}x_{i+1,+}+x_{i,+}x_{i+1,-}.
\end{aligned}
\]
This is equation (1.5) of [1] with coefficients \(a_{i,i+1}=1\) and all other coefficients zero; no symmetry of the coefficient matrix is assumed. The map preserves the simplex and the pair masses \(c_i\). The deterministic equilibrium statement assumes \(c_i>0\) for all \(i\), automatically true almost surely under the distributions below.

For the probabilistic statement, choose the initial vector according to \(\operatorname{Dirichlet}(a,\ldots,a)\) on the \(2m\) coordinates, independently for each dimension \(m\), with fixed \(a\ge1\). First iterate the deterministic dynamics to convergence at that fixed dimension and *then* let \(m\to\infty\); no assertion is made about a joint time/dimension limit. The limit parameter \(\beta_m\) is the common ratio, so the final \(2m\) coordinates are \((c_i\beta_m,c_i(1-\beta_m))\).

## Proof
### Step 1: exact consensus and its invariant
Because each pair sum \(c_i\) is invariant, \(q_i=x_{i,+}/c_i\) obeys the **exact** relation
\[
q'_i=(1-c_{i+1})q_i+c_{i+1}q_{i+1}.
\]
All \(c_i\in(0,1)\) because the fiber is strictly positive and \(m\ge3\). Therefore this row-stochastic matrix is aperiodic (positive diagonal) and irreducible (every forward cyclic edge has positive weight). Its unique stationary left vector is
\[
\omega_i=\frac{1/c_{i+1}}{\sum_{j=1}^m1/c_{j+1}},
\]
since the stationarity equation is \(\omega_i c_{i+1}=\omega_{i-1}c_i\). Perron–Frobenius convergence of the finite primitive stochastic matrix gives \(q_i(n)\to\sum_j\omega_jq_j(0)=\beta_m\). This argument separately establishes convergence for the asymmetric cyclic specialization without invoking any symmetry-restricted result in [1].

### Step 2: gamma representation of the randomized limit
Let \(H_{i,+},H_{i,-}\), all independently distributed as \(\operatorname{Gamma}(a,1)\), represent the initial Dirichlet vector by normalizing their sum. Define \(G_i=H_{i,+}+H_{i,-}\) and \(U_i=H_{i,+}/G_i\). Gamma–Beta independence yields independent \(G_i\sim\operatorname{Gamma}(2a,1)\), independent \(U_i\sim\operatorname{Beta}(a,a)\), and independence between the entire two families. In particular,
\[
\beta_m-\tfrac12=
\frac{\sum_{i=1}^m Y_i}{\sum_{i=1}^m G_{i+1}^{-1}},
\qquad Y_i=\frac{U_i-1/2}{G_{i+1}}.
\]
The \(Y_i\) are independent and identically distributed for each \(m\), including across the wraparound, because all the pairs \((U_i,G_{i+1})\) are independent. Their mean is zero since \(U_i-1/2\) is symmetric and independent of the denominator. For \(a\ge1\), \(\mathbb E G^{-1}=1/(2a-1)<\infty\), so the denominator divided by \(m\) tends in probability to \(1/(2a-1)\).

### Step 3: ordinary Gaussian regime
When \(a>1\),
\[
\operatorname{Var}(U_i)=\frac1{4(2a+1)},\qquad
\mathbb EG_i^{-2}=\frac1{(2a-1)(2a-2)}.
\]
Thus
\[
\operatorname{Var}(Y_i)=\frac1{4(2a+1)(2a-1)(2a-2)}.
\]
The ordinary independent-summand central limit theorem and the denominator law of large numbers, followed by Slutsky's theorem, yield the first boxed limit.

### Step 4: the critical logarithmic normal law
When \(a=1\), the \(U_i\) are uniform on \((0,1)\) and the \(G_i\) have the \(\operatorname{Gamma}(2,1)\) law. Set \(Y=(U-1/2)/G\). Direct integration with gamma density \(g e^{-g}\) gives, for every \(t>0\),
\[
\begin{aligned}
\Pr(|Y|>t)
&=\int_0^{1/(2t)}(1-2tg)g e^{-g}\,dg\\
&=1-4t+(1+4t)e^{-1/(2t)}
=\frac1{24t^2}+O(t^{-3}),\quad t\to\infty.
\end{aligned}
\]
By the tail-integration identity, the truncated second moment satisfies
\[
H(T):=\mathbb E[Y^2\mathbf1_{\{|Y|\le T\}}]
=2\int_0^T t\Pr(|Y|>t)\,dt-T^2\Pr(|Y|>T)
=\frac1{12}\log T+O(1).
\]
Take \(b_m=\sqrt{m\log m/24}\). Then
\[
\frac{m H(b_m)}{b_m^2}\to1,\qquad
m\Pr(|Y|>b_m)\to0.
\]
Truncate the symmetric variables \(Y_i\) at \(b_m\); their means remain zero. For every fixed \(0<\epsilon<1\), the Lindeberg condition follows from
\[
\frac m{b_m^2}\mathbb E\left[Y^2\mathbf1_{\{\epsilon b_m<|Y|\le b_m\}}\right]
=\frac m{b_m^2}\bigl(H(b_m)-H(\epsilon b_m)\bigr)\to0,
\]
because the parenthesized difference is \(O_\epsilon(1)\) and \(m/b_m^2=O(1/\log m)\). Lindeberg–Feller therefore gives \(b_m^{-1}\sum_iY_i\Longrightarrow N(0,1)\). The chance that any summand was removed is at most \(m\Pr(|Y|>b_m)=o(1)\), so the same law holds without truncation. Since \(m^{-1}\sum_iG_{i+1}^{-1}\to1\), the original ratio converges after multiplying by \(\sqrt{m/\log m}\) to \(N(0,1/24)\). Both fluctuation results entail \(\beta_m\to1/2\) in probability.

### Step 5: symmetric complete-mixing comparison
Instead set \(a_{ij}=1\) whenever \(i\ne j\). Then direct substitution gives \(q'_i=\sum_jc_jq_j\) for every \(i\), so consensus occurs in one step and equals \(\sum_ix_{i,+}\). Under symmetric Dirichlet initialization it is exactly \(\operatorname{Beta}(ma,ma)\), because the sums of the \(+\) and \(-\) gamma coordinates have independent \(\operatorname{Gamma}(ma,1)\) laws. Their standard central limit theorem gives
\[
\sqrt m\left(\sum_i x_{i,+}-\tfrac12\right)\Longrightarrow N\left(0,\frac1{8a}\right).
\]
This completes the promised structural comparison. \(\square\)

## Verification
Run the accompanying stand-alone Python standard-library file with `python verify.py`. It checks the exact fiber invariant and cycle-stationary weighted ratio by rational arithmetic for several dimensions, the inverse-gamma critical-tail expansion at high precision, the finite-variance constants, and direct iteration to the predicted consensus. Its finite simulations illustrate—not prove—the two fluctuation scales. The analytical proof above supplies all infinite-dimensional and limit claims.

## Relationship to prior work
Omirov and Rozikov [1] introduce precisely the many-loci quadratic operator containing this coefficient specialization and characterize deterministic orbits using invariant fibers. Their equation (1.5), Lemma 2, and results on limit points are foundational here. We do not claim the fiber decomposition or the underlying finite-dimensional Markov-chain convergence as new. The additional question treated here is the random **selection** of those equilibria under a natural \(2m\)-coordinate Dirichlet law, and in particular the critical fluctuation scale when the number of loci increases. Inverse-gamma heavy tails and logarithmic-variance central limit arguments are classical probability tools; the contribution is their exact coupling to the equilibrium selected by this particular nonlinear dynamics, with evaluated constants and a complete-mixing comparison. An existing result for the two-locus selection density does not imply the growing directed-cycle limit.

## Limitations
The theorem is for fixed \(a\ge1\), strictly positive fibers, directed nearest-neighbor cyclic coefficients, and the specified symmetric Dirichlet distribution. It does not establish rates uniform in the dimension for convergence in iteration time, does not treat Dirichlet shapes below one, and does not assert a publication-priority guarantee against all unindexed work. The limiting Gaussian statements describe distributional convergence, not convergence of second moments; at the critical parameter the prelimit variance can be sensitive to rare extremes. Independent audit has not been performed.

## References
[1] B. A. Omirov and U. A. Rozikov, *A many-loci system with evolution characterized by uncountable linear operators*, arXiv:2409.19687v1 (first public 2024-09-29), https://arxiv.org/abs/2409.19687; especially equation (1.5), Lemma 2 and Theorem 2.

[2] Standard gamma–Dirichlet decomposition, finite-state Markov-chain convergence, and Lindeberg–Feller triangular-array central limit theorem (used in their classical forms; not claimed as new).
