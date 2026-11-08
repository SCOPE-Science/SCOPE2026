# Scientific review

## Correctness

**PASS.** Lax splitting reduces to orientations of outdegree at most one, equivalently pseudoforests. Edge-minimal non-pseudoforests are connected bicircular circuits with one more edge than incident vertices and no leaves; bipartite degree counting gives the sharp upper limit. Two explicit theta families, preserved by double subdivision, attain every cardinality in the stated interval. The six- and seven-edge counts follow by unique small circuit types. The standalone exhaustive checker directly tests semantic splitting and independently compares spectra through a four-by-four rectangle. The proof, rather than any bounded enumeration, covers all positive alphabet sizes.

## Originality

**PASS within the inspected evidence.** The 2025 inverse-dependence paper establishes the target formula's global incoherence, not the exact finite-alphabet circuit-size spectrum. The 2026 coherence paper supplies the exact-size definition, not this fixed-rectangle cutoff. Standard bicircular matroid theory recognizes the circuit families; the 2003 complete-bipartite paper enumerates *bases* and does not give the stated minimal-*circuit* size spectrum, and the 2024 paper studies the lattice-path subclass. A related prior result under alternative terminology is possible. The separate result counting successful disjoint splitting witnesses (item `6bf80f7f-8110-43be-a416-9f1ee60ae994`) does not imply this obstruction spectrum or its exact-size coherence boundary.

## Mathematical value

**PASS.** Coherence asks whether local consistency checks certify an entire relation. On finite alphabets a sharp obstruction cutoff gives the exact maximum witness size needed for falsification; the full interval determines which local test arities are insufficient, and the two smallest coefficients count the first failure patterns. The contrast between bounded-size witness detection and literal exact-size coherence is structural, and the formula applies uniformly to all rectangular alphabets. The conclusion is intentionally specific rather than an asserted new matroid circuit taxonomy.

## Risks and limits

The standard bicircular circuit classification is prior mathematics; an older precise parameterized spectrum is possible. The 2003 full-text primary source was inspected in selected pages addressing definitions, objectives, bases and tables; no whole-document automated text comparison was available. All infinite-family proofs are mathematical, with experiments confined to small rectangles. Independent historical-priority and mathematical audits have not been performed.

Self-review: passed. Independent audit: not yet performed.
