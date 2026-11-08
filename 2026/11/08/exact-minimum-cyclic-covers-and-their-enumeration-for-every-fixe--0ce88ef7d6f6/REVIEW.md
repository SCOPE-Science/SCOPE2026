# Scientific review

## Correctness — PASS
The overlap graph uses complete length-\(n\) labeled words as edges. The distinct support-necklace components follow from the invariant that successive fixed-weight windows force the appended nonzero indicator to equal the dropped one. Every component is balanced; its normalized random walk resets to uniform colors after \(n\) transitions, making the component irreducible and giving only phase-root and zero eigenvalues. The resulting exact arborescence count, multiplied by the BEST local factors, proves both the minimum number and the number of minimum covers. The pure-Python checker independently reconstructed twelve finite instances, computed each exact Laplacian cofactor, and directly enumerated Euler circuits for three small instances. The checker is corroboration, not a substitute for the all-parameter proof.

## Originality — PASS against checked evidence
The two-nonzero case admits a simpler special calculation, whereas the present theorem treats arbitrary weight, including all weights greater than two, by a general reset-spectrum argument. Sawada–Williams addresses shorthand fixed-content construction rather than enumeration of minimum covers of original windows. Campbell–Janik-Jones–Sawada (arXiv:2603.11954) and Gabrić–Imam–Janik-Jones–Sawada (arXiv:2603.11934) likewise construct and decode bounded-weight or shorthand universal cycles; the inspected theorem statements and relevant full-text passages do not furnish the claimed enumeration. The known binary necklace formula and classical BEST/de Bruijn case are acknowledged components, not novelty claims. An equivalent old or unindexed enumeration remains a possible priority risk.

## Value — PASS
An exact full-word fixed-weight cycle is generally impossible because the binary supports cannot cross necklace classes. The natural replacement question is the smallest number of circular tracks and the number of optimal designs. The arbitrary-weight theorem gives both answers, interpolates the classical de Bruijn enumeration at the all-nonzero boundary, and resolves a family of higher-order support components not covered by the previously analyzed two-nonzero case. The general reset-spectrum law is structural, and the exact counts quantify a genuine design space beyond existence.

## Closest literature and limits
The 2026 bounded-weight construction and decoding papers and the fixed-content shorthand universal-cycle paper use related words and necklaces but different representations or objectives. The present result is limited to minimum-track covers without identifying reversals or alphabet permutations. Historical priority beyond the inspected evidence remains uncertain; no independent audit was carried out.

Self-review: passed. Independent audit: not yet performed.
