# Morita Non-Equivalence of Symmetric Irreflexive Graphs vs Equivalence Relations via the Sentence Lattice Sub(1)

## Context

Let T_gra be the countable coherent single-sorted theory of symmetric irreflexive graphs in signature {E} with axioms E(x,y) |- E(y,x) and E(x,x) |- bot, and T_eq the countable coherent single-sorted theory of equivalence relations in signature {R} with axioms top |- R(x,x), R(x,y) |- R(y,x), R(x,y) /\ R(y,z) |- R(x,z). Write C_T for the countable coherent syntactic site, J_T for the coherent coverage, and E_T = Sh(C_T, J_T) for the classifying topos, with universal model U_T. Theories are Morita equivalent iff their classifying toposes are equivalent as categories. The admitted target asked for a separating ledger L4 or an explicit Morita equivalence (resolutions (a)/(b)).

## Definitions

Geometric sentences are (possibly infinitary) disjunctions of regular sentences exists xbar. C(xbar) with C a finite conjunction of atoms and equalities. Each geometric sentence phi determines a subterminal object [phi] in the classifying topos, with [phi] <= [psi] iff T |- phi -> psi geometrically; conversely every subobject of 1 arises this way. Sub(1) is a bare-topos invariant: any equivalence sends 1 to 1 and subobject lattices to isomorphic lattices. Define Gamma_n := exists x_1..x_n. /\_ {i<j} (E(x_i,x_j) /\ E(x_j,x_i)) with Gamma_0 := top, and Inhab := exists x. top.

## Result

|Sub(1_eq)| = 3, namely {bot < Inhab < top}, while Sub(1_gra) is countably infinite (it contains the pairwise-separated clique sentences Gamma_n). Hence E_gra is not equivalent to E_eq: T_gra and T_eq are Morita-inequivalent (target resolution (b)).

Ledger L4: (i) atomicity of E_T: open on both sides, not used; (ii) presheaf type: open on both sides, not used (an earlier universal-Horn/free-amalgam argument was withdrawn); (iii) Sub(1): countably infinite for graphs vs exactly 3 for equivalence relations -- SEPARATES; (iv) Sub(U^2) for canonical universals: infinite for graphs (walk formulae P_k pairwise separated on paths; [E] vs [x=y] incomparable) vs collapsed bottom chain bot < [x=y] < [R] < top for equivalence relations (ledger-level, universal-relative, not a bare-topos invariant); (v) enough points: yes on both sides (Deligne for coherent toposes), non-separating; (vi) connectedness: yes on both sides (proved via empty-model characterization), non-separating.

## Proof / Evidence

Invariance: Sub(1) depends only on the terminal object, unique up to unique isomorphism, so it is preserved by any equivalence.

Equivalence relations (exactly three sentences): every disjunct exists xbar. C reduces as follows. Eliminate equalities between distinct variables by substitution. If no variables remain, the disjunct is top (no constants exist). If variables remain, every diagonal R-atom is provable by reflexivity, and mapping all variables to one fresh z sends every off-diagonal R-atom to provable R(z,z); hence the disjunct entails and is entailed by exists z. top. A nonempty conjunction of R-atoms and equalities is satisfiable (one-point model with R = {(pt,pt)} after identifying equal variables), hence consistent with the universal Horn axioms and not bot by coherent completeness; the only contradiction is the empty disjunction bot. So every sentence is bot, top, or Inhab. The empty model satisfies only top; the singleton satisfies all but bot, so the three are pairwise separated and Sub(1_eq) is the 3-chain.

Graphs (infinitely many sentences): K_m |= Gamma_n iff m >= n. If m >= n, distinct vertices witness the quantifiers; conversely a witness tuple with a_i = a_j for i != j refutes E(a_i,a_j) by irreflexivity, so witnesses are pairwise distinct and need m >= n. Hence K_n |= Gamma_n but K_n |/= Gamma_{n+1}: the Gamma_n are pairwise inequivalent, Gamma_{n+1} |- Gamma_n strictly, and Sub(1_gra) is infinite.

Corroboration: stdlib-only verify_ledger.py checks clique truth tables (m,n <= 6), walk separations on paths (Boolean matrix powers), exhaustive 2-variable eqrel existential-pattern collapse to exactly 3 sentence patterns, Sub(U^2) bottom patterns, and embedding-span bounds: ALL CHECKS PASSED (finite-machine corroboration of lemmas proved analytically above).

Connectedness: a geometric sentence in either constants-free signature true in the empty structure is provably top (some disjunct must hold with empty variable tuple, hence is the empty conjunction top). For graphs this forces any complemented decomposition of 1 to be trivial; for equivalence relations Sub(1) is the 3-chain whose only complemented pair is {bot,top}.

## Limitations

Atomicity and presheaf-type rows are explicitly open; nothing in the separation depends on them. Sub(1_gra) is bounded below (infinite) rather than fully classified. Sub(U^2) comparison is data for the canonical universals, not a bare-topos invariant. Enough-points uses Deligne; no literature search underlies the self-contained argument.

## Reproducibility

Run `python3 output/artifacts/verify_ledger.py` (stdlib only; expects ALL CHECKS PASSED). Recorded output in `output/artifacts/verify_ledger_output.json`.

## References

P. T. Johnstone, Sketches of an Elephant, Part D (coherent classifying toposes, syntactic sites, Deligne); O. Caramello, Theories, Sites, Toposes and unification via topos theory (Morita-equivalence, presheaf-type theories, invariants).
