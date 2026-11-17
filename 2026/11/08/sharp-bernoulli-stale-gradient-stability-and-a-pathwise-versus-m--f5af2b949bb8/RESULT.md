# A pathwise-stable but mean-square-explosive Bernoulli stale-gradient iteration

## Finding
For scalar gradient descent with i.i.d. Bernoulli choices between a fresh and a one-iteration-stale gradient, there is a concrete fixed-step instance in which **every deterministic initial state contracts exponentially almost surely, but the expected squared error from a fixed nonzero initial state grows exponentially**. Specifically, let
\[
 x_{n+1}=x_n-\frac32 x_{n-D_n},\qquad
 \Pr(D_n=1)=\frac14,\quad \Pr(D_n=0)=\frac34,
\]
where the delays are independent across time. For every fixed real pair \((x_{-1},x_0)\), the augmented state \((x_n,x_{n-1})\) decays exponentially almost surely. With \((x_{-1},x_0)=(0,1)\), however,
\[
  \mathbb E[x_n^2]\sim C\rho^n,\qquad C>0,\quad 1<\rho<9/8,
\]
where \(\rho\) is the unique positive root of \(128z^3-8z^2-105z-27\). Thus samplewise optimization success can coexist with exponential divergence of the expected objective value \(\frac12\mathbb E[x_n^2]\) for the same stochastic algorithm.

This is an **explicit separation between almost-sure convergence and second-moment stability**, not a claim of a newly discovered mean-square stability frontier. The exact all-parameter criterion \(h+ph^2<2\) for the same Bernoulli stale-gradient recurrence, with stronger energy and noisy-stationary conclusions, had already been established in *Exact quadratic energy and the sharp mean-square frontier for Bernoulli stale-gradient descent* (published November 2, 2026). That prior result is used here to contextualize, not to claim, the second-moment threshold.

## Assumptions and scope
The objective is the strictly convex scalar quadratic \(f(x)=x^2/2\), the stepsize is the constant \(3/2\), and \((D_n)_{n\ge0}\) is an i.i.d. sequence independent of the deterministic initial pair. Outcome \(D_n=0\) uses the current gradient and outcome \(D_n=1\) the immediately preceding gradient. Almost-sure exponential decay means \(\limsup_{n\to\infty}n^{-1}\log\|(x_n,x_{n-1})\|_*<0\) for a nonzero initial pair, with possible finite-time zero states interpreted as already converged. Mean-square growth concerns the given initial pair, not every possible pair. No statement is made about correlated delays, other step sizes, nonquadratic objectives or physical parallel-worker timing.

## Proof
**Samplewise contraction.** Put \(Y_n=(x_n,x_{n-1})^{\mathsf T}\). The two matrices of the exact random recursion are
\[
A_0=\begin{pmatrix}-1/2&0\\1&0\end{pmatrix},\qquad
A_1=\begin{pmatrix}1&-3/2\\1&0\end{pmatrix}.
\]
In the norm \(\|(u,v)\|_*=\max\{|u|,|v|/2\}\), direct row-sum calculation after conjugation by \(\operatorname{diag}(1,2)\) gives the exact induced norms \(\|A_0\|_*=1/2\) and \(\|A_1\|_*=4\). Let \(N_j(n)\) count the occurrences of delay choice \(j\) in the first \(n\) updates. Submultiplicativity yields pathwise
\[
\|Y_n\|_*\le\|Y_0\|_*\, 2^{-N_0(n)}4^{N_1(n)}.
\]
The strong law gives \(N_0(n)/n\to3/4\) and \(N_1(n)/n\to1/4\) almost surely. Consequently
\[
\limsup_{n\to\infty}\frac1n\log\frac{\|Y_n\|_*}{\|Y_0\|_*}
\le \frac34\log(1/2)+\frac14\log4=-\frac14\log2<0,
\]
whenever the logarithm is defined. If a state becomes exactly zero, the iteration stays zero. The law of large numbers event depends only on the sampled delay sequence, so one probability-one event suffices for every fixed (indeed every) initial state.

**Exact second-moment growth.** For \(v_n=(\mathbb E x_n^2,\mathbb E[x_nx_{n-1}],\mathbb E x_{n-1}^2)^{\mathsf T}\), independence of the fresh delay yields
\[
v_{n+1}=Tv_n,\qquad
T=\begin{pmatrix}7/16&-3/4&9/16\\-1/8&-3/8&0\\1&0&0\end{pmatrix}.
\]
With \((x_{-1},x_0)=(0,1)\), \(v_0=(1,0,0)^{\mathsf T}\) and exact inversion gives
\[
\sum_{n\ge0}\mathbb E[x_n^2]z^n
=\frac{1+3z/8}{1-z/16-105z^2/128-27z^3/128}.
\]
The characteristic polynomial of \(T\) is \(P(\rho)=128\rho^3-8\rho^2-105\rho-27\). Its signs at \(-1,-1/2,0,1,9/8\) are respectively negative, positive, negative, negative, positive. There are exactly three distinct real roots, one in each of \((-1,-1/2)\), \((-1/2,0)\), and \((1,9/8)\). The last root \(\rho\) therefore strictly dominates the other two in modulus. The numerator is strictly positive at the positive pole \(z=1/\rho\), so it does not cancel that pole. The denominator has negative derivative there, giving a positive leading coefficient \(C\). Partial fractions yield \(\mathbb E[x_n^2]\sim C\rho^n\) with \(C>0\) and \(\rho>1\), as asserted.

The exact mean-square boundary is also confirmed by the previously published positive quadratic energy identity for the same recurrence, since at the witness parameters \(h+ph^2=33/16>2\). The independent moment computation above establishes the claimed growth for the specified initial pair without asserting priority for that boundary.

## Verification
The unchanged supplied `verify.py` symbolically checks the covariance recurrence, determinant and characteristic polynomial, the rational generating function, exact weighted operator norms and the negative logarithmic exponent. It also exhaustively compares the second moment against all delay histories through ten updates. These checks corroborate the identity and witness; the samplewise convergence and asymptotic divergence follow from the strong law and exact characteristic-root proof, not a finite experiment.

## Relationship to prior work and originality
The published November 2, 2026 theorem *Exact quadratic energy and the sharp mean-square frontier for Bernoulli stale-gradient descent*, https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-exact-quadratic-energy-and-the-sharp-mean-square-frontier-for-be--1b8d6aef9d3a/RESULT.md, concerns the **identical** Bernoulli fresh/one-stale scalar recursion and supplies the sharp condition \(h+ph^2<2\), an explicit quadratic energy, the stationary error with additive noise, and examples of **first-moment** stability despite second-moment instability. These statements are already known and are excluded from the present originality claim. First-moment decay is not almost-sure pathwise decay; the present theorem demonstrates the latter while the second moment explodes, using an explicit simultaneously negative almost-sure upper Lyapunov rate and positive moment growth rate.

Arjevani, Shamir and Srebro (2018) treat fixed stale iterations; Lale, Teke, Hassibi and Anandkumar (2021) study general random asynchronous systems; Mulayoff and Michaeli (2024) consider random minibatch current-gradient updates. The general distinction between top Lyapunov exponents and moment growth is standard in random matrix products, and no broad originality is claimed for that principle. The contribution is this reproducible, fully quantified strict separation for the natural one-step stochastic gradient-staleness model. An older exact random-coefficient recurrence example might imply the witness under a change of notation; historical priority remains qualified.

## Limitations
Only the fixed witness \(h=3/2,p=1/4\) is claimed as new, within a scalar noiseless two-delay-value model. The exact all-parameter mean-square stability threshold is prior work, and this result does not give a general almost-sure Lyapunov-exponent phase diagram. Its a.s. exponential rate is a certified upper bound, not an exact Lyapunov exponent. No external expert attestation or formal proof is asserted.

## References
1. *Exact quadratic energy and the sharp mean-square frontier for Bernoulli stale-gradient descent*, published November 2, 2026, https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-exact-quadratic-energy-and-the-sharp-mean-square-frontier-for-be--1b8d6aef9d3a/RESULT.md.
2. Y. Arjevani, O. Shamir, N. Srebro, *A Tight Convergence Analysis for Stochastic Gradient Descent with Delayed Updates*, arXiv:1806.10188 (2018), https://arxiv.org/abs/1806.10188.
3. S. Lale et al., *Stability and Identification of Random Asynchronous Linear Time-Invariant Systems*, PMLR 144 (2021), https://proceedings.mlr.press/v144/lale21a.html.
4. R. Mulayoff and T. Michaeli, *Exact Mean Square Linear Stability Analysis for SGD*, arXiv:2306.07850 (2024), https://arxiv.org/abs/2306.07850.
