# Independent mathematical audit

## correctness

PASS

The initial tricolored hub triangle is invariant under three-color rotation, while its absence leads to extinction in at most four steps by case analysis on initial hub state. With a persistent hub rotor, site t+7 depends only on the length-15 radius-seven light cone, so an exhaustive finite local comparison for all 3×3^15=43,046,721 rotor-phase/neighborhood pairs proves F^7=F^4 in every wheel size; independently compiled and ran the inspected C recurrence, and every comparison passed. Independent full-state wheel enumeration for n=3..7 reproduced the 3 and 4 entry bounds, E_n=3tr(S^n), and 3P_n=3(tr(T^n)-1). Transfer-matrix S counts cyclic words avoiding 12/21 after a hub relabeling, and T counts globally rotating rim words with fixed hub phase; the characteristic polynomials yield distinct positive Perron roots 1+sqrt(2) and ρ=2.205569... . No finite-size enumeration alone is used to extrapolate; the light-cone reduction proves uniform all-n recurrence.

## originality

PASS

The qualitative circulation/conservativity synchronization criterion is classical (Gravner–Lyu–Sivakoff) and not new. The wheel-specific exact extinction basin, primitive orbit transfer matrices, sharp first-entry count, and distinct asymptotic exponential rates go beyond that general theorem; related published SCOPE studies concern other graph families.

## value

PASS

For a natural infinite family of finite graph dynamical systems, the result gives complete exact basin and primitive-cycle counts and reveals sharply different rates for eventual recurrence and initial recurrence. The exhaustive finite light cone combined with symbolic transfer matrices is meaningful mathematical structure, not a bound inferred from simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
