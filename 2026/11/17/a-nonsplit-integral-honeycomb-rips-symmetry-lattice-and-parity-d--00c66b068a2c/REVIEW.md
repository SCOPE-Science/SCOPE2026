# Scientific review

## Correctness — PASS

The relative chain complex of the Rips space modulo the centered tetrahedral subcomplex has precisely the \(2L^2\) alternating face triangles. The connecting boundary sends both colors to the same oriented facial cycle. Since the only integral relation on all facial cycles is their total sum, its kernel has exactly the claimed basis \(T,s_f\). Every symmetry acts on this basis with the stated sign and color-swap rules; the translation-and-rotation argument proves integral nonsplitting, while the reflection-and-rotation presentation yields the parity-sensitive Smith factors without extrapolating finite computations. Two independent finite checks test all local simplices and the full oriented relative cellular action, and exact Smith reductions corroborate the parity result. The listed finite examples are not used as a proof for infinitely many periods.

## Originality — PASS (qualified)

The closest published source is *Scale-two Vietoris–Rips complexes of periodic honeycomb graphs* (8 November 2026), fully read: it proves \(T^2\) wedged with one two-sphere per face and expressly does not determine the integral equivariant action. Its underlying homotopy computation does not imply the **nontrivial integral extension class**, the parity-dependent algebraic coinvariants, or the rational quotient statement. Decker–Zaremsky's 28 October 2026 paper concerns affine Coxeter groups and eventual or alternate-generator contractibility, not this low-scale finite torus symmetry action. Published honeycomb perfect-matching character results and square-grid Rips representations use different complexes and do not cover this one. Actual database and literature searches for aliases, symmetry modules and coinvariants found no dominating result. Unindexed or inaccessible work remains a nonzero priority risk, and search results cannot prove novelty absolutely.

## Mathematical value — PASS

The pre-existing homotopy description has \(L^2+1\) free second-homology generators but does not determine their integral symmetry action. The exact failure of integral splitting is a structural arithmetic invariant, and the odd/even transition in full-symmetry coinvariants is a natural qualitative phenomenon that rational Betti numbers cannot detect. This answers a specifically identified equivariant gap for every valid period, not an arbitrary finite enumeration.

## Verification and limits

Reproduce with `python3 verify.py` and `python3 verify_modules.py` (SymPy required for the latter). Integral actions are tested via all relative chain basis elements for periods five through eight; the theorem for all periods follows from the accompanying proof. The algebraic coinvariants are not asserted to equal integral homology of the geometric quotient. The literature comparison is subject to unindexed prior work.

Self-review: passed. Independent audit: not yet performed.
