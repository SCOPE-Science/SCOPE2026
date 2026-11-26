# Independent mathematical audit

## correctness

PASS

The upper absorber has incoming rate lambda from state n=m-1. The defective transform at state 1 is lambda^n/det(s I-Q) by the tridiagonal resolvent cofactor; its normalized logarithmic derivative gives the conditional mean. The determinant and its s derivative at zero give respectively the geometric sum B_n and the numerator A_n after scaling. At rho=0 this also gives n/lambda, as required for pure birth. For the derivative numerator the coefficient at degree j is the sum of (2i-j-1)(i+1)(n-i) over max(0,j+1-n) <= i <= min(n-1,j+1); expanding the power sums gives the two stated factors. Thus n=1 and n=2 are decreasing (zero endpoint slope for n=2), and for n>=3 the coefficient sequence has exactly one sign change, with opposite signs at zero and infinity. Reciprocity forces f'_m(1)=-f_m(1)/2<0 for f_m=lambda E[T|S], so the unique critical point lies below 1. Independently, in log-rate coordinates the normalized A_n weights have mean (m-2)/2 and variance (m^2-4)/20, while the B_n weights have mean (m-1)/2 and variance (m^2-1)/12. These give f_m(1)=(m^2-1)/6 and f''_m(1)=-(m^2-1)(m^2-19)/180. On the O(m^-2) left window the positive eigenvalues are bounded below by a constant times j^2/m^2, their first derivatives are O(j^2/m^2) and higher derivatives through order 3 are bounded; summing the differentiated inverses gives the required O(m^4) Taylor bound. The derivative then brackets the optimum at 1-(15+o(1))/m^2 and the peak gain is 15/12-225/360=5/8 in units of 1/lambda. Independent polynomial bisection reproduces rho_4=0.2828147640150715, f_4=3.155153445116 and success probability 0.721802949254. The uploaded checker was inspected but not run.

## originality

PASS

Bounded pass for the all-threshold maximizer classification and the two large-m constants. The conditional passage-time problem, spectral machinery, and examples of a nonmonotone time curve are not new. The examined prior results do not provide the all-m derivative sign result or the shrinking-window optimizer and peak limits.

## value

PASS

This separates a conditional dwell-time bottleneck from the monotonically decreasing probability of success. The onset threshold and global uniqueness generalize an observed numerical effect, and the two asymptotics identify both the rate scale at which it occurs and the absolute size of the excess rather than suggesting a sizable relative increase. This is useful for interpreting conditioned passage times in the reference chain, without implying that stronger dissociation improves attachment yield.

The dated certificate retains the supplied scientific assessment, sources and limitations.
