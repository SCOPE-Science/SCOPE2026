# Scientific self-review

**Correctness — PASS.** The underlying vertex-coordinate formula and braid-fan completeness are Theorem 4.1 and the end of Section 4 of Bottman–Poliakova (arXiv:2208.14529v1). The standalone integer checker generates every collision order, deduplicates to the published exact vertex count 108, and tallies all 5778 unordered pairs, comparing all 174 multiplicities with a separately generated CSV. Two independently coded interval/block and union-find constructions produced the same vertex vectors. This is an exhaustive finite proof using a known all-vertex generation theorem, not an inference from sampled data.

**Originality — PASS (priority provisional).** Queries on Bottman–Poliakova constrainahedra, exact diameter 430, 108-vertex C(3,4) and chord-distance spectra returned the already-indexed inball result, which does not imply the diameter graph or entire distance table. The 2022 full source gives vertex formulas and normal-fan properties, not the derived metric census; Chapoton–Pilaud tabulate the total vertices in a different geometric realization. No covering statement was identified, but an inaccessible indexed inball record and unindexed examples are priority risks.

**Mathematical value — PASS.** This is a complete, exactly reproducible Euclidean chord metric of the smallest mixed constrainahedron outside the classical one-axis associahedron and two-axis multiplihedron families. It provides the exact diameter graph and a sharp separation to the next metric shell, allowing metric comparison across distinct realizations of the same face poset. It is a deliberately finite natural classification, not a claimed infinite-family formula.

**Scope and limitations.** The 108-vertex count and coordinate realization belong to the cited antecedents. The 174-level Euclidean table is specific to the Bottman–Poliakova coordinates, not the Chapoton–Pilaud realization. Historical priority is provisional and independent mathematical review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
