# Independent mathematical audit

## correctness

PASS

The rooted-plane-tree contour is a Dyck path; leaves correspond to peaks and the leftmost-leaf depth to the first-peak height. Direct Narayana normalization of the exact joint count gives Pr(H=h | L=k)=h*C(n-h-1,k-2)/C(n,k); k=1 is a sentinel. Nested uniform k-subsets supply the monotone second-order-statistic coupling; finite-population gaps give the mean/variance and conventional sampling limits give Beta, Gamma and negative-binomial scaling. Independent enumeration verified 285 complete joint cells through n=9. The infinite statements follow from elementary generating functions and sampling, not from this finite check.

## originality

FAIL

The central purported new conditional first-ascent/leaf-depth law is fully implied by Emeric Deutsch, Dyck path enumeration, Discrete Mathematics 204 (1999), §6.7, equations (6.24)-(6.27). In fact (6.27) is precisely the unnormalized joint (peaks, first-peak-height) count h/n*C(n,k-1)*C(n-h-1,k-2), and division by the standard Narayana count yields the submitted conditional formula verbatim. The remaining sample-order-statistic realization, simultaneous monotone nesting and scaling regimes are elementary corollaries of this already published count, not a surviving distinct research result. The source result was not identified in the original self-review, which acknowledged it as a possible risk. Neither different object naming nor newer finite verification recovers priority.

## value

FAIL

The conditioned first-leaf statistic itself is natural, but its exact joint distribution was published in 1999 and the proposed additional coupling is the immediate order-statistic coupling obtained by revealing a uniform random permutation, with standard gap moments and Poisson/order-statistic limits. As a standalone remaining contribution this is a textbook-level reformulation of the known enumeration rather than a mathematically motivated new theorem. Correctness of the package does not change that value assessment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
