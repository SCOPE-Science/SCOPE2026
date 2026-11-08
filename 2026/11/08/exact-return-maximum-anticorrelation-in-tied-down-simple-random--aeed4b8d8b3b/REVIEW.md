# Scientific review

## Correctness

**PASS.** The proof identifies the precise sample space, endpoint convention, and one-sided maximum. Reflection produces the exact height-capped bridge generating function; first-return factorization produces the excursion-marked generating function. Differentiation, height-tail summation, rationalization in \(\sqrt{1-4z}\), and coefficient extraction give every mixed and marginal moment. A strict induction on the central-binomial ratio proves negativity for all lengths beyond one; Stirling's formula establishes both limits. The independent standard-library checker agrees on 432 exact rational assertions, including exhaustive short bridges. Finite checks supplement rather than replace the proof.

## Originality

**PASS, with historical-priority qualification.** Pitman's full 1998 report identifies local-time and maximum-related Brownian-bridge laws, but does not furnish this finite conditioned nearest-neighbor return/maximum covariance. Lindell–Holst's full 2007 article treats the **duration** of longest excursions and related ranked-duration counting, not the height maximum coupled to the number of completed excursions. Voss gives the discrete bridge return-count marginal. Literature and claim comparisons concerning return counts, excursion lengths, height maxima, and Lévy identities did not locate this explicit mixed identity or its all-length sign rule. Existing reflection/renewal identities make an implicit earlier derivation possible; absence from searches is not a uniqueness certificate.

## Value

**PASS.** Returns to zero measure discrete local time and excursion count, whereas the one-sided maximum measures a global height extreme. Their separate distributions alone leave their dependence undetermined. The formula gives a complete finite-size sign theorem, an exact rate of linear covariance growth, and a nonzero limiting Pearson correlation. This documents a persistent nontrivial local-time/extremal dependence in a standard tied-down walk model and is useful for comparing discrete excursion decompositions with their Brownian-bridge analogues.

## Boundaries and literature

The theorem is only for uniformly conditioned simple symmetric bridges, the one-sided maximum, and the convention that the terminal return is counted. It does not claim stochastic negative association or new Brownian joint distribution theory. The closest inspected primary works are Pitman (1998), Lindell and Holst (2007), and Voss (2007); broad older combinatorial enumeration and an inaccessible full text on continuous Brownian maxima remain qualified priority risks.

Self-review: passed. Independent audit: not yet performed.
