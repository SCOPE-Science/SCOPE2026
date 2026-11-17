# Independent mathematical audit

## correctness

PASS

For every k>=2,N>=k+1,gamma>0 the q1,q2 Hessian block has determinant one, hence H_gamma is SPD, and the exact V-reduced Hessian is I_2. Gaussian LS regression z=(X^T X)^-1 X^T y has isotropic two-dimensional density (k-1)/(2pi)(1+||z||^2)^(-(k+1)/2), giving radial survival (1+t^2)^(-(k-1)/2). Symmetrization yields Hhat=I_2+gamma[[z1,z2/2],[z2/2,0]] with lower eigenvalue 1+gamma(z1-||z||)/2; J_2 Hhat has a positive real eigenvalue iff Hhat is indefinite. Uniform Gaussian direction gives arcsine c=(1-cos(theta))/2 and the stated exact one-dimensional probability. Dominated convergence at gamma down to 0 and boundary Laplace asymptotics at c=1 yield sharp constants for k large. Independent numerical integration matched 60,000-sample Gaussian regression experiments for k=2,3,5 within sampling error; Monte Carlo alone cannot prove the all-k integral.

## originality

PASS

No inspected primary or prior mathematical-result theorem gave the probability of indefinite *symmetrized least-squares sketched* reduced Hessian for this exactly SPD oscillator, or the sharp k-asymptotic. Classical Wishart/Student regression and positive-Ritz failure in another sketching algorithm do not imply the coupled-oscillator instability cone probability without deriving its geometry. Herkert et al supply the algorithm and sufficient error conditions; their accessible abstract describes perturbation bounds, not this unconditional probability. Full latest paper inaccessible, so a real priority risk remains.

## value

PASS

This gives a physically meaningful sharp failure probability for Hamiltonian structure-preserving randomized reduction: symplectic form survives but positive energy can fail with positive probability at every finite sketch width. The explicit SPD witness and sharp exponential sketch-budget law quantify an important gap between geometric conservation and dynamical boundedness; not a cheap unmotivated normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
