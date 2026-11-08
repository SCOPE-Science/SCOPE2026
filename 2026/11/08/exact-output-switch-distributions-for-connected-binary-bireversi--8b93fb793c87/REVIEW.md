# Scientific review

## Correctness: PASS

The inverse's two output-conditioned successor maps are permutations if and only if \(A(S)=B(S)\); the proof checks both directions, including all-swapping and no-swapping boundary cases. For fixed \(S\) of size \(k\), choosing \(A\) and a set-preserving relative permutation establishes \(n!k!(n-k)!\) tables, and summing over \(S\) yields the exact uniform counts. State-graph components are the orbits of two permutations; independent restriction of their tables justifies the labeled-set exponential formula and the explicit recurrence. The actual standalone checker independently evaluates the defining inverse maps for all \(470{,}322\) tables at \(n\le5\), matching all connected and total counts. No finite check substitutes for the all-\(n\) arguments.

## Originality: PASS under accessible comparisons, with priority risk

Godin (2019), Proposition 3.2, gives a general probability upper bound for bireversibility rather than exact binary \(k\)-switch statistics or connected enumeration. D'Angeli–Rodaro (2025/2026), Section 6, treats free-group obstructions and connected bireversible components, not a bivariate labeled count. Curtin–Savchuk (July 2026) provides a closely relevant general characterization and is a serious comparison: its primary PDF/HTML could not be read, and the visible abstract alone cannot establish absence of an implicit enumeration. Searches for the precise factorial law, invariance of switching subsets, component recurrence, and other formulations did not identify a prior equivalent. This is evidence-based provisional originality, not a proof of absolute novelty. An earlier result about two-state machines modulo relabeling is not equivalent to the present arbitrary-state labeled connected count.

## Value: PASS

The theorem computes two complete natural distributions, including the connected subclass most relevant when studying irreducible automaton actions. The uniform unconditional law and its nonuniform connected refinement are structurally different, and the latter is accessible for every state size without raw enumeration of \((n!)^2 2^n\) tables. The exact switch-profile is directly relevant to unbiased random-model experiments and to sizing connected bireversible test families. The result does not claim an algorithmic complexity breakthrough or a group-theoretic classification.

## Residual risks and limitations

The 57-page 2026 Curtin–Savchuk source was not available in primary full text, so implicit coverage remains possible and independent priority validation is outstanding. Other sources' general characterizations of bireversibility supply some ingredients. The exact enumeration does not apply to larger alphabets, quotient automata, or noninvertible/nonreversible tables. Independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
