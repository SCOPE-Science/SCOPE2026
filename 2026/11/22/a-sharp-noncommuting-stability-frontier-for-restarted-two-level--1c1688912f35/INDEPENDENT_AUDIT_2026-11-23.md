# Independent mathematical audit

## correctness

PASS

Under strict Euclidean positive-definite contraction hypotheses, parallel C relaxation gives Fx at every positive coarse index from constant initialization; the second F relaxation does not change C points. The fine coarse-point residuals are zero at index one and (F²−F)x thereafter. Exact coarse forward substitution gives the ordered partial geometric sum and operator-norm convergence to V∞=F−C⁻¹D for C=I−Ψ and D=F(I−F). D^{1/2} conjugates this to H=F−D^{1/2}C⁻¹D^{1/2}≺I. Complementing the symmetric block matrix with diagonal blocks I+F and C first on C and then on I+F gives Inertia(I+H)=Inertia((I+F²)(I+F)⁻¹−Ψ), including nullity. Thus singular semidefinite difference gives a nondecaying −1 mode; a negative direction gives an eigenvalue below −1. Direct 2×2 arithmetic gives trace 43/840 and determinant (2−15 sin²θ)/3360 of the difference; at π/4 the endpoint trace is −51/32 and determinant 27/64, giving the stated eigenvalues. This is an analytic verification of the limiting restart, not of a finite-length trajectory or repeated solves on one trajectory. The frozen check.py was inspected, not executed.

## originality

PASS

Credit the algorithm, ordered one-sweep operator, and commuting endpoint formula as prior. The distinct contribution supported here is the necessary-and-sufficient noncommuting SPD restart condition, its exact boundary inertia, and the rotated stability loss, not discovery of the restart algorithm or geometric-sum identity. No inspected prior result supplies that sharp noncommuting restart classification.

## value

PASS

For natural nonmatching fine/coarse quadratic surrogates the exact gain boundary and its unstable-mode count are usable design tests. The smallest possible rotation example shows why individual strict contractions and their spectra alone cannot ensure restart stability. The Schur algebra is standard, but this exact criterion for the endpoint restart addresses a substantive failure mode of the method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
