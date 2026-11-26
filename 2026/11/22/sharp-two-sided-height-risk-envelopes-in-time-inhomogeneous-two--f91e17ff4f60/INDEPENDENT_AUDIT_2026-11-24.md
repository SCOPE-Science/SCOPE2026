# Independent mathematical audit

## correctness

PASS

The actual increments start at one, and a nearest choice gives one while a farther choice flips the preceding increment. Hence depths never decrease, the newest vertex attains the height, and zero increments cannot be adjacent. Independence gives F_i(z)=z[p_i F_(i-1)(z)+(1-p_i)F_(i-2)(z)]. Reversal R_i(s)=s^i F_i(1/s) gives the determinant recurrence for R_n(-s): the off-diagonal product is s(1-p_i) and the diagonal is p_i (initial entry 1). In the interior, dividing by the positive diagonal on both sides gives a real symmetric weighted path; each eigenvector is determined by its first coordinate, so eigenvalues are simple. Bipartite symmetry gives exactly floor(n/2) nonzero positive/negative pairs and, for odd n, one zero. Reversing and normalizing at z=1 gives a product of r Bernoulli factors times z^h. Compactness of the Bernoulli parameter cube handles p_i=0 or 1. The deterministic odd-index resets make each even increment exactly its independent nearest-parent indicator, proving converse realization. At fixed mean, averaging two Bernoulli parameters raises every convex expectation by the nonnegative second-difference term; choosing the most separated pair at every step drives the parameter spread to zero (the sum of centered squares decreases by half the squared spread). The adjacent-integer secant proves the universal lower bound on integer-valued laws; both extremizers are realized by the reset schedules. The upper variance equality is equality in the sum-of-squares bound, and for the lower one the quadratic secant is strict off the adjacent integers, with the mean forcing a point mass when integral. A line segment between parameter vectors with the same sum realizes intermediate variances by continuity, including the degenerate cases. Independent finite corroboration: at n=8, for all 128 schedules with nearest weights 1/3 or 2/3, enumerated the 128 parent-choice histories per schedule and summed products of integer weights after clearing denominator 3^7; each vector of counts indexed by n minus the maximum depth equaled the reversed recurrence coefficients. This auxiliary check does not supply the general factorization; the frozen verify.py was read, not executed.

## originality

PASS

Credit is confined to the exact time-inhomogeneous tree-height family, its converse schedule realization and the resulting simultaneously sharp tree envelopes. Weighted matching real-rootedness, the binomial convex-order maximum for independent Bernoulli sums, and the adjacent-integer lower benchmark are not independent novelty claims. The closest occupation laws and general inequalities do not establish the attainable family under the tree's attachment controls in the material that could be compared. This judgment is limited by access to the pinpointed primary sources and by the possibility of an equivalent occupation-count formulation.

## value

PASS

A full attainable-law description for a finite, geometrically defined random tree under independent time-varying probabilities is a natural structural result. It converts fixed-mean design into explicit schedules simultaneously bounding every convex loss and classifies the exact variance range, without misidentifying the actual increments as independent or claiming tail ordering.

The dated certificate retains the supplied scientific assessment, sources and limitations.
