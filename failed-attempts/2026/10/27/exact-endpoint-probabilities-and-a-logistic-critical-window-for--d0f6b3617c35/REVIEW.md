# Independent mathematical audit

## correctness

PASS

Conditioning the first A coupon to be the fixed starting vertex changes no total-time distribution by exchangeability and leaves independent future draws. Thus the side must be B precisely when T_b>=T_a: compare physical step indices 2T_b-1 and 2(T_a-1), including a=1. Summing the finite inclusion-exclusion expressions for the A point mass and B survival function over time gives the stated denominator by a geometric series; zero bases at time zero represent 1. Within each non-start orbit, exchangeability gives the claimed probabilities. For m>=2 the squared l2 norm of a mixture of translates of the last geometric stage is at most the squared norm 1/(2m-1) of that stage alone. It is strict for m>=3 because the earlier-stage sum has nondegenerate support, and two distinct translates differ. For the collision asymptotic use integer Fourier inversion after t rescaling: one geometric factor gives a uniform (1+2t^2/pi^2)^{-1} bound on |t|<=pi*m. Gumbel convergence, independent limits, dominated convergence and Plancherel yield the integral of the Gumbel density squared, 1/4. The deterministic difference of centerings divided by m is delta*log(m)/m+o(1) for delta=o(m); centered fluctuation differences are tight, and at finite limits their independent Gumbel difference is continuous logistic. The two-vertex case uses the pgf at 1/2 of the other coupon time and yields the central-binomial identity. Verified 81 small side probabilities, 20 thin-part instances, and 11 balanced cases exactly with a separately written state recurrence (python3 /workspace/branches/frozen_math_recheck.py 5); asymptotic claims use the argument, not those cases. The frozen checker was inspected, not executed.

## originality

FAIL

Material equivalent coverage is present in the distinct indexed record 2b607d0cfc50. It treats exactly the same walk, start convention, side and individual endpoint law on all positive a,b, declares the same balanced asymptotic coefficient and proves a stronger logistic statement for general scaled integer sequences as well as both infinite drift cases. It uses even the same Gumbel Fourier/Plancherel limit for the collision. The double sum is only another evaluation of the identical coupon comparison; the remaining exact specializations do not support the original core. This is a statement comparison, not a conclusion about authorship or a priority order inferred from catalog dates.

## value

FAIL

The observable and the exact critical scales are intrinsically meaningful, but that substantive work is already represented by a mathematically equivalent or stronger record. The different rational summation, gap normalization and thin-part evaluation are routine consequences in the same model; no new structural or computational need is met by submitting them as this finding. There is no identified valuable distinct remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
