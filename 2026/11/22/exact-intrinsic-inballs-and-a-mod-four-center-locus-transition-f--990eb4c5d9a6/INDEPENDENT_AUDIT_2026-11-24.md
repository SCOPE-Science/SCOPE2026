# Independent mathematical audit

## correctness

PASS

In the repaired odd case, the columns are I+Sᵀ up to scaling and centering. Odd alternating closure makes this incidence map invertible, so the hull is a simplex in 1⊥. The normalized facet height opposite vertex i is 1−n, with all other heights 1 by centering. The scaled normal (α/2)w alternates between −(n−1)/2 and (n+1)/2 with multiplicities (n+1)/2 and (n−1)/2, hence the exact norm squared (n−1)²(n+1). The normal sum vanishes under cyclic shifts. Summing the equal-norm inequalities proves the global bound attained at zero, and spanning forces the center to be zero at the bound. Undoing the scale α/2 gives 2/√(n(n²−1)) for the standard edge polytope. A separate exact linear-system reproduction through n=26 passed 1,034 checks including all odd orders 3–25 and the original even cases; replay /workspace/branches/a151a61d-dd0c-4695-a180-f57d69810054/independent_check.py. The frozen verify.py was inspected without execution. The finite replay tests sample the exact formula; they do not prove all orders.

## originality

PASS

The final finding is the exact odd-cycle metric invariant. It avoids the prior even case by a structural distinction (odd cycles are nonbipartite); affine independence and simplex combinatorics are credited, not claimed. No inspected exact statement supplies the odd-cycle radius.

## value

PASS

Odd cycles are the natural nonbipartite class of the Hamiltonian selection, not an arbitrary finite slice. The exact radius and all-facet tangency measure the roundness of that simplex family in its fixed canonical Euclidean metric; the coefficient of its n^−3/2 decay and the absolute inball scale are useful geometric data not supplied by its face type.

The dated certificate retains the supplied scientific assessment, sources and limitations.
