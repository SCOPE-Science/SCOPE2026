# Independent mathematical audit

## correctness

PASS

For a=Hx the sequential energy drop is a_i^2+(a_j-H_ji*a_i)^2, including repeats (second term zero). At x=1, Hx=(1-dc)1 and x^T Hx=n(1-dc), so the three ordered-pair types give normalized decreases proportional to 1, 2, and 2+2c+c^2. This bounds all fixed joint laws and forces edge support at equality. Uniform orientations have both margins 1/n, yielding the bracket (2+c^2)I+(2c/d)A in the expected loss as a quadratic form in Hx, with factor 1/n. For eigenvalue lambda, the difference of the unscaled decrease from the lambda=d mode is c(d-lambda)[dc^2+2c(d+lambda)+2(d-1)]/d, strictly positive if lambda<d, also for d=1. Connectedness gives the unique worst direction for this law. The distinct-pair comparator scales the c^2 and 2c/d terms by theta=d/(n-1); its mode function is concave and the difference of its -d versus d endpoint values is 2c[d(2+theta*c^2)-2theta]>0. The formula is strict versus edges exactly for noncomplete graphs; the cycle limit is (2+1+1/4)/2=13/8. The analysis is for one pair; it neither proves uniqueness of the law nor a multistep speedup.

## originality

PASS

The strongest same-object comparison optimizes ordered pairs on a nonregular path and has a different support transition; the cyclic-block result uses a simultaneous, not sequential, operator. Inspected rate theorems do not determine this sharp worst-direction optimum over all fixed ordered laws on regular graphs. On the inspected evidence, the sharp regular-graph statement and comparator are distinct, not a priority guarantee.

## value

PASS

Repeated and correlated coordinate choices are natural competitors for a budget of two exact updates. The theorem certifies that spending both updates along an edge is necessary for minimaxity among all fixed laws, and that regularity alone, without vertex transitivity, suffices for uniform edges to attain the bound. The sharp distinct-pair benchmark quantifies why adjacency rather than merely avoiding a repeat matters. These are one-pair design facts, not a claimed runtime improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
