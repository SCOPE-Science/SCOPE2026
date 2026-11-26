# Independent mathematical audit

## correctness

PASS

Every profile's value must lie in the unique joint cell for its action blocks. For a doubleton, a fixed copy must see both symbols in its slice of that cell; partitions ensure that profiles outside that cell cannot supply either symbol. If fewer than two axes have length at least two, fixing the only potentially varying axis leaves a one-entry slice. If two axes vary, parity of their copy indices supplies both outcomes in every fixed-action slice, even for budgets greater than two. Singleton cells use their only outcome and impose no constraint. The cell constructions glue because joint cells partition the outcome set and all type triples are allowed. Each triangle needs two doubled vertices exactly when every one of its edges is covered. Extra copies beyond two are removable without violating feasibility, and isolated vertices need only one. Thus all optimum vectors correspond exactly to minimum covers and the displayed example has total 8. Independently tested 38 small cell shapes with bitmask slice-surjectivity enumeration, not the parity construction (`python3 /workspace/frozen_review_replay.py 4`); this is bounded corroboration. The frozen script was read, not run.

## originality

PASS

The supported claim is the exact per-block heterogeneous three-agent budget region and its instance-specific minimum for transverse binary refinements. General representability, modular addition as a construction, the two-agent rectangular region, and elementary graph-cover duality are not claimed original. The strongest accessible comparisons do not give this quantitative three-way classification or its graph reduction.

## value

PASS

This resolves the cost of exact simultaneous-action representation for a natural class where a qualitative theorem leaves the cost open. It identifies all per-block feasible budgets and reduces the exact instance-dependent minimum to a graph computable from the refinement; this permits nonuniform optima that the uniform-copy existence constructions do not explain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
