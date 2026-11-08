# Review of the vertex-retention volume-budget theorem

## Correctness — PASS

The volume of a retained-vertex hull is exactly the number of admissible coordinate orthant simplices times the simplex volume, except that the all-singleton case has zero full-dimensional volume. This yields the stated product-difference expectation for arbitrary independent vertex probabilities. Internal antipodal balancing decreases every singleton factor without changing pair sums. The external balancing step is not a bare AM–GM assertion: the derivative of the exact two-variable objective with respect to the pair product is strictly positive whenever the pair sums differ. It proves global sharpness and uniqueness. The argument is valid for any nonsingular linear deformation and every integer dimension at least two.

The actual standalone geometric checker enumerated independent Bernoulli vertex masks and computed convex-hull volumes with SciPy/Qhull in dimensions two through four. It matched the analytic expectation; additional constrained random tests agreed with the inequality. No numerical result is used to assert a theorem for all dimensions.

## Originality — PASS, historical priority provisional

Newman (arXiv:2006.07000, 2020) introduces the iid-retention model for vertices of general polytopes in a two-stage random construction and obtains complexity bounds, not a globally optimal nonidentical-probability volume design. A previously obtained equal-probability face–volume law for thinned cross-polytopes provides the uniform specialization, but not the present heterogeneous optimization theorem. Kabluchko's 2020 random convex-cone and half-sphere results concern distinct random objects. Targeted searches did not identify the same sharp inequality under unequal inclusion probabilities. Search non-detection cannot prove historical priority; a reformulation in sampling design or a general multilinear-extremal theorem remains a residual risk.

## Mathematical value — PASS

The expected volume is a natural measure of fidelity when a high-dimensional cross-polytope is approximated by independently retaining vertices. Under one fixed expected number of sampled vertices, the result determines the globally optimal design and proves its uniqueness in the full \(2n\)-parameter probability cube. It makes a shape-independent statement for all linear images, and the strict two-stage balancing proof is not implied by knowing the expected volume along the uniform-probability diagonal. This is a complete natural optimization classification rather than an arbitrary finite numerical case.

## Remaining limitations

The theorem excludes correlated and fixed-cardinality sampling and objectives other than expected full-dimensional volume. A second scholar should independently check historical priority and the proof.

Self-review: passed. Independent audit: not yet performed.
