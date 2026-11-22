# Scientific review: simultaneous avoidance of binary two- and three-step squares

## Correctness

**PASS.** The definition uses bi-infinite periodic extensions, so short circumferences are not exempt from the six-window test. The 32-state local transition predicate is explicit, and the complete recurrent component has 16 states. Complementary pairing yields two eight-state matrices whose exact determinants are written out in the proof. Matrix-trace and Möbius inversion give all marked- and primitive-orbit counts. The absent periods are proved from exact low-degree counts, and the unbounded existence assertion from three explicit, simple rooted return loops and primitive return-length itineraries. The graph has cycles of coprime lengths four and five, ensuring primitive Perron behavior. Both packaged verification programs ran successfully. The finite checks alone are not presented as proofs of infinitely many periods.

## Originality

**PASS, with historical-priority risk.** Richard and Grimm's 2003/2004 full text concerns ternary words avoiding **all** squares through a prescribed half-length, including half-length one. Grimm and Heuer's 2008 article reviews finite-forbidden-language transfer methods and different binary cubefree/ternary squarefree families. Mousavi and Shallit's 2012 full-text exposition treats an exponent threshold applied to circularizations of all factors, not this pair of forbidden fixed square lengths. A previously registered result for length-six squares alone does not imply the intersection language: excluding additional four-letter squares changes the admissible graph and exact orbit counts. Registered studies of antisquare or other pseudo-period shifts likewise use different local predicates. The numerical Perron root is present as a ratio in OEIS A225490, but the entry records an unrelated rational coefficient series, not these periodic orbits or their primitive-period support. Web and mathematical-record queries found no direct implication or covering table. These searches cannot rule out unindexed older computations.

## Value

**PASS.** This is not merely a finite numerical evaluation: a concrete first coupled fixed-square-period system admits an all-circumference rational zeta identity and a complete least-period classification, including the nonobvious lack of primitive cycles at circumferences eight and twelve despite admissible circles of those lengths. The compact complement-signed determinant quotient explains the two sextic factors, and the explicit return-loop argument independently explains eventual period abundance. These are natural symbolic-dynamics invariants of a repetition-avoidance language that is different from the existing single-period restriction. Standard transfer-matrix technology is not claimed as novel; the actual restricted system, complete factorization and period boundary are the specific contributions.

## Closest literature and limitations

- C. Richard and U. Grimm, *On the Entropy and Letter Frequencies of Ternary Square-Free Words* (arXiv:math/0302302, 2003; 2004 publication): inspected introduction and generating-function section; different alphabet and includes half-length-one exclusion.
- U. Grimm and M. Heuer, *On the Entropy and Letter Frequencies of Powerfree Words* (2008): inspected transfer-matrix and finite-forbidden-language discussion; no exact coupled binary periodic-orbit formula.
- H. Mousavi and J. Shallit, *Repetition Avoidance in Circular Factors* (2012): inspected definition and binary-case theorem; its circularization-of-every-factor restriction is not equivalent.
- OEIS A225490: the same algebraic growth ratio occurs without an identification of the binary square-avoidance language.

The scope does not concern squares of half-length one, complete square avoidance or any larger alphabet. External unindexed tables and equivalent automata remain a historical-priority risk. The review is not an independent audit.

Self-review: passed. Independent audit: not yet performed.
