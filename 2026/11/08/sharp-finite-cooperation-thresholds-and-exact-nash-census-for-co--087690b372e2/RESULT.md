# Sharp finite cooperation thresholds and exact Nash census for complete pair-and-triple social dilemmas

## Finding
Consider the weighted sum of symmetric games played on every unordered pair and every unordered triple of \(n\ge3\) labeled players. Each player chooses cooperation \(C\) or defection \(D\). Every pure Nash equilibrium has either no cooperators, or \(k\) cooperators with
\[
 d_L(k-1)\ge0\ge d_L(k),\qquad L=n-1,\qquad
 d_L(j)=-\frac L2+\lambda\left(3j(L-j)-\frac{L(L-1)}4\right).
\]
For \(1\le k\le n-1\), these inequalities are necessary and sufficient, and exactly \(\binom nk\) distinct labeled profiles have that number of cooperators. Consequently
\[
 E_{n,\lambda}=1+\sum_{k=1}^{n-1}\binom nk\,\mathbf 1\!\left\{d_L(k-1)\ge0\ge d_L(k)\right\}.
\]
The first nonzero-cooperation equilibrium appears at the sharp intensity
\[
 \lambda_c(n)=\frac{L}{2\left(3\lfloor L^2/4\rfloor-L(L-1)/4\right)}.
\]
At this threshold the exact labeled equilibrium count is
\[
 E_{n,\lambda_c}=\begin{cases}
 1+\binom n{(n+1)/2}, & n\text{ odd},\\
 1+\binom n{n/2}+\binom n{n/2+1},&n\text{ even}.
 \end{cases}
\]
Furthermore, an equilibrium with exactly one defector is possible at some nonnegative intensity if and only if \(3\le n\le12\); in that range it is possible exactly for
\[
 \lambda\ge\frac{2(n-1)}{(n-2)(13-n)}.
\]
At every intensity there are at most two cooperative equilibrium *population sizes* (which, when there are two, are consecutive); no such bound is claimed on the number of labeled equilibria.

## Assumptions and scope
For every pair, focal payoffs \(R=1\) against \(C\) and \(S=-1/2\) against \(D\) when cooperating; \(T=3/2\) against \(C\) and \(P=0\) against \(D\) when defecting. For each triple, focal cooperating payoffs against two, one, zero cooperating coplayers are respectively \(1,5/2,-1/2\); corresponding defecting payoffs are \(3/2,0,0\). Each pair has weight \(1\), each triple weight \(\lambda\ge0\). Total player payoff is the sum of incident pair-game payoffs and weighted triple-game payoffs. All \(n\) labels are distinct. A pure Nash equilibrium prohibits a strictly profitable unilateral switch; indifference permits both strategies. Intensities are real and nonnegative. This is a static weighted complete pair-and-triple interaction game, **not** a claim about the stochastic update process or phase diagram of the motivating paper.

## Proof
Fix a player and write \(j\) for the number of cooperating players among the other \(L=n-1\) players. For either opponent action, the pairwise advantage of cooperation relative to defection is \(-1/2\), hence the aggregate pairwise advantage is \(-L/2\). In triples the advantage is \(-1/2\) with both coplayers cooperating, \(5/2\) when exactly one cooperates, and \(-1/2\) with both defecting. There are \(\binom j2\), \(j(L-j)\), and \(\binom{L-j}2\) such pairs of other players. Since these three counts sum to \(\binom L2\), the triple advantage equals
\[
 -\frac12\binom L2+3j(L-j)=3j(L-j)-\frac{L(L-1)}4.
\]
Adding the two types proves the displayed formula for \(d_L(j)\). If there are \(k\) cooperating players, every cooperating player's \(L\) opponents contain \(k-1\) cooperators. Such a player has no profitable deviation precisely when \(d_L(k-1)\ge0\). Every defector sees \(k\) cooperators and has no profitable deviation precisely when \(d_L(k)\le0\). The all-defector profile is stable since \(d_L(0)<0\) for every \(\lambda\ge0\). The all-cooperator profile cannot be stable since \(d_L(L)<0\). This yields the exact census, including all equalities.

The quadratic \(j(L-j)\) is nondecreasing to the center of \([0,L]\) and nonincreasing after it. The maximum of \(d_L\) is \(-L/2+\lambda M_L\), where \(M_L=3\lfloor L^2/4\rfloor-L(L-1)/4>0\) for \(L\ge2\). If the maximum is negative, no cooperator can be stable. If it is nonnegative, take its rightmost nonnegative index \(j\); its immediate successor, if any, is nonpositive and yields an equilibrium with \(k=j+1\). Because \(d_L(L)<0\), this successor always exists. This proves the sharp threshold. At threshold, when \(L\) is even there is exactly one central zero, yielding \(k=(n+1)/2\); when \(L\) is odd there are two adjacent central zeros, yielding \(k=n/2\) and \(k=n/2+1\). All other indices are negative. The same unimodality shows that any cooperative equilibrium is at the descending zero crossing; only a zero tie permits two consecutive equilibrium sizes.

For the one-defector case \(k=n-1=L\), every cooperator sees \(L-1\) cooperating opponents and the unique defector sees \(L\). Direct substitution gives
\[
 d_L(L-1)=-\frac L2+\frac{\lambda(L-1)(12-L)}4,
 \qquad d_L(L)=-\frac L2-\frac{\lambda L(L-1)}4<0.
\]
The first inequality can hold only for \(L\le11\), equivalent to \(n\le12\), and in that range it is equivalent to the stated lower bound. This proves the claimed sharp cutoff.

## Verification
The supplied `verify.py` directly sums exact rational payoffs over all pairs and all triples for each player and both potential actions. It compares these direct payoffs with the quadratic formula and every enumerated Nash profile for all \(3\le n\le8\) across up to 14 threshold and off-threshold intensities, then checks the threshold and one-defector claims over \(3\le n\le39\). It reports `VERIFY_OK` after 49,976 exact action-advantage comparisons. The proof above is valid for arbitrary \(n\) and is not inferred from the finite computation. Run: `python verify.py` using Python 3 standard library only.

Examples: at \(n=5\), \(\lambda_c=2/9\) and the threshold equilibrium count is \(11\); at \(n=6\), \(\lambda_c=5/26\) and the count is \(36\). For \(n\ge13\), no weighted triple intensity permits exactly one defector in equilibrium.

## Relationship to prior work
Civilini, Sadekar, Battiston, Gómez-Gardeñes and Latora (first preprint March 20, 2023) introduced higher-order cooperative social-dilemma games and analytically characterized a *well-mixed mean-field evolutionary* bistable transition, supplemented by stochastic hypergraph simulations. Their payoff notation includes \(T,S,G,W\) and their analysis establishes a macroscopic cooperation threshold; it motivates the model here. Our specified *finite static fully connected weighted* interaction game differs from the random-hypergraph update rule. The finite labeled Nash census, parity-dependent threshold multiplicity and sharp one-defector cutoff are not supplied by the paper's continuum replicator equation. No claim is made that the asymptotic cooperation fraction or general coexistence mechanism was previously unknown. Searches of accessible related records and literature found no identical finite claim, but unindexed equivalent formulas remain a priority risk.

## Limitations
The counting theorem is confined to the declared payoff table, complete pair-and-triple interaction structure, and unilateral pure strategies; it does not establish stochastic long-time behavior, other social-dilemma payoffs, arbitrary hypergraphs, mixed-strategy equilibria, or selection among the many equilibria. A census by population size is not a prediction of which equilibria dynamics will reach. The exact ratio of triple-to-pair weights is a modeling parameter and need not equal the fraction of triples in a random hypergraph. Searches cannot prove worldwide priority; independent external validation is not yet available.

## References
1. A. Civilini, O. Sadekar, F. Battiston, J. Gómez-Gardeñes, and V. Latora, *Explosive Cooperation in Social Dilemmas on Higher-Order Networks*, arXiv:2303.11475 (first submitted March 20, 2023), https://arxiv.org/abs/2303.11475.
2. A. Civilini et al., *Physical Review Letters* **132**, 167401 (2024), https://doi.org/10.1103/PhysRevLett.132.167401, including Supplementary Material.
