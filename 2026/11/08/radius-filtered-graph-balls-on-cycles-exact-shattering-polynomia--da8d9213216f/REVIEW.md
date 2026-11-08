# Mathematical review: radius-filtered cycle balls

## Correctness — PASS

The stated family consists of all actual nonempty integer-radius balls with radius at most the specified cutoff. For a proper ball on a simple cycle, the vertex set is a circular contiguous arc of odd length. On a triple, the full trace is achievable exactly when its maximal circular gap is at least the complement threshold; the three pair-only traces are simultaneously achievable exactly when all three gaps are at most the diameter threshold. Zero-radius balls supply the singleton and empty traces when the cycle has at least four vertices. The two diameter cases require separate arguments, which are included. Alternating four-point traces are impossible for any connected circular arc. The positive three-gap compositions and their inclusion–exclusion count give every coefficient. The normalized composition simplex proves the two-piece limiting density. A standalone checker exhaustively tested 117 cycle/cutoff families, 259527 supports, and 54318 triples; this is corroboration, not a substitute for the symbolic proof.

## Originality — PASS with historical-priority qualification

Chalopin, Chepoi, Mc Inerney, Ratel and Vaxès, *Sample compression schemes for balls in graphs* (arXiv:2206.13254, first public 2022-06-27), establish a size-three sample-compression theorem for graph balls on cycles. Their Section 4 and Proposition 10 concern reconstruction of samples, not the enumeration of VC-shattered vertex supports for each cutoff radius, nor the two-regime random-triple density. Coudert, Csikós, Ducoffe and Viennot (arXiv:2405.07588) investigate graph VC-dimension algorithms for closed neighborhoods, the special radius-one setting, without the stated cycle-ball polynomial for every radius. Comparisons with cyclic-window translates (fixed length, adaptive/Littlestone dimension) do not imply coefficientwise counts for the union of all allowed odd lengths. Related records for finite cyclic harmonic analysis and cycle neighborhood complexes concern different invariants. No equivalent enumerator was found in the checked materials. An equivalent result in literature on circular arcs, range spaces or sample compression could still exist.

## Mathematical value — PASS

The coefficientwise census is a complete, natural exact invariant of a standard metric-ball range family across every cycle size and integer cutoff. The support classification isolates the two necessary geometric constraints, gives a sharp three-shattering threshold at one-quarter circumference, and exposes two distinct asymptotic quadratic regimes with a further transition at one-third circumference. Unlike a single VC-dimension bound, it quantifies the proportion of all three-point supports that can be labeled arbitrarily; both the finite parity exceptions and the density limit are substantive geometric information.

## Scope and limits

The result concerns undirected, unweighted simple cycles and centered integer-radius balls. It does not classify arbitrary circular arcs, weighted cycles, arbitrary graph-ball families, or nonuniform random samples. Exhaustive computations have a finite cutoff and provide no stand-alone universal proof. Historical priority and proof soundness need independent mathematical inspection.

Self-review: passed. Independent audit: not yet performed.
