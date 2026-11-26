# Independent mathematical audit

## correctness

PASS

For a=attenuation, E=exp(-kL) and E≤y≤x≤1, the jump/decay recurrence gives row-two and row-three incoming speeds 1−ax and 1−ay−a(1−ax)y/x. Integrating the added deficits gives S/a=3−(1−a)^2 E−ax−a(1−a)y−ay/x−(1−a)E/x−E/y. As an independent uniqueness check this is strictly concave in (−log x,−log y) on the closed position triangle: the terms −ax and −a(1−a)y alone supply a negative definite Hessian there, and the remaining nonconstant terms are concave. Direct maximization for fixed y gives X_E(y)=min(1,sqrt(y+(1−a)E/a)), which is greater than y for y<1. The reduced derivative has sign E−F_E(y) with F_E=a y²(1−a+1/X_E(y)); both branches are strictly increasing, since y²/sqrt(y+c) is increasing, and they join continuously. X_E(E)≥sqrt(E), so F_E(E)/E≤a(1−a)E+a sqrt(E)<1; F_E(1)=E1=a(2−a). This proves the unique cluster including E=E1, or a unique interior y below E1. The constrained branch root sqrt(E/E1) is admissible exactly when sqrt(E/E1)+(1−a)E/a≥1. The left side increases strictly from 0 to >1 at E1, proving the E2 crossing including its equality case. On the separated branch the untruncated scalar left-hand side F_E with X_E replaced by sqrt(y+c) is strictly increasing throughout (E,1), hence its already established interior root is the only one there. The partial regime has x=1>y; the separated regime has x²>y; at either nonclustered root y²/(Ex)=1/[a(1+(1−a)x)]>1. These are exactly the two strict gap comparisons. For a=1/2 the second threshold equation is satisfied by E=1/3; at E=1/9 the stated x,y satisfy the interior equations. Independently summing the three interval contributions 1/6+1/3+4/9 gives 17/18, versus (1−(1/2)^3)(1−1/9)=7/9 and relative gain 3/14. The frozen standalone checker was inspected, not executed; its reported finite tests are not the global argument.

## originality

PASS

Pass the exact, finite-field, pinned-first-row three-impulse classification and strict gap theorem, not the ideas of integrated shelter or optimizing windbreak spacing. The actual closest statements inspected do not establish or imply the two thresholds for this model. This is a bounded best-of-knowledge judgment, not a finding of historical priority.

## value

PASS

The whole-field deficit is a motivated aggregate protection benchmark. Two exact independent length thresholds determine when separation first pays and when the remaining coincidence breaks; the strict ordering including the terminal interval rules out equal-gap prescriptions in the separated optimum. The result is globally unique and directly computable and gives a reproducible test for more realistic models or solvers. It does not support a field-spacing recommendation or claim predictive aerodynamic fidelity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
