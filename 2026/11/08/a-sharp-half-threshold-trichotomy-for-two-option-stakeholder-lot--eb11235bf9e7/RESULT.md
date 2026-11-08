# A sharp half-threshold trichotomy for two-option stakeholder lotteries

## Finding

**Theorem.** For the deterministic membership-query minimization-of-violations problem defined below, the exact worst-case additive rejection regret under a budget of \(K\) distinct queried agents is

\[
\mathcal R_{n,K}(a,b)=
\begin{cases}
0,&b\le \tfrac12,\\
\max\{0,n-K-(K\bmod 2)\},&a>\tfrac12,\\
n-K,&a\le\tfrac12<b.
\end{cases}
\]

This holds for all integers \(n\ge1\) and \(0\le K\le n\), and all known \(0<a\le b\le1\) in the finite-grid model. Thus two alternatives already attain the full \(n-K\) worst-case gap if allowable thresholds straddle \(1/2\), while strict thresholds wholly above \(1/2\) admit a parity-dependent improvement. A common lottery is acceptable to all agents when all thresholds are at most \(1/2\).

## Assumptions and scope

There are two alternatives. A lottery is \((t,1-t)\) with \(t\in[0,1]\). Each of \(n\) agents has a hidden normalized binary utility vector, either \((1,0)\), called right-oriented, or \((0,1)\), called left-oriented, and a hidden threshold \(\tau_i\in[a,b]\). The numbers \(a,b\) and a common finite rational threshold grid \(\Gamma\subset(0,1]\) are publicly known, with \(a,b\in\Gamma\); \(\tau_i\in\Gamma\cap[a,b]\). Right-oriented agents accept iff \(t\ge\tau_i\), and left-oriented agents accept iff \(t\le1-\tau_i\). Every agent accepts some lotteries and rejects others.

A membership query names one agent and one \(t\), and returns only acceptance or rejection. Algorithms are deterministic, always terminate after finitely many queries, and contact at most \(K\) *distinct* agents, with arbitrarily many queries to a contacted agent. Their output may be any real \(t\in[0,1]\). Let \(V_I(t)\) be the number of rejecting agents in profile \(I\), let \(\mathrm{OPT}(I)=\min_{t\in[0,1]}V_I(t)\), and let \(\mathcal R_{n,K}(a,b)\) be the infimum over such algorithms of the supremum over all permitted profiles of \(V_I(t_A(I))-\mathrm{OPT}(I)\). The algorithm knows \(n,K,a,b,\Gamma\), but no private type or threshold.

## Proof

**Common-threshold side.** If \(b\le1/2\), both orientations accept \(t=1/2\), because \(\tau_i\le b\le1/2\). Hence the output \(1/2\), without any queries, is optimal on all profiles.

**Strict-threshold side: upper bound.** Assume \(a>1/2\). No right- and left-oriented acceptance intervals meet; no lottery can satisfy both orientations. Hence the full-information optimum is a pure lottery supporting the numerically larger orientation class. The membership query at \(t=1\) identifies orientation (right accepts; left rejects), regardless of the exact threshold. Query any \(K\) agents and choose a pure lottery supporting the majority of their orientations, with an arbitrary fixed tie break. Let \(d\) be the absolute difference between the two queried class sizes and \(U=n-K\). If the unqueried agents all favor the opposite side, they can reverse the majority only when \(U>d\); in any completion the regret is at most \(\max\{0,U-d\}\). Since \(d\ge K\bmod2\), the upper bound is \(\max\{0,n-K-(K\bmod2)\}\).

**Strict-threshold side: lower bound against adaptive querying.** Fix an arbitrary deterministic algorithm. On the first contact of each new agent, answer all its subsequent queries consistently with threshold \(a\) and with orientations assigned alternately right, left, right, left, independently of the identity of the new agent. This defines a consistent transcript. Suppose \(q\le K\) agents were contacted and their orientation-count difference has absolute value \(d=q\bmod2\). The algorithm's chosen \(\widehat t\) is either in the right acceptance region \([a,1]\), in the left acceptance region \([0,1-a]\), or in the gap \((1-a,a)\). In the first case complete every untouched agent as left-oriented at threshold \(a\); in the second complete them all as right-oriented at threshold \(a\). Since the observed orientations differ by only \(d\), comparing the algorithm's accepted count with the better pure lottery gives regret at least \(\max\{0,n-q-d\}\). In the gap the algorithm has zero acceptances while some pure lottery accepts at least \(n-q\) untouched agents, so the same bound holds. Finally \(q+(q\bmod2)\le K+(K\bmod2)\), and regret is nonnegative. This gives the claimed lower bound, including when an algorithm stops before using all \(K\) contacts.

**Crossing-threshold side: upper bound.** Suppose \(a\le1/2<b\). By asking each of any \(K\) designated agents about \(t=1\), one learns its orientation. Finite-grid binary search of its interval endpoint then recovers its threshold exactly using finitely many queries. Select a lottery minimizing the number of rejections among these \(K\) agents; this is possible by sorting their closed acceptance-interval endpoints. Compare that lottery with a globally optimal lottery: on the queried agents it performs no worse, and among the \(U=n-K\) others it can incur at most \(U\) additional rejections. Thus regret is at most \(U\).

**Crossing-threshold side: lower bound against adaptive querying.** Fix a deterministic algorithm, and answer all its queries as though every agent is right-oriented with threshold \(a\). This is a consistent transcript involving \(q\le K\) contacted agents and output \(\widehat t\). Retain that type on the contacted agents. Set all untouched agents as follows:

- If \(\widehat t<b\), make them right-oriented with threshold \(b\). They reject \(\widehat t\), but \(t^*=1\) satisfies everybody.
- If \(\widehat t\ge b\) and \(\widehat t>1-a\), make them left-oriented with threshold \(a\). They reject \(\widehat t\), but \(t^*=a\) satisfies everybody, since \(a\le1/2\).
- Otherwise \(b\le\widehat t\le1-a\). Make them left-oriented with threshold \(b\). Since \(b>1/2\), they reject \(\widehat t\); also \(b\le1-a\), so \(t^*=a\) satisfies everybody.

The completed profile reproduces all answers and the algorithm's output, since untouched agents were never queried. Its optimal violation count is zero while at least \(n-q\ge n-K\) agents reject the output. Hence the lower bound matches the upper bound. The construction uses only the two permitted threshold endpoints \(a,b\) and therefore respects the finite grid.

Combining the three cases proves the theorem. If \(K=n\), all formulas correctly return zero.

## Verification

The companion standalone Python program `check_exact.py` uses only the standard library and rational arithmetic. It exhausts all fixed-observed-\(K\) type profiles and adversarial unqueried multisets for \(1\le n\le5\), \(0\le K\le n\), in seven threshold-domain configurations (\(140\) comparisons to the closed form). It also tests the constructive crossing-threshold adversary at all breakpoints and open-chamber representatives on four rational grids (\(470\) tests). These finite enumerations are consistency checks, not proofs for arbitrary \(n,K,a,b\) or arbitrary adaptive algorithms; those claims follow from the preceding adversarial transcript arguments.

Run with `python3 check_exact.py`.

## Relationship to prior work

Teh and Goldberg (2026, arXiv:2610.37828v1), Section 6, prove the exact \(n-K\) deterministic worst-case rejection gap for **at least three** alternatives. Their proof explicitly needs a third alternative; Appendix E.1 gives exact full-information optimization for two alternatives, and Appendix I.1 supplies a general post-history regret formula without a two-option threshold classification. The result above gives a sharp two-alternative phase diagram under a public threshold-range constraint, with a parity improvement when all thresholds strictly exceed half. Choo, Goldberg and Teh (2026, arXiv:2604.17505v1) address unanimous feasibility from membership queries rather than worst-case loss in the minimum-violations objective. Explicit-constraint maximum feasible subsystem algorithms do not by themselves establish the unknown-agent query-budget trichotomy.

## Limitations

The theorem concerns deterministic algorithms, worst-case profiles and a bound on **distinct contacted agents**, not the total number of membership queries, randomized sampled-agent algorithms, average-case performance, or more than two alternatives. Its finite-grid condition is necessary for the stated *exact-recovery* upper bound when thresholds are otherwise arbitrary real numbers; the direct lower bounds need only the two endpoint thresholds. An exact equivalent theorem in unindexed literature remains possible. No independent audit has been performed.

## References

1. Nicholas Teh and Paul W. Goldberg, *Learning Lotteries with Minimal Stakeholder Violations from Membership Queries*, arXiv:2610.37828v1 (first public 2026-10-27), https://arxiv.org/html/2610.37828v1, especially Section 2, Section 6, Appendix E.1 and Appendix I.1.
2. Davin Choo, Paul W. Goldberg and Nicholas Teh, *Learning Unanimously Acceptable Lotteries via Queries*, arXiv:2604.17505v1 (first public 2026-04-19), https://arxiv.org/html/2604.17505v1.
