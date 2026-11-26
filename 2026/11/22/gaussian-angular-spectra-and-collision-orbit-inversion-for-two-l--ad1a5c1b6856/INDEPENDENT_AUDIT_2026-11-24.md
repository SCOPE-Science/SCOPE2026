# Independent mathematical audit

## correctness

PASS

The largest sum is the pair of marginal maxima; the second is the larger of the two one-coordinate replacements by a marginal runner-up. Every other entry is bounded by at least one of these candidates, and entries differing in both indices are smaller than both. Each candidate order is achievable by choosing the relevant gap strictly smaller and fixing the labels. Positivity and w1>w2 give distinct vectors within each orbit and the singleton support in one block distinguishes the orbits. The strict top-two inequalities give a unique weighted-sum maximizer. Uniform independent rank permutations give the stated orbit cardinalities and the per-vertex probabilities. The gap survivor is the integral conditional on the value/label of the top Gaussian; its derivative is dominated on bounded t intervals by a constant times phi(x), so the density integral and independent-gap comparison are valid. Summing squared masses gives C, including the balanced case. Independent check at (2,3): for the three ordered column labels write U=X1−X2, V=X2−X3, and let W be the difference of the two independent row coordinates. Alpha is six times the positive orthant probability of (U−W,U+W,V), with correlations 0 and twice −1/(2 sqrt(2)). The centered trivariate sign expansion gives alpha=3/4−(3/pi)asin(1/(2 sqrt(2)))=0.4049198157560762, and C=0.0568367116719710 (python3 /workspace/reproductions/5.py; output 5.txt). For the limits, Mills' ratio gives m tails tending to exp(−x) under the stated scaling; disjoint threshold cells give independent Poisson counts, hence joint marginal top-r convergence. The exponential map takes the first two limiting values to the first two unit Poisson arrivals; their ratio is uniform, giving a rate-one log gap. Rescaling yields independent rates sqrt(a),sqrt(b); comparison and the minimum give both limits. The squared-mass ratio is the bounded positive limiting odds squared times (q−1)/(p−1), proving the inversion and constants for a≠b. Every pair outside the first r rows or columns has at least r strictly greater entries in its own column or row, even in the limiting field. The finite r×r limiting array has no equal values almost surely by the joint densities of the two independent finite lists; sorting hence preserves convergence with ranks. The finite check does not prove the limit. The frozen slogan's 'exactly two ... levels' should be read as two orbits with at most two distinct masses: at p=q the masses coincide. The Finding itself gives the correct balanced case and does not require two distinct masses.

## originality

PASS

The supported contribution is the evaluation of the isotropic Gaussian cone and collision laws for these two orbits, the quantitative inversion for unequal growth, and the joint fixed-rank additive-grid specialization. The two exposed orbits, additive scoring and lineup cones are antecedents. The marginal Gaussian extreme-value convergence is standard and is not separately credited as new.

## value

PASS

This is a motivated metric invariant of a natural lineup polytope: all cone probabilities reduce to one spacing comparison, and the two-direction coincidence law reveals why the majority single-exposure orbit becomes rare among collisions. The limiting constants and orbit selection give genuinely different information from the known enclosing sphere and vertex counts. The additional marked top-r limit describes the rank structure of the same model, not just its single largest score.

The dated certificate retains the supplied scientific assessment, sources and limitations.
