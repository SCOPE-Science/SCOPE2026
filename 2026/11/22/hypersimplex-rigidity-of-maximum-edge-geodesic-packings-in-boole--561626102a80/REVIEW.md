# Scientific review: hypersimplex rigidity of cube edge-geodesic packings

## Correctness — PASS
For each \(d\ge2\) and \(2\le t\le d\), uniform averaging over antipodal geodesics supplies the known sharp objective bound \(t2^{d-1}\). Equality saturates every antipodal geodesic, not merely their mean. Two choices of a two-edge square route, each completed by an identical remaining-coordinate tail, yield the independent identities \(a+c=b+h\) and \(a+b=c+h\). They force opposite-square edge weights to coincide. Hypercube square connectivity propagates these equalities along each coordinate class. All feasible optimal fractional weights therefore correspond exactly to \(\Delta(d,t)\); its integral points give the optimum set classification and \(\binom dt\) count. No unproved auxiliary combinatorial lemma or finite-to-infinite inference is required.

In addition, every optimum was exhaustively checked for \(d=2,3\) across all eligible \(t\), and complete integer-programming enumerations checked \(d=4,t=2,3\), including exclusion of every other maximum. Each program is supplied in full with reproducible output; the finite checks corroborate, rather than certify, the all-dimensional proof.

## Originality — PASS (provisional publication priority)
The primary 2021 paper, arXiv:2105.04292, Theorem 3.2, proves the optimum size for capacity two and constructs a pair of coordinate classes. Its proof does not derive all-case rigidity. The 2022 generalization, arXiv:2207.07357, Theorem 4.2, proves the optimum value for each admissible capacity, again not the equality-case classification or the fractional optimum face. The related 2023 partial-cube paper studies Fibonacci and Lucas cubes, and a 2024 extremal paper studies different graph families. A previously computed four-dimensional finite case counts six optima, consistent with this theorem; it cannot imply every dimension and capacity. Searches under all-optima, coordinate-class, equivalent linear-programming, and hypersimplex formulations found no published all-parameter classification.

Risks: unindexed dissertations, subsequent preprints, and alternative descriptions of the same polyhedral face may exist. A 2025 subscription article has an accessible abstract describing small-diameter graph families, but not accessible full theorem details; its scope appears distinct. This is a best-knowledge priority assessment, not proof of global uniqueness of publication.

## Mathematical value — PASS
The existing literature determines \(t2^{d-1}\) but does not, in the inspected results, say what every maximizing edge configuration looks like. The new opposite-square saturation lemma is a nontrivial equality mechanism covering every dimension and every allowed capacity. The entire optimal LP face is the standard hypersimplex, which simultaneously gives integrality of all vertices, exactly \(\binom dt\) maximum edge sets, and the optimizer-face dimension. This is a natural, all-parameter structural refinement of an established extremal problem, not a routine recomputation of a single minimum.

## Scope and limits
Only Boolean cubes, ordinary graph geodesics, capacity \(2\le t\le d\), and the explicitly defined box-constrained fractional relaxation are treated. Arbitrary feasible subsets and other partial cubes are not classified. Independent external mathematical validation and exhaustive publication-priority clearance have not been performed.

Self-review: passed. Independent audit: not yet performed.
