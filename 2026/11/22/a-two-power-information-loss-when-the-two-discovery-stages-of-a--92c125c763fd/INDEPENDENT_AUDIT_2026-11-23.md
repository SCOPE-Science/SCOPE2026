# Independent mathematical audit

## correctness

PASS

Independence of the two failure counts follows by restarting the iid draws at the first usable coupon: the second success probability is independent of its label. With zeta=1/(2m-1), eta=zeta^2, the two inverse success probabilities are h(1-zeta) and h(1+zeta). Multiplying their geometric pgfs gives the stated rational pgf, mean 2h-2 and variance 2h^2(1+eta)-2h; these invert to m and theta. At homogeneity the labeled score is (S2-S1)/(h-1), of information 2/a. The derivative pgf for the sum is h^(-2)(1-z)^2/(1-az)^4; coefficient division by the homogeneous negative-binomial mass gives the stated quadratic score. The factorial moments E[(T)_j]=(j+1)!(h-1)^j give mean zero, orthogonality to T, and information 1/(3a^2). Tail bounds for the coefficient derivatives follow from a common complex-parameter neighborhood and a pgf circle of radius just below 1/a; positive physical masses have a lower geometric bound with base arbitrarily close to a. These bounds justify the third-order log Taylor remainder, a rowwise score CLT and a second-derivative LLN (choose geometric bases close enough for the second moment). The increments are asymptotic to -1/(2m^3) in eta and -1/(2m^2) in zeta; the information times n times their squares gives both stated Gaussian variances, with mean minus half the variance. Taylor expansion of KL plus Pinsker gives merging below the thresholds. The midpoint tests have influence functions (3a^2/2) times the total score and (a/2) times the pair score; their limiting variances, half-separations and the likelihood-ratio errors agree. Uniform moments and the denominators bounded below by 2 in the sample statistics give the supercritical consistency and compact-h scope. The fixed-mean path is a hard nuisance comparison (the homogeneous h score is orthogonal to both shape scores), not a claim for common known theta or an unrestricted global minimax theorem. I inspected the exact-fraction diagnostic without running it. Independent bounded diagnostic: at h=2, sum the convolved mass times x-log(1+x), x=P_(m+1)(t)/P_m(t)-1, over t=0,...,160, and use the independent two-geometric KL formula for the pair. At m=192 the scaled values were 0.166662 and 0.500030, near 1/6 and 1/2; this does not prove the limits.

## originality

PASS

Pass is for the fixed-mean repeated-testing comparison, its critical constants, and nuisance-free efficient moment rules, not for the geometric convolution, the vanishing first-order heterogeneity term, or classical likelihood theory. The closest published statements establish ingredients, not an inference theorem that covers the two observation regimes.

## value

PASS

This measures a concrete information loss in a natural recording decision: remembering the two discovery stages saves two powers of the number of coupon types in independent repetitions at matched mean. Exact population identifiability alone does not predict the loss. The sharp errors and nuisance-free efficient tests specify the operational difference even at the critical scales. The motivation depends on an unknown usability rate and is not extended to general numbers of discoveries or fixed known rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
