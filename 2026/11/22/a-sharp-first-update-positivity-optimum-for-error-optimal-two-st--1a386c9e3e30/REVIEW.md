# Independent mathematical audit

## correctness

PASS

Corollary 4.2 gives the stated coefficients. Multiplying the scalar recurrence by (3−κ)(1+κ) gives the stated F over a positive denominator. For 0<κ≤1, the maximum of exp(−z)(κz−1−κ+κ²) on z≥0 is κ exp(−2−1/κ+κ); log(2/κ)−2−1/κ+κ increases to log 2−2<0, so ∂z F<0, including at the extended endpoint. At κ=0 the numerator is 4 exp(−z)−1. The initial signs and negative limits give the unique crossing for each κ<1. For z>0, B>0, C<0, and B+2C<0 by 2 tanh(z/2)<z, so the quadratic's maximum is interior and its envelope strictly decreases (evaluate both steps at the later maximizer). The discriminant is positive at log 4 and at z=2 equals 32 exp(−2)(4 exp(−2)−1)<0. This proves uniqueness of both the frontier maximum and its maximizing κ. The sign at log 4 factors as κ[(2−log 4)−2(log 4−1)κ], including both equality cases. Independent 55-digit Decimal bisection on (log 4,2) gave z*=1.51721474033625558337747…, κ*=0.36687163516240389375386…, and κc=0.79434972478104491540269…. This checks the digits, not the analytic uniqueness. Frozen check.py and VERIFICATION.md were read, not executed. The result is for the first output from the exact pair on scalar decay, not for future outputs.

## originality

PASS

The coefficients, generic scalar recurrence, and hence the unoptimized first-output expression are prior or direct substitutions. The supported increment is the unique global exact-start, one-output optimum and exact comparison with BDF2. The strongest inspected positive-start phase diagram classifies an inequivalent all-iterate event; its failure condition cannot decide the first-update sign. Priority remains qualified by the unresolved second source and by the scope of the search.

## value

PASS

The exact first-output margin is a natural comparison of two-step schemes under the same error-free starting data. It exposes a different optimizing damping parameter from the robust all-iterate objective and a mathematically sharp interval in which damping improves rather than worsens the BDF2 margin. The ordinary single-output diagnostic can therefore give a positive answer well beyond persistent positivity; its sharp boundary is useful without being a safe integration stepsize or a claim about nonlinear behavior. The value rests on this distinction and the global optimization, not on the direct substitution F.

The dated certificate retains the supplied scientific assessment, sources and limitations.
