# Scientific review: arithmetic edge-midpoint lifting

## Correctness

PASS. The wedge identity counts each line-graph adjacency exactly once and supplies a direct expression for the output seminorm. Graph coarea reduces the global operator quotient to indicator cuts without missing arbitrary real inputs. On each crossing edge, the two same-side neighbor counts total at most the number of other vertices; equality forces the stated boundary-universal property. The tree upper bound and matching bridge-cut witnesses are independent of any finite enumeration. The standard-library checker verifies all connected labeled graphs through five vertices using both direct edge-midpoint differences and the combinatorial wedge counts; no floating-point arguments are needed. No extension to weighted or directed graphs is asserted.

## Originality

PASS, qualified to the inspected literature. The 2014 full-text graph-variation source treats signal recovery and quadratic graph variation rather than a vertex-to-edge midpoint-lift operator between absolute-edge variation seminorms. The 2024 full-text line-graph source uses edge-sampling smoothness, not this induced norm. Closely indexed published results on positive edge averaging concern the \(\ell_\infty\)-generating radius, and published descendant-tree averaging concerns a same-domain averaging map; neither gives the cut-wedge expression, the all-tree degree-sum law, or its equality classification. A complete full-text comparison with every possible historical combinatorial treatment of wedges is unavailable; the priority claim is consequently qualified.

## Mathematical value

PASS. Arithmetic edge-midpoint interpolation is the canonical fixed, positive vertex-to-edge lift. Its stability changes qualitatively with branching: complete graphs and stars attain a sharp linear-in-order envelope, whereas all paths and cycles are nonexpansive. The exact all-graph cut formula, rigorous equality criterion, and complete tree classification identify when the simplest local positive interpolation preserves or magnifies absolute graph variation; this information does not follow from positivity or maximum-norm stability.

## Closest literature and limits

Chen et al., arXiv:1411.7414 (2014-11-26); Yanagiya et al., arXiv:2407.10149 (2024-07-14); indexed positive edge-averaging generating-radius and descendant-tree-averaging statements. The claim does not extend to arbitrary edge weights, multigraphs, or optimal lifts, and priority beyond examined sources remains uncertain. Exact finite checks are supplementary to the analytical proof.

Self-review: passed. Independent audit: not yet performed.
