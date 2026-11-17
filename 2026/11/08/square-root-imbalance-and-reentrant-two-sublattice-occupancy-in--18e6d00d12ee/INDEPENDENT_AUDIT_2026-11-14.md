# Independent mathematical audit

## correctness

PASS

Partition configurations on K_{a,b} into empty, left-only, right-only, both-nonempty classes, with exact disjoint weights 1, (1+2z)^a-1, (1+2z)^b-1, 2[(1+z)^a-1][(1+z)^b-1]. For a=n, b=n-floor(kappa sqrt n), z=c/sqrt n, Taylor logs yield three nonzero limiting weights exp(-2c²), exp(-2c²-2kappa c), 2 exp(-c²-kappa c), with empty weight vanishing. Normalizing gives P_B(c)=[1+exp(-c²)cosh(kappa c)]^{-1}. The derivative sign is the negative of -2c+kappa tanh(kappa c); since tanh(t)/t strictly decreases, the exact reentrance threshold is kappa>sqrt2 with a unique minimum c*. Conditional binomial laws and O(sqrt n) variances prove the three-atom count limit. Fixed-c pointwise convergence at three chosen c values proves nonmonotonicity of finite-n probability for all sufficiently large n in the supercritical case. Independent direct enumeration for all 1<=a,b<=3 and z=1/3,2/3 matched exact four-class partition weights. No claim of a thermodynamic phase transition or finite-n monotonicity below threshold.

## originality

PASS

The exact finite K_{a,b} partition enumeration and WR graph-homomorphism interpretation are familiar, but among the inspected full published primary and Resultary sources none established the simultaneous c/sqrt n fugacity and kappa sqrt n side-imbalance crossover, its three-atom occupation law, or the unique sharp kappa=sqrt2 reentrance boundary for a finite-volume observable. Earlier nonmonotonic WR papers analyze Gibbs symmetry-breaking on modified trees and unrelated bounded-degree lattices, while Cohen-Perkins-Tetali treat regular-graph occupancy extrema. This is best-of-knowledge originality with named inaccessible primary literature risk.

## value

PASS

The precise competition of one-side/two-side occupancy sectors in a canonical high-degree bipartite WR model gives a motivated sharp critical window and previously nonobvious reentrant event-probability threshold. The three distinct normalized occupation-count atoms and the exact uniqueness of the reversal are coherent structural results; they do not purport to be thermodynamic phase transitions. A finite graph count alone would be standard, but the scaling classification is a useful natural asymptotic invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
