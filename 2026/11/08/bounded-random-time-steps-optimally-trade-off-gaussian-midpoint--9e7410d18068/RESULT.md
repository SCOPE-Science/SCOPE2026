# Bounded random time steps optimally trade off Gaussian midpoint autocorrelations

## Finding
Consider the stationary scalar Ornstein–Uhlenbeck equation \(dX_t=-aX_t\,dt+\sqrt{2a}\,dW_t\) with \(a>0\), discretized by the implicit midpoint rule using fresh independent Gaussian noise and independent random steps \(H_j\). Put \(U_j=aH_j/2\), and impose the natural bounded mean-step design constraints \(0<U_j\le B\) almost surely and \(\mathbb E U_j=m\), for fixed \(B>0\) and \(0<m\le B\). The numerical Markov chain has the **exact** invariant distribution \(N(0,1)\) for every admissible step law.

For stationary observations \(g_1(x)=x\) and \(g_2(x)=x^2-1\), define their integrated autocorrelation factors by \(\tau_i=1+2\sum_{j\ge1}\operatorname{Corr}(g_i(X_0),g_i(X_j))\). Write
\[
 r(u)=\frac{1-u}{1+u},\qquad f(u)=r(u)^2,\qquad q_1=\mathbb E r(U),\qquad q_2=\mathbb E f(U).
\]
Both autocorrelation factors are exactly
\[
 \tau_i=\frac{1+q_i}{1-q_i}\quad(i=1,2).
\]
Every nonconstant admissible random step law strictly **increases** \(\tau_1\) over the deterministic step \(U=m\).

For the quadratic observable, the **unique** mean- and cap-constrained optimal step law is as follows:

* If \(B\le2\), or if \(B>2\) and \(m\le t_B:=1+2/B\), use the deterministic step \(U=m\); then \(q_2^*=f(m)\).
* If \(B>2\) and \(t_B<m<B\), use exactly the two steps \(t_B\) and \(B\), with probabilities \((B-m)/(B-t_B)\) and \((m-t_B)/(B-t_B)\), respectively. Its optimal correlation is
\[
 q_2^*=\frac{B^2m-B^2-B+1}{(B+1)^3}.
\]
* If \(m=B\), only the deterministic law is admissible, including when \(B>2\).

Consequently, randomization can strictly **reduce** the quadratic integrated autocorrelation factor precisely when \(B>2\) and \(t_B<m<B\). The exact reduction in the lag-one quadratic multiplier, relative to the deterministic step, is
\[
 f(m)-q_2^*=\frac{(B-m)(Bm-B-2)^2}{(B+1)^3(1+m)^2}>0.
\]
Thus, in the improvement region, the unique quadratic-optimal randomization strictly worsens the linear-observable asymptotic variance. This is an observable-dependent tradeoff despite an exactly unchanged Gaussian invariant law.

For example, at \(B=10\), \(m=5\), the optimal law uses \(U=6/5\) with probability \(25/44\) and \(U=10\) with probability \(19/44\). The quadratic factor falls from \(13/5\) (deterministic) to \(861/470\); the linear factor rises from \(1/5\) to \(36/85\).

## Assumptions and scope
The numerical method uses independent \(H_j\) with the same law for all updates, independent \(\xi_j\sim N(0,1)\), and the exact one-step midpoint solution
\[
 X_{j+1}=X_j-\frac{aH_j}{2}(X_j+X_{j+1})+\sqrt{2aH_j}\,\xi_j.
\]
The cost constraint is on the **mean dimensionless step per update**, not on a fixed realized total physical time. The maximum \(B\) is finite and all optimal steps are strictly positive. The theorem concerns the two canonical Gaussian Hermite observables and stationary sampling variance per numerical update. It does not assert improved strong/weak path approximation, uniform improvement for all observables, or an optimum across multiple drift rates.

## Proof
Solving the midpoint equation gives, conditional on \(U=u\),
\[
 X_{j+1}=r(u)X_j+\sqrt{1-r(u)^2}\,\xi_j,
 \qquad r(u)=\frac{1-u}{1+u}.
\]
For \(u>0\) finite, \(|r(u)|<1\). Each conditional Gaussian transition preserves \(N(0,1)\), hence so does every mixture over admissible steps. A synchronous coupling of two copies has mean squared difference multiplied by \(q_2=\mathbb E[r(U)^2]<1\), proving uniqueness of this invariant distribution and geometric mean-square contraction.

Let \(P\) denote the averaged transition operator. Direct Gaussian conditional moments yield \(P g_1=q_1g_1\) and \(P g_2=q_2g_2\). Therefore, in stationarity, for every integer \(j\ge0\), the corresponding normalized lag correlations equal \(q_i^j\). As \(|q_1|<1\) and \(0\le q_2<1\), summing the geometric series proves \(\tau_i=(1+q_i)/(1-q_i)\). Each fixed-step Gaussian AR kernel is reversible for \(N(0,1)\). Its Hermite polynomials of positive degree \(j\) are eigenfunctions with eigenvalues \(r(u)^j\); the mixture has eigenvalues \(\mathbb E[r(U)^j]\). Since \(\sup_{j\ge1}|\mathbb E[r(U)^j]|\le\mathbb E|r(U)|<1\), the stationary kernel has an \(L^2\) spectral gap. The stationary central-limit asymptotic variance of the sample mean of \(g_i\) therefore equals \(\operatorname{Var}_{N(0,1)}(g_i)\tau_i\), namely \(\tau_1\) and \(2\tau_2\).

Now \(r''(u)=4/(1+u)^3>0\) on \([0,B]\). Jensen's inequality, strict for every nondegenerate law, gives \(q_1\ge r(m)\), with strict inequality under randomization. Since \(q\mapsto(1+q)/(1-q)\) is strictly increasing on \((-1,1)\), this proves the linear-observable assertion.

For \(f=r^2\),
\[
 f''(u)=\frac{8(2-u)}{(1+u)^4}.
\]
When \(B\le2\), strict convexity throughout the relevant interval makes the point mass at \(m\) the unique minimizer of \(\mathbb E f(U)\).

Suppose \(B>2\), and put \(t=t_B=1+2/B\in(1,2)\) and
\[
 \ell_B(u)=\frac{B^2u-B^2-B+1}{(B+1)^3}.
\]
The line \(\ell_B\) is tangent to \(f\) at \(t\) and meets \(f\) again at \(B\). The exact identity
\[
 f(u)-\ell_B(u)=\frac{(B-u)(Bu-B-2)^2}{(B+1)^3(1+u)^2}\ge0
 \qquad(0\le u\le B)
\]
proves that the piecewise function equal to \(f\) on \([0,t]\) and to \(\ell_B\) on \([t,B]\) is a convex minorant. In fact it is the lower convex envelope: it is convex because \(f''>0\) up to \(t\) and its derivative there matches the line's slope, and no convex minorant can exceed the chord joining the two contact points on \([t,B]\).

Jensen's inequality for that envelope gives the claimed lower bound on \(\mathbb E f(U)\). For \(m\le t\), the point mass at \(m\) attains it; for \(t<m<B\), the stated two-point law at \(t\) and \(B\) attains the affine value. Equality conditions give uniqueness: strict convexity forces a point mass below \(t\), while in the affine segment contact with \(f\) occurs only at \(t\) and \(B\). The endpoint \(m=B\) also forces a point mass. Substituting \(u=m\) into the factorization yields the explicit strict improvement formula and its exact phase boundary.

## Verification
Run `python verify.py` with SymPy installed. It checks the two curvature identities, tangent/chord/contact identities, the global factorization, the exact rational example and 9,952 admissible rational two-atom competitors. Recorded output appears in `verification_output.txt`. These tests support, but do not substitute for, the convex-envelope proof for all probability laws or the stationary Gaussian Markov argument.

## Relationship to prior work
Abdulle and Garegnani (arXiv:1801.01340, first public 2018-01-04) introduce random-time-step numerical integration with geometric preservation and fixed-mean steps, and analyze path accuracy. The current result uses that mean-step design motivation but concerns a noisy scalar Gaussian Markov chain, its **stationary observable correlations**, and an exact bounded-support distributional optimum. He, Balasubramanian and Erdogdu (arXiv:2011.03176) study a different randomized-intermediate-point Langevin algorithm with stationary bias, not this exact implicit midpoint mixture. Lie, Stahn and Sullivan (arXiv:2103.16506) analyze randomised time integration for deterministic operator equations, not this OU autocorrelation design.

Classical Gaussian conditional moments, Jensen's inequality and the lower-convex-envelope principle are prior mathematical tools, not claimed new. A related prior result for randomly stepped scalar implicit-midpoint damping optimizes the **scale of an equiprobable log-symmetric binary law**, without optimizing over all laws of fixed arithmetic mean and cap or deriving the opposing linear/quadratic Gaussian sampling effects. The novelty assessment applies only to the explicit unique optimal bounded step law and its observable-dependent sharp phase boundary.

## Limitations
This is a scalar stationary Gaussian benchmark, not a numerical time-accuracy or pathwise error guarantee. The optimal law for \(m>t_B\) may have a broad range of time steps, so it can be inappropriate when accurate trajectory timing or small-step convergence is required. The simple expectation \(\mathbb E_{\pi}[X^2]=1\) is known here; the significance is the exact risk mechanism and design constraint, not estimating an unknown scalar OU variance. Historical work on constrained step-law optimization could contain a related specialization; no independent literature audit has been performed.

## References
1. A. Abdulle and G. Garegnani, *Random time step probabilistic methods for uncertainty quantification in chaotic and geometric numerical integration*, arXiv:1801.01340 (first public 2018-01-04), https://arxiv.org/abs/1801.01340.
2. Y. He, K. Balasubramanian and M. A. Erdogdu, *On the Ergodicity, Bias and Asymptotic Normality of Randomized Midpoint Sampling Method*, arXiv:2011.03176 (2020), https://arxiv.org/abs/2011.03176.
3. H. C. Lie, M. Stahn and T. J. Sullivan, *Randomised one-step time integration methods for deterministic operator differential equations*, arXiv:2103.16506 (2021), https://arxiv.org/abs/2103.16506.
