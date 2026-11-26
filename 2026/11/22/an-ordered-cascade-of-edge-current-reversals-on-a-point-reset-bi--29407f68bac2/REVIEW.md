# Independent mathematical audit

## correctness

PASS

The continuous-time reset generator gives the homogeneous recurrence off 0, with π_n=π_0. The two roots x<1<y have xy=p/q; the positive unnormalized profile x^j/(1−x^n)+y^j/(y^n−1) takes the same value at j=0 and n, satisfies the recurrence, and the last balance equation follows by conservation. Irreducibility makes this the unique stationary law. For the hopping-only current, dividing the negative root contribution by the positive one gives R_j=x^(n−2j−1)F_j with F_j=h^(j+1)(1−x)(1−x^n)/[(h−x)(h^n−x^n)], h=p/q. At fixed x, F_j(1,x)=1 and ∂_h log F_j<(j+1−n)/h−1/(h−x)<0. Thus nonnegative exponent implies a permanently positive current, including exponent zero. For negative exponent, log R_j is strictly decreasing in x with nonzero derivative: both rational factor derivatives after grouping are negative, as is the power term. Since x′(r)<0 and x goes from 1 to 0, R_j increases from zero to infinity with a simple unit crossing. R_(j+1)/R_j=h/x²>1 then gives strict reversed ordering of the rates, exactly floor(n/2) distinct crossings and the contiguous counterflow arc. For the small-bias expansion, analyticity follows by solving the normalized finite system near δ=r=0 after scaling rates by q. The r-derivative of the current at zero bias obeys a_j−a_(j−1)=−1/n and Σa_j=0, while J_j(δ,0)=δ/n. The implicit-function slope is therefore 2/(2j+1−n), positive on each reversing edge; the error is O(δ²/q) for fixed n,j,q, not uniform in n. Independently bisected actual stationary currents for the n=6 example by pivoted Gaussian elimination on the nonreset balance equations and normalization (r bracket [0,5]); edges 5,4,3 gave 0.226733124762156, 0.484739267504340, 3.435620322241912. These floating-point examples are ancillary. The submitted rational checker and verification notes were inspected without executing the uploaded code.

## originality

PASS

The general reset stationary representation and ideas of current reversal are prior background. The distinct supported result is the global, all-size and all-edge record of simple hopping-only crossings with strict rate ordering and weak-bias thresholds. The closest discrete and continuum statements do not supply that classification. This is a bounded best-of-knowledge comparison, not a priority certificate.

## value

PASS

The model is a canonical nonequilibrium ring with one reset destination. The result explains precisely how local physical hopping can flow against the global clockwise bias even though the total hopping current remains positive. It proves absence of hidden or repeated local crossings and gives a sharp spatial and rate sequence and its near-equilibrium scale, none of which follows from forward stationary probabilities or conservation alone. The observable remains tied to actual hopping transitions and does not depend on assigning paths to teleportation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
