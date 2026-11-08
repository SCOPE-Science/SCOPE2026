# Exact primitive-two chip-mass spectrum on complete split graphs

## Finding

Let \(G_{a,b}=K_a\vee\overline K_b\) be the labelled complete split graph, with \(a\ge2\) clique vertices and \(b\ge2\) independent vertices. Let \(F\) be the *loopless*, synchronous parallel chip-firing map: a vertex fires if its nonnegative integer chip count is at least its degree, sends one chip to each neighbour, and all firings occur simultaneously. Write
\[
H_{a,b}(z)=\sum_{\substack{x\in\mathbb Z_{\ge0}^{a+b}\\ F^2x=x,\ Fx\ne x}}z^{\sum_v x_v}.
\]
Set \([0]_z=0\) and \([r]_z=1+z+\cdots+z^{r-1}\) for \(r\ge1\), interpreting any zeroth power as one (including \([0]_z^0\)). Then the complete chip-mass distribution is the finite polynomial
\[
\boxed{\begin{aligned}
H_{a,b}(z)&=\sum_{k=0}^{a}\sum_{\ell=0}^{b}
\binom ak\binom b\ell\,z^{\mu(k,\ell)}
[a+b-k-\ell]_z^k[k+\ell]_z^{a-k}
[a-k]_z^\ell[k]_z^{b-\ell},\\
\mu(k,\ell)&=a(a+2b-1)-k(a+b)+k^2+\ell(2k-a).
\end{aligned}}
\]
Write \(S_{a,b}=2a(a-1)+4ab-a-b\). The polynomial is reciprocal,
\[
H_{a,b}(z)=z^{S_{a,b}}H_{a,b}(z^{-1}),
\]
and its nonzero coefficients occur **at every integer** in the interval
\[
\boxed{[L_{a,b},\ S_{a,b}-L_{a,b}]\cap\mathbb Z},\qquad
L_{a,b}=\begin{cases}
a(a+b-1),&b\ge a,\\
a(a+2b-1)-\lfloor(a+b)^2/4\rfloor,&2\le b<a.
\end{cases}
\]
Both endpoint coefficients equal
\[
\boxed{\begin{cases}
2,&b\ge a,\\
2\binom{a}{(a+b)/2},&2\le b<a,\ a+b\text{ even},\\
2\left(\binom{a}{\lfloor(a+b)/2\rfloor}+\binom{a}{\lceil(a+b)/2\rceil}\right),&2\le b<a,\ a+b\text{ odd}.
\end{cases}}
\]
Every coefficient is even; half of \(H_{a,b}(z)\) is the exact chip-mass generating polynomial of distinct primitive-two temporal orbits. In particular \(H_{4,2}(1)=14880\), with support \([19,31]\) and eight configurations at each endpoint.

## Assumptions and scope

The clique and independent set are fully labelled, and no vertex is a sink. Vertices have degrees \(d=a+b-1\) (clique) and \(a\) (independent set). A configuration is counted only when *already* on a least-period-two orbit at time zero; no transient or attraction-basin census is asserted. The result is about synchronous fixed-energy dynamics, not the sink-based Abelian sandpile model. The range \(b\ge2\) excludes the degenerate complete-graph specialization \(b=1\).

## Proof

**1. Exactly one firing per vertex.** For any connected undirected graph, if \(F^2x=x\), let \(s_v\in\{0,1,2\}\) be the number of firings of vertex \(v\) in these two updates. Conservation of the initial chip vector after two updates means the graph Laplacian annihilates \(s\). Since the graph is connected, all \(s_v\) are equal. If that common number is zero, no vertex fires and \(Fx=x\); if it is two, every vertex fires in both rounds and \(Fx=x\). Therefore a primitive-two configuration has \(s_v=1\) for every vertex, and the first-round firing set is complemented in the second round. Conversely, any valid complementary firing pattern gives \(F^2x=x\); since the pattern has opposite firings in consecutive rounds, the least period is two.

**2. Exact local intervals.** Designate phase \(0\) as firing in the first round, and phase \(1\) as waiting in the first round. If \(v\) has degree \(d_v\) and exactly \(q_v\) phase-zero neighbours, the first-round firing rule and the required opposite second-round firing rule yield precisely
\[
\begin{array}{ll}
\text{phase }0:& d_v\le x_v\le 2d_v-q_v-1,\\
\text{phase }1:& d_v-q_v\le x_v\le d_v-1.
\end{array}
\]
The lengths are \(d_v-q_v\) and \(q_v\), respectively. Nonempty intervals imply nonnegative counts. For the split graph, suppose exactly \(k\) clique vertices and \(\ell\) independent vertices fire in round one. The four vertex types (clique phase zero, clique phase one, independent phase zero, independent phase one) have lower bounds and interval lengths
\[
\begin{array}{c|c|c|c}
\text{type}&\text{multiplicity}&\text{lower bound}&\text{length}\\\hline
C_0&k&d&a+b-k-\ell\\
C_1&a-k&d-k-\ell&k+\ell\\
I_0&\ell&a&a-k\\
I_1&b-\ell&a-k&k
\end{array}
\]
where \(d=a+b-1\). Intervals for distinct vertices are independent once the phases are fixed. Their generating polynomial is the product of the corresponding shifted interval polynomials. Summing over the \(\binom ak\binom b\ell\) labelled phase choices proves the displayed exact formula, including the convention that impossible phase patterns contribute zero.

**3. Sharp minimum.** Summing the four lower bounds gives \(\mu(k,\ell)\). Its dependence on \(\ell\) is affine with slope \(2k-a\). If \(k\ge a/2\), the minimum occurs at \(\ell=0\); if \(k<a/2\), at \(\ell=b\). The latter pattern is a temporal-phase complement of the pattern with parameters \((a-k,0)\), and the two have the same possible conserved masses via one update. Thus a global minimum is achieved among \((k,0)\) with \(\lceil a/2\rceil\le k\le a\). All such patterns are admissible: the first-round firing clique vertices have a waiting neighbour, and all other vertices have a firing clique neighbour. Minimizing
\[
\mu(k,0)=a(a+2b-1)-k(a+b)+k^2
\]
over these integers places \(k\) at the nearest integer to \((a+b)/2\), truncated at \(a\), and yields \(L_{a,b}\) as stated.

**4. No missing interior masses and reciprocity.** Every primitive-two coordinate satisfies \(0\le x_v\le2d_v-1\). Define \((Cx)_v=2d_v-1-x_v\). Complementation reverses firing status and satisfies \(F(Cx)=C(Fx)\) on these confined configurations, so it maps primitive-two states bijectively to primitive-two states and sends total mass \(M\) to \(S_{a,b}-M\). This proves reciprocity and the maximal mass. More strongly, choose the minimizing \((k,0)\) pattern. Its own generating polynomial is
\[
z^{\mu(k,0)}[a+b-k]_z^k[k]_z^{a-k+b}.
\]
Both bracket lengths are positive, and its supported powers are every integer from \(\mu(k,0)\) to \(\mu(k,0)+W\), where
\[
W=k(a+b-k-1)+(a-k+b)(k-1)=S_{a,b}-2\mu(k,0).
\]
Thus this *single* phase pattern already realizes every mass from \(L_{a,b}\) to \(S_{a,b}-L_{a,b}\). No mass can lie outside that interval, completing the support proof.

**5. Endpoint multiplicities and orbit count.** In each fixed admissible labelled phase pattern, the coefficient at its lowest possible total mass is exactly one. When \(b\ge a\), the only minimizing patterns are the two all-opposed clique/independent phase assignments, so each endpoint coefficient is two. When \(2\le b<a\) and \(a+b\) is even, the minimizers are \((k,0)\) and its temporal-phase complement, with \(k=(a+b)/2\), giving \(2\binom ak\). When \(a+b\) is odd there are two adjacent minimizing integers \(\lfloor(a+b)/2\rfloor\) and \(\lceil(a+b)/2\rceil\), together with their temporal-phase complements, producing the stated sum. Exactly two configurations inhabit each primitive temporal orbit, and their conserved total mass is identical; this proves evenness and the orbit polynomial.

## Verification

The standalone program `verify_direct.py` enumerates all \(3,178,320\) configurations in the bounded local boxes \(0\le x_v<2d_v\) across ten labelled graphs and computes two literal updates, comparing the resulting mass histogram with an independently implemented phase-interval enumeration. It found equality for every coefficient. This box is exhaustive for initially primitive-two states by Step 4; it is not a search over unbounded chip totals. The second program, `verify_formula.py`, constructs the exact finite-sum polynomial for all \(132\) parameter pairs with \(2\le a\le12\), \(1\le b\le12\), checking all support intervals, endpoint counts, reciprocal coefficients, evenness and total specializations. The tests include \(b=1\) only as a boundary cross-check, not as claimed new scope. Both programs use integer arithmetic and require only Python's standard library. Run `python3 verify_direct.py` and `python3 verify_formula.py` from the directory containing them; the accompanying JSON output files record the actual successful results. These finite checks support, but do not replace, Steps 1–5.

## Relationship to prior work

Bitar and Goles (1992) initiated parallel chip-firing on general graphs. Jiang (arXiv:1003.0943, §§2–4) proves the common-firing-count criterion and studies possible periods on complete multipartite graphs, not the present complete-split mass enumerator. Jiang, Scully and Zhang (arXiv:1211.6786, §§2, 6–7) classify possible firing patterns, not their labelled chip-mass populations on split graphs. Levine (arXiv:0811.2800, §§1–4) studies activity and rotation numbers for complete graphs, using a self-loop convention equivalent to the usual loopless threshold after adjustment; it does not supply this split-graph polynomial. Dukes (arXiv:2006.08006) and Derycke–Dukes–Le Borgne (arXiv:2402.15372) investigate the same complete-split graph *under a different sink-based Abelian sandpile process*: their recurrent-state and height polynomials are not the initially primitive-two periodic-point distribution of the conservative synchronous map. The general middle-stair period-two result (arXiv:2608.04153) concerns eventual period by chip-total band, not initial periodic-point populations or the sharp support here. The novelty asserted is the explicit complete-split polynomial and the sharp no-gap, parity-sensitive extremal phase transition, not the general two-step firing criterion or chip complementation.

## Limitations

The theorem does not classify periods other than two or their basins. It does not count configurations with arbitrary chip mass but only those initially in least-period-two cycles. The 1992 Bitar–Goles full text was not accessible for direct comparison, leaving a bounded historical-priority risk; its publisher abstract was accessible. An exhaustive independent literature census is not claimed. The computational checks cover finite ranges only; infinite quantifiers follow from the displayed proof. No independent audit has been performed.

## References

1. J. Bitar and E. Goles, “Parallel chip firing games on graphs,” *Theoretical Computer Science* 92 (1992), 291–300, DOI: 10.1016/0304-3975(92)90316-8.
2. T.-Y. Jiang, “On the Period Lengths of the Parallel Chip-Firing Game,” arXiv:1003.0943, first submitted 2010-03-04, https://arxiv.org/abs/1003.0943.
3. T.-Y. Jiang, Z. Scully, Y. X. Zhang, “Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game,” arXiv:1211.6786, first submitted 2012-11-29, https://arxiv.org/abs/1211.6786.
4. L. Levine, “Parallel Chip-Firing on the Complete Graph: Devil's Staircase and Poincaré Rotation Number,” arXiv:0811.2800, first submitted 2008-11-17, https://arxiv.org/abs/0811.2800.
5. M. Dukes, “The sandpile model on the complete split graph, Motzkin words, and tiered parking functions,” arXiv:2006.08006, first submitted 2020-06-14, https://arxiv.org/abs/2006.08006.
6. H. Derycke, M. Dukes, Y. Le Borgne, “The sandpile model on the complete split graph: \(q,t\)-Schröder polynomials, sawtooth polyominoes, and a cycle lemma,” arXiv:2402.15372, first submitted 2024-02-23, https://arxiv.org/abs/2402.15372.
7. D. Wang and N. Lannan, “All parallel chip-firing games with \(2|E|-|V|<|\sigma|<2|E|\) have period \(2\),” arXiv:2608.04153, submitted 2026-08-04, https://arxiv.org/abs/2608.04153.
