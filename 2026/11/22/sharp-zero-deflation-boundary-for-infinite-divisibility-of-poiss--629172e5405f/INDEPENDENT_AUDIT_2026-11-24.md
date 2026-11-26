# Independent mathematical audit

## correctness

PASS

Integrating the conditional Poisson PGF against the normalized Bilal density gives c/[(1−az)(1−bz)] with 0<b<a<1. The modified positive masses remain positive exactly up to the stated upper scale, where p0 vanishes. For d=p0>0, factoring the numerator gives the formal log coefficients (a^n+b^n−ρ1^n−ρ2^n)/n. For inflation x=(1−t)/d lies in (0,1). Nonreal numerator parameters are conjugate with modulus √(xab), so their power sum is bounded by a^n+b^n by AM–GM. Real parameters are nonnegative with total x(a+b) and maximum ≤a (evaluate the polynomial at a and use the total); weak majorization then gives the same bound. At t=1 the numerator parameters vanish. For deflation the parameters are r and −s with 0<r<b (test the polynomial at 0,b) and s increasing strictly with y=(t−1)/d. The crossing s=a solves y=a/(a+2b): equivalently the numerator vanishes at z=−1/a, giving t*=1/[1−G(−1/a)]=1+3/[(β+1)(2β+7)]. Up to and including that crossing, odd and even log coefficients are nonnegative and all parameters are strictly inside the unit circle, so summation at 1 gives total intensity −log d. Beyond it s>a>b>r implies every sufficiently high even coefficient is negative. At d=0 the minimum supported value is 1, which cannot be the minimum of an iid two-fold sum on the nonnegative integers. At t=0 the law is the point mass at zero. The uploaded verify.py was inspected, not run; its finite recurrence checks are not needed for the all-order inequalities.

## originality

PASS

Pass for the sharp additive infinite-divisibility boundary on the specified zero-modified Bilal path, including critical equality and the eventual even-order obstruction, to the best of the evidence. The unmodified Newton/geometric convolution, discrete compound-Poisson criterion and power-sum machinery are not credited as new.

## value

PASS

A scale cutoff for compound-Poisson representability of a named count law answers a natural robustness question for zero-mass modification. It shows not just that zero inflation is safe but that some deflation is admissible with a strictly positive margin, then identifies how the property fails at arbitrarily high even orders. This is a structural boundary determined by the numerator and pole geometry, not a parameter rename or a finite collection of examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
