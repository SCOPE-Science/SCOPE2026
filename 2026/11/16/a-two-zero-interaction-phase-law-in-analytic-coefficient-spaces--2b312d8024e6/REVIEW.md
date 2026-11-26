# Independent mathematical audit

## correctness

PASS

The repair at repairs/2/RESULT.md corrects Step 6: if D is the minimum of the q-norm (not its q-th power), the energy is D^(-p), not D^(1-p). For example at p=2,r=1/2 the jet norm D=1/sqrt(15) gives energy 15, not sqrt(15). Both constraints follow for a_n=-|w_n|^(q-2)w_n/D^q from stationarity against the second constraint vector and pairing against w; sharp Hölder gives optimality. The perturbed constraint vectors converge in ell^q, remain independent by their first two coordinates, and the trial t=0 and reverse triangle inequality uniformly bound the minimizing multipliers. Their positive minimum norms thus converge and the corrected power proves confluence. For the rest: sharp Hölder and the even-coordinate projection give the single/antipodal formulas and the endpoint limits of the explicit crossing. For Y_s=(1-s)N_s, conditioning on N_s>floor(u/(1-s)) gives the claimed stop-loss formula. Its derivative is nonnegative on each floor interval and positive above the smallest atom except at isolated thresholds. Integration against the positive-a.e. second derivative of |1+by|^q gives strict convex expectation growth at every nonzero b; the minimizing b is nonzero because the derivative at zero is q. Comparing at the larger-s minimizer yields strict growth of F_q. The exact quadratic minimum s/(1+s), monotonicity of probability L^q norms, and F_q(s)~s as s tends to zero prove the interaction inequalities and uniqueness. The normalized geometric tails are uniformly exponentially bounded near s=1, so uniform integrability and bounded minimizers give the exponential limit. The independent finite KKT witness and collision checks are evidence/2/reproduce.py and replay.txt; proof, not truncation, covers all p and r in the claim.

## originality

PASS

The corrected package presents one-zero and antipodal formulas as benchmarks, not as a new duality theorem or a priority claim for elementary substitutions. The supported contribution is the normalized geometric monotonicity argument yielding an all-radius repeated-zero interaction classification, a boundary variational constant, and transfer of strict signs to nearby distinct zeros. The examined prior finite-zero and multiplicity frameworks do not supply that quantitative classification.

## value

PASS

Repeated zero constraints arise naturally from colliding prescribed zeros. A unique sign boundary against the twice-single benchmark, with a rigorous boundary constant and openness for genuinely distinct pairs, addresses a motivated quantitative question beyond sharp interpolation duality. The strict monotonicity argument controls a continuum of radii; leaving the crossing implicit does not weaken its uniqueness or sign characterization. The repair is not accepted merely for correcting a normalization typo.

The dated certificate retains the supplied scientific assessment, sources and limitations.
