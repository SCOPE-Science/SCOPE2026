# Tribonacci-optimal abductive explanations for a fixed two-event response specification

## Finding

In finite-trace linear temporal logic with **strong next**, fix the *single* formula
\[
\Theta=\mathsf G\bigl((\mathsf X\top\wedge r)\to(d\vee\mathsf Xd)\bigr).
\]
There are just two atomic propositions: a request \(r\) and a delivery \(d\). At each nonfinal position, a request must be satisfied by delivery now or at the next position. The final-position guard is essential to the stated convention.

Let \(n\ge2\), and let \(A_n\) be the largest number of **subset-minimal abductive explanations (AXps) of satisfaction** among all compliant length-\(n\) traces, with each time-indexed truth value a separate, lockable Boolean feature. Then
\[
\boxed{A_2=3,\quad A_3=5,\quad A_4=9,\qquad
 A_n=A_{n-1}+A_{n-2}+A_{n-3}\quad(n\ge5).}
\]
Thus \(A_n\) has generating function
\[
\sum_{n\ge2}A_nz^n=\frac{3z^2+2z^3+z^4}{1-z-z^2-z^3},
\]
and grows as \(\Theta(\alpha^n)\), where \(\alpha>1\) is the real root of \(\alpha^3=\alpha^2+\alpha+1\). Specifically, \(A_n=\operatorname{A000213}(n+1)\) in OEIS indexing; the numbers are the pre-existing Tribonacci sequence, shifted by one position; **the sequence itself is not claimed as new**.

**Exact maximizers.** Exactly two compliant length-\(n\) traces attain \(A_n\): in each, every delivery \(d_j\) is true, and every nonfinal request \(r_i\), \(0\le i\le n-2\), is false. The final request \(r_{n-1}\) may be true or false. Every other compliant trace has strictly fewer AXps.

At either maximizer, the exact AXp cardinality polynomial is
\[
F_n(u)=\sum_{\substack{b\in\{0,1\}^n\\ \text{no }111\text{ and no initial/final }11}}
 u^{\sum_{j=0}^{n-1} b_j+\sum_{i=0}^{n-2}(1-b_i)(1-b_{i+1})}.
\]
In particular \(F_n(1)=A_n\), its nonzero exponents range from \(\lfloor n/2\rfloor\) through \(n-1\), and for \(n\ge3\) its coefficient of \(u^{n-1}\) is exactly four. It has the finite transfer representation
\[
F_n(u)=(u,u,u,0)\!
\begin{pmatrix}u&u&0&0\\0&0&1&u\\u&u&0&0\\0&0&1&0\end{pmatrix}^{n-2}
\begin{pmatrix}1\\1\\1\\0\end{pmatrix},
\]
the states in order being \(00,01,10,11\).

For every compliant length-\(n\) trace there are **at most \(n-1\) subset-minimal contrastive explanations (CXps)** of satisfaction, and at both AXp maximizers there are *exactly* \(n-1\), each containing three time-indexed observations. Hence one fixed formula on a fixed two-proposition alphabet can have exponentially many AXps but only linearly many CXps.

## Assumptions and scope

Traces have exact length \(n\ge2\). Strong next \(\mathsf X\psi\) is false at the final position; \(\mathsf X\top\) is therefore an exact nonfinal guard. At a trace \(\pi\), an AXp is an inclusion-minimal set of time-indexed literals true in \(\pi\) such that **every** trace of the same length preserving those literal values satisfies \(\Theta\). A CXp is an inclusion-minimal set of time-indexed literals of \(\pi\) which, if allowed to change with all other observations locked, permits **some** length-\(n\) trace violating \(\Theta\). These are the satisfaction-side duals of the finite-trace explanation definitions of Fionda, Ielo and Ricca (2026). A time-indexed atom and its negation encode the same lockable feature at different values.

Write \(r_i,d_j\) for the values at position \(i,j\). The exact bounded propositional translation is
\[
\Theta_n=\bigwedge_{i=0}^{n-2} e_i,\qquad
 e_i=(\neg r_i\vee d_i\vee d_{i+1}).
\]
Each clause \(e_i\) has its own private negative-request literal \(p_i=\neg r_i\), and two shared positive-delivery literals \(q_j=d_j\). Every one of these \(2n-1\) literals has a consistent polarity throughout \(\Theta_n\). The final request does not occur.

## Proof

**1. Exact AXp and CXp hypergraphs.** For a compliant \(\pi\), let \(E_i(\pi)\subseteq\{p_i,q_i,q_{i+1}\}\) be the set of literals of clause \(e_i\) true in \(\pi\). This set is nonempty. A locked set \(S\) guarantees satisfaction exactly if it meets each \(E_i(\pi)\). The forward implication follows because one true literal is then fixed in each clause. For the reverse implication, if \(S\cap E_i(\pi)=\emptyset\), set all three literals in that clause false; this is compatible with \(S\), since the literals have globally consistent polarities, and it makes \(\Theta_n\) false. Thus AXps are precisely the minimal transversals of \(\{E_i(\pi)\}\).

Likewise, unlocking \(S\) permits a violation if and only if \(E_i(\pi)\subseteq S\) for some \(i\): in that case make all true clause literals false; conversely any violating completion has falsified a clause, so every originally true literal in it must have been unlocked. Therefore CXps are exactly the inclusion-minimal sets among \(E_0(\pi),\ldots,E_{n-2}(\pi)\). This immediately bounds their number by \(n-1\).

**2. Sharp global optimization and uniqueness.** Let \(H\) be the full hypergraph with edges \(\{p_i,q_i,q_{i+1}\}\) for \(i=0,\ldots,n-2\), and let \(U(\pi)\) be the set of true literals drawn from its vertex set. Minimal transversals of \(\{E_i(\pi)\}\) are *exactly* the minimal transversals of \(H\) contained in \(U(\pi)\). Indeed, a transversal contained in \(U\) hits \(E_i=U\cap e_i\) iff it hits \(e_i\), and inclusion-minimality is the same property for that fixed transversal. Thus restricting true literals can only delete explanations, never create new ones from this family.

Every vertex of \(H\) occurs in some minimal transversal of \(H\). The private vertex \(p_i\) occurs in \(\{p_0,\ldots,p_{n-2}\}\). For \(q_j\), let \(I_j\) be the one or two indices of clauses incident with \(q_j\). Then
\[
\{q_j\}\cup\{p_i: i\notin I_j\}
\]
is a minimal transversal: \(q_j\) is indispensable on its incident clauses, and every remaining private \(p_i\) is indispensable on its own clause. Hence deleting **any** vertex from \(U\) strictly lowers the number of available minimal transversals. The maximum is attained iff \(U\) contains every vertex of \(H\), which says all \(d_j\) are true and all nonfinal \(r_i\) are false. Because the unused final request has either value, exactly two full traces maximize.

**3. Binary-word bijection and full size distribution.** For a minimal transversal \(S\subseteq V(H)\), write \(b_j=1\) iff \(q_j\in S\). Private vertices must then be selected **exactly** when their two adjacent deliveries are absent:
\[
p_i\in S\iff b_i=b_{i+1}=0.
\]
If either adjacent delivery were selected, \(p_i\) would be redundant; if neither were selected, \(p_i\) would be required. For \(q_j\in S\) to be indispensable, at least one incident clause must contain no other selected delivery. At an endpoint this forbids the adjacent pair \(11\); at an interior position it forbids \(111\). Conversely, when there is no \(111\) and no endpoint \(11\), every selected delivery has a private incident clause and every selected private \(p_i\) has its private clause. This proves the asserted bijection and polynomial \(F_n(u)\).

The state pair \((b_{j-1},b_j)\) suffices to track the restrictions. On appending a bit, its weight is \(u\) when the new bit is \(1\), plus another factor \(u\) instead when the last pair is \(00\); otherwise the weight is \(1\). Starting with permitted length-two states \(00,01,10\), each of weight \(u\), and rejecting the state \(11\) at the end gives the displayed transfer matrix. At \(u=1\), its characteristic polynomial is \(\lambda(\lambda^3-\lambda^2-\lambda-1)\). Together with direct evaluations \(F_2(1)=3,F_3(1)=5,F_4(1)=9\), this yields the order-three recurrence and generating function.

For size bounds, the \(n-1\) clauses require distinct private-witness clauses for the elements of a minimal transversal, so its cardinality is at most \(n-1\). Each selected delivery covers at most two clauses, and each selected private literal covers one, giving size at least \(\lceil(n-1)/2\rceil=\lfloor n/2\rfloor\). More precisely, for each \(0\le k\le\lfloor(n-1)/2\rfloor\), start with all private literals and replace the \(2k\) literals \(p_0,\ldots,p_{2k-1}\) with the \(k\) deliveries \(q_1,q_3,\ldots,q_{2k-1}\). Their incident clause pairs are disjoint and each is the unique selected literal on its pair; the remaining private literals retain their own witness clauses. This gives a minimal transversal of size \(n-1-k\), proving **every** integer between the stated lower and upper bounds occurs. For \(n\ge3\), an explanation of size \(n-1\) gives an injective assignment of one private-witness clause to each selected literal, so all \(n-1\) clauses must be used. If an interior delivery \(q_j\), \(1\le j\le n-2\), is selected, its two incident clauses cannot be private witnesses for *any other* selected element. Of the \(n-1\) clauses, at most one can witness \(q_j\) and the other \(n-3\) clauses can witness the remaining elements, forcing \(|S|\le n-2\). Only endpoint deliveries may replace their adjacent private vertices. Hence there are exactly four maximum-size explanations: all private \(p_i\), with neither, either one, or both endpoint replacements \(p_0\mapsto q_0\) and \(p_{n-2}\mapsto q_{n-1}\). For \(n=2\), there are three explanations, all of size one.

**4. Contrastive extremality.** At a maximizing trace, each \(E_i=\{p_i,q_i,q_{i+1}\}\). The \(n-1\) sets are distinct and none contains another, so all are CXps. Each has size three. The general upper bound from Step 1 is therefore sharp.

## Verification

The independent standard-library Python program `verify.py` performs both (i) brute-force semantic locking/unlocking tests, independently of transversal reduction, for every compliant trace of lengths \(2,3,4\) (242 traces in total), and (ii) exhaustive searches for the AXp maximum and its exact two maximizing traces among every compliant trace of lengths \(2,\ldots,8\) (39,818 compliant traces). It additionally checks the binary-polynomial size distributions and Tribonacci recurrence through length \(19\), and the sharp CXp count at all maximizers tested. All tests pass. Finite checks corroborate but do not replace the general proof.

For example, \(F_4(u)=5u^2+4u^3\), \(F_5(u)=u^2+12u^3+4u^4\), and \(F_6(u)=7u^3+20u^4+4u^5\). The first maximum counts are \(3,5,9,17,31,57,105\) for lengths \(2,\ldots,8\).

## Relationship to prior work

Fionda, Ielo and Ricca (2026), arXiv:2610.35169v1, give the finite-trace AXp/CXp definitions, prove their hitting-set duality, and exhibit a family of formulas growing with \(N\) that has \(N\) AXps but \(2^N\) CXps. The present result is a complementary separation in the opposite direction: one fixed two-atom formula, compliant rather than violating traces, exponentially many AXps, and linearly many CXps. Their general definitions and duality alone do not give this per-length exact extremum, its unique maximizing valuations, or its size distribution. These are the claims evaluated here, not the already-known duality.

Ferrère, Maler and Ničković (2015) study temporal implicants for LTL and MTL traces, using different trace models and a constructive diagnostic procedure; the inspected theorem and algorithms do not provide the fixed-finite-length count or optimization. The Tribonacci sequence itself and several binary-word/graph interpretations are classical and are catalogued as OEIS A000213. The present result claims a precise temporal-explanation realization and extremal characterization, **not a new recurrence or a new integer sequence**.

## Limitations

The theorem is for the exact fixed formula with its nonfinal guard and ordinary fixed-length finite-trace semantics. It treats subset-minimal explanations, not minimum-cardinality explanations alone, and its maxima are over **compliant** traces; it does not assert the same bounds for violating traces, arbitrary temporal formulas, added constraints correlating features, or alternative interventions. Existing combinatorial results may give a shorter derivation after the explicit hypergraph reduction. A historical equivalent under other explanation or transversal terminology remains possible.

## References

- Valeria Fionda, Antonio Ielo, Francesco Ricca, *Formal Explanations for Linear Temporal Logic over Finite Traces*, arXiv:2610.35169v1, first posted 2026-10-26. https://arxiv.org/abs/2610.35169
- Thomas Ferrère, Oded Maler, Dejan Ničković, *Trace Diagnostics using Temporal Implicants* (2015). https://thomasferrere.com/TraceDiagnosticsUsingTemporalImplicants.pdf
- The On-Line Encyclopedia of Integer Sequences, *A000213: Tribonacci numbers*. https://oeis.org/A000213
