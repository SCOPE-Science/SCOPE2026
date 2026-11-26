# Half-Gumbel physical stabilization times for sparse conflict graphs

## Finding

Consider the standard conflict-guard, free-color vertex-recoloring rule with independent rate-one Poisson activation clocks. Measure **elapsed physical time to a proper coloring**, not the number of recolorings. Write \(H\) for the graph of initially monochromatic edges, \(m=|E(H)|\), and \(D_2(H)=\sum_{v\in V(H)}d_H(v)(d_H(v)-1)\). Let \(T\) be the elapsed stabilization time. For any finite \(H\), any \(t\ge0\), and \(q=e^{-t}\),

\[
\Pr(T\le t)=\sum_{I\subseteq V(H):\,I\,\mathrm{independent}}q^{|I|}(1-q)^{|V(H)|-|I|}.
\]

Moreover, if \(Z_t\) is the number of initial-conflict edges whose two endpoint clocks have not rung by \(t\), then \(\{T\le t\}=\{Z_t=0\}\) and the following quantitative Poisson bound holds:

\[
d_{\rm TV}\bigl(\mathcal L(Z_t),\operatorname{Pois}(m q^2)\bigr)
\le 2\bigl[(m+D_2(H))q^4+D_2(H)q^3\bigr].
\]

Consequently, for **every deterministic sequence** of finite initial conflict graphs \((H_n)\) satisfying

\[
m_n\longrightarrow\infty,\qquad D_2(H_n)=o(m_n^{3/2}),
\]

and every real \(x\),

\[
\lim_{n\to\infty}\Pr\left(2T_n-\log m_n\le x\right)=\exp(-e^{-x}).
\]

Thus the limit is the standard Gumbel law, with the factor two in the clock. This condition holds, for example, whenever the maximum conflict degree is \(o(\sqrt{m_n})\); it includes arbitrary bounded-degree conflict graphs with diverging edge counts, without connectivity or girth assumptions.

The degree-overlap hypothesis cannot simply be omitted. On a star with \(r\to\infty\) leaves, \(T\) converges to \(\operatorname{Exp}(1)\) without centering, whereas on a complete graph with \(n\to\infty\), \(T-\log n\) has limiting CDF \(e^{-e^{-x}}(1+e^{-x})\). These examples show qualitatively distinct high-degree behavior.

## Assumptions and scope

Let \(G=(V,E)\) be a finite simple undirected graph and let the initial vertex colors \(\gamma:V\to\mathcal C\) be fixed. Assume a palette with at least \(\Delta(G)+1\) colors. Each vertex has an independent homogeneous Poisson activation clock of rate one, also independent of any randomized free-color choices. Upon activation, a vertex changes its color if and only if an adjacent vertex presently shares that color, choosing any currently absent neighbor color in a single atomic operation. Disabled activations do nothing. Fix the initial conflict graph \(H=(V,\{uv\in E:\gamma(u)=\gamma(v)\})\). The elapsed physical stabilization time \(T\) is the first nonnegative time at which every edge is bichromatic. In a graph without initial conflicts, \(T=0\).

For comparison, the *number of successful recolorings* is a different random variable already investigated in the cited motivating paper; the present limit theorem concerns the clock time, with all untouched initial-conflict edges having to be resolved. The sequence \(H_n\) is deterministic; the same conditional conclusion applies to random initial conflict graphs on events where the deterministic assumptions and estimates hold, but no unconditional random-graph assertion is made here.

## Proof

**Step 1: a pathwise edge-clock representation.** Let \(\tau_v\) be the first activation of vertex \(v\). These variables are mutually independent \(\operatorname{Exp}(1)\). A recoloring never introduces a new same-color edge, because the selected new color is absent from all its current neighbors. Thus an edge that is initially bichromatic remains so forever. On an initially monochromatic edge \(uv\), both endpoint colors remain their original values until the first activation of either endpoint. At that first activation, the activated endpoint still has a conflict on \(uv\) and must recolor, so \(uv\) becomes bichromatic forever. Hence, *pathwise* for every realization without tied first clock arrivals,

\[
T=\max_{uv\in E(H)}\min(\tau_u,\tau_v),
\]

with the maximum of an empty edge set interpreted as zero. This gives \(Z_t=\sum_{uv\in E(H)}\mathbf1_{\{\tau_u>t,\tau_v>t\}}\) and the asserted identity between the events. No assumption on which free neighbor color is selected is needed.

**Step 2: an exact independent-set survival formula.** Put \(S_t=\{v:\tau_v>t\}\). Each vertex belongs to \(S_t\) independently with probability \(q=e^{-t}\). By Step 1, \(T\le t\) precisely when no edge of \(H\) is contained in \(S_t\), i.e. \(S_t\) is independent. Summing over all possible independent sets gives the displayed formula. Equivalently, for \(0\le q<1\) it is \((1-q)^{|V|}I_H(q/(1-q))\), with \(I_H(z)=\sum_{I\text{ independent}}z^{|I|}\); at \(q=1\) use the original finite sum.

**Step 3: quantitative rare-edge comparison.** For each \(e=uv\in E(H)\), set \(X_e=\mathbf1_{\{u,v\in S_t\}}\), so \(\mathbb EX_e=q^2\) and \(\mu=\mathbb E\sum_eX_e=mq^2\). Indicators indexed by vertex-disjoint edges depend on disjoint independent Bernoulli variables and are independent. The edge-intersection graph is therefore a dependency graph for the indicators. If \(d_v=d_H(v)\), the number of ordered pairs of distinct edges sharing a vertex is

\[
D_2=\sum_v d_v(d_v-1).
\]

In the standard dependency-graph Stein–Chen inequality (Arratia–Goldstein–Gordon), the two error sums are exactly \(b_1=(m+D_2)q^4\) and \(b_2=D_2q^3\): each edge contributes its self-pair to \(b_1\), and two distinct adjacent edges share exactly three endpoints, giving joint probability \(q^3\). The independent-outside-neighborhood term \(b_3\) is zero. The conservative form \(d_{\rm TV}\le2(b_1+b_2)\) proves the stated inequality for every finite graph and \(t\ge0\). The event of zero surviving edges then differs from \(e^{-mq^2}\) by at most the same error.

**Step 4: the universal window.** Put \(t=\frac12(\log m+x)\) and thus \(q=m^{-1/2}e^{-x/2}\), for a fixed real \(x\) and sufficiently large \(m\). The mean is \(mq^2=e^{-x}\). The Step 3 upper bound becomes

\[
2\left[e^{-2x}\left(m^{-1}+D_2m^{-2}\right)+e^{-3x/2}D_2m^{-3/2}\right]\longrightarrow0.
\]

Here \(D_2=o(m^{3/2})\) also implies \(D_2=o(m^2)\). Since \(\{2T-\log m\le x\}=\{Z_t=0\}\), the limit is \(e^{-e^{-x}}\), at every continuity point \(x\). Also \(D_2\le2m\Delta(H)\), giving the stated degree-based sufficient condition.

**Step 5: high-degree boundaries.** On a star with center \(c\) and \(r\) leaves, \(T=\min(\tau_c,\max_{1\le j\le r}\tau_j)\). The exact distribution is

\[
\Pr(T\le t)=(1-q)+q(1-q)^r.
\]

For every fixed \(t>0\), the second term vanishes as \(r\to\infty\), leaving \(1-e^{-t}\). For the complete graph, survival without an edge means at most one vertex has not activated; hence

\[
\Pr(T\le t)=(1-q)^n+nq(1-q)^{n-1}.
\]

Setting \(t=\log n+x\) gives the announced second-upper-order Gumbel CDF. Both examples violate the degree-overlap hypothesis. They establish the necessity of imposing some structural control before claiming a universal half-Gumbel law, not sharp necessity of this *particular* sufficient condition.

## Verification

A standalone Python checker, `checker.py`, uses only the standard library. It checks the pathwise clock-ranking identity for every labeled simple graph on at most four vertices, every three-color initial assignment and every first-activation ordering; the test recolors conflicts greedily using a palette of size \(n+1\), and compares properness at each prefix with the absence of surviving original conflict edges. It separately checks independence-polynomial distributions exactly over every labeled graph on at most five vertices at three rational retention probabilities, all ordered edge-pair overlap formulas on those graphs, and the star/complete graph boundary distributions. The checker passed 632,891 assertions. These finite tests do not prove the infinite-graph limit or the Stein–Chen inequality; the analytical proof above supplies those steps. To reproduce: run `python checker.py` in the directory containing that file.

## Relationship to prior work

De Panafieu, Mathieu, Potop-Butucaru and Tixeuil (2026), Lemma 1 and Propositions 1–2, establish the initial-conflict-graph reduction and the Poisson-clock scheduling interpretation for the **number of recolorings**. In particular, their Proposition 1(2) observes that the physical completion time equals the first tick of the last non-peak. Those components are credited, not new here. The contribution of the present result is the graph-uniform **elapsed-time** half-Gumbel theorem with a degree-overlap criterion, its explicit finite-size Poisson approximation bound, and contrasting high-degree limiting clocks. The classical Stein–Chen dependency-graph theorem is also credited as a proof ingredient, not new. The finite independent-set formula is a direct consequence of the known clock representation and is provided for exact interpretation, not as an independent originality claim.

Searches for equivalent formulations were conducted against the motivating paper and relevant published indexed graph-probability and stabilization literature. No inspected theorem directly supplies the displayed physical-time limit under \(D_2=o(m^{3/2})\); nonetheless, a possible unindexed statement or an implicit specialization of a broader vertex-percolation Poisson theorem cannot be excluded.

## Limitations

The result concerns **fixed initial configurations** and independent rate-one vertex clocks under atomic free-color updates. It does not cover adversarial or synchronous clocks, the Grundy guard, arbitrary recoloring policies that can introduce a conflict, simultaneous adjacent updates, or a time normalization based on the number of successful moves. The \(D_2=o(m^{3/2})\) hypothesis is sufficient rather than necessary. At finite \(m\), the provided bound may exceed one and is not claimed optimal; truncating it at one is harmless. Random graph models require separately establishing the overlap condition. Priority beyond inspected accessible literature is unverified, and there is no independent mathematical review.

## References

1. É. de Panafieu, F. Mathieu, M. Potop-Butucaru, and S. Tixeuil, *The Exact Stabilization Time of Self-Stabilizing Coloring: Mean, Variance, and Distribution*, arXiv:2611.17989v1, posted 2026-11-13, https://arxiv.org/abs/2611.17989 (especially Section 3, Lemma 1 and Propositions 1–2; comparison to Section 5 and Appendix A).
2. R. Arratia, L. Goldstein, and L. Gordon, *Two Moments Suffice for Poisson Approximations: The Chen–Stein Method*, Annals of Probability 17 (1989), 9–25, https://doi.org/10.1214/aop/1176991491 (dependency-graph Poisson bound).
