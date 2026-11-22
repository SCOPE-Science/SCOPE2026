# Scientific review

## Correctness

**PASS.** The point profile is exhaustively determined by either a visible exact permutation period of length at most \(d\), plus its cyclic color word, or a no-repeat window of \(d+1\) colors. Short cycle necklaces are necessary and pairwise non-substitutable. Every no-repeat word requires a separate long vertex, giving the stated lower bound. A de Bruijn cycle realizes all long profiles at equality. Equality at the bound forces exactly one copy of each short necklace and exactly one occurrence of every long window. The resulting arc labeling bijects all optimizers with short-cycle-free de Bruijn transition systems, and inclusion–exclusion correctly counts those systems: a short arc-permutation cycle cannot revisit a length-\(d\) de Bruijn state without repeating an arc word, hence it projects to a simple graph cycle. The automorphism count follows from independent rotations of forced short components and rigidity of the long component(s). The standalone finite verifier returned `VERIFY_OK 25`.

## Originality

**PASS within inspected evidence.** The exact universal colored-permutation minimum and the all-optima circuit-partition census were not located in the inspected primary sources or targeted database searches. The strongest overlaps are the established unary forward-profile framework, de Bruijn Euler tours, and colored permutation necklace enumerations. These do not directly determine all minimum models: already at binary depth two there are three minimum models, but only two long one-cycle de Bruijn words. General inclusion–exclusion is acknowledged as a method; its specialization to the logical optimization problem and the resulting exact structural classification are the assessed contribution. Potential pre-existing special-case circuit-partition enumerations remain a historical-priority risk.

## Value

**PASS.** This supplies the optimal *single-model witness budget* for all bounded-depth one-point types of a natural finite permutation language, rather than only counting individual types. The full extremal classification explains why constructions based solely on a single de Bruijn cycle miss valid optimum structures. The exact finite census and automorphism factor make the constrained resource invariant reproducible and distinguishable from classical cyclic-word counts.

## Boundaries and closest literature

Kuželka (2026) treats all endofunctions and profile compatibility for model counting, not this exact saturation optimization. Sawada and Gabrić (2025) develop universal-cycle generation, not optimal multi-cycle colored-permutation realization. Earlier colored-cycle and circuit-partition theory can overlap with ingredients, so absence of a located identical theorem is not proof of global novelty. The result does not extend to transient orbits, deeper first-order quantifiers, or uncolored palette size one.

Self-review: passed. Independent audit: not yet performed.
