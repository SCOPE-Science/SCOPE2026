# Two S5 agents and one proposition attain every finite believed-announcement lifetime

## Finding

For each integer \(n\ge 1\), there is an \(n\)-world, **initially two-agent \(\mathsf{S5}\)** Kripke model with exactly one relevant propositional variable, and there is one **fixed** modal-depth-one formula (independent of \(n\)) whose repeated *believed public announcements* make exactly \(n\) strict model changes before stabilization. Each agent's initial equivalence classes have size at most two. Thus the known general \(n\)-world upper bound is attained even with two equivalence relations of uniformly bounded class size and one bit of propositional information.

Precisely, let \(W_n=\{0,1,\ldots,n-1\}\), \(V(p)=\{j\in W_n:j\text{ is even}\}\), and let \(R_a\) be the equivalence relation whose classes are consecutive pairs \(\{0,1\},\{2,3\},\ldots\), with a terminal singleton if necessary. Let \(R_b\) have singleton class \(\{0\}\), followed by pairs \(\{1,2\},\{3,4\},\ldots\), again with a terminal singleton if necessary. Use throughout the same announcement
\[
\varphi=(p\wedge\Diamond_a\neg p)\vee(\neg p\wedge\Diamond_b p).
\]
For \(M^0=M\) and \(M^{k+1}=M^k|\varphi\), the first fixed stage is exactly \(n\):
\[
M^k\ne M^{k+1}\quad (0\le k<n),\qquad M^n=M^{n+1}.
\]

For comparison, on *arbitrary* initially one-agent finite \(\mathsf{S5}\) models with \(n\) worlds and at most \(r\ge0\) proposition letters appearing in the announcement, the exact worst-case number of strict updates is
\[
\min\{n,2^r\}.
\]
The valuation-type upper-bound mechanism is already contained in Yamada's 2026 single-agent \(\mathsf{K45}\) argument; the elementary lower-bound construction below makes the exact frontier explicit. In particular, one propositional letter permits at most two changes with one \(\mathsf{S5}\) agent but arbitrarily many with two agents, even with a uniform modal-depth-one formula.

## Assumptions and scope

The language uses classical Boolean connectives and two normal diamond modalities; \(\Diamond_i\chi\) means there exists an \(R_i\)-successor satisfying \(\chi\). The announcement semantics is **belief update, not ordinary public announcement that deletes worlds**:
\[
R_i^{k+1}=R_i^k\cap(W\times\llbracket\varphi\rrbracket_{M^k}),\quad W^{k+1}=W^k=W,\quad V^{k+1}=V^k=V.
\]
For the two-agent result, \(n\) ranges over all positive integers. Both initial relations are reflexive, symmetric and transitive; the updated relations need not retain \(\mathsf{S5}\), as required by this belief-update semantics. The same formula is used at every stage and for every \(n\). No announcement modalities, auxiliary propositional letters, or common-knowledge modalities occur in that formula.

For the one-agent comparison, \(n\ge1\) and \(r\ge0\) are integers, and arbitrary static modal formulas over \(r\) atoms are permitted. The maximum ranges over initially \(\mathsf{S5}\) models of that size and such formulas; there is no requirement that the one-agent maximizing formula be independent of \(r\).

## Proof

**Target sets.** At stage \(k\), write
\[
T_k=\{v\in W:\exists i\in\{a,b\},\exists u\in W,\ (u,v)\in R_i^k\}.
\]
The update rule removes *all* remaining arrows into a target \(v\) precisely when \(\varphi\) fails at \(v\). Thus
\[
T_{k+1}=T_k\cap\llbracket\varphi\rrbracket_{M^k}.
\]
Because initially every world is targeted and every agent filters on the same target truth set, induction also yields \(R_i^k=R_i^0\cap(W\times T_k)\) for each of the two agents. Every strict update strictly reduces \(T_k\), and so there are at most \(n\) strict updates in any \(n\)-world model. This **general upper bound is previously established**; its inclusion fixes the quantity being optimized.

**Two-agent sharpness.** We prove by induction on \(k=0,\ldots,n\) that
\[
T_k=\{0,\ldots,n-k-1\},
\]
where the right-hand set is empty if \(k=n\). At \(k=0\), every world is a target because both equivalence relations are reflexive.

Fix \(k<n\) and assume the formula. For an even \(j<n-1\), the unique \(a\)-equivalent world of *opposite* \(p\)-value is \(j+1\). Thus the first disjunct of \(\varphi\) is true at \(j\) in \(M^k\) precisely when the arrow from \(j\) to \(j+1\) remains, which occurs precisely when \(j+1\in T_k\). For an odd \(j<n-1\), the analogous assertion holds for the \(b\)-pair \(\{j,j+1\}\) and the second disjunct. At the terminal world \(n-1\), whichever disjunct is relevant has no opposite-valued counterpart in that agent's equivalence class, so \(\varphi\) is false there at every stage. Every world has the other disjunct false by its \(p\)-value.

Consequently, among the currently active targets,
\[
T_k\cap\llbracket\varphi\rrbracket_{M^k}=\{0,\ldots,n-k-2\}.
\]
The target recurrence gives the induction step, with \(T_{k+1}\subsetneq T_k\). Hence every stage \(0,\ldots,n-1\) changes at least one relation; at \(k=n\) no targets or arrows remain, so \(M^n=M^{n+1}\). All initial equivalence classes have size at most two by construction.

**One-agent comparison: upper bound.** Partition the initial \(\mathsf{S5}\) frame into equivalence blocks \(B\). Within any block, every world has the same successor set \(B\cap T_k\) after each belief update. By induction on the syntax of every formula, worlds of the same \(r\)-bit valuation type in \(B\) agree on all formulas at each stage. Thus each strict update within \(B\) deletes every active target of at least one entire valuation type. There are at most \(2^r\) types. Moreover, once a block undergoes no change, its local model and the truth of the fixed announcement formula never change again, so it cannot start changing later. Each block therefore stops by stage \(2^r\); the entire model stops by stage \(2^r\), and also by stage \(n\). This specializes the type-deletion argument of Yamada, Lemma 6, and the general state-count bound.

**One-agent comparison: attainability.** Let \(m=\min\{n,2^r\}\). Choose \(m\) pairwise distinct \(r\)-bit valuations, described by mutually exclusive complete Boolean literals \(q_0,\ldots,q_{m-1}\); assign those types to the \(n\) worlds, repeating the first type if necessary. Take the universal \(\mathsf{S5}\) relation, and announce
\[
\psi_m=\bigvee_{j=0}^{m-2}(q_j\wedge\Diamond q_{j+1}),
\]
interpreting an empty disjunction as \(\bot\). The active targets initially realize exactly the types \(q_0,\ldots,q_{m-1}\). At the first update, exactly the last type disappears; subsequently the largest remaining type disappears at each update, because each \(q_j\)-world satisfies \(\psi_m\) if and only if a \(q_{j+1}\)-world is still accessible. Exactly \(m\) strict updates occur. Together with the upper bound, this proves the exact one-agent maximum.

## Verification

The independent set-based finite checker `verify.py` constructs the two initial equivalence relations, tests reflexivity, symmetry and transitivity, evaluates the displayed two-agent formula from the *actual current relations*, and checks the exact active-target sequence and strictness for every size \(1\le n\le100\). It separately tests the one-agent bit-type construction for \(0\le r\le4\) and \(1\le n\le30\), including the degenerate empty-disjunction case. Its output is provided only as finite corroboration; the proofs above establish the unbounded claims.

Run: `python3 verify.py` (standard Python 3, no dependencies).

## Relationship to prior work

Yamada [1, Definition 5] supplies the believed-public-announcement semantics. His Lemma 6 proves a finite single-agent \(\mathsf{K45}\) stabilization mechanism by deleting entire propositional valuation types. It supplies the **upper-bound principle** in the one-agent comparison; we do not claim that principle as new. His multi-agent constructions in Section 4 allow non-reflexive \(\mathsf{K45}\) relations and richer formulas and study eventuality rather than the minimal resources needed for the sharp finite lifetime.

An existing published result [2] proves the general active-target upper bound \(|W|\) and realizes it by a **directed one-agent cycle**, which is not an \(\mathsf{S5}\) frame. It explicitly does not establish sharpness under \(\mathsf{S5}\) or \(\mathsf{K45}\) initial restrictions. The new point here is that a fixed one-letter two-agent formula reaches that bound on initially \(\mathsf{S5}\) frames whose equivalence classes each have at most two worlds. The exact one-agent resource contrast quantifies the role of a second agent.

Yamada [3] treats truth-value patterns and \(\sigma\)-validity in multi-agent \(\mathsf{S5}\), including constructions whose formulas and propositional-type vocabularies depend on the target pattern length. Its inspected statements do not give the present fixed-formula, one-letter, size-\(n\) sharpness construction. General repeated-announcement phenomena and valuation-type reasoning are prior art, not claimed as discoveries here.

## Limitations

The \(\mathsf{S5}\) condition is imposed on the **initial** model only: a believed announcement deletes arrows and need not preserve reflexivity or symmetry. This is not a theorem about ordinary world-deleting public announcements or about requiring all intermediate models to remain \(\mathsf{S5}\).

The two-agent construction proves sufficient resources and a sharp lifetime, not uniqueness or classification of all maximizing models or formulas. It uses precisely the specified fixed depth-one formula and an alternating pair structure. The argument does not claim any new general finite-state upper bound. Historical originality is assessed relative to inspected primary and indexed literature and is not an independent priority certification.

## References

[1] Eiji Yamada, *Eventual and Strong Eventual Notions in Public Announcements*, arXiv:2609.24006v1, first posted 2026-09-21. Definition 5, Proposition 3, Lemma 6, and Section 4. https://arxiv.org/abs/2609.24006

[2] *Sharp state-count stabilization bound for finite believed announcements*, published research record (2026-10), identifier `2026/10/4/SCOPE-sharp-state-count-stabilization-bound-for-finite-believed-announ--65b4b662c65e`. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-state-count-stabilization-bound-for-finite-believed-announ--65b4b662c65e

[3] Eiji Yamada, *Classification of σ-validity in iterated announcements*, arXiv:2607.04685, first posted 2026-07-06. Sections 3 and 4. https://arxiv.org/abs/2607.04685
