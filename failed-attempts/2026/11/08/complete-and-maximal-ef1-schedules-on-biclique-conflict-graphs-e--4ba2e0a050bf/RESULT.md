# Complete and maximal EF1 schedules on biclique conflict graphs: exact census and a sharp half-completion gap

## Finding

Fix integers \(a,b\ge 1\) and \(n\ge 2\). Let \(K_{a,b}\) be the *conflict graph on chores*: there are \(a\) individually labeled chores of type A and \(b\) of type B; chores of different types conflict, whereas chores of the same type do not. There are \(n\) labeled agents; every chore costs one to every agent. A feasible partial allocation gives each agent an independent set of chores, with any remaining chores unallocated. It is *maximal* if no unallocated chore can be added to any agent's bundle without violating feasibility. It is *EF1* if, for any two agents, deleting at most one chore from the envying agent's bundle removes cost-envy. Write \(M=a+b\), \(q=\lfloor M/n\rfloor\), and \(r=M-nq\).

**Classification.** Every maximal EF1 allocation falls into exactly one of the following disjoint types:

1. A complete equitable proper \(n\)-coloring of \(K_{a,b}\), allocating every chore and giving each agent either \(q\) or \(q+1\) chores.
2. An incomplete allocation giving every B chore to the agents and leaving every A chore unallocated; each agent receives at least one B chore, and bundle sizes differ by at most one. This type exists exactly when \(b\ge n\).
3. The symmetric incomplete allocation giving every A chore and leaving every B chore; it exists exactly when \(a\ge n\).

**Exact enumeration.** Let \(C(a,b;n)\) be the number of complete EF1 allocations. If \(M<n\), then \(C(a,b;n)=n!/(n-M)!\). If \(M\ge n\), put \(u_s=a-sq\), \(v_s=b-(n-s)q\). Then

\[
C(a,b;n)=\frac{a!b!}{(q!)^{n-r}((q+1)!)^r}
\sum_{\substack{1\le s\le n-1\\0\le u_s\le s\\0\le v_s\le n-s}}
\binom ns\binom s{u_s}\binom{n-s}{v_s}.
\]

For \(z\ge1\), define

\[
E_n(z)=\begin{cases}
0,&z<n,\\[2pt]
\displaystyle\binom n h\frac{z!}{(t!)^{n-h}((t+1)!)^h},&z\ge n,\quad z=nt+h,\quad0\le h<n.
\end{cases}
\]

The number of **all** maximal EF1 allocations is exactly \(C(a,b;n)+E_n(a)+E_n(b)\); the incomplete count is \(E_n(a)+E_n(b)\).

**Sharp throughput gap.** A maximal EF1 allocation exists for every \(a,b\ge1\), \(n\ge2\). The maximum number \(T(a,b;n)\) of allocated chores among them is

\[
T(a,b;n)=\begin{cases}M,&C(a,b;n)>0,\\\max\{a,b\},&C(a,b;n)=0.\end{cases}
\]

Thus \(T(a,b;n)/M\ge1/2\). This uniform bound is asymptotically sharp even with four agents and balanced conflict classes: for all integers \(h\ge3\), on \(K_{2h-1,2h+1}\) with \(n=4\), no complete EF1 allocation exists and \(T=2h+1\), giving \(T/M=(2h+1)/(4h)\to1/2\). For example, \(K_{5,7}\) with four agents admits exactly \(2760\) maximal EF1 allocations, every one incomplete, and the largest allocate seven of the twelve chores.

## Assumptions and scope

All chores and agents are distinguishable; all costs are the same unit cost. Conflicts constrain chores assigned to the *same* agent, not social connections between agents. An empty bundle is allowed, but an incomplete maximal allocation on the biclique cannot contain one. Envy is cost-envy for chores (a player prefers a bundle with fewer chores). EF1 means removing one chore from the *envying agent's* own bundle, if needed; with unit costs this is equivalent to \(\max_i |X_i|-\min_i |X_i|\le1\). Maximality is inclusion maximality of a partial allocation, not global Pareto optimality or maximum cardinality. Only graph edges across the two entire nonempty sides are present.

## Proof

**1. Maximality trichotomy.** Suppose some A chore is unallocated. Every agent must then hold at least one B chore: otherwise that agent's bundle is either empty or entirely A, so the unallocated A chore could be added without conflict. Consequently no agent can hold any A chore, because every agent holds B. Therefore every A chore is unallocated. Also every B chore must be allocated: adding an unallocated B chore to any of the existing B-only bundles is feasible. This proves type 2 even *without* fairness. Interchanging A and B gives type 3. If neither side contains an unallocated chore, the allocation is complete, type 1. Both incomplete types are mutually exclusive because each side is nonempty.

**2. EF1 and arithmetic.** For unit costs, a bundle of size \(x\) can lose at most one unit by deleting one owned chore, so EF1 holds iff \(x\le y+1\) for every ordered pair of agents with respective loads \(x,y\), equivalent to the claimed size-spread bound. In any complete allocation the loads are therefore exactly \(q\) and \(q+1\), occurring \(n-r\) and \(r\) times.

If \(q=0\), each of the \(M\) chores must go to a different agent, giving \(n!/(n-M)!\) assignments. For \(q\ge1\), no agent can receive chores from both sides, and no bundle is empty. Let \(s\) be the number of agents allocated A chores; hence \(1\le s\le n-1\). Exactly \(u_s=a-sq\) of those \(s\) agents receive \(q+1\) chores, and exactly \(v_s=b-(n-s)q\) of the other \(n-s\) agents receive \(q+1\). These values must be in their respective closed integer intervals. Conversely, every choice meeting those bounds yields a complete feasible EF1 allocation. Choose the A agents in \(\binom ns\) ways, their larger-load recipients in \(\binom s{u_s}\) ways, and the larger-load B recipients in \(\binom{n-s}{v_s}\) ways. Distribute the individually labeled A and B chores across their specified sizes in \(a!b!/((q!)^{n-r}((q+1)!)^r)\) ways. Since the A recipient set is determined uniquely by any allocation, distinct terms do not overcount. Summation gives \(C\).

For an incomplete allocation keeping \(z\) chores of one side, maximality forces all \(n\) agents to have nonempty bundles, so \(z\ge n\). EF1 forces \(h=z-nt\) bundles of size \(t+1\) and \(n-h\) bundles of size \(t\), with \(t\ge1\). Choosing which agents have larger bundles and assigning the labeled chores gives \(E_n(z)\), establishing the entire census.

**3. Existence and throughput.** If either \(a\ge n\) or \(b\ge n\), an incomplete maximal EF1 allocation exists by splitting that side's chores as equally as possible into \(n\) nonempty bundles. Otherwise \(a,b<n\). If \(M<n\), allocate each chore to a distinct agent; this is complete and EF1. If \(n\le M<2n\), every agent needs one or two chores. Choose integers \(s_A\) and \(s_B\) such that \(s_A+s_B=n\), \(\lceil a/2\rceil\le s_A\le a\), and \(\lceil b/2\rceil\le s_B\le b\): the lower endpoints sum to at most \(n\) since \(a,b<n\), and the upper endpoints sum to \(M\ge n\); any integer between the sums of two integer intervals is attainable. Assign the A chores to \(s_A\) agents and B chores to \(s_B\) agents with each recipient getting one or two. This is a complete EF1 allocation. Thus every instance has a maximal EF1 allocation, and if no complete one exists, at least one side has size \(\ge n\). By step 1 every incomplete maximal allocation contains exactly an entire side, and the larger side can be allocated fairly; hence the claimed value of \(T\) and the half bound.

**4. Sharpness.** With \(a=2h-1\), \(b=2h+1\), \(n=4\), the total is \(4h\). A complete EF1 allocation would force all four bundles to have size precisely \(h\). For \(h\ge3\) each bundle lies wholly within A or wholly within B; hence both \(a\) and \(b\) would be sums of multiples of \(h\). But \(2h-1\) and \(2h+1\) are not divisible by \(h\), a contradiction. The larger side has \(2h+1\ge4\) chores, so the maximal partial allocation retaining exactly this side and balancing the bundles exists. This gives the sharp ratio. At \((a,b,n)=(5,7,4)\), \(E_4(5)=240\), \(E_4(7)=2520\), and \(C=0\), hence \(2760\) maximal EF1 allocations.

## Verification

The accompanying standalone `verify_biclique.py` uses Python 3's standard library. It independently enumerates every mapping of each labeled chore to one of the \(n\) agents or to the unallocated category, tests each bundle's independence directly, checks all unit-cost EF1 size inequalities and direct insertion maximality, and compares complete/incomplete counts and maximum throughput against the formulas. It passes all \(63\) tested cells with \(n\in\{2,3,4\}\), \(1\le a,b\le5\), \(a+b\le8\) (with \(a+b\le7\) for four agents), examining \(726261\) complete assignment states in total. It also checks the arithmetic formulas at \((a,b,n)=(4,5,3)\) and \((5,7,4)\), and the nonexistence formula across \(67\) values in the infinite sharpness family. Those finite computations are cross-checks; the preceding general proof, not an extrapolation from enumeration, establishes the infinite statements.

Reproduce by running `python3 verify_biclique.py`. No external packages, data files, online services or nondeterministic inputs are required.

## Relationship to prior work

Equbal et al. (arXiv:2402.04353, first public February 6, 2024) formulate EF1 maximal scheduling with conflict graphs, proving important existence results for interval graphs and paths. Igarashi, Manurangsi and Yoneda (arXiv:2506.14149) study general conflict graphs, prove two-agent existence and give negative and complexity results for three or more agents. The later unified work (arXiv:2605.09930) develops these directions further. These results motivate the sharply specified identical-unit-cost biclique case; their inspected text does not supply this maximum-throughput law or the census of incomplete maximal EF1 schedules. Yan and Wang (arXiv:1207.3578) and prior equitable-coloring literature already study the complete equitable coloring question for complete multipartite graphs: the complete-colorability portion is not claimed as independently novel. The additional statements concern **all inclusion-maximal partial EF1 schedules**, their exact number, their maximum possible completion and a sharp uniform loss bound. These are not deductions of the *published theorem statements* just cited without an additional maximality analysis. No claim is made of a conclusive exhaustive novelty search.

## Limitations

Only complete bipartite conflict graphs with two nonempty sides, labeled indivisible chores, identical unit costs and inclusion-maximality are treated. Weighted or heterogeneous disutilities, general bipartite conflict graphs, Pareto optimality, dynamic selection and arbitrary preferences are not addressed. The sharp half bound measures throughput among maximal EF1 schedules, not a price of anarchy for strategic agents. Exact publication priority cannot be guaranteed; equivalent statements may appear under equitable partial-coloring terminology outside the material inspected. The exhaustive computation covers only the finite cells stated above.

## References

- S. Equbal, R. Gurjar, Y. Kumar, S. Nath, R. Saxena and R. Vaish, *Fair Interval Scheduling of Indivisible Chores*, arXiv:2402.04353, first public 2024-02-06. https://arxiv.org/abs/2402.04353
- A. Igarashi, P. Manurangsi and H. Yoneda, *Dividing Conflicting Items Fairly*, arXiv:2506.14149, first public 2025-06-17. https://arxiv.org/abs/2506.14149
- S. Equbal et al., *Fair Allocation under Conflict Constraints*, arXiv:2605.09930, first public 2026-05-11. https://arxiv.org/abs/2605.09930
- Z. Yan and W. Wang, *Equitable chromatic threshold of complete multipartite graphs*, arXiv:1207.3578, first public 2012-07-16. https://arxiv.org/abs/1207.3578
- P. Hummel and L. Hetland, *Fair Allocation of Conflicting Items*, Autonomous Agents and Multi-Agent Systems, DOI 10.1007/s10458-021-09537-3. https://doi.org/10.1007/s10458-021-09537-3
