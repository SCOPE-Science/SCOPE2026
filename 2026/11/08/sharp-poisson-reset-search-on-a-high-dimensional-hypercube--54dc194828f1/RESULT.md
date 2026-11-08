# Sharp Poisson-reset search on a high-dimensional hypercube

## Finding

Fix an integer \(k\ge2\). A continuous-time random walker on the binary \(d\)-cube starts at Hamming distance \(k\) from a single absorbing target. Every coordinate flips at rate one; before capture, independent Poisson resets at rate \(r\) return the walker to its original vertex. Let \(M_{d,k}(r)\) be the mean target-capture time. For all \(d\ge k\), \(M_{d,k}\) is continuous on \([0,\infty)\) and attains its global minimum. As \(d\to\infty\) with \(k\) fixed,

\[
\lim_{d\to\infty}\frac{\min_{r\ge0}M_{d,k}(r)}{d^{k-1}}
=\frac{k^k}{k!\,(k-1)^{k-1}}.
\]

Moreover, **every** choice of a global minimizer \(r_{d,k}^{*}\) satisfies

\[
\lim_{d\to\infty}\frac{r_{d,k}^{*}}{d}=\frac{1}{k-1}.
\]

Without resetting, \(M_{d,k}(0)\sim 2^d/d\); hence the optimized search changes exponential expected first-passage time to polynomial order. For example, at fixed distance two the sharp optimized mean is asymptotic to \(2d\) and the optimizing reset rate is asymptotic to \(d\); at distance three, the corresponding expressions are \((9/8)d^2\) and \(d/2\).

## Assumptions and scope

The graph is \(Q_d=\{0,1\}^d\), \(d\ge k\ge2\). A state changes by flipping one coordinate, with each of the \(d\) possible coordinate flips occurring at individual rate one (so total non-reset jump rate \(d\)). The target is \(0^d\); the initial and reset vertex is any vertex of Hamming weight \(k\). Capture terminates all motion. Reset times are independent of coordinate flips, with constant rate \(r\ge0\). The minimization is only over the Poisson reset rate, not over arbitrary state-dependent or non-Poisson restart policies. The dimensional asymptotics hold for **each fixed \(k\)**, not for \(k\) growing with \(d\).

## Proof

**1. Exact renewal/resolvent representation.** Define

\[
q(t)=\frac{1+e^{-2t}}{2},\qquad a(t)=\frac{1-e^{-2t}}{2}.
\]

Independence of coordinate flips gives the unabsorbed transition probabilities \(p_t(0,0)=q(t)^d\) and \(p_t(x,0)=a(t)^kq(t)^{d-k}\). For \(r>0\), set

\[
G_0(r)=\int_0^\infty e^{-rt}q(t)^d\,dt,\qquad
G_k(r)=\int_0^\infty e^{-rt}a(t)^kq(t)^{d-k}\,dt.
\]

If \(T_0\) is the target first-passage time **without** resetting, the strong Markov property at \(T_0\) yields \(G_k(r)=\mathbb E_x[e^{-rT_0}]G_0(r)\). Write \(\phi(r)=G_k(r)/G_0(r)\). Restart-cycle renewal (one cycle succeeds when \(T_0\) precedes an independent exponential reset) yields

\[
M_{d,k}(r)=\frac{1-\phi(r)}{r\phi(r)}
=\frac{N(r)}{rG_k(r)},\quad
N(r)=\int_0^\infty e^{-rt}q(t)^d[1-\tanh(t)^k]\,dt.
\]

This is an exact finite-graph identity; no diffusion approximation is made.

**2. Uniform asymptotics on the proposed reset-rate scale.** Put \(r=cd\), with \(c\) in a compact subset of \((0,\infty)\), and change variables \(u=dt\). Since \(q(u/d)^d\to e^{-u}\) and \(d a(u/d)\to u\), dominated convergence gives, uniformly on those compact sets,

\[
dG_0(cd)\longrightarrow\frac1{1+c},\qquad
d^{k+1}G_k(cd)\longrightarrow\frac{k!}{(1+c)^{k+1}}.
\]

For uniform domination one may use \(e^{-cu}q(u/d)^d\le e^{-c_-u}\) and \(e^{-cu}(d a(u/d))^kq(u/d)^{d-k}\le u^ke^{-c_-u}\), where \(c_->0\) is the minimum permitted \(c\). Consequently,

\[
\frac{M_{d,k}(cd)}{d^{k-1}}\longrightarrow
F_k(c):=\frac{(1+c)^k}{k!\,c}
\]

uniformly on compacts. Logarithmic differentiation shows that \(F_k\) has a unique global minimizer at \(c=1/(k-1)\), with value \(k^k/[k!(k-1)^{k-1}]\).

**3. Exclusion of faster and slower reset scales.** Set \(c_0=3/(16e)\) and \(\rho=q(1)<1\). If \(0<r\le d\), integrate \(N(r)\) over \([0,1/d]\). On that interval \(e^{-rt}\ge e^{-1}\), \(q(t)^d\ge(1-1/d)^d\ge1/4\), and \(1-\tanh(t)^k\ge3/4\); hence \(N(r)\ge c_0/d\). For \(0\le t\le1\), \(q(t)=e^{-t}\cosh(t)\le e^{-t/2}\), whereas \(q(t)\le\rho\) for \(t\ge1\). Also \(a(t)^kq(t)^{d-k}=q(t)^d\tanh(t)^k\le q(t)^d t^k\). Therefore

\[
rG_k(r)\le \frac{k!r}{(r+d/2)^{k+1}}+\rho^d
\le \frac{2^{k+1}k!r}{d^{k+1}}+\rho^d.
\]

Combining the bounds,

\[
\frac{M_{d,k}(r)}{d^{k-1}}
\ge\frac{c_0}{2^{k+1}k!(r/d)+d^k\rho^d}.
\]

This tends to infinity whenever \(r/d\to0\), uniformly including the \(r=0\) limit (see step 4). Conversely, if \(r\ge d\), integrating \(N(r)\) over \([0,1/r]\) gives \(N(r)\ge c_0/r\), and \(G_k(r)\le \int_0^\infty e^{-rt}t^k\,dt=k!/r^{k+1}\). Thus

\[
\frac{M_{d,k}(r)}{d^{k-1}}
\ge \frac{c_0}{k!}\left(\frac rd\right)^{k-1},
\]

which tends to infinity whenever \(r/d\to\infty\) because \(k\ge2\). These uniform boundary bounds force every sequence of global minimizers into a compact positive interval in the scaled rate \(r/d\). The compact convergence in step 2 and the unique minimum of \(F_k\) establish both asserted limits, including convergence of **all** global optimizers, rather than merely producing a candidate rate.

**4. Zero resetting and existence.** As \(r\downarrow0\), the finite irreducible unabsorbed cube chain has stationary mass \(2^{-d}\) at the target, so \(rG_k(r)\to2^{-d}\) and

\[
M_{d,k}(0)=2^d\int_0^\infty q(t)^d[1-\tanh(t)^k]dt.
\]

The integral is finite because the bracket decays exponentially. As \(d\to\infty\) at fixed \(k\), its contribution from \([0,1]\) is asymptotic to \(1/d\), by \(q(u/d)^d\to e^{-u}\), \(q(t)\le e^{-t/2}\) for \(0\le t\le1\), and dominated convergence. The contribution from \([1,\infty)\) is exponentially small since \(1-\tanh(t)^k\le 2k e^{-2t}\) and \(q(t)\le\rho<1\). This proves \(M_{d,k}(0)\sim2^d/d\). For each fixed \(d\), continuity at \(r=0\) follows from the same renewal limit. As \(r\to\infty\), \(G_k(r)\sim k!/r^{k+1}\) and \(N(r)\sim1/r\), so \(M_{d,k}(r)\sim r^{k-1}/k!\to\infty\). By continuity, a global minimizer exists for every \(d\ge k\ge2\).

## Verification

The companion `verify.py` uses two independent finite-dimensional numerical implementations: (i) a direct tridiagonal solution of the killed Hamming-weight birth–death equations and (ii) Simpson quadrature of the exact independent-coordinate resolvent. All 45 comparisons passed at prescribed dimensions, separations, and scaled reset rates. Bounded numerical optimization at \(d=20,40,80,160\) for \(k=2,3,4\) approaches the proved constants; for \(d=160\) the scaled optimizing rates were approximately \(0.98425,0.48737,0.32224\). These tests detect algebraic or normalization mistakes but **do not certify the infinite theorem**; steps 1–4 prove it analytically.

Run with Python 3 standard library: `python verify.py`.

## Relationship to prior work

Janson and Peres (2010) optimize state-dependent restart policies on infinite Euclidean lattices via potential kernels and the grade/Gittins index. Their optimization class is more general than Poisson resetting, but their graph family and dimensional regime differ and their results do not imply a sharp fixed-Hamming-distance Poisson optimum on finite hypercubes. Evans and Majumdar (2011) establish Poisson resetting and optimize Brownian search in continuous space; their renewal principle is used here but their Brownian formulas do not yield the cube's polynomial exponent and constant. Dharmaraja et al. (2015 preprint text available as arXiv:2103.10984) analyze an Ehrenfest-type chain with catastrophes that jump **to** state zero and study passage through zero. Here resets return to an initial **non-target** vertex of fixed Hamming weight \(k\), and the target is an extreme, exponentially rare corner; our objective and high-dimensional optimization are different. No claim is made to invent resetting, Ehrenfest dynamics, or the renewal identity.

## Limitations

The results apply only to independent, equal-unit-rate flips on binary cubes, a single corner target, fixed integer Hamming separation \(k\ge2\), and homogeneous Poisson resetting to the initial vertex. They do not establish a globally optimal restart policy among state-dependent or other non-Poisson strategies. The originality comparison is based on identified accessible sources and indexed searches; historical priority is not independently certified, and an unindexed earlier specialization may exist. No independent scientific audit has been performed.

## References

1. S. Janson and Y. Peres, *Hitting times for random walks with restarts*, arXiv:1005.4275v1 (first public 2010-05-24), https://arxiv.org/html/1005.4275v1.
2. M. R. Evans and S. N. Majumdar, *Diffusion with Stochastic Resetting*, arXiv:1102.2704v1 (first public 2011-02-14), https://arxiv.org/abs/1102.2704.
3. M. R. Evans and S. N. Majumdar, *Diffusion with Optimal Resetting*, arXiv:1107.4225v1 (2011), https://arxiv.org/abs/1107.4225.
4. S. Dharmaraja, A. Di Crescenzo, V. Giorno, and A. G. Nobile, *A Continuous-Time Ehrenfest Model with Catastrophes and Its Jump-Diffusion Approximation*, Journal of Statistical Physics 161 (2015), open preprint arXiv:2103.10984, https://arxiv.org/abs/2103.10984.
