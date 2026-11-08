# Two-ballot EJR+ and fractional core+ coincide on the Pareto frontier

## Finding

**Theorem.** Let a finite approval election have two distinct voter approval sets \(A,B\), occurring \(a,b\ge 1\) times, and \(1\le k\le |C|\) seats. Every candidate has at least one supporter. Set \(q=(a+b)/k\). Let \(W\subseteq C\) be an *integral Pareto-efficient* size-\(k\) committee, and put \(u_A=|A\cap W|\), \(u_B=|B\cap W|\). Then the following are equivalent:

1. \(W\) satisfies the Hare-quota fractional **core+**, as defined via fractional blocking in Becker--Greger--Peters (2026).
2. \(W\) satisfies extended justified representation plus (**EJR+**).
3. For each type \(i\in\{A,B\}\) with at least one approved **unelected** candidate, \(n_i<(u_i+1)q\), where \(n_A=a\), \(n_B=b\).

Furthermore, the core+ certificate can be chosen *type-symmetric* and *constant within each of the three nonempty support classes* (approved only by \(A\), only by \(B\), or by both). This yields a direct rational payment construction, without solving a general linear program.

The Pareto requirement is essential even for two voters: with two shared candidates \(s_1,s_2\), two candidates \(t_1,t_2\) approved only by the second voter, \(k=3\), and \(W=\{s_1,t_1,t_2\}\), EJR+ holds but core+ fails.

## Assumptions and scope

Approval utility is the count of approved elected candidates, with no weights on candidates. Type populations are positive integers, all candidates have positive support, committees have exactly \(k\) seats, and the quota is the Hare quota \(q=(a+b)/k\). Pareto efficiency means that no other size-\(k\) committee weakly improves both types and strictly improves at least one. The result has unbounded populations, seat counts, and candidate counts, but **only two approval types**.

For a committee \(W\), a core+ certificate consists of nonnegative payments \(p_{ic}\) from voter \(i\) to approved winners and reserves \(r_i\), such that
\[
r_i+\sum_{c\in A_i\cap W}p_{ic}=1,\qquad 0\le p_{ic}\le r_i,\qquad \sum_{i:c\in A_i}p_{ic}\le q\quad(c\in W),
\]
and for every losing candidate \(d\notin W\),
\[
\sum_{i:d\in A_i}r_i<q.
\]
By the payment-system equivalence of Becker--Greger--Peters (2026, Theorem 3.2 in arXiv v2), this is equivalent to their fractional core+ definition. EJR+ means: for every losing candidate \(d\), every \(\ell\in\{1,\ldots,k\}\), and every group of at least \(\ell q\) supporters of \(d\), some member of the group approves at least \(\ell\) winners.

## Proof

**1. Pareto saturation of shared candidates.** Partition the candidates into the shared class \(A\cap B\), the \(A\)-only class, and the \(B\)-only class. Write \(h,y,z\) for their elected counts, so \(h+y+z=k\). If an unelected shared candidate existed while a private candidate were elected, replacing that private candidate by the shared candidate would preserve one type's utility and strictly increase the other's. Hence Pareto efficiency requires \(h=\min\{k,|A\cap B|\}\).

**2. The all-shared case.** If \(h=k\), every voter approves all winners. Give each voter reserve \(1/(k+1)\) and payment \(1/(k+1)\) to each winner. A winner collects \((a+b)/(k+1)<q\), and every losing candidate's supporters hold total reserves at most the same quantity. This is a core+ certificate. EJR+ also holds because every voter approves \(k\) winners; condition 3 is vacuous or automatic.

**3. EJR+ and necessary reserve inequalities.** Suppose \(h=|A\cap B|<k\). There are no losing shared candidates. A losing \(A\)-only candidate has exactly \(a\) supporters, all with \(u_A=h+y\) elected approvals. The EJR+ condition for this candidate is equivalent to \(a<(u_A+1)q\): if the inequality fails, choose \(\ell=u_A+1\), and if it holds, every larger \(\ell\) requires more than \(a\) supporters, while smaller \(\ell\) is already met. The analogous condition holds for \(B\).

For any core+ certificate, every voter of type \(i\) has at most \(u_i\) winner payments, each bounded by the reserve. Thus \(1\le(u_i+1)r_i\), even without assuming type-symmetric payments. For a losing type-private candidate, summing the reserves of its supporters yields \(n_i/(u_i+1)\le\sum r_i<q\). Therefore core+ implies condition 3.

**4. Type-symmetric certificate: the limiting budgets.** Assume the strict inequalities in condition 3. For each type \(i\), let \(y_i\) denote the number of selected private candidates, \(n_i\) its population, and \(L_i\) the assertion that a type-private unelected candidate exists. Set a provisional per-voter reserve
\[
\rho_i^*=\begin{cases}
\min\{1,q/n_i\},&L_i,\\
1,&\text{otherwise}.
\end{cases}
\]
If \(n_i<q\) or \(L_i\) is false, that type can retain its full budget with no payments. Otherwise \(n_i\rho_i^*=q\). Its aggregate payment requirement is \(P_i^*=n_i(1-\rho_i^*)\). A private winner can collect up to \(\min\{n_i\rho_i^*,q\}\). Pay as much as possible, up to \(P_i^*\), through its \(y_i\) private winners. The remaining demand for the \(h\) common winners is
\[
D_i^*=\begin{cases}
\max\{0,n_i-(y_i+1)q\},&L_i\text{ and }n_i\ge q,\\
0,&\text{otherwise}.
\end{cases}
\]
If \(D_i^*>0\), condition 3 says \(n_i<(h+y_i+1)q\), hence \(D_i^*<hq=h n_i\rho_i^*\). In particular when \(h=0\), both residual demands vanish *with strict slack*. When \(h>0\), the total demand is strictly below the common-seat capacity \(hq\): if only one \(D_i^*\) is positive this follows from the previous inequality; if both are positive, then
\[
D_A^*+D_B^*=(a+b)-(y+z+2)q=(h-2)q<hq.
\]

**5. Strictification and allocation of payments.** For a type with \(L_i\) and \(n_i\ge q\), replace \(\rho_i^*\) by \(\rho_i=\rho_i^*-\varepsilon_i\), with a sufficiently small positive rational \(\varepsilon_i\); for the other types keep \(\rho_i=1\). The strict inequalities above remain true by continuity, and each losing private candidate's reserves satisfy \(n_i\rho_i<q\). For each type, set \(P_i=n_i(1-\rho_i)\), private-seat capacity \(c_i=\min\{n_i\rho_i,q\}\), private aggregate payment \(E_i=\min\{P_i,y_i c_i\}\), and common aggregate demand \(D_i=P_i-E_i\). Distribute \(E_i\) equally among its \(y_i\) private winners and among its \(n_i\) voters; distribute \(D_i\) equally among the \(h\) shared winners and those voters (zero allocations when a class is absent). The maintained inequalities \(D_i\le h n_i\rho_i\) and \(D_A+D_B\le hq\) ensure the per-voter reserve bounds and shared-seat quota; the definition of \(E_i\) ensures the private-seat quota. Each voter pays exactly \(1-\rho_i\). Thus all core+ payment conditions hold, proving condition 3 implies core+.

**6. Necessity of the Pareto hypothesis.** For the stated two-voter example, the quota is \(q=2/3\). The losing shared candidate \(s_2\) has both voters as supporters. The selected committee yields utilities \((1,3)\), so EJR+ holds at levels \(1,2,3\). However every core+ certificate would require reserves at least \(1/2\) and \(1/4\), respectively. Their sum \(3/4>2/3=q\) violates the strict reserve bound for \(s_2\). Replacing \(t_1\) by \(s_2\) Pareto-improves the committee. This completes the proof. \(\square\)

## Verification

Run `python3 coreplus_check.py` with the standard Python library. It checks \(80{,}000\) finite, Pareto-saturated aggregate instances covering populations \(1\) through \(8\) per type, each of the three approval-class inventories \(0\) through \(4\), all feasible committee sizes and selected private counts. Of those, \(70{,}370\) satisfy the two inequalities and receive exact rational type-symmetric payment certificates; \(9{,}630\) fail a necessary reserve lower bound. The verifier checks the budget equalities, each payment bound, winner quotas, and strict losing-candidate reserve bounds using rational arithmetic. The universal assertion is proved above, **not** by finite enumeration.

## Relationship to prior work

Becker, Greger, and Peters (2026, arXiv:2609.11912, first public September 10) introduce fractional core+ and its exact payment certificate (Theorem 3.2 in v2), and prove unrestricted existence using harmonic entropy. Their general existence result does not imply that every Pareto-efficient EJR+ committee satisfies core+. Dong and Peters (2026, arXiv:2605.04612) give the general EJR+ definition and axiomatic characterizations, not this equivalence with core+. Becker, Greger, and Peters (2026, arXiv:2605.06194) prove core existence for up to seven voter types via fractional rounding, rather than classifying all Pareto-efficient two-type committees for the stricter core+. The contribution here is the precise *committee-by-committee* equivalence and an explicit type-constant certificate, together with a two-voter boundary example showing that Pareto efficiency cannot be omitted.

## Limitations

The result is specific to at most two approval types and the Hare quota. It assumes complete size-\(k\) committees and positively supported candidates. It does not assert an equivalence on arbitrary non-Pareto committees, for three or more approval types, for weighted candidate utilities, or at the Droop quota. The result has not undergone independent external mathematical validation. Literature indexing or previously unnoticed equivalent formulations may affect the novelty assessment.

## References

1. P. Becker, M. Greger, D. Peters, *Existence of the Core in Approval-Based Committee Elections*, arXiv:2609.11912, first public September 10, 2026 (v1); payment characterization checked in v2 of November 3, Theorem 3.2. https://arxiv.org/abs/2609.11912
2. C. Dong, J. Peters, *An Axiomatic Analysis of Proportionality Notions in Approval-Based Multiwinner Voting*, arXiv:2605.04612v1, May 6, 2026, Section 2. https://arxiv.org/abs/2605.04612
3. P. Becker, M. Greger, D. Peters, *Core Existence in Approval-Based Committee Elections with up to Seven Voter Types*, arXiv:2605.06194v2, August 17, 2026, Sections 2 and 6. https://arxiv.org/abs/2605.06194
