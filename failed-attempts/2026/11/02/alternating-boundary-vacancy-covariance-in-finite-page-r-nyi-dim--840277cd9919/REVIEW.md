# Independent mathematical audit

## correctness

PASS

Under the uniform order of path edges, conditioning on the first accepted edge leaves independent uniform relative orders on the disjoint fragments. The marginal recurrence gives A(z)=z exp(-z)/(1-z); the joint recurrence divides the coefficient of z^(n-2) in A(z)^2 by n-1. For m=n-4 the coefficient sum is (m+3) times the partial sum of exp(-2) minus 2(-2)^m/m!, giving the stated joint formula. Taylor's remainder gives b_n-exp(-2)=2(-2)^m/m! times [I_m-1/(m+3)]. The strict Jensen bound I_m>exp(-2/(m+2))/(m+1)>1/(m+3) follows from the beta mean and log((1+x)/(1-x))>2x for x=1/(m+2). The marginal square differs from exp(-2) with the opposite sign. The beta moment expansion has leading difference 2/[(m+1)(m+2)(m+3)] with O(m^-4) error; the marginal contributes O(1/n!), verifying the coefficient and relative O(1/n) error. For n=2 both endpoints are occupied and for n=3 one remains vacant with equal probability, giving zero and -1/4 respectively.

## originality

FAIL

A distinct earlier Resultary record contains the same finite open-path covariance formula, strict parity at every length, and the same sharp factorial scale including the relative O(1/n) error in its proof. The alternative Jensen estimate does not change the result or its scope.

## value

FAIL

The finite endpoint covariance is a meaningful observable, but this record rederives an already available exact formula, all-length sign and quantitative asymptotic in the same model. The use of Jensen in place of the earlier pointwise exponential inequality does not establish an independently useful new bound or extension. There is no substantive surviving result to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
