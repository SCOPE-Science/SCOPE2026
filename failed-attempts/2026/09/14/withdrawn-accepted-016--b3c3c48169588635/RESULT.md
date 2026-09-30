# Lone-axis dichotomy of a→b, b→ca, c→d, d→a in Out(F4): reducible and toroidal

## Context

Let F4 = F(a,b,c,d). Let Φ2 be the endomorphism a↦b, b↦ca, c↦d, d↦a and φ2 = [Φ2] ∈ Out(F4). The admitted target asks whether φ2 is fully irreducible, atoroidal, and ageometric, and asks for the Mosher–Pfaff lone-axis dichotomy for its Handel–Mosher axis bundle in CV4: whether the ideal Whitehead graph IW(φ2) is connected with no cut vertex (unique periodic fold line) or otherwise. The target expressly accepts a concrete witness — reduction, periodic conjugacy class, Nielsen path, or separating vertex — refuting the claimed alternative as a complete answer.

## Definitions

- Fully irreducible (iwip): no positive power preserves the conjugacy class of any proper free-factor system.
- Atoroidal: no nontrivial conjugacy class is periodic; toroidal means some [w] ≠ 1 satisfies φ^k([w]) = [w] for some k ≥ 1.
- Ageometric iwip and IW(φ)/lone-axis dichotomy (Bestvina–Handel; Handel–Mosher; Mosher–Pfaff) are theories of fully irreducible, resp. atoroidal ageometric, automorphisms: unique periodic fold line iff IW is connected with no cut vertex.

## Result

φ2 is reducible and toroidal, hence neither fully irreducible nor atoroidal nor an ageometric iwip. The Mosher–Pfaff lone-axis / IW cut-vertex dichotomy therefore has vacuous premise and no IW verdict is owed.

Precisely: A = ⟨a,c⟩ and B = ⟨b,d⟩ are complementary rank-2 free factors with F4 = A ∗ B, Φ2(A) = B and Φ2(B) = A, so φ2 swaps {[A],[B]} and φ2² fixes each. And w = [a,c] = acAC satisfies the tightened orbit acAC → bdBD → caCA → dbDB → acAC under Φ2, so φ2⁴([w]) = [w] with [w] ≠ 1.

## Proof / evidence

1. Φ2 is an automorphism. Ψ(a)=d, Ψ(b)=a, Ψ(c)=bD, Ψ(d)=c satisfies Ψ∘Φ2 = id and Φ2∘Ψ = id on generators (only length-2 cancellations Dd and aA occur). Hence φ2 ∈ Out(F4).
2. Reduction. Images are positive words: Φ2(a)=b, Φ2(c)=d ∈ B gives Φ2(A) ⊆ B; Φ2(b)=ca, Φ2(d)=a ∈ A gives Φ2(B) ⊆ A. Generation both ways gives equality: b=Φ2(a), d=Φ2(c) generate B; a=Φ2(d) and c=(ca)a⁻¹ ∈ Φ2(B) generate A. Explicitly Φ2²(a)=ca, Φ2²(c)=a generate A and Φ2²(b)=db, Φ2²(d)=b generate B. Thus φ2{[A],[B]} = {[A],[B]}, φ2²[A]=[A], φ2²[B]=[B]: a period-2 proper free-factor system. So φ2 is reducible, not fully irreducible. Corroboration: with M_{e,e′} = #(e in f(e′)) in order (a,b,c,d), M² reordered to (a,c,b,d) is block-diagonal with two [[1,1],[1,0]] blocks.
3. Periodic class. Tightening after each application: Φ2(acAC)=bdBD (reduced); Φ2² gives ca·a·AC·A = caCA; Φ2³ gives dbDB (reduced); Φ2⁴ gives a·ca·A·AC = acAC. Each intermediate word is reduced; only the two indicated aA cancellations occur. Cyclically reduced representatives are pairwise distinct up to rotation, so [w] ≠ 1 has period dividing 4. Hence φ2 is toroidal, not atoroidal.
4. Consequence. Since the irreducibility and atoroidality premises fail, φ2 is not an ageometric fully irreducible atoroidal automorphism and there is no Handel–Mosher IW(φ2)/lone-axis dichotomy to decide.

All identities are positive-word or single-cancellation computations, hand-checkable and machine-checked.

## Limitations

Decided through refuting witnesses (reduction plus periodic class) rather than an IW computation; no Nielsen-path survey or Whitehead-graph computation is included. No claim is made about exact minimal periods beyond the exhibited orbit data dividing 4 and the period-2 factor swap.

## Reproducibility

Run `python3 output/artifacts/verify_phi2.py` (copied from inputs/artifacts/verify_phi2.py): checks the two-sided inverse on all eight oriented edges, the factor swap and squares, the full commutator orbit, and the M² block-diagonal form. All assertions pass.

## References

- M. Bestvina, M. Handel, Train tracks and automorphisms of free groups, Ann. of Math. 1992.
- M. Handel, L. Mosher, Axes in Outer Space, Mem. Amer. Math. Soc. 2011.
- L. Mosher, C. Pfaff, Lone axes in outer space, Algebr. Geom. Topol. 16 (2016), 3385–3418.
- C. Pfaff, Ideal Whitehead Graphs in Out(Fr) IV, arXiv:1511.08933.
