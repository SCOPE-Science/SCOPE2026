# Review of exact truncated-octahedral vertex-tetrahedron spectrum

## Correctness
**PASS.** The polyhedron is given both by 14 explicit supporting halfspaces and by its 24 signed-permutation vertices. Every one of the \(\binom{24}{4}=10626\) unordered choices is enumerated with an exact integer determinant. A separate group-orbit check exhausts 265 orbits under 48 orthogonal signed-coordinate transformations, reproduces the full 17-level table and establishes the 6-plus-24 split of maximizers. A third calculation through the orthogonal four-dimensional permutation realization independently reproduces every frequency via perfect-square Gram determinants. The code was run successfully directly from the package input paths. The cell volume is 32 by orthant inclusion–exclusion. The scope is finite and no infinite extrapolation occurs.

## Originality
**PASS, with historical-priority risk.** Relevant published-finding corpus searches for all vertex quadruple volumes, their 17-level truncated-octahedral spectrum, the 24-vertex permutohedron, and the second-largest tetrahedron found the existing cube–octahedron intersection theorem. Its full RESULT.md was read and gives the largest inscribed volume and one-sixth occupancy fraction, explicitly declining a classification of all maximizing tetrahedra. It does not furnish the complete vertex-volume distribution, the second discrete level, or the two noncongruent maximum-volume orbit types. Lángi's 2021 study of parallelohedra treats mean-width extremality and zonotopal volume; Murphy–Weed's 2024 Archimedean construction treats face embeddings. Earlier own records were used solely to exclude overlap, including a different regular-dodecahedral vertex volume spectrum. Unindexed comparable classifications remain possible.

## Mathematical value
**PASS.** This is the exact complete distribution of a natural vertex-supported metric invariant of the highly symmetric three-dimensional permutohedron, also the body-centered-cubic lattice Voronoi cell and a canonical parallelohedron. The absence of missing volume levels, the sharp 1/3 runner-up gap and the two inequivalent optimal shapes are not consequences of the previously known maximal-volume number. They provide a precise finite classification usable as a benchmark for tetrahedralization and extremal inscribed-simplex questions. The claim is about an entire canonical solid, not a selected arbitrary slice.

## Scope and risk
The second-largest claim is discrete and vertex-supported; arbitrary points in the body allow tetrahedral volumes arbitrarily close to the maximum. The computer-assisted count is finite and independently reproducible, but not independently audited. Historical priority for any unpublished equivalent table is unresolved.

Self-review: passed. Independent audit: not yet performed.
