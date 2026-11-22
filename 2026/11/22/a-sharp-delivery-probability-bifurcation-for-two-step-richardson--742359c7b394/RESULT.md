# A sharp delivery-probability bifurcation for two-step Richardson acceleration

## Finding

Let \(A\) be an arbitrary real symmetric positive-definite matrix whose spectrum lies in a known interval \([\mu,L]\), where \(0<\mu<L\). Choose two nonnegative Richardson step sizes in advance. Each attempted gradient update succeeds independently with probability \(p\in(0,1]\), and otherwise the iterate remains unchanged. In exact arithmetic, the smallest possible **worst-case expected squared Euclidean error factor after two attempts**, uniformly over the spectral interval, has a sharp design transition at
\[
\boxed{p_*=\frac{(\mu+L)^2}{2(\mu^2+L^2)}.}
\]
For \(0<p\le p_*\), the unique optimal pair, including at equality, is
\[
\boxed{h_1=h_2=\frac{2}{\mu+L},\qquad \mathcal R_{\rm opt}=(1-p+p c^2)^2,\qquad c=\frac{L-\mu}{L+\mu}.}
\]
For every \(p>p_*\), this repeated-step schedule is strictly suboptimal, and there exist two **unequal positive** steps that achieve strictly smaller worst-case expected squared error. Moreover, because the optimal repeated step is always \(2/(\mu+L)\), **no schedule repeating one fixed step can be optimal above the transition**. The theorem makes no assertion of a closed-form global optimizer above the threshold.

For example, when \(L/\mu=3\), the threshold is \(p_*=4/5\). At \(p=9/10\), the two normalized steps \(4/5\) and \(6/5\), meaning actual steps \(4/[5m]\) and \(6/[5m]\) for \(m=(L+\mu)/2\), achieve the exact squared amplification \(3233/31250\), strictly below the best repeated-step factor \(169/1600\).

## Assumptions and scope

The iteration is \(x_{i}=x_{i-1}+B_i h_i(b-Ax_{i-1})\), with deterministic preset \(h_i\ge0\), independent \(B_i\sim\operatorname{Bernoulli}(p)\), and a single fixed matrix \(A=A^{\mathsf T}\succ0\) for both attempts. A failed transmission performs the identity step, not an importance-rescaled stochastic gradient. The sharp robust objective is
\[
\mathcal R_p(h_1,h_2)=\sup_{\lambda\in[\mu,L]}\prod_{i=1}^{2}\bigl(1-p+p(1-h_i\lambda)^2\bigr).
\]
Since the two multiplier matrices commute and \(A\) is symmetric, this is the exact supremum of \(\mathbb E\|x_2-x_*\|_2^2/\|x_0-x_*\|_2^2\) over all admissible matrices and nonzero deterministic initial errors; it also applies to a particular matrix if its extremal spectral values realize the supremum. No independence across eigenmodes is needed: the same erasure bit applies to the whole vector on each attempt. The result is a finite-horizon design theorem, not an asymptotic iteration-rate claim.

## Proof

**1. Normalization and the repeated-step benchmark.** Put \(m=(\mu+L)/2\), \(c=(L-\mu)/(L+\mu)\), \(z=\lambda/m\in[1-c,1+c]\), and \(a_i=m h_i\). Define
\[
g(a,z)=1-p+p(1-a z)^2,\qquad B=1-p+p c^2.
\]
For a repeated normalized step \(a\), the risk equals \(\bigl[1-p+p\max\{(1-a(1-c))^2,(1-a(1+c))^2\}\bigr]^2\), since the absolute value of an affine function is maximized at an endpoint. The endpoint maximum is uniquely minimized at \(a=1\), by balancing \(1-a(1-c)\) and \(1-a(1+c)\) with opposite signs. Hence the unique best repeated pair has risk \(B^2\). This also supplies a feasible upper bound for arbitrary pairs.

**2. An exact global certificate.** Write \(a_1=1+x\), \(a_2=1+y\), allowing arbitrary real \(x,y\) for a stronger bound, and set \(F_- =g(1+x,1-c)g(1+y,1-c)\), \(F_+=g(1+x,1+c)g(1+y,1+c)\). The strictly positive endpoint weights \((1+c)/2\) and \((1-c)/2\) sum to one. Direct expansion yields the **identity**
\[
\begin{aligned}
\frac{1+c}{2}F_-+\frac{1-c}{2}F_+-B^2
=p(1-c^2)\big[&[1-p(1+c^2)](x^2+y^2)\\
&+2pc^2(x+y+xy)^2\\
&+p(1+c^2)x^2y^2\big].
\end{aligned}
\]
If \(0<p\le 1/(1+c^2)\), the right-hand side is nonnegative. The maximum of the complete objective over \([1-c,1+c]\) is at least this convex weighted endpoint average, so every pair has risk at least \(B^2\). For strictly smaller \(p\), equality forces \(x=y=0\) by the first square term. At the critical \(p\), equality requires \(xy=0\) and \(x+y+xy=0\), which likewise force \(x=y=0\). Therefore the repeated pair is globally optimal and unique throughout the closed low-reliability regime. No local-optimum or stagewise-nonexpansiveness assumption is used.

**3. Breaking the repeated-step optimum above the threshold.** For \(p>1/(1+c^2)\), set \(a_1=1-d\), \(a_2=1+d\), \(d>0\), and write \(F_d(z)=g(1-d,z)g(1+d,z)\). Another exact identity is
\[
F_d(z)=g(1,z)^2+2p z^2[1-p-p(1-z)^2]d^2+p^2z^4d^4.
\]
At both endpoints \(z=1\pm c\), the coefficient of \(d^2\) is strictly negative, since \(1-p(1+c^2)<0\). At \(d=0\), the continuous baseline \(g(1,z)^2\) reaches its maximum \(B^2\) **only** at these two endpoints; it is strictly smaller at every interior \(z\). By continuity, choose fixed small neighborhoods of the endpoints where the \(d^2\)-coefficient remains negative and then choose \(d>0\) small so the negative quadratic term dominates the positive quartic term there. On the compact interval remaining between those neighborhoods, strict baseline slack and uniform continuity preserve \(F_d(z)<B^2\). Hence \(\sup_{z\in[1-c,1+c]}F_d(z)<B^2\). Taking \(d<1\) ensures both steps are positive. Uniqueness of the best repeated step from part 1 shows that *every* globally optimal pair must be unequal when \(p>p_*\); existence follows from coercivity of the risk in \(a_1,a_2\) for each fixed \(p>0\).

**4. Exact example.** With \(c=1/2\), \(p=9/10\), \((a_1,a_2)=(4/5,6/5)\), the polynomial \(F_d(z)\) has positive second derivative on \([1/2,3/2]\) (its quadratic second derivative has negative discriminant and positive leading coefficient). Consequently its maximum lies at an endpoint. Their exact respective values are \(3233/31250\) and \(2873/31250\); their maximum is less than \(169/1600=B^2\), proving an explicit strict improvement.

## Verification

The bundled `artifacts/verify_bernoulli_richardson.py` verifies both displayed algebraic identities in symbolic arithmetic, checks the global endpoint certificate for rational grids of \(p,c,a_1,a_2\), and checks strict superiority of the stated concrete rational example through a polynomial convexity certificate. Invoke `python3 artifacts/verify_bernoulli_richardson.py` with Python 3 and SymPy; the recorded output is `artifacts/verification_output.txt`, reporting `VERIFY_OK 1010`. The universal mathematical statements are proved analytically above; a finite grid alone does not prove them.

## Relationship to prior work

Agarwal, Goel and Zhang (2021) study deterministic Chebyshev step schedules and the control of internal amplification, including deterministic inexact-gradient perturbations. Their explicit and factored spectral polynomials motivate the present question, but their inspected recurrence does not incorporate independently erased *whole steps* or optimize a finite-horizon expected squared-error minimax objective. The classical Chebyshev factorization at perfect delivery is a familiar limiting case, not a claim of newly discovering degree-two polynomial acceleration. Eftekhari and collaborators (2018) analyze stabilized gradient descent for strongly convex optimization, without the same erasure model in the inspected abstract. Sambharya and Stellato (2024) optimize step schedules across distributions of parametric problem instances; their inspected two- and three-step mean-square design is not a worst-case spectral-band objective with independent step erasures.

A previous exact stagewise-safe two-step Richardson frontier optimizes deterministic worst-case absolute polynomial error under a per-step nonexpansiveness constraint. Its condition-number threshold is unrelated to the present probabilistic threshold: here no such stagewise constraint is imposed, and the objective is an expectation of the square under random omissions. Other previously published studies treat random curvature shared among stages or constant-parameter scalar heavy ball with unbiased, rescaled Bernoulli gradients. Neither implies the claimed sharp switch between equal and unequal *preset* step sizes at all spectral condition numbers. Exact historical priority among all stochastic polynomial-approximation literature remains subject to independent assessment.

## Limitations

This is a **two-attempt** theorem, with independent identical erasure probabilities, predetermined nonadaptive nonnegative steps, a fixed symmetric positive-definite operator and an interval-uniform worst-case expected squared **error**. It does not optimize wall-clock time, the expected objective gap relative to a varying Hessian norm, numerical roundoff, correlated losses, unbiased rescaled gradient observations, adaptive schedules or general multistage methods. The all-regimes formula identifies the repeated-step optimum and the sharp boundary at which it stops being optimal; it **does not identify a closed-form optimal unequal pair above that boundary**. Full historical novelty has not been independently certified.

## References

1. N. Agarwal, S. Goel, and C. Zhang, *Acceleration via Fractal Learning Rate Schedules*, arXiv:2103.01338v1, first public 2021-03-01, https://arxiv.org/abs/2103.01338 and full text https://arxiv.org/html/2103.01338v2.
2. A. Eftekhari, B. Vandereycken, G. Vilmart, and K. C. Zygalakis, *Explicit stabilised gradient descent for faster strongly convex optimisation*, arXiv:1805.07199v1, 2018-05-18, https://arxiv.org/abs/1805.07199.
3. T. Stillfjord and M. Williamson, *SRKCD: a stabilized Runge–Kutta method for stochastic optimization*, arXiv:2201.12782v1, 2022-01-30, https://arxiv.org/abs/2201.12782.
4. R. Sambharya and B. Stellato, *Learning Algorithm Hyperparameters for Fast Parametric Convex Optimization*, arXiv:2411.15717v1, 2024-11-24, https://arxiv.org/html/2411.15717v1.
