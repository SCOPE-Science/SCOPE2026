# Independent mathematical audit

## correctness

PASS

Verified that Definition 3.2 and Theorem 1.4 of arXiv:2505.24326 apply to exactly the equality-of-residue-occupancies hypothesis with N=17·15 square-free. Independently checked the required F_15 computation using the two quartic factors X^4+5X^3+15X^2+11X+1 and X^4+11X^3+15X^2+5X+1 of Φ_15 mod 17. All primitive roots have degree ord_15(17)=4, so these irreducible factors cover the two Frobenius orbits. Gaussian rank over each quotient field, using exact multiplication/log tables and coefficientwise subtraction, yielded zero singular cases among all 32,768 subsets in each factor (32,767 nonempty). Replay: python3 /workspace/checks/order255_audit.py 5 for the timed slice or python3 /workspace/checks/order255_audit.py for all sizes; output /workspace/checks/order255_audit.out. The empty determinant is one. This replay checks the finite-field premise, not a direct enumeration at order 255. The two supplied checkers and frozen verification notes were inspected, not run. The record's two-orbit Frobenius argument suffices; a separate second-orbit check is not logically indispensable if one also uses the complementary-minor identity for F_15 inverse.

## originality

PASS

The lift is published; credit only the new parameter-specific finite-field premise and resulting 15-principal nonsingularity at order 255. The closest exact indexed statements concern a different characteristic for F_15 or a different order for the lift.

## value

PASS

The instance is a three-prime square-free order outside the inspected unconditional families and spacing estimate, in a conjecture-driven class. A tractable exhaustive premise certifies an all-sizes conclusion at a substantially larger Fourier order, and the residue-balanced result is strictly broader than principal-only nonsingularity. This is a substantive finite instance, not a claim about arbitrary composite Fourier minors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
