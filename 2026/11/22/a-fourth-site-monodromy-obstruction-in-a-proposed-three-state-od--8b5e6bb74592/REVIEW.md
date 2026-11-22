# Scientific review

## Correctness — PASS

The claim is exact for the synchronous, one-sided, fixed-left-boundary rule in Table 3 of Kamilya–Kari–Paturi (2026). Triangular conditional permutations make the finite prefix factors bijective; a cyclic base orbit lifts to a product with the explicit return monodromy. The finite words `012`, `010201122`, and `010112220201201011122020102` yield a three-cycle, a three-cycle, and the identity in the next-coordinate fiber. The full 27-state base orbit is listed in RESULT.md. Therefore the first three prefix factors are single cycles, whereas the fourth is precisely three 27-cycles. The nontransitivity of the infinite map then follows from three proper clopen invariant factor components. `check.py` independently exhausts all 81 four-symbol words and reproduces all monodromies; computation supports the exact finite certificate and is not used as a substitute for the clopen argument.

## Originality — PASS within inspected evidence

The motivating primary paper proves an odometer theorem only for its first rule (predecessor zero acts as the identity), then suggests but expressly does not prove odometer-like dynamics for the distinct rule in concluding Table 3. Its general qualitative results do not imply this explicit fourth-site failure, and the direct exact-source, alias, cocycle, and finite-factor searches did not identify a prior treatment of the precise table. The closest broader research records concern other finite CA rules, not this triangular ternary boundary rule. Negative search is not proof of world-wide novelty; historical priority remains a residual risk.

## Value — PASS

This is a motivated counterexample to a specific published candidate for a highly nontrivial minimal equicontinuous non-uniform cellular automaton. More than a trivial failed numerical iterate, it identifies the **sharp first finite-coordinate obstruction**, proves the complete three-orbit 81-state factor census and explains it by cancellation of a nonabelian permutation cocycle. The resulting clopen dynamical decomposition conclusively rules out even topological transitivity, distinguishing the suggested variant from the proven one and guiding future searches for uniform-boundary odometers.

## Scope and risks

The candidate was described as plausible rather than asserted as a theorem in the source. This calculation does not retract or alter the proven first odometer. It does not classify all higher finite factors or the entire minimal decomposition; no independent review or exhaustive historical-priority proof is available.

Self-review: passed. Independent audit: not yet performed.
