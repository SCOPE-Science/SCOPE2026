# Scientific review: two-term Magnus positivity on reverse pure-birth cascades

## Correctness — PASS

The Markov row-generator and chronological right-action conventions are stated. Direct commutator multiplication yields the displayed upper triangular four-state Magnus logarithm. Its first three columns follow from the nilpotent part of a repeated-eigenvalue block, while row-sum conservation forces the final column. All entries except one are manifestly nonnegative; the remaining entry has derivative \(e^{-h}h^2(h^2-8)/8\), giving a unique strictly positive root, exact global sign classification, and sharp minimum. The higher-dimensional \(-a_1a_2a_3h^3/3\) coefficient is checked by direct path counting in the power-series exponential; the lower-order coefficient vanishes. Independently coded exact-rational and high-precision tests passed 674 assertions. No numerical enumeration is used to prove the universal statements.

## Originality — PASS, with residual literature risk

Iserles–Macnamara (arXiv:1701.02522, Section 4.5) already state the general non-preservation of positivity by truncated Magnus expansions and the non-Markov character of commutators. Blanes–Iserles–Macnamara (arXiv:2102.08242, Sections 3.3/3.5) cover the same broad obstruction and alternative positive integrators; Jasuja–Atzberger (arXiv:2212.08978) address a different stochastic-structure setting. None of these inspected discussions establishes the specific four-state recovery interval, exact extremal negative probability, or dimension-uniform cubic reverse-cascade obstruction. Earlier general negativity is not rebranded as new. Other specialized Markov, chronological exponential, or Magnus literature may contain equivalent results and remains a genuine publication-priority risk.

## Value — PASS

Mass preservation alone is insufficient for probability interpretation. This natural smallest equal-rate reverse-cascade witness identifies the complete set of pulse masses where the two-term Magnus approximation can be interpreted as a Markov transition matrix, including a counterintuitive recovery of positivity at large pulse mass where approximation error is pronounced. Its exact cubic rate law quantifies why reducing pulse magnitudes does not repair positivity across longer cascades. These are reproducible structural benchmarks for geometric integration and positivity safeguards, not an arbitrary slice or an unproved claim of practical accuracy.

## Scope and reservations

The if-and-only-if positive interval is specific to four equal-rate reverse-ordered pure-birth pulses. Higher-dimensional results concern sufficiently small positive total rates only. Pulse supports must be disjoint and in the prescribed order; the rate shapes may be smooth. Publication priority is provisional pending broader specialized search. No external or independent audit is represented.

Self-review: passed. Independent audit: not yet performed.
