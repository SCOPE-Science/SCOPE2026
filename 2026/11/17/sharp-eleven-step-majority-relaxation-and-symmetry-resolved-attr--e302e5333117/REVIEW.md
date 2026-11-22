# Independent mathematical audit

## correctness

PASS

For the specified LCF=[−12,7,−7]^8 simple cubic 24-vertex graph, the update rule is an exact 24-bit map using each of the three open neighbors and threshold two; the state domain has exactly 2^24=16,777,216 masks. The frozen C++ source constructs all successors, traces each functional-graph component to a recurrent cycle, and back-propagates first-entry depths. An independently written new C++ traversal (not a replay of saved logs) classified all 16,777,216 states: 550 fixed configurations, 63,715 primitive two-cycles, the listed 12-entry table and consensus basins 1,033,256 each. It confirmed F^13=F^11 for every state, and F^12≠F^10 at witness 152253, so 11 is sharp. Separate NetworkX group enumeration found exactly 32 automorphisms; applying all permutations to recurrent masks and identifying phase-exchanged two-cycle orbits yielded 39 and 2,415 spatial classes. Exhaustive finite proof is appropriate because the theorem explicitly concerns only this one finite state space; it is not an infinite-family extrapolation.

## originality

PASS

Existing universal Goles–Olivos symmetric threshold-network result proves eventual period≤2 but neither a uniform eleven-step bound nor specific McGee basin counts. Benjamini et al discuss general/random graphs; Turau proves tree-specific statements; other published cubic cage classifications have non-isomorphic vertex sets and dynamics. No prior exact McGee 24-bit census in Resultary search; a historical unindexed exact census remains a risk, and the 1980 full text could not be opened through lawful access.

## value

PASS

McGee is the canonical 24-vertex (3,7)-cage, so its exact majority transients, attractor basins and symmetry quotient form a natural finite classification. The sharp eleven-update maximum and its 320 extremal initial configurations, plus the global 39/2415 symmetry classification, are nontrivial intrinsic dynamical invariants, not arbitrary tiny parameter checks. Fully exhaustive finite computer-assisted mathematics is proportionate to the exact finite claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
