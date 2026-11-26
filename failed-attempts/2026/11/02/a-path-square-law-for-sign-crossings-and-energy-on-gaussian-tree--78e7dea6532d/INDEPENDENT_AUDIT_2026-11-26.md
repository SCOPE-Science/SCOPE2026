# Independent mathematical audit

## correctness

PASS

The exact local identity can be checked without using the frozen integration. For a standardized Gaussian triple (U,V,Z), write r=Corr(U,V), a=Corr(U,Z), b=Corr(V,Z). Tilt the law by exp(t Z^2/2) and normalize for t close to zero. The derivative at zero of the tilted crossing probability is one half the sign–square covariance. Regressing (U,V) onto Z shows that the tilt changes just Var(Z) to 1/(1-t), adding t/(1-t) times (a,b)(a,b)^T to the bivariate covariance. Hence the derivative of the new U,V correlation is ab-r(a^2+b^2)/2; differentiating arccos(r)/pi gives precisely [r(a^2+b^2)-2ab]/[pi sqrt(1-r^2)] for the covariance. This argument allows zero residual covariance and thus covers z at an edge endpoint. Independent tree innovations and variance one give the product along each path (condition at the last common ancestor). On the u-side of edge uv this means a=eta, b=r eta; substitution gives -r sqrt(1-r^2) eta^2/pi. Covariance bilinearity gives the weighted result; if all r have a common nonzero sign all path squares are positive, so there is no cancellation and nontrivial weights give strict sign. In the chain there are 2(n-1-h) site-edge pairs at distance h, including h=0, and the divided geometric sum tends to 1/(1-rho^2) for fixed |rho|<1. The non-Markov example has leading principal minors 1, 3/4, 9/50 and numerator 33/200 with sqrt(1-r^2)=sqrt(3)/2, proving positive definiteness and the stated opposite sign.

## originality

FAIL

The exact general Gaussian sign-event/square covariance is already explicit in earlier Resultary e0f4a1d0a49b, Proof §1. The proposed tree law follows by substituting the defining Gaussian Markov path correlations into that stronger identity; the weighted sign follows by linearity and same-sign summands. The AR(1) local/aggregate covariances and limit are explicitly given in the earlier 96b52b268e48. The non-Markov example is a positive-definite numerical instance of the same general signed formula. Thus the central claim is mechanically implied even though a standalone tree statement did not surface. This verdict rests on readable formulas, not on inaccessible texts or priority assumptions about same-day records.

## value

FAIL

The statistic and Markov tree are natural, and the specialization is potentially useful as exposition. But the entire path-square invariant is a routine substitution into the known stronger covariance formula, the common-sign result is a same-sign sum, the chain calculation is already explicit, and the counterexample fixes one admissible triple in an open region easily read from the numerator. There is no distinct nonmechanical scientific result in the frozen package; rejection does not call its formulas incorrect or deny their descriptive utility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
