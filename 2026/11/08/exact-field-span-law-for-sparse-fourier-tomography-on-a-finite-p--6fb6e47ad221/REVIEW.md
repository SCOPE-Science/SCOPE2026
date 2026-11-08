# Self-review

## Correctness — PASS
The complete Fourier data along each frequency line are equivalent, by finite-field character orthogonality, to every fiber sum of the quadratic map \(t\mapsto t^2-ct\). The fibers give exactly the involution relations \(f(c-t)=-f(t)\), including the unique fixed point. Composing two involutions yields invariance under the prime-field span of the offset differences. The quotient has odd cardinality and its reflection has one fixed coset, giving a complete explicit kernel basis and hence the stated nullity, rank, support minimum and sharp uniform sparse-identifiability threshold. Affine dimension immediately yields the optimal complete-view budget. The proof covers every odd prime power and every nonempty offset set. A standalone checker additionally verified 390 offset configurations (including a genuine extension field) by exact rational incidence rank and separate numerical Fourier matrices. Numeric tests are not used as an infinite proof.

## Originality — PASS relative to available scientific comparisons
The recent source Lewko, arXiv:2606.22882, studies nonlinear Fourier extension estimates on paraboloids, not rank of unions of complete frequency lines. Feldman–Grinberg, arXiv:1707.06695, studies the projective X-ray transform and minimal admissible line complexes on another domain; only an abstract and subject summary were available. Two highly relevant indexed results were compared: one concerns **unit-conic two-view** tomography with multiplicities governed by norm-one-torus rotations, and another concerns **coordinate-character** Gram spectra on higher-dimensional paraboloids. Neither available statement implies the prime-subfield affine-span kernel formula for the parabola. The full indexed files could not be accessed; that is a residual originality risk, as is possible older finite-field Radon literature. The positive judgment is best-knowledge, not a claim of exhaustive novelty or independent certification.

## Value — PASS
This is a complete, sharp sampling-design classification rather than an arbitrary finite census: it determines the invisible subspace for every choice of nonhorizontal complete frequency-line views, the exact minimum support of invisible signals, and a necessary-and-sufficient uniform sparse-recovery threshold. Its field-extension barrier is operationally substantive: two views suffice for prime fields, but \(m+1\) affinely spanning views are required in degree \(m\), even though incomplete views can still recover all signals below a sharp sparsity threshold.

## Scope and risk
No statement about stability under noise, arbitrary partial frequency selections, phase retrieval or characteristic two. The relation of the result to older general discrete-tomography theorems may merit further independent comparison. The standalone code is corroboration, not an independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
