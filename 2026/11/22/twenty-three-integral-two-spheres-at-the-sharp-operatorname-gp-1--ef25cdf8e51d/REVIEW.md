# Scientific review of the \(\operatorname{GP}(18,3)\) radius-two boundary classification

## Correctness: PASS

The exact domain is the 36 labelled vertices of the unweighted generalized Petersen graph with outer step one and inner step three, using inclusive graph-metric radius two. The proof first classifies all 21 graph hexagons, 42 maximal exceptional triangles and the full four-level face vector. It then collapses the 36 neighborhood tetrahedra and centered faces onto the graph, transports the exceptional two-cell attachments, and splits off one integral \(S^2\) from each paired hexagon. Of the remaining 21 disks, 18 have unique inner edges and leave one circle; each of three inner cycles wraps once around that circle, giving two additional \(S^2\) factors. This yields exactly 23 two-sphere summands by actual CW homotopy equivalences, not by homology alone. The package contains executable exhaustive finite checks of all clique/collapse hypotheses, a separate 127-step integral cellular-generator elimination ending at 23 trivial relators, and signed modular chain-rank cross-checks. All checks replayed successfully. No extrapolation from a finite parameter sample is used.

## Originality: PASS against inspected evidence

The closest published same-family result, *Persistent hexagon spheres in generalized Petersen graph thickenings* (https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-persistent-hexagon-spheres-in-generalized-petersen-graph-thicken--c6f4ddebbf06), proves the integral \(n\ge19\) stable range but **explicitly does not** classify the homotopy type for \(n=18\); it gives the now-agreed mod-two ranks only. A mod-two homology vector cannot imply the new integral homotopy type. Adamaszek's girth-seven closed-neighborhood collapse and hexagon-packing results under edge-disjointness exclude the present overlapping girth-six graph. The graph-power and metric-gluing primary works and hypercube Rips classification do not imply the boundary result. Searches for the exact graph, the radius-two graph-square clique complex, its 23 sphere count, and generalized Petersen aliases returned no stronger coverage. Residual risk: a not-indexed general graph-square theorem or independent classification could cover this case.

## Value: PASS

The prior family theorem explicitly identifies \(n=18\) as the obstruction to its sharp range but leaves its **integral homotopy** unresolved. The present classification resolves this motivated natural boundary, explains why three additional inner hexagons kill the unique circle, and proves torsion-freeness and a genuine sphere wedge. It is not merely a recomputation of the already published mod-two ranks and does not claim a general theorem beyond the single boundary graph.

## Scientific limits

The proof classifies only scale two and only \(\operatorname{GP}(18,3)\). The finite face enumerator and Tietze checker are independently reproducible; the conceptual CW argument is required to deduce the homotopy equivalence. No assertion of independent external validation is made.

Self-review: passed. Independent audit: not yet performed.
