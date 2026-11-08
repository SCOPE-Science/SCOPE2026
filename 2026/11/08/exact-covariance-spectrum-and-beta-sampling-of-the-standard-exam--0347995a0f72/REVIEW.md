# Scientific review — standard-example order polytope

## Correctness — PASS
The proof disintegrates Lebesgue volume by the two largest lower coordinates, verifies the exact beta laws, and uses independent uniform interval factors to reconstruct the full conditional joint law. Explicit beta moments and level-complementation yield the covariance orbit entries. Block diagonalization under simultaneous permutations gives the four rational spectral branches with stated multiplicities; all numerators are positive, and the correlation gap and isotropic limit follow algebraically. An independent ordered-simplex enumeration checked all first and second coordinate orbits in dimensions \(4,6,8\) without discrepancies. This finite replay corroborates, rather than certifies, the all-\(n\) proof.

## Originality — PASS (historical priority provisional)
The closest exact-object prior is Reilly, Scheinerman and Zhang (2014), Proposition 14, which **already establishes the volume** and rank order count. The volume is explicitly credited, not submitted as new. The 2021 generalized-snake order-polytope work by von Bell et al. supplies triangulation context but does not state the same-object second-moment spectrum. Chan and Pak (2022) prove general inequalities for weighted poset partitions rather than the evaluated continuous covariance entries. The closely named cyclic-crown family is geometrically different for \(n\ge4\). No inspected claim logically covers the submitted beta sampler plus exact four spectral branches and correlation gap. The strongest remaining risk is an earlier evaluation under conditional threshold weights or random linear-extension terminology; no search can establish universal priority.

## Value — PASS
The standard example is the central extremal poset-dimension construction, making its order-polytope covariance a natural invariant rather than an arbitrary slice. The exact sampler is useful for geometric simulation and all-degree integration. The evaluated four-branch spectrum, strict matched/unmatched cross-correlation gap, and isotropic-constant limit provide a full-dimensional geometric classification not captured by the classical volume count alone.

## Closest literature and limitations
Reilly–Scheinerman–Zhang, *Random Threshold Digraphs*, EJC 21(2), P2.48 (2014); von Bell et al., arXiv:2102.11306 (2021); Chan–Pak, arXiv:2212.11954 (2022). The claims cover only \(n\ge2\) and standard Euclidean coordinates; they are not assertions about every height-two poset or cyclic crown. The code checks only three finite dimensions, and historical priority remains provisional.

Self-review: passed. Independent audit: not yet performed.
