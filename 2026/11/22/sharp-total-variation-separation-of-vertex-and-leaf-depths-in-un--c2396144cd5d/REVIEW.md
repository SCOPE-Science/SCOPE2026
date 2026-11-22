# Scientific review

## Correctness — PASS
The vertex pgf follows from uniform-parent recursion. Leaf survival is independent of birth depth; exact leaf-size-biased sampling gives a second product pgf. A log-concave Bernoulli convolution has the required single mode, giving the half-mode TV identity. Exact leaf-count variance yields the ordinary-sampling error, and a Fourier local limit theorem gives the leading constant. The checker passed 99 exact-rational/numerical assertions; infinite assertions rest on the written analytic proof, not enumeration.

## Originality — PASS within inspected scope
Closest source: Lundblad and Wagner, [2026 conference paper](https://doi.org/10.4230/LIPIcs.AofA.2026.2), first public July 13, 2026, and [expanded preprint](https://arxiv.org/abs/2611.16674), November 12, 2026. They compare per-tree average depths and moment differences, not annealed depth-law TV. Published nearby results concern Gaussian mean-gap fluctuations or leaf-label conditioning; neither found theorem asserts the displayed sharp ordinary-leaf TV constant. Panholzer–Prodinger (2007) and Elizalde (2024) study node/leaf depths, but the Elizalde full paper was not accessible, leaving a concrete historical-priority risk. Search absence is not proof of uniqueness.

## Value — PASS
The precision is motivated by vertex versus leaf depth sampling in recursive trees, where equality of limiting normalized mean statistics does not quantify distribution-level distinguishability. The new exact sampling coupling and sharp \((\log n)^{-1/2}\) total-variation rate resolve a natural whole-distribution comparison; the finite \(n\) bound ensures that the practically relevant tree-first leaf law is genuinely covered.

## Limitations
Uniform recursive trees, annealed distributions, no claim of quenched TV convergence or of exact finite pgf under ordinary uniform leaf sampling. The standard versus size-biased distinction is essential. Unreviewed classical full texts remain a historical-priority risk; independent assessment has not been conducted.

Self-review: passed. Independent audit: not yet performed.
