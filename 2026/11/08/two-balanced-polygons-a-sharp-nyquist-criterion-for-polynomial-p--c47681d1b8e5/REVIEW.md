# Self-review

## Correctness — PASS

The sampling transform of a pair of degree-\(d\) real trigonometric intensity profiles has \(4d\) real degrees of freedom after identifying the normalized top coefficients. Discrete Fourier orthogonality determines every lower mode and leaves exactly two top-mode real equations. Their coefficient determinant is \(-\sin(d\alpha)\), nonzero precisely on the theorem's domain. Continuous equality on both radii then gives rational reflection identities and dilation invariance, forcing the quotient of the polynomials to be a constant of modulus one. Explicit paired polynomials show every excluded condition really fails. The argument covers arbitrary coefficients, zeros, and lower degrees. The attached arithmetic checker corroborates \(5148\) finite identities; its output is not used as the infinite proof.

## Originality — PASS (historical priority provisional)

Pohl–Li–Boche [2], Theorem 7, is the closest finite two-circle design. It uses \(2d+1\) samples on one circle and \(2d-1\) on the other, with interpolation relying on that unbalanced split; it neither asserts injectivity of two equally sized \(2d\)-point polygons nor its exact angular resonance. Chalendar–Partington [1] covers all-point sampling on two circles but not their discrete reduction. Bodmann–Hammen [3] uses intersecting circles and Przybyłek–Siedlecki [4] a substantially larger grid. These distinctions concern logical implication, not titles. The degree-two two-square case is already known as an individual instance and is deliberately excluded. An unlocated general theorem for balanced finite analytic sampling remains a residual historical risk.

## Mathematical value — PASS

Balanced angular orbits are a natural structured design, not an arbitrary parameter slice. The theorem gives an all-degree \(4d\)-sample reconstruction with exact, rather than merely sufficient, angular feasibility; the obstruction is a genuine discrete Nyquist alias and produces constructive non-retrieval examples. It also shows the measurements invert an entire natural \(4d\)-dimensional real harmonic-profile space, a useful reduction for algorithms and conditioning analysis. Existing \(4d\)-count theorems do not settle this balanced design or its failure boundary. There is no asserted improvement of the known unrestricted measurement count or noise-optimality theorem.

## Closest sources and limitations

[1] Chalendar–Partington, arXiv:2403.16255, full PDF examined. [2] Pohl–Li–Boche, DOI:10.1109/SAMPTA.2017.8024411, accessible author-uploaded full text inspected through Theorem 7. [3] Bodmann–Hammen, arXiv:1302.5487, full PDF examined. [4] Przybyłek–Siedlecki, arXiv:1907.09371, full PDF examined including Theorem 4.2. The theorem covers regular concentric polygons and noiseless intensities, not arbitrary points or full nonlinear stability.

Self-review: passed. Independent audit: not yet performed.
