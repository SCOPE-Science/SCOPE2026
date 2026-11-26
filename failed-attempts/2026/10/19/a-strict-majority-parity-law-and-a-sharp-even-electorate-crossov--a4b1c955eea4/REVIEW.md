# Independent mathematical audit

## correctness

PASS

For strict rather than randomized ties, adding voter 2m to an odd electorate loses exactly the event of m correct votes in the old electorate and a final incorrect vote; adding voter 2m+1 to an even electorate gains exactly the old tie followed by a correct vote. Adding two voters to the even electorate gains from m old successes followed by two successes, and loses from m+1 old successes followed by two failures. This gives the frozen conditional increment; tilting the Beta law by u^(m+1)(1-u)^m gives the strictly positive numerator m(alpha-beta)+alpha+2m+1. A2=E[Theta^2]<p. Dominated convergence and reflection of the beta density about 1/2 give L-p=integral over (1/2,1) of (1-u)(f(u)-f(1-u))>0, so at most one even tie and a finite first strict exceedance follow. At (2,1) the mass is 2(k+1)/((n+1)(n+2)); summing it gives both frozen formulas, equality at 8 and A10=15/22. This proof handles all stated real shape parameters. Inspected frozen RESULT.md lines 33–72, VERIFICATION.md and verify.py. The latter is an exact rational finite corroboration (replay with Python 3); no new script execution or formal verification is needed for this analytical result.

## originality

FAIL

The distinct indexed finite-peak finding does give the exact signed odd-electorate increments for the same beta mixture, in its proof. The even classification is a mechanical consequence of those increments and the fair-tie/strict-tie relation with the previous odd electorate, not just a topic match. The stipulated asymptotic advantage and stationary count law are also prior results. The simplest integer cutoff and closed forms evaluate the known beta-binomial mass by a sum of successive integers; no independently surviving theorem is established for that remainder. This is a coverage decision, not an inference of priority from posting dates or missing text.

## value

FAIL

The tie-as-failure convention raises a natural question, but the frozen answer uses a correction of known monotone accuracies by elementary, decreasing tie masses. The example cutoff is a direct tail evaluation of the known stationary law at the smallest integer asymmetry. It illustrates the convention, but does not leave a nonmechanically implied exact invariant or independent structural contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
