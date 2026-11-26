# Independent mathematical audit

## correctness

PASS

In a single excursion, the Laplace transforms of the right-first and left-first absorption times, evaluated at the reset rate, are sinh(b)/sinh(a+b) and sinh(a)/sinh(a+b). Renewal with the given instantaneous relocations and the remaining one-target mean (exp(distance)−1)/r gives the stated dimensionless objective. With s=sinh(a), u=e^a and S=sinh(b), the numerator of its derivative over (s+S)² simplifies to u s²+2Su s−S²/u, which gives the quartic after multiplication by 4u. This quartic increases strictly for u>1, starts negative and grows without bound. At u=t=e^(b/3), direct substitution gives t⁶P=(t²−1)²(t²+1)(t⁶−t²−1), proving both the unique crossing and its direction. Equivalently at the optimum, S=(u²−1)(u+√(u²+1))/2, which gives S/a→1+√2 at a→0 and S/u³→1 at a→∞. Hence the two asymptotics, including the negative log(2) correction, hold. The analytic ratio is below its large-distance limit for b>b_c and converges to that limit, so it attains a global minimum at some finite b>b_c; each such minimum is locally strict by analyticity and nonconstancy. There is no assertion of uniqueness of that ratio minimum. I inspected the symbolic/numerical checker without executing it; the decision uses the analytic argument.

## originality

FAIL

Calvert–Evans give the same all-parameter optimizer equation and uniqueness in Eq. (35). Evaluating this exact relation at the natural test ratio from their Eq. (37) gives the proposed threshold by direct polynomial factorization, and its already monotone left-hand side gives both signs. Moreover Eq. (36), not just the rounded ratio equivalent in Eq. (37), gives e^{a_*}∼(e^b/2)^{1/3}; taking logs already yields the stated negative log(2)/(3b) correction. Together with their small-distance limit, this independently forces nonmonotonicity and finite attainment. The named threshold is an unstated but mechanically implied corollary, not a new optimizer structure. This is a positive prior-coverage finding, not a failure to locate a source.

## value

FAIL

Comparing an optimum to its asymptotic ratio is a natural design question, and the closed-form constant is a useful way to present the prior solution. The submitted standalone advance, however, amounts to evaluating one already-published exact optimizer equation at that ratio, with the qualitative nonmonotonicity and asymptotic correction already forced by the published endpoint estimates. It supplies no independent exact invariant beyond that mechanical extraction and does not determine the ratio's turning-point structure. This is a useful explanatory corollary, not a surviving research claim under the value criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
