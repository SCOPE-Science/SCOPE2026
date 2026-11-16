# Mathematical review

## Correctness

PASS. The Fourier transform creates \(n\) independent two-vector Gram blocks from the normalized Fock kernels. Differentiating vectors in Fock norm and calculating the rank-one orthogonal complement gives the exact quadratic collision coefficient as the conditional Poisson variance. A roots-of-unity filter yields an exact derivative representation. Isolating the two closest nontrivial roots in that finite sum gives an exponentially small but sign-changing oscillatory correction; its uniform error is smaller than the gap between the prescribed sector and all others at the explicit radius sequence. Small-radius behavior follows from the first two nonzero Poisson probabilities, not numerical extrapolation. The supplementary finite checker passed 125 assertions.

## Originality

PASS under the inspected literature and database evidence, with residual publication-priority uncertainty. Horoshko et al. (arXiv:1602.07852, Section II) supply a single-circle circulant kernel spectrum, not radial two-orbit collision or Poisson-conditional variance coefficients. Fang–Tien (arXiv:2609.23572) prove qualitative density criteria for infinite sampling/interpolation in mixed-norm Gaussian Fock spaces, not finite two-ring Gram weak directions. Kellay–Omari (arXiv:2603.14679) concern complete interpolating sequences in other radial-weight Fock-type spaces. Semantic searches on the public mathematics record found no matching two-concentric-orbit recurrence claim. This does not certify that equivalent work is absent from the older coherent-state literature.

## Value

PASS. Stable finite interpolation deteriorates dramatically when two circular sampling orbits merge. The theorem supplies exact conditioning constants, sharp small-radius factorial collapse, and a non-obvious recurrent switching of the worst symmetry sector at arbitrarily large radii. This distinction between convergence of all sector coefficients and nonconvergence of the identity of the weakest sector makes the result a motivated stability feature rather than a generic two-vector Taylor calculation.

## Limitations and closest literature

The conclusions hold for fixed finite polygon order and radially aligned concentric orbits in the Gaussian Hilbert Fock space. The collision limit precedes the large-radius limit. The closest directly relevant primary text is Horoshko et al. (2016), read in its circular-state calculation section; it does not, in the inspected parts, contain the new two-radius recurrence statement. The 2026 mixed-norm and Fock-type interpolation papers address distinct density and weight regimes. Other variants under coherent-state or signal-processing terminology remain an originality risk.

Self-review: passed. Independent audit: not yet performed.
