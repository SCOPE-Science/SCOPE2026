# Independent mathematical audit

## correctness

PASS

Completing the square in a perpendicular chord of E(A) replaces A=[[a,b],[b,c]] by diag(a,det(A)/a). Thus D=det(A) is fixed and the squared semiaxis on the new line is x cos²(delta)+(D/x)sin²(delta). With t=x/sqrt(D) and u=(t-1)/(t+1), elementary substitution gives u_new=u(u+C)/(1+uC) with C=cos(2 delta); 1+uC>0. Subtracting its squared ratio from one gives (1-u²)(1-C²)/(1+uC)². This is in [0,1] and keeps |u|<=rho=|u_1|. For nonzero previous iterates it is between [(1-rho)/(1+rho)](1-C²) and (1-C²)/(1-rho)². The lower bound gives the claimed exponential estimate; if an iterate is zero it is absorbing, otherwise summable energy makes the squared-ratio product positive (the tail log is summable). The two semiaxes tend to the same radius exactly in the circular case, independently of direction. Finite cancellation is exactly C=-u for u nonzero, and the finite rational compositions on each aligned sign branch have nonzero power-series leading terms at zero and finitely many real zeros per step. In particular, if 'principal axes' permits the major axis along H_1 or along H_1 perpendicular, use initial u_1=rho or -rho; the finite-zero proof covers both. The harmonic directions cross arbitrarily late lifts of every target angle with overshoot tending to zero, and C>0 at each step preserves positive u_1, giving exactly the stated orbit. C=0 is a 45-degree change (not a literal quarter-turn); it squares u and validates the displayed double-exponential law. The bundled checker was read, not executed; exact products and cancellation are certified here by algebra, not finite floating-point tests.

## originality

PASS

The ellipse matrix step, convergence in shape, and dense-direction nonconvergence are prior work. The nonzero residual-versus-exact-cancellation alternative for every finite-energy sequence, the resulting all-initial-ellipses iff, and the explicit anisotropy bound in prescribed, not realized, angles are the new package on the compared evidence.

## value

PASS

For a given infinite prescribed sequence the result separates collapse to a disk from noncircular shape limits, using an intrinsic angular sum with no need to track the changing major axis. The quantitative estimate and finite-cancellation distinction give genuine additional content beyond mere convergence up to rotations and explain why dense prescribed lines do not settle this question. It is a planar ellipse theorem and does not infer circularization for arbitrary convex bodies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
