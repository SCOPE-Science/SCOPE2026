# Scientific review: directed de Bruijn NOR synchronization

## Correctness — PASS

The statement applies to incoming-neighbor NOR on the loop-retaining directed \(q\)-ary word-overlap graph, for every integer \(q\ge2,d\ge1\). The proof constructs the exact depth-\(t\) NOR tree at every prefix, verifies that disjoint prefix blocks partition the initial coordinates, and thereby establishes the unique recurrent two-cycle, the sharp worst-case first entry \(d\), and exact arbitrary-bias cumulative counts. The \(p_*\) phase transition follows from an elementary unimodality and three-fixed-point argument for the second-iterate probability map, together with explicit near-endpoint power bounds. The computational checks are exhaustive only for the stated small instances; the all-size result is analytic. Critical derivative, endpoint behavior, normalization and \(p=0,1\) boundaries were checked separately.

## Originality — PASS, with priority qualifications

Pearl (1980) establishes the alternating AND/OR tree recursion, nontrivial critical bias, and superexponential off-critical decay in a game-tree setting; these are credited as prior input rather than independent claims. McIntosh (1991) develops word-overlap/de Bruijn diagrams and their matrix relations, but not this nonlinear NOR temporal-basin law. The previously recorded directed de Bruijn OR first-hitting formula has no alternating nesting and cannot directly supply the present tree recursion, critical slowdown, or two-phase first-entry histogram. The published 2020 directed NOR paper constructs arbitrary recurrent periods on other digraphs but does not analyze de Bruijn graphs, their exact first-entry times, or random initializations. The most relevant indexed records inspected do not present the complete combined claim. Mathematical equivalence to an unindexed treatment remains possible; no assertion of absolute publication priority is made. A natural main overlap risk is an unindexed derivation obtained by combining Pearl's tree recursion with de Bruijn coordinate partitions.

## Value — PASS

The intrinsic object is a classical strongly connected directed graph whose word-overlap gives a natural finite mixing clock. The first-entry distribution and critical bias reveal a substantial qualitative transition: almost all independent noncritically biased states synchronize in doubly logarithmic time in the vertex count (equivalently logarithmic in word depth), yet at one fixed critical bias they need almost the full deterministic worst-case depth. Exact labelled shell formulas and a sharp bound make the result a reproducible benchmark for finite inhibitory Boolean network dynamics. This extends beyond mere evaluation of one tree or a routine parameter substitution, because the distribution concerns simultaneous synchronization of all word-overlapping graph vertices.

## Limitations and closest work

The word-overlap graph has its canonical self-loops; results may fail if these are deleted, if all sites do not update simultaneously, or if random initial bits are dependent. The off-critical asymptotics keep \(p\) and \(q\) fixed, and no near-critical moving-bias scaling theorem is claimed. Earlier literature contains the single-tree fixed-point and convergence mechanism; the combined directed-network first-entry distribution and scale comparison are the limited subject of this finding. Historical priority is not independently established.

Self-review: passed. Independent audit: not yet performed.
