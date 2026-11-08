# Sharp population and arrival thresholds for online unit-chore \(\mathrm{Prop1}\) with eligibility constraints

## Finding

**Sharp small-population and short-horizon theorem.** In irrevocable online restricted assignment of *unit-size chores*, with each arriving chore eligible for a nonempty subset of the machines and with proportional share defined by equal fractional division among its eligible machines:

Let \(h(m)\) be the smallest arrival horizon by which an adaptive adversary can force a violation of exact prefix \(\mathrm{Prop1}\), regardless of the online policy, and set \(h(m)=\infty\) if no finite such horizon exists. Then, for every integer \(m\geq1\),

\[
h(m)=\begin{cases}
\infty,&1\leq m\leq3,\\
5,&m=4,\\
3,&m\geq5.
\end{cases}
\]

For \(m\leq3\), the minimum-discrepancy online policy maintains exact eligibility-aware \(\mathrm{Prop1}\) at **every prefix of every finite sequence**, without future information. For \(m=4\), the same policy handles **every sequence of at most four chores**; an adaptive five-chore sequence defeats **every** irrevocable online policy. With \(m\geq5\), three chores suffice for an adversarial defeat, and two cannot force failure. All chores have identical unit size.

Thus four machines are the smallest population in which exact online \(\mathrm{Prop1}\) can fail in the unit-chore restricted-assignment model, and the four-machine frontier has the exceptional sharp five-arrival horizon. The positive four-arrival assertion admits complete finite verification; the unlimited three-machine guarantee and both impossibility constructions have analytic proofs.

## Assumptions and scope

Fix \(m\) labeled machines. At time \(t\), a unit-size chore \(j=t\) arrives with a revealed, nonempty eligibility set \(E_t\subseteq\{1,\ldots,m\}\). The allocator immediately and irrevocably chooses a receiver \(a_t\in E_t\); future eligibility sets are unknown. Repeated eligibility sets are allowed. The adversary may adapt each new set to prior allocations. Define, after any prefix of length \(t\),

\[
L_i(t)=\bigl|\{s\leq t:a_s=i\}\bigr|,\qquad
P_i(t)=\sum_{\substack{s\leq t\\i\in E_s}}\frac{1}{|E_s|},\qquad
d_i(t)=L_i(t)-P_i(t).
\]

Here \(P_i\) is the eligibility-aware proportional share of the chores, and \(L_i\) is the number of chores assigned to machine \(i\). Exact chore \(\mathrm{Prop1}\) means \(L_i(t)-1\leq P_i(t)\) for every \(i\) with \(L_i(t)>0\); it is automatic for empty bundles. Equivalently, since \(P_i(t)\geq0\), the condition is \(d_i(t)\leq1\) for every machine. Always \(\sum_i d_i(t)=0\).

The positive rule is **minimum discrepancy**: give each arriving chore to an eligible machine of minimum current \(d_i\), breaking ties by the lowest fixed label. The arrival contributes \(1/|E_t|\) to each eligible proportional share. Allocating to \(a_t\) changes its discrepancy by \(1-1/|E_t|\) and every other eligible machine's discrepancy by \(-1/|E_t|\). A singleton eligibility set changes no discrepancy.

## Proof

**I. At most three machines, arbitrary horizon.** A one-machine system is trivial, and any two-machine system can be embedded as a three-machine system with one permanently ineligible dummy. For three machines, all discrepancies under minimum-discrepancy assignment are integer multiples of \(1/6\). We claim the stronger invariant

\[
-\frac56\leq d_i(t)\leq\frac56\quad(i=1,2,3)
\]

at every time. It holds initially and is unchanged by singleton-eligible chores. Suppose a two-eligible chore appears, with eligible discrepancies \(u\leq v\), so the receiver moves from \(u\) to \(u+1/2\) and the other moves from \(v\) to \(v-1/2\). If \(u\geq1/2\), then \(v\geq1/2\) and the third discrepancy is at most \(-1\), contradicting the invariant. By the \(1/6\) lattice, \(u\leq1/3\), whence \(u+1/2\leq5/6\). Likewise, if \(v\leq-1/2\), the third discrepancy would be at least \(1\). Thus \(v\geq-1/3\), so \(v-1/2\geq-5/6\). The other two sides of the invariant improve automatically.

For a three-eligible chore, the selected minimum discrepancy is at most zero, so after receiving the chore it is at most \(2/3\). Were an unselected machine at discrepancy at most \(-2/3\), the selected machine would also have discrepancy at most \(-2/3\), forcing the third to have discrepancy at least \(4/3\); contradiction. Therefore every unselected discrepancy is at least \(-1/2\), and after the \(-1/3\) update it remains at least \(-5/6\). All other sides of the invariant are immediate. Induction proves the invariant, which implies \(d_i(t)<1\) and hence \(\mathrm{Prop1}\) for all prefixes.

**II. Four machines, an adaptive five-chore obstruction.** Label the machines \(A,B,C,D\). Give the first chore eligibility \(\{A,B,C,D\}\). By renaming, suppose \(A\) receives it; discrepancies are \((9,-3,-3,-3)/12\). Give the second chore eligibility \(\{B,C,D\}\). By renaming, suppose \(B\) receives it; the discrepancies become \((9,5,-7,-7)/12\). Give the third chore the same eligibility set \(\{B,C,D\}\). If \(B\) receives it, then \(d_B=13/12>1\), already violating \(\mathrm{Prop1}\). Otherwise rename the chosen agent \(C\), and the discrepancies are

\[
(d_A,d_B,d_C,d_D)=(9,1,1,-11)/12.
\]

Give the fourth chore eligibility \(\{B,C\}\), and call its chosen receiver \(X\). Now \(d_A=9/12\) and \(d_X=7/12\). Give the fifth chore eligibility \(\{A,X\}\). If \(A\) receives it, \(d_A=15/12>1\); if \(X\) receives it, \(d_X=13/12>1\). Thus no online rule can guarantee prefix \(\mathrm{Prop1}\) through five arrivals. In particular, the fourth machine cannot be dispensed with, by part I.

**III. Four machines, optimality of the five-chore horizon.** We prove that minimum-discrepancy assignment succeeds for all prefixes of up to four chores by an exhaustive *finite proof*, not by sampling. On four labeled machines there are exactly \(11\) non-singleton eligibility sets: six of size two, four of size three, and one of size four. Singletons do not affect discrepancies and are forced assignments, so deleting all singleton chores cannot affect future minimum-discrepancy choices or the \(\mathrm{Prop1}\) test. It therefore suffices to check the \(1+11+11^2+11^3+11^4=16{,}105\) possible sequences of at most four non-singleton sets.

The standalone exact-integer verifier `verify.py` enumerates every one of these sequences and updates both loads and proportional shares with denominator \(12\), which is divisible by every possible eligibility size. At each prefix it checks the defining inequality \(12(L_i-1)\leq12P_i\) whenever \(L_i>0\). All \(16{,}105\) sequences satisfy it. Separately, `verify_independent.cpp` checks the same assertion by directly enumerating *all* \(1+15+15^2+15^3+15^4=54{,}241\) sequences, including singleton sets, computing the minimum-discrepancy assignment from loads and proportional shares and rechecking fairness after every step. Both checks are exhaustive and terminate. Every possible adaptive sequence realizes one of the checked prefixes, so this is a complete four-step existence proof. This proves the four-machine threshold exactly.

**IV. Five or more machines: exactly three chores.** Send two chores each eligible for all \(m\) machines. If the allocator sends both to one machine, its discrepancy after the second chore is \(2-2/m>1\), so it has already failed. Otherwise the two recipients \(A,B\) are distinct, and each has discrepancy \(1-2/m\). Send the third chore with eligibility \(\{A,B\}\). Whichever receives it has discrepancy \(3/2-2/m>1\) for \(m\geq5\), causing failure by time three.

To see that two chores never *force* failure for any population, use minimum-discrepancy assignment for the first two arrivals. If the first is a singleton, it leaves all discrepancies at zero; the second chore gives its recipient discrepancy at most \(1-1/|E_2|\leq1\). If the first is non-singleton, its recipient has strictly positive discrepancy while all others have nonpositive discrepancies. Thus the second job is assigned to a *different* machine whenever its eligibility set has size at least two; both loads remain at most one and consequently satisfy \(\mathrm{Prop1}\). If the second eligibility set is a singleton, discrepancies are unchanged. Therefore two arrivals always admit a valid online policy. Combined with parts I–III and the three-chore adversary, this proves the complete formula for \(h(m)\).

## Verification

With Python 3.10 or later, run `python verify.py`. Expected outputs include `three invariant (91, 364)`, `four greedy prefixes 16105`, a successful minimax assertion that the four-machine game can be survived for four but not five steps, and `adversary (108, [0, 0, 0, 12, 0, 96])`. The integers \(12\) and \(96\) count, respectively, three-step failure paths and five-step failure paths within the displayed adaptive adversary.

For an independent direct implementation, run `g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_independent.cpp -o verify_cpp && ./verify_cpp`. Its successful output is `Direct all-eligibility 4-job prefixes checked: 54241; allocation transitions: 54240`. These programs use only standard-language libraries; no external data, guessed timeouts, or nondeterministic numerical tests are required. The finite verification is precisely confined to the stated four-machine, four-arrival assertion and is not used to infer the arbitrary-horizon three-machine theorem or the adversarial five-arrival obstruction.

## Relationship to prior work

Biburger, Megow and Shahkarami (arXiv:2610.08064, first posted October 6, 2026) introduce and analyze this identical-value online eligibility-constrained proportionality model; their section 3 gives asymptotically sharp \(\Theta(\sqrt m)\) deterministic approximation for chores, including an adversary using unit-size jobs. Their construction yields a lower-bound factor of order \(\sqrt m\), but its explicit four-machine instance reaches the boundary factor one and does **not** establish the strict five-arrival failure or the global exact guarantee for three machines. The present theorem addresses the unresolved *exact small-population* boundary, not a stronger asymptotic approximation rate.

Sun, Wang and Li (arXiv:2602.18098, first posted February 20, 2026) study equivalent eligibility-aware fractional shares under the term relevance constraints and establish existence and complexity results for **offline** \(\mathrm{Prop1}\) orientations. Offline existence does not imply an irrevocable online policy against an adaptive adversary. Elkind et al. (arXiv:2410.14593, first posted October 18, 2024) study temporal envy-based fairness rather than the eligibility-aware proportionality invariant proved here.

## Limitations

All chores have identical unit disutility to all eligible machines; the proof does not establish the same positive results for arbitrary chore sizes or private heterogeneous costs. The three- and five-chore obstructions are adaptive, observing recipients; the theorem does not claim the same impossibility against every oblivious fixed arrival distribution or an allocator given exact future information. Four-arrival minimality uses a small fully specified exhaustive computation rather than an independent human-only case enumeration. No approximation-ratio or computational-efficiency claim is made for higher populations, and no independent external scientific audit is asserted.

## References

1. J. Biburger, N. Megow, G. Shahkarami, *Online Fair Division under Eligibility Constraints*, arXiv:2610.08064 (first public version 2026-10-06), https://arxiv.org/abs/2610.08064.
2. A. Sun, R. Wang, B. Li, *Fair Orientations: Proportionality and Equitability*, arXiv:2602.18098 (first public version 2026-02-20), https://arxiv.org/abs/2602.18098.
3. E. Elkind, A. Lam, M. Latifian, T. Y. Neoh, N. Teh, *Temporal Fair Division of Indivisible Items*, arXiv:2410.14593 (first public version 2024-10-18), https://arxiv.org/abs/2410.14593.
