# Independent mathematical audit

## correctness

PASS

The rule on the labelled graph C4 square C5 uses four distinct neighbors and synchronous binary threshold >=3, <=1 and incumbent retention on ties. Two separately written packaged C++17 implementations construct all 2^20=1048576 transitions; indegree peeling finds exactly recurrent functional-graph cycles and recovers entrance depths backwards; independent column-major trajectory traversal and Burnside fixed-cycle sums yield period/symmetry counts. An independent newly written C++ 20-bit enumerator was compiled and executed this run and reproduced 3186 fixed states, 3225 primitive two-cycle orbits, maximum entry depth five, exact 12 period-by-entry counts and 53+67=120 classes under 160 symmetries. The exact joint table by t=0..5: period1 [3186,96300,346900,226680,68760,5800], period2 [6450,94740,138400,51120,10080,160], totaling 1,048,576. Group action is correct because graph automorphisms and bitwise complement commute with F; Burnside sums 8480 and 10720 divided by 160 equal 53 and 67. Full finite enumeration is exhaustive for THIS graph and proves its finite assertion; the classical period-two theorem is not replaced or claimed novel.

## originality

PASS

The period<=2 assertion follows already from classical Goles–Olivos for finite symmetric threshold dynamics and is not new. Nakar–Ron 2025 treats stability and periodic pattern structure on 2D tori, but does not state the full C4xC5 global attraction basins, exact 5-step entry distribution and 120 orbit quotient. Other published exact dynamic censuses for C4xC4≅Q4, dodecahedral and prism graphs have different adjacency matrices and cannot supply these 20-site torus counts by graph isomorphism. Novelty rests on the exact complete basin and symmetry census for this particular natural graph, not generic period-two behavior.

## value

PASS

A finite complete basin and symmetry classification on the smallest non-hypercubic 4x5 square torus with an odd cycle provides exact benchmark data at a natural graph size. Its sharp 5-step settling time, 120 spatial classes and precise split of one- vs two-period attraction are not determined by the generic period-two theorem or recurrent-state structural classification. A natural exact finite invariant can be valuable without a theorem for all grid sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
