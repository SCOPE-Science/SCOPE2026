# Independent mathematical audit

## correctness

PASS

Exact terminal-child appointment probability 1/(n-1)_r leads to correct one-/two-vertex inclusion–exclusion excluding a younger counted parent. The uniform factorial-series covariance kernel c(a,b)=e^-a[(1+(a-1)b)e^-b-1] was checked algebraically, including r=1 boundary factors; its integral over 0<b<a<1 is (5-e^2)/(4e^2), diagonal 1/2-e^-1+e^-2/2, total (3-e)/e^2 independently integrated by SymPy. The undirected-root correction has probability 1/(n-1) and changes variance only O(1). Exhaustively enumerated all parent arrays n=3..8 directly for undirected M0, and checked source pair formulas against its verifier source. Existing Holmgren–Janson protected-count CLT supplies normality. Finite checks do not prove uniform o(n^-1) asymptotics.

## originality

PASS

Existing Holmgren–Janson theory already implies the joint fringe-tree Gaussian limit (and hence a one-dimensional CLT); independent contribution is the explicit covariance kernel and evaluated limiting variance (3-e)/e² for undirected leaf-degree zero. Primary Hartle–Krapivsky work treats the same observable but only first-order count and fitted/simulated fluctuations.

## value

PASS

The exact variance is a motivated natural invariant of leaf-neighbor statistics in recursive trees and quantifies cancellation among long-range indicator covariances. It provides the missing calibrated scale for the established Gaussian limit, not a relabeling of a known mean or CLT.

The dated certificate retains the supplied scientific assessment, sources and limitations.
