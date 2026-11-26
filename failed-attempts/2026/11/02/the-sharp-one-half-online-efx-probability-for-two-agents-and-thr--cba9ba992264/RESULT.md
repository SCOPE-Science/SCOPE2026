# The sharp one-half online EFX probability for two agents and three goods

## Finding

For two agents with arbitrary nonnegative additive valuations, three indivisible goods arriving sequentially, immediate irrevocable assignment of each good, and an oblivious (input-fixed) adversary, the optimal worst-case probability of an exact envy-free-up-to-any-good (EFX) final allocation is

\[
\sup_{\mathcal A}\inf_{I:\,|N|=2,\,|G|=3}
\Pr[\mathcal A(I)\text{ is EFX}]=\frac12.
\]

The supremum ranges over all randomized online algorithms that observe the current good's two values before allocating it, and the infimum ranges over fixed ordered valuation profiles. A constructive algorithm achieves the lower bound using only two fair coins and no future valuations. The upper bound holds even for identical strictly positive valuations and even when the number of goods is announced.

## Assumptions and scope

Let the agents be \(1,2\) and the goods arrive as \(g_1,g_2,g_3\). Agent \(i\)'s valuation is additive, \(v_i(S)=\sum_{g\in S}v_i(g)\), with \(v_i(g)\geq0\). The algorithm observes both values of \(g_t\) before irrevocably assigning it at time \(t\); it cannot inspect later values or move previously allocated goods. The adversary fixes the complete ordered sequence independently of the algorithm's random choices.

An allocation \((A_1,A_2)\) is EFX when for all \(i\ne j\) and every \(g\in A_j\), \(v_i(A_i)\geq v_i(A_j\setminus\{g\})\). The lower-bound algorithm always outputs bundles of cardinalities \(1\) and \(2\). For such an allocation, EFX holds **exactly when** the singleton recipient values her singleton at least as highly as each good in the pair. The pair recipient automatically satisfies the EFX condition when comparing her pair to the singleton (after deleting the singleton's only good, the other bundle is empty).

To handle equal valuations, rank goods by decreasing value, breaking ties in fixed order \(g_1\succ g_2\succ g_3\). A good called 'top' below is top under this deterministic total ranking, which guarantees it is also weakly value-maximal.

## Proof

**Online policy.** Toss a fair coin to choose the recipient of \(g_1\). Upon observing \(g_2\), compare each agent's value for \(g_1\) versus \(g_2\), with the tie convention above.

* If the agents favor **opposite** members of \(\{g_1,g_2\}\), call the agent favoring \(g_1\) agent \(a\). If the first good went to \(a\), give the second to the other agent; otherwise give the second to the same recipient as the first.
* If the agents favor the **same** member of \(\{g_1,g_2\}\), use a second fair coin: give the second good to the first recipient with probability \(1/2\), or to the other recipient with probability \(1/2\).

After observing \(g_3\), try both possible recipients for it, and choose a completion satisfying the EFX inequalities if one exists; otherwise choose either recipient. This last step never revises earlier decisions and can be carried out by four direct comparisons.

**Lower bound: opposite two-good rankings.** Write \(a\) for the agent favoring \(g_1\), and \(b\) for the agent favoring \(g_2\). With probability \(1/2\), \(a\) receives \(g_1\), so the algorithm gives \(g_2\) to \(b\). If \(g_3\) is **not** top for both agents simultaneously, at least one of \(g_1\) for \(a\) and \(g_2\) for \(b\) is top for its owner. The final good can be given to the other agent, leaving that top good alone; EFX follows from the singleton criterion. In the complementary event that \(g_3\) is top for both, the other first-coin outcome occurs with probability \(1/2\): \(b\) gets both first goods and \(a\) receives \(g_3\), again EFX. Thus the success probability is at least \(1/2\).

**Lower bound: both favor \(g_1\).** Every agent's chosen top among the three goods is either \(g_1\) or \(g_3\). Write \(T_i=1\) if agent \(i\)'s top is \(g_3\), and \(T_i=0\) otherwise. Conditional on \(g_1\) going to \(i\), write \(j\ne i\). Giving \(g_2\) to \(i\) succeeds if \(T_j=1\), by making \(g_3\) the singleton for \(j\). Giving \(g_2\) to \(j\) succeeds if \(T_i=0\), by making \(g_1\) the singleton for \(i\). Consequently the conditional success probability is at least \((T_j+1-T_i)/2\). Averaging over the uniform choice of first recipient yields exactly \(1/2\) as a lower bound, since the two \(T\)-terms cancel.

**Lower bound: both favor \(g_2\).** Conditional on any first recipient \(i\), write \(j\ne i\). Agent \(j\)'s top is either \(g_2\) or \(g_3\). Giving \(g_2\) to the first recipient \(i\) allows \(g_3\) to be \(j\)'s singleton if \(j\) ranks \(g_3\) first. Giving \(g_2\) to \(j\) permits \(g_2\) to be \(j\)'s singleton if \(j\) ranks \(g_2\) first. One of these mutually exclusive events always occurs, and each second-good choice has probability \(1/2\). Therefore the success probability is at least \(1/2\). These cases exhaust every profile, including ties via the common tie-breaking convention.

**Upper bound.** Fix any randomized irrevocable algorithm, even one told that three goods will arrive. Compare two fixed inputs, identical through time \(2\): each agent values each of \(g_1,g_2\) at \(1\). In the first input both value \(g_3\) at \(\varepsilon\) for some \(0<\varepsilon<1\); in the second, both value \(g_3\) at \(L\) for any \(L>1\). In the first input, a successful EFX allocation requires \(g_1,g_2\) to have **different recipients**, since otherwise the low-valued final singleton would envy the pair after any deletion. In the second, a successful EFX allocation requires \(g_1,g_2\) to have the **same recipient**, since otherwise the earlier singleton would envy the bundle containing \(g_3\) after its other good is deleted. The algorithm's distribution over the two mutually exclusive events is identical on the two inputs, because the prefixes coincide. Hence at least one input has success probability at most \(1/2\). Together with the policy, the minimax value is exactly \(1/2\). \(\square\)

## Verification

The standalone Python 3 file `verify_online_efx.py` directly tests EFX inequalities, computes the exact probability of the displayed policy using rational arithmetic, and enumerates all \(5^6=15{,}625\) two-agent three-good valuation profiles with values in \(\{0,1,2,3,4\}\). Every profile had exact success probability at least \(1/2\); the histogram was \(9{,}200\) profiles at \(1/2\), \(2{,}800\) at \(3/4\), and \(3{,}625\) at \(1\). It also enumerates all eight deterministic complete recipient strings for each of the two indistinguishable-prefix upper-bound instances and verifies that their required first-two-good allocation patterns are disjoint. Run `python3 verify_online_efx.py` from the directory containing this document.

The enumeration is a finite cross-check **not** an infinite-domain proof; the proof above covers all real nonnegative additive values. No computer-assisted classification or external certificate is needed for the theorem.

## Relationship to prior work

Cohen, Teh, and Wooldridge (arXiv:2609.28333v1, Theorem 5.4 and its proof) establish that for \(n\) agents and \(n+1\) sequential goods the worst-case exact-EFX success probability is at most \(1/n!\), and give a universal algorithm achieving at least \(2/((n+1)n!)\). At \(n=2\), these bounds specialize to \(1/2\) and \(1/3\). The present adaptive first-two-good policy establishes the **matching \(1/2\) lower bound** for that first nontrivial case; the cited general theorem supplies an independent upper bound, while the two-input proof above is self-contained.

Neoh and Teh (arXiv:2504.03951v1, Proposition 3.6) establish the existence and tight minimum number of EFX allocations for \(m=n+1\) goods in the offline model. Counting ex-post EFX allocations does not give the sharp guarantee for an irrevocable online algorithm that sees goods only upon arrival. Garg and Sharma (arXiv:2410.08986) study randomized envy-cycle elimination with ex-post fairness, but their allocation procedures use complete-instance preprocessing and/or changes to bundles, unlike the irreversible chronological choices here.

## Limitations

The exact value is for two agents and **exactly three** goods under additive nonnegative valuations with both current item values visible, full allocation, and no reallocations. The proof does not determine the optimal success probability for three or more agents, four or more goods, chores, private valuations, or stronger fairness properties. It does not show the exact worst-case expected approximate-EFX ratio; exact success probability is a different objective. While targeted comparisons identify the distinction from relevant published results, exhaustive publication-priority searches across every venue are not possible.

## References

1. S. Cohen, N. Teh, and M. Wooldridge. *Online Fair Division Against an Oblivious Adversary*. arXiv:2609.28333v1, first submitted September 23, 2026. Theorem 5.4, Section 5.3.
2. T. Y. Neoh and N. Teh. *Understanding EFX Allocations: Counting and Variants*. arXiv:2504.03951v1, April 4, 2025. Proposition 3.6.
3. J. Garg and E. Sharma. *Best-of-Both-Worlds Fairness of the Envy-Cycle-Elimination Algorithm*. arXiv:2410.08986, October 11, 2024. Relevant ex-post EFX context; not an irrevocable online bound.
