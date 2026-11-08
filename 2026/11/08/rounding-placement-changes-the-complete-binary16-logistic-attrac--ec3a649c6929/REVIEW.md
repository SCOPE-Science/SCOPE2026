# Scientific review

## Correctness — PASS

Every admissible binary16 input is encoded exactly as an integer multiple of \(2^{-24}\), and both stated rounded maps are generated using exact integer nearest-even comparisons. The supplied finite exhaustive certificate visits all 15,361 nodes and labels every cycle and basin. An independently written NumPy implementation reproduced all 30,722 successor edges. The five-cycle encodings, basin totals, maximum preperiods, distinct-cycle counts, and inter-map differing-edge count were independently checked. The result is finite; no real-valued infinity claim follows from it.

## Originality — PASS, provisional historical priority

Prior research already teaches that changing floating-point operation order changes dynamics (Galias, 2021). Corless and Fillion's 2024 slides already identify the staged half-precision period-40 cycle and its 10,267-node basin; this staged component is not claimed as new. The 2026 motivating work studies staged float32 data and forecast-error estimates, not this binary16 all-node comparison. The apparently new content is the explicitly correctly rounded one-final-round graph, its period-five orbit with 117-node basin, its 15,236-node zero basin, and exact 2,774-edge difference from the staged graph.

The closest accessible published exact-cycle study is Galias (2021). The closest exact half-precision precedent is Corless and Fillion (2024). Klöwer et al. (2023) study binary16 rounding and finite periodicity; their full paper PDF was unavailable for complete inspection, so the comparison to unseen supplementary information remains a historical-priority risk. Several additional mathematical-record and web queries for the exact paired numerical invariants found no stronger covering result, but absence of search hits does not prove priority.

## Mathematical value — PASS

Full state-cycle structure (periods, basins, convergence times) is the natural invariant for digital chaotic maps because eventual recurrence governs the amount of distinct trajectory data. A change from a 40-cycle with a 10,267-node basin to a 5-cycle with a 117-node basin, under two natural and explicitly defined rounding semantics for precisely the same real polynomial and numerical format, is a substantial qualitative change. Exhaustive proof is feasible at binary16 resolution and avoids inference from a random ensemble of initial seeds. This is a motivated exact finite cutoff, not a claim that finite precision is inherently novel.

## Limitations and sources

Scope is nonnegative IEEE 754 binary16 numbers on \([0,1]\), deterministic nearest-even rounding, gradual subnormals, and logistic parameter four. No claim of arbitrary compiler behavior, other precisions, floating-point association identities beyond those checked, or independence of scientific validation. The complete 2023 article could not be read, and historical priority remains provisional.

Sources: Velichko and Pham (2026), arXiv:2608.16120; Galias (2021), DOI 10.1109/TCSII.2021.3081604; Klöwer et al. (2023), DOI 10.1038/s41598-023-37004-4; Corless and Fillion (2024), *Floats for Philosophers*, slide 60.

Self-review: passed. Independent audit: not yet performed.
