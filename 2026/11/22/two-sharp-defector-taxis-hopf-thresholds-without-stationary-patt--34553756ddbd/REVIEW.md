# Independent mathematical audit

## correctness

PASS

Substitution verifies the positive coexistence solution. At the constant state the no-flux conditions give Neumann conditions for the linear perturbations: the public-good derivative vanishes, so the defector boundary flux reduces to its own derivative. The defector taxis contribution is -2wD_v v_* times the public-good Laplacian; on cos(kx) this yields +qw/4 in entry (2,3), q=k^2. I independently reconstructed the reaction Jacobian and used trace, principal minors and determinant to compute A,B,C and H=AB-C exactly. A,B,C are positive on q,w>=0; the q=0 margin is 19/2 and each k>=3 has nonnegative w slope because H_w=q(2q-11)/16. For q=1,4 the margins are (1297-18w)/32 and (5908-24w)/32, with ordered zeros 1297/18 and 1477/6. Routh–Hurwitz gives stability before each zero and instability after; positive coefficients exclude any nonnegative real root, so any unstable eigenvalues form a conjugate pair. At equality the polynomial is (lambda+A)(lambda^2+B), with B computed as 3431/144 and 797/3. At a simple imaginary root implicit differentiation gives Re(lambda')=-H_w/[2(A^2+B)]>0, establishing transverse crossings. The first pair is already unstable at the second threshold and no zero eigenvalue is possible. For any fixed w the scaled modal matrices M(k^2,w)/k^2 tend to -I/4 plus a nilpotent off-diagonal term, so the large modes have real parts tending to minus infinity, consistently with the all-mode result. This is a linear spectral conclusion, not exclusion of all nonlinear stationary patterns and not a nonlinear Hopf theorem.

## originality

PASS

The model, modal linearization and cubic stability machinery are prior. The supported distinct result is the exact, two-crossing and all-mode linear classification under defector attraction alone at equal fixed diffusivities. The closest actual published claims use a different varied coefficient or unequal diffusion with zero taxis; they do not specialize to this phase diagram.

## value

PASS

This is a concrete counterexample to relying on the stationary determinant condition when interpreting stronger defector attraction as suppressing spatial instability. The fixed equal-diffusivity path isolates the directed-motion mechanism; two exact thresholds and an all-mode exclusion give a reproducible classification rather than one computed example of an unstable complex pair. The second crossing is a change in the unstable mode count, not a second loss of stability of an otherwise stable equilibrium.

The dated certificate retains the supplied scientific assessment, sources and limitations.
