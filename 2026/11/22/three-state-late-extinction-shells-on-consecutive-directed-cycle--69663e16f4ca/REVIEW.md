# Scientific assessment

## Correctness — PASS

For every integer \(a\ge2\), the induction from the coordinatewise AND rule to exact-length walk predecessor sets is valid. The two-generator semigroup has conductor \(a(a-1)\), with a single missing integer above \(a(a-2)\); this fact is checked explicitly in the proof, not taken from finite experiments. At times \(E-k\), the only missing predecessor class has distance sum \(2a+1-k\). Multiplicities of distances to the hub give exactly \(2k-1\) single-zero initial states and \(k-1\) two-zero states that remain live. Absorption then gives the exact three-state late shells and one-state final shell. Exhaustive direct dynamics for \(2\le a\le7\) and an independent predecessor-walk computation for \(2\le a\le40\) passed; the all-size proof is the basis of PASS.

## Originality — PASS, with limited historical-priority uncertainty

Jarrah–Laubenbacher–Veliz-Cuba (arXiv:0805.0275, Lemma 2.7) already derive Boolean-network height from adjacency-matrix exponent; that is explicitly **not** the new claim. Noual (arXiv:1011.3930) treats the same two-cycle geometry but obtains recurrent-attractor formulas rather than the stated late transient zero-weight census; its synchronous positive-positive case is delegated to earlier work. The indexed sections of Demongeot–Noual–Sené (2012) cover doubly positive recurrent configurations; the complete published text was not independently accessible here, leaving a specific priority risk. The source on asynchronous intersected cycles (arXiv:1310.5747) has a non-equivalent update protocol. Searches for the identical late shell, semigroup and zero-weight formulations, and comparisons with accessible indexed mathematical records, identified no statement that implies this one. Absence from those searches alone is not treated as proof of novelty.

## Value — PASS

The quadratic maximum extinction time is a classical type of network invariant; what matters here is a new quantitative refinement, the complete natural family of the final \(a\) first-entry shells. Their striking constant population three and the restriction to initial configurations with only one or two zero bits separate worst-case relaxation from its extremely sparse near-extremal states. The terminal window width is one full shorter-cycle length, not an arbitrary parameter slice. This yields a reproducible structural witness for how two return-path lengths and their Frobenius gap govern finite-time convergence.

## Remaining scientific limits

Only the final \(a\) extinction shells are classified. The system must be a directed one-hub bouquet with consecutive cycle lengths and synchronous AND rule. The full earlier transient histogram and independent external verification are not provided. Historical equivalences in material that was only indexed or inaccessible remain possible.

Self-review: passed. Independent audit: not yet performed.
