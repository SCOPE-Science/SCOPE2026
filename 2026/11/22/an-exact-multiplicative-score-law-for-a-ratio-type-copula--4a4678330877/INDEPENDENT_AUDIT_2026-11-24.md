# Independent mathematical audit

## correctness

PASS

The exact theorem survives unchanged. The stated density is the mixed derivative of the copula, with nonnegative values and uniform margins. Independently, transforming (u,v) to (u,z=uv) gives f_Z(z)=2/(1+z)^3 times the integral of (1+z/u^2) from z to 1, hence f_Z(z)=4(1-z)/(1+z)^3 and the stated CDF with no endpoint masses. For t=-log z, the sign of the CDF difference is the sign of H(t)=4/(1+exp(-t))^2-1-t. Its derivative changes once from positive to negative for t>0, at log(2+sqrt(5)); H(0)=0 and H tends to minus infinity. This proves the unique interior crossing and both signs. Transforming the CDF gives P(W<=w)=tanh^2(w/2), the maximum of two independent absolute standard logistics. Integrating the survival function and twice its product with w gives mean 2 and second moment 8 log 2; inversion gives the stated quantile. The frozen crossing decimal was incorrect beyond its leading digits. A separate bisection of H on [2,3] using Python Decimal with 55-digit precision gives z*=0.09920455417194699830218..., consistent with the independent double-precision check. The repaired files correct the decimal and the checker count: the code contains 13 symbolic asserts and 16 numerical/domain assertions, not 14 and 16. The scientific notes now describe the assertions actually in the code; the verification front matter is unchanged. The corrected finding was reassessed against the exact proof and the verified decimal.

## originality

PASS

Best-of-knowledge pass for the complete ordinary product law and unique crossing relative to the independent product. The original copula, its validity and its known dependence properties are prior work. The historical access risk remains explicit in the corrected finding.

## value

PASS

The ordinary product calibrates a multiplicative score for a previously specified dependence model. Its exact law provides a quantile rule and resolves how independence miscalibrates lower versus higher thresholds. Uniform marginals imply the same mean negative-log score as independence, but do not give a unique threshold separating the opposite errors. The exact sign law and threshold, not the standard change-of-variables recipe or the marginal mean, are the substantive contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
