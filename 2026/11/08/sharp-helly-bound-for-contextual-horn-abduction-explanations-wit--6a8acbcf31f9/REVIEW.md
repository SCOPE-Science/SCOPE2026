# Review of the sharp Horn-obstruction rank theorem

## Correctness
**PASS.** For fixed context, forward-chaining entailment is upward-monotone and consistency is downward-monotone, hence the valid explanation family is order-convex. A minimal empty intersection supplies one witness per omitted context; those witnesses cannot contain a three-term strict inclusion chain. The generalized two-level Sperner bound yields the explicit upper limit. Sharpness is supported by a constructive Horn compilation of the order-convex families obtained by deleting one element from the two middle levels. Every claimed context family is evaluated by elementary closure semantics; the finite checker reproduces the witness law through eight hypothesis atoms and exhausts the upper combinatorics through four. Boundary \(h=0\), locally feasible sharp cases \(h\ge1\), and unrestricted rule width are distinguished.

## Originality
**PASS under presently inspected evidence, with priority risk.** Yang's arXiv:2610.32805v1, Sections 4.3 and 6.1, contains the \(2^h\) upper bound and the order-convexity observation, but does not state the sharp unrestricted \(B_h\) law or a fixed-hypothesis extremal compilation. Its rectangular-slot theorem is not the unrestricted case. The two-level Sperner inequality is a classical ingredient, not new. The closest separately established observation-contract result concerns minimum source-context counts for realizing a *contract*, not the maximum size of a *single minimal obstruction* with a fixed hypothesis budget. Remaining uncertainty concerns older abstract order-convexity Helly theorems and potentially unpublished exact corollaries.

## Value
**PASS.** The number of hypotheses is a natural representation resource in abductive reasoning. This theorem supplies its exact obstruction-rank capacity and distinguishes acyclic Horn constraints from unrestricted abstract explanation tables. The gap between the old \(2^h\) ceiling and the attained \(B_h\) grows to a factor on the order of the square root of the hypothesis count. The construction works with locally feasible explanations for every nonzero budget, making the bound relevant to higher-order observation obstructions rather than trivial inconsistent instances.

## Scientific limits
The number and width of construction rules are unrestricted; no efficient algorithm or optimal formula length is asserted. The upper bound is a direct use of a classical extremal set theorem. Known geometric Helly results use a different convexity. Independent historical priority confirmation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
