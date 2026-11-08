# Scientific review

## Correctness — PASS

The proof begins with the actual homogeneous polynomial and computes all its partial derivatives, fixing the unique singular point and tangent line. It gives a polynomial inverse for the affine normalization and invokes only the elementary classification of automorphisms of the one-variable polynomial ring. The corresponding affine-projective matrix has all coefficients determined by comparison of five *distinct* monomials (the hypothesis \(n\ge2\) is essential here). A direct substitution proves the converse. Finite-field rational-point and minimal-extension statements follow from elementary cyclic-field arithmetic and the multiplicative order calculation. `verify.py` independently replays polynomial identities at five degrees and exact finite-field actions in three fields. Finite tests are corroboration, not a substitute for the universal proof.

## Originality — PASS, provisional historical priority

Kollár's motivating full text constructs the curve and analyzes its singularity but does not give its full projective stabilizer or rational-versus-geometric symmetry gap. Hemmig (2019) studies projective equivalence of complements, not this stabilizer of an embedded positive-characteristic curve. Search comparisons of abstract automorphism groups, plane-curve stabilizers, the explicit equation and the specific polynomial embedding produced no equivalent statement in the inspected sources. Closest research-record hits concern projectively unrelated complex cuspidal quintics and a Halphen curve. Classical work on nonstandard characteristic-two affine-line embeddings may still contain an implicit equivalent formulation; full historical priority is not guaranteed.

## Mathematical value — PASS

For a family introduced to exhibit exceptional large-degree cuspidal geometry in small characteristic, the theorem completely determines embedding-preserving symmetries and a sharp arithmetic descent phenomenon: the \(\mathbb F_2\) stabilizer is trivial while the geometric group grows without bound. This comparison distinguishes the intrinsic affine-line normalization from its particular plane realization, provides full-group and field-of-definition invariants, and is structurally more informative than a low-degree numerical exercise.

## Scope and residual risk

The result concerns only ordinary projective stabilizer groups of field-valued points. Automorphism group schemes in characteristic two and nonprojective birational automorphisms are not calculated. The exact 2026 motivating family and complement-isomorphism literature have been checked, but older embedding-classification literature cannot be exhaustively ruled out as implicit coverage. External independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
