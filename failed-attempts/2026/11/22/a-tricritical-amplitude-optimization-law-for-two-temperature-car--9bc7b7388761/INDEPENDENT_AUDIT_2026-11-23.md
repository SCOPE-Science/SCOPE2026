# Independent mathematical audit

## correctness

PASS

The max-rate model is a positive multiple of f_p after rescaling, with the exact closed amplitude domain stated. For p≤1 strict concavity forces a=0. For p>1 set x=m−a, y=m+a, and S=(p−1)(y^p−x^p)/(p(y^(p−1)−x^(p−1))). In the interior the sign of J' is the sign of i_p−S. Equivalently it is the sign of M_p(z)−m for z=atanh(a/m), since the factors removed in the stationarity equation are positive. The hyperbolic derivative establishes strict monotonicity for p≠2, with endpoints i_p and b_p. In Step 2 the phrase ‘at most one’ must be read for p≠2, as its preceding sentence and the explicit flat p=2 case in Step 4 indicate. For 1<p<2 any interior positive root is a minimum, and comparing the endpoints gives c_p strictly between i_p and b_p, with precisely two maximizers at equality. For p>2 the root is a maximum; at m>.5 the warm-end derivative stays negative because f'(1)=−1 and f'(x)>−1 for x<1. The endpoint thresholds have no other equality case. The interior branch tends to b_p at its lower endpoint and to zero only at i_p; its warm temperature y=p[1−(r−1)/(r^p−1)]/(p+1), r=y/x, decreases as m increases because r decreases and (r^p−1)/(r−1) increases in r. Thus a=y−m indeed decreases there. The expansion S=m+(p−2)a²/(3m)+O(a⁴) confirms the exact onset coefficient. The polynomial identities at p=2 and p=3 give the flat interval and example gain exactly. Read VERIFICATION.md and checks/verify.py without executing them; an independent amplitude grid spanning 13 exponents and 99 means found no violation in 310167 comparisons. This does not replace the analytic boundary and uniqueness checks.

## originality

FAIL

The exact thermal optimizer classification is a direct application of known Schur monotonicity of Stolarsky extended means, not just of general Jensen averaging. An available full-text theorem reproduces the established classification for the exact parameter line used in the optimizer equation, including the change of direction at p=2. The remaining endpoint comparison and expansion are elementary. The neighboring same-day thermal records are on different functions or forcing constraints and are not the basis of this verdict.

## value

FAIL

The fixed-mean comparison is interpretable for the assumed model and the different optimizer types are correct. However, as a claimed exact mathematical contribution it is the direct fixed-sum specialization of a known Schur-monotonicity classification, with routine endpoint algebra and a local Taylor coefficient. The record does not provide independent experimental calibration, an additional mathematical invariant, or an extension beyond that corollary; the illustrative gain cannot supply a distinct surviving claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
