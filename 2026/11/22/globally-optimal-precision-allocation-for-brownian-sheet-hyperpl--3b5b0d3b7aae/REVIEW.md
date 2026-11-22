# Scientific review

## Correctness — PASS

The statement specifies the exact Gaussian field, target, observation functionals, independent noise model, precision normalization, and the boundary case of zero allocated precision. Tensor covariance integration gives the rank-one cross-orientation covariance factorization. The conditional residuals of distinct hyperplane averages are mutually independent given the volume integral; their positive variances and the full posterior-precision formula are established algebraically. Each channel has a unique location maximizer by a one-crossing derivative, and the optimum per-channel information is **strictly concave** in its assigned precision, proved by explicit signed polynomials. Strict Jensen inequality therefore optimizes all allocations including the boundary. Dimension scaling and noiseless limit follow from the unique root and exact risk. `verify.py` passed exact rational covariance checks and supplemental numerical comparisons, but the infinite theorem rests on the written proof.

## Originality — PASS, provisional publication priority

Longi et al. (2020), *Sensor Placement for Spatial Gaussian Processes with Integral Observations*, was inspected in full, especially its Gaussian line-covariance formulas (2–3), model-based placement criteria, experiments and discussion. It develops numerical/model-based and geometric placement methods for line observations, rather than the present all-dimensional tensor Brownian-sheet scalar integral with one axis-normal complete hyperplane per direction and an optimized shared noise budget. Hendriks et al. (2018) study numerical evaluation of **squared-exponential** double-line covariance integrals; the inspected sections do not supply an optimal Brownian-sheet volume rule. General Bayesian quadrature work supplies posterior-covariance machinery but does not itself entail global location/precision uniqueness or the dimension crossover. The related single-point Brownian-sheet volume-design problem has different observation functionals and does not imply this theorem. Targeted publication and mathematical-record searches found no covering statement, but this is best-knowledge originality, not proof of historical priority. Further priority work is advisable.

## Value — PASS

A complete exact experimental-design theorem answers a naturally motivated problem in integrated sensing of a spatial Gaussian field: how to distribute a finite precision budget across one full slice for every coordinate direction and where to place each slice. The result is not merely a special value of a general estimator: it proves conditional independence after projection on the target, global uniqueness of equal allocation, and an exponential-in-dimension precision crossover. The noiseless optimal residual fraction \(1/(8d+1)\) gives a useful benchmark for genuinely multidimensional line/hyperplane measurement designs. The domain restriction is explicit and scientifically important.

## Remaining limitations

Independent mathematical and publication-priority assessments are outstanding. The observed cross-direction conditional independence uses the product Brownian-sheet kernel and complete slices. No claim is made for oblique/partial measurements, repeated orientations, correlated noise, different instrument-cost normalization, sequential policies or reconstruction of the entire field.

Self-review: passed. Independent audit: not yet performed.
