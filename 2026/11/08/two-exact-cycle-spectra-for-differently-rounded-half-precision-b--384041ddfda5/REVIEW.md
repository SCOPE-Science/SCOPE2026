# Scientific assessment

## Correctness — PASS

The definition of the two rounded maps specifies the complete input domain, ties-to-even normalization, product and remainder order, and the special case of a rounded remainder equal to one. Every binary16 input can be represented exactly by an integer numerator with power-of-two denominator. A standard-library verifier converts all 15,360 inputs to 30,720 exact successors, exhaustively finds the five primitive cycles of each graph, checks every basin label and preperiod, and reproduces all reported numbers. The exact-integer graph digests and an independent NumPy evaluation with zero successor mismatches provide corroborating evidence. The scope is entirely finite; no probabilistic sampling is used as a completeness argument.

## Originality — PASS within inspected evidence

Boghosian, Coveney and Wang (2019; DOI `10.1002/adts.201900125`) analyze numerical pathologies and the beta=3/2 case, but the exhaustive orbits they report are for binary32. Klöwer, Coveney, Paxton and Palmer (2023; DOI `10.1038/s41598-023-37004-4`) study the same beta map, explicitly distinguish low-precision and wider-precision multiplication, and discuss exact graph-based measures. The inspected main article does not state the complete two-way binary16 cycle/basin table or 512 edge differences. Those are the assessed contribution.

Risk: the 2023 supplementary exact-invariant-measure figures and associated notebooks were not completely accessible; they might contain one convention's results. An equivalent unindexed or unpublished table remains possible. This assessment does not assert historical priority beyond inspected material.

## Value — PASS

The exact ten-period/basin data quantify dramatic graph-level changes caused by a realistic choice of arithmetic ordering in the canonical noninteger beta shift: the fixed-point basin jumps from 468 to 5,705 encoded initial states, while a dominant 164-cycle is replaced by a 41-cycle. The full state census is a complete natural invariant of two well-defined finite dynamical systems, motivated directly by published discussion of finite-precision numerical pathology.

## Limitations

Uniform counts of representable numbers are not Lebesgue masses; no claims are made about infinite-precision dynamics, alternative rounding semantics or beta parameters. The finite-state classification and its exact arithmetic are internally reproducible, but independent mathematical review and publication-priority validation have not occurred.

Self-review: passed. Independent audit: not yet performed.
