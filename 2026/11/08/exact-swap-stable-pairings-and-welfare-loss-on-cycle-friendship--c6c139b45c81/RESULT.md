# Exact swap-stable pairings and welfare loss on cycle friendship networks

## Finding

**Theorem.** Let \(n\ge6\) be even and let the agents be the \(n\) individually labeled vertices of an unweighted simple cycle \(C_n\). Partition the agents into unordered coalitions of size two. An agent receives utility \(1\) if their partner is adjacent on \(C_n\), and \(0\) otherwise. A partition is *swap stable* if no two agents belonging to different coalitions can exchange partners such that one swapping agent strictly improves and the other does not lose utility.

Let \(u\) be the number of agents with utility \(0\), and \(B_n(u)\) the number of swap-stable partitions with exactly \(u\) such agents. The social optimum is \(n\). Every stable partition has \(u\) even, and its welfare is \(n-u\). There are exactly two stable optimal partitions, so \(B_n(0)=2\).

The *local characterization* is exact: (i) no two utility-zero vertices are adjacent on the cycle; (ii) no utility-zero pair \(\{x,y\}\) is the pair of endpoints of a three-edge cycle path \(x,p,q,y\) whose middle edge \(\{p,q\}\) is a utility-one coalition. When \(u>0\), consecutive utility-zero vertices in cyclic order have intervening cycle gaps of odd lengths at least three. The two endpoints of a gap of length three may not form one coalition.

For \(u=2\),
\[
B_n(2)=\frac n2\max\!\left\{0,\frac{n-8}{2}\right\}.
\]
For even \(u\ge4\), if \(3u\le n\), set \(s=(n-3u)/2\). With \((-1)!!=1\),
\[
B_n(u)=\frac nu\sum_{j=0}^{u/2}(-1)^j\frac{u}{u-j}\binom{u-j}{j}(u-2j-1)!!\binom{s+u-j-1}{u-j-1}.
\]
All other \(B_n(u)\) are zero. These expressions count partitions of the labeled vertices; the pairs themselves are unordered and unlabeled. Therefore the total number of stable partitions is \(\sum_u B_n(u)\).

The maximum number \(u_{\max}\) of utility-zero agents in a stable partition is \(0\) for \(n\in\{6,8\}\), and \(2\lfloor n/6\rfloor\) for every even \(n\ge10\). Consequently the **exact price of anarchy** is
\[
\operatorname{PoA}(C_n)=\begin{cases}
1,&n\in\{6,8\},\\
\displaystyle\frac{n}{n-2\lfloor n/6\rfloor},&\text{even }n\ge10.
\end{cases}
\]
The first inefficient stable partition occurs at \(n=10\), where the price is \(5/4\). The global bound \(\operatorname{PoA}(C_n)\le3/2\) is attained for every positive multiple of six at least twelve.

## Assumptions and scope

Utilities are **binary and symmetric**, reflecting whether a pair is a cycle edge. Only coalitions of size two are allowed, and the deviation is an **exchange of partners** by two agents drawn from different pairs. The rule is *weak/strict* swap improvement: one of the two agents strictly gains while the other weakly gains; it is neither transferable-utility improvement nor the stronger condition that both strictly gain. Cyclic vertex labels are distinct and held fixed throughout the count. No assumption is made on random preferences or stochastic dynamics. All statements apply to every even \(n\ge6\), not merely to numerically checked sizes.

## Proof

**1. Swap criterion.** Call a coalition a *good pair* if it is an edge of \(C_n\), and a *bad pair* otherwise. Each agent in a good pair has utility one, while both members of a bad pair have utility zero. Exchanging agents between two good pairs cannot improve either exchange participant. Exchanging agents between two bad pairs is improving precisely when an edge of \(C_n\) connects agents belonging to the two bad pairs: then one agent gains and the other cannot lose. (Two members of the same bad pair are nonadjacent by definition.) Thus bad vertices must form an independent set. Finally, when swapping an agent from a bad pair \(\{x,y\}\) with an agent from a good pair \(\{p,q\}\), improvement requires that both swapping agents end up in good pairs, since the initially good participant cannot lose. This happens exactly when \(x,p,q,y\) is a length-three path on \(C_n\), with \(\{p,q\}\) the good pair, up to path reversal. This proves necessity and sufficiency of (i) and (ii).

**2. Gaps.** Remove the bad vertices from the cycle, retaining their cyclic order \(z_1,\ldots,z_u\). The remaining vertices are each in a good pair, so the vertices strictly between successive bad vertices in a gap must be paired consecutively along that gap. Every gap therefore contains an even positive number of interior vertices and has odd edge-length at least three. Conversely every cyclic choice of such gaps admits exactly this matching on their interior vertices. The three-edge forbidden path in part 1 connects exactly the two bad endpoints of a gap of length three, so the bad vertices may be paired arbitrarily except that this endpoint pair is prohibited. Note that the mere presence of a length-three alternating path with unmatched endpoints is insufficient to block a partition: those endpoints must be partners **of the same bad pair**.

**3. Counting for \(u\ge4\).** Write each gap length as \(3+2t_i\) with \(t_i\ge0\). Since the sum of the gap lengths is \(n\), one has \(\sum_i t_i=s\). A gap with \(t_i=0\) forbids pairing its two endpoints. To count legal pairings, apply inclusion-exclusion to the \(u\) cyclic potential forbidden edges between consecutive bad vertices. A selection of \(j\) such edges can be enforced as bad pairs only if the edges are disjoint. For even \(u\ge4\), the number of size-\(j\) matchings of the \(u\)-cycle is
\[
\frac{u}{u-j}\binom{u-j}{j}.
\]
For such a selection, the \(j\) corresponding gap parameters are zero; the other \(u-j\) parameters can be chosen in \(\binom{s+u-j-1}{u-j-1}\) ways. The remaining \(u-2j\) bad vertices can be paired in \((u-2j-1)!!\) ways. Inclusion-exclusion yields the displayed sum. Selecting a first bad vertex yields \(n\) possible labels for the cyclic gap sequence, while each final partition has exactly \(u\) such choices; multiply by \(n/u\). This completes the count.

**4. The case \(u=2\).** There are exactly two gaps between the same two bad partners, so *both* must have length at least five. Writing them as \(5+2a\) and \(5+2b\) gives \(a+b=(n-10)/2\), with \((n-8)/2\) nonnegative ordered solutions for \(n\ge10\). Choosing a first bad vertex in \(n\) ways and dividing by two proves the separate expression. With \(u=0\) there are precisely the two alternating perfect matchings of an even cycle.

**5. Worst welfare.** For \(u>0\), all gaps have length at least three, so \(3u\le n\); since \(u\) is even, \(u\le2\lfloor n/6\rfloor\). The case \(u=2\) additionally forces \(n\ge10\), proving no bad vertices are possible at \(n=6,8\). When \(n=10\), choose two bad vertices five edges apart and pair them, making all other pairs good. For even \(n\ge12\), put \(u=2\lfloor n/6\rfloor\ge4\) bad vertices at gap lengths \(3+2t_i\) with \(\sum t_i=(n-3u)/2\); choose any such composition and match each bad vertex \(z_i\) with its opposite-index vertex \(z_{i+u/2}\). These bad pairs have no adjacent indices, so no gap of length three is closed by a bad pair, and part 1 makes the resulting partition swap stable. Therefore the bound is attained. The optimal welfare is \(n\) (two all-good perfect matchings), while worst stable welfare is \(n-u_{\max}\); dividing proves the exact ratio and the stated sharpness cases.

## Verification

Run `python3 verify_cycle_pairs.py` with the standard library. It enumerates all \(146595\) pair partitions on the cycle orders \(6,8,10,12,14\), checks every agent-to-agent exchange directly, and independently compares with the local characterization and the closed exact count. The counts by \(u\) are: at \(n=10\), \((2,5)\) for \(u=(0,2)\); at \(n=12\), \((2,12,3)\) for \(u=(0,2,4)\); at \(n=14\), \((2,21,14)\). It also checks calculated totals through \(n=30\). These finite calculations verify sample cases, not the unbounded quantifiers; the proof above provides the latter.

## Relationship to prior work

Bilò, Monaco, and Moscardelli introduce the symmetric additively separable fixed-size coalition model, distinguish swap stability from transferable and strict swap variants, prove stability existence and general social-welfare bounds, and establish general complexity results. Their Theorem 6 bounds the price of anarchy by \(2k-1\) for \(k\) coalitions; this does not determine the exact ratio or count of stable assignments on a cycle with pairs. The present theorem adds a specialized local characterization, exact labeled-partition enumeration, a first inefficient order, and a uniform sharp \(3/2\) price bound. Exchange-stable roommates literature more generally concerns ordinal preferences, rather than this fixed symmetric binary cycle-valued instance. The standard graph-theoretic condition of absence of augmenting paths is **not** equivalent to the stated weak swap rule: the endpoints of a length-three path must belong to one existing bad coalition.

## Limitations

This theorem is limited to even, simple cycles and binary adjacency utilities, fixed coalition size two, and weak/strict swap improvement. It does not characterize other graphs, larger coalitions, odd numbers of agents, strict-both-improvement swaps, or swaps under transferable utilities. The exact formula is a sum that may be evaluated arithmetically, not a claimed asymptotic estimate for the full census. Full originality cannot be guaranteed against unindexed, unpublished, or inaccessible literature; in particular specialized matching-enumeration work may contain equivalent statements. The computational checker is finite and not an external proof of the general theorem. Independent external validation has not occurred.

## References

1. V. Bilò, G. Monaco, and L. Moscardelli, *Hedonic Games with Fixed-Size Coalitions*, Proceedings of AAAI 36(9), 9287–9295 (published 2022-06-28). DOI: https://doi.org/10.1609/aaai.v36i9.21156. Full text: https://ojs.aaai.org/index.php/AAAI/article/download/21156/20905.
2. J. Wilczynski, *Ordinal Hedonic Seat Arrangement under Restricted Preference Domains: Swap Stability and Popularity*, IJCAI 2023, https://www.ijcai.org/proceedings/2023/324. This concerns a distinct host/seating graph model.
