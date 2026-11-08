# Scientific review

## Correctness — PASS

The statement uses the real SPD screened cycle \(A_\mu=(\mu+2)I-P-P^{\mathsf T}\), even \(n\ge4\), positive \(\mu\), and two nonempty disjoint probe supports. The cyclic Green recurrence gives the exact inverse. Rademacher pair-product orthogonality reduces the variance minimization over all partitions to the Rayleigh minimization of the squared-Green circulant. Its explicitly summed Fourier spectrum has a unique lowest eigenvalue at the alternating frequency, so the only binary minimizers are the two alternating signs. Direct geometric summation proves the minimum and exact independent-two-probe comparator. All signs and boundary limits are checked analytically. A standalone standard-library exact-rational replay passed 33,861 assertions, which supplements rather than replaces the proof. No stronger statement is inferred from finite sampling.

## Originality — PASS (best-knowledge assessment)

The nearest detailed comparison is Frommer–Rinelli–Schweitzer (arXiv:2308.07722, Section 3.2, Theorem 3.3): it supplies the general within-color variance, which is used and acknowledged. It does not give a global minimum over **every** two-color partition for a screened cycle, its uniqueness, or the exact same-cost variance gap. The lattice-coloring discussions of Switzer et al. (arXiv:2106.01275), Stathopoulos et al. (arXiv:1302.4018), and Frommer–Schimmel–Schweitzer (arXiv:2009.01589) motivate local and hierarchical distance colorings, not the exact all-partition quadratic optimization here. Related earlier mathematical statements concern unstructured Hadamard-row probing, tensor probe variance, exchangeable signs for diagonal estimation, and dependent probes of two trace functions; none implies this variance-minimizing screened-cycle coloring for every screen. Source and equivalence queries were conducted against the research index and literature. Unknown older results on circulant antiferromagnetic quadratic minimization pose a residual precedence risk, rather than proof of novelty.

## Value — PASS

Trace-of-inverse estimation for sparse periodic operators is a recurring numerical task. A graph-distance-one checkerboard is intuitively plausible, but it is not automatically the globally best stochastic partition when the inverse is dense and contains contributions at every graph distance. Here an exact positive-screening-independent optimizer and uniqueness theorem settle that question, and an explicit finite-\(n\) variance formula allows algorithm-cost comparisons, not only asymptotic error bounds. It certifies strict variance improvement over the natural same-cost two-probe baseline for every parameter and identifies its large-cycle and near-singular limits. This is a complete, interpretable design benchmark; its scope is intentionally not generalized to arbitrary matrices or sampling laws.

## Closest literature and remaining risks

The result is an exact specialization of a general variance identity followed by a nontrivial optimization of its full dense covariance, not a new trace-estimator construction. The link with classical Fourier Rayleigh bounds and antiferromagnetic circulant sign energies may permit earlier equivalent formulations. The primary papers were inspected in their pertinent full-text sections. No independent scientific evaluation has been performed.

Self-review: passed. Independent audit: not yet performed.
