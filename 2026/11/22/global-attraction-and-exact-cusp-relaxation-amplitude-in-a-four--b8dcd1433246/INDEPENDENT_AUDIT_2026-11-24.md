# Independent mathematical audit

## correctness

PASS

The nonnegative coordinate faces are inward, and on H=0 one has H'=(C+B)/(1+128C^3)+T>=0. At equilibrium B=C and S=T=h(C), and the factored F has just the physical root 1/4. In (c,v,z,y) coordinates, the proposed V has derivative with cross-terms -(3/4)h'vy and -(3/4)vz. The bounds -1/3<=h'<=1 and g>=1/129 give v, y, z dissipation constants 8/3, 3/8, 125/1032 by Young's inequality. The only invariant set with zero dissipation is E, so LaSalle applies on the compact simplex. For the local result the stable (v,y) block has trace -53/12 and determinant 53/12, with the remaining stable eigenvalue -1/3 from z, and the zero direction is the c direction in these coordinates. On a center manifold chosen in z=0, the transverse linear operator is invertible, so the invariance equations eliminate terms of order two. The cubic forcing is F=32u^3+O(u^4), and the equations for v=a u^3+O(u^4), y=b u^3+O(u^4) give b=4a/3 and (53/12)a=-32. Thus (1/u^2)'=768/53+O(u) on either nonzero branch. Local exponential tracking by the stable foliation transfers the signed limit to the corresponding physical trajectories; the leaf tracking the zero center orbit is the three-dimensional strong-stable manifold. Global convergence makes this dichotomy applicable after a finite time for all initial states. Returning to original coordinates multiplies the scalar limit by (-1/3,1,1,-1/3). The bundled symbolic and numerical checker was inspected read-only; finite-time integrations are not evidence for the tracking theorem.

## originality

PASS

The model, stationarity equation, and qualitative global attraction at these exact parameters are already covered. The prior sufficient Lyapunov inequality actually holds strictly at this stationarity cusp; only the stationarity classification lies on the equality boundary L=0. PASS is for the distinct exact signed four-coordinate relaxation law and the separation of the full exceptional set, not for proving global convergence again.

## value

PASS

At the nonhyperbolic equilibrium, qualitative global convergence does not quantify equilibration. The result identifies which trajectories evade the algebraic tail and fixes its signed coefficient and relative amplitudes in all four observables. The difference between the dynamical and stationary coefficients is a substantive critical benchmark for the existing model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
