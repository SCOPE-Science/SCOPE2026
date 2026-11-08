# Exact Nash welfare and optimizer multiplicity on odd enemy cycles

## Finding
Let \(n=2k+1\ge3\) and consider the symmetric aversion-to-enemies hedonic game on labeled agents \(V(C_n)=\{0,\dots,n-1\}\). Two agents are enemies exactly when adjacent in the simple odd cycle \(C_n\); each enemy has symmetric value \(-n\), and each other agent has value \(+1\). Among individually rational coalition partitions, write \(P_n\) for the maximum product of all agents' utilities and \(W_n=P_n^{1/n}\) for geometric-mean Nash welfare.

Then the complete odd-cycle formula is
\[
P_{2k+1}=\begin{cases}
0,&k=1,2,\\
(k-1)^k(k-2)^{k-1},&k\ge3.
\end{cases}
\]

For each \(k\ge3\), the maximizing partitions are **exactly** the partitions into independent coalitions of sizes \((k,k-1,2)\). The number of maximizing partitions, with agents labeled and coalitions unordered, is
\[
N_{2k+1}=\begin{cases}
14,&k=3,\\
2(2k+1)(k-1),&k\ge4.
\end{cases}
\]
Thus, although the odd cycle is three-colorable, the five-agent odd cycle has zero optimal Nash welfare; the seven-agent cycle is the smallest odd case with positive optimum. For instance, \(P_9=648\) and \(N_9=54\).

## Assumptions and scope
- The enemy graph is precisely the **simple, undirected, labeled odd cycle** \(C_{2k+1}\) for an integer \(k\ge1\). All other unordered pairs of distinct agents are mutually friendly.
- Each agent evaluates a coalition by summing values of the other members; enemies contribute \(-n\) and friends contribute \(+1\).
- A partition is individually rational if all agents have nonnegative utility. Nash welfare is the geometric mean of utilities on individually rational partitions; equivalently, maximize their product.
- The optimizer counts concern partitions of labeled agents into **unlabeled** coalitions. The theorem does not enumerate zero-product maximizers for \(C_3\) and \(C_5\).

## Proof
**Step 1: Graph and utility reduction.** If a coalition of size \(s\le n\) contains an enemy of agent \(i\), then \(i\)'s utility is at most \((s-2)-n<0\). Consequently, every individually rational coalition is an independent vertex set of the enemy graph. Conversely, an independent coalition of size \(s\) gives each member utility \(s-1\ge0\). If any coalition is a singleton, the Nash product is zero. Otherwise, for a proper partition into independent parts of sizes \(s_1,\dots,s_t\ge2\), the Nash product is
\[
\prod_{j=1}^{t}(s_j-1)^{s_j},\qquad\sum_j s_j=2k+1.
\]

**Step 2: A sharp size majorization bound for odd cycles.** An independent set of \(C_{2k+1}\) has size at most \(k\). Moreover, an odd cycle requires at least three independent sets to cover its vertices. Suppose the product is positive, so all its \(t\ge3\) coalition sizes are at least two. In particular \(k\ge3\). Arrange the sizes in nonincreasing order and pad with zeroes. Then \((k,k-1,2,0,\ldots)\) majorizes that vector: the largest size is at most \(k\); the first two sizes total at most \(n-2=2k-1\); and the first three entries of the displayed vector already sum to \(n\).

Define the convex function \(f:[0,\infty)\to[0,\infty)\) by \(f(x)=0\) for \(0\le x\le2\), and \(f(x)=x\log(x-1)\) for \(x\ge2\). It is continuous at \(2\); its right derivative there is \(2\), while the left derivative is \(0\), and \(f''(x)=(x-2)/(x-1)^2\ge0\) for \(x>2\). The log product is \(\sum_j f(s_j)\). Karamata's inequality therefore yields
\[
\log P\le k\log(k-1)+(k-1)\log(k-2).
\]
Equality for positive-product partitions requires the multiset \((k,k-1,2)\). When \(k=3\), it is the only possible positive size multiset by the sum and independence constraints. For \(k\ge4\), if the largest size is below \(k\), any majorization decomposition from the candidate vector must average a component at \(k>2\) with a smaller component. If the largest equals \(k\) but the second-largest is below \(k-1\), it must instead average the component at \(k-1>2\). Convexity is strict under either operation because \(f\) is strictly convex above \(2\). Finally, if the two largest sizes are \(k,k-1\), the remaining size total is \(2\) and therefore is a single two-agent coalition. Hence every other positive size multiset has strictly smaller product.

**Step 3: Attainment and exact optimizer counts.** In \(C_{2k+1}\), choose a maximum independent set \(A\) of size \(k\). Its complement induces exactly one edge and \(k-1\) isolated vertices. Select one endpoint of that edge together with one of those \(k-1\) isolates to form a two-person independent coalition \(C\). The remaining \(k-1\) vertices form an independent coalition \(B\). For \(k\ge3\), this gives the positive and optimal size multiset \((k,k-1,2)\).

There are exactly \(2k+1\) maximum independent sets: when their vertices are arranged cyclically, the \(k+1\) unchosen vertices occupy \(k\) nonempty gaps, so exactly one gap has two unchosen vertices, with the choice of gap location uniquely determining the independent set. For each \(A\), there are \(2(k-1)\) possible choices for \(C\). When \(k\ge4\), the sizes of \(A,B,C\) differ, so every maximizing partition is counted once. When \(k=3\), the two size-two coalitions can be exchanged, and every partition is counted twice. This proves the displayed formula for \(N_{2k+1}\).

**Step 4: Small odd cycles.** The cycles \(C_3\) and \(C_5\) are nonbipartite, so every independent-set partition has at least three coalitions. Three coalitions each containing at least two agents would require at least six agents. Accordingly, every individually rational partition for these cases contains a singleton and has Nash product zero. The all-singleton partition attains this maximum.

## Verification
Two standalone finite enumerators independently construct all partitions into enemy-independent coalitions of labeled cycles and compute the exact integer Nash product. The C++ verifier checks the formulas and optimizer counts on odd orders \(3,5,7,9,11,13\) and also uses even orders through \(12\) as controls; the independent Python verifier checks through order \(11\). The C++ enumeration counts \(3,633,280\) legal partitions on \(C_{13}\), obtaining product \(16,000,000\) and exactly \(130\) maximizing partitions. Both programs agree for all shared sizes. Run `g++ -std=c++17 -O2 verify_cycle_nash.cpp -o verify && ./verify` or `python3 verify_cycle_nash.py`. These finite checks test the formulas but do not replace the all-size proof above.

## Relationship to prior work
Pagano and Schlenga (2026) introduce Nash welfare for additively separable hedonic games, show hardness and approximation bounds for aversion-to-enemies games, and establish that positive Nash welfare is equivalent to the existence of a suitable \(\{K_2,K_3\}\)-factor in the mutual-friendship graph. Their two-coalition result addresses bipartite enemy graphs, which includes **even cycles**; those cases are not claimed as new here. Odd cycles require at least three coalitions, and their general positivity criterion does not give this odd-cycle optimum, optimizer-size rigidity, or exact multiplicity. Their relevant appendix proofs were also inspected. Elkind, Flammini and Varricchio (2025) investigate *egalitarian* rather than Nash welfare for friends-and-enemies games; a bound on the minimum agent utility does not determine the product of all utilities. Fractional hedonic games use average rather than sum coalition utilities and are likewise a distinct model.

## Limitations
The theorem concerns only a single **odd enemy cycle**, not a friendship cycle, general graphs, unions of cycles, asymmetric or heterogeneous preferences, or other welfare objectives. For \(C_3,C_5\), the optimum is zero and the theorem does not classify all maximizing zero-product partitions. No complexity classification is asserted for broader graph classes, and finite enumeration does not substitute for the mathematical proof. Possible unindexed equivalent prior results remain a publication-priority risk.

## References
1. Marta Pagano and Alexander Schlenga, *Nash Welfare in Additively Separable Hedonic Games* (first public version 18 May 2026), arXiv:2605.19030, https://arxiv.org/abs/2605.19030 . Relevant: Sections 2, 3, 6, 8 and Appendix proofs of Lemmas 1–2, Theorem 6.1 and related results.
2. Edith Elkind, Michele Flammini and Giovanna Varricchio, *Maximizing the Egalitarian Welfare in Friends and Enemies Games* (23 December 2025), arXiv:2512.20261, https://arxiv.org/abs/2512.20261 . Relevant: Sections 2–3.
3. Haris Aziz, Serge Gaspers, Joachim Gudmundsson, Julián Mestre and Hanjo Täubig, *Welfare Maximization in Fractional Hedonic Games*, IJCAI 2015, https://ijcai.org/proceedings/2015/71 . Compared for model distinction only.
