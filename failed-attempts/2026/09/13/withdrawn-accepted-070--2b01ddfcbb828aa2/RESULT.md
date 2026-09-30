# Morita Non-Equivalence of the Schanuel Topos and the DLO Classifying Topos

## Context

Let T_inf be the countable coherent single-sorted theory of an infinite decidable set: sort X, equality, and a binary apartness relation # with sequents x=y ∧ x#y ⊢ ⊥, ⊤ ⊢ x=y ∨ x#y, and for each n ≥ 1, ⊤ ⊢ ∃x_1…x_n ⋀_{i<j} x_i#x_j. Its classifying topos E_inf = Sh(C_inf, J_inf) is the Schanuel topos. Let T_dlo be the countable coherent theory of dense linear orders without endpoints in {<} with irreflexivity, transitivity, linearity, density, and no endpoints. Its classifying topos is E_dlo = Sh(C_dlo, J_dlo). Two coherent theories are Morita equivalent iff their classifying toposes are equivalent as Grothendieck toposes. The target asks whether E_inf ≃ E_dlo, computing the ledger L1: Booleanness, atomicity, two-valuedness/connectedness, and the topological automorphism groups of the countable homogeneous universal models with orbit counts.

## Definitions

A Set-point of a classifying topos of a coherent theory T bijects with a Set-model of T (Diaconescu / Makkai–Reyes). The point groupoid Pt(E) has Set-points as objects and natural isomorphisms as arrows; a topos equivalence induces a groupoid equivalence, hence isomorphisms on each vertex group Aut(p). Define P_2(E): every Set-point p of E has an element of order 2 in Aut(p). This is invariant under topos equivalence. Both theories are ℵ_0-categorical with countable homogeneous universal models ℕ (pure set) and (ℚ,<); the relevant groups with pointwise-convergence topology are S_∞ = Sym(ℕ) and Aut(ℚ,<), with open subgroups the finite-tuple stabilizers.

## Result

Both E_inf and E_dlo are Boolean, atomic, two-valued, and connected, so those entries do not separate them. The separating invariant is P_2: it holds for E_inf and fails for E_dlo. Ledger: Aut groups S_∞ versus Aut(ℚ,<); orbits on n-tuples for n = 0,1,2,3,4 are Bell 1,1,2,5,15 versus ordered Bell 1,1,3,13,75, differing already at n = 2 (2 vs 3). Therefore E_inf ≄ E_dlo as Grothendieck toposes, so T_inf and T_dlo are Morita inequivalent.

## Proof / Evidence

Lemma 1 (Schanuel side): every Set-point of E_inf has 2-torsion. A point is an infinite set M; pick distinct a ≠ b and take the transposition swapping a,b and fixing the rest. It is a model automorphism of order exactly 2 preserving # = ≠.

Lemma 2 (DLO side): no Set-point of E_dlo has 2-torsion. Let (M,<) be any dense linear order without endpoints and σ ∈ Aut(M,<) with σ² = id. If σ(x) ≠ x for some x, then either x < σ(x) or σ(x) < x. In the first case applying the strict order-embedding σ gives σ(x) < σ²(x) = x, contradicting x < σ(x) by asymmetry; the second case follows by applying the same to σ⁻¹ = σ. Hence σ = id, so Aut(M,<) is torsion-free at every cardinality, countable or uncountable.

Theorem: if E_inf ≃ E_dlo, the induced point-groupoid equivalence would preserve P_2, contradicting Lemmas 1–2. Hence the toposes are not equivalent. Independently, S_∞ orbits on ℕ^n biject with set partitions (Bell numbers) while Aut(ℚ,<) orbits on ℚ^n biject with weak total orders (ordered Bell / Fubini numbers) by ultrahomogeneity of (ℚ,<); at n = 2 the patterns are {x=y, x≠y} versus {x<y, x=y, x>y}. The script artifacts/orbit_counts.py brute-force-enumerates both families for n ≤ 5 and checks the recurrences, confirming the sequences and the n = 2 split.

## Limitations

Relies on standard classifying-topos existence and points-as-models correspondence for countable coherent theories (Makkai–Reyes / Johnstone, Elephant D3, C3). The Cont(G) identifications are quoted for ledger context (open subgroups as finite-tuple stabilizers via QE and ultrahomogeneity); the separating proof uses only points-as-models plus point-groupoid functoriality. Orbit counts are machine-checked for n ≤ 5 and extended by textbook recurrences. The completeness/quantifier-elimination background for T_inf and T_dlo is standard.

## Reproducibility

Run `python3 artifacts/orbit_counts.py`; expected output confirms Bell = [1,1,2,5,15,52] and ordered Bell = [1,1,3,13,75,541] for n = 0…5 with the n = 2 separation 2 vs 3. Lemmas 1–2 are self-contained combinatorial checks: exhibit a transposition on any infinite set, and apply strict monotonicity plus σ² = id on any linear order.

## References

P. T. Johnstone, Sketches of an Elephant, vols. 1–2. M. Makkai and G. Reyes, First Order Categorical Logic. W. Hodges, Model Theory (QE for DLO, ℵ_0-categoricity, ultrahomogeneity). S. Mac Lane and I. Moerdijk, Sheaves in Geometry and Logic, Ch. VII–VIII. O. Caramello, Atomic toposes and countable categoricity, arXiv:0811.3547. J. Marquès, Atomic toposes with co-well-founded categories of atoms, arXiv:2406.14346. nLab, Schanuel topos.
