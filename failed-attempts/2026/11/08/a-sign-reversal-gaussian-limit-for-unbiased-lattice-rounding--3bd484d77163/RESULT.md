# A sign-reversal Gaussian limit for unbiased lattice rounding

## Finding
Let \(\mathcal R(y;U)=\lfloor y\rfloor+\mathbf 1\{U<y-\lfloor y\rfloor\}\), where each application uses a fresh independent uniform \(U\) on \([0,1]\). Fix \(0<\theta<1\), and for \(0<r<1\) consider the two integer-valued iterations
\[
X_{k+1}^{\,+}=\mathcal R\bigl(\theta+r(X_k^{\,+}-\theta);U_k\bigr),\qquad
X_{k+1}^{\,-}=\mathcal R\bigl(\theta-r(X_k^{\,-}-\theta);U_k\bigr).
\]
They are discretizations of affine fixed-point iterations with identical absolute contraction \(r\) and fixed point \(\theta\). Each chain has a unique invariant probability measure \(\pi_r^\pm\) with finite second moment, and in either stationary regime \(\mathbb E X=\theta\).

For every \(0<r<1\), \(\pi_r^+=(1-\theta)\delta_0+\theta\delta_1\), so \(\operatorname{Var}_{\pi_r^+}(X)=\theta(1-\theta)\) independently of \(r\).

Suppose also \(2\theta\notin\mathbb Z\), and put \(p=\{2\theta\}=2\theta-\lfloor2\theta\rfloor\in(0,1)\). In contrast,
\[
\lim_{r\uparrow1}(1-r^2)\operatorname{Var}_{\pi_r^-}(X)=p(1-p),\qquad
\sqrt{1-r^2}\,(X-\theta)\ \xRightarrow[\,r\uparrow1\,]{}\ \mathcal N\bigl(0,p(1-p)\bigr),\quad X\sim\pi_r^-.
\]
In particular, \(\operatorname{Var}_{\pi_r^-}(X)/\operatorname{Var}_{\pi_r^+}(X)\sim p(1-p)/[\theta(1-\theta)(1-r^2)]\to\infty\). For \(\theta=1/4\), the positive-slope variance is \(3/16\), whereas the negative-slope variance is asymptotic to \(1/[4(1-r^2)]\), and the normalized negative-slope fluctuations converge to \(\mathcal N(0,1/4)\).

## Assumptions and scope
The state and arithmetic grid are exactly \(\mathbb Z\) (unit lattice, no saturation, overflow, underflow, or floating-point exponent spacing). Rounding is to the two adjacent integers with probabilities proportional to distance. Fresh uniforms are independent of the entire previous chain. The deterministic affine expression is evaluated exactly before its single rounding. The parameter \(r\) is positive and strictly less than one; the negative-slope limit is only asserted for \(2\theta\notin\mathbb Z\). The theorem is about stationary laws and their weak-contraction asymptotics, not transient finite-time pathwise rounding error, not a universal floating-point assertion, and not a general nonlinear-iteration theorem.

## Proof
**1. Contractivity and invariant measures.** For fixed \(U\), the map \(y\mapsto\mathcal R(y;U)\) is nondecreasing. If \(y\le z\), then \(\mathbb E_U[\mathcal R(z;U)-\mathcal R(y;U)]=z-y\), hence
\[
\mathbb E_U\bigl|\mathcal R(y;U)-\mathcal R(z;U)\bigr|=|y-z|.
\]
Using the same uniform for two copies therefore contracts their expected distance by exactly \(r\). The Markov kernel is an \(r\)-contraction in Wasserstein-1 on probability laws with finite first moment (the image of \(\delta_0\) has finite first moment). This complete metric space gives a unique invariant law in that class and convergence from each deterministic starting state. Moreover, if \(Y_k=X_k-\theta\), then \(\mathbb E[Y_{k+1}\mid X_k]=\pm rY_k\) and
\[
\mathbb E[Y_{k+1}^2\mid X_k]=r^2Y_k^2+v\bigl(\theta\pm r(X_k-\theta)\bigr),\quad
v(y)=\{y\}(1-\{y\})\le1/4.
\]
Iteration from \(X_0=0\) gives a uniform second-moment bound; Fatou's lemma gives a finite second moment for the limiting invariant law. Any other invariant law, even without an a priori moment assumption, is identical: convergence from each deterministic state together with bounded convergence for each singleton probability proves it. At stationarity, the conditional mean identity yields \(\mathbb E X=\theta\), and the variance identity is
\[
(1-r^2)V_r^\pm=\mathbb E_{\pi_r^\pm}v\bigl(\theta\pm r(X-\theta)\bigr),\qquad 0\le V_r^\pm\le[4(1-r^2)]^{-1}.
\]

**2. Positive slope.** For integer states \(0,1\), both unrounded images \(\theta+r(x-\theta)\) lie strictly between zero and one. Thus \(\{0,1\}\) is closed. A Bernoulli law on those states with probability \(\theta\) at one is invariant, because the expectation of its next state is \(\theta+r(\theta-\theta)=\theta\), and any variable supported on \(\{0,1\}\) is determined by its mean. Uniqueness proves the asserted law and variance, irrespective of the initial integer state.

**3. Negative-slope variance.** Put \(p=\{2\theta\}\in(0,1)\). Because \(X\) is integer,
\[
q_r(X):=\{\theta-r(X-\theta)\}=\bigl\{2\theta+(1-r)(X-\theta)\bigr\}.
\]
The second-moment bound gives
\[
\mathbb E_{\pi_r^-}\bigl[(1-r)^2(X-\theta)^2\bigr]\le\frac{1-r}{4(1+r)}\longrightarrow0.
\]
Since the fractional-part map is continuous at the noninteger \(2\theta\), \(q_r(X)\to p\) in probability. The function \(u\mapsto u(1-u)\) is bounded on \([0,1]\), so the variance identity and bounded convergence in probability yield \((1-r^2)V_r^-\to p(1-p)\).

**4. Gaussian law (not inferred from the variance alone).** Realize a two-sided stationary version of the negative chain with independent uniforms \((U_k)_{k\in\mathbb Z}\). Let \(e_k=X_{k+1}-[\theta-r(X_k-\theta)]\) and \(\eta_k=\mathbf 1\{U_k<p\}-p\). The latter are independent, centered, bounded Bernoulli noises of variance \(p(1-p)\). Since the rounding threshold is \(q_r(X_k)\), the common-uniform coupling gives for \(d_k=e_k-\eta_k\):
\[
\mathbb E[d_k\mid\mathcal F_k]=0,\qquad
\mathbb E[d_k^2]\le 2\mathbb E|q_r(X_k)-p|+2\mathbb E|q_r(X_k)-p|^2\longrightarrow0.
\]
Here \(\mathcal F_k\) includes the entire state and uniforms preceding time \(k\). Thus \((d_k)\) is an orthogonal martingale-difference sequence. The stationary recurrence has the convergent \(L^2\) backward expansion
\[
X_0-\theta=\sum_{j=0}^\infty(-r)^j e_{-1-j}.
\]
Replacing \(e\) by \(\eta\) makes a normalized mean-square error exactly
\[
\mathbb E\left|\sqrt{1-r^2}\sum_{j\ge0}(-r)^j d_{-1-j}\right|^2=\mathbb E d_0^2\longrightarrow0.
\]
Finally, the independent weighted Bernoulli sum \(\sqrt{1-r^2}\sum_{j\ge0}(-r)^j\eta_{-1-j}\) has variance \(p(1-p)\), maximum coefficient \(\sqrt{1-r^2}\to0\), and sum of absolute cubed coefficients \((1-r^2)^{3/2}/(1-r^3)\to0\). Its characteristic function therefore tends to \(\exp[-p(1-p)t^2/2]\). Slutsky's theorem gives the claimed Gaussian limit.

## Verification
The standalone `verify.py` uses exact rational transition kernels and solves finite invariant-distribution equations for \(\theta=1/4\) and \(r\in\{1/2,2/3,3/4,4/5,7/8,15/16,31/32\}\). It verifies the Bernoulli invariant positive branch, the invariant mean and exact variance balance on both branches, and records increasing scaled negative variance toward \(1/4\). The script also independently simulates negative-slope chains for four near-critical parameters and checks the variance scale. Its finite tests confirm algebraic examples only; the infinite-parameter and Gaussian-limit conclusions follow from the proof above.

## Relationship to prior work
Unbiased adjacent-grid rounding and conditional-variance identities are established tools, including the analysis of El Arar et al. (2022) and Xia et al. (2022). Weiß and Zhu (2024) study mean-preserving rounding in integer-valued ARMA recursions and provide stationary-moment and autocovariance identities; those general identities are not presented here as new. The present claim isolates the **sign-sensitive stationary law** for a same-fixed-point, equal-absolute-contraction pair, and proves a **nondegenerate weak-contraction Gaussian limit** for the negative branch through an adapted-noise coupling. The 2024 autoregression places a separate integer-valued innovation outside its rounded linear predictor; our noninteger intercept is inside rounding and is crucial to the limit. A published equivalent near-unit result for this exact recursion would supersede the originality claim; none was located in the comparisons described in `REVIEW.md` and `AUDIT.json`.

## Limitations
The continuous parameter \(r\) approaches one while the unit lattice remains fixed, which is a useful fixed-point arithmetic model but not the scaling of ordinary IEEE floating-point spacing. The nonresonance condition is essential to the stated nondegenerate Gaussian limit: at \(2\theta\in\mathbb Z\), the limiting innovation variance vanishes and a different finer-scale analysis is required. No convergence rate in a distribution metric is proved. Correlations between successive rounded errors are allowed and handled by martingale differences, not assumed away. Novelty is evaluated against inspected accessible sources rather than independently certified against all publications.

## References
1. L. Xia, S. Massei, M. E. Hochstenbach, B. Koren, *On the influence of stochastic roundoff errors and their bias on the convergence of the gradient descent method with low-precision floating-point computation*, arXiv:2202.12276, first posted 2022-02-24, https://arxiv.org/abs/2202.12276.
2. E.-M. El Arar, D. Sohier, P. de Oliveira Castro, E. Petit, *The Positive Effects of Stochastic Rounding in Numerical Algorithms*, arXiv:2207.03837, first posted 2022-07-08, https://arxiv.org/abs/2207.03837.
3. E.-M. El Arar, D. Sohier, P. de Oliveira Castro, E. Petit, *Stochastic rounding variance and probabilistic bounds: A new approach*, arXiv:2207.10321, first posted 2022-07-21, https://arxiv.org/abs/2207.10321.
4. C. H. Weiß, F. Zhu, *Mean-preserving rounding integer-valued ARMA models*, arXiv:2402.15772, first posted 2024-02-24, https://arxiv.org/abs/2402.15772.
