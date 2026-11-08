# Sharp rational-exchange horizons for repeated two-good fair division

## Finding

**Theorem (exact three-axiom compatibility, count, and sharp horizon).** Consider two agents and two persistent indivisible goods \(A,B\), each available once in each of \(k\ge1\) rounds. The additive, time-independent values are
\[
(u_1(A),u_1(B))=(a,b),\qquad (u_2(A),u_2(B))=(c,d),
\]
where \(a>b>0\) and \(c>d>0\) are arbitrary real numbers. Every good is assigned to exactly one agent each round. Require simultaneously (i) envy-freeness up to one good in **every** round, (ii) envy-freeness of the total allocation of all copies, and (iii) Pareto optimality of that total allocation **among all unrestricted allocations of the copies**, including ones with both goods assigned to the same agent in a round.

Set \(\rho_1=a/b\), \(\rho_2=c/d\). If \(\rho_1=\rho_2\), put \(T=\infty\). Otherwise define the positive integer
\[
T=\min\left\{t\ge2:\ \exists s\in\{1,\ldots,t-1\}\text{ with }\min(\rho_1,\rho_2)\le \frac ts\le\max(\rho_1,\rho_2)\right\}.
\]
Then the number of valid **ordered** \(k\)-round allocation sequences is exactly
\[
N_k=\begin{cases}
\displaystyle\binom{2m}{m},&k=2m,\quad m<T,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, for unequal ratios, compatibility fails at every even horizon \(k\ge2T\), whereas proportional utility vectors permit compatibility for every even horizon.

For positive integer values, let \(g_1=\gcd(a,b)\), \(g_2=\gcd(c,d)\). If \(\rho_1\ne\rho_2\), the cutoff satisfies the **sharp** bound
\[
T\le\min\left\{\frac a{g_1},\frac c{g_2}\right\}.
\]
For each integer \(h\ge1\), the values \((a,b;c,d)=(h+1,h;h+2,h+1)\) attain equality \(T=h+1\). Thus the first failing even horizon can be arbitrarily delayed even under positive integral values where both agents strictly prefer the same good.

## Assumptions and scope

Every period makes one copy of each of the two goods available and assigns both copies completely. The two agents have time-independent positive additive valuations, and each strictly prefers \(A\) over \(B\). A round is EF1 if every agent's envy can be eliminated by deleting at most one good from either of the two compared bundles (the ordinary EF1 definition for nonnegative goods). Overall envy-freeness and overall Pareto efficiency evaluate the \(2k\) separate item copies; efficiency competitors need **not** obey per-round EF1 or any one-good-per-agent constraint. Ordered rounds are distinguishable, though copies of the same good have the same utility.

No integrality is needed for the main exact cutoff. The separate sharp bound assumes strictly positive **integer** values. At \(\rho_1=\rho_2\), the cutoff is formally infinite, not an integer.

## Proof

**Step 1 (per-round EF1 forces a perfect pairing).** If both strictly positive goods go to one agent, the agent with the empty bundle still envies after either one good is removed from the other bundle. Therefore the round is not EF1. Conversely, if each agent receives exactly one good, removing the other's good eliminates any envy. Thus every admissible round is one of the two orientations \((A,B)\) or \((B,A)\).

**Step 2 (overall envy fixes the counts).** Let \(x\in\{0,\ldots,k\}\) denote the number of rounds in which agent 1 gets \(A\). The per-round pairing condition means agent 1 gets \(B\) in the remaining \(k-x\) rounds, so her total utility is \(ax+b(k-x)\). Agent 2's total utility is \(c(k-x)+dx\). Since every item is allocated, two-agent envy-freeness is equivalent to each agent obtaining at least half of their respective value for all \(k\) copies of both goods. The inequalities reduce to
\[
(a-b)(x-k/2)\ge0,\qquad (c-d)(k/2-x)\ge0.
\]
Strict positivity of \(a-b\) and \(c-d\) therefore forces \(x=k/2\). In particular, odd \(k\) is impossible. For \(k=2m\), there are exactly \(\binom{2m}{m}\) paired sequences and they all induce the same total item counts: each agent receives \(m\) copies of each good.

**Step 3 (complete integer characterization of strict Pareto domination).** Write \(X,Y\in\{0,\ldots,2m\}\) for the counts of \(A,B\) allocated to agent 1 in an arbitrary competing allocation. Every such pair is attainable without imposing the roundwise pairing restriction. Relative to the balanced counts \((m,m)\), put \(\delta X=X-m\), \(\delta Y=Y-m\). The two agents' changes in utility are
\[
\Delta_1=a\delta X+b\delta Y,\qquad \Delta_2=-c\delta X-d\delta Y.
\]
If both changes are nonnegative and at least one is positive, \(\delta X\) and \(\delta Y\) must be nonzero with opposite signs. If \((\delta X,\delta Y)=(s,-t)\) with \(s,t\ge1\), the conditions are precisely \(c/d\le t/s\le a/b\). If instead \((\delta X,\delta Y)=(-s,t)\), the conditions are precisely \(a/b\le t/s\le c/d\). The bounds \(0\le X,Y\le2m\) are equivalent to \(s,t\le m\). If \(\rho_1=\rho_2\), both utility changes must vanish for any weakly improving exchange, hence strict domination is impossible. If \(\rho_1\ne\rho_2\), any rational \(t/s\) in the closed interval between the distinct ratios has at least one strict utility improvement. Since both endpoints exceed 1, every such positive rational satisfies \(t>s\), so \(s,t\le m\) is equivalent to \(t\le m\). Consequently the balanced allocation is Pareto optimal exactly when \(m<T\). Combining with Step 2 proves the formula for \(N_k\), including all boundary equalities.

**Step 4 (finite and sharp integer horizon).** For unequal ratios and positive integer values, each reduced endpoint fraction, \((a/g_1)/(b/g_1)\) or \((c/g_2)/(d/g_2)\), is a permitted rational, giving the stated upper bound on \(T\). For the family \((h+1,h;h+2,h+1)\), the distinct ratio interval is
\[
\left[\frac{h+2}{h+1},\frac{h+1}{h}\right].
\]
The right endpoint is attained by \((t,s)=(h+1,h)\). No smaller numerator \(t\le h\) is possible: when \(h=1\), such a numerator cannot exceed its positive denominator; when \(h\ge2\), every \(1\le s<t\le h\) has
\[
\frac ts\ge\frac{t}{t-1}\ge\frac h{h-1}>\frac{h+1}{h}.
\]
Thus \(T=h+1\), with equality in the general integer bound. At the first failing horizon, the explicit exchange of \(h\) copies of \(A\) toward agent 1 against \(h+1\) copies of \(B\) away from agent 1 changes the agents' utilities by \((0,1)\), witnessing a strict Pareto improvement. This completes the proof.

## Verification

Run `python3 verify.py` using the supplied standalone script. It uses only standard-library integer and rational arithmetic. It compares the rational-cutoff criterion against direct Pareto dominance over all \((X,Y)\in\{0,\ldots,k\}^2\) for \(5{,}292\) integer-profile/horizon combinations, checks \(34\) parametric sharp-horizon instances, and independently enumerates \(109{,}220\) complete round-by-round sequences across five representative utility profiles and horizons \(1\) through \(7\). The script also checks all four possible single-round assignments for positive values.

These computations corroborate, but do not replace, the unbounded algebraic proof above. No computer-assisted assertion is required to establish the theorem for arbitrary real valuations or arbitrary horizons.

## Relationship to prior work

Igarashi, Lackner, Nardi, and Novaro's *Repeated Fair Allocation of Indivisible Items* (arXiv:2304.01644v1, posted 2023-04-04) defines the same unrestricted repeated-allocation model and proves universal two-round feasibility and a fixed counterexample for more than two rounds (its Corollary 14 and Proposition 12). Those statements are respected here. The present theorem instead characterizes **every** pair of strictly positive two-good preference vectors sharing a strict ranking, gives a complete ratio-dependent exact horizon and the number of successful sequences, and identifies the sharp reduced-integer-valuation horizon bound.

Caragiannis and Narang's *Repeatedly Matching Items to Agents Fairly and Efficiently* (arXiv:2207.01589) imposes a perfect matching in every round and studies other notions of efficiency and repeated EF1; it is not a covering theorem for unrestricted Pareto competitors. Gorantla, Marwaha, and Velusamy's *Fair allocation of a multiset of indivisible items* (arXiv:2202.05186) treats ordinary overall EF/EFX for item types, not this three-way conjunction with per-round EF1 and unrestricted Pareto optimality. The arithmetic rational-exchange reduction is elementary, and equivalent specialist work may exist outside the inspected sources.

## Limitations

This is an exact result only for two agents, two objective goods per period, constant additive values and a shared strict ranking. It does not assert a comparable one-dimensional cutoff for mixed goods/chores, agents with opposing rankings, more types, time-varying values, or per-round matching-constrained Pareto comparison. The threshold is an arithmetical characterization, not an asserted closed elementary formula for arbitrary real input ratios; irrational inputs may require numerical approximation with care. The enumerated tests are finite checks only. Literature searches do not establish priority against all unindexed prior work; independent external audit has not been performed.

## References

1. A. Igarashi, M. Lackner, O. Nardi, A. Novaro, *Repeated Fair Allocation of Indivisible Items*, arXiv:2304.01644v1, 2023-04-04. https://arxiv.org/abs/2304.01644 (AAAI 2024, DOI:10.1609/aaai.v38i9.28837).
2. I. Caragiannis, S. Narang, *Repeatedly Matching Items to Agents Fairly and Efficiently*, arXiv:2207.01589, 2022-07-04. https://arxiv.org/abs/2207.01589.
3. P. Gorantla, K. Marwaha, S. Velusamy, *Fair allocation of a multiset of indivisible items*, arXiv:2202.05186, 2022-02-10. https://arxiv.org/abs/2202.05186.
