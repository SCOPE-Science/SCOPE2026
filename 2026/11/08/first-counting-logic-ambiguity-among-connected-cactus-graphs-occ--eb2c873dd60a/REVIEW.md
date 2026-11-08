# Scientific review — First counting-logic ambiguity among connected cactus graphs occurs at twelve vertices

## Correctness — PASS
The complete induction by leaf-block deletion justifies the enumerator's coverage of all connected cacti through order twelve; the rooted cyclic-order encoding distinguishes isomorphism types exactly. Globally shared integer color signatures at each refinement round avoid fingerprint collisions. Counts match the published independent cactus census; the two colliding pairs are decoded, checked for cactus blocks, and separately checked for nonisomorphism. The finite computation is exhaustive for the stated cutoff, not an extrapolation.

## Originality — PASS, with priority limitations
The standard 2015 counting-logic papers establish the abstract characterization but do not state the exact connected-cactus cutoff or two-pair classification. The standard cactus enumeration lists isomorphism-type counts, not logical equivalence classes. Comparisons distinguish class-relative isomorphism identification from the distinct question whether color refinement's vertex cells equal automorphism orbits, and from general chordal or cograph first-obstruction results. Historical priority is not independently certified.

## Mathematical value — PASS
Connected cacti extend both trees and unicyclic graphs but remain extremely sparse and have an exact decomposition into cycle and bridge blocks. Finding the first order at which ordinary counting-logic identification breaks, and *classifying the entire first failure layer* rather than merely exhibiting a counterexample, gives a substantive boundary for logical graph recognition. The two witnesses display different modes of blindness, including different cycle-block length spectra in one pair.

## Closest literature and limitations
Arvind et al. (arXiv:1502.01255), Kiefer et al. (arXiv:1503.08792), and OEIS A000083. This is not a theorem for arbitrary graph order or higher logic. The proof is a self-contained finite exhaustive certificate with explicit implementation; no separate independent audit was performed.

Self-review: passed. Independent audit: not yet performed.
