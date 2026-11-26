# Independent mathematical audit

## correctness

PASS

Gessel's congruence identifies the positive input residues exactly as ternary digit sums 1 and 2. Carrying and discarding a top carry cannot raise digit sum. Targets of weights 2 through 4 are obtained by partitioning their digit units into two nonempty groups of size at most two. The top-position sums in the proof supply weight 0 and every weight 1, including r=1. The ordered-pair transitions on the two input digit weights and incoming carry follow from a_i+b_i+c_i=t_i+3c_{i+1}; both outgoing carries count, but either zero input weight is rejected. My separate exact check /workspace/branches/reproduce_5.py folds partial weights by exchange symmetry, reconstructs 18 reachable states, verifies the annihilator T^2(T-3I)(T-I)^5 on every basis row and checks the full initial histograms plus direct sums for r=1..9. The eight initial values and recurrence prove the histograms for all depths since the formulas at r>=2 are degree-at-most-four polynomials plus the 3^r term, and the two early exceptions are killed by the squared shift. Summing j^2H_j gives the displayed energy, with r=1 checked separately. I inspected the supplied certificate and four-input check without executing them.

## originality

PASS

The exact cyclic ordered histogram and energy for this specific ternary weight-one-or-two index set are distinct in the inspected evidence. The closest catalog analogue changes the set and carry language, not just the names; graph congruences supply membership, and general energy estimates do not give the exact distribution.

## value

PASS

This arithmetic index set is natural before enumeration, and ordered cyclic collisions are a genuine invariant of it. The precise uniform cap, full distribution and energy distinguish ordinary partition counts from carry-induced collisions and provide an exact benchmark for higher digit-weight carry problems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
