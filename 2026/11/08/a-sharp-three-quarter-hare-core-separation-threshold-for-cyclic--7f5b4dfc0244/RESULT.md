# A sharp three-quarter Hare-core separation threshold for cyclic two-approval elections

## Finding

**Theorem.** For integers \(n\ge4\) and \(1\le k\le n\), consider the approval election with voters and candidates both indexed by \(\mathbb Z/n\mathbb Z\) and the approval ballot \(A_i=\{i-1,i\}\) for each voter \(i\). A committee \(W\subseteq\mathbb Z/n\mathbb Z\) has size \(k\). Under the ordinary Hare-quota integral core, **some committee is simultaneously Pareto efficient and satisfies extended justified representation (EJR), but is blocked by a coalition**, if and only if

\[
\boxed{\left\lceil\frac{3n}{4}\right\rceil\le k\le n-4.}
\]

In particular, the smallest such cyclic two-approval electorate has \(n=16\) voters and \(k=12\) seats. Every size-\(k\) committee of this election is Pareto efficient, and EJR is equivalent to justified representation (JR). The theorem characterizes existence of an EJR-but-noncore committee, **not** the core status of every committee.

## Assumptions and scope

Each voter approves exactly two adjacent candidates and has additive approval utility \(u_i(X)=|A_i\cap X|\). There are \(n\) distinct candidates and \(n\) distinct voters; indices and predecessor/successor operations are cyclic. A size-\(k\) committee \(W\) belongs to the integral Hare core if there are no nonempty voter set \(S\) and candidate set \(T\) such that \(|S|k\ge n|T|\) and \(u_i(T)>u_i(W)\) for every \(i\in S\). The deviating set \(T\) may have a different size from \(k\). For \(\ell\ge1\), an \(\ell\)-cohesive group of voters has size at least \(\ell n/k\) and at least \(\ell\) commonly approved candidates; EJR requires at least one voter in the group to receive \(\ell\) approved committee members. JR is the \(\ell=1\) condition.

Pareto efficiency means that no other **size-\(k\)** committee weakly improves every voter's approval utility and strictly improves at least one. This is not a claim about variable-size outcomes. No stochastic preference assumptions are made.

## Proof

**1. Welfare and representation.** Every candidate appears on exactly two ballots, so for every size-\(k\) committee \(W\), \(\sum_i u_i(W)=2k\). Consequently, any strict Pareto improvement by another size-\(k\) committee is impossible: it would increase this constant sum. Two different ballots overlap in at most one candidate for \(n\ge4\). Thus a group jointly approving at least two candidates contains at most one voter, whereas every \(\ell\)-cohesive group with \(\ell\ge2\) would require at least \(2n/k\ge2\) voters. Hence EJR and JR coincide.

If \(k<n/2\), then \(n/k>2\) and even the two supporters of any candidate are too small to form a JR group, so JR holds automatically. If \(k\ge n/2\), a JR violation occurs precisely when both voters \(i,i+1\) who approve candidate \(i\) are unrepresented. These voters' approved sets together cover the three consecutive candidates \(i-1,i,i+1\), so this is equivalent to their all being absent from \(W\). Thus JR is equivalent to the absence of three consecutive unselected candidates in the cyclic binary word of \(W\). (When \(k=n\), this condition is automatic.)

**2. Blocking bound.** For any proposed candidate set \(T\), write \(I_W(T)=\{i:u_i(T)>u_i(W)\}\). If \(T\) blocks \(W\), then \(k|I_W(T)|\ge n|T|\). Indeed, any blocking coalition lies in \(I_W(T)\), and taking all improvers witnesses the converse. If \(|T|>k\), the quota would require more than \(n\) voters, which is impossible. If \(|T|=k\), the quota requires every voter to improve, which contradicts the constant welfare sum established above. Thus only proper smaller sets \(0<|T|<k\) can block.

Suppose \(W\) is JR and \(k\ge n/2\). A proper nonempty \(T\) is a disjoint union of maximal cyclic runs of consecutive chosen positions; a run of \(r\) candidates touches exactly \(r+1\) voters, and the touched-voter sets of separate runs are disjoint. A singleton run cannot improve both touched voters: doing so would require all three consecutive candidate positions centered on the singleton to be missing from \(W\), violating JR. A two-candidate run cannot improve all three touched voters: improving both endpoint voters would require four consecutive missing candidates, again violating JR. Each run of length \(r=1,2\) therefore has at most \(r\) improvers, while a run of length \(r\ge3\) has at most \(r+1\le4r/3\) improvers. Summing over runs gives the sharp uniform inequality

\[
\boxed{|I_W(T)|\le\tfrac43|T|.}
\]

Therefore, if \(k<3n/4\), then \(k|I_W(T)|\le (4k/3)|T|<n|T|\), and no JR committee is blocked. The case \(k<n/2\) also has no blocking: any candidate set \(T\) touches at most \(2|T|\) voters because each candidate has two supporters, so \(k|I_W(T)|\le2k|T|<n|T|\).

**3. Near-full committees are core.** It remains to consider \(k\ge n/2\), because all smaller \(k\) were handled in step 2. If \(n-k\le3\) and \(W\) is JR, at most one voter can be unrepresented. Indeed, an unrepresented voter requires two adjacent missing candidates. Two different such voters require either three consecutive missing candidates (for overlapping pairs, violating JR) or four distinct missing candidates, exceeding the allowed three. For any proper run of \(r\) proposed candidates, its \(r+1\) touched voters cannot all strictly improve: the two endpoint voters each receive exactly one candidate from this run, so both would have to be unrepresented under \(W\). Hence each run has at most \(r\) improvers, giving \(|I_W(T)|\le|T|\). Since \(k<n\), this rules out blocking. For \(k=n\), \(W\) is the entire candidate set and cannot be blocked. Thus every EJR committee is core if \(n-k\le3\).

**4. Sharp construction.** Assume \(\lceil3n/4\rceil\le k\le n-4\) and put \(z=n-k\ge4\). Define the missing-candidate positions by

\[
Z=\{0,1,3,4\}\,\cup\,\{7+3j:0\le j\le z-5\},\qquad W=(\mathbb Z/n\mathbb Z)\setminus Z.
\]

The second set is empty when \(z=4\). The largest added position is \(3z-8\), and \(z\le n/4\) ensures it lies strictly below \(n-1\). Thus these positions are distinct, and there are no three consecutive cyclic missing candidates. Since \(k\ge n/2\), the committee \(W\) satisfies JR and hence EJR; it is also Pareto efficient by step 1.

Choose \(T=\{1,2,3\}\). Precisely voters \(1,2,3,4\) strictly improve, with their utilities changing from \((0,1,1,0)\) under \(W\) to \((1,2,2,1)\) under \(T\). The four-voter coalition can afford the three candidates because \(4k\ge3n\). Hence \(W\) is blocked. These parameter inequalities have a solution only for \(n\ge16\), with the first solution \((n,k)=(16,12)\). All directions are proved.

## Verification

The self-contained file `verify_cycle.py` implements exact integer bit-mask approval utilities, core-block tests, the representation criterion and the constructive witness. Executing `python3 verify_cycle.py` in the same directory produced:

```
exhaustive committees n=4..10: 2025
sharp witness n=16,k=12: 4 voters improve via 3 candidates
all constructive parameter pairs n=16..99: 924
random 4/3-bound checks: 733
PASS
```

For \(4\le n\le10\), every candidate committee was enumerated and every alternative smaller coalition proposal was checked for JR committees. This checks the necessity statements in those sizes, not the infinite claim. The complete proof is given above; finite tests are independent corroboration of definitions, edge cases and the construction.

## Relationship to prior work

Becker, Greger and Peters (2026) prove the existence of an integral Hare-core committee (in fact core+) for every approval election and provide an algorithm. Their universal existential result neither says **all** EJR committees are core nor determines when a Pareto-efficient EJR committee can fail core on this particular sparse cycle. The present result determines a sharp phase diagram for **existence of such a failure**, without contradicting general core existence. Pierczyński and Skowron (2022) study core-stable committee existence on restricted preference domains; domain-specific existence is logically distinct from this complete EJR-versus-core separation threshold. Aziz et al. introduce and compare JR and EJR, which are weaker than core in general; the new result makes their gap quantitative on this exact two-approval cyclic family.

## Limitations

The theorem covers only the specified cyclic two-approval ballot profile, Hare-quota integral deviations, and additive approval utilities. It does not establish uniqueness of any committee, characterize *all* core committees, cover arbitrary degree-two approval graphs, establish a general minimal counterexample over all election profiles, or assert an impossibility of finding a core committee (a core committee always exists). The finite verifier is not an infinite proof. Originality is assessed against accessible literature and indexed records; unindexed equivalent results and stronger theorems remain possible. Independent audit has not been performed.

## References

- P. Becker, M. Greger, D. Peters, “Existence of the Core in Approval-Based Committee Elections,” arXiv:2609.11912 (first publicly posted September 10, 2026). https://arxiv.org/abs/2609.11912
- G. Pierczyński and P. Skowron, “Core-Stable Committees under Restricted Domains,” arXiv:2108.01987 (WINE 2022). https://arxiv.org/abs/2108.01987
- H. Aziz, M. Brill, V. Conitzer, E. Elkind, R. Freeman, T. Walsh, “Justified Representation in Approval-Based Committee Voting,” arXiv:1407.8269. https://arxiv.org/abs/1407.8269
