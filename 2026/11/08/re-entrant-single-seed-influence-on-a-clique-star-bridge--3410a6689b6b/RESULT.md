# Re-entrant single-seed influence on a clique–star bridge

## Finding
For every integer \(q\ge4\), let \(G_q\) consist of a clique \(K_q\), a star with center \(u\) and exactly \(q\) leaves, and one bridge joining \(u\) to a marked clique vertex \(v\). Independently retain every undirected edge with probability \(p\in(0,1)\). Let \(I_x(p)\) be the expected size of the open-edge component containing seed \(x\), including the seed itself. The only possible globally maximizing seeds are \(u\) and \(v\). Although \(\deg(u)=q+1>q=\deg(v)\), \(u\) is uniquely optimal for all sufficiently small and all sufficiently large \(p\), whereas \(v\) is uniquely optimal at \(p=1/2\), with the quantitative bound
\[
I_v(1/2)-I_u(1/2)\ge \frac{7q-23}{64}>0.
\]
Consequently there are at least two changes of optimal seed on every \(G_q\), \(q\ge4\).

The cutoff \(q=4\) is sharp within this balanced clique–star family: for \(q=2,3\), \(u\) is uniquely optimal for every \(p\in(0,1)\). For \(q=4\) (nine vertices), exactly two switching probabilities \(p_-<p_+\) exist, the only zeros in \((0,1)\) of
\[
 f(p)=1-6p+21p^3-21p^4+6p^5.
\]
They satisfy \(0.184<p_-<0.185\) and \(0.709<p_+<0.710\), approximately \(0.1849230526\) and \(0.7093317407\). The unique optimum is \(u\) when \(0<p<p_-\) or \(p_+<p<1\), and \(v\) when \(p_-<p<p_+\); at either switch exactly \(u,v\) tie.

## Assumptions and scope
The graph is simple, fixed and undirected. All edges survive independently with the *same* probability \(p\), and exactly one node is chosen as the seed. The reachable set is the seed's connected component in the resulting random subgraph; the objective is its expected cardinality, not the probability of reaching a prescribed target, a multi-seed objective or a temporal/SIS model. This is the independent-edge final-size contagion model; it should not be conflated with a general SIR process with correlated edge transmissions or with multilayer time-scheduled dynamics. The number of leaves is deliberately matched to the clique order, making the star center have precisely one more neighbor than the clique bridge vertex.

Write \(r_q(p)=\Pr(a\leftrightarrow b\text{ in }G(q,p))\) for two distinct fixed vertices of a percolated clique \(K_q\), and \(c_q(p)=1+(q-1)r_q(p)\), the expected size of its component containing a fixed vertex. All asymptotic and uniqueness assertions refer to \(0<p<1\); the degenerate endpoints are excluded.

## Proof
**1. The two candidate seeds.** The bridge is the only connection between the clique and star. For the star center, the expected number of vertices reached in its own star is \(1+qp\). Crossing the bridge occurs with probability \(p\), after which the expected clique contribution is \(c_q(p)\). Hence
\[
 I_u(p)=1+qp+p c_q(p).
\]
For seed \(v\), the clique contribution is \(c_q(p)\); crossing the bridge brings the star center and on average \(qp\) leaves. Thus
\[
 I_v(p)=c_q(p)+p(1+qp),\qquad
 I_u-I_v=(1-p)\bigl(1+qp-c_q(p)\bigr)
 =p(1-p)\left(q-(q-1)\frac{r_q(p)}p\right).
\]
Any other clique vertex \(w\) has the same expected within-clique contribution \(c_q(p)\), but must first connect to \(v\) before reaching the star. Its outside contribution is \(r_q(p)p(1+qp)\), strictly below \(v\)'s \(p(1+qp)\) because \(r_q(p)<1\) for \(0<p<1\). For any star leaf \(\ell\), in each edge configuration its cluster agrees with the center's cluster when \(u\ell\) is open, and is a singleton when \(u\ell\) is closed. The center's cluster is at least as large, and strictly larger on a positive-probability event. Thus \(I_\ell<I_u\). All global optimizers are therefore in \(\{u,v\}\).

**2. Re-entrance for every \(q\ge4\).** The direct clique edge shows \(r_q(p)=p+O(p^2)\) as \(p\downarrow0\), while \(r_q(1)=1\). Therefore \(q-(q-1)r_q(p)/p\) tends to \(1\) at both endpoints, and \(I_u>I_v\) for sufficiently small and sufficiently large interior probabilities. At \(p=1/2\), if the direct edge is closed, each of the \(q-2\) edge-disjoint two-edge routes via an intermediate vertex is open independently with probability \(1/4\). Counting just these routes yields
\[
 r_q(1/2)\ge\frac12+\frac12\left[1-\left(\frac34\right)^{q-2}\right]
 \ge \frac{23}{32}\quad(q\ge4).
\]
The expression for \(I_v-I_u\) then gives
\[
 I_v(1/2)-I_u(1/2)
 =\frac12\left[(q-1)r_q(1/2)-\frac q2\right]
 \ge\frac{7q-23}{64}>0.
\]
Continuity forces at least two interior optimality switches for each \(q\ge4\). For \(q=2\), \(r_2=p\) and the bracket in Step 1 is identically \(1\). For \(q=3\), \(r_3=p+p^2-p^3\) so \(r_3/p=1+p-p^2\le5/4\); the bracket is at least \(3-2(5/4)=1/2>0\). No switching occurs for \(q=2,3\).

**3. Complete nine-vertex phase diagram.** For \(q=4\) write the two unmarked clique vertices as \(a,b\). If the marked-to-target direct edge is closed, condition on whether \(ab\) is open. If it is closed, there are two independent two-edge alternative paths, giving connection probability \(2p^2-p^4\); if it is open, connection requires at least one edge from the source to \(\{a,b\}\) and at least one from \(\{a,b\}\) to the target, giving \((2p-p^2)^2\). It follows exactly that
\[
 r_4(p)=p+(1-p)\left[(1-p)(2p^2-p^4)+p(2p-p^2)^2\right]
 =p+2p^2-7p^4+7p^5-2p^6.
\]
Thus \(I_u-I_v=p(1-p)f(p)\) with the stated quintic \(f\). Put \(t=p/(1-p)>0\). Direct expansion gives
\[
 (1+t)^5 f\!\left(\frac{t}{1+t}\right)
 =t^5+2t^4-5t^3-14t^2-t+1.
\]
Its nonzero coefficient signs in descending order change exactly twice, so Descartes' rule bounds its positive roots, counting multiplicity, by two. Since \(f(0)=f(1)=1\) and \(f(1/2)=-1/2\), the intermediate-value theorem supplies two distinct roots in \((0,1)\), hence exactly two. Direct rational substitution isolates the first between \(184/1000\) and \(185/1000\), and the second between \(709/1000\) and \(710/1000\). Continuity and root uniqueness give the full optimality pattern, with all other vertices strictly inferior by Step 1.

## Verification
Run `python3 verify.py` in the directory containing the accompanying file. The standard-library-only verifier prints a PASS summary after 68 exact checks. It independently enumerates all \(2^{11}\) edge states of \(G_4\), computes a full polynomial for each seed's expected component size, checks the two analytic formulas, independently enumerates clique connection reliability, checks the Descartes transform and root brackets with rational arithmetic, and verifies the strict topological optimizer at three exact rational probabilities. It also compares a separate connected-graph recurrence with the four-clique calculation and checks finite examples of the all-size inequality. The all-\(q\) assertion is proved by the two-hop argument above, not by a finite enumeration.

## Relationship to prior work
Lin, Yang, Liu, Chen and Tessone (2022) analyze dynamics-dependent rankings of influential spreaders using a dynamic Markov approximation. Zhang, Xie, Liu and Zhan (2023) study heuristic influence maximization under a multilayer independent-cascade model. Min (2017) derives message-passing estimates of single-seed epidemic reach on locally tree-like networks. Mann et al. (2021) provide exact percolation expressions for clique motifs and giant-component thresholds. Erkol, Castellano and Radicchi (2019) compare empirical seed-ranking heuristics. The independent-edge objective and clique connectivity are established notions, not claimed as new. The contribution assessed here is the explicit balanced clique–star *global seed-ranking* reversals for every clique size, the sharp first instance and its two exact switch boundaries. Those statements are not asserted or immediately supplied as classification theorems by the inspected sources.

## Limitations
The theorem does not describe all switch counts for \(q>4\), multiple seeds, directed or heterogeneous transmission, recovery-time correlations, or competing information. \(p=0\) and \(p=1\) are excluded because all seeds tie. The exact clique reliability polynomial is elementary/known methodology; the novelty assessment concerns its combination with exact global optimizer transitions. No claim of comprehensive literature coverage or independent external validation is made. A potentially relevant older work on parameter-sensitive epidemic centrality could be inspected only through openly available summary information, leaving a residual priority risk.

## References
1. J.-H. Lin, Z. Yang, J.-G. Liu, B.-L. Chen, C. J. Tessone, *Rank the spreading influence of nodes using dynamic Markov process*, first public 2022-06-17, https://arxiv.org/abs/2206.08764 .
2. S.-S. Zhang, M. Xie, C. Liu, X.-X. Zhan, *Influence maximization in multilayer networks based on adaptive coupling degree*, first public 2023-11-15, https://arxiv.org/abs/2311.08663 .
3. P. Mann et al., *An exact formula for percolation on higher-order cycles*, first public 2021-02-18, https://arxiv.org/abs/2102.09261 .
4. B. Min, *Identifying an influential spreader from a single seed in complex networks via a message-passing approach*, first public 2017-10-19, https://arxiv.org/abs/1710.07064 .
5. S. Erkol, C. Castellano, F. Radicchi, *Systematic comparison between methods for the detection of influential spreaders in complex networks*, *Scientific Reports* 9 (2019), https://doi.org/10.1038/s41598-019-51209-6 .
6. M. Šikić et al., *Epidemic centrality—is there an underestimated epidemic impact of network peripheral nodes?*, *European Physical Journal B* 86 (2013), https://doi.org/10.1140/epjb/e2013-31025-5 .
