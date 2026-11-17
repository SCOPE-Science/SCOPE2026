# Scientific assessment: full nine-vertex volume-Hessian spectrum

## Correctness — PASS

The 20 tetrahedral facets of the square–pentagon orthogonal free sum have strict supporting gaps to nonincident vertices. Thus the standard oriented facet-volume polynomial is a genuine local volume formula, not merely a formal extension. The spherical chart in RESULT.md parametrises all 27 tangent degrees of freedom, and a direct second-order expansion of the two area bivectors yields the displayed quadratic form. Tight-frame decompositions produce an exact sum of squares and a complete 27-eigenvalue spectrum, with precisely the six orthogonal-rotation modes in the kernel. The tubular-neighbourhood argument converts its minimum positive coefficient into the sharp asymptotic orbit-distance deficit. The standalone verifier passed 2,993 independent finite checks, including a full numerical Hessian and 300 random directions; independent convex-hull tests also agreed with the predicted second variation. These checks support, but do not replace, the analytical proof.

## Originality — PASS (subject to historical-priority limitations)

Medgyes (arXiv:2611.10078v1) established the global nine-vertex optimum and the Hodge-star area-vector factorisation. Those facts are inputs and are not claimed as new. Its available abstract, introduction, preliminaries, and beginning of the factorisation proof describe a sharp volume bound, not the complete constrained quadratic spectrum or its least positive eigenmode. The closely related published sharp Hessian result for **seven** vertices has different vertices, dimension of tangent space, and extremal configuration; no implication of this nine-vertex computation follows. A prior local stability result for a **three-dimensional** nine-vertex spherical polyhedron likewise does not cover this four-dimensional object. An existing nine-vertex simplex-volume result concerns the same object, but that concerns sub-simplex volumes rather than variation of the full polytope. Targeted research-index searches for the square–pentagon Hessian, Fourier modes, and stability modulus found no equivalent statement. **Risk:** The later sections of the same November 2026 paper were not accessible for a complete text-level comparison during this assessment; a historic equivalent calculation under other terminology remains possible. Search absence alone does not prove novelty.

## Mathematical value — PASS

The complete constrained Hessian is a natural quantitative stability invariant of the first solved nine-vertex maximum-volume problem on the three-sphere. In contrast with merely differentiating one angular coordinate, the computation classifies **all** 27 independent spherical vertex directions, rigorously identifies and removes all six rigid-motion zero modes, and determines the sharp coefficient for ordinary Euclidean distance to the unique maximizing orbit. Its softest mode is an explicit first Fourier harmonic of the pentagon, which identifies the actual slowest loss of volume. No unproved downstream theorem is needed for this intrinsic complete classification to be valuable.

## Limitations and priority

The resulting inequality holds only locally and with arbitrary positive loss from the asymptotically sharp coefficient. It does not provide global quantitative stability, a new maximum-volume value, or an independently audited theorem. The motivating article's later full text could not be inspected, leaving a specific priority uncertainty. All claims are confined to the proof and checks described in RESULT.md and VERIFICATION.md.

Self-review: passed. Independent audit: not yet performed.
