# Scientific review: phase-shifted triangle Lissajous sextic

## Correctness — PASS
The specified sextic is exactly the phase-shifted triangle equation printed in Mascarin, Example 3.10. Its normalization is proved directly, rather than inferred from the trigonometric parametrization: the normal smooth torus ring is a finite birational extension, as witnessed by a nonzero determinant for the basis \(1,x,x^2,x^3\) over \(\mathbb C[y,z]\). The four exact algebraic conductor identities prove \((xyz)R\) lies in the conductor, while the generic two-preimage property on all six prime components proves the reverse inclusion. The remaining local calculations explicitly identify double crossings, twelve pinch germs and four distinct branches at the origin. Exact symbolic identities were rerun with the accompanying checker. Main risks are addressed by the explicit restriction to the affine complex surface and by separating computational identities from geometric arguments.

## Originality — PASS, with residual priority risk
The starting sextic and its Lissajous/Kuramoto interpretation are already in [1, Example 3.10] and [2]; no priority is claimed for the equation. The current paper's Section 5 gives general singular-locus inclusions and an exact hypersurface formula under an ambient-dimension condition excluding this triangle example. A complete local-type classification and exact conductor of this sextic were not found in the accessible full texts. Focused published-finding corpus searches returned other normalization/conductor and oscillator findings, but none whose statement implies the conductor equality and all three singularity strata for this polynomial. Related known Chebyshev surfaces and trigonometric curves concern different objects; those statements do not imply this calculation. Search absence is not proof of priority: previously unpublished, unindexed or overlooked local analyses are a residual risk.

## Value — PASS
This is the basic three-cycle phase-shifted Lissajous surface used to encode Kuramoto equilibria. Determining its normalization and conductor is intrinsically motivated by the paper's unresolved nonnormal/singularity geometry; the precise pinch and multibranch strata distinguish different mechanisms of failure of local normality that cannot be read from the defining polynomial's degree or from a mere set-theoretic singular-locus bound. The explicit conductor also provides the gluing data needed for subsequent local and scheme-theoretic study. The result is not a generic formula for arbitrary Lissajous hypersurfaces; its value lies in completely settling a small central example.

## Closest literature and limits
[1] F. M. Mascarin, *Intersections, Equations, and Singularities of Lissajous Varieties*, arXiv:2611.15725v1, Example 3.10 and Section 5 (full accessible HTML inspected): equation, intersections, general inclusion criteria, but not this exact conductor or local stratification.

[2] F. M. Mascarin and S. Telen, *Lissajous Varieties*, arXiv:2509.06844v2 (full accessible HTML inspected): parametrization, defining relations and applications; no matching conductor/local theorem identified.

The present result covers the affine complex surface only. It does not assert the projective singularity census, full Jacobian ideal structure or an independent review.

Self-review: passed. Independent audit: not yet performed.
