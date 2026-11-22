# A sharp contextual criterion for faithful Krom projections of finite Horn programs

## Finding

For every finite positive Horn program, the exact contexts in which rule-by-rule Krom projection can preserve least-model semantics admit a **necessary-and-sufficient local test**. Its failure has a sharp obstruction certificate whose size is bounded by the largest clause body. In particular, faithful projection for the original least model is always possible even when exact syntactic Krom factorization fails.

Let \(M_F=\operatorname{LM}(P\cup F)\) denote the least model when the atoms in \(F\) are added as facts. For every proper clause \(r=(a\leftarrow B)\), define

\[
H_r(\mathcal C)=B\setminus\bigcup_{F\in\mathcal C,\ a\notin M_F}M_F.
\]

**Context theorem.** A faithful Krom projection for all contexts in \(\mathcal C\) exists exactly when \(H_r(\mathcal C)\neq\varnothing\) for every proper clause. Failure has a subfamily of at most \(w(P)\) contexts witnessing it, and this bound is attained for every \(w(P)\ge2\). At one extreme, for the singleton context \(\{\varnothing\}\), projection is always possible. At the other extreme, for *all* fact contexts, it is possible exactly when every proper rule \(a\leftarrow B\) has \(b\in B\) with \(a\in\operatorname{LM}(P\cup\{b\})\).

**Compatible decomposition.** If a faithful projection exists for \(\mathcal C\), then with \(m=\max(1,w(P))\) there are Krom factors \(K_1,\ldots,K_m\subseteq P^{\lor}\) such that

\[
P\subseteq K_1\sqcup\cdots\sqcup K_m,
\qquad
\operatorname{LM}(P\cup F)=\bigcap_{i=1}^m\operatorname{LM}(K_i\cup F)
\quad(F\in\mathcal C).
\]

This semantic equality does **not** assert syntactic equality of the source program and the body-union.

## Assumptions and scope

Fix a finite nonempty atom alphabet \(A\). A positive definite Horn rule \(a\leftarrow B\) has head \(a\in A\) and a finite body \(B\subseteq A\), with \(B=\varnothing\) a fact. A program is a set of rules; distinct rules may share their head. For \(F\subseteq A\), writing \(P\cup F\) means adjoining every atom in \(F\) as a fact. The least model \(\operatorname{LM}(P\cup F)\) is the smallest set closed under all implications in that extended program.

A Krom projection of \(P\) retains all facts and, independently for each proper rule \(a\leftarrow B\), chooses one \(b_r\in B\) and installs \(a\leftarrow\{b_r\}\). Duplicate resulting rules may coalesce. Let \(P^{\lor}\) be the set of all these available unary rules together with source facts. The width \(w(P)\) is the largest nonempty-body size, or zero when there are no proper rules. No claim is made about normal programs with negative literals, disjunctive heads, or arbitrary rule-context extensions.

The body-union \(K_1\sqcup\cdots\sqcup K_m\) combines one rule with the same head from each factor and takes the union of the selected bodies. It does not mean ordinary union of rule sets. All statements quantify over every finite positive definite program and every designated fact-context family \(\mathcal C\), including the empty family.

## Proof

**1. Local necessity and sufficiency.** For any selected unary rule \(a\leftarrow b_r\) with \(b_r\in B\), every model of the projection \(K\cup F\) is a model of \(P\cup F\): replacing \(B\) by a member of \(B\) strengthens a rule. Therefore

\[
M_F\subseteq\operatorname{LM}(K\cup F).
\]

Equality holds precisely when \(M_F\) itself models \(K\). For the selected rule this means \(a\in M_F\) or \(b_r\notin M_F\). Across all contexts with \(a\notin M_F\), the available choices are exactly the elements of \(H_r(\mathcal C)\). Since choices for different source rules are independent, a common faithful projection exists if and only if every \(H_r\) is nonempty; selecting any member of each gives a constructive projection. The empty family has no restrictions beyond each nonempty body being nonempty.

**2. Sharp context obstruction.** If \(H_r(\mathcal C)=\varnothing\), for each \(b\in B\) choose one context \(F_b\in\mathcal C\) in which \(a\notin M_{F_b}\) yet \(b\in M_{F_b}\). The at most \(|B|\le w(P)\) chosen contexts still make \(H_r\) empty, and so preclude every faithful projection. For every \(t\ge2\), take the \(t+1\) atoms \(a,b_1,\ldots,b_t\), the sole clause \(a\leftarrow\{b_1,\ldots,b_t\}\), and precisely the contexts \(F_i=\{b_i\}\). Then \(M_{F_i}=F_i\). All \(t\) contexts rule out every possible selected body atom, whereas any strict subfamily leaves one available. Thus the obstruction bound \(t\) is exact.

**3. Extreme context regimes.** With \(\mathcal C=\{\varnothing\}\), write \(M=\operatorname{LM}(P)\). If the head \(a\notin M\), the full body \(B\) cannot be contained in \(M\), because \(M\) models the source rule. Therefore \(B\setminus M\neq\varnothing\); when \(a\in M\), every \(b\in B\) is permitted. Thus a faithful projection always exists.

For \(\mathcal C=\mathcal P(A)\), if a chosen \(b\in B\) works for every context, apply it to \(F=\{b\}\): since \(a\) is derived by the projected unary rule, faithfulness implies \(a\in\operatorname{LM}(P\cup\{b\})\). Conversely, if the latter membership holds, every model of \(P\) containing \(b\) contains \(a\). Hence in any fact context with \(a\notin M_F\) we must also have \(b\notin M_F\). This is exactly the local common-witness condition.

**4. Completion to body-union factors.** Let \(K_1\) be the faithful projection from Step 1 and put \(m=\max(1,w(P))\). For each nonempty-body source rule, enumerate all elements of its body in a length-\(m\) sequence whose first element is the selection used by \(K_1\); repeat any member when the body has fewer than \(m\) elements. Let factor \(K_i\) contain all original facts and the unary rule given by the \(i\)-th element of every sequence. Every factor lies within \(P^{\lor}\); choosing the corresponding rule in every factor reconstructs each source rule, so \(P\subseteq K_1\sqcup\cdots\sqcup K_m\). Every factor is a rulewise relaxation of \(P\), hence \(M_F\subseteq\operatorname{LM}(K_i\cup F)\). Since the first factor is faithful for all \(F\in\mathcal C\), the intersection is exactly \(M_F\). Cases with only facts or no rules take \(m=1\) and the same argument applies.

## Verification

A standalone deterministic Python verifier, `verify.py`, enumerates complete projection choices independently of the proved criterion. It checked 84,168 program/context-family instances: every one- and two-atom program with every context family, all three-atom programs of at most two rules with every context family, and 3,000 reproducibly sampled four-atom instances. It also checks the all-fact-context simplification, constructs the compatible body-union factors, verifies their inclusion and least-model intersection, and tests the sharp obstruction family for widths 2 through 6. Running `python verify.py` prints `VERIFY_OK` followed by the number of comparisons. These finite checks are consistency tests, not a substitute for the general proof above.

## Relationship to prior work

Antić's 2026 paper establishes exact syntactic and least-model decompositions for minimalist programs (Theorem 66), but for arbitrary Horn programs its Theorem 68 gives upper inclusions for the reconstructed program and the intersection of Krom-factor least models. The present theorem keeps the full nonminimalist domain and proves that an *appropriate selection* always makes the least-model intersection exact at the original fact context. More substantially, it classifies the possible failure of *simultaneous* exactness under arbitrary prescribed fact contexts, with a sharp width-sized obstruction certificate. This does not claim source-level syntactic equality.

Antić's 2023 note characterizes uniform equivalence **between two already-Krom programs** using reachability. It does not specify which arbitrary many-body Horn programs admit a rulewise unary selection preserving a designated family of context extensions. The more general 2024 algebra of sequential composition does not state the local selection criterion. Source comparisons were made at the level of their respective hypotheses and conclusions, not merely titles.

## Limitations

The selection uses knowledge of the source least models under the chosen fact contexts; this is a classification and polynomial-time verification for explicitly listed contexts, not an unconditional constant-time compilation. It preserves least-model consequences only, not full logical equivalence, immediate consequence operators, supported models, or arbitrary program extensions. The body-union may introduce extra rules for heads with multiple source clauses. The all-fact-context equivalence does not assert that a collection of several projections could not jointly preserve more contexts when no single one does. Independent historical-priority and mathematical reviews have not been performed.

## References

1. Christian Antić, *Set-like Operations on Propositional Logic Programs*, first public arXiv version May 5, 2026, arXiv:2605.03613; especially Theorems 66 and 68 and Example 69. https://www.cambridge.org/core/journals/theory-and-practice-of-logic-programming/article/setlike-operations-on-propositional-logic-programs/2216B8E01234B4A5C4C14F94D401A651
2. Christian Antić, *Algebraic characterizations of least model and uniform equivalence of propositional Krom logic programs*, arXiv:2302.04664v2 (2023), especially Section 5. https://arxiv.org/html/2302.04664
3. Christian Antić, *Sequential composition of propositional logic programs*, *Annals of Mathematics and Artificial Intelligence* 92 (2024), 505–533, DOI 10.1007/s10472-024-09925-x. https://link.springer.com/article/10.1007/s10472-024-09925-x
