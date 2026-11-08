# An exact two-ballot characterization of full justified representation plus

## Finding

Let an approval-based committee election have precisely two distinct ballot types \(A,B\subseteq C\), each occurring a positive number \(a,b\) of times. Set \(n=a+b\) and let \(W\subseteq C\) have size \(k\), where \(1\le k\le |C|\). Write \(u_A=|A\cap W|\), \(u_B=|B\cap W|\), and \(r=|A\cap B\cap W|\). For \(s\in\{A,B\}\) and each integer \(1\le\ell\le k\), say that type \(s\) is *eligible-deficient* at level \(\ell\) if \(u_s<\ell\) and \(s\setminus W\ne\varnothing\).

**Exact criterion.** The committee violates full justified representation plus (FJR+) if and only if for some \(\ell\in\{1,\ldots,k\}\) at least one of the following occurs:

1. Type \(A\) is eligible-deficient and \(ak\ge\ell n\).
2. Type \(B\) is eligible-deficient and \(bk\ge\ell n\).
3. Both types are eligible-deficient and an unelected candidate belongs to \(A\cap B\).
4. Both types are eligible-deficient, no unelected candidate belongs to \(A\cap B\), and \(2\ell-r\le k\).

Thus FJR+ can be checked on this domain using only ballot-type sizes, elected utilities, common winners, and the presence of unelected approved candidates, without solving a linear program.

**Collapse on supported committees.** If every winner is approved by at least one voter (\(W\subseteq A\cup B\)), then FJR+ and EJR+ are equivalent. The same equivalence holds for every Pareto-optimal committee, with no support assumption. The support qualification cannot be dropped for arbitrary committees: there is a two-ballot election whose committee satisfies both FJR and EJR+ but violates FJR+ (explicitly given below).

## Assumptions and scope

Voters use binary additive committee utility \(u_i(X)=|A_i\cap X|\). Candidates may have zero supporters; the election may contain unelected candidates approved by one or both types. Ties and empty ballots are permitted in the general criterion, provided \(A\ne B\) and \(a,b\ge1\). We use the integral Hare quota \(h=n/k\). FJR+ is exactly Definition 3.2 of Teh (2026), with nonnegative weights \(z_i,x_{ic},y_c\): at an integer level \(\ell\), only voters receiving fewer than \(\ell\) approved winners may have positive \(z_i\); \(x_{ic}=0\) for unapproved candidates; \(\sum_c x_{ic}=\ell z_i\), \(x_{ic}\le y_c\), \(x_{iw}\le z_i\) for elected \(w\in W\), and \(Z=\sum_i z_i>0\), \(Z\ge hY\) for \(Y=\sum_c y_c\).

EJR+ forbids an unelected candidate \(c\) and an integer level \(\ell\) at which at least \(\ell h\) of its approvers have utility below \(\ell\). FJR forbids a group \(S\) and set \(T\) with \(|S|\ge h|T|\), every member approving at least \(\ell\) candidates in \(T\), and every member obtaining fewer than \(\ell\) winners.

## Proof

**1. Eligible types.** If a type has \(u_s<\ell\) but approves no unelected candidate, then any positive-weight voter of that type would have \(\sum_c x_{ic}=\ell z_i\), while every approved candidate is elected and satisfies \(x_{ic}\le z_i\). Hence \(\sum_c x_{ic}\le u_s z_i<\ell z_i\), a contradiction. Conversely, an eligible-deficient type can participate alone: assign all its required \(\ell z_i\) to one unelected approved candidate and set that candidate's \(y_c=\ell z_i\). Averaging an arbitrary fractional witness over the identical voters of each ballot type preserves all inequalities and total \(Z\), so we may write a common nonnegative voter weight \(s\) for type \(A\) and \(t\) for type \(B\).

**2. Only one participating type.** If only type \(A\) participates, \(Y\ge\ell s\) because \(\sum_c x_{ic}=\ell s\le\sum_c y_c\). Therefore \(Z/Y\le a/\ell\), with equality attained by assigning \(\ell s\) to an unelected approved candidate. The analogous maximum for type \(B\) is \(b/\ell\). Comparing to \(h=n/k\) yields exactly tests 1 and 2.

**3. Both participating types, with an unelected common candidate.** If \(c\in(A\cap B)\setminus W\), every voter is below level \(\ell\) and approves \(c\). Assign \(z_i=1\), \(x_{ic}=\ell\), and \(y_c=\ell\) to obtain \(Z=n\), \(Y=\ell\). Since \(\ell\le k\), the inequality \(Z\ge hY\) holds. This is also an EJR+ violation, giving test 3.

**4. Both participating types, without an unelected common candidate.** The only candidates usable by both types are the \(r\) elected common candidates. For each such candidate \(c\), the cost \(y_c\) can save at most \(\min(x_{Ac},x_{Bc})\) relative to paying separately for both types; elected-candidate bounds give \(\min(x_{Ac},x_{Bc})\le\min(s,t)\). For every candidate used by just one type, \(y_c\) pays its entire assigned amount. Summing over candidates yields

\[
Y\ge \ell(s+t)-r\min(s,t).
\]

This bound is attained for each of the three ratios \((s,t)=(1,0),(0,1),(1,1)\): the first two use one eligible type's unelected candidate; for \((1,1)\), assign one unit to each of the \(r\) common elected candidates for both types and all remaining \(\ell-r\) units per type to any unelected private candidate of that type. Such candidates exist because both types are eligible-deficient and no common unelected candidate exists; also \(r<\ell\). The corresponding \(Z/Y\) ratios are

\[
\frac a\ell,\qquad \frac b\ell,\qquad \frac{a+b}{2\ell-r}.
\]

For general \(s,t\ge0\), the upper bound \((as+bt)/(\ell(s+t)-r\min(s,t))\) is fractional-linear on each of the intervals \(s\le t\) and \(s\ge t\) (after scaling). Its maximum is attained at one of the three ratios above. Hence a violation occurs precisely when one of tests 1, 2, or 4 holds, since \(a+b=n\) and \(n/(2\ell-r)\ge n/k\) exactly when \(2\ell-r\le k\). This proves the criterion.

**5. Supported and Pareto-optimal committees.** Suppose \(W\subseteq A\cup B\). Let \(p=|W\cap(A\setminus B)|\) and \(q=|W\cap(B\setminus A)|\), so \(k=p+q+r\), \(u_A=p+r\), and \(u_B=q+r\). When both are deficient at level \(\ell\), we have \(\ell>p+r\) and \(\ell>q+r\), whence \(2\ell-r>p+q+r=k\). Test 4 is impossible. Tests 1 and 2 are exactly single-type EJR+ violations, and test 3 is a common-candidate EJR+ violation. All EJR+ violations are FJR+ violations by the source definition, proving equivalence. Finally, if a Pareto-optimal committee contains an unsupported winner, every supported candidate must already be elected: otherwise swapping that winner with an unelected supported candidate weakly increases every voter's utility and strictly increases at least one. In that case there are no eligible-deficient types at any level, and both FJR+ and EJR+ hold. This proves the Pareto-optimal version.

**6. Why support is relevant.** Let there be five voters with ballot types \(A=\{c_1,c_2,a\}\) (two voters) and \(B=\{c_1,c_2,b_1,b_2\}\) (three voters). Add three candidates \(d_1,d_2,d_3\) approved by no one. Set \(k=6\) and \(W=\{c_1,c_2,b_1,d_1,d_2,d_3\}\). The type utilities are \(2\) and \(3\), and \(h=5/6\). EJR+ holds: the only unelected approved candidates are \(a\) and \(b_2\); their two and three deprived approvers are below their first applicable thresholds \(3h=5/2\) and \(4h=10/3\), respectively. FJR holds: the only possibly deficient groups are type \(A\) at levels at least three and type \(B\) at levels at least four; at the only feasible such levels, their maximum sizes \(2\) and \(3\) are below \(3h=5/2\) and \(4h=10/3\), and neither type can justify any higher level with its distinct approved candidates. Yet FJR+ fails at level four: put weight one on every voter; each voter uses one unit of each \(c_1,c_2\), and the remaining two units from \(a\) for type \(A\) or \(b_2\) for type \(B\). Set \(y_{c_1}=y_{c_2}=1\), \(y_a=y_{b_2}=2\), and other \(y\)'s to zero. Then \(Z=5=hY\) with \(Y=6\), so this is a valid fractional violation. The supported-winner condition therefore cannot simply be omitted.

## Verification

Run `python verify.py` with Python 3 and SciPy installed as specified in `requirements.txt`. The checker constructs the exact source linear-program constraints independently of the closed-form criterion, compares the two on a deterministic collection of small complete and random two-ballot elections, and checks EJR+, FJR and the explicit strictness example. Computational samples test implementations and boundary handling, not the universal proof. The mathematical proof above establishes the unbounded statement.

## Relationship to prior work

Teh, *Strengthening Full Justified Representation: Efficient Verification and Computation*, arXiv:2608.11500v1 (August 11, 2026), introduces FJR+ as a fractional linear-programming strengthening of FJR and EJR+, proves that FJR+ is strictly stronger than their conjunction on unrestricted elections, and proves equivalence with lower quota on disjoint party-list profiles. The present finding instead completely eliminates the linear program for **two potentially overlapping ballot types**, identifies when FJR+ collapses to EJR+ on supported or Pareto-optimal committees, and provides a two-type unsupported-winner separation. Teh's strictness example has more than two ballot types; his party-list equivalence concerns disjoint types and a different comparison axiom.

Dong and Peters, *An Axiomatic Analysis of Proportionality Notions in Approval-Based Multiwinner Voting*, arXiv:2605.04612v1 (May 6, 2026), gives axiomatic characterizations of EJR+ and PJR+, and treats FJR separately; it does not state the fractional two-type characterization here. A related two-type JUQ/JNQ/EJR+ existence construction is not a characterization of FJR+ and does not imply the present exact tests. Literature/database searches do not certify worldwide uniqueness; an equivalent theorem in unindexed work remains possible.

## Limitations

The equivalence is restricted to at most two ballot types; three or more distinct types are not covered. The exact criterion allows unsupported elected candidates, but the clean collapse requires every winner to have positive approval support or the committee to be Pareto-optimal. It uses the integral, unweighted, Hare-quota committee FJR+ definition of Teh and does not assert analogous conclusions for Droop-FJR+, weighted agents, participatory budgeting with unequal project costs, temporal voting, or fractional outcome committees. No independent mathematical audit is claimed.

## References

- N. Teh, *Strengthening Full Justified Representation: Efficient Verification and Computation*, arXiv:2608.11500v1, first submitted August 11, 2026. https://arxiv.org/html/2608.11500v1
- C. Dong and J. Peters, *An Axiomatic Analysis of Proportionality Notions in Approval-Based Multiwinner Voting*, arXiv:2605.04612v1, first submitted May 6, 2026. https://arxiv.org/html/2605.04612v1
- D. Avramidis, M. de Berg, and U. Schmidt-Kraepelin, *Best-of-Both Worlds Proportionality in Structured Committee Elections*, arXiv:2610.28151v1, first submitted October 20, 2026; a related but distinct ex-ante/ex-post framework. https://arxiv.org/abs/2610.28151
