# Independent mathematical audit

## correctness

PASS

Subtracting the common rotation ω−Mγ in the complete unnormalized diffusive system gives (β_j−Mε−k|u_j|²)u_j+(ε+iγ)Σu_l. Closure with the prescribed positive radii is rank two in phases exactly at noncollinear polygons; the implicit function theorem gives an (M−2)-dimensional equilibrium patch and its continuation in ε. At ε=0 the real Jacobian is minus the sum of the positive radial projectors scaled by 2k, plus the skew-adjoint mean-field term. Its real semigroup is contractive (and the complexification satisfies the same Hermitian energy inequality), so imaginary-axis eigenvalues are semisimple. Any imaginary-axis eigenvector has vanishing radial projections. If frequency is nonzero, the remaining eigenvector equation forces a common two-vector across oscillators; orthogonality to the two independent real radii forces it to be zero. At zero frequency the kernel is exactly the phase variations with sum zero because γ≠0. The other M+2 eigenvalues have strictly negative real parts. The gap is uniform on a sufficiently small relatively compact regular patch; the local stable foliation of the equilibrium manifold gives exponential approach to a nearby equilibrium, not a fixed polygon. The rotation does not change the growth rates (for ω−Mγ=0 these are equilibrium exponents). The local spectral cluster near zero keeps multiplicity M−2 under small ε and the continued tangent space already has that dimension, so no additional small normal modes appear and the gap stays negative. Strict triangle inequalities supply both orientations. Independent replay: python /workspace/reproductions/check.py 3, 16 finite-difference Jacobians at two heterogeneous radius profiles, both orientations, both signs of γ and ε=0 or 0.0001; smallest sampled normal gap 0.079792784. This supports the linearization but is not a nonlinear or uniform-gap proof. The frozen script was inspected, not run; it constructs one explicit triangular orientation (the independent replay tests both).

## originality

PASS

Credit the closed-polygon manifold to the same-model literature and the exact homogeneous purely reactive stability case to indexed work. The supported distinct result is universal local normal attraction for arbitrary unequal positive growth rates and every admissible noncollinear polygon, together with its local small-positive-dissipation continuation when reactive strength is held fixed. The nearest exact heterogeneous triangle and same-model sampling results have a nonzero real component on different parameter paths; they neither imply nor contradict this quantifier and limit.

## value

PASS

Normal stability of the existing polygon family is not automatic from its existence or stable samples. The result settles every regular shape for arbitrary positive growth rates at the pure-reactive boundary, separates phase and shape neutrals from damped directions, and explains how radial damping stabilizes through the skew mean field. Continuation gives a genuine nearby parameter regime, without claiming a uniform coupling threshold or global basin.

The dated certificate retains the supplied scientific assessment, sources and limitations.
