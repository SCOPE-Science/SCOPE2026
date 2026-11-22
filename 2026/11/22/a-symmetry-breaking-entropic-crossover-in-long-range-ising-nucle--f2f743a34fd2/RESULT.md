# A symmetry-breaking entropic crossover in long-range Ising nucleation

## Finding

A finite ferromagnetic Ising chain with almost spatially uniform coupling has an exact low-temperature crossover between **binomially many transition gates** and **two boundary-attached nucleation gates**. The scale separating the two is the product of inverse temperature and interaction-decay exponent; the crossover function is an explicit finite sum of logarithmic spatial cut gaps.

Fix an integer \(N\ge3\), \(J>0\), and \(0<h<J\). Put \(m=\lfloor N/2\rfloor\). Let \(\tau_+\) be the first passage from all negative spins to all positive spins under discrete-time serial Metropolis updates (one uniformly chosen site per time step). Denote by \(E=\{1,\ldots,m\}\) the leftmost set of positive spins and by \(\Gamma_q\) its energy above the all-negative configuration.

For any sequence of exponents \(q_\beta\ge0\) satisfying \(q_\beta\to0\) and \(\beta q_\beta\to\lambda\in[0,\infty]\),

\[
\lim_{\beta\to\infty}e^{-\beta\Gamma_{q_\beta}}\mathbb E_-\tau_+
=F_N(\lambda)
=\frac{N^2}{m(N-m)\displaystyle\sum_{\substack{S\subseteq[N]\\|S|=m}}e^{-\lambda G_N(S)}}.
\]

Here the nonnegative shape gaps are

\[
G_N(S)=2J\left(\sum_{\substack{i\in E\\j\notin E}}\log|i-j|-
\sum_{\substack{i\in S\\j\notin S}}\log|i-j|\right).
\]

Exactly the two edge intervals, \(E\) and its reflection, have gap zero. When \(\lambda=\infty\), only those two terms contribute. Therefore

\[
F_N(0)=\frac{N^2}{m(N-m)\binom Nm},\qquad
F_N(\infty)=\frac{N^2}{2m(N-m)}.
\]

The function is continuous, strictly increasing, and its limiting prefactors differ by the exact factor \(\binom Nm/2\). For each fixed sufficiently small \(q>0\), the \(\beta\to\infty\) prefactor also equals \(F_N(\infty)\). For \(N=4\), the six central-layer subsets contribute two copies of each gap \(0\), \(2J\log3\), and \(4J\log2\), so

\[
F_4(\lambda)=\frac{2}{1+e^{-2J\lambda\log3}+e^{-4J\lambda\log2}}.
\]

## Assumptions and scope

A state is specified by a subset \(S\subseteq[N]=\{1,\ldots,N\}\) of plus-spin sites. Write \(s_i(S)=1\) for \(i\in S\) and \(-1\) otherwise. Its open-boundary energy is

\[
H_q(S)=-J\sum_{1\le i<j\le N}|i-j|^{-q}s_i(S)s_j(S)-h\sum_{i=1}^{N}s_i(S),\qquad q\ge0.
\]

From \(S\), choose one site uniformly and propose the single spin flip \(S\triangle\{i\}\); accept it with probability \(\min\{1,e^{-\beta[H_q(S\triangle\{i\})-H_q(S)]}\}\). Otherwise remain in place. Each unit of time is one attempted update, not one attempted update per site. The process is reversible for the Gibbs weights. The hitting time \(\tau_+\) is the smallest nonnegative update count at the all-positive state, starting from \(S=\varnothing\).

Define

\[
\Gamma_q=H_q(E)-H_q(\varnothing)=2J\sum_{\substack{i\in E\\j\notin E}}|i-j|^{-q}-2hm.
\]

For the joint result, \(N,J,h\) stay fixed, \(q_\beta\to0\), and \(\beta\to\infty\). For the fixed-exponent endpoint result, there exists a constant \(q_0=q_0(N,J,h)>0\) such that the assertion holds for every \(0<q<q_0\). This is an existence statement, not an explicit optimal range for \(q\). The endpoint \(\lambda=\infty\) is also valid when \(q_\beta\to0\) and \(\beta q_\beta\to\infty\).

## Proof

**1. A uniformly separated central gate.** At \(q=0\), all \(k\)-plus states have the same energy relative to all-minus:

\[
B_0(k)=2Jk(N-k)-2hk.
\]

The differences are \(B_0(k)-B_0(k-1)=2J(N-2k+1)-2h\). Since \(0<h<J\), this strictly increases up to \(k=m\) and strictly decreases afterward (including both parities of \(N\)). Thus \(B_0(m)\) is the unique maximal magnetization-layer energy. Moreover, \(B_0(k)=2k[J(N-k)-h]>0\) for every \(1\le k<N\). The gaps between the central layer and both adjacent layers are positive. By continuity of the finitely many energies, these statements persist uniformly for all \(0\le q\le q_0\), after choosing \(q_0\) sufficiently small: every configuration outside layer \(m\) lies a fixed positive energy below *every* layer-\(m\) configuration, every mixed configuration is a fixed positive energy above all-minus, and every single-spin neighbor of a layer-\(m\) state lies below that state. The two sets

\[
\mathcal L=\{S:|S|<m\},\qquad \mathcal R=\{S:|S|>m\}
\]

are each connected by single-spin paths, and all their internal edge conductances are exponentially larger than those incident to the central layer.

**2. Edge-interval minimization and positive shape gaps.** For any strictly decreasing distance kernel \(w(1)>\cdots>w(N-1)\), the sum of \(w(|i-j|)\) over pairs *within* a fixed \(k\)-element set is maximized by consecutive sites. Indeed, for its sorted sites \(x_1<\cdots<x_k\), \(x_b-x_a\ge b-a\); summing the decreasing weights gives the claim, and strictness follows if a gap between successive sites exceeds one. The same is true for its complement. As the sum of all pair weights is fixed, minimizing the cross-cut interaction is equivalent to maximizing the two within-set interaction sums. Both sets can simultaneously be intervals exactly when they occupy opposite ends. Therefore the two end intervals are the unique minimizers of the cross-cut interaction for all strictly decreasing distance kernels. This applies to \(w(r)=Jr^{-q}\) for \(q>0\), and to \(w(r)=\log(N/r)\), which is also strictly decreasing.

There are exactly \(m(N-m)\) pairs crossing every cut \(S\) of size \(m\). Since \(\log(N/r)=\log N-\log r\), the previous minimization implies \(G_N(S)\ge0\), with equality only at the two end intervals. Expanding the energy in the exponent at \(q=0\) gives, uniformly over the finite collection of central-layer subsets,

\[
H_q(S)-H_q(E)=qG_N(S)+O(q^2).
\]

**3. Capacity reduction to parallel stars.** Denote the Gibbs law by \(\pi_\beta(S)=Z_\beta^{-1}e^{-\beta H_q(S)}\). The conductance of an allowed spin-flip edge is exactly

\[
c_\beta(S,T)=\pi_\beta(S)P_\beta(S,T)=\frac{e^{-\beta\max\{H_q(S),H_q(T)\}}}{NZ_\beta}.
\]

All edges wholly within \(\mathcal L\) or \(\mathcal R\) carry, relative to \(e^{-\beta[H_q(\varnothing)+\Gamma_q]}/Z_\beta\), an exponentially diverging conductance, uniformly in \(0\le q\le q_0\). The finite Dirichlet variational principle therefore short-circuits each connected basin to constant potential, \(1\) on \(\mathcal L\) and \(0\) on \(\mathcal R\), up to a relative \(o(1)\) in the resulting capacity. For completeness, the upper bound uses the trial potential constant on each basin; the lower bound follows because any minimizer with energy on the rare-gate scale has potential differences across the finite connected basin edges of order at most the square root of their conductance ratio. All bounds are uniform in \(q\le q_0\).

No spin flip joins two central-layer states. Each \(m\)-plus state \(S\) has \(m\) neighbors in \(\mathcal L\) and \(N-m\) neighbors in \(\mathcal R\), all of lower energy. Consequently the rare gate has \(m\) equal conductances and \(N-m\) equal conductances, each equal to \(\pi_\beta(S)/N\). Its optimal potential is \(m/N\), and its minimized energy contribution is

\[
\pi_\beta(S)\left[\frac{m}{N}\left(1-\frac mN\right)^2+
\frac{N-m}{N}\left(\frac mN\right)^2\right]
=\pi_\beta(S)\frac{m(N-m)}{N^2}.
\]

Summing these parallel gates gives the uniform capacity asymptotic

\[
\operatorname{cap}_\beta(\varnothing,[N])=
\frac{e^{-\beta H_q(\varnothing)}}{Z_\beta}
 e^{-\beta\Gamma_q}\frac{m(N-m)}{N^2}
\sum_{|S|=m}e^{-\beta[H_q(S)-H_q(E)]}(1+o(1)).
\]

**4. Convert capacity to the mean first-passage time.** The exact reversible-chain hitting identity for singleton endpoints is

\[
\mathbb E_{\varnothing}\tau_{[N]}=
\frac{\displaystyle\sum_S\pi_\beta(S)\,\Pr_S(\tau_{\varnothing}<\tau_{[N]})}
{\operatorname{cap}_\beta(\varnothing,[N])},
\]

with the equilibrium potential interpreted as \(1\) at \(\varnothing\) and \(0\) at \([N]\). All other mixed states have energy uniformly above \(H_q(\varnothing)\), while the all-plus state has potential zero. Hence the numerator equals \(\pi_\beta(\varnothing)(1+o(1))\), uniformly for \(q\le q_0\). Substitution proves the stronger intermediate statement

\[
e^{-\beta\Gamma_q}\mathbb E_{\varnothing}\tau_{[N]}
=\frac{N^2}{m(N-m)\displaystyle\sum_{|S|=m}e^{-\beta[H_q(S)-H_q(E)]}}(1+o(1))
\]

uniformly for sufficiently small nonnegative \(q\).

**5. Scale and endpoints.** If \(\beta q_\beta\to\lambda<\infty\), then \(\beta q_\beta^2\to0\); the finite gate sum converges to \(\sum_{|S|=m}e^{-\lambda G_N(S)}\). If \(\beta q_\beta\to\infty\) with \(q_\beta\to0\), strictness of every non-edge gap and the uniform expansion ensure its Boltzmann weight tends to zero. The same follows for fixed \(0<q<q_0\), since its non-edge energy gaps are strictly positive. At \(\lambda=0\), every one of the \(\binom Nm\) gates has unit weight; at \(\lambda=\infty\), only two do. Since at least one non-edge gate exists for \(N\ge3\), differentiating the denominator proves strict increase of \(F_N\). The six \(N=4\) subsets give the displayed explicit expression.

## Verification

The accompanying `checker.py` uses only the Python standard library. Run `python3 checker.py`. It independently enumerates the cross-log rearrangement for all subsets of each length for chain sizes \(3\le N\le10\), solves finite-state Metropolis first-passage linear systems using 75-digit Decimal arithmetic for small chains, compares their low-temperature ratios to the central-gate capacity approximation, and checks the exact three-level splitting for \(N=4\). The checker reports 2,049 successful finite checks. Computation corroborates, but does not replace, the finite-graph capacity proof above.

## Relationship to prior work

Jacquier's 2025 review surveys the metastability questions of critical droplets, energy barriers, and exact prefactors and specifically discusses the one-dimensional long-range model. Van Enter, Kimura, Ruszel, and Spitoni (2019) establish the long-range open-chain boundary droplet geometry and logarithmic Arrhenius exponent: their Theorem 3.2 gives \(\beta^{-1}\log\mathbb E\tau\to\Gamma\), not a microscopic multiplicative prefactor. The present claim accepts the established droplet geometry and classical potential-theoretic method; it calculates instead an explicit *temperature-dependent symmetry-breaking gate sum* when the distance exponent tends to zero, including the noncommuting fixed-positive-exponent and fully uniform-coupling prefactors.

Dommers, den Hollander, Jovanovski, and Nardi (2016) establish a general low-temperature energy–entropy prefactor framework on finite graphs, but do not evaluate this deterministic one-dimensional weak-exponent crossover. Jacquier's 2025 random-regular-graph paper bounds long-range metastable barriers in a different geometry. General capacity theory is not presented as new.

## Limitations

The theorem fixes the number of sites before sending inverse temperature to infinity. It proves no thermodynamic limit, no uniform estimate as \(N\to\infty\), no finite-temperature error constant, and no assertion for arbitrary larger decay exponents. It assumes free boundaries, a strictly positive field below \(J\), independent uniform site proposals, and the specified Metropolis acceptance rule; other kinetic normalizations change the prefactor. This is a self-review, not an independent external validation. The absence of a found equivalent formula does not establish absolute publication priority.

## References

1. V. Jacquier, *Exploring Metastability in Ising Models: Critical Droplets, Energy Barriers and Exit Time*, arXiv:2501.06163, first submitted 10 January 2025. https://arxiv.org/abs/2501.06163 ; journal version https://doi.org/10.1007/s11040-025-09514-2.
2. A. C. D. van Enter, B. Kimura, W. M. Ruszel and C. Spitoni, *Nucleation for One-Dimensional Long-Range Ising Models*, Journal of Statistical Physics **174** (2019), 1327–1345. https://doi.org/10.1007/s10955-019-02238-y.
3. S. Dommers, F. den Hollander, O. Jovanovski and F. Nardi, *Metastability for Glauber Dynamics on Random Graphs*, arXiv:1602.08900, first submitted 29 February 2016. https://arxiv.org/abs/1602.08900.
4. V. Jacquier, *Estimate of the Exit Time for the Long Range Ising Model on Random Regular Graphs*, arXiv:2509.02188, first submitted 2 September 2025. https://arxiv.org/abs/2509.02188.
5. A. Bovier, F. den Hollander and S. Marello, *Metastability for Glauber Dynamics on the Complete Graph with Coupling Disorder*, arXiv:2107.04543. https://arxiv.org/abs/2107.04543.
