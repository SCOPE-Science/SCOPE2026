# Scientific review

## Correctness — PASS

The exact B3/S23 column map with dead vertical exterior defines a 64-vertex one-step recurrence graph and a 4096-vertex two-phase recurrence graph. A closed length-\(n\) walk is in bijection with one indexed width-\(n\) configuration returning after respectively one or two updates. The exact integer certificate isolates cycle-bearing SCCs (40 vertices for one-step and 48,6,6 for two-step), computes their characteristic polynomials and checks the strict Collatz–Wielandt certificates. Strong connectivity and a self-loop make the large components primitive. This proves the all-length spectral formulas and strict exponential gap. Independent full bit-level enumeration matches the count table for \(n=3,4,5,6\). Risk: implementation bugs remain theoretically possible; the transparent local graph definitions and a separate exhaustive implementation reduce but do not eliminate this risk.

## Originality — PASS, qualified

The foundational Life rule and standard de Bruijn technique are preexisting. McIntosh's *Conway's Life* and *Life's Still Lifes* discuss periodic-state diagrams, but the accessible abstracts do not give the present exact labelled vertically-open three-row cylinder spectra or prove the strict threshold separating their Perron roots. Related current mathematical-record results concern other dynamics and/or vertical periodic boundary conditions. Searches for the precise spectra, equivalences and numerical constants revealed no matching prior statement. Full comparison with the McIntosh text was unavailable, so historical priority is qualified; this cannot establish uniqueness.

## Value — PASS

This is a natural minimal-height strip supporting the canonical blinker mechanism. It gives exact all-length enumeration of both still lifes and temporal-two configurations, and a nontrivial qualitative conclusion: temporal-two configurations asymptotically dominate still lifes even though the two entropy bases are quite close. The strict difference requires a genuine 40- versus 48-state primitive spectral comparison and is not a restatement of the generic transfer-matrix method. No claim is made about higher temporal periods or attraction basins.

## Limitations and closest literature

McIntosh (1988 manuscript; 2010 book chapters) is the strongest plausible prior technical source, and complete text comparison remains unresolved. Gardner (1970) establishes the original rule, not a documented comparable strip census. MathWorld discusses still-life objects and counts by population and symmetry, a different enumerative question. A separate mathematical-record result treats cyclic dominance on a 3-row torus, not Conway Life with open vertical boundaries.

Self-review: passed. Independent audit: not yet performed.
