# Independent mathematical audit

## correctness

PASS

For s zeros, their cross-edge cost is (s²−u²−v²−w²)/2. Sorting occupancies, the first partial sum is at most a and the second at most a+b, as well as at most s. Filling largest shores first attains both partial-sum bounds, so strict convexity of the squares forces the same sorted vector in every equality case. This yields the sharp piecewise lower bound with slopes 0,a,a+b. Its three positive-field vertices are feasible with zero nonpreferred edge cost. At h=0 any proper coloring uses three disjoint nonempty shore color sets and hence exactly one color per shore. At h=a the largest shore must be full of zeros and the extra k may occupy only one other shore. For partial filling of that shore, both nonzero shores are nonempty and must use opposite constant colors; when the shore is exhausted every vertex of the last shore chooses independently. The two cases add, including when their monomials coincide (e.g. k=c on B and all of C). This gives the displayed P_a and its sum 3(2^b+2^c)−6 even for c=1. At h=a+b strict capacities force A and B full; all three colors of each C vertex are free, giving x^(a+b)(2+x)^c. The strict regimes follow from unique minimizing s and the same equality rules. The optional residual-entropy limits follow by bounding the first degeneracy between constants times 2^b and by taking logs of the other exact counts.

## originality

PASS

The all-graph field partition-function identity covers the model and implicitly its coefficients. The explicit all-size ground-energy and full labeled occupation classification at the two finite-coupling crossings is not stated or immediately supplied by the inspected comparisons. Related findings change either the geometry and field or the spin count and optimization criterion. Credit is limited to the explicit tripartite classification.

## value

PASS

An all-size exact finite-field classification for the natural first three-shore family distinguishes independent color choices when a shore is saturated from constrained two-shore choices. It separates two distinct critical entropy mechanisms and also exposes an extensive intermediate degeneracy, neither of which the ground-energy envelope alone determines. The critical polynomials are useful finite-size information, not just checks at chosen parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
