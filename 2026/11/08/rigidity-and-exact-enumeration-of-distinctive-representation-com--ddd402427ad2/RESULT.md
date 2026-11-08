# Rigidity and exact enumeration of distinctive-representation committees under laminar voter supports

## Finding

Let an approval election have \(n\ge1\) labeled voters, \(m\ge k\ge1\) labeled candidates, and approval supporter sets \(S_c\subseteq N\). Suppose the **supporter-set family is laminar**: for every two candidates \(c,d\), the sets \(S_c,S_d\) are disjoint or one contains the other. Repeated identical supporter sets are allowed. Put \(q=\lceil n/k\rceil\), and let \(B_1,\ldots,B_r\) be the distinct supporter sets of size exactly \(q\). Write \(w_i\) for the number of labeled candidates supported by precisely \(B_i\), let \(M=\sum_{i=1}^r w_i\), and put \(U=\bigcup_{i=1}^r B_i\).

A committee has **distinctive representation (DR)** when it contains exactly \(k\) candidates, every selected candidate is supported by exactly \(q\) voters, and the committee satisfies justified representation (JR): every group of at least \(n/k\) voters jointly approving a candidate has a voter who approves a selected candidate.

**Complete classification.** A DR committee exists if and only if

\[
M\ge k\quad\text{and}\quad |S_c\setminus U|<q\ \text{for every candidate }c.
\]

When these conditions hold, a size-\(k\) committee has DR **if and only if** it selects at least one candidate from each of the \(r\) multiplicity classes \(B_i\), and selects no other candidates. Every DR committee therefore represents **exactly the same voters**, namely \(U\). The exact number of labeled DR committees is

\[
\boxed{D_k=[z^k]\prod_{i=1}^r\bigl((1+z)^{w_i}-1\bigr)}.
\]

If either condition fails, \(D_k=0\). Hence DR existence, one witness, the represented voter set, and the exact count are computable in polynomial time on this domain; integer-polynomial multiplication truncated to degree \(k\) suffices.

**Lottery consequence and boundary.** For \(k\ge1\), take \(n=2k\) voters split into \(k\) disjoint pairs and exactly two separately labeled candidates approved by each pair. Every support set is laminar and quota-sized. Exactly \(2^k\) of the \(\binom{2k}{k}\) size-\(k\) committees satisfy DR, so uniform committee sampling succeeds with probability

\[
\frac{2^k}{\binom{2k}{k}}\sim \frac{\sqrt{\pi k}}{2^k}.
\]

Thus certain hierarchically structured elections have many available DR committees but an exponentially vanishing share among randomly sampled committees. The coverage-rigidity conclusion relies on laminarity: with \(n=4\), \(k=2\), and three candidates supported respectively by \(\{1,2\}\), \(\{2,3\}\), \(\{3,4\}\), both committees consisting of the first two and of the first and third candidates satisfy DR, but they cover different voter sets.

## Assumptions and scope

The supporter set \(S_c\) is \(\{v:c\text{ is approved by }v\}\). Empty sets and candidates with identical supporter sets are permitted; candidates remain labeled and distinct. A voter may approve no candidate. The laminar condition is a restriction on the **candidate supporter sets**, and should not be confused with the distinct recursive notion of *laminar proportionality* used for some approval election rules. There is no restriction that \(k\le n\); the quota is always \(\lceil n/k\rceil\), which equals one when \(k\ge n\). All conditions and formulas include boundary cases \(r=0\), \(q=1\), and \(m=k\).

## Proof

**Step 1: A JR residual criterion.** Fix any committee \(W\), and let \(R(W)=\bigcup_{d\in W}S_d\) be its represented voters. A cohesive group violating JR exists exactly when some candidate \(c\) has at least \(\lceil n/k\rceil=q\) supporters outside \(R(W)\). Indeed, those unrepresented supporters form a jointly approving group of the requisite size; conversely every JR-violating group consists of at least \(q\) such supporters for one jointly approved candidate. Therefore

\[
W\text{ satisfies JR}\iff |S_c\setminus R(W)|<q\quad\text{for all }c\in C.
\]

**Step 2: Disjoint quota blocks and mandatory representation.** Each two distinct \(B_i,B_j\) have the same cardinality \(q\). By laminarity, they must be disjoint; equality was already merged into one class. Consequently \(rq\le n\), and since \(q=\lceil n/k\rceil\), we have \(r\le\lfloor n/q\rfloor\le k\). Any DR committee uses only quota-sized supporter sets. If it omits all candidates supported by some \(B_i\), then none of its selected supporters intersects \(B_i\), because all other distinct quota blocks are disjoint. Thus all \(q\) voters of \(B_i\) remain unrepresented, contradicting the residual JR criterion for any candidate supported by \(B_i\). Every DR committee therefore selects at least one candidate from each \(B_i\).

**Step 3: Exact coverage and existence.** Conversely, selecting one or more labeled candidates from each \(B_i\), and no other candidate, represents precisely \(U\). By Step 1, such a committee satisfies JR exactly when \(|S_c\setminus U|<q\) for all candidates. If \(M\ge k\), then, because \(r\le k\), one can take one candidate from each quota block and fill the remaining \(k-r\) positions from the other \(M-r\) quota-sized candidates, giving a size-\(k\) committee. If \(M<k\), any size-\(k\) committee must include a non-quota-sized candidate, violating DR. This proves both necessity and sufficiency and the invariant represented set.

**Step 4: Exact count and algorithm.** For class \(i\), choosing a nonempty subset of its \(w_i\) labeled candidates has ordinary generating polynomial \((1+z)^{w_i}-1\), where degree counts selected candidates. Choices across disjoint classes are independent, so the degree-\(k\) coefficient of their product counts exactly the DR committees. Compute the supporter sets, group quota-sized sets, test the residual criterion, and multiply these polynomials by dynamic programming while discarding degrees above \(k\). A direct implementation uses \(O(m^2n+mk^2)\) elementary set and integer operations; the counts have at most \(m+1\) binary digits, so bit complexity is polynomial.

**Step 5: The lottery and nonlaminar boundary.** In the pair-block example there are \(k\) quota classes, each of multiplicity two. A size-\(k\) DR committee must choose exactly one of the two candidates per class, giving \(2^k\) favorable committees; the denominator counts all size-\(k\) subsets of the \(2k\) candidates. Stirling's formula gives \(\binom{2k}{k}\sim4^k/\sqrt{\pi k}\). For the three overlapping two-voter supporter sets \(\{1,2\},\{2,3\},\{3,4\}\), every two-candidate committee satisfies JR because any unselected two-voter set intersects the represented union, but the first two cover three voters and the first and third cover four. This proves failure of the coverage invariance without the hypothesis.

## Verification

The standalone `verify.py` checks the theorem's predicted count against direct enumeration of all size-\(k\) committees, using an independent JR residual test. It exhaustively checks 26,996 ordered laminar candidate-support tuples on up to four labeled voters and four labeled candidates, amounting to 134,760 count comparisons when supplemented by 30,000 fixed-seed randomly generated laminar instances on up to ten voters and nine candidates. It separately tests a feasible eight-voter instance with exactly four DR committees and a nonlaminar coverage counterexample. The verifier prints `VERIFIED` if every check passes. These finite checks corroborate, but do not replace, the proof for all \(n,m,k\).

## Relationship to prior work

Chingoma, Grossi, Lindeboom and Maly (2026, arXiv:2609.29332) introduce DR with the exact quota-sized supporter-set condition, prove general DR decision NP-complete (Definition 25 and Theorem 28), and give a polynomial-time *local* DR heuristic. Their results do not assert the laminar-support feasibility criterion, mandatory quota-block structure, coverage rigidity, exact count, or exponential-scarcity family derived here. The comparison uses relevant sections and Appendix D of the openly accessible full HTML manuscript, not solely its abstract.

Aziz et al. (2014/2017) establish general JR, while Elkind et al. (2021, arXiv:2108.12949) show that a *smallest unrestricted JR-justifying candidate group* can be found efficiently with a tree representation of voter approvals. That is a different optimization: it permits arbitrary candidate supporter sizes and neither fixes the committee to DR's quota-sized candidates nor counts all DR committees. Their discussion of JR committee counts does not imply this restricted exact enumeration. The present laminar-support condition is also different from the previously defined recursive *laminar proportionality* election domain. An independently indexed identical classification has not been located; elementary reductions and unpublished observations remain possible priority risks.

## Limitations

The theorem applies only to laminar **candidate supporter sets**. Overlapping quota-sized support sets can make the represented voter set depend on the committee, as the counterexample shows. No tractability assertion is made for unrestricted or general voter-interval profiles. The exponential probability statement concerns uniform sampling of complete committees, not a behavioral or strategic model of voters. The result characterizes mathematical DR feasibility and count, not the welfare or strategic performance of any election mechanism. Its relationship to unindexed literature remains subject to external scholarly validation; no independent audit has been performed.

## References

1. J. Chingoma, D. Grossi, F. Lindeboom and J. Maly, *Diverse Representation in Approval-Based Committee Voting*, arXiv:2609.29332 (first submitted 2026-09-24; full HTML version 2 dated 2026-10-28), https://arxiv.org/html/2609.29332v2 .
2. H. Aziz, M. Brill, V. Conitzer, E. Elkind, R. Freeman and T. Walsh, *Justified Representation in Approval-Based Committee Voting*, arXiv:1407.8269 (first submitted 2014-07-31), https://arxiv.org/abs/1407.8269 .
3. E. Elkind, P. Faliszewski, A. Igarashi, P. Manurangsi, U. Schmidt-Kraepelin and W. Suksompong, *Justifying Groups in Multiwinner Approval Voting*, arXiv:2108.12949 (first submitted 2021-08-30), https://arxiv.org/abs/2108.12949 .
