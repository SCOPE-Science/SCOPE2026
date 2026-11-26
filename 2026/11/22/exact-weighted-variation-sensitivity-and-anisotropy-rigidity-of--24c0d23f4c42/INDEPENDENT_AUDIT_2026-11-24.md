# Independent mathematical audit

## correctness

PASS

For a fixed contact chain, chord interpolation Q replaces the increments on [a,b] by the total increment on the block distributed proportionately to the knot gaps. Its weighted nodal variation on that block is the length-weighted average edge weight times |h_b-h_a|, bounded by the displayed block ratio times the input block variation. The region where the chain gives the hull can be described by closed linear inequalities: increasing chord slopes in the non-strict sense and data on or above the chords. Such a chordal interpolation is the GCM since it is feasible and any convex minorant lies below the chords between its endpoint contact bounds. These finitely many regions cover all inputs and intersect a segment in closed intervals. Subdividing at their endpoints lets the bound be summed over the segment, including a segment inside tie loci. Each prescribed face is strictly realizable by keeping x_i^2 at its endpoints and outside it, lifting interior data above its chord. Outside consecutive chord slopes are strictly increasing and those immediately adjacent to the chosen face bound its slope strictly wherever present. A tiny upward unit step immediately after a cheapest edge preserves the chain, contributes only that edge to input variation, and changes the GCM values by a chord ramp on the desired face and constants elsewhere. This attains the corresponding exact quotient even for arbitrarily close pairs. Equal weights give one on all intervals; unequal weights give a quotient strictly above one on the full interval. In the four-knot example the first two edges give (1+14)/3=5; the last two also give 5, the full interval gives 4, and single edges give 1. The two-knot and constant-difference cases are consistent with the stated seminorm and translation property.

## originality

PASS

The arbitrary-knot sharp nonunit coefficient and every-interval sharpness in the nodal variation seminorm pass on the inspected evidence. The standard cumulative-sum representation is more closely related than the frozen literature discussion suggests: it gives an exact weighted slope-projector conjugacy, not a least-squares projection of the original nodal vector. Uniform-mesh contraction rigidity is already a consequence of Yang–Barber after that conjugacy. What distinguishes the full finding is the exact operator norm over all pooled blocks with independent fitting masses and target coordinate weights, not the mere use of isotonic regression or the unweighted contraction.

## value

PASS

Nodal variation is a natural error measure for lower hull convexification on irregular meshes. The exact amplification for independently chosen edge weights identifies the responsible interval and cheapest perturbation edge, with witnesses at arbitrarily small scale. This is sharper than just knowing strict anisotropy breaks contraction or bounding by the global weight ratio, and it quantifies an operator and a perturbation regime a later stability analysis could use. The main value is this sharp arbitrary-mesh, arbitrary-weight coefficient and where it is attained, not transferring a binary isotonic-contraction criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
