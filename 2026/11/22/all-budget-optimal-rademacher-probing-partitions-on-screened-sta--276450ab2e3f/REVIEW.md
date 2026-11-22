# Scientific review

## Correctness — PASS
The off-diagonal entries of the screened star inverse follow by direct Schur complementation and imply exactly two pair weights in the class-probe variance. Pairwise balancing and the strictly increasing integer first differences establish the global minimum and classify every minimizer for all \(m\ge2\), \(3\le k\le m+1\), and \(\mu>0\). The special case \(k=m+1\) has only one feasible hub occupancy and is explicitly included. The accompanying exact arithmetic verifier evaluates 35,280 admissible finite partitions and confirms both the entry formula and the variance comparison; computation supplements rather than establishes the infinite-parameter proof.

## Originality — PASS, with residual risk
The 2023 stochastic-probing variance identity concerns a fixed partition and is used, not claimed as new. A directly relevant public theorem on complete bipartite resolvents, including stars, completely solves the \(k=2\) case but explicitly leaves budgets above two unoptimized. All budgets \(3\le k\le m+1\), their occupancy minimizers and the exact budget-sensitive properness transition are therefore not implied by that theorem. The 2021 multilevel trace-estimation and 2013 hierarchical probing articles do not supply the all-budget star classification. An older symmetric weighted-partition or balanced-clustering theorem could be equivalent and remains the main publication-priority risk.

## Value — PASS
Optimal partition selection under a fixed number of sparse sign probes is the natural design question arising from stochastic trace estimation. This result gives all optimizers and the exact risk for every budget and shift on the canonical hub-and-spokes graph, and reveals a sharp condition under which a standard proper graph coloring fails the variance objective. The exact \(k=3\), nine-leaf example saves \(7/64\) of the variance with no extra quadratic forms. Its value is a complete structural benchmark on a natural family, not a claimed advance for arbitrary graphs or wall-clock performance.

## Closest work and remaining limits
Frommer, Rinelli and Schweitzer, arXiv:2308.07722v1, Theorem 3.3 and Lemma 3.5; *Sharp two-color stochastic-probing transition on complete bipartite resolvents* (2026); Hallman and Troester, arXiv:2103.10516v1; Stathopoulos, Laeuchli and Orginos, arXiv:1302.4018. The model requires exactly one independent sign probe on each of \(k\) disjoint nonempty classes, with no optimization over correlated probes or unequal repetitions. Priority relative to specialized older weighted clustering remains provisional.

Self-review: passed. Independent audit: not yet performed.
