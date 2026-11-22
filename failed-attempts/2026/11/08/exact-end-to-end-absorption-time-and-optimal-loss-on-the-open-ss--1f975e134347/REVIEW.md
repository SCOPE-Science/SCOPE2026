# Independent mathematical audit

## correctness

PASS

For n>=1 and v,w,kappa>0, the irreducible Jacobi H has simple spectrum and endpoint-cyclic eigenvectors, hence B is Hurwitz and X solves the unique Lyapunov equation. The staggered real-skew gauge and real-symmetric parity decomposition imply the diagonal Gramian is exactly a/kappa+b*kappa (commutant consists of even polynomials in irreducible skew A; cyclicity determines the first row, and L(Z)=D(Z)=0 has only zero solution). Weak-loss eigenbasis cross terms are bounded and reflection symmetry yields a=2n. Strong-loss Schur elimination leaves 2n-1 sites; its paired nonzero eigenmodes have squared endpoint ratios v^2/w^2 and its single zero mode has ratio (w/v)^(2n-2), giving b=(n-1)/(2w^2)+w^(2n-2)/(4v^(2n)). Differentiate positive a/kappa+b kappa to obtain the unique optimum; fixed-ratio term comparison yields both asymptotic regimes. Boundary n=1 correct with no intercell hopping. Independent 96 complex Lyapunov solves n=1..8, four hopping pairs and three rates, with max normalized error 1.8e-13 and max residual 3.6e-13; 48 rate-normalization comparisons to prior exact theorem all agree. Tests corroborate rather than prove general n.

## originality

FAIL

The earlier published finite-dimerized-chain theorem gives exactly the same all-n lifetime, unique absorber optimum and both asymptotic regimes. Its no-jump generator uses -gamma P whereas this one uses -(kappa/2)P, so gamma=kappa/2 produces equality term by term. Prior public mirror commit precedes submission import on 2026-11-08. This is exact prior coverage, not merely a similar study.

## value

FAIL

Endpoint capture and optimized irreversible loss in a dimerized quantum path are naturally motivated transport observables. However the all-parameter exact lifetime, optimal sink strength, minimum and sharp linear/exponential regimes are already explicitly established in an earlier published result, including a more general affine-in-loss lemma. The submitted variant changes the absorber-rate convention and proof organization but supplies no independently unknown exact invariant, meaningful new boundary or structural mathematical consequence. Correctness and utility as a benchmark do not make this a distinct valuable mathematical finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
