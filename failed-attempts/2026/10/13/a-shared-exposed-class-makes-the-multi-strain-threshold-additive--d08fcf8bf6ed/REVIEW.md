# Independent mathematical audit

## correctness

PASS

For the printed equations (2.1)–(2.7), the disease-free equilibrium has (S+D)/N=1 and incidence only into the single E. Progression is not new infection. Thus F has just its first row nonzero, and solving Vz=e_1 gives 1/a, alpha phi_j/(a d_j), and (1-alpha) phi/(a d_C) in the respective coordinates. F V^(-1) has one positive eigenvalue, its (1,1) entry, exactly the additive expression. Independently, the infected Jacobian's eigenvalue equation in the closed right half-plane is t+a=beta[sum_j alpha phi_j/(t+d_j)+(1-alpha)phi/(t+d_C)]. If the corrected ratio is below one, the modulus of the right side is less than a while that of the left is at least a; if above one, the real right side starts above a at t=0 and decreases while t+a increases, giving a positive root. The uninfected block in order R,S,D is triangular with negative diagonal -(delta+mu), -(mu+lambda), -(mu+delta_2). The strict claims therefore hold for the full system. Equation (3.8) really uses max_j sqrt(C_0+A_j), and Theorem 3.4 uses it as a stability threshold. In the exact example the infected matrix minus its -I diagonal shift is an off-diagonal row/column product with squared nonzero eigenvalue 27/20; this gives the claimed unstable eigenvalue -1+3 sqrt(15)/10, with printed R=9/10. The frozen claim does not decide the threshold equality, endemic dynamics or the interpretation of the paper's inconsistent prose beyond the printed equations. The nested shipped checker was inspected, not run; its final numerical root assertion is floating point, but the sign follows exactly from 27/20>1.

## originality

FAIL

Distinct Resultary record 742f77f7a142 contains the same correction to exactly the same printed system, the same comparison with (3.8), the rank-one proof and a valid counterexample to false stability. Its parameter scope includes the frozen scope. This is demonstrable equivalent coverage, not a priority inference from the catalogue date. A different set of positive rationals for the counterexample does not escape the existing coverage.

## value

FAIL

Correcting a model's printed local stability threshold is meaningful in itself. But that source-specific correction and the existence of a false-stability example are already supplied by the distinct matching record. The frozen package adds only another choice of rational parameters for a known counterexample, with no separately motivated calibration, new regime, or further stability result. The numerical substitution is not a surviving worthwhile contribution to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
