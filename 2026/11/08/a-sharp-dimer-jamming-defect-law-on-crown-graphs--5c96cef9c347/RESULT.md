# A sharp dimer-jamming defect law on crown graphs

## Finding
Let \(C_n\), for each integer \(n\ge2\), be the bipartite crown graph with labeled vertex classes \(L=\{L_1,\ldots,L_n\}\), \(R=\{R_1,\ldots,R_n\}\), and edges \(L_iR_j\) exactly when \(i\ne j\). Independently put an equal-rate continuous adsorption clock on each edge. Whenever an edge's clock rings and neither endpoint is occupied, deposit a dimer on its endpoints permanently. Equivalently, repeatedly choose a uniformly random currently available edge and delete both incident vertices.

Let \(q_n\) be the probability that the saturated deposit is not a perfect matching. With \(H_r=\sum_{j=1}^{r}1/j\),
\[
\frac{2}{n+1}-\frac{4H_{n-1}}{n(n+1)}\ \le\ q_n\ \le\ \frac{2}{n+1},
\qquad\lim_{n\to\infty}nq_n=2.
\]
Every terminal deposit has exactly \(n\) or \(n-1\) dimers; in the latter case, the two uncovered sites have the same label \(i\), namely \(L_i,R_i\). Thus its expected number of deposited dimers is exactly \(n-q_n\). The following two-parameter rational recurrence computes the complete finite-size probability, including \(q_2=0\), \(q_3=1/3\), \(q_4=4/21\), and \(q_5=4/21\):
\[
F(1,0)=0,\quad F(1,1)=1,\qquad
F(m,c)=\frac{c(c-1)F(m-1,c-2)+2c(m-c)F(m-1,c-1)+(m-c)^2F(m-1,c)}{m^2-c},
\quad q_n=F(n,n).
\]
The recurrence is used for integer \(m\ge2\), \(0\le c\le m\) with \(m^2-c>0\); zero-coefficient summands with inadmissible arguments are omitted. In a reachable state with \(m\ge2\), that denominator is positive.

## Assumptions and scope
The graph has two labeled parts of equal size and only the \(n\) diagonal cross-edges are absent. Each available edge has the same independent continuous exponential clock rate. Rejected attempts at edges with already occupied endpoints have no effect; exponential memorylessness gives the uniform-available-edge description. Dimers are permanent and each occupies its two endpoint vertices. The theorem concerns the terminal matching and its failure probability, not transient coverage curves. Arbitrary nonuniform adsorption rates are not included.

## Proof
After \(n-m\) successful deposits, let \(A\) and \(B\) be the uncovered label sets on the left and right. Both have size \(m\); define \(C_m=|A\cap B|\). The available graph has \(m^2-C_m\) edges, because exactly the common-label diagonal pairs are forbidden. For a uniformly chosen permissible edge, the new common-label count is \(c-2\), \(c-1\), or \(c\) with respective edge counts \(c(c-1)\), \(2c(m-c)\), and \((m-c)^2\) when \(C_m=c\). These counts sum to \(m^2-c\), proving the finite-size recurrence.

The terminal matching has a common number of uncovered vertices in each part. If at least two remain then an available cross-edge exists; hence termination occurs at \(m=0\), or at \(m=1\) with its sole left and right labels equal. In particular the defect has exactly one unmatched vertex per part.

For the asymptotic law define \(Y_m=C_m/[m(m+1)]\). Conditional on \(C_m=c\), direct averaging gives
\[
\mathbb E[C_{m-1}\mid C_m=c]
=c\left(1-\frac{2(m-1)}{m^2-c}\right),
\]
and, for \(m\ge2\),
\[
\mathbb E[Y_m-Y_{m-1}\mid C_m=c]
=\frac{2c(c-1)}{m(m-1)(m+1)(m^2-c)}\ge0.
\]
To control this drift, for \(m\ge3\) calculate the second factorial moment
\[
\mathbb E[C_{m-1}(C_{m-1}-1)\mid C_m=c]
=\frac{c(c-1)((m-2)^2-c+2)}{m^2-c}.
\]
When \(c\ge2\), elementary algebra shows
\[
\frac{(m-1)(m-2)}{m(m+1)}-
\frac{(m-2)^2-c+2}{m^2-c}
=\frac{2((2m-1)c-3m)}{m(m+1)(m^2-c)}\ge0,
\]
since \(m\ge3\). The inequality is automatic when \(c<2\) because the factorial moment vanishes. Dividing by \((m-1)^2((m-1)^2-1)\) and iterating from \(C_n=n\) proves, for every integer \(2\le m\le n\),
\[
\mathbb E[C_m(C_m-1)]\le\frac{m^2(m^2-1)}{n(n+1)}.
\]
Because \(m^2-c\ge m(m-1)\), the expected drift satisfies
\[
0\le\mathbb E[Y_m-Y_{m-1}]
\le\frac{2\mathbb E[C_m(C_m-1)]}{m^2(m-1)^2(m+1)}
\le\frac{2}{n(n+1)(m-1)}.
\]
Summing from \(m=n\) down to \(m=1\), using \(Y_n=1/(n+1)\) and \(\mathbb E[Y_1]=q_n/2\), proves
\[
0\le \frac1{n+1}-\frac{q_n}{2}\le\frac{2H_{n-1}}{n(n+1)}.
\]
This is precisely the claimed bound. Since \(H_{n-1}=O(\log n)\), multiplying by \(n\) yields the stated limit \(nq_n\to2\).

## Verification
The standalone files `checks/verify_exact.py` and `checks/verify_masks.py` independently verify the finite-size probabilities using (respectively) the two-parameter rational recurrence and an explicit labeled-subset recursion. The first tests the conditional-moment equalities and their inequality over all integer states with \(3\le m<90\); the second exactly enumerates the full labeled Markov chain through \(n=8\). Both check their respective reference values, and the first checks the rigorous harmonic bounds for \(2\le n\le10\). These finite tests corroborate but do not replace the displayed all-size proof. Run with `python checks/verify_exact.py` and `python checks/verify_masks.py` using the standard Python library alone.

## Relationship to prior work
The mechanism is the random greedy matching/dimer random-sequential-adsorption process studied generally by Pippenger (1989), Dyer and Frieze (1991), Miller and Pritikin (1997), and Gamarnik and Goldberg (2008). The last authors' published theorem evaluates fixed-degree, large-girth regimes; for \(n\ge4\), the crown graph has degree \(n-1\) and girth four; the generic theorem then formally applies, but its large girth-correction term gives no sharp \(2/n\) law. The available statements do not imply the exact crown-graph defect recurrence or the sharp constant \(2\). The classical number of perfect matchings on a crown graph counts derangements, whereas this calculation measures the terminal distribution produced by irreversible random edge choices, which is not the uniform distribution on matchings. Some earlier primary full texts could not be accessed; priority remains subject to that material risk.

## Limitations
The theorem is proved only for equal-rate noninteracting permanent dimers on these finite graphs. It does not cover unequal edge rates, correlated clocks, desorption, higher-order occupancies, or transient jamming times. The asymptotic error bound is \(O(\log n/n^2)\); no optimal second-order term is asserted. Literature-based originality is provisional pending broader historical comparison; this is not an independently certified scientific result.

## References
1. N. Pippenger, “Random Sequential Adsorption on Graphs,” *SIAM Journal on Discrete Mathematics* **2** (1989), 393–401. DOI: 10.1137/0402034.
2. M. Dyer and A. Frieze, “Randomized greedy matching,” *Random Structures & Algorithms* **2** (1991), 29–45. DOI: 10.1002/rsa.3240020104.
3. Z. Miller and D. Pritikin, “On randomized greedy matchings,” *Random Structures & Algorithms* **10** (1997), 353–383. DOI: 10.1002/(SICI)1098-2418(199705)10:3<353::AID-RSA5>3.0.CO;2-V.
4. D. Gamarnik and D. A. Goldberg, “Randomized greedy algorithms for independent sets and matchings in regular graphs: Exact results and finite girth corrections,” arXiv:0807.1277, first posted 2008-07-08. https://arxiv.org/abs/0807.1277.
5. Z. G. Tang, X. Wu and Y. Zhang, “Towards a Better Understanding of Randomized Greedy Matching,” arXiv:1907.05135 (2019); different random-decision-order model.
