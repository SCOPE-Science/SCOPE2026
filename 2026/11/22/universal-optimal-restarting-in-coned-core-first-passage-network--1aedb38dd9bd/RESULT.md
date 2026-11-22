# Universal optimal restarting in coned-core first-passage networks

## Finding

For every integer \(m\ge3\), let \(H\) be **any** simple graph on \(m-1\) vertices. Add a new vertex \(g\) adjacent to every vertex of \(H\), then attach the path \(g-s-u-a\). A continuous-time walker starts at \(s\), traverses each incident edge at rate one, and is absorbed upon reaching \(a\). Independently, at Poisson rate \(r\ge0\), the walker is instantaneously returned to \(s\). Let \(\tau_{m,H,r}\) denote the absorption time.

The **entire distribution** of \(\tau_{m,H,r}\) is independent of the internal edges of \(H\). Its mean is
\[
M_m(r)=\mathbb E\tau_{m,H,r}=
\frac{mr^2+4mr+2m+r^3+5r^2+6r+3}{mr+r^2+r+1}.
\]
For every \(m\ge3\), the mean has exactly one minimizer \(r_m\) on \([0,\infty)\), and \(0<r_m<\sqrt2\). The minimizer is the unique positive root of
\[
\begin{aligned}
F_m(r)={}&r^4+(2m+2)r^3+(m^2+2m+2)r^2\\
&+(4-2m)r+3-m-2m^2.
\end{aligned}
\]
The sharp large-core limits, including first corrections, are
\[
r_m=\sqrt2-\frac{1+3/(2\sqrt2)}m+O(m^{-2}),
\]
\[
M_m(r_m)=4+2\sqrt2-\frac{2+3\sqrt2/2}{m}+O(m^{-2}),
\qquad M_m(0)=2m+3.
\]
Thus optimal restart bounds mean absorption time as the core grows, while unrestarted absorption time diverges linearly. These results hold whether \(H\) is empty, complete, sparse, dense, connected, or disconnected.

## Assumptions and scope

All graphs are finite, undirected, simple and unweighted. Every edge rings at its own rate one for the walker; the total outward jump rate therefore equals the vertex degree. The target \(a\) is absorbing. Reset events are independent of edge clocks, do not consume additional time, and send any nonabsorbed state to \(s\); reset events while already at \(s\) do not alter the state. No claim is made for degree-normalized jump probabilities or nonzero reset overhead.

## Proof

**1. Strong lumpability, including the law.** Partition the nonabsorbed vertices into four classes \(\{s\}\), \(\{u\}\), \(\{g\}\), and \(B=V(H)\). From any vertex of \(B\), the rate of transition to \(g\) is precisely one and the rate of reset to \(s\) is \(r\), regardless of its other neighbors in \(B\). A transition within \(B\) does not change its class. From \(g\), the aggregate rate to \(B\) is \(m-1\). All other class transitions are likewise independent of the choice of \(H\). The partition together with the absorbing singleton \(\{a\}\) is therefore strongly lumpable, with a common finite-state generator for every \(H\). As the initial class is \(\{s\}\), the full hitting-time law of \(a\), not just its mean, is identical for every \(H\).

**2. Exact backward equations.** Write \(S,U,G,B_0\) for the expected remaining absorption times starting in the four classes. Since all rates are per edge and reset events at \(s\) do not change state, the backward equations are
\[
\begin{aligned}
2S&=1+U+G,\\
(2+r)U&=1+(1+r)S,\\
(m+r)G&=1+(m-1)B_0+(1+r)S,\\
(1+r)B_0&=1+G+rS.
\end{aligned}
\]
The coefficient matrix is the negative of the killed-chain generator. Absorption occurs almost surely with finite mean for every finite \(m\) and \(r\ge0\): from any state there exists a bounded-length positive-probability route to \(a\), uniformly over the finitely many states. Hence the finite linear system has a unique solution. Elementary elimination gives
\[
S=M_m(r)=\frac{mr^2+4mr+2m+r^3+5r^2+6r+3}{mr+r^2+r+1}.
\]
In particular \(M_m(0)=2m+3\).

**3. Global uniqueness of optimal restarting.** Differentiation yields
\[
M_m'(r)=\frac{F_m(r)}{(mr+r^2+r+1)^2}.
\]
For every \(m\ge3\), the coefficients of \(F_m\), in descending degree, have signs \(+,+,+,-,-\). Descartes' rule of signs gives at most one positive root, counted with multiplicity. Since \(F_m(0)=3-m-2m^2<0\) and \(F_m(r)\to\infty\) as \(r\to\infty\), there is exactly one positive root and the derivative changes from negative to positive there. Moreover
\[
F_m(\sqrt2)=m(3+2\sqrt2)+11+8\sqrt2>0,
\]
so the minimizer lies strictly between zero and \(\sqrt2\). The formula also shows \(M_m(r)\to\infty\) as \(r\to\infty\), ensuring this is the global minimizer.

**4. Large-core asymptotics.** For each fixed \(r>0\),
\[
\lim_{m\to\infty}M_m(r)=r+4+\frac2r.
\]
The minimizers are confined to \((0,\sqrt2)\). Dividing \(F_m\) by \(m^2\) gives \(r^2-2+O(m^{-1})\) uniformly on this interval. Root uniqueness then implies \(r_m\to\sqrt2\). Substitution of \(r_m=\sqrt2+c/m+O(m^{-2})\) into \(F_m(r_m)=0\) gives \(c=-1-3/(2\sqrt2)\); the implicit function theorem applies to the simple limiting root. Expanding the rational expression for \(M_m\) at this rate yields
\[
M_m(r_m)=4+2\sqrt2-\frac{2+3\sqrt2/2}{m}+O(m^{-2}).
\]
This proves every part of the finding.

## Verification

The accompanying `verify.py` checks the derivative polynomial, limiting expansion and first-order correction symbolically. It independently constructs full labelled killed generators for four different internal-core structures at each of six core sizes, solving the mean-hitting equations at three rational reset rates. It also compares nonzero Laplace transforms for additional full-generator instances. Its 96 independent exact rational comparisons passed. These finite tests support, but do not replace, the all-graph lumpability proof and all-parameter polynomial argument.

Reproduce with `python verify.py` using Python 3.10+ and SymPy.

## Relationship to prior work

Evans and Majumdar (2011) introduced the Poisson resetting first-passage framework for diffusion. Reuveni (2016) and Pal and Reuveni (2016) gave universal statements and renewal identities for first passage under restart. Riascos, Boyer, Herringer and Mateos (2019/2020) derived spectral first-passage formulas for degree-normalized discrete-time resetting walks on arbitrary networks. None of these full texts gives the particular per-edge-rate, coned-core invariance and universal \(\sqrt2\) optimizer established here.

Related indexed results address resetting to a **clique gateway** in clique–path networks, resetting from an **initial leaf** in two-hub trees, and resetting to an **apex** with competing pendant targets. Their resetting locations and/or targets differ: changing the restart point alters the backward equations and can reverse whether restart helps. Exact textual and implication comparisons are detailed in `AUDIT.json` and `REVIEW.md`. Full text of those indexed records was not available for inspection; no definitive historical-priority certification is claimed.

## Limitations

The result depends critically on unit **edge** rates and a universal gateway adjacent to every internal-core vertex. It concerns a single absorbing terminal, a reset vertex two edges from that terminal, and cost-free instantaneous Poisson resets. It gives exact finite means and hitting-time-law invariance, not a claim of optimality among non-Poisson restart clocks or of nonuniform edge-rate universality. The optimum is mathematically exact but has not undergone independent external review.

## References

- M. R. Evans and S. N. Majumdar, *Diffusion with Stochastic Resetting*, arXiv:1102.2704, first public 2011-02-14, https://arxiv.org/abs/1102.2704.
- S. Reuveni, *Optimal stochastic restart renders fluctuations in first passage times universal*, arXiv:1512.01600, first public 2015-12-05, https://arxiv.org/abs/1512.01600.
- A. Pal and S. Reuveni, *First Passage Under Restart*, arXiv:1607.06048, first public 2016-07-20, https://arxiv.org/abs/1607.06048.
- A. P. Riascos, D. Boyer, P. Herringer, and J. L. Mateos, *Random walks on networks with stochastic resetting*, arXiv:1910.13568, first public 2019-10-29, https://arxiv.org/abs/1910.13568.
