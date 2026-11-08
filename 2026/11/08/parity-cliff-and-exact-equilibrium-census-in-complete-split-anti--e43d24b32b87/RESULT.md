# Parity cliff and exact equilibrium census in complete-split anti-coordination games

## Finding
For all integers \(c,m\ge 1\), consider the unweighted binary anti-coordination game on the complete split graph \(G_{c,m}=K_c\vee\overline K_m\). There are \(c\) mutually adjacent core agents and \(m\) mutually nonadjacent peripheral agents, every peripheral agent adjacent to every core agent. Each player receives one payoff unit per disagreeing neighbor, and is permitted to retain an action when indifferent. Social welfare is twice the crossing-edge count.

Let \(k\) core agents and \(\ell\) peripheral agents choose action 1. Define the finite integer index set
\[
\mathcal K_{c,m}=\left\{0\le k<\frac c2:\; (k=0\ \mathrm{and}\ m\ge c-1)\ \mathrm{or}\ (k>0\ \mathrm{and}\ c-1\le 2k+m\le c+1)\right\}.
\]
The **complete equilibrium classification** consists of: (i) for each \(k\in\mathcal K_{c,m}\), all profiles with occupancies \((k,m)\) or \((c-k,0)\); and (ii) only when \(c\) is even, profiles with \(k=c/2\) and \(|2\ell-m|\le1\). The exact number of labeled equilibria is
\[
E_{c,m}=2\sum_{k\in\mathcal K_{c,m}}\binom ck + \mathbf1_{2\mid c}\binom{c}{c/2}\sum_{\substack{0\le\ell\le m\\ |2\ell-m|\le1}}\binom m\ell.
\]
The maximum cut, and the minimum cut among equilibria, respectively, are
\[
M_{c,m}=cm+\left\lfloor\frac{\max(c-m,0)^2}{4}\right\rfloor,\qquad
B_{c,m}=\begin{cases}M_{c,m},&c\text{ odd},\\ c^2/4+cm/2,&c\text{ even}.\end{cases}
\]
Consequently, the price of anarchy is \(M_{c,m}/B_{c,m}\), while the price of stability is 1. Every equilibrium is welfare-maximizing whenever \(c\) is odd; when \(c\) is even and \(m\ge2\), the only inefficient equilibria are precisely the equal-core-split profiles in (ii). For every fixed positive even \(c\), the price of anarchy approaches 2 as \(m\to\infty\), while for every odd \(c\) it remains 1 for all \(m\). At \(m=c\) with even \(c\), it is exactly \(4/3\).

## Assumptions and scope
The network is finite, simple, undirected, complete-split with every core-to-peripheral edge present. Actions are exactly \(\{0,1\}\); all edge payoffs are symmetric and of unit weight, and ties count as best responses. All results concern pure-strategy Nash equilibria, not mixed equilibria, directed networks, heterogeneous weights, or general split graphs. Core vertices and peripheral vertices are distinguishable as labeled agents; the binomial coefficients count their labeled assignments. The theorem includes \(c=1\), \(m=1\), and all parity boundary cases.

## Proof
**1. Local response inequalities.** For a core agent currently choosing 1, the number of disagreeing neighbors is \((c-k)+(m-\ell)\), while the number of agreeing neighbors is \((k-1)+\ell\). Hence such a player has no profitable switch exactly when \(2(k+\ell)\le c+m+1\), whenever \(k>0\). For a core agent currently choosing 0, the analogous condition is \(2(k+\ell)\ge c+m-1\), whenever \(k<c\). A peripheral agent observes exactly \(k\) action-1 and \(c-k\) action-0 neighbors. Thus every peripheral agent must play 1 if \(2k<c\), must play 0 if \(2k>c\), and is indifferent if \(2k=c\).

**2. Exhaustive equilibrium classification.** If \(k<c/2\), then \(\ell=m\). Substituting this in the two core inequalities yields \(m\ge c-1\) when \(k=0\), and \(c-1\le2k+m\le c+1\) when \(0<k<c/2\). Complementing every action gives the counterpart \((c-k,0)\). When \(c\) is even and \(k=c/2\), the peripheral players are indifferent, but the core inequalities reduce to \(m-1\le2\ell\le m+1\), equivalently \(|2\ell-m|\le1\). These conditions are individually both necessary and sufficient for every player to be best responding. Counting core labels by \(\binom ck\), peripheral labels by \(\binom m\ell\), and the two distinct noncentral orientations gives the stated equilibrium census. No cases have been omitted.

**3. Global maximum.** The cut weight for a profile with occupancies \((k,\ell)\) is exactly
\[
C_{c,m}(k,\ell)=k(c-k)+k(m-\ell)+(c-k)\ell.
\]
For each \(k<c/2\) its maximum over \(\ell\) occurs at \(\ell=m\); for \(k>c/2\) at \(\ell=0\); and for \(k=c/2\) it is independent of \(\ell\). Action-complement symmetry therefore reduces global optimization to integers \(0\le k\le\lfloor c/2\rfloor\) of
\[
F(k)=(c-k)(m+k)=cm+k(c-m-k).
\]
This concave integer quadratic attains \(cm+\lfloor\max(c-m,0)^2/4\rfloor\). Indeed, if \(c\le m\), its maximum is at \(k=0\); otherwise \(k\) is one of the nearest integers to \((c-m)/2\), which lies in the permitted range because \(m\ge1\). Thus \(M_{c,m}\) is exact and is always realized by a Nash equilibrium (every global cut optimum is locally stable).

**4. Local versus global optimum.** For noncentral equilibria, the core inequalities are precisely the discrete-neighbor maximality conditions for \(F\):
\[
F(k)-F(k-1)=c-m-2k+1\quad(k>0),\qquad F(k+1)-F(k)=c-m-2k-1.
\]
At the upper admissible boundary, symmetry leaves no larger global value on the other half. As \(F\) is concave, every noncentral equilibrium realizes \(M_{c,m}\). If \(c\) is odd no central family exists, so \(B_{c,m}=M_{c,m}\). If \(c\) is even, central core occupancy is \(k=c/2\) and the cut formula gives exactly \(c^2/4+cm/2\) for every permitted \(\ell\), independent of the peripheral split. All central profiles exist, and their cut cannot exceed the global maximum; hence they realize the minimum equilibrium cut. They are strictly inefficient if \(m\ge2\): shifting one core player to make the core split unbalanced and keeping all peripheral agents opposite the resulting core minority improves the cut by at least \(m-1>0\) (more precisely \(F(c/2-1)-F(c/2)=m-1\)). For \(m=1\) there is equality. Welfare is twice cut size, so the ratio and asserted parity boundaries follow.

## Verification
Run the embedded Python 3 standard-library program \(`python3 verify.py`\). It directly enumerates every labeled action profile for each \(1\le c,m\le8\) (260100 profiles), constructing edges explicitly and testing each individual best response, comparing against the theorem's profile, count, maximum-cut, and worst-equilibrium formulas. A separate 4900-parameter compressed occupancy check covers \(1\le c,m\le70\) with independent profile summation. The expected terminal line is \(`VERIFY_OK labeled_masks=260100 compressed_pairs=4900`\). These finite tests independently check numerous small and boundary instances but are not the proof for arbitrary sizes; Steps 1–4 above supply the latter.

## Relationship to prior work
Deligkas, Eiben, Gutin, Neary, and Yeo study welfare objectives in binary-action network coordination and anti-coordination, establishing general complexity classifications [1,2]. Lampis studies minimum locally stable cuts and their relationship to the price of anarchy, chiefly under graph width/degree constraints [3]. The present exact labeled equilibrium census and the odd/even clique-size efficiency cliff specialize to complete-split graphs and are not consequences of the general complexity bounds alone. The equivalence between Nash profiles and locally stable cuts is standard, not claimed as new. A previous exact census of balanced complete multipartite networks covers the different equal-part-size family; the unequal-part complete split graph \(K_{m,1,\ldots,1}\) with \(m>1\) is outside that theorem's balanced hypothesis.

## Limitations
The calculation does not extend automatically to noncomplete split graphs, weighted edges, asymmetric player payoffs, mixed strategies, or stochastic learning dynamics. The class is naturally structured, so equivalent special-family formulas may exist under graph-theoretic terminology such as stable cuts or unfriendly partitions; the literature search cannot rule out every unindexed prior result. The computational verifier is exhaustive only over its specified finite ranges and provides no infinite-size certificate. The work has not received independent external validation.

## References
[1] A. Deligkas, E. Eiben, G. Gutin, P. R. Neary, A. Yeo, *Complexity of Efficient Outcomes in Binary-Action Polymatrix Games with Implications for Coordination Problems*, arXiv:2305.07124v1, first public 2023-05-11, https://arxiv.org/abs/2305.07124.

[2] A. Deligkas, E. Eiben, G. Gutin, P. R. Neary, A. Yeo, *Some coordination problems are harder than others*, arXiv:2311.03195v1, 2023-11-06, https://arxiv.org/abs/2311.03195. Closely related expanded work by the same authors.

[3] M. Lampis, *Minimum Stable Cut and Treewidth*, arXiv:2104.13097, first public 2021, https://arxiv.org/abs/2104.13097.
