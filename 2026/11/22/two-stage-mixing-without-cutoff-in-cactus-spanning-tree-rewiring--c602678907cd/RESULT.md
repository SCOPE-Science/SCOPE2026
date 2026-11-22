# Two-stage mixing without cutoff in cactus spanning-tree rewiring

## Finding

Fix any real \(\alpha>0\). For each integer \(L\ge3\), put \(c_L=\lfloor e^{L/\alpha}\rfloor\), and let \(G_L\) be the simple cactus made of one triangle and \(c_L\) cycles of length \(L\), with all cycles meeting at exactly one common vertex and otherwise disjoint. Let \(q_L=2+c_L(L-1)\), the number of edges in every spanning tree of \(G_L\). Consider the **cut-first exchange chain**: from a spanning tree, delete one of its \(q_L\) edges uniformly, then reconnect the resulting components by choosing uniformly among all host edges crossing that cut, *including the edge just deleted*.

The unique stationary law \(\pi_L\) is uniform on spanning trees. Let \(d_L(t)\) be the total-variation distance from \(\pi_L\) after \(t\) steps, from any deterministic initial spanning tree (all starts give the same distance). For each fixed \(u>0\),

\[
\lim_{L\to\infty}d_L(\lfloor q_Lu\rfloor)=
\begin{cases}
1,&0<u\le 1/\alpha,\\
\frac23e^{-3u/2},&u>1/\alpha.
\end{cases}
\]

The discontinuity at \(1/\alpha\) has a precise microscopic transition profile. Set

\[
t_L(s)=\left\lfloor\frac{q_L}{L}\bigl(\log c_L+\log(L-1)+s\bigr)\right\rfloor,
\quad \eta_\alpha=e^{-3/(2\alpha)},\quad v_s=e^{-s}.
\]

Let \(Z_s\sim N(-v_s/2,v_s)\). Independently, let \(A_\alpha\) be \(1+2\eta_\alpha\) with probability \(1/3\), and \(1-\eta_\alpha\) with probability \(2/3\). Then, for every fixed \(s\in\mathbb R\),

\[
\lim_{L\to\infty}d_L(t_L(s))=F_\alpha(s)
:=\frac12\mathbb E\left|A_\alpha e^{Z_s}-1\right|.
\]

The profile decreases from \(1\) to the **strictly positive plateau** \(2\eta_\alpha/3\). In particular there is no total-variation cutoff. Writing \(t_{\mathrm{mix},L}(\epsilon)=\min\{t:d_L(t)\le\epsilon\}\), the exact first-order mixing-time dichotomy is

\[
\lim_{L\to\infty}\frac{t_{\mathrm{mix},L}(\epsilon)}{q_L}=
\begin{cases}
1/\alpha,&2\eta_\alpha/3<\epsilon<1,\\
\frac23\log\!\frac{2}{3\epsilon},&0<\epsilon<2\eta_\alpha/3.
\end{cases}
\]

No limiting claim is made here at the single boundary \(\epsilon=2\eta_\alpha/3\).

## Assumptions and scope

All graphs are finite simple connected undirected graphs. Each flower cycle has its own nonhub vertices, so distinct cycles share only the hub. Every step uses one uniformly chosen currently present tree edge, then one uniformly chosen crossing host edge; in particular holding is allowed. Total variation is half the sum of absolute state-mass differences. The limit sends integer \(L\) to infinity with **fixed** \(\alpha\); the exponentially growing number of long cycles is part of the theorem's specified graph sequence. All logarithms are natural.

## Proof

**1. Exact product chain.** On a cactus, each spanning tree retains all bridges and omits exactly one edge from each cycle. Thus a tree of \(G_L\) corresponds bijectively to \(x\in\{1,2,3\}\times\{1,\ldots,L\}^{c_L}\), where each coordinate names the omitted edge. Deleting a tree edge on one cycle creates precisely two reconnecting host edges: the deleted edge and the originally omitted edge. A transition between two states differing in exactly one coordinate therefore has probability \(1/(2q_L)\); all other off-diagonal transitions have probability zero. This symmetric, irreducible, holding chain has the uniform law as its unique stationary measure. If \(U_i\) resamples coordinate \(i\) uniformly and \(\ell_i\) is its cycle length, the transition operator is

\[
P_L=I+\sum_i\frac{\ell_i}{2q_L}(U_i-I),
\qquad(\ell_i)=(3,L,\ldots,L).
\]

The product-mean-zero eigenspace indexed by a subset \(S\) of coordinates has eigenvalue \(1-\sum_{i\in S}\ell_i/(2q_L)\) and multiplicity \(\prod_{i\in S}(\ell_i-1)\). All eigenvalues are nonnegative. In particular the exact chi-square distance at integer time \(t\) is

\[
\chi_L^2(t)=\sum_{\substack{z\in\{0,1\},\ 0\le k\le c_L\\(z,k)\ne(0,0)}}
2^z\binom{c_L}{k}(L-1)^k
\left(1-\frac{3z+kL}{2q_L}\right)^{2t}.
\]

**2. Continuous-time coordinate laws.** In continuous time with semigroup \(\exp[t(P_L-I)]\), coordinates evolve independently. A coordinate of size \(\ell\), started at one symbol, has distribution \((1-\varepsilon_\ell(t))U_\ell+\varepsilon_\ell(t)\delta_{\mathrm{start}}\), with \(\varepsilon_\ell(t)=\exp[-\ell t/(2q_L)]\). Relative to uniform stationarity its likelihood factor equals \(1+\varepsilon_\ell(t)(\ell\mathbf1\{X=\mathrm{start}\}-1)\).

At the central time \(t=t_L(s)\), elementary substitution gives

\[
c_L(L-1)\varepsilon_L(t)^2\longrightarrow e^{-s}=v_s,
\qquad\varepsilon_3(t)\longrightarrow\eta_\alpha.
\]

Under the stationary product law, the log-likelihood of the \(c_L\) long coordinates converges to \(N(-v_s/2,v_s)\). To verify this without a heuristic central limit step, each centered factor uses \(B=L\mathbf1\{X=\mathrm{start}\}-1\), for which \(\mathbb EB=0\), \(\mathbb EB^2=L-1\), and \(\mathbb E|B|^3=O(L^2)\). The Taylor remainder across all long factors is bounded in expectation by \(O(c_LL^2\varepsilon_L^3)=O(\sqrt{L/c_L})=o(1)\), while the centered sum satisfies Lindeberg because \(L\varepsilon_L=O(\sqrt{L/c_L})=o(1)\). Its mean and variance tend to \(-v_s/2\) and \(v_s\). Uniform integrability of the long likelihood follows from its exact second moment \([1+(L-1)\varepsilon_L^2]^{c_L}\to e^{v_s}\). The independent triangular coordinate contributes \(A_\alpha\). Therefore the continuous-time total-variation limit is \(F_\alpha(s)\).

**3. Discrete versus continuous time.** For an eigenspace with \(k\) long and \(z\) triangular nonconstant coordinates, write \(\delta_{k,z}=(kL+3z)/(2q_L)\). The squared \(L^2(\pi_L)\)-difference between the discrete-time mass ratio and the continuous-time mass ratio is exactly the multiplicity-weighted sum of

\[
\big[(1-\delta_{k,z})^t-e^{-t\delta_{k,z}}\big]^2.
\]

At \(t=t_L(s)\), each fixed \((k,z)\) contributes \(o(1)\), since \(t\delta_{k,z}^2=O(L(k+1)^2/c_L)\to0\). The summands are dominated by a summable multiple of \(C_s^k/k!\), using \(\binom{c_L}{k}\le c_L^k/k!\) and the bound \((1-\delta)^t\le e^{-t\delta}\). Dominated convergence proves the entire \(L^2\)-difference is \(o(1)\), hence so is total variation. The same argument applies at \(t=\lfloor q_Lu\rfloor\) for each \(u>1/\alpha\).

**4. Macroscopic regimes.** At \(u>1/\alpha\), the long-coordinate chi-square distance vanishes, because

\[
\bigl(1+(L-1)e^{-Lu+o(1)}\bigr)^{c_L}-1\longrightarrow0.
\]

The triangular coordinate alone has total-variation distance \((2/3)e^{-3u/2}\). For \(0<u\le1/\alpha\), instead count long coordinates still in their initially omitted-edge state. Their mean exceeds the stationary mean \(c_L/L\) by \(c_L(1-1/L)(1-L/(2q_L))^{\lfloor q_Lu\rfloor}\). The indicators have nonpositive pairwise covariances, since the two-coordinate eigenvalue \(1-L/q_L\) does not exceed the square of the one-coordinate eigenvalue \((1-L/(2q_L))^2\). Consequently the variance under the evolving law is at most its mean, whereas under stationarity it is at most \(c_L/L\). As \(c_Le^{-Lu}\ge c_Le^{-L/\alpha}\asymp1\), the squared separation of the two means dominates both variances by a factor tending to infinity (at the boundary the factor is at least order \(L\)). A Chebyshev separating event gives total variation tending to one.

**5. Mixing times and absence of cutoff.** The central profile tends to one as \(s\to-\infty\) and to \(2\eta_\alpha/3\) as \(s\to+\infty\), by convergence of \(e^{Z_s}\) and bounded likelihood moments. Monotonicity of total variation with time and the two macroscopic limits then yield the displayed mixing-time formula for every \(\epsilon\) except the plateau level. The two branches have different limiting mixing times on the \(q_L\) scale, ruling out a cutoff.

## Verification

The standalone script `verify_cactus_chain.py` independently enumerates spanning trees of small cactus flowers; constructs the full cut-and-reconnect transition kernel directly from graph cuts using exact rational arithmetic; checks the product-coordinate kernel, reversibility, all coordinate-subset eigenfunctions, and exact spectral chi-square identities through five steps. It also computes the lumped mismatch-count chains and compares finite total-variation distances with the stated limiting Gaussian and Gaussian–triangle profiles. Running `python verify_cactus_chain.py` completes **1,818 successful assertions** in the supplied implementation. Finite computations verify only small graph instances and numerical consistency, not the asymptotic proof.

## Relationship to prior work

Hora (1997) proves precise total-variation cutoff behavior for **homogeneous** Hamming graphs with varying alphabet size, an essential precursor but not a mixed one-triangle/exponentially-many-long-cycles law. Chen and Kumagai (2017) establish general product-chain cutoff criteria and comparison theory; their framework motivates, but does not itself state, the mixed exact limiting profile above. Russo, Teixeira, and Francisco (2018) study uniform spanning-tree generation via **insert-first** cycle exchange, with mixing bounds for cactus-type hosts; their transition rule is not the cut-first chain here. Mohamed (2014) concerns deterministic spanning-tree enumeration by restricted edge exchanges, rather than the uniform cut-first stochastic dynamics. All four should be credited as related prior methods rather than mistaken for this exact claim. A published cactus minimum-spanning-tree **weight-refresh** theorem instead studies the number of changed deleted-cycle maxima, not this exchange-chain convergence. A published **fastest-mixing** theorem for heterogeneous clique products optimizes a one-step spectral radius; it does not address this prescribed chain or its two-stage total-variation profile.

## Limitations

The flower graphs and the exponential cycle-growth balance are specifically chosen; no universal two-scale theorem is asserted for all cacti or all spanning-tree samplers. The mixing-time boundary at \(\epsilon=2\eta_\alpha/3\) is not resolved here. The general product-chain literature may contain formulations from which some conclusions can be deduced; the exact mixed law has not been independently priority-verified. The original full PDF of Mohamed (2014) was not accessible during comparison, so only its dated abstract and method description were inspected. Independent mathematical audit is not claimed.

## References

1. N. Mohamed, *Enumeration of Spanning Trees Using Edge Exchange with Minimal Partitioning*, arXiv:1407.0699, first posted 2014-07-02, https://arxiv.org/abs/1407.0699.
2. A. Hora, *The Cut-Off Phenomenon for Random Walks on Hamming Graphs with Variable Growth Conditions*, Publ. RIMS Kyoto Univ. 33 (1997), 695–710, https://doi.org/10.2977/prims/1195145152.
3. G.-Y. Chen and T. Kumagai, *Cutoffs for Product Chains*, arXiv:1701.06665 (2017); Stochastic Processes and their Applications 128 (2018), 3840–3879, https://arxiv.org/abs/1701.06665.
4. L. M. S. Russo, A. S. Teixeira and A. P. Francisco, *Linking and Cutting Spanning Trees*, Algorithms 11 (2018), article 53, https://doi.org/10.3390/a11040053.
