# Sharp two-step residual weighting for a two-level corrupted Kaczmarz system

## Finding

Consider an unrelaxed, scalar residual-weighted randomized Kaczmarz iteration with a proportion \(p\) of equal positive corruptions and a proportion \(q=1-p\) of clean measurements. Write \(z=p/q\) and let \(t\in(0,1]\) be the weight assigned to a nonzero residual divided by the weight at zero. For two updates, define the worst-level normalized mean-square risk
\[
R_2(t)=\max_{x_0\in\{0,c\}}\frac{\mathbb E_{x_0}[x_2^2]}{c^2}.
\]
For every \(p\in(0,1)\), the exact risk is
\[
R_2(t)=1-\frac{t\,[2z+(1+z^2)t]}{(z+t)^2(1+zt)}.
\]
If \(p<1/2\), the **unique** minimizer \(t_*(p)\) is the unique root in \((z,1)\) of
\[
N_z(t)=2z+2z^2t+z(z^2-3)t^2-(1+z^2)t^3=0.
\]
It strictly improves on uniform row sampling: \(R_2(t_*(p))<R_2(1)=p\). If \(p\ge1/2\), the unique minimizer is \(t_*(p)=1\). The threshold \(p=1/2\) is sharp. As \(p\downarrow0\) through attainable rational proportions,
\[
t_*(p)\sim(2p)^{1/3},\qquad
R_2(t_*(p))\sim\frac{3}{2^{2/3}}p^{4/3}.
\]
Thus two-step minimax tuning suppresses rare-corruption squared risk below the order-\(p\) uniform-sampling baseline. The two-step objective, not the underlying reversible-chain formula, is the result assessed here.

## Assumptions and scope

Take integers \(m\ge2\), \(1\le k\le m-1\), and \(p=k/m\). The unknown target is \(x^*=0\). The observed scalar system consists of \(m\) unit rows, with \(m-k\) measurements equal to zero and \(k\) measurements equal to the same \(c>0\). At step \(n\), a row with measurement \(b_i\) is sampled with probability proportional to \(f(|x_n-b_i|)\), where \(f\) is fixed in time, nonnegative and nonincreasing, \(f(0)>0\), and \(t=f(c)/f(0)\in(0,1]\). The exact unrelaxed projection sets \(x_{n+1}=b_i\). Only the two possible starting values \(x_0\in\{0,c\}\) enter the worst-case objective.

The parameter \(t\) can take any prescribed value in \((0,1]\), for instance with the fixed exponential function \(f(r)=\exp[-\eta r/c]\), \(\eta=-\log t\). This is not the adaptively rescaled weighting algorithm. The endpoint \(t=0\) is excluded from the minimization; it makes the two levels absorbing and has worst-start two-step risk one.

## Proof

**Exact two-state reduction.** Put \(G=0\) and \(B=c\). The clean-to-corrupt transition probability and corrupt-to-clean transition probability are respectively
\[
\alpha=\frac{pt}{q+pt},\qquad
\beta=\frac{qt}{p+qt}.
\]
For \(t>0\), the chain is irreducible and reversible. Direct two-state calculation gives its nontrivial eigenvalue
\[
\lambda=1-\alpha-\beta=\frac{pq(1-t^2)}{(q+pt)(p+qt)}\in[0,1).
\]
The two-step probability difference \(\Pr(B_2\mid B_0)-\Pr(B_2\mid G_0)=\lambda^2\ge0\). Hence the worst initial level is \(B\), and direct multiplication yields
\[
R_2(t)=\Pr(B_2\mid B_0)=1-\beta(1+\lambda).
\]
Substituting \(p=z/(1+z)\) and \(q=1/(1+z)\) gives the displayed rational risk formula. In particular \(R_2(1)=p\). At one update, by comparison, the worst-start risk is \(R_1(t)=1-\beta\), which is strictly decreasing in \(t\) and uniquely minimized at \(t=1\) for **every** contamination fraction; two updates are the first horizon for which a nontrivial interior optimum can arise.

**Global optimization.** Let the two-step success probability be
\[
F_z(t)=1-R_2(t)=\frac{t[2z+(1+z^2)t]}{(z+t)^2(1+zt)}.
\]
Differentiation without approximation gives
\[
\frac{dF_z}{dt}=\frac{zN_z(t)}{(z+t)^3(1+zt)^2}.
\]
For \(0<z<1\), \(N_z(0)=2z>0\), \(N_z(z)=2z(1-z^2)>0\), \(N_z(1)=(z-1)(z+1)^2<0\), and
\[
N_z''(t)=2z(z^2-3)-6(1+z^2)t<0\quad(t\ge0).
\]
Strict concavity with a positive initial value and negative endpoint implies exactly one zero on the positive half-line before \(t=1\), which belongs to \((z,1)\). The derivative of \(F_z\) changes from positive to negative there, giving the unique global minimizer of \(R_2\) and a strict improvement over the endpoint \(t=1\).

At \(z=1\), \(N_1(t)=2(1-t)(1+t)^2>0\) for \(0\le t<1\). Further,
\[
\frac{\partial N_z(t)}{\partial z}=2+4zt+3z^2t^2-3t^2-2zt^3.
\]
For \(z\ge1\) and \(0\le t\le1\), this partial derivative is positive: it increases with \(z\), and at \(z=1\) it equals \(2+4t-2t^3>0\). Thus \(N_z(t)>0\) throughout \(0\le t<1\) whenever \(z\ge1\). So \(F_z\) strictly increases and \(R_2\) strictly decreases up to the unique optimum \(t=1\).

**Rare-corruption scale.** For \(z\downarrow0\), substitute \(t=a z^{1/3}\) into the cubic. For each fixed \(a>0\), \(N_z(a z^{1/3})/z\to 2-a^3\). The unique-root property sandwiches its positive root between any constants below and above \(2^{1/3}z^{1/3}\); hence \(t_*(p)\sim(2p)^{1/3}\). The two-state stationary bad probability
\[
\pi_B=\frac{p^2+pqt}{p^2+q^2+2pqt}
\]
and the nontrivial eigenvalue yield the exact identity \(R_2=\pi_B+(1-\pi_B)\lambda^2\). Under this scaling, \(\pi_B\sim pt\) and \(\lambda\sim p/t\), giving
\[
R_2(t_*)\sim pt_*+p^2/t_*^2
\sim\bigl(2^{1/3}+2^{-2/3}\bigr)p^{4/3}
=3\,2^{-2/3}p^{4/3}.
\]
This proves the claimed rate along any sequence of admissible rational corruption fractions tending to zero.

## Verification

The self-contained standard-library script `verify.py` checks the rational two-state identities and worst-initial-state ordering across a finite mesh of \(m,k,t\), the exact polynomial differentiation identity by symbolic polynomial arithmetic, the optimizer's rational endpoint and sign conditions, and asymptotic numerical diagnostics. Run `python verify.py`. It checks 4,406 parameter cases in addition to the exact polynomial identity. The finite checks do not prove the quantifiers or limiting asymptotics, which follow from the algebra above.

As a rational witness, \(p=1/10\), \(t=1/2\) gives \(R_2=175/2299\approx0.07612\), whereas \(R_2(1)=1/10\); the unique continuous optimum is near \(t_*=0.52258\), with risk near \(0.07600\).

## Relationship to prior work

Chen, Cheng, He, Kryshchenko, Chi, Ma and Haddock introduce the residual-weighted corrupted-system Kaczmarz framework and establish one-step expected-error bounds and other sufficient convergence results [1]. The present restricted two-level calculation uses their fixed positive nonincreasing weight setting but instead optimizes the **exact worst-start risk after two projections**. This sharp finite-horizon design threshold and its rare-contamination exponent are not implied by the published one-step inequality. Elementary reversibility and stationary formulas are background, not asserted to be new. Earlier residual-power Kaczmarz methods [2,3] favor *larger* residuals in their principal acceleration results, a different sampling objective. Published two-state results for sampled-quantile Kaczmarz concern quantile selection, not the continuously tunable residual-weight ratio analyzed here. A covering older treatment of this exact rational optimization cannot be excluded.

## Limitations

The theorem concerns duplicate scalar rows, identical positive corruption amplitudes, two starting measurement levels, two exact-arithmetic updates and one fixed weight ratio. It does not assert an optimizer for all possible real initial conditions, larger horizons, higher-dimensional systems, changing or data-dependent weights, or a globally optimal algorithm for general sparse corruption. It provides neither a finite-sample statistical guarantee under unknown corruption fractions nor an infinite-time minimax optimum.

## References

1. Jessie Chen, Ziyu Cheng, Yunhui He, Alona Kryshchenko, Jocelyn T. Chi, Anna Ma and Jamie Haddock, *Weighted Randomized Kaczmarz for Sparsely Corrupted Linear Systems*, arXiv:2611.03889v1 (first public 2026-11-02). https://arxiv.org/abs/2611.03889
2. Stefan Steinerberger, *A Weighted Randomized Kaczmarz Method for Solving Linear Systems*, arXiv:2007.02910 (2020). https://arxiv.org/abs/2007.02910
3. Lu Zhang, Ziyang Yuan, Hongxia Wang and Hui Zhang, *A Weighted Randomized Sparse Kaczmarz Method for Solving Linear Systems*, arXiv:2306.06813 (2023). https://arxiv.org/abs/2306.06813
