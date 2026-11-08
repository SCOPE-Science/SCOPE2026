# Scientific review: exact quasiperiod spectra of three-marker binary words

## Correctness — PASS

The claim is a complete all-length theorem, not an extrapolation from experiments. Any proper cover of a three-one word contains exactly one or two ones. Aligning the first and last occurrences forces its length uniquely in each case. The one-one criterion requires the same zero run surrounding each marker and interval gaps at most the proposed cover length; the two-one criterion forces equal inner marker distances. A disjoint parameterization and one explicit intersection count prove all three rational generating functions and their leading asymptotics. Direct occurrence-by-occurrence enumeration through length 25 (14,950 words) and two independent coefficient implementations through degree 65 returned `VERIFY_OK`. Risk: incorrect manipulation of endpoint inequalities, addressed by proof of both directions and exhaustive independent endpoint testing.

## Originality — PASS (qualified)

The nearest primary works are Levé–Richomme's *On Quasiperiodic Morphisms* (arXiv:1304.6280, 2013) and Gamard–Richomme's *Determining Sets of Quasiperiods of Infinite Words* (MFCS 2016), which concern morphism behavior and infinite quasiperiod sets, respectively. The survey *Computing regularities in strings* discusses algorithmic discovery of covers; OEIS A320434 tabulates the unrestricted number of binary quasiperiodic words. These statements do not provide the fixed-three-marker complete inequalities, three-way count, rational functions, or limiting probability by specialization. Queries for the direct result and its aliases did not uncover a covering source. This is qualified by the possibility of an unindexed or implicit equivalent enumeration; absence in search is not proof of uniqueness.

## Value — PASS

Coverability is a standard notion of string repetitiveness. The first nontrivial fixed-content family allowing two distinct covers is three marked letters (with two, there can be at most one). Here all possibilities are structurally classified and the full count distribution is enumerated at every length; this also produces the non-obvious positive limiting quasiperiodic density \(1/90\) and decaying probability of two quasiperiods. The gap conditions and generating functions support comparisons of sparse-word cover algorithms and conditional random-word behavior. No claims about unrestricted words or four-marker patterns are made.

## Scope and risks

The result applies to labeled linear binary words with exactly three ones and proper covers only. It is not a uniqueness claim against all potentially unpublished or unindexed results. Independent mathematical audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
