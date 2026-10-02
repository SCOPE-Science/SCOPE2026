# Independent mathematical audit — 2026-09-30

## Record

Certified nonlinearity / differential-uniformity table for seven committed 4-to-6-bit S-boxes with bent certificate and structured-vs-random gap

## Disposition

failed

## Correctness: PASS

A fresh implementation independently reconstructed GF(32) and GF(64), all structured power maps, the two committed permutations, exhaustive Walsh spectra, differential-distribution tables, and Möbius ANF degrees. Every row of the claimed table matched exactly, including histograms, S2 almost-bent spectrum, the 6-variable flat bent spectrum, and all structured-versus-baseline inequalities.

## Originality: PASS

The structured Gold, inverse, PRESENT, and Maiorana-McFarland properties are established prior art and are not original contributions. The only claim-specific novelty that survived search is the exact pair of seed-committed random baselines and their finite joint comparison with the structured examples; Resultary surfaced no independent exact copy of those seed-specific tables.

## Scientific value: FAIL

The purported new content is a comparison against only two arbitrary pseudorandom draws. The record itself disclaims any ensemble statement, and the structured rows are classical. A seed-specific two-draw inequality is an unmotivated finite slice rather than a meaningful mathematical gap, classification, boundary, or invariant; exact reproducibility and novelty of the random outputs do not meet the required value bar.

## Limitations and residual risks

- All table entries were independently recomputed exactly.
- The scientific rejection is for value, not correctness.
- The only surviving novelty is tied to two arbitrary fixed pseudorandom baselines and does not support a random-ensemble conclusion.

## Sources inspected

- K. Nyberg, `Differentially Uniform Mappings for Cryptography`, accessible author PDF.
- The assigned RESULT.md and exact truth-table/definition artifacts.

This file records a mathematical audit of the scientific claim. It is not an expert attestation or a statement about any separate verification channel.
