# Independent mathematical audit

## correctness

PASS

The equation is for fixed total outgoing migration per individual, with generator m(Pᵀ−I); switching to equal rates per edge would change the result. Dividing by m and shifting gives the irreducible Metzler matrix Pᵀ−q e_de_dᵀ. Its positive Perron vector is invariant on vertex orbits; summing its components in the eigen-equation shows z<1 for q>0. The three orbit equations reproduce the cubic and both quadratics. The bracket (√α,1) for the cubic gives positive orbit components and hence identifies the Perron root; analogous positive-component roots lie in (α,1) and (0,1) for clique and hub. At the clique root z, substituting q=(1−z)(z+β)/(z−α) into F_H=z(z+q)−1 gives α(1−z)/(z−α)>0. Then F_L=zF_H−αq gives −αβ(1−z)/(z−α)<0. The hub polynomial increases for positive z and the leaf polynomial is positive at 1, proving the strict ranking without assuming global monotonicity of the cubic. Weak-damage differentiation gives the stationary masses of the damaged patches; dividing the reduced equations by q verifies the strong-damage limits using the positive brackets. At q=0 all exponents agree and n=3 is included in the strict result when q>0. An independent root calculation at n=5,q=1 reproduces (0.933099131255, 0.882782218537, 0.618033988750); the supplied script was inspected, not executed.

## originality

PASS

Pass for the exact all-n, all-positive-damage leaf–clique–hub ordering under common total outgoing migration, not for the generic observation that adding a corridor can harm a three-patch population, or for the stationary-weight perturbation law. Statement-level comparisons of the accessible results do not establish the uniform ordering. The closest 2024 three-lattice article remains an unresolved risk for n=3, not a basis for a negative assertion about its contents.

## value

PASS

At fixed emigration effort the sign of completing a star depends on the damaged patch, and the signs persist across all relative severities of damage. That is a useful exact benchmark against topology-independent intuitions and is stronger than matching signs at both weak- and strong-damage limits, which would not exclude a crossover. The claim is for principal linear growth, not a statement about nonlinear persistence or extinction risk.

The dated certificate retains the supplied scientific assessment, sources and limitations.
