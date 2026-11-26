# Independent mathematical audit

## correctness

PASS

The Frobenius brackets vanish at all rational points. Differentiating them at a rational point gives four cyclic bilinear gradient equations. If X3 were zero, the first and second equations would force X1=X2=0 and the fourth would force bX0²=0; if X3 is nonzero, X2 X1=X3² and X1 X0=X2² give the other nonzero coordinates. Normalize X3=1: the gradient vanishes exactly at (t⁻³,t,t⁻¹,1) for b=t⁵−t³; the fourth equation follows from the first three. The degree-two Taylor term is the product of the linear coefficient variations and the linear parts of the Frobenius brackets, since q≥3. The displayed Hessian has determinant 6b/t²−2t³=2t(2t²−3); at its zeros, 3t⁻² is a nonzero two-by-two minor. Odd characteristic gives the ordinary-node criterion. At an exceptional point, (1,t²,1/2) annihilates the Hessian, so the rational line restriction has multiplicity at least three there plus q other distinct zeros, exceeding its degree q+2. The incidence count removes exactly t=±1; the roots of 2t²=3, if nonzero and present, give distinct b=3t/4. Characteristic three has none. Replay: from /workspace, python3 reproductions/algebra.py surfaces. The independent run exhausted the rational gradient incidence sets over F3, F5, F19, F9 and F25 (0, 2, 16, 6 and 22), and checked the formal polynomial restriction on every exceptional line in those fields (0, 2, 2, 0 and 2). The frozen checker was inspected, not executed; its evaluations at rational line points alone cannot detect geometric containment, since all rational points lie on the surface. The uniform proof establishes containment and the rational census; neither the proof nor the run classifies nonrational singularities or the exceptional analytic germs.

## originality

PASS

Pass the supported distinct local Hessian and node/corank stratification with its contained-line consequence, not the companion construction or the first-order singular point relation. The exact converse and total incidence count are close deductions from the published gradient equations; the exceptional stratification needs the additional quadratic computation.

## value

PASS

The original family was constructed to study rational smoothness of space-filling surfaces. At parameters where rational smoothness fails, a sharp second-order criterion separates ordinary nodes from exceptional points and identifies a geometrically contained line, uniform over all odd finite fields. This information is not recoverable from a rational-point count alone and gives concrete local geometry for the known family without overstating what happens over the algebraic closure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
