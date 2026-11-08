# A universal deadline reversal for two sentinels on epidemic paths

## Finding

Consider continuous-time susceptible-infectious (SI) transmission on the undirected path \(P_n\) with vertices \(0,1,\ldots,n-1\). A single initially infected vertex is uniformly chosen from all \(n\) vertices. Each infected--susceptible edge transmits at rate \(\beta>0\), independently, and infected vertices never recover. Two distinct vertices are watched continuously and perfectly; detection occurs at the instant either watched vertex is first infected, including time zero if the seed is watched. For each watched pair \(S\), let \(T_S\) be this first-detection time and let \(Q_{n,S}(t)=\Pr(T_S>t)\) be the failure-to-detect probability by deadline \(t>0\). We minimize \(Q_{n,S}(t)\) over all two-element subsets \(S\).

**Universal deadline reversal.** For every integer \(n\ge4\), the endpoint pair \(E=\{0,n-1\}\) is **not optimal** for all sufficiently short positive deadlines, but is the **unique optimal** pair for all sufficiently long finite deadlines. Consequently no two-sentinel placement is optimal at every positive deadline on any such path. At \(n=2\), the endpoint pair is the only choice; at \(n=3\), it uniquely minimizes failure at every positive deadline. Thus four vertices is the sharp minimum size for deadline dependence in this model.

**Exact smallest case.** Put \(x=\beta t\), and let \(\xi>0\) be the unique positive solution of \(e^\xi=1+2\xi\), numerically \(\xi=1.2564312086261697\ldots\). On \(P_4\), the only optimal pairs are \(\{0,2\}\) and its reflected pair \(\{1,3\}\) for \(0<x<\xi\); all three pairs \(\{0,2\}\), \(\{1,3\}\), and \(\{0,3\}\) tie at \(x=\xi\); and \(\{0,3\}\) is uniquely optimal for \(x>\xi\). Nevertheless both competing placement classes have the *same* mean first-detection time \(3/(8\beta)\). The equal mean thus does not determine which placement is best at a specified detection deadline.

## Assumptions and scope

Transmission clocks are independent unit-memory exponential clocks with common rate \(\beta\) across every SI edge. All seeds are equiprobable, and the watched vertices neither prevent nor delay transmission. There are no recoveries, background importations, false observations, or delay after sentinel infection. The optimization criterion is finite-deadline detection probability, not mean detection time, epidemic size, or probability of eventual infection. The path has undirected nearest-neighbor contacts, and exactly two **distinct** watched vertices. For \(n\ge4\), the theorem guarantees an early/late change; it does not classify all intermediate optimal pairs for every larger path.

## Proof

Write \(x=\beta t\) and, for integers \(d\ge1\), define
\[
H_d(x)=\sum_{j=0}^{d-1}\frac{x^j}{j!},\qquad U_d(x)=e^{-x}H_d(x),\qquad U_0(x)=0.
\]
The time needed to transmit across a prescribed path of \(d\) edges has the \(\operatorname{Gamma}(d,\beta)\) distribution, so its probability of exceeding \(t\) is \(U_d(x)\). Distinct leftward and rightward infection paths from a seed use disjoint independent transmission clocks. Thus for a monitored pair \(S=\{a,b\}\), \(0\le a<b\le n-1\), conditioning on the uniform seed yields the **exact** identity
\[
Q_{n,S}(t)=\frac1n\left[\sum_{i=0}^{a-1}U_{a-i}(x)
+\sum_{i=a+1}^{b-1}U_{i-a}(x)U_{b-i}(x)
+\sum_{i=b+1}^{n-1}U_{i-b}(x)\right]. \tag{1}
\]
An empty sum is zero. A seed at a monitored vertex contributes zero. Equation (1) is exact for every \(n\ge2\), \(\beta,t>0\).

**Early deadlines.** Let \(c(S)\) count path edges with exactly one endpoint in \(S\). As \(t\downarrow0\), the seed lies in \(S\) with probability \(2/n\); otherwise first-order detection requires one transition across such a cut edge. Consequently, from (1),
\[
Q_{n,S}(t)=\frac{n-2}{n}-\frac{c(S)}{n}\beta t+O_n((\beta t)^2). \tag{2}
\]
For the endpoint pair \(E\), \(c(E)=2\) when \(n\ge3\). For \(n=4\), the pair \(S=\{0,2\}\) has \(c(S)=3\); for every \(n\ge5\), the interior-separated pair \(S=\{1,n-2\}\) has \(c(S)=4\). Thus the designated alternative has strictly smaller \(Q\) than \(E\) for all sufficiently small positive \(t\).

**Long deadlines.** For endpoint sentinels, every unwatched seed lies strictly between them, so (1) becomes
\[
Q_{n,E}(t)=\frac{e^{-2x}}n\,R_n(x),\qquad
R_n(x)=\sum_{i=1}^{n-2}H_i(x)H_{n-1-i}(x). \tag{3}
\]
Here \(R_n\) is a polynomial of degree at most \(n-3\). If \(S\ne E\), at least one path endpoint is unwatched. Conditional on the seed being that endpoint (probability \(1/n\)), the first watched vertex is at a positive graph distance \(d\), and its failure probability is \(U_d(x)\ge e^{-x}\). Hence
\[
Q_{n,S}(t)\ge \frac{e^{-x}}n. \tag{4}
\]
Since \(e^{-x}R_n(x)\to0\) as \(x\to\infty\), (3) is strictly smaller than (4) for all sufficiently large \(x\), *simultaneously for every other monitored pair*. This proves unique endpoint optimality at long deadlines. The small- and long-deadline statements together establish the general reversal.

**The sharp four-vertex case.** Up to reflection, the four classes \(\{0,1\}\), \(\{0,2\}\), \(\{0,3\}\), and \(\{1,2\}\) have the exact failure probabilities
\[
\begin{array}{c|c}
S&Q_{4,S}(t)\\ \hline
\{0,1\}&e^{-x}(2+x)/4\\
\{0,2\}&(e^{-x}+e^{-2x})/4\\
\{0,3\}&e^{-2x}(1+x)/2\\
\{1,2\}&e^{-x}/2.
\end{array} \tag{5}
\]
For all \(x>0\), the first and fourth classes have strictly larger failures than \(\{0,2\}\), since
\[
Q_{4,\{0,1\}}-Q_{4,\{0,2\}}
=\frac{e^{-2x}}4((1+x)e^x-1)>0,
\quad
Q_{4,\{1,2\}}-Q_{4,\{0,2\}}
=\frac{e^{-2x}}4(e^x-1)>0. \tag{6}
\]
The remaining difference is
\[
Q_{4,\{0,2\}}-Q_{4,\{0,3\}}
=\frac{e^{-2x}}4(e^x-1-2x). \tag{7}
\]
Let \(f(x)=e^x-1-2x\). It satisfies \(f(0)=0\), \(f'(0)=-1\), and \(f''(x)=e^x>0\) for all \(x\ge0\). Because \(f'\) increases strictly from \(-1\) to infinity, \(f\) decreases initially, then increases to infinity, crossing zero **exactly once** at positive \(x=\xi\). This proves the complete optimum classification including the tie at \(\xi\). Finally, integrating the survival functions in (5) gives
\[
\mathbb E T_{\{0,2\}}=\frac1{4\beta}\left(1+\frac12\right)
=\frac3{8\beta},\qquad
\mathbb E T_{\{0,3\}}=\frac1{2\beta}\left(\frac12+\frac14\right)
=\frac3{8\beta}. \tag{8}
\]
For \(n=3\), endpoint sentinels have \(Q=e^{-2x}/3\), while either adjacent pair has \(Q=e^{-x}/3\), proving endpoint uniqueness. The \(n=2\) case is immediate.

## Verification

The standalone \(\texttt{verify.py}\) reconstructs every four-vertex exponential-polynomial identity symbolically and confirms the exact mean-time tie. It independently builds the complete continuous-time SI generator on all infected-subset states and compares its matrix exponential with (1) for all two-sentinel placements on paths of sizes \(2\) through \(8\), at four dimensionless deadlines (336 comparisons). It also tests 950 additional small- and large-deadline inequalities at sizes \(4\) through \(18\), using high precision when necessary. The checker printed all tests passed and located \(\xi\) at the value shown above. These finite numerical tests are corroboration only; the infinite-in-\(n\), all-positive-horizon conclusions follow analytically from (1)--(8).

To reproduce: install Python 3 with SymPy, NumPy, SciPy, and mpmath; execute \(\texttt{python verify.py}\) from the directory containing the extracted files. The script has no external data dependency or network access.

## Relationship to prior work

Christakis and Fowler (2010) developed network-sentinel early detection and reported central versus randomly sampled monitoring. Their empirical analysis does not optimize two fixed sites by deadline on paths. Bai and collaborators (2017) explored SI sentinel strategies on temporal empirical networks, evaluating lead time rather than this finite-horizon path-law classification. Holme (2017) computed exact multi-sentinel SIR **mean discovery-or-extinction times** on small graphs, not the no-recovery first-detection survival function; his mean objective cannot recover the distinction in (7) because the two candidate mean times are equal. Holme (2018) compared several surveillance objectives under SIR with one sentinel, and specifically asked how multiple sentinels should be distributed. Heavey and colleagues (2022) proved approximation and hardness results for minimizing **mean** detection delay of preselected sensor sets under specified cascades or SIR simulations; they neither address this continuous-time SI finite-deadline crossing nor imply it from a mean objective. None of these directly contains (1)--(8) or implies the universal endpoint reversal from the displayed findings. More general reliability/first-passage literature could contain equivalent representations; independent historical-priority assessment remains appropriate.

## Limitations

The result applies only to homogeneous exponential SI transmission and uniform seeding on paths. Recovery, heterogeneous edge rates, delayed/noisy monitoring, different priors, networks with cycles or branching, and multiple outbreak seeds may alter optimality. The four-node exact cutoff is not a field-calibrated epidemic intervention threshold. The theorem does not offer an explicit deadline cutoff for each larger path, nor a complete list of all intermediate optimizers. The novelty assessment is based on the specified inspected literature and searches, not on a proof that no earlier equivalent theorem exists.

## References

1. Christakis, N. A., and Fowler, J. H. (2010), *Social Network Sensors for Early Detection of Contagious Outbreaks*, PLOS ONE 5(9):e12948. First arXiv public submission 2010-04-27: https://arxiv.org/abs/1004.4792 ; DOI https://doi.org/10.1371/journal.pone.0012948.
2. Bai, Y., Yang, B., Lin, L., Herrera, J. L., Du, Z., and Holme, P. (2017), *Optimizing sentinel surveillance in temporal network epidemiology*, Scientific Reports 7:4804, https://doi.org/10.1038/s41598-017-03868-6.
3. Holme, P. (2017), *Three faces of node importance in network epidemiology: Exact results for small graphs*, Physical Review E 96:062305, https://doi.org/10.1103/PhysRevE.96.062305.
4. Holme, P. (2018), *Objective measures for sentinel surveillance in network epidemiology*, Physical Review E 98:022313, https://doi.org/10.1103/PhysRevE.98.022313.
5. Heavey, J., Cui, J., Chen, C., Prakash, B. A., and Vullikanti, A. (2022), *Provable Sensor Sets for Epidemic Detection over Networks with Minimum Delay*, Proceedings of AAAI 36(9), 10202–10209, https://doi.org/10.1609/aaai.v36i9.21260.
