# Self-review

## Correctness — PASS

The rooted-even-offspring determinant and inverse-root-entry lemma is proved by induction using Schur complements. Exactly two even-degree vertices make every spine vertex carry an odd number of healthy side branches, which gives the uniform reduced tridiagonal matrix. Its determinant, cyclic presentation, equivalence with the reversible path-wave module, and exact order/fixed-space populations are deduced algebraically, including all boundary cases with distance at least one. The general theorem is not inferred from finite experiments. Independent program implementations verified the characteristic polynomial for 102548 labelled trees and finite-field fixed populations for 96 additional trees, with exact direct state checks on 5440 inputs.

## Originality — PASS, qualified

Primary comparisons include the 2005 full paper on general tree characteristic polynomials by Jacobs, Machado and Trevisan; the full revised arXiv article by Akın on linear automata on homogeneous Cayley trees; and the published abstract of Macfarlane's 2004 second-order reversible cellular automata. A general determinant algorithm, a one-dimensional reversible rule, and a regular-tree invertibility study are relevant foundations, but no inspected claim supplies the two-even-vertex reduction to a path-wave primary component. A previously recorded one-even-degree tree result is purely nilpotent; the separately recorded path-wave result does not link to irregular trees. Targeted aliases and general-coverage searches did not identify a stronger result. Full text for Macfarlane was unavailable; equivalent results in unindexed literature remain a priority risk. These are limitations, not evidence that failed searches prove novelty.

## Mathematical value — PASS

The result makes a global recurrent-state invariant of an infinite class of arbitrarily branched finite trees depend only on the distance between two even-degree vertices. It determines a sharp global clock, fixed populations for all times, and primitive orbit counts while isolating the dimension of transient degrees of freedom. The transition from one even-degree defect (nilpotent) to two defects (reversible recurrent part) is a motivated structural phenomenon; no downstream application is assumed.

## Closest literature and limits

Jacobs–Machado–Trevisan (2005): general tree determinant technique. Akın (2012 initial release; 2017 revision): regular Cayley-tree matrix rules, reversibility and entropy. Macfarlane (2004): one-dimensional reversible second-order cellular automata, abstract only. The result does not classify transient entrance-time populations or graphs with more even-degree vertices, and independent mathematical validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
