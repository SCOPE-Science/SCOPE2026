# Sharp positivity frontier for three-feature Legendre Bayesian quadrature

## Finding

Consider regularized Bayesian quadrature for the uniform probability measure on \([-1,1]\) and the first three Legendre features. For every integer \(n\ge 2\), the exact nugget needed to keep **all** quadrature weights nonnegative for **every centrally symmetric \(n\)-point multiset** is
\[
\eta\ge a_2 C_n,\qquad
C_n=\begin{cases}
(n-2)/4,&n\text{ even},\\
(n-1)/16,&n=3,5,7,\\
(n-6)/4,&n\ge9\text{ odd}.
\end{cases}
\]
Here \(a_2>0\) is the coefficient of the second-degree Legendre feature. The threshold is sharp for every \(n\): below it, a symmetric design with a negative weight exists; at it, a symmetric design with a zero weight exists when \(n\ge3\); strictly above it, all weights are positive. The constant and the sign boundary are independent of the constant- and linear-feature coefficients.

A consequence is an unavoidable bias trade-off for the **unmodified** posterior-mean rule. Any sequence \(\eta_n\) that guarantees nonnegative weights for every symmetric design satisfies
\[
\liminf_{n\to\infty}\left|Q_{\eta_n}(1)-1\right|
\ge \frac{a_2}{4a_0+a_2}>0.
\]
This lower bound holds for every corresponding choice of symmetric design nodes; it is a worst-design stability safeguard, not an assertion about optimally chosen nodes or an explicitly normalized rule.

## Assumptions and scope

Let \(P_2(x)=(3x^2-1)/2\), and let \(a_0,a_1,a_2,\eta\) be arbitrary positive real numbers. Set
\[
k(x,y)=a_0+a_1xy+a_2P_2(x)P_2(y),\qquad
\mathbb P(dx)=\tfrac12\,dx\quad(x\in[-1,1]).
\]
The nodes \(x_1,\ldots,x_n\in[-1,1]\) form a centrally symmetric multiset, meaning that the multiplicity of every nonzero node matches that of its negative. Repeated nodes are permitted because the nugget \(\eta>0\) makes the system strictly positive definite even then. Define the Gram matrix \(K_{ij}=k(x_i,x_j)\), kernel-mean vector \(\mu_i=\int k(x_i,y)\,\mathbb P(dy)=a_0\), weights \(w=(K+\eta I_n)^{-1}\mu\), and unmodified quadrature functional \(Q_\eta(f)=\sum_iw_if(x_i)\). These formulas specify the exact algebraic estimator; there is no forced normalization of the weights to sum to one.

The finite-feature polynomial kernel is of the Legendre spectral form of Zhu and Li (2026), but this result does **not** assume the auxiliary-domain padding or sample-design hypotheses of their convergence theorems. It concerns the finite-feature estimator itself, not those rates.

## Proof

**1. Exact signed-weight formula.** Write \(z_i=P_2(x_i)\), \(S_1=\sum_jz_j\), \(S_2=\sum_jz_j^2\), and let \(\mathbf1\), \(x\), and \(z\) be the corresponding column vectors. Symmetry and the evenness of \(P_2\) imply \(x^T\mathbf1=x^Tz=0\). Put \(A=\eta I_n+a_1xx^T+a_2zz^T\). The rank-one inverse identity, first on \(A\) and then on \(A+a_0\mathbf1\mathbf1^T\), yields
\[
A^{-1}\mathbf1=\frac1\eta\left(\mathbf1-\frac{a_2S_1}{\eta+a_2S_2}z\right),\qquad
w=\frac{a_0}{1+a_0T}A^{-1}\mathbf1,
\]
where
\[
T=\mathbf1^TA^{-1}\mathbf1
=\frac1\eta\left(n-\frac{a_2S_1^2}{\eta+a_2S_2}\right)>0.
\]
The strict positivity of \(T\) also follows from \(A\) being positive definite. Therefore
\[
\boxed{\quad
w_i=\frac{a_0\bigl[\eta+a_2(S_2-z_iS_1)\bigr]}
{\eta(1+a_0T)(\eta+a_2S_2)}\quad}
\]
and the weight sign is the sign of \(\eta-a_2d_i\), with
\[
d_i=z_iS_1-S_2=\sum_{j\ne i}z_j(z_i-z_j).
\]
Since \(P_2([-1,1])=[-1/2,1]\), every \(z_i\) belongs to that interval.

**2. Sharp symmetric-design optimization.** For any \(t,s\in[-1/2,1]\),
\[
s(t-s)=\frac{t^2}{4}-\left(s-\frac t2\right)^2\le\frac{t^2}{4}.
\]
If \(n\) is even, every \(z_i=t\) has a second occurrence (its opposite node). That partner contributes zero to \(d_i\). The other \(n-2\) terms give
\[
d_i\le(n-2)t^2/4\le(n-2)/4.
\]
Equality is achieved with one opposite pair \(x=\pm1\) (so \(t=1\)) and all remaining pairs \(x=\pm\sqrt{2/3}\) (so \(s=1/2=t/2\)). This includes \(n=2\), with \(C_2=0\).

For odd \(n\), choose one zero node as the central unpaired node. If the target index is this central node, then \(t=P_2(0)=-1/2\); pairing the other \(n-1\) nodes and applying the inequality gives
\[
d_i\le(n-1)/16.
\]
Equality holds when all other nodes equal \(\pm1/\sqrt6\), since their Legendre value is \(-1/4=t/2\).

For any other target index, let \(t=z_i\). Its reflected partner contributes zero, the central zero node contributes \((-1/2)(t+1/2)\), and the remaining \(n-3\) nodes each contribute at most \(t^2/4\). Hence
\[
d_i\le g_n(t):=\frac{n-3}{4}t^2-\frac t2-\frac14.
\]
The function \(g_n\) is convex on \([-1/2,1]\); its maximum there is attained at an endpoint, giving
\[
\sup g_n=\max\left\{\frac{n-3}{16},\frac{n-6}{4}\right\}.
\]
The first entry is strictly dominated by the central-node bound. The second is attained by a target opposite pair \(\pm1\), the one central zero node, and all other opposite pairs \(\pm\sqrt{2/3}\). Therefore the exact all-index maximum is
\[
C_n=\max\left\{\frac{n-1}{16},\frac{n-6}{4}\right\}
\]
for odd \(n\), whose active branch changes between \(n=7\) and \(n=9\). The displayed piecewise formula follows.

**3. Sign classification and sharpness.** All weights have nonnegative signs for every design precisely when \(\eta\ge a_2\sup_{X,i}d_i=a_2C_n\). The preceding witness designs attain the supremum and give zero weights at equality (for \(n\ge3\)) and negative weights strictly below it. Above the threshold the numerator of every weight is strictly positive. At \(n=2\), \(C_2=0\) and every admissible \(\eta>0\) is strictly safe. Even if distinctness is required, continuity under symmetric node perturbations preserves a negative weight for any fixed strict subthreshold \(\eta\); exact threshold attainment by repeated-node examples is a statement for multisets.

**4. Constant-function bias.** Positive semidefinite order gives
\[
K+\eta I_n\succeq\eta I_n+a_0\mathbf1\mathbf1^T.
\]
Because inversion reverses this order for positive definite matrices,
\[
0< Q_\eta(1)=a_0\mathbf1^T(K+\eta I_n)^{-1}\mathbf1
\le\frac{a_0n}{\eta+a_0n}<1.
\]
Thus \(1-Q_\eta(1)\ge\eta/(\eta+a_0n)\). A universal nonnegative-weight guarantee imposes \(\eta_n\ge a_2C_n\), and \(C_n/n\to1/4\). Monotonicity of the right-hand side implies
\[
\liminf_{n\to\infty}(1-Q_{\eta_n}(1))\ge
\frac{a_2/4}{a_0+a_2/4}=
\frac{a_2}{4a_0+a_2}.
\]
This is uniform over all symmetric node choices. It does not apply to an explicitly renormalized or constrained-simplex quadrature estimator, which is a different rule.

## Verification

The accompanying standalone \(\texttt{verify.py}\) uses only Python standard-library exact fractions. It checks the witness maximas for every integer \(2\le n\le50\), including the parity switch; verifies strict sign changes at the threshold; and compares the closed formula against direct exact-rational Gram-system elimination for 220 seeded random symmetric designs, including the constant-function bias bound. A completed run returned \(\texttt{VERIFY_OK 269 exact-rational tests}\). These finite checks are supplementary: the proof above establishes the assertion for every integer \(n\ge2\) and every admissible symmetric node multiset.

## Relationship to prior work

Zhu and Li (2026, Section 2.2 and Section 5.2) define finite-feature Bayesian quadrature with an operator-adapted Legendre basis and ridge regularization, and study error and uncertainty guarantees. The present result concerns a different property: a sharp all-symmetric-design, finite-feature sign threshold and its induced constant-function bias. It uses a three-feature algebraic specialization; no claim is made that the source's auxiliary-domain statistical assumptions are met.

Karvonen, Kanagawa and Särkkä (2019, especially Section 3) analyze positivity and magnitudes of Bayesian quadrature weights, including a sufficient positivity condition for locally optimal designs with a totally positive univariate kernel. That is not an all-design, all-\(n\) nugget characterization for the finite-rank Legendre model here. Hayakawa (2026, Sections 2–5) establishes rates for quadrature weights constrained to a positive simplex; an explicitly constrained rule is not equivalent to the unconstrained ridge rule studied here.

## Limitations

The result is exact for a rank-three polynomial kernel, symmetric designs, a uniform target measure and a positive ridge nugget. It does not classify nonsymmetric designs, general nonpolynomial kernels, higher-dimensional feature spaces, or more than three Legendre features. The limiting bias is for the unmodified posterior-mean quadrature weights under the stringent universal nonnegativity guarantee; node-adapted regularization, weight renormalization, or explicit positivity constraints can behave differently. Historical priority has not been exhaustively established.

## References

- Huanyan Zhu and Cheng Li, *Scalable Bayesian Quadrature via Operator-Adapted Features*, arXiv:2610.38212v1 (first public 2026-10-28), https://arxiv.org/html/2610.38212v1, Sections 2.2 and 5.2.
- Toni Karvonen, Motonobu Kanagawa and Simo Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, *Statistics and Computing* 29 (2019), 1317–1333, https://doi.org/10.1007/s11222-019-09901-0, especially Section 3.
- Satoshi Hayakawa, *Convex-Geometric Error Bounds for Positive-Weight Kernel Quadrature*, arXiv:2605.05705v1 (2026-05-07), https://arxiv.org/html/2605.05705v1, Sections 2–5.
