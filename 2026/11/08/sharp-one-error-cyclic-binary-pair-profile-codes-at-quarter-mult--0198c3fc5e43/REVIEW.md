# Self-review

## Correctness — PASS
The complete feasible profile set follows from cyclic transition balance and positive symbol runs. The unit read-label corruption balls are disjoint precisely when half-\(\ell_1\) profile distance is at least three. The exact coordinate distance reduces the problem to a two-dimensional lattice packing. At every quarter-multiple length the proof partitions the entire mixed region into \(m^2\) disjoint four-point conflict cliques and supplies a residue-class construction attaining one point per clique plus the two constants. The selected constant-to-mixed distances are explicitly checked. Monotonic embedding gives the stated bounds at other lengths. The executable replay confirms the required boundary cases and finite certificates, but is not used as an infinite proof.

## Originality — PASS, with residual historical risk
Kiah–Puleo–Milenkovic (2014/2015), examined directly in its public PDF at the noisy-profile distance definitions and Sections 4 and 6, provides the general framework and asymptotic-order constructions, but the inspected statements do not imply the exact \(m^2+2\) optimum. Jacquet–Knessl–Szpankowski (2010) counts clean Markov types, not maximum one-read-corruption-resilient subcodes. Available published records on binary *linear* pair multispectra and cyclic positional symbol-pair codes do not have the same observation or error metric. Independent historical-priority verification remains open, particularly for potentially uninspected later specialized literature. A failed search alone is not taken as proof of novelty.

## Value — PASS
This identifies an exact infinite sequence of zero-error capacities for a natural noisy unordered-read channel and gives the sharp asymptotic constant. Unlike a routine evaluation of the number of feasible histograms, it solves a nontrivial packing problem and pairs an explicit tight clique upper certificate with a constructive code. Both the read model and the exact quarter-multiple boundary are mathematically motivated by the binary de Bruijn graph and the four-point packing geometry.

## Scientific limitations
Only binary cyclic length-two reads and at most one misreported read label are covered. The proof does not establish exact capacities for nonmultiples of four, source-symbol substitutions, longer reads or larger alphabets. The finite verification is not independent expert review. The historical-priority comparison is necessarily incomplete.

Self-review: passed. Independent audit: not yet performed.
