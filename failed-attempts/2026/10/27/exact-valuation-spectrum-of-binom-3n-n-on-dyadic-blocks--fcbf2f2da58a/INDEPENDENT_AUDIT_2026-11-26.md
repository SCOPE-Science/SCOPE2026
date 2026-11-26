# Independent mathematical audit

## correctness

PASS

Legendre gives ν₂=2s₂(n)−s₂(3n). Multiplying by 3 from the least significant bit uses carries 0,1,2, and each output digit y has increment 2x−y; subtracting the digit sum of the final carry retains all leading digits of 3n. The corresponding row transitions give the displayed Laurent matrix and terminal column. The cofactor numerator of the resolvent is (1+z)(1−uz), and det(I−zM)=1−(1+u)z+(u−u²−1)z²+u(u+1)z³. Its coefficient identity gives the initial values and recurrence; at u=1 the series reduces to 1/(1−2z). For moments, D(1,z)=(1−2z)(1−z)(1+z) and D_u(1,z)=−z−z²+3z³ give the derivative fractions in the proof. In particular the second factorial moment is L²/4−L/4−4/9 + [ (L+1)/2 + (−1)^L((L+1)/6−2/9) ]/2^L, which combines with the mean to yield the displayed variance. Both moments vanish for L=0,1. The isolated eigenvalue 2 of M(1) is separated from ±1; implicit differentiation gives λ′(1)=1 and λ″(1)=4/3. The analytic leading projection contributes a factor tending to 1 under the characteristic-function scaling, and the second log derivative of λ(exp(w))/2 is 11/12. After centering by L/2, Lévy's theorem yields the stated CLT. This applies only to the initial blocks [0,2^L).

## originality

FAIL

Two distinct indexed statements give exact coverage: 02997d82d076 gives the same enumerator, exact mean and CLT under the pointwise-identical ternary Fuss–Catalan valuation, and 767a9e2b871f gives a stronger joint law with this exact marginal. The printed finite variance is a direct differentiation and coefficient extraction from the already available rational function; it does not escape that coverage.

## value

FAIL

The initial-block distribution is a natural and useful exact object, but this record gives no substantive mathematical gain beyond the established complete distribution. In this context the newly printed variance correction is routine coefficient extraction from an identical generating function; the Gaussian limit already has identical constants in the pointwise-equivalent formulation. The alternative size-three transfer is tidy but the finding does not establish a distinct minimality, computational or structural benefit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
