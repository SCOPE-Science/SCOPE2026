# Scientific review: line-pencil Fourier synthesis

## Correctness (C): PASS

The proof minimizes a strictly convex fourth-power Fourier moment subject to one fixed nonzero Fourier coefficient. Scalar-dilation invariance forces constant values on punctured lines; character orthogonality computes the exact \(q^2\)-frequency Fourier moment. Crucially the moment has a **permutation symmetry of direction amplitudes** even when the geometric point set lacks projective symmetry. Strict convexity forces equal real amplitudes. The one-variable quartic is minimized analytically, including the one-line and full-plane boundaries. Explicit unitary versus raw Fourier normalizations cancel in the ratio. A standalone Python checker passed 3,015 finite-field and random-complex-signal checks; the proof, not the checker, covers all prime powers. Risk: the mathematical conclusion requires the indicated counting-measure normalization, not a normalized probability measure.

## Originality (O): PASS relative to inspected evidence

The exact affine-transitive theorem of Iosevich–Li–Yu (arXiv:2609.25404, 2026-09-21, Section 4, Theorem 4.1) has a hypothesis absent from proper line pencils, whose shared intersection is distinguished. Its indicator maximizers do not encompass the nonuniform and negative-center extremizers. Bhowmik–Deodhar–Iosevich (arXiv:2508.12194, 2025-08-17, Theorem 5) provide a nonsharp-for-this-class indicator-based estimate. A prior exact computation for two coordinate axes is a genuine \(k=2\) specialization, rather than an independent novelty claim. The new statement is the complete arbitrary-direction, all-\(k\), all-prime-power invariance theorem; the previously inspected three-line Fourier sampling literature concerns matrix rank, not this fourth-power synthesis constant. Finite-field restriction/extension norms run in the opposite inequality direction. Risk: a mathematically equivalent projective-line arrangement result may exist under different nomenclature; bibliographic searching is not an exhaustive proof of novelty.

## Value (V): PASS

There are \(\binom{q+1}{k}\) direction selections, not all projectively equivalent. A universal sharp constant and complete equality cases across these configurations are an exact natural classification. The result reveals an unexpectedly larger permutation symmetry of the minimization than the geometry permits, and an explicit change from positive to signed center weights. This supplies a structural and quantitative benchmark for spectral synthesis on finite-field arrangements beyond affine-transitive supports, rather than a routine evaluation of one example.

## Limits and closest work

The result is confined to concurrent lines in a two-dimensional field vector space, fourth-power Fourier synthesis and counting-measure norms. Sources considered are the full HTML texts of arXiv:2609.25404 and arXiv:2508.12194, published records on finite-field line sampling and Fourier extension, and the previously established two-axis specialization. Prior-result comparisons concern statements and implications, not title matches. Residual bibliographic uncertainty remains; no independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
