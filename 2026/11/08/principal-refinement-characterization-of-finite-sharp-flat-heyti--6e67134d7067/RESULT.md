# Principal-refinement characterization of finite sharp flat Heyting–Lewis frames

## Finding

Let \(F=(W,\preceq,R)\) be a nonempty **finite** flat frame, with \(\preceq\) a preorder and \(R\subseteq W\times W\) arbitrary. Write
\[
\widehat R[x]=\{z\in W:\exists v\;(xRv\ \text{and}\ v\preceq z)\},\qquad \uparrow z=\{v\in W:z\preceq v\}.
\]
Under flat strict-implication semantics, \(F\) validates the sharp antecedent-distribution axiom
\[
\mathsf{di}:\quad ((p\mathbin{\rightsquigarrow}r)\wedge(q\mathbin{\rightsquigarrow}r))
\to((p\vee q)\mathbin{\rightsquigarrow}r)
\]
**if and only if** the following *principal-refinement property* holds:
\[
\tag{PR}
\forall x\in W\;\forall t\in\widehat R[x]\;\exists y,z\in W:
\quad x\preceq y,\quad z\preceq t,\quad
\widehat R[y]=\uparrow z\subseteq\widehat R[x].
\]
Equivalently, for every world \(x\), its upward-closed successor row is the union of all principal successor rows available at future worlds and contained in that row:
\[
\widehat R[x]
=\bigcup\{\widehat R[y]:x\preceq y,\ \widehat R[y]\subseteq\widehat R[x],\
\ \widehat R[y]=\uparrow z\ \text{for some }z\in W\}.
\]
Empty rows satisfy the requirement vacuously. The criterion is decidable by a direct \(O(|W|^4)\)-time algorithm on adjacency matrices. It strictly weakens the pointwise downward-directed sufficient condition in de Groot and Litak's 2026 semantics: an upward-flat counterexample with **three** worlds satisfies \(\mathsf{di}\) despite having a non-directed successor row, and three is the minimum possible size for such a separation.

## Assumptions and scope

We use exactly the finite flat-frame semantics of de Groot and Litak (2026). A valuation assigns each propositional variable an upset of the preorder. The ordinary connectives have intuitionistic Kripke meanings, while for any formulas \(\alpha,\beta\),
\[
 x\Vdash \alpha\mathbin{\rightsquigarrow}\beta
\ \Longleftrightarrow\
 \forall y\succeq x\;(R[y]\subseteq\llbracket\alpha\rrbracket
 \Longrightarrow R[y]\subseteq\llbracket\beta\rrbracket).
\]
This is **not** the usual pointwise Kripke conditional \(R[x]\cap\llbracket\alpha\rrbracket\subseteq\llbracket\beta\rrbracket\). The theorem permits reflexive, nonreflexive, cyclic and empty modal rows and does not require \(\preceq\) to be antisymmetric. No extra modal axiom or frame condition is imposed.

## Proof

**1. Upward normalization.** Every truth set of a formula is an upset, by induction on formulas. For every upset \(A\) and each \(x\in W\), \(R[x]\subseteq A\) holds if and only if \(\widehat R[x]\subseteq A\). Therefore replacing \(R\) with \(\widehat R\) does not change any formula truth value, and it suffices to work with upward-closed successor rows \(U_x=\widehat R[x]\).

**2. Prime upsets and finite decomposition.** A nonempty upset \(U\) in a finite preorder is *join-prime* among upsets (i.e., \(U\subseteq A\cup B\) for upsets \(A,B\) forces \(U\subseteq A\) or \(U\subseteq B\)) precisely when \(U=\uparrow z\) for some \(z\). The forward direction follows since \(U\) is the union of principal upsets of its minimal equivalence classes in the quotient partial order. If it has at least two distinct such minimal classes, those principal upsets split into two proper upsets \(A,B\) with \(U=A\cup B\), contradicting join-primality. Conversely, if \(\uparrow z\subseteq A\cup B\), then \(z\in A\) or \(z\in B\), so the whole principal upset belongs to that side.

**3. Principal refinement implies \(\mathsf{di}\).** Fix any valuation and \(w\in W\) with \(w\Vdash p\rightsquigarrow r\) and \(w\Vdash q\rightsquigarrow r\). Suppose, seeking a contradiction, that \(w\not\Vdash(p\vee q)\rightsquigarrow r\). There is \(x\succeq w\) with \(U_x\subseteq V(p)\cup V(q)\) but \(U_x\not\subseteq V(r)\). Choose \(t\in U_x\setminus V(r)\). By (PR), choose \(y\succeq x\) and \(z\preceq t\) with \(U_y=\uparrow z\subseteq U_x\). The prime-upset observation gives \(U_y\subseteq V(p)\) or \(U_y\subseteq V(q)\). As \(y\succeq w\), the corresponding assumed strict implication forces \(U_y\subseteq V(r)\), contradicting \(t\in U_y\setminus V(r)\). Thus \(\mathsf{di}\) holds at every world under every valuation.

**4. Failure of principal refinement refutes \(\mathsf{di}\).** Suppose (PR) fails at \(x\) and \(t\in U_x\): no principal row \(U_y\) at \(y\succeq x\) contains \(t\) while remaining inside \(U_x\). Consider the finite nonempty family \(\mathcal S=\{U_y:x\preceq y,\ t\in U_y\subseteq U_x\}\), which contains \(U_x\). Select an inclusion-minimal \(U\in\mathcal S\). By assumption, \(U\) is not principal. By Step 2, there exist proper upsets \(A,B\subsetneq U\) with \(U=A\cup B\). Set \(C=W\setminus\downarrow t\), where \(\downarrow t=\{s:s\preceq t\}\). This \(C\) is an upset and \(t\notin C\).

Assign \(V(p)=A\), \(V(q)=B\), and \(V(r)=C\). If for some \(v\succeq x\) we had \(U_v\subseteq A\) but \(U_v\not\subseteq C\), choose \(s\in U_v\cap\downarrow t\). Since \(U_v\) is an upset, \(t\in U_v\). Thus \(U_v\in\mathcal S\) and \(U_v\subseteq A\subsetneq U\), contradicting the minimality of \(U\). Hence \(x\Vdash p\rightsquigarrow r\). The same proof gives \(x\Vdash q\rightsquigarrow r\). But the row \(U=U_y\) at some \(y\succeq x\) is contained in \(A\cup B\) and contains \(t\notin C\), so \(x\not\Vdash(p\vee q)\rightsquigarrow r\). The axiom therefore fails at \(x\), proving necessity.

**5. Strictness and sharp size.** On \(W=\{b,u,v\}\), let the preorder consist of reflexivity and \(b\preceq u,b\preceq v\), and define \(R[b]=\{u,v\}\), \(R[u]=\{u\}\), \(R[v]=\{v\}\). Every row is an upset; \(R[b]=\uparrow u\cup\uparrow v\) is covered by the two future principal rows, so (PR) holds. Yet \(R[b]\) is not downward directed: no element of that row lies below both \(u\) and \(v\). On at most two worlds, any non-directed row must consist of two incomparable elements; the preorder is then discrete, and the offending row has no future principal refinement, so (PR) fails. This proves sharp three-world separation.

**6. Complexity.** Compute the preorder matrix and each \(U_x\) using Boolean closure, then precompute which rows equal some principal upset. For each pair \((x,t)\) with \(t\in U_x\), scan \(y\succeq x\) for a principal \(U_y\subseteq U_x\) containing \(t\). There are at most \(O(|W|^3)\) such attempts and a subset check costs \(O(|W|)\) using naive Boolean arrays, giving \(O(|W|^4)\) time. If a check fails, Step 4 constructs an explicit three-atom countervaluation.

## Verification

The included standalone `checker.py` independently compares (PR) with direct propositional-valuation testing of the flat conditional and \(\mathsf{di}\), using all upsets as possible values of \(p,q,r\). It exhausts all labelled preorders and all raw modal relations on one, two and three worlds: respectively \(2\), \(64\) and \(14{,}848\) frame pairs, totalling \(14{,}914\). It also checks \(600\) four-world cases generated from a fixed seed, tests the separating three-world example, and tests a nearby failing example. The printed success line is `FINITE_FLAT_DI_PRINCIPAL_REFINEMENT_OK`. These finite tests support the independently given proof but do not establish the universal theorem by enumeration.

## Relationship to prior work

De Groot and Litak, *Relational semantics for flat Heyting-Lewis Logic* (first released March 30, 2026, arXiv:2603.28402), define the flat-frame strict implication in Definition 3.1 and its upward closure invariance in Proposition 3.10. Their Lemma 3.12 supplies a **sufficient** pointwise downward-directed condition for the sharp distribution axiom, and Proposition 3.15 obtains soundness and completeness over this sufficient subclass. The criterion (PR) is a necessary-and-sufficient characterization of **all finite flat frames** validating that specific axiom; the three-world example proves that the sufficient subclass does not exhaust them. Their Table 1 and Lemma 5.2 address other axioms, including \(\mathsf p_a\), not the full equivalence asserted here.

Celani and Jansana, *Bounded distributive lattices with strict implication* (2005), establish weak Heyting algebras and their dual relational semantics, including the algebraic join-distribution identity. Their canonical relational clause is pointwise, involving an intersection of a relation row with the antecedent; it is not the flat whole-row containment clause used here. Their algebraic identity is acknowledged as prior mathematics rather than claimed anew. Litak and Visser (2018) supply additional background for constructive strict implication. Searches of the cited literature and relevant mathematical research records did not identify the finite principal-refinement equivalence; this does not constitute a guarantee of historical novelty.

## Limitations

The necessity argument uses finite inclusion-minimal rows and finite decomposition of nonprincipal upsets. It does not establish an analogous characterization for arbitrary infinite flat frames. No independent audit or complete historical-priority review has been carried out. The checker tests finite examples only; the main assertion is proved separately. The result concerns frame validity of \(\mathsf{di}\), not soundness or completeness of any new axiom system.

## References

1. J. de Groot and T. Litak, *Relational semantics for flat Heyting-Lewis Logic*, arXiv:2603.28402, first posted March 30, 2026. https://arxiv.org/abs/2603.28402
2. S. A. Celani and R. Jansana, *Bounded distributive lattices with strict implication*, Mathematical Logic Quarterly 51 (2005), 219–246. https://doi.org/10.1002/malq.200410022
3. T. Litak and A. Visser, *Lewis meets Brouwer: Constructive strict implication*, Indagationes Mathematicae 29 (2018), 36–90. https://doi.org/10.1016/j.indag.2017.10.003
