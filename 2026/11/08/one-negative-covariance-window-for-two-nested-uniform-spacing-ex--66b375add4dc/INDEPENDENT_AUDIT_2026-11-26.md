# Independent mathematical audit

## correctness

PASS

Root the cyclic gaps at one designated sampled point: conditional on its rotation, the remaining n−1 rotated points are iid uniform, so their order-statistic gaps (including both ends of the unit interval) have the required Dirichlet law. The gap counts are invariant to the root; the Dirichlet claim need not hold for an indexing rooted by a fixed external origin. Translating the simplex gives the joint threshold probabilities; separating equal indices from unequal indices yields the exact covariance. The bracket is (1−s^x)(1−g(x)), where g=x(1−exp(−δx))/(exp(αx)−1), α=−ln s and δ=ln(s/t)>0 (since s−t=ab/(1−b)). The positive term in (log g)'' is α²/[4 sinh²(αx/2)]<1/x², so log g is strictly concave and g tends to zero at both ends. Its level 1 has at most two roots and its strict superlevel set is a single bounded interval or empty. Here real x is an interpolation of the sign expression, not a noninteger-sample covariance. Independent exact rational replay of F_n=1+(n−1)(4/5)^(n−1)−n(17/20)^(n−1) gave F_5=4539/160000, F_6=−38131/1600000, F_13=−100389363459021/4096000000000000, F_14=180270269513333/8192000000000000. Continuity and the two-root bound put a root strictly in each of the two transition brackets and rule out any other zeros. The supplied notes and checker were inspected, not executed.

## originality

PASS

Credit is for the global fixed-threshold sample-size sign classification and a sharp re-entrant witness, not for the Dirichlet probability or the resulting fixed-n covariance formula. The closest distinct compared results vary a threshold rather than n or concern different occupancy observables. The available evidence does not establish equivalent coverage of the credited claim; this is a best-of-knowledge assessment.

## value

PASS

Nested counts in a standard spacing model can be positively associated at both small and large sample sizes but negatively associated at intermediate sizes. The theorem gives the exact allowed geometry of that reversal for every threshold pair in scope, and the rational witness proves the two-reversal bound is sharp. This is more informative than the covariance formula or a finite simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
