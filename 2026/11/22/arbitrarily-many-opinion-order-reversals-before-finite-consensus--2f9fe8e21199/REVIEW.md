# Independent mathematical audit

## correctness

PASS

Convexity keeps the diameter ≤3/4 so each forward gate of size 1 stays open. During the one-way phase W=(2I+P)/3 has nonconstant eigenvalues (3±i√3)/6, of angle ±π/6 and modulus 1/√3. Thus W⁶ acts by −1/27 on differences and W¹² by 1/729. Independently replayed the first twelve hypothetical steps by the integer recurrence z_i(t+1)=2z_i(t)+z_{i+1}(t) with denominator 4·3^(t+1): the minimum gap is 1/2916, with no ties. Factoring out 729^(−k) in each twelve-step block makes every gap through t=12m+11 exceed δ_m, so induction gives the actual cyclic phase through observation 12m+12, with every pair flipping in each of the disjoint six-step observation windows. Scaling the base trajectory about its initial mean 1/3 scales every gap and every reverse threshold together and leaves all forward gates open. A separate, exact gate-by-gate replay verifies the displayed scaled differences and all gate decisions through t=17 for m=0. The first complete graph is at time 16 with a nonzero remaining gap, and its update gives exact consensus at time 17. In units of δ_0, mean increments at t=13,14,15 are −2/27, 8/81 and 28/243; all other updates preserve the current mean. Their sum 34/243 gives consensus at 236213/708588. Scaling yields the claimed value and first time for every m. For two agents the difference multiplier is nonnegative even at τ=1/2 and simultaneous activation, so neither reversal nor reversal through a tie is possible.

## originality

PASS

Prior work defines the same fixed-step ordered-pair model, and the damped rotation of a directed circulant is standard. What is distinct on the checked evidence is the verified autonomous threshold schedule: at least 2m+2 consecutive-observation sign reversals per pair in a three-agent transient, followed by exact consensus with explicit time and value and a two-agent obstruction. The indexed rank-reversal and attracting-cycle results do not match that claim at the available statement level, and the same-date directed-cycle comparison cannot establish priority.

## value

PASS

The construction separates convergence from pre-consensus temporal ranking stability in the smallest possible population. Three agents suffice with strictly positive, time-independent confidence bounds, one fixed step, and common initial opinions across the family; every pair reverses repeatedly, but the actual gates enforce a finite, explicitly timed consensus. This quantifies a concrete limitation of reasoning about rankings from eventual agreement rather than merely observing the usual directed-cycle eigenoscillation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
