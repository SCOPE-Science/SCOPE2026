# Scientific review

## Correctness — PASS

For each finite \(T>0\), the direct information determinant factors into a nonzero time constant and \((1-s^2)(1-t^2)(s+kt)^2\). The global reduction accounts for signs, reflection, coincident points, and all endpoints. The logarithm is strictly concave in the two positive magnitudes, giving a unique magnitude optimizer. The first-order equations reduce to a quadratic equation with a unique admissible root, yielding the exact location pair and value. The location migrations and endpoint asymptotics follow by differentiation and Taylor expansion. `CHECK.py` independently evaluates the original measurement matrix and passes 149121 finite supplementary assertions. Numerical tests do not substitute for the all-parameter proof.

## Originality — PASS, qualified

Aldroubi et al. (arXiv:2004.14032, inspected HTML) treat continuous-band space-time sampling and stability bounds; Alexanderian–Saibaba (arXiv:1711.05878, inspected full HTML sections) treat PDE-scale D-optimal design algorithms; Cheng–Paley (arXiv:2111.01343) treat covariance-and-guidance path optimization; Huang–Needell–Tang (arXiv:2109.14079, inspected HTML) treat randomized graph-space-time sampling. Their examined theorems and stated objectives do not imply an explicit D-optimal assignment of one distinct location at each of two prescribed heat times. The closest indexed exact cycle result instead maximizes the smallest singular value of a four-by-three raw sampling matrix with two sensors at both times; a path-graph D-optimal result instead optimizes a single endpoint's temporal spacing. A specialized earlier two-mode regression or thermal inverse-design identity might have escaped the search; publication priority has not been independently established.

## Value — PASS

The two-dimensional initial-coefficient space is the smallest Dirichlet heat model in which spatial placement must simultaneously resolve differently decaying modes. The theorem completely classifies the two-time D-optimal designs for every positive time separation, including unique reflection equality cases, a nontrivial continuous relocation between geometry regimes, different large-time spatial approach rates, and an exact \(27/16\) limiting information advantage over a fixed geometry. It addresses a motivated finite-information experiment-design problem, rather than an arbitrary table entry. No more general sensor-placement theorem or real-world performance gain is claimed.

## Closest literature and limits

The key difference from general dynamical-sampling frame results is the objective: likelihood Fisher determinant for precisely two scalar time-staggered measurements and two independently chosen continuous positions. The exact comparison risks are pre-existing specialized static sine-regression designs and older heat-identification literature, some of which is available only through abstracts. The result is not independently audited, does not optimize Bayesian posterior risk or mobility-constrained paths, and does not extend by assertion beyond two heat modes.

Self-review: passed. Independent audit: not yet performed.
