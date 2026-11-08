# The sharp seven-voter Kelly no-show boundary for four-candidate sequential PAV

## Finding

For three-seat sequential proportional approval voting (seqPAV) on four labeled candidates with nonempty approval ballots and all possible greedy tie branches, a strict Kelly no-show paradox first occurs with **seven voters**. There are exactly **12** anomalous anonymous, candidate-labeled seven-voter profiles out of \(\binom{21}{14}=116280\); they form one orbit under candidate relabeling. Every anomalous profile has two profitable abstention ballot types, each appearing twice, hence four individually identifiable voters who can profitably abstain.

Up to renaming the four candidates \(a,b,c,d\), the sole profile is
\[
2\{a,b\}+2\{a,c\}+\{b,d\}+\{c,d\}+\{b,c,d\}.
\]
Its full-electorate winning-committee set is
\[
\bigl\{\{a,b,c\},\{a,b,d\},\{a,c,d\}\bigr\},
\]
whereas deleting any single voter of type \(\{a,b\}\) or \(\{a,c\}\) leaves the singleton set \(\bigl\{\{a,b,c\}\bigr\}\). Either abstainer's approved-candidate counts across full-electorate committees are \(2,2,1\), compared with \(2\) after abstention. This is a **strict Kelly comparison of set-valued rules**, and does **not** assert a paradox for every fixed deterministic tie-breaker.

## Assumptions and scope

The candidate set is \(C=\{a,b,c,d\}\), and the committee size is \(k=3\). Each of \(n\ge1\) voters approves a nonempty subset of \(C\). A profile is anonymous when only the multiplicities \(n_B\) of the 15 nonempty ballot types \(B\subseteq C\) matter; candidate names remain distinct. Sequential PAV starts with \(S=\varnothing\) and chooses, at each of three steps, any unelected candidate maximizing the exact marginal score
\[
G(c\mid S)=\sum_{\substack{B\subseteq C,\ B\ne\varnothing\\ c\in B}}\frac{n_B}{1+|B\cap S|}.
\]
All branches at all score ties are retained; \(F(A)\) denotes the nonempty set of three-seat committees reached.

For a voter with ballot \(B\), committee utility is \(u_B(W)=|B\cap W|\). The abstention set \(F(A-B)\) is strictly Kelly-preferred to \(F(A)\) exactly if
\[
\min_{U\in F(A-B)}u_B(U)\ \ge\ \max_{W\in F(A)}u_B(W)
\quad\text{and}\quad
\max_{U\in F(A-B)}u_B(U)\ >\ \min_{W\in F(A)}u_B(W).
\]
The subtraction \(A-B\) removes one voter with ballot \(B\), not all voters of that type. This finite-boundary theorem concerns \(1\le n\le7\), not arbitrary electorate size, candidate count, or committee size.

## Proof

**Exact exhaustive recurrence.** Encode a committee \(S\subseteq C\) as a four-bit mask and every nonempty ballot type as one of the 15 nonzero masks. For a multiplicity vector \(\boldsymbol n\in\mathbb Z_{\ge0}^{15}\), let \(\mathcal S_0=\{0\}\) and, successively for \(t=0,1,2\), set
\[
\mathcal S_{t+1}=\bigcup_{S\in\mathcal S_t}\left\{S\cup\{c\}:c\notin S,\ G(c\mid S)=\max_{d\notin S}G(d\mid S)\right\}.
\]
This recurrence exhausts every possible tie-breaking path by induction on \(t\), so \(F(A)=\mathcal S_3\) is exact. Since \(|S|\le2\) at each marginal-score comparison, the possible denominators are \(1,2,3\). Multiplication by six yields integer comparisons with no rounding. Hence all decisions in the verifier are exact.

For each electorate size \(n\), the nonnegative integer vectors with \(\sum_Bn_B=n\) are enumerated without omission by combinations with replacement over the 15 ballot masks. Their count is \(\binom{n+14}{14}\). Every labeled-voter profile maps to one such vector, and both greedy scores and the Kelly abstention test depend only on that vector and on which ballot type loses one copy; consequently no potential abstention event is lost by anonymization. Each positive-coordinate deletion is checked with the same exact recurrence and the two extremal inequalities above.

Running the complete embedded program `verify.py` gives the following exhaustive count:

| Voters \(n\) | Anonymous candidate-labeled profiles | Profiles containing a strict Kelly no-show event |
|---|---:|---:|
| 1 | 15 | 0 |
| 2 | 120 | 0 |
| 3 | 680 | 0 |
| 4 | 3060 | 0 |
| 5 | 11628 | 0 |
| 6 | 38760 | 0 |
| 7 | 116280 | 12 |

The program verifies that these 12 profiles are exactly the orbit of the displayed representative under all 24 candidate permutations; orbit cardinality is 12. It checks every reported profitable type and multiplicity, as well as the winning committees before and after deletion. The orbit equality proves both completeness and uniqueness up to relabeling.

**Independent explicit witness calculation.** In the seven-voter representative, the initial greedy scores for \((a,b,c,d)\) are \((4,4,4,3)\). Starting with \(a\), the second-step scores for \((b,c,d)\) are \((3,3,3)\). Starting with \(b\) or \(c\), the opposite candidate among \(b,c\) is the unique best second choice, with score \(7/2\). The final choices produce exactly \(\{a,b,c\},\{a,b,d\},\{a,c,d\}\). After removing one \(\{a,b\}\) voter, the initial scores become \((3,3,4,3)\), so \(c\) is uniquely first; then \(b\) is uniquely next with score \(5/2\), and \(a\) uniquely finishes with marginal score \(3/2>4/3\). The case of removing \(\{a,c\}\) is symmetric. Strict Kelly preference follows from the respective approved-seat counts \(\{1,2,2\}\) versus \(\{2\}\).

## Verification

From a clean invocation `python3 verify.py` (Python standard library only), the submitted code exhausts **170543** anonymous profiles at sizes one through seven and **813960** distinct present-ballot deletion comparisons. It compares its integer-based winners with a separately coded direct `fractions.Fraction` tie-branch recursion in **5075** checks, including every profile through four voters, a deterministic sample of seven-voter profiles, and all paradox outcomes and witnessing deletions. The finite proof relies on completeness of the exact recurrence and enumeration; the rational cross-check is independent corroboration, not a replacement for exhaustive coverage. The program terminates with `PASS` and supplies the reproducibility assertions.

## Relationship to prior work

Bullinger, Dong, Lederer and Mehler established that seqPAV and nearly all sequential Thiele rules can violate participation, and that sequential Thiele rules satisfy participation for committee sizes at most two. Their work supplies the exact Kelly set-preference convention used here. The added statement is the **sharp electorate-size threshold** and **complete 12-profile orbit census** in the first nontrivial fixed four-candidate, three-seat cell, not general impossibility. Sánchez-Fernández and Fisteus studied support monotonicity with population increase, a related but different axiom, with examples on larger committees; Lackner and Skowron discuss a related sequential-rule monotonicity failure. These sources do not furnish the exact seven-voter Kelly census in the inspected materials.

## Limitations

The result is a finite, machine-assisted exhaustive classification rather than a closed-form infinite-family theorem. All approval ballots must be nonempty; abstention is unilateral, and all greedy ties are kept. The failure exploits a genuine tie in the participating election; it is **not** a tie-breaking-independent failure. No conclusion is asserted for fixed tie-breaking conventions, different committee rules, more candidates, or larger electorates. Published or unindexed equivalent results outside the inspected sources may exist; independent validation and publication-priority certification have not been performed.

## References

1. M. Bullinger, C. Dong, P. Lederer and C. Mehler, *Participation Incentives in Approval-Based Committee Elections*, arXiv:2312.08798v1 (December 14, 2023), especially §§2.2 and 3.1, Theorem 2 and Remark 1; DOI: 10.1609/aaai.v38i9.28810 (2024).
2. L. Sánchez-Fernández and J. A. Fisteus, *Monotonicity Axioms in Approval-Based Multi-Winner Voting Rules*, arXiv:1710.04246v1 (2017); subsequent 2019 publication.
3. M. Lackner and P. Skowron, *Multi-Winner Voting with Approval Preferences*, Springer (2023), Appendix, Proposition A.3; DOI: 10.1007/978-3-031-09016-5.
