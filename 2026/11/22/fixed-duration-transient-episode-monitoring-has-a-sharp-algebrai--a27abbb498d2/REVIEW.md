# Independent mathematical audit

## correctness

PASS

An episode arriving before the preceding window ends cannot have its first detection later: it either intersected a previous window or expired. Conditional on a not-yet-arrived episode, the exponential arrival clock restarts. The one-window arrival/survival integral at equal rates gives e^(−y)(y+1−x), with y=λg and x=e^(−λw); adding the future value gives e^(−y)(y+1−x+xv). Its derivative is e^(−y)[x(1−v)−y], establishing a strict global maximum and a unique continuation by induction, since the future term has strictly positive weight at every finite gap. The scalar iterates increase strictly to 1, so chronological gaps are positive and strictly increasing when there is more than one. The miss recurrence e_(j+1)=1−exp(−xe_j)<xe_j implies both the strict idle-time bound (the positive-width limit is below x/[λ(1−x)]) and strict improvement over the miss x^n at equal active time but not equal elapsed time. The sum of logs of the product factors converges absolutely by e_j≤x^j, giving 0<C<1. At w=0 the separately defined perfect point observation has the same Bellman rule at x=1; the reciprocal increment tends to 1/2, yielding n e_n→2 and the harmonic-sum idle asymptotic. A fresh 75-digit recurrence at x=1/2 gives v_4=0.9581868628320855 and gaps (.042712464884,.089295725693,.196734670144,.5), confirming RESULT.md's example. The supplied checker was read, not run; its recorded finite diagnostics do not prove the optimization or the limits.

## originality

PASS

The quoted point-observation boundary is already known and explicitly credited. The surviving claim is the positive-width global calendar and its sharp relative miss constant and bounded idle cost under the stated one-episode model. The strongest inspected finite-window and survey-calendar alternatives have different arrival laws, objectives or horizon constraints; they do not supply this positive-width result.

## value

PASS

The natural constrained interception problem has an exact unique solution, not just an example or numerical optimization. The singular change in miss rate and in aggregate idle time at zero window width quantifies a design difference and the strict constant measures the benefit of separation at equal active effort. It is a useful mathematical benchmark under perfect overlap detection and a free finish time, not a claim about empirical sampling performance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
