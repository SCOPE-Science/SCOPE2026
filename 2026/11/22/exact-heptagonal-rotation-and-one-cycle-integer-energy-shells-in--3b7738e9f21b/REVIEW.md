# Self-review

## Correctness — PASS

The assertion is a single all-parameter theorem for a fixed two-season piecewise-integral map. The rational invariant is an explicit algebraic identity for the two-step positive Lyness map, checked by symbolic cancellation; its tropical logarithmic limit proves the global invariant. The eight affine terms determine all seven polygon edges for every real level strictly above three, and their primitive lengths give the claimed circumference. Each piece of the update has unimodular linear part and the global map is orientation-preserving, so the induced circle isometry is a rigid rotation; the computed image of the first vertex fixes its exact shift. The integer-shell orbit count follows from a Bézout identity and the separate central seven-state enumeration. No probabilistic computation, sampled trajectory or finite cutoff is substituted for the general proof. The SymPy-backed exact checker and lattice/edge enumerations replay successfully.

## Originality — PASS, with historical-priority qualification

The closest directly relevant paper is Cima–Gasull–Mañosa (2009; arXiv:0912.5031), which proves invariance and rotation properties for positive *rational* two-periodic Lyness recurrences. Its formulas motivate the tropical limit but do not state the exact two-threshold heptagonal rotation law or the integer-shell transitivity. De Angelis (2004) studies an autonomous one-threshold max recurrence; its full available paper treats the single map throughout. Takahashi–Iwao (2007) develops a different autonomous piecewise-linear map. The published result *Exact action-twist and Pareto rotation spectrum of a max-plus QRT map* uses an octagonal autonomous map and a different normalized rotation law; it is not a covering claim. The published *Global periodicity and exact cycle multiplicities for unit-gap nonlinear lattice rotations* uses a sign-driven affine lattice map with different dynamics and cycle-length spectrum.

A direct algebraic relationship between rotation fractions for differently normalized autonomous maps would not, without a map conjugacy respecting the full integer lattice, imply the alternating system's phase portrait or the one-orbit-per-energy theorem. Search failures do not prove priority. The full 1998 Grove–Kent–Ladas nonautonomous max-equation article was not obtained and is an explicit residual risk, as is unindexed equivalent work.

## Value — PASS

Alternating forcing is a natural minimal departure from the well-studied autonomous Lyness max map and the two-periodic rational Lyness equation. The precise questions are whether an exact polygonal circle action survives, what its full rotation law is, and whether integer points split into multiple cycles on a fixed conserved level. The answer gives an all-level strict twist together with a rigid, arithmetic *single-cycle-per-shell* law for the entire integer lattice; it also distinguishes the genuinely flat central real level from the uniform exterior polygonal dynamics. These global structural properties are not merely a recomputation of a known periodic table or an arbitrary finite slice.

## Verification limits and closest literature

The packaged rational sample and integer-shell experiments are controls, not infinite certificates. The proof handles all real outer levels and all integer initial states, but not arbitrary alternating threshold pairs or real interior dynamics at the minimal level. Bibliography and precise implication comparisons appear in `RESULT.md` and `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
