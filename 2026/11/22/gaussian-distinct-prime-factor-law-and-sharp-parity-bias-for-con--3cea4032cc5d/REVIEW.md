# Independent mathematical audit

## correctness

PASS

A prime divides the product/LCM quotient exactly when at least two entries are multiples. For L=k+1, this holds always for p<=L/2, never for p>=L, and on L-p residues for the intermediate primes. CRT gives independent Bernoullis. Shifting by any candidate period times T_k/p isolates the p-indicator, forcing divisibility by p; the empty product case has period 1. The parity product vanishes iff 3p=2L, hence iff p=2 and k=2. The PNT integrals of t^(-1)-1 and (t^(-1)-1)(2-t^(-1)) give log 2-1/2 and 3 log 2-2, and the constant small-prime count adds 1/2 to the mean coefficient. Bernoulli third absolute moments are bounded by the variances, so Berry–Esseen divides the total third moment by sigma^3 and gives O(1/sigma). For parity, g(t)=log|3-2/t|=log 3+log|t-2/3|-log t integrates to -(2/3)log 2. With x=L and eta=exp(-c sqrt(log x)/3), truncation to log eta makes total variation O(sqrt(log x)); Stieltjes summation with the quoted PNT error makes its weighted prime-sum error o(x/log x). The truncated integral converges in L^1 and 1<=|3p-2x| for integers x>=4, so the O(eta x+1) affected integers contribute an error at most O((eta x+1)log x)=o(x/log x). This proves the magnitude asymptotic without an unsupported uniform-prime approximation at the singularity.

## originality

PASS

The complete finite law is available by compressing prior joint valuation data. This is credited as coverage, not a novel law. The distinct content assessed here is the claimed growing-window law and sharp logarithmic parity-bias asymptotic: the prior finite census supplies inputs but gives neither the uniform asymptotic estimates nor the constants for these observables. The strongest other quotient limits found treat log size, maximality, or the Liouville sign, not the statistics under audit.

## value

PASS

A natural arithmetic statistic has both ordinary Gaussian fluctuations and a substantially smaller alternating bias, with explicit constants. The Gaussian part is a routine distributional mechanism once the prime support is identified, but the log bias measures arithmetic cancellation not captured by the Gaussian law or the finite census alone; the singular prime sum is a worthwhile additional estimate for this established quotient family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
