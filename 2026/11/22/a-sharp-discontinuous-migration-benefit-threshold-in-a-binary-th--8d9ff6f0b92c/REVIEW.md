# Independent mathematical audit

## correctness

PASS

For the stated symmetric exchange after reproduction, the trace can be checked by separating closed three-step patch paths into zero and two switches. With t=1-d it is (r+1)[r t^3+(r^2+r+1)t d^2]; the determinant is r^3(1-2d)^3. The smaller eigenvalue is below r^2 throughout: on [0,1/2] it lies in [0,r^(3/2)], and above 1/2 it is negative. Therefore the sign of growth minus r^2 is the opposite of the sign of the frozen quadratic Q_r(d) for d>0. Its positive leading coefficient, vertex in (1/2,1), positive values at zero and one, and discriminant (r^2-4r+1)(r^2+4r+1) prove the exact open winning interval and the double-root tie at (3-sqrt(3))/2 when r=2+sqrt(3). Compactness gives maximizers, and the interval endpoints converge to the tie rate from above. At zero the right derivative of growth is -3r^2 by the characteristic identity, so the improvement does not come from small exchange. On the capped interval Q is decreasing, with Q_r(1/2)=(-r^2+4r+1)/4; this gives the second threshold and the exact tie. Patch conjugation and cyclic characteristic-polynomial invariance include singular half exchange; for constant calendars the column-sum norm gives the sedentary upper bound. Replay: RESULT.md §§1–5; hand substitution yields Q_4(2/3)=-2/9, Q_4(1/2)=1/4, Q_5(1/2)=-1. The supplied checker and JSON were inspected, not executed: the counter includes floating-point grid iterations where the comparison may be skipped and is not a count of exact assertions or a continuum certificate. The analytic argument does not depend on it.

## originality

PASS

The unrestricted direct-exchange classification, including the exact winning interval and the nonzero limiting optimum, is not covered by the inspected endpoint or paired-season results. Credit is for that classification and its contrast to the capped model, not for discovering capped endpoint optimality or the general phenomenon of discontinuous migration onset.

## value

PASS

The full binary three-season contrast family is a natural minimal seasonal imbalance, not a single favorable example. Its classification separates local loss at zero exchange from a global gain first attainable at a rate bounded away from zero, and isolates the interval of fitness contrasts for which changing the physical exchange rule changes whether a gain is possible. This gives a useful benchmark for two-patch deterministic growth models without asserting an empirical or evolutionary conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
