# Independent mathematical audit

## correctness

PASS

Path differences are linear coordinates on each fixed-mean hyperplane. The potential is the quadratic sum of path drops minus the two log-cosh terms in their total and the distinguished drop, all divided by K. Permuting the differences preserves its values and Hessian inertia but not the flow metric. The two columns (ones and the distinguished coordinate vector) have Gram matrix [[K-1,1],[1,1]], giving the stated Perron eigenvalue and the unique first loss of positive Hessian at consensus. At or below threshold, y·grad Phi is positive for every nonzero y by z tanh(alpha z)<alpha z^2 when z is nonzero (and is ||y||^2 if both repulsive drops vanish). Coercivity and gradient dissipation give global convergence to the unique critical point. Above threshold the negative Hessian direction implies linear instability, and coercivity gives a nonzero global minimum. Replacing all drops by their absolute values strictly decreases energy if there were both positive and negative drops. Stationarity of a nonzero aligned minimum then forces positive ordinary drops u and distinguished drop u+v. The positive Perron direction and the all-ones vector bracket a positive fixed point; the maximum ratio of two vectors cannot exceed one in either direction by strict subhomogeneity of tanh, proving uniqueness. The positive Jacobian of this two-component map sends the fixed vector strictly below itself (z sech^2(z)<tanh(z)); the corresponding rank-two Hessian perturbation has spectral radius less than one, so both sign-related minima are exponentially attracting in the fixed-mean flow. For the optional onset coefficient the complementary eigenspace is invertible at threshold; its component is cubic in the amplitude and projection of the tanh cubic onto (1,t) gives the stated coefficient. No classification of additional stationary states or equality of transients is needed. I inspected the finite checker without executing it.

## originality

PASS

Boyce et al. already supply the tanh-gradient model and the boundary-placement quadratic form. The exact onset is a short rank-two evaluation of that quadratic form, and linear threshold placement invariance follows from the permutation of its distinguished coordinate. The materially distinct claim is the sharp nonlinear classification on fixed-mean hyperplanes: uniqueness and global convergence through the degenerate endpoint, exactly two global minima above it, and their explicit placement-invariant positive branch and strict local stability. These are not consequences of the prior quadratic bracket or of general signed-Laplacian inertia alone. No historical exclusivity is asserted.

## value

PASS

This is a named previously analyzed arrangement and its natural complete placement family. The practical invariant is that, although the distinguished step can move, neither the polarization range nor the global minimum energy changes, and only the position of the larger drop changes at all supercritical strengths. The fixed-mean consensus statement at the nonhyperbolic endpoint and the exact global profiles distinguish actual nonlinear polarization from a simple spectral threshold. The small matrix diagonalization alone would be a weaker contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
