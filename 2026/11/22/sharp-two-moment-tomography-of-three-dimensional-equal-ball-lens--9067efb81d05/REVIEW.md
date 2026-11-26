# Independent mathematical audit

## correctness

PASS

For a>0 each supporting sphere contributes the cap on the opposite side of the midplane, and both have area 2πR²(1−a). Sphere area in axial coordinate and azimuth is constant; the seam has measure zero and at a=0 the construction partitions a sphere into hemispheres. Independently integrated the two-point fourth power by averaging over the azimuth difference, treating same-cap and opposite-cap pairs separately. For b=1−a and R=1 this gives μ=2b and ν=4b²(b²−2b+5)/3; scaling restores the stated R factors. The dimensionless ratio (4+a²)/3 is strictly increasing on [0,1), so a and then R are uniquely recovered; the ball is included and a=1 excluded. The bound follows from |a₁²−a₂²|≥|a₁−a₂|², with equality against a=0 setting the constant and exponent. One positive even moment can be held fixed over varying a by scaling R. The independently integrated one-cap case also gives the claimed shared wedge, with distinct surfaces off the full-sphere endpoint. Replay: python3 /workspace/reproductions/review_04_lens.py (SymPy, exact integrals). The frozen symbolic/simulation checker was inspected, not run. No volume-sampling, unequal-ball, noisy-estimation or uniform radius-stability claim is verified; collapse as a→1 refers to fixed R. The two moments recover absolute scale as well as shape.

## originality

PASS

The exact moment law and sharp separation inverse are supported as distinct for the entire equal-ball lens boundary. The single-cap wedge is verified overlap, not an originality claim; the lens realization of the same wedge gives the ambiguity. The generic iid-pair expansion and the geometry of spherical zones are not claimed as new.

## value

PASS

This is a complete inverse law for two natural rigid-motion invariant statistics on a geometrically motivated family. It specifies what can be recovered from two moments, the sharp loss of resolution near a ball, and a concrete ambiguity if the family is unknown. These are not consequences of a general distance expansion alone, and they are exact population statements, not statistical guarantees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
