# Independent mathematical audit

## correctness

PASS

On the connected feasible region the trace-inverse Hessian is strictly positive on a nonzero weight perturbation: the perturbed Laplacian is nonzero by its off-diagonals, and after conjugation the quadratic trace is that of its square against a positive-definite weight. The compact price simplex has a strictly positive feasible point and objective tending to infinity at disconnected limits. Uniqueness forces S3×Sm invariance, and connectivity forces cross conductance b>0. Vectors of sum zero within each block and the block-constant contrast give eigenvalues x=3a+mb (twice), y=mc+3b (m−1 times), and nb. The reduced objective divided by n is therefore 2/x+(m−1)/y+1/(nb). Its classwise KKT stationarity is equivalent to individual-edge stationarity at invariant points because each class gradient is the common edge gradient times its class size. In the interior, y²=rx² and (x/b)²=n[3(m+1)/r−2m]. Positivity breaks at the smaller of r_A=(m+1)(m+3)/(m(m+2)) and r_C=3(m+4)/(2(m+3)); the sign of r_C−r_A is that of m³+4m²−6m−18, negative for m=2 and positive thereafter. For m≥3 on a=0, y²/b²=m(m+1)(m+3)/(m+2)>9; the missing triangle gradient has acceptable slack precisely at r≥r_A. For m=2 on c=0, (x/b)²=(45/r−15)/2, with missing-complement slack iff r(x/b)²≤9, i.e. r≥9/5, and a>0 iff r<45/23. With both deleted the budget gives b=B/6, and the scaled KKT multiplier 23/(90b²) yields group slacks (23r−45)/(30b²) and 1/(30b²). This covers both boundaries including equality, so no other regime is needed. Budget scaling and the three eigenvalues give the stated minimum and r_A−1=(2n−3)/[(n−3)(n−1)].

## originality

PASS

The support classification and the unmarked-before-marked deletion at n=5 are the distinct claims, not the trace-inverse objective, convexity, group averaging or KKT method.

## value

PASS

The solution gives a complete active-set classification for a motivated edge-price pattern, not just an optimization prescription. The cheaper complement edge is the first omission at exactly n=5, even though the entire premium triangle survives on a nonempty interval. The proof accounts for why this support topology cannot occur for larger sizes under the same budget/objective, and supplies the exact thresholds for comparisons or design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
