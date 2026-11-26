# The four-world threshold and exact census for flattening in centred selection conditionals

## Finding
Let \(W\) be a labelled, nonempty finite set of \(n\) worlds. A **total deterministic strongly centred selection policy** chooses \(f(w,A)\in A\) for every \(w\in W\) and nonempty \(A\subseteq W\), subject to \(f(w,A)=w\) whenever \(w\in A\). Its conditional on the Boolean algebra \(\mathcal P(W)\) is
\[
 A\Rightarrow B=\{w\in W:A=\varnothing\ \text{or}\ f(w,A)\in B\}.
\]
The flattening/preconditional axiom \(\mathrm{P5}\) is
\[
 A\Rightarrow((A\cap B)\Rightarrow C)\subseteq (A\cap B)\Rightarrow C
\]
for all \(A,B,C\subseteq W\). Every centred policy satisfies the other four preconditional axioms, conditional identity, semicomplementation and double-negation inflation.

**Sharp threshold.** Every such selection policy satisfies \(\mathrm{P5}\) for \(n\le3\), but some fail it for \(n=4\).

**Complete first nonautomatic layer.** On four labelled worlds, there are exactly \(24^4=331776\) centred selection policies, of which exactly **138** satisfy \(\mathrm{P5}\); exactly **331638** fail. The 138 satisfying policies split into precisely seven relabelling classes, with orbit sizes \(6,12,24,24,24,24,24\). Their associated Boolean conditionals are pairwise distinct on the fixed labelled algebra. On three labelled worlds, there are exactly eight centred policies, all satisfying \(\mathrm{P5}\).

## Assumptions and scope
The carrier is the **full** power-set Boolean algebra. Each nonempty antecedent has exactly one selected world at each evaluation world; there are no restricted domains, inaccessible worlds, ties, or partial selections. Strong centering is required. The equivalence and finite census are about this semantic class, not about all abstract preconditionals or arbitrary selection frames. Relabelling means simultaneous permutation of the four world names in the policy and the Boolean algebra.

## Proof
A policy always satisfies \(\mathrm{P1}\): \(W\Rightarrow B=B\), since strong centering chooses \(f(w,W)=w\). It satisfies \(\mathrm{P2}\): \(A\cap B\subseteq A\Rightarrow B\), again by centering. Success \(f(w,A)\in A\) gives \(A\Rightarrow B=A\Rightarrow(A\cap B)\), which implies \(\mathrm{P3}\). Consequent monotonicity implies \(\mathrm{P4}\). Identity \(A\Rightarrow A=W\) holds. For nonempty \(A\), \(A\Rightarrow\varnothing=\varnothing\), whereas \(\varnothing\Rightarrow\varnothing=W\). Consequently derived negation is \(\neg\varnothing=W\) and \(\neg A=\varnothing\) for nonempty \(A\); this proves semicomplementation and double-negation inflation.

For nonempty \(X\subseteq A\) and any world \(w\), the axiom \(\mathrm{P5}\), with \(X=A\cap B\), holds for **all** consequences \(C\) if and only if
\[
 \boxed{f(f(w,A),X)=f(w,X).}\tag{1}
\]
Indeed the left-side conditional holds exactly when \(f(f(w,A),X)\in C\), while the right side holds exactly when \(f(w,X)\in C\); inclusion for every subset \(C\subseteq W\) forces equality by taking \(C\) to be the singleton consisting of the left selected world. Empty \(A\) or \(X\) is automatic. This equivalence is the usual strong-density equation specialized to total functional selection.

If \(w\in A\), equation (1) is immediate from centering. If \(w\notin A\) and \(n\le3\), then \(|A|\le2\). The only possible nonempty \(X\subseteq A\) is \(X=A\), for which (1) is automatic by centering at \(f(w,A)\), or a singleton, for which both sides choose that same singleton. Thus the first failure cannot occur below four worlds.

For a four-world set and a fixed \(w\), write its other worlds as \(v,a,b\). There are three unordered pair antecedents excluding \(w\), each with two possible selections, and the triple antecedent \(W\setminus\{w\}\), with three possible selections. Hence \(2^3\cdot3=24\) independent choices per world, or \(24^4\) policies overall.

For (1), all nonautomatic tests at \(w\) arise when \(A=W\setminus\{w\}\) and \(X\) is a pair in \(A\). Suppose \(f(w,A)=v\). For \(X=\{v,a\}\) and \(X=\{v,b\}\), equation (1) forces \(f(w,X)=v\), because \(v\in X\) and centering makes \(f(v,X)=v\). The remaining pair \(\{a,b\}\) can be oriented either way. Thus each potentially admissible local policy corresponds uniquely to an ordered triple \((v,a,b)\), meaning \(v\) is selected from the triple, \(v\) is selected from either pair containing it, and \(a\) is selected from \(\{a,b\}\). There are six such triples at each world, giving \(6^4=1296\) candidate combinations.

Only one compatibility condition remains: for each world \(w\), if its order is \((v,a,b)\), then the order belonging to world \(v\) must rank \(a\) ahead of \(b\). This is precisely equation (1) with \(A=W\setminus\{w\}\) and \(X=\{a,b\}\). The finite sum
\[
 \sum_{(\rho_w)\in\prod_{w\in W}\mathrm{Sym}(W\setminus\{w\})}
 \prod_{w\in W}{\boldsymbol1}\bigl[\rho_{\rho_w(1)}^{-1}(\rho_w(2))<\rho_{\rho_w(1)}^{-1}(\rho_w(3))\bigr]=138
\]
is evaluated exhaustively by the included independent ranking checker; here \(\rho_w\) is an ordered triple and the inverse notation means position in the list. No infinite extrapolation enters this finite identity. Exhaustive relabelling under the 24 permutations of \(W\) gives the seven orbit sizes stated above.

An explicit four-world failure is: at world \(0\) select \(1\) from \(\{1,2,3\}\), select \(2\) from \(\{2,3\}\), and at world \(1\) select \(3\) from \(\{2,3\}\); complete all other selections arbitrarily subject to strong centering. Then (1) fails for \(w=0\), \(A=\{1,2,3\}\) and \(X=\{2,3\}\).

## Verification
Run `python3 check_selection.py` with the standard Python library. It separately enumerates all \(24^4\) centred policies directly using the strong-density equality on every nonempty nested antecedent; constructs and counts the reduced \(6^4\) ranked candidates; confirms their exact agreement; and computes relabelling orbits. Output is `CENTRED_SELECTION_FLATTENING_OK total=331776 valid=138 invalid=331638 orbits=7`. The enumeration is **complete** for the finite four-world universe: each antecedent/world choice has been explicitly covered. No assertion about an unknown larger-world census follows.

## Relationship to prior work
Holliday, *Preconditionals*, Definition 1, Example 14 and Propositions 15–16, establishes the five axioms and the strong-density representation of selection preconditionals, including its relation to centering, functionality and normality. Chen, *Fundamental Propositional Logic with Preconditional*, Definition 3.1 and Section 3, restates the axioms and defines the stronger fundamental-preconditional class, motivating the precise redundancy question. These **underlying semantic facts are prior work**. The new finite computation concerns the sharp world-number at which their fifth axiom stops being automatic in the strongly centred functional-total subclass, and the complete first failing-layer enumeration. Neither source is claimed to be a novelty certificate; equivalent historical enumerations remain possible.

## Limitations
The count concerns a constrained but natural selection-policy class, not all preconditional operations on an eight- or sixteen-element Boolean algebra. It does not address partial, nonfunctional, non-centred or infinite selection systems. Four-world non-satisfying policies meet P1–P4 and the stated extra axioms but **are not themselves preconditionals**; only the 138 satisfying policies are. The originality comparison cannot exclude inaccessible or differently named historical conditional-selection censuses. The result has not received independent mathematical audit.

## References
- Z. Chen, *Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations*, arXiv:2607.20221 (first posted 2026-07-22), especially Definition 3.1 and Section 3. https://arxiv.org/abs/2607.20221
- W. H. Holliday, *Preconditionals*, arXiv:2402.02296 (first posted 2024-02-04), especially §2.5, Example 14 and Propositions 15–16. https://arxiv.org/abs/2402.02296
