# Independent mathematical audit

## correctness

PASS

Original six-coordinate quadratic rule preserves three pair masses c_i and gives exact u'=B_c u with B=( [1-c2,c1,0],[0,1-c3,c2],[c3,0,1-c1] ). Direct determinant computation yields (t-1)(t^2-t+s), s=c1c2+c2c3+c3c1. The discriminant 1-4s=2sum(c_i^2)-1 gives a genuine incircle of radius squared 1/6 in the conserved-mass simplex. Positive masses make eigenvalue 1 simple, and Pi=c(c3,c1,c2)/s is the stationary projection. On the critical circle N=(B-I/2)(I-Pi) is square-zero but nonzero because B13=0 whereas Pi13/2>0, yielding B^n=Pi+2^-n E+n2^-(n-1)N. The Dirichlet(1^6) push-forward gives Dirichlet(2,2,2) density 120c1c2c3. In orthonormal planar coordinates the Jacobian is 1/sqrt3, the odd cubic term integrates to zero over the centered incircle and exact integration is 25pi/(54sqrt3)=0.839721927886212. Independent SymPy symbolic determinant/Jordan and exact-rational original evolution checks corroborate; the proof is algebraic for all strictly positive c, not an inference from finite rational grids. Boundaries with zero mass excluded from Jordan statement, probability-zero circle/tangencies correctly treated. RESULT.md blob 2a1878c466b9d7611029301f645d73deb0acf631 and checks/verify.py blob 87ad30b82068d8defed4fe7902a2af2f9d0c46f9 read.

## originality

PASS

The incircle/Jordan exceptional boundary and its uniform-six-simplex spectral prevalence are a precise integrated statement not supplied by the prior original fiber reduction or the published same-directed-cycle many-locus equilibrium-selection CLT.

## value

PASS

The sharp exceptional-point incircle separates real monotone from complex oscillatory relaxation within a natural conserved-mass triangle; the nonzero nilpotent term supplies the actual polynomial-transient law. Weighting this phase diagram by the canonical uniform six-coordinate simplex measure gives a nontrivial exact probability needed for random-initial-state interpretation of this QSO. This is a motivated natural invariant, not a free choice of prior or a textbook discriminant alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
