# Local PMMS equals leximin on weighted stars: exact census and a zero-hub transition

## Finding

**Theorem (complete connected-allocation classification).** Let the item graph be a star with a center and \(k\ge1\) indexed leaves. There are \(1\le n\le k+1\) individually labeled agents with the same nonnegative additive utility. Write \(h\ge0\) for the value of the center and \(w_1,\ldots,w_k\ge0\) for the leaf values. Every item is allocated and every agent receives a nonempty connected bundle. Put \(r=k-n+1\). A connected allocation is locally pairwise maximin-share fair (PMMS), in the sense of the induced neighboring-bundle relation, **if and only if** its sorted vector of agent utilities is lexicographically maximal among all such connected allocations (leximin).

More explicitly, let \(I\) be the set of \(r\) leaves held by the agent receiving the center, and let \(S=[k]\setminus I\). When both sets are nonempty, the allocation is PMMS exactly when either

\[
\max_{i\in I} w_i\le\min_{j\in S}w_j,
\]

or \(h=0\) and at most one leaf in \(I\) has positive value. The first alternative says that the center recipient holds the \(r\) least-valued leaves, with arbitrary tie-breaking; the second is a genuine zero-center exception. The cases \(r=0\) and \(S=\varnothing\) are always PMMS.

Let \(z=|\{i:w_i=0\}|\), \(p=k-z\), and interpret \(\binom{a}{b}=0\) outside \(0\le b\le a\). For \(r>0\), let \(v_r\) be the \(r\)-th smallest leaf value, \(s_r=|\{i:w_i<v_r\}|\), and \(t_r=|\{i:w_i=v_r\}|\). The exact number \(Q_r\) of possible center-recipient leaf subsets in PMMS allocations is

\[
Q_r=\begin{cases}
1,&r=0,\\
\binom{z}{r}+p\binom{z}{r-1},&h=0,\quad 1\le r\le z+1,\\
\binom{t_r}{r-s_r},&\text{otherwise}.
\end{cases}
\]

The exact number of PMMS allocations to labeled agents is \(n!Q_r\), out of \(n!\binom{k}{r}\) connected allocations. Thus a uniformly sampled connected allocation is PMMS with probability \(Q_r/\binom{k}{r}\). These are exact finite equalities for arbitrary nonnegative real values, including ties and zero values.

**Sharp boundary phenomenon.** If all leaf values are positive and pairwise distinct, then for \(2\le n\le k-1\) the fair fraction is \(1/\binom{k}{r}\). When \(n=k\), it jumps to \(1\) if \(h=0\), but remains \(1/k\) for every \(h>0\), however small. At \(n=k+1\) every connected allocation is PMMS. For \(k\ge3\), the transition from \(n=k-1\) to \(n=k\) at \(h=0\) multiplies the fair fraction by exactly \(\binom{k}{2}\).

## Assumptions and scope

The star has one center, \(k\) distinguishable leaves, and no other edges. Valuations are common to every agent, additive and nonnegative on each vertex; utilities need not be integral. Each agent's bundle must be nonempty and connected, and the allocation must partition all \(k+1\) vertices. Only agents whose allocated bundles touch across a graph edge compare, and their two-way maximin share is computed over connected bipartitions of the induced subgraph on their pooled vertices. The theorem makes no assertion about heterogeneous valuations, other item graphs, or allocations with empty bundles.

## Proof

**1. Shape of connected partitions.** At most one bundle contains the center. Every other connected nonempty bundle consists of exactly one leaf, so the center bundle is \(\{c\}\cup I\), with \(|I|=r\), and each leaf of \(S\) is given to a different agent. Conversely, every such choice, together with an assignment of the bundles to agents, is feasible. There are \(n!\binom{k}{r}\) connected allocations.

**2. Exact local two-way maximin share.** Write \(H=h+\sum_{i\in I}w_i\). For any singleton leaf \(j\in S\), the union of its bundle with the center bundle is a star on \(I\cup\{j\}\) and the center. Any connected bipartition of this union isolates exactly one leaf \(\ell\), hence the pair's common maximin share is

\[
\mu_j=\max_{\ell\in I\cup\{j\}}\min\bigl(w_\ell,H+w_j-w_\ell\bigr).
\]

The existing pair of utilities is \((H,w_j)\), and choosing \(\ell=j\) shows \(\mu_j\ge\min(H,w_j)\). Both neighboring agents satisfy PMMS precisely when equality holds. Distinct singleton agents are not adjacent, so there are no other nontrivial comparisons.

**3. Classification of violations.** Fix \(i\in I\) and \(j\in S\). If \(w_i\le w_j\), isolating \(i\) produces a minimum at most \(w_i\le\min(H,w_j)\), using \(H\ge w_i\). If \(w_i>w_j\), then \(H\ge w_i>w_j\), and the alternative isolated-\(i\) partition strictly improves the minimum if and only if \(H>w_i\). Thus an allocation fails PMMS precisely when there exist \(i\in I,j\in S\) with \(w_i>w_j\) and \(H>w_i\). Either no such inversion exists, yielding the sorted-leaf condition, or every inversion requires \(H=w_i\). By additivity and nonnegativity, the latter equality can hold only when \(h=0\) and all other leaves in \(I\) have zero value, giving the exceptional condition. Conversely, either alternative prevents all strict improvements, proving the classification. Empty \(I\) or \(S\) gives no offending pairs.

**4. Exact count.** In the sorted case \(I\) contains all \(s_r\) leaves below \(v_r\), none above it, and exactly \(r-s_r\) of the \(t_r\) leaves equal to it. Hence it has \(\binom{t_r}{r-s_r}\) choices. If \(h>0\), these are all choices. If \(h=0\) and \(r>z+1\), the center bundle necessarily contains at least two positive leaves, so again there are no exceptional choices. If \(h=0\) and \(1\le r\le z+1\), every sorted center bundle has at most one positive leaf, and the entire fair family is exactly the subsets with zero or one positive leaf. There are \(\binom{z}{r}+p\binom{z}{r-1}\) of them. For \(r=0\), there is one center-leaf subset (empty). Multiplying by the \(n\) choices for the center recipient and the \((n-1)!\) bijections for singleton recipients gives \(n!Q_r\).

**5. PMMS is exactly leximin.** If an allocation fails PMMS, Step 3 supplies leaves \(i\in I\) and \(j\in S\) with \(w_i>w_j\) and \(H>w_i\). Exchange these two leaves between the center and singleton recipients. The old pair has minimum \(w_j\); the new pair has utilities \(H-w_i+w_j\) and \(w_i\), both strictly larger than \(w_j\), and the other agents' utilities are unchanged. Thus the globally sorted utility vector improves lexicographically. Every leximin allocation is therefore PMMS.

Conversely, all sorted-leaf PMMS allocations have the same multiset of held-leaf values, hence the same multiset of agent utilities. If the zero-center exception applies, each positive leaf value appears as the utility of exactly one agent, while all other agents have utility zero; the resulting utility multiset is again independent of the exceptional center choice. The sorted options in this regime are also exceptional. Consequently **all** PMMS allocations share a single sorted utility vector. A leximin allocation exists by finiteness and, as just proved, is PMMS. Every PMMS allocation therefore has that leximin vector, establishing the reverse implication.

**6. The zero-center transition.** With distinct positive leaf values, \(z=0\). For \(r\ge2\), the only PMMS center-leaf subset is the \(r\) smallest leaves. At \(r=1\), if \(h=0\) every leaf can be the center's leaf, whereas for \(h>0\) only the least-valued leaf works. For \(r=0\), all singleton assignments work. The fractions and their exact jump follow by dividing by \(\binom{k}{r}\).

## Verification

Run `python3 verify_star_pmms.py` in the directory containing the attached standalone verifier. It independently enumerates connected paired bipartitions rather than assuming the sorted-leaf criterion, enumerates all center-subset choices for each parameter instance, compares the theorem's counts, and optimizes every global sorted utility vector to test the PMMS–leximin equivalence. Actual execution returned `CHECK_OK settings 83309 connected_partition_choices 1391766` and `ZERO_HUB_CLIFF_OK`. The exhaustive portion covers \(1\le k\le7\), all leaf values in \(\{0,1,2\}\), and center values \(\{0,1,2\}\); supplementary deterministic-seed random tests cover \(k=8,9\). These finite checks corroborate but do not replace the general proof.

## Relationship to prior work

Hummel and Igarashi (2024, arXiv:2401.14825) introduce the local connected-bundle PMMS framework. Their Theorem 6.1 proves that a leximin allocation is PMMS under common valuations, and their tree algorithm finds an allocation with PMMS and MMS guarantees. The **converse on stars**, the all-allocation structural characterization, the exact labeled count for all nonnegative common additive weights, and the zero-hub fairness transition are the distinctions established here; the prior existence/algorithmic theorems do not imply this complete census. Bouveret et al. (2017, arXiv:1705.10239) introduce connected graph fair division and address proportionality, envy-freeness and MMS, including star algorithms, without stating the local PMMS classification. A published exact equivalent elsewhere cannot be conclusively ruled out by finite bibliographic searches.

## Limitations

The classification concerns nonempty bundles under identical nonnegative additive utility. It does not extend without further analysis to heterogeneous valuations, arbitrary graph topologies, or empty-bundle conventions. The finite verifier is not an infinite proof or an independent external audit. Novelty is judged relative to inspected accessible literature and may be affected by unindexed prior work. The sharp change at zero center utility is not claimed for a strictly positive center.

## References

1. H. Hummel and A. Igarashi, *Keeping the Harmony Between Neighbors: Local Fairness in Graph Fair Division*, AAMAS 2024, pp. 852–860; preprint first public 2024-01-26, https://arxiv.org/abs/2401.14825 .
2. S. Bouveret, K. Cechlárová, E. Elkind, A. Igarashi and D. Peters, *Fair Division of a Graph*, IJCAI 2017, pp. 135–141, https://arxiv.org/abs/1705.10239 .
3. G. Amanatidis, G. Birmpas and E. Markakis, *Comparing Approximate Relaxations of Envy-Freeness*, preprint https://arxiv.org/abs/1806.03114 (background on unconstrained PMMS, distinct from local graph-connected PMMS).
