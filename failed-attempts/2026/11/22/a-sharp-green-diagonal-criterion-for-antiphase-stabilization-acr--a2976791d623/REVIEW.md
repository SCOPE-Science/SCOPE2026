# Independent mathematical audit

## correctness

PASS

The specified unrestricted ordered triad is K2 Im(Z2 conj(Z1) exp(-i theta_i)); at an antipode Z1=0 and Z2=1, yielding -K2 ss^T/N. On the rotation quotient the scaled negative Jacobian is H-zz^T, where z=e_a-e_b, H=L_A⊕L_B+gamma ss^T/N, and gamma=K2 d/K1. For gamma>0, H is positive definite on this quotient, and the rank-one test has leverage z^T H^(-1)z=R+4/(gamma N); equality gives exactly one extra zero, and leverage above one gives exactly one unstable mode. For gamma=0, s gives a negative direction of the scaled negative Jacobian and a rank-one subtraction permits no more. This includes m=1, where R=0. Synchrony has strictly negative pairwise Laplacian on the quotient plus a negative semidefinite triadic term. The endpoint Green sum on paths is (m-1)(2m-1)/(3m), and on barbells is 2(m-1)/m^2. The finite path checks can be replayed with endpoint_green_values() in /workspace/branches/independent_replay.py (Python 3/SymPy); they are not a proof of arbitrary graph stability. No nonlinear claim is established at equality.

## originality

FAIL

A distinct November 17 record states an exact stronger theorem for the same ordered-index dynamics and all connected weighted graphs with balanced antipodes. Its specialized compression and scalar Schur complement give the claimed single-bridge criterion by rank-one inversion; the absence of the displayed Green-diagonal abbreviation in that source does not make the criterion distinct. This is verified prior implication, not a failure of source retrieval or a mathematical error in the frozen proof.

## value

FAIL

The Green-diagonal formula is a convenient way to teach or compute the existing graph-spectral test, and the path–barbell contrast is useful illustration. As an independent new result, however, the claimed obstruction, threshold and examples are obtained from the prior exact theorem by one rank-one inversion and standard Green diagonal evaluations. The singleton calculation, extra neutral mode, and coexisting synchrony do not leave a substantive independent result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
