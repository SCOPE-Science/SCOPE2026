# Independent mathematical audit

## correctness

PASS

The ranking is a uniform fixed-content word. Its initial and terminal runs give the minima and maxima, respectively. Uniform compositions of one color into the gaps of the other give the mean and same-color products. Integrating the cross-color joint probability over 0<x<y<1 gives 1-1/binom(a+b,a) after multiplying by ab. Combining these recovers (1), including the a=b=1 degenerate case. The exact independent replay verifies the difference factorization and the 65 strictly positive coefficients of the cleared lower bound for a≥3, and for a=2 verifies the degree-six numerator with coefficients 1,23,219,1129,3188,4056,936 over a positive denominator. The diagonal lower bound after a=u+2 has numerator 14u³+76u²+122u+48; the a=1 polynomial and fixed-a negative quadratic tail check separately. For scale, put e=1/a and r=(b-a)/a in the rational part F. Then F(0,r)=0, its e derivative there is -r²(r+2)³/(r+1)³, and the e² coefficient at r=0 is 8. Taylor expansion at r=c√e with bounded c is uniform; the reciprocal binomial is at most (2a+1)/4^a. This gives the claimed limit and, by monotonic sign bracketing on both sides of c=1, b_*(a)-a~√a. No finite-size tie is excluded. Supplied verify.py was inspected but not executed; separate exact replay: branches/afdeadca-c733-4153-b111-b74305c48a13/replay_certificates.py and replay_certificates.txt.

## originality

PASS

The finite covariance is covered by summation of general dyadic joint probabilities; no separate novelty credit for the ranking reduction or (1). The strict integer imbalance monotonicity and sharp square-root threshold survive comparison with the known pairwise formula, conditional peak-labeling papers and differently defined run statistics. This is qualified best-of-knowledge coverage, not exhaustive historical priority.

## value

PASS

Strict separation of positive and negative mixed count covariance is a meaningful all-size dependence classification, not an isolated exact entry. A square-root amount of shore imbalance already changes the balance of the competing dyadic terms; the sharp limit identifies that scale and the formula resolves finite boundaries. The scope is iid atomless heights on bicliques, not arbitrary graph modifications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
