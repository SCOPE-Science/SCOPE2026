# Scientific review: diamond preconditional isomorphism spectrum

## Correctness — PASS
The proof starts from the five explicit preconditional axioms, derives the forced bottom/top/atom-row forms, and checks the only surviving (P5) restrictions. It separates the three possible bottom values without double counting. For the top-bottom-row case, the four marked terminal forms and arrows to a *different* atom provide a bijective functional-digraph encoding. A permutation cycle of length \(d\) has exactly \(3+\sum_{e\mid d}e c_e\) equivariant choices, yielding the stated Burnside formula. The unlabelled multiset decomposition and the classical Otter-root singularity produce the given generating function and square-root-pole asymptotic. Both packaged checkers executed successfully and agree on the first nine reported sizes. The infinite statements rest on proofs, not finite checks.

## Originality — PASS within inspected literature
The labeled row normal form, including the exact labeled count \((m+3)^m+2^m+2m3^{m-1}\), is a prior ingredient and is excluded from the novelty claim. Holliday's preconditional axiomatization and Chen's recent logical extensions are also prior work. The new object is the **isomorphism quotient** under all atom permutations: the orbit formula, the four-colored functional-graph correspondence, the component generating function, and the exact \(\rho^{-m}m^{-1/2}\) growth exponent and coefficient. Comparisons against relevant algebraic-logical literature and exact-index searches did not uncover this quotient classification. Routine uses of Burnside, Pólya and Otter are acknowledged, not relabeled as original lemmas. An unindexed or not-yet-accessible equivalent classification remains a priority risk.

## Value — PASS
Isomorphism classification is the natural structural refinement of a labeled model count: it measures genuinely distinct algebraic semantics, not presentations obtained merely by naming atoms differently. The theorem gives an all-sizes exact spectrum and a canonical decomposition into four-colored termination trees and directed-cycle components; the asymptotic exponent further describes the distribution of the entire family, not an arbitrary small-case numerical improvement. The result provides natural combinatorial infrastructure for studying subclasses of these preconditionals. No assertion is made about other lattices or stronger axioms.

## Limits and closest sources
Holliday (2024), *Preconditionals*, defines the five axioms. Chen (2026), *Fundamental Propositional Logic with Preconditional*, connects the class to \(\mathsf K\), \(\mathsf T\) and \(\mathsf F\) logics. The labeled finite-diamond normal form and classical rooted-tree singularity are explicitly treated as known inputs. External independent checking of the claimed novelty and of the proof has not been performed. The finite checkers cover only their stated ranges.

Self-review: passed. Independent audit: not yet performed.
