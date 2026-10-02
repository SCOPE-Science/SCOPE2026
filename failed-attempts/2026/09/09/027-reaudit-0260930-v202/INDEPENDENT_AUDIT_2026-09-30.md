# Independent mathematical audit — 2026-09-30

## Final claim
The assigned package gives a complete equilateral angle-defect census for the 73 triangulated 2-spheres on four through nine vertices and a protocol-P0 Willmore benchmark.

## Correctness — UNRESOLVED
The intrinsic finite census checks cleanly: fresh code verified 73 rows with counts 1,1,2,5,14,50; every graph has the required sphere edge/face counts, every stored defect is 6-degree and sums to 12, all 1,327 within-order pairs are non-isomorphic under an independent backtracking test, and all 893 flippable edges land in the stored same-order set. The stored Willmore values have the reported T9_0 maximum. However, the claimed P0 spring-embedding provenance of the stored coordinates was not regenerated from the seed/dynamics, so that protocol-generation component is not independently closed.
Checked sources: Assigned census.json at 92c7f26b45ce94be6cda0eafed44298c598d7b47; Fresh independent graph-isomorphism and edge-flip closure checks; Bobenko arXiv:0707.1318
Residual risks: The deterministic P0 embedding dynamics were not replayed; only the stored positions/numerical benchmark were inspected. Completeness uses the standard flip-connectivity theorem plus the verified closed flip set.

## Originality — FAIL
The intrinsic headline defect census is covered by prior complete small triangulated-sphere classifications/generators: for an equilateral triangle complex the defect multiset is the immediate degree transform 6-degree, so once the known 73 graphs are enumerated the advertised intrinsic table is mechanically implied. The P0 Willmore numbers are protocol-specific numerics, not a stronger intrinsic mathematical invariant that rescues originality.

### Equivalent formulations
Searches: triangulated 2-spheres 4 to 9 vertices angle defect census degree sequences Willmore; triangulated sphere degree sequence n<=9; simplicial polyhedra A000109
Evidence: The angle defect in this equilateral setting is exactly a linear transform of vertex degree, so degree-sequence data are an equivalent formulation of the intrinsic claim.
Reasoning: Searching degree multisets is necessary because the defect notation can hide that the claimed invariant is just 6-degree.

### Broader coverage
Searches: Köhler–Lutz small-vertex triangulations; plantri maximal planar graph generation; OEIS A000109
Evidence: Prior classification/generation covers all triangulated 2-spheres in the stated vertex range, including the known counts 1,1,2,5,14,50.
Reasoning: A complete stronger enumeration of the objects plus their adjacency data mechanically determines the degree/defect rows.

### Exact database or table
Searches: triangulated 2-spheres 4 to 9 vertices angle defect census degree sequences Willmore; OEIS A000109 simplicial polyhedra counts
Evidence: Even if an identical formatted defect table is absent, the exact underlying graph database/classification is prior and suffices to compute every defect row without new geometric input.
Reasoning: The originality standard compares implication, not whether the same columns were printed.

### Claim versus prior implication
Searches: equilateral angle defect formula; Bobenko discrete Willmore definition
Evidence: The intrinsic part follows directly as defect equals 6-degree in units of pi/3. Bobenko's Willmore energy depends on geometric realization, so the record's P0 maximum is only a chosen-protocol benchmark.
Reasoning: The prior graph classification decisively covers the intrinsic result; the arbitrary protocol statistic is logically separate and does not create a new intrinsic theorem.

### Source inspections
- **Surfaces from Circles** (https://arxiv.org/abs/0707.1318): Confirms that Willmore energy depends on a geometric realization and is not fixed by the equilateral combinatorial defect data. Material read: Full-text definition of discrete Willmore energy via circumcircle intersection angles and relevant propositions. Evidence: The energy is defined from circumcircle/hinge geometry, not merely vertex degrees.

Checked sources: Resultary published-record search; OEIS A000109; Köhler–Lutz arXiv:math/0506520 as cited classification context; plantri generation literature; Bobenko arXiv:0707.1318
Residual risks: A historical source may tabulate exactly the same degree multisets; that would only strengthen the coverage finding. The P0 values may be new numerical data, but they are not an invariant and were not motivated independently of the chosen embedding protocol.

## Scientific value — FAIL
The intrinsic defect table is a known-classification degree recomputation, while the only less-covered component is the maximum under an ad hoc spring-embedding protocol. That protocol-relative maximum has no demonstrated invariant meaning or downstream mathematical need, so it does not meet the stated value bar.
Checked sources: OEIS A000109; Köhler–Lutz classification context; Bobenko arXiv:0707.1318
Residual risks: A differently motivated realization protocol could lead to a valuable geometric optimization problem, but that is not the final claim audited here.

## Limitations
- The intrinsic defect rows are exact degree transforms of a prior complete small-sphere classification, so originality fails.
- The P0 Willmore maximum is protocol-relative and lacks invariant mathematical motivation, so value fails.
- The fresh audit did not regenerate the spring-embedding dynamics from seed, so correctness of that provenance remains unresolved even though stored numerical rows were internally checked.

## Disposition
failed
