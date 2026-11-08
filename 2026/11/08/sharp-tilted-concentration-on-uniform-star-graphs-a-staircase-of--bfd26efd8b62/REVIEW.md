# Self-review: sharp star-graph Laplace envelope

## Correctness — PASS

The claim concerns the *entire* centered exponential moment envelope for real one-Lipschitz functions on the uniform unit-edge star with at least three leaves, for every real tilt. Fixing the hub value to zero makes the feasible region a cube. The tilted covariance Hessian is positive definite because the hub retains positive tilted probability, forcing every maximizer to be a sign vertex. The consecutive-count ratio is strictly decreasing and has a unique crossing at the stated \(X_n(t)\). The derivative of \(X_n\) has an explicit sign certificate using the hyperbolic-sine square identity and a positive group of summands. Boundary limits, integer ties, exact threshold counts and the fixed-tilt infinite-leaf limit all follow by the displayed steps. The embedded standard-library checker provides independent exact-rational finite spot checks; those checks are not the infinite proof.

## Originality — PASS, with residual risk

The relevant 2006 primary paper by Bobkov, Houdré and Tetali solves the centered Laplace envelope for a path and the sub-Gaussian constant for a complete graph; it therefore contains the already known \(K_{1,2}\) case, which this claim excludes. Stars with three or more leaves have a different metric: distinct leaves are at distance two, and the hub links all arms. The 2009 Sammer–Tetali transportation paper treats cycles and concentration, not the present star-specific leaf-sign staircase. Searches against indexed mathematical findings and the accessible previous own claim titles/objects did not reveal the same family of centered exponential-moment maximizers, integer tilt thresholds, or large-leaf limit. The current claim does not present the inherited convexity principle, general sub-Gaussian definition, or the path case as new. Relevant unindexed exact star-Laplace results remain a possible priority risk.

## Mathematical value — PASS

The exact centered Laplace envelope is the input for sharp Chernoff bounds for all tensor powers of a finite graph, a finer object than a single variance/spread or variance-proxy constant. The theorem determines not merely its value but all optimal potentials, with \(\lfloor n/2\rfloor-1\) distinct changes of optimizer topology as the tilt increases and a nontrivial limiting leaf-sign density. The transition staircase is not a restatement of the known path or complete-graph formulas; it quantifies how branching redistributes rare positive deviations. It naturally motivates new concentration comparisons on branching trees and weighted stars, without asserting those extensions.

## Scientific limitations and residual risks

The theorem is for uniform stars with at least three leaves and unit edge lengths. It does not explicitly evaluate the subsequent continuous tilt supremum defining the optimal sub-Gaussian quadratic proxy; nor does it address nonuniform measures or other trees. The literature comparison is necessarily incomplete outside the inspected primary papers and indexed findings. Independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
