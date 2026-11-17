# Scientific review

## Correctness — PASS

A degree-two vertex that flips in a two-cycle forces its two neighbors to flip and their initial opinions to alternate across each incident edge. Propagating around an odd cycle excludes any flipping ring vertex other than its degree-three connector endpoint. Any nonconstant two-cycle therefore has precisely the entire connecting path flipping. The degree-three boundary requires opposite static ring-neighbor bits, and static ring interiors must have no singleton runs. This yields a constructive bijection with two independently chosen opposite-end, no-singleton binary words and one connector phase bit. The count \(2W_aW_b\) of temporal phases and hence \(W_aW_b\) orbits follows for all odd ring sizes and all connector lengths. The run-composition generating function gives the displayed Fibonacci-and-period-six formula. Independent exhaustive and constructive tests are provided, but infinity is handled by the graph argument, not by extrapolating the tests.

Limits: this is an immediate two-cycle census, not a transient-basin result; it excludes even cycle lengths. A bounded test does not establish the universal quantifiers without the given proof.

## Originality — PASS, qualified

General finite-majority period-two results in Goles–Olivos and the 2014 and 2015 primary papers do not determine this graph-family count. The closest published one-pendant-cycle classification **does** determine the same local word sequence, which is explicitly credited and excluded from the novelty claim. The singly chorded odd-cycle result uses a theta graph with a three-mechanism cycle census, not a dumbbell with one connector. The published clique-barbell count covers complete graphs rather than cycles and has a different parity obstruction. The identified dumbbell study concerns a different stochastic update rule. No equivalent all-distance path-localization and count theorem was found in the mathematical-record or primary-literature checks. This is evidence for originality, not proof of absolute priority.

Residual risk: earlier graph-majority treatments under alternative nomenclature might contain an equivalent joining theorem; inaccessible or unindexed literature was not exhaustively excluded. The original 1980 source was available through bibliography rather than complete primary text.

## Mathematical value — PASS

The graph family is a natural two-cycle analogue of the weakly coupled odd-ring majority problem, on which each isolated odd ring has no oscillation. The theorem exhibits an exact bridge-enabled oscillation mechanism in which both odd rings serve as independent static spatial constraints, while an arbitrarily long joining path transmits a two-phase signal without changing orbit count. It proves an exact length-independent orbit population, phase-parity transport, a sharp five-site threshold on each ring, and a factor-of-two decay in the share of recurrent initial states per added connector site. The factorization is motivated by weak coupling and gives a concrete, all-size classification rather than an arbitrary isolated enumerative slice.

Risk: the local path-word enumerator is already known; its reuse alone would not be valuable. The mathematical value lies specifically in proving the connector-length independence and complete flip-support rigidity for the coupled family.

Self-review: passed. Independent audit: not yet performed.
