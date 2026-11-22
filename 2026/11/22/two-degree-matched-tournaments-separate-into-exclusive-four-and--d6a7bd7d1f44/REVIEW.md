# Self-review

## Correctness — PASS
The two exact programs under `code/` both enumerate every one of \(8,388,608\) input states for **each** tournament. They independently reconstruct the successor maps, detect actual primitive cycles, and count full first-periodic-entry and period strata. Every table agrees and each sums to the full configuration space. Their algorithms are not two invocations of one classifier: one peels indegrees after building all successors, and the other uses fresh direct-neighbor updating during path discovery. Directly iterated witnesses check primitive period four, primitive period twenty-three, and the sharp respective depth-ten/depth-four cutoffs. No inference extends beyond these two finite networks.

## Originality — PASS, qualified
The closest publicly inspectable Paley tournament majority classification treats orders three, seven, eleven and nineteen, not twenty-three. Literature on undirected majority cannot cover long-period dynamics on these directed orientations. A centered one-dimensional majority rule is exactly shift-equivalent to carousel out-neighbor majority, and the 2022 structural results were compared rather than ignored; they do not state the current paired finite 23-vertex period-and-basin census. Searches against alternative graph names, directed majority, and period aliases found no covering exact table. This does not establish exhaustive historical priority; the most important residual risk is an unindexed equivalent computation or a stronger shifted-ring special case.

## Value — PASS
Two canonical vertex-transitive orientations of the complete graph with the **same** 23 sites and eleven out-neighbors display completely disjoint nontrivial cycle periods, four and twenty-three, and have markedly different oscillatory attraction fractions. The complete census and sharp clocks isolate an interpretable structural effect of orientation geometry, providing reference data for directed threshold systems rather than merely recomputing an arbitrary graph invariant.

## Scientific limitations
The result is finite, and the computational proof relies on correct execution of the supplied fully enumerative C++17 sources. It has not undergone independent mathematical audit or priority adjudication. Published one-dimensional automaton results may encode some carousel facts after additional deductions; this limitation is factored into the originality assessment.

Self-review: passed. Independent audit: not yet performed.
