# Scientific review: exact constructible image of the minimal two-block rank-one map

## Correctness — PASS

The claim is quantified over **all fields**, including characteristic two. The proof gives both a necessary obstruction and an explicit construction in all remaining cases. Its critical linear-algebra lemma is elementary: a nonscalar two-by-two operator has a cyclic vector, so the linear functional satisfying two prescribed evaluations exists. Scalar operators force the exact quadratic obstruction \(\lambda(\lambda-1)=0\). All geometric claims follow from a rank-one \(4\times2\) determinantal cone, and the finite-field counts follow from multiplying \(q-2\) by \(\#\operatorname{GL}_2(\mathbb F_q)\). The accompanying exact-arithmetic checker exhausts fields of orders two, three and four, but the proof, not the experiments, establishes the infinite-field theorem.

## Originality — PASS, qualified

Alexandr, Grillo, Holleben, Montúfar and Yu, arXiv:2611.23846v1, Theorem 1 characterize the Zariski closure; Example 3 proves one pair is omitted; Proposition 4 decides when the entire image is closed. None states all missing points in the minimal three-neuron case. The original paper explicitly leaves pointwise representability as a separate question. Closest comparisons include Alexandr–Montúfar (arXiv:2508.03867v2), Finkel–Fu–Wu (arXiv:2611.20346v1), and public nearby low-rank completion records. The new if-and-only-if is not a logical consequence of knowing a closure and one excluded point. Searches and actual source inspections are recorded in `AUDIT.json`. Residual publication-priority risk persists from unindexed simultaneous rank-one perturbation or pencil literature; originality here is best knowledge, not established uniqueness.

## Value — PASS

The selected \((2,3,2)\) architecture is the first possible nonclosed one under the known closure criterion. Its closure has no equations, yet precise parametrization misses a structured codimension-three set. Characterizing exactly that discrepancy supplies a natural and complete algebro-geometric invariant of the motivating example. The geometry of the missing set and all finite-field attainment counts follow with no further conjectures or numerical assumptions.

## Boundaries

This is a theorem about the formal algebraic two-pattern parameter map, not about real activation-cell feasibility. The standard Segre cone is not claimed as a new variety; its exact role as the complete missing-locus closure is the contribution. The result does not classify larger architectures or assert independent validation.

Self-review: passed. Independent audit: not yet performed.
