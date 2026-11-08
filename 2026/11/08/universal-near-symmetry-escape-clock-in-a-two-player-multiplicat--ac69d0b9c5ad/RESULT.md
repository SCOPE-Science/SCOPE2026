# Universal near-symmetry escape clock in a two-player multiplicative-weights map

## Finding

Let \(a>8\) and let
\[
F_a(x,y)=\left(\frac{x}{x+(1-x)e^{a(y-1/2)}},\frac{y}{y+(1-y)e^{a(x-1/2)}}\right),\qquad 0<x,y<1.
\]
Write \(f_a(u)=F_a(u,u)_1\). There is a unique \(\sigma_a\in(0,1/2)\) such that \(f_a(\sigma_a)=1-\sigma_a\). Define
\[
\Lambda(a)=1+a\sigma_a(1-\sigma_a),\qquad \gamma(a)=\log\Lambda(a).
\]
The diagonal two-cycle \((\sigma_a,\sigma_a)\leftrightarrow(1-\sigma_a,1-\sigma_a)\) is attracting along the diagonal but repelling transversely, with **the same one-step transverse multiplier** \(\Lambda(a)\) at both points. The function \(\gamma(a)\) is strictly decreasing on \((8,\infty)\), with
\[
\lim_{a\downarrow8}\gamma(a)=\log3,\qquad
\gamma(a)\sim a e^{-a/4}\quad(a\to\infty).
\]

Put \(E_a=\bigcup_{m\ge0}f_a^{-m}(\{1/2\})\), a countable subset of \((0,1)\). For every fixed \(z\in(0,1)\setminus E_a\), there is \(\delta_0=\delta_0(a,z)>0\) such that for every \(0<\delta<\delta_0\), and sufficiently small \(\varepsilon>0\), the **first original-iteration separation time**
\[
N_{a,z,\delta}(\varepsilon)=\min\{n\ge0: X_n-Y_n\ge2\delta\},\quad (X_0,Y_0)=(z+\varepsilon,z-\varepsilon),\quad (X_n,Y_n)=F_a^n(X_0,Y_0),
\]
is finite and satisfies
\[
\boxed{\ N_{a,z,\delta}(\varepsilon)=\frac{\log(1/\varepsilon)}{\gamma(a)}+O_{a,z,\delta}(1)\ },\qquad \varepsilon\downarrow0.
\]
In particular, the leading escape coefficient is **independent of the interior diagonal starting point and the sufficiently small fixed exit threshold**. Define, for each \(a>8\),
\[
c(a):=\lim_{\varepsilon\downarrow0}\frac{N_{a,z,\delta}(\varepsilon)}{\log(1/\varepsilon)}=\frac1{\gamma(a)},
\]
using any allowable fixed \(z\notin E_a\) and \(0<\delta<\delta_0(a,z)\); the result above makes this definition independent of both choices. Then
\[
\lim_{a\to\infty}a e^{-a/4}c(a)=1.
\]
As the gain varies, admissible exit thresholds may have to vary too; no uniform joint limit in \(a\) and \(\varepsilon\) is asserted. Interchanging the two initial coordinates gives the same escape clock in the opposite direction. The original paper proves that the two signs ultimately select opposite pure-strategy fixed points.

## Assumptions and scope

The map is defined for every real \(a>8\), with symmetric cost parameter \(b=1/2\) in the original two-parameter family. The initial state lies in the open square. The integer \(n\) counts iterations of \(F_a\), **not** returns to a quotient map or to a period-two Poincaré section. For each fixed \(a\), the exceptional set \(E_a\) is precisely the set of diagonal points eventually hitting the repelling fixed point \(1/2\). The threshold \(\delta_0\) can depend on \(a,z\), and the error constant is not uniform as \(a\to\infty\) or \(z\to E_a\).

Inputs from Chotibut–Falniowski–Misiurewicz–Piliouras (2018), used as *prior theorems*, are: for \(a>8\), all diagonal trajectories not in \(E_a\) converge to the single attracting two-cycle (Theorem 3.9), and off-diagonal trajectories converge to one of the two opposite pure Nash equilibria (Theorem 4.6 and Corollary 4.7). The present quantitative exit and gain-law statement is derived below.

## Proof

**1. Two-cycle parameter and transverse derivative.** Define \(L(u)=\log(u/(1-u))\). Direct substitution into the displayed map gives the **exact** identities
\[
L(F_a(x,y)_1)=L(x)-a(y-1/2),\qquad
L(F_a(x,y)_2)=L(y)-a(x-1/2),
\]
so their difference is \(L(x)-L(y)+a(x-y)\). In particular the map strictly preserves the order of the two coordinates. The scalar map satisfies \(f_a(1-u)=1-f_a(u)\), and the equation \(f_a(\sigma)=1-\sigma\) is equivalent to
\[
\frac{\sigma}{1-\sigma}=\exp\bigl((a/2)(\sigma-1/2)\bigr).
\]
Put \(t=1-2\sigma\). The equation becomes \(a=8\operatorname{artanh}(t)/t\), for \(0<t<1\). The right side is strictly increasing from \(8\) to \(+\infty\): its derivative has the sign of \(t/(1-t^2)-\operatorname{artanh}(t)\), whose derivative is \(2t^2/(1-t^2)^2>0\) and whose value at \(t=0\) is zero. Thus \(\sigma_a\) is uniquely defined.

At a diagonal point \((u,u)\), the Jacobian has eigenvectors \((1,1)\) and \((1,-1)\), with multipliers
\[
\lambda_{\parallel}(u)=\frac{[1-au(1-u)]e^{a(u-1/2)}}{[u+(1-u)e^{a(u-1/2)}]^2},\quad
\lambda_{\perp}(u)=\frac{[1+au(1-u)]e^{a(u-1/2)}}{[u+(1-u)e^{a(u-1/2)}]^2}.
\]
The two-cycle equation implies \(e^{a(\sigma-1/2)}=[\sigma/(1-\sigma)]^2\) and \(\sigma+(1-\sigma)e^{a(\sigma-1/2)}=\sigma/(1-\sigma)\). Hence \(e^{a(\sigma-1/2)}/[\sigma+(1-\sigma)e^{a(\sigma-1/2)}]^2=1\). By reflection this also holds at \(1-\sigma\). Thus at **each** point the tangential and transverse factors are respectively \(1-h\) and \(1+h\), where \(h=a\sigma(1-\sigma)>0\).

**2. Exact gain trend and singular high-gain limit.** The cycle parameterization gives
\[
h=2(1-t^2)\frac{\operatorname{artanh}(t)}{t}.
\]
Its derivative equals \(2[t^{-1}-(1+t^{-2})\operatorname{artanh}(t)]<0\), because \(\operatorname{artanh}(t)>t>t/(1+t^2)\). Consequently \(0<h<2\), the diagonal cycle is tangentially attracting, and \(\Lambda=1+h\) decreases strictly from \(3\) to \(1\). Moreover
\[
\sigma e^{a/4}=(1-\sigma)e^{a\sigma/2}.
\]
Since \(t\to1\) and \(a\sigma=4(1-t)\operatorname{artanh}(t)/t\to0\), the last equality shows \(\sigma e^{a/4}\to1\). Therefore \(\log(1+a\sigma(1-\sigma))\sim ae^{-a/4}\).

**3. A quantitative local exit lemma.** Write \(u=(x+y)/2\), \(v=(x-y)/2\), and let \(c_n\) alternate between \(\sigma_a\) and \(1-\sigma_a\). Analyticity and symmetry under exchanging the two coordinates yield, uniformly in a sufficiently small fixed neighborhood of this two-cycle,
\[
|u_{n+1}-c_{n+1}|\le q|u_n-c_n|+C v_n^2,\qquad
v_{n+1}=\Lambda v_n[1+O(|u_n-c_n|+v_n^2)],
\]
with \(q\in(|1-h|,1)\). The second formula is positive for \(v_n>0\). Choose the neighborhood and \(\delta>0\) small enough that, as long as \(0<v_n<\delta\), the factor \(v_{n+1}/v_n\) lies in \([\mu,M]\), with \(1<\mu<\Lambda<M\), and all center deviations remain in this neighborhood. A center deviation initially sufficiently small is bounded by the contracting recurrence; the resulting \(v_n\) grows by at least \(\mu\) until exit, so the exit time is finite.

Before the first exit \(N\), \(v_{N-1}<\delta\) and \(v_{j+1}\ge\mu v_j\). Thus
\[
\sum_{j=0}^{N-1}v_j^2\le\frac{\delta^2}{1-\mu^{-2}},\qquad
\sum_{j=0}^{N-1}|u_j-c_j|\le\frac{|u_0-c_0|+C\sum_{j<N}v_j^2}{1-q}.
\]
Taking logarithms and summing the second recurrence gives
\[
\log(v_N/v_0)=N\log\Lambda+O\left(\sum_{j<N}|u_j-c_j|+\sum_{j<N}v_j^2\right)
=N\log\Lambda+O(1).
\]
At first exit, \(\delta\le v_N\le M\delta\), whence \(N=[\log(\delta/v_0)]/\log\Lambda+O(1)\). The constants depend on the fixed local neighborhood and initial center displacement, but not on \(v_0\downarrow0\).

**4. Transfer to every nonexceptional diagonal start.** By the cited 2018 Theorem 3.9, for each fixed \(z\notin E_a\), the orbit \(f_a^n(z)\) approaches one phase of the two-cycle. Fix a finite \(n_0=n_0(a,z)\) after which that diagonal orbit is sufficiently close to the cycle. At \(\varepsilon=0\), the first \(n_0\) iterates are a fixed finite orbit segment. Smoothness and the positive transverse Jacobian factors give, for \(\varepsilon\downarrow0\),
\[
v_{n_0}=K_{a,z}\varepsilon+O(\varepsilon^2),\quad K_{a,z}>0,\qquad u_{n_0}=f_a^{n_0}(z)+O(\varepsilon^2).
\]
Choose \(n_0\) so the latter center lies in the local tube and choose \(\delta\) smaller than the transverse separation generated by no fixed transient iterate (possible for all sufficiently small \(\varepsilon\)). The local lemma applies with a fixed small center displacement and \(v_{n_0}\asymp\varepsilon\). Its summation bound proves \(N_{a,z,\delta}(\varepsilon)=\log(1/\varepsilon)/\log\Lambda+O(1)\). The strict order identity ensures the trajectory cannot reverse sides. At the end, use the high-gain asymptotic of step 2; note the order of limits. This completes the proof.

## Verification

`CHECK.py` uses only Python's standard library. Run `python3 CHECK.py` after extracting it beside this file. It recomputes sampled cycle identities, tangential/transverse multipliers, the strictly decreasing sampled multiplier sequence, and finite first-exit times with perturbations down to \(10^{-12}\) at four gains. Thirty sampled escape comparisons satisfy the predicted bounded-offset law. These tests illustrate the theorem; the proof of all real gains and all eligible starting states is analytic and does **not** rely on finite sampling. In particular no uniform-in-gain exit radius is claimed.

## Relationship to prior work

Chotibut et al., *Family of chaotic maps from game theory* (2018), define the map and prove diagonal two-cycle convergence and off-diagonal convergence to the pure strategy equilibria; their Equation (16) gives a transverse derivative along the diagonal. Those foundations are **not** new here. The new assertion is the **universal original-iteration first-separation clock for all nonexceptional interior diagonal starting points**, together with the exact strict gain-dependence and the exponentially slow large-gain exponent. It is not merely a fixed-point linearization: its uniform leading coefficient along the entire diagonal basin requires controlling nonlinear drift over \(O(\log(1/\varepsilon))\) iterates.

Palaiopanos–Panageas–Piliouras (2017) study related multiplicative-weight update algorithms and game instability. Bielawski et al. (2022) treat a continuum-agent EWA model with memory loss, not the present two-agent off-diagonal initial-condition problem. The 2019 routing-game preprint investigates aggregate/one-dimensional learning dynamics. A separate published record concerns stability of a periodic orbit in a two-strategy *replicator* map under *parameter* asymmetry; this is not the state-space separation exit problem of the displayed map. These comparisons do not prove worldwide publication priority.

## Limitations

The theorem is confined to the symmetric-cost model and \(a>8\). The countable set \(E_a\) is excluded; the boundary value \(a=8\) has nonhyperbolic tangential dynamics and is not addressed. The duration is defined as first crossing of a fixed **small** separation threshold, not time to approach a pure equilibrium within a prescribed distance. The high-gain conclusion is an iterated limit, not a uniform simultaneous \((a,\varepsilon)\)-limit. The local error constants and admissible threshold may depend strongly on \(a\) and \(z\). There is a residual risk of equivalent unpublished or unindexed statements; no independent mathematical audit has been performed.

## References

1. T. Chotibut, F. Falniowski, M. Misiurewicz and G. Piliouras, *Family of chaotic maps from game theory*, arXiv:1807.06831v1 (public 2018-07-18), especially Equations (6), (7), (15), (16), Theorems 3.9 and 4.6. https://arxiv.org/html/1807.06831v1
2. G. Palaiopanos, I. Panageas and G. Piliouras, *Multiplicative Weights Update with Constant Step-Size in Congestion Games: Convergence, Limit Cycles and Chaos*, arXiv:1703.01138 (2017). https://arxiv.org/abs/1703.01138
3. J. Bielawski, T. Chotibut, F. Falniowski, M. Misiurewicz and G. Piliouras, *Unpredictable dynamics in congestion games: memory loss can prevent chaos*, arXiv:2201.10992 (2022). https://arxiv.org/abs/2201.10992
4. T. Chotibut, F. Falniowski, M. Misiurewicz and G. Piliouras, *The route to chaos in routing games: When is price of anarchy too optimistic?*, arXiv:1906.02486 (2019). https://arxiv.org/abs/1906.02486
