# Sharp Helly bound for contextual Horn-abduction explanations with finitely many hypotheses

## Finding
For every integer \(h\geq0\), let \(\mathcal P=(X,H,T,g,C)\) be a finite contextual propositional Horn-abduction instance with exactly \(|H|=h\) hypothesis atoms, an arbitrary finite set of source variables, a finite nonempty context set, and integrity constraints. A nonempty family of contexts \(D\subseteq C\) is a *minimal obstruction* when its valid-explanation families have empty common intersection but every proper subfamily has nonempty common intersection (with the empty-family intersection understood as \(2^H\)). Define
\[
B_h=\binom{h}{\lfloor h/2\rfloor}+\binom{h}{\lfloor h/2\rfloor+1},
\]
where a binomial coefficient with bottom index exceeding the top is zero. Then every minimal obstruction obeys
\[
|D|\le B_h.
\]
The bound is attained for every \(h\) by a finite *acyclic* Horn theory whose rules have only the manifestation or the integrity symbol as heads. For \(h\geq1\) every context of the extremal instance has at least one valid explanation. Consequently the maximum obstruction rank across the class equals \(B_h\); its first values for \(h=0,1,2,3,4,5,6\) are \(1,2,3,6,10,20,35\). As \(h\to\infty\),
\[
B_h\sim 2^{h+1}\sqrt{\frac{2}{\pi h}}.
\]
This is an exact sharp resource law, strengthening the universal \(2^h\) witness bound.

## Assumptions and scope
The source vocabulary contains two distinct facts \(x^0,x^1\) for each binary source variable \(x\in X\). A context \(c\) supplies precisely its own source facts \(F_c\). Hypothesis atoms never occur as heads. Horn rules may derive auxiliary atoms, the designated manifestation \(g\), or the integrity marker \(\bot\), and no rule body contains \(\bot\). Write \(\operatorname{cl}_T\) for least Horn closure. A hypothesis subset \(S\subseteq H\) is valid at \(c\) iff \(g\in\operatorname{cl}_T(F_c\cup S)\) and \(\bot\notin\operatorname{cl}_T(F_c\cup S)\). The family of all valid sets is \(\mathcal E_c\subseteq2^H\). All memberships and intersections refer to *all* hypothesis subsets, not only inclusion-minimal explanations. The upper bound does not require acyclicity; only its sharpness construction does. No bound is imposed on the number of source variables, contexts, clauses or clause width. No assertion concerns weighted, preferred, nonmonotonic, or probabilistic abduction.

## Proof
**1. Order-convex explanations.** Suppose \(A\subseteq B\subseteq Z\subseteq H\), with \(A,Z\in\mathcal E_c\). Horn-closure monotonicity implies that \(g\) derived from \(F_c\cup A\) is also derived from \(F_c\cup B\). If \(\bot\) were derived from \(F_c\cup B\), monotonicity would derive it from \(F_c\cup Z\), contradicting validity of \(Z\). Therefore \(B\in\mathcal E_c\): each \(\mathcal E_c\) is order-convex in the inclusion-ordered Boolean lattice.

**2. Witnesses avoid three-term inclusion chains.** If \(D\) is a minimal obstruction of cardinality at least two, for each \(c\in D\) choose \(S_c\in\bigcap_{d\in D\setminus\{c\}}\mathcal E_d\). Empty total intersection forces \(S_c\notin\mathcal E_c\); these witnesses are pairwise distinct. Suppose \(S_a\subsetneq S_b\subsetneq S_c\) for distinct indices \(a,b,c\in D\). The extreme sets \(S_a,S_c\) belong to \(\mathcal E_b\), whereas \(S_b\) does not. This contradicts order-convexity. Hence \(W=\{S_c:c\in D\}\) has no strict inclusion chain of three members. A one-context obstruction also satisfies the desired bound.

**3. The exact numerical upper bound.** A uniformly random maximal inclusion chain of \(2^H\) contains a particular set of size \(j\) with probability \(1/\binom hj\). Since it meets \(W\) at most twice, linearity of expectation gives
\[
\sum_{S\in W}\frac{1}{\binom h{|S|}}\le2.
\]
Let \(a_j\) be the number of \(j\)-element sets in \(W\). Then \(0\le a_j\le\binom hj\) and \(\sum_j a_j/\binom hj\le2\). Maximizing \(\sum_j a_j\) under these constraints fills the two largest binomial levels first (when \(h=0\), only one level exists). Their cardinality sum is \(B_h\). This proves \(|D|\le B_h\). This is the standard two-level instance of the generalized Sperner bound; the contribution here is its exact application to Horn explanations together with sharp realizability under the same hypothesis budget.

**4. Explicit matching acyclic Horn construction.** Fix \(h\ge0\), put \(k=\lfloor h/2\rfloor\), and let
\[
W=\{S\subseteq H:|S|=k\text{ or }|S|=k+1\}.
\]
Then \(|W|=B_h\), and every subset of \(W\) is order-convex: its distinct comparable members have cardinalities differing by exactly one, so no third Boolean-lattice set lies strictly between them. Choose \(h\) source variables \(x_1,\ldots,x_h\), and one context \(c_A\) for each \(A\in W\), defined by \(c_A(x_i)=1\) exactly when \(i\in A\). These context codes are distinct. Prescribe
\[
\mathcal E_{c_A}=W\setminus\{A\}\qquad(A\in W).
\]
For each \(A\), let \(U_A=\uparrow\mathcal E_{c_A}\) and \(L_A=\downarrow\mathcal E_{c_A}\), with upward and downward closures taken inside \(2^H\). Since \(\mathcal E_{c_A}\) is order-convex, \(\mathcal E_{c_A}=U_A\cap L_A\). For every inclusion-minimal set \(B\in U_A\), include the guarded Horn rule
\[
g\leftarrow F_{c_A},\ B.
\]
For every inclusion-minimal set \(B\) in the upward-closed complement \(2^H\setminus L_A\), include
\[
\bot\leftarrow F_{c_A},\ B.
\]
Here a displayed set in a rule body means the conjunction of its elements; empty sets give empty sub-bodies. There are finitely many rules. Only source and hypothesis atoms occur in bodies and only \(g\) and \(\bot\) in heads, so the dependency graph is acyclic. At context \(c_A\) no guard for a distinct code activates: each such guard contains a source fact absent from \(F_{c_A}\). For a candidate hypothesis set \(S\), the manifestation is derived precisely when \(S\in U_A\), while inconsistency is derived precisely when \(S\notin L_A\). The valid sets are therefore *exactly* the prescribed family \(W\setminus\{A\}\).

Now \(\bigcap_{A\in W}(W\setminus\{A\})=\varnothing\), but if any one context \(c_B\) is omitted, the subset \(B\in W\) is valid in all remaining contexts. Hence all \(|W|=B_h\) contexts form a minimal obstruction. For \(h\ge1\), \(|W|\ge2\), so each individual explanation family is nonempty. For \(h=0\), \(W=\{\varnothing\}\) and the one context has no valid explanation, giving the required singleton obstruction. This establishes sharpness in every case.

**5. Asymptotics.** The two largest adjacent binomial levels are asymptotically equal; Stirling's formula yields the displayed asymptotic value of \(B_h\).

## Verification
The standalone `checker.py` uses exact integer/Boolean operations to: (i) enumerate every candidate witness family for \(0\le h\le4\) and confirm that the maximum three-chain-free cardinality is \(B_h\); (ii) build the guarded manifestation and integrity rules for \(0\le h\le8\), then evaluate their closure semantics on every hypothesis subset in every extremal context; (iii) check each target explanation family, minimal-obstruction witness condition and interval convexity. Executing `python checker.py` prints `ALL_CHECKS_OK`. The exhaustive upper checks end at four hypotheses. Higher-dimensional validity follows from the proof, not finite enumeration.

## Relationship to prior work
Yukun Yang, *Choosing What to Observe: Higher-Order Obstructions in Horn Abduction*, arXiv:2610.32805v1 (first public 2026-10-23), defines minimal context obstructions and proves the general \(2^h\) witness ceiling in Lemma 2; Section 6, Lemma 4 records order-convexity. Its Proposition 4 proves unbounded obstruction ranks using one hypothesis atom per targeted context, and Theorem 6 gives a separate sharp bound for rectangular choice-slot families. Neither its general ceiling nor the rectangular bound states the exact unrestricted rank \(B_h\) with \(h\) hypotheses and an acyclic matching construction. The extremal two-level set-system bound itself is classical: Erdős's generalization of Sperner's theorem (discussed, for example, in Das–Gan–Sudakov, arXiv:1302.5210). We claim neither the generalized Sperner theorem nor the original contextual-abduction definitions as new. Geometric discrete Helly bounds for arbitrary Euclidean-convex traces are not substitutes for this order-convex restriction.

## Limitations
The construction may use exponentially many contexts and Horn clauses, and the theorem makes no complexity bound on finding a smallest obstructing context family from a succinct input. The numerical formula uses unrestricted integrity constraints and nonminimal hypothesis explanations. Without integrity constraints, nonempty families are upward-closed and share the full hypothesis set, so the phenomenon changes. The relationship to older abstract-poset order-convexity Helly theory could affect historical priority; the precise historical provenance of this special Helly number remains incompletely verified. The result has undergone only a self-review, not an independent mathematical audit.

## References
1. Yukun Yang. *Choosing What to Observe: Higher-Order Obstructions in Horn Abduction*. arXiv:2610.32805v1, posted October 23, 2026. https://arxiv.org/html/2610.32805v1.
2. Shagnik Das, Wenying Gan, Benny Sudakov. *Sperner's Theorem and a Problem of Erdős–Katona–Kleitman*. arXiv:1302.5210 (2013). https://arxiv.org/abs/1302.5210.
3. Gennadiy Averkov. *On Maximal S-Free Sets and the Helly Number for the Family of S-Convex Sets*. arXiv:1109.6179 (2011); related background for a **different** convexity notion, not a theorem implying the present order-convex rank.
