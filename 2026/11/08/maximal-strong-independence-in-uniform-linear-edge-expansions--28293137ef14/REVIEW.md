# Scientific review

## Correctness

PASS. The private-vertex argument forces exactly one chosen representative on every hyperedge, while original choices form an independent set. Conversely the no-isolate assumption ensures every omitted original vertex is blocked by a selected representative in one incident hyperedge, so the characterization is necessary and sufficient. The cardinality formula follows by disjoint counting; degree sums and direct substitutions yield the minimum, maximum, equal-cardinality criterion, cycles and complete graphs. The connected \(3\)-uniform counting reduction adds a universal vertex, which changes the independent-set count by exactly one. The code independently enumerates all subsets in stated finite instances and checks full families, not only totals.

## Originality

PASS on best available comparisons, with material residual risk. Barát–Gerbner–Halfpap (arXiv:2211.14101, full arXiv HTML examined) give general global maxima for maximal strong independence and \(A\)-transversals; they do not supply this construction-specific weighted cardinality polynomial. Provan–Ball (1983) establishes the source counting hardness but not the reduction to connected linear triple systems. Susada–Eballe (2023) treats the different semitotal domination condition. Cabrera-Martínez et al. (2026) analyze the independent domination number of edge coronas, which is a potentially close special-case source; the accessible abstract does not exhibit the full maximal-set census, while the inaccessible article text prevents completely excluding a stronger formulation. A full-text comparison of that article remains a publication-priority risk. Published-record and sequence-database comparisons did not identify an equivalent assertion; absence of a match is not proof of originality.

## Mathematical value

PASS. The classification addresses a standard enumerative problem studied for hypergraphs, on a canonical and genuinely linear uniform edge expansion of unrestricted graphs. It transfers full cardinality distributions to weighted graph-independent-set enumeration, identifies all equal-cardinality cases, gives exact loose-cycle and clique-family counts and unbounded missing cardinality intervals, and proves counting hardness even for connected linear triple systems. It is not an arbitrary finite table, a renamed extremal statistic, or a deduction that requires an unproved computational extrapolation.

## Closest literature and limits

The source definition and global bounds for maximal strong independence are in Barát–Gerbner–Halfpap (2022 preprint, 2024 journal). The most relevant possibly covering comparison is Cabrera-Martínez et al. (2026) on edge-corona **independent domination numbers**: only its abstract and bibliographic information were accessible. No claim of independent validation or settled publication priority is made. The proof applies to expansions with private vertices, not arbitrary linear hypergraphs. Computation is supplementary to the complete elementary proof.

Self-review: passed. Independent audit: not yet performed.
