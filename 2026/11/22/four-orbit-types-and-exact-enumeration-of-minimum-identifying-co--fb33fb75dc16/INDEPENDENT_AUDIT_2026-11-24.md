# Independent mathematical audit

## correctness

PASS

Under positive row and column degrees, equal same-row signatures require two column leaves at that row (and conversely); for cells differing in both coordinates, any common signature consists only of the two possible cross edges. Positivity forces both of those edges to be isolated if the signatures coincide. An empty row would force every other row to have degree at least two, as a degree-one row and the empty row would agree at its selected column. Thus an empty line costs at least 2(n-1)>3n/2 for n>=6, and the kP4 construction ensures a minimizer stays below that cost. For the remaining covered boards, a component other than the at-most-one K2 has at least four vertices and defect 4e-3v>=v-4, with a further multiple of four for cycle excess. The total defect is at least -2 and is divisible by four, proving the bound. At equality, either all components are P4 or a K2 uses defect -2 and the remaining trees spend exactly two units above the P4 sizes. The no-two-leaves condition reduces the possibilities to P6 or T6, or two oppositely oriented P5s, with all residual components P4; the criterion proves the converse. All graph automorphisms preserve or exchange the row/column clique families. In the shore-preserving group the path components of even order have trivial internal stabilizers, the odd paths have a size-two stabilizer each, and T6 has a size-two stabilizer but permits two shore orientations. Permuting equal P4 components provides the factorial divisors. This recovers every stated count, including the factor four for the two P5s and the cancellation of the T6 stabilizer by its two orientations. At k=3 the counts give 86,400, 518,400, 518,400 and 129,600. The supplied verification/verify_n6_direct.cpp, verification/verify_n6_structural.cpp and verification/verify_n4_boundary.py were inspected, not executed; VERIFICATION.md reports bounded runs, not a proof for every order.

## originality

PASS

The minimum size is established prior art, as are the no-isolated-edge equality case, the existence of optima with an isolated edge and the main line-graph viewpoint. The supported distinct claim is the complete even-order classification with the isolated-edge cases exhausted and their labeled counts and proportions. The inspected lower-bound proofs inform the equality analysis but do not contain that full implication without additional work. The closest distinct same-day ordinary-identifying record is about odd order. This is not a priority certification.

## value

PASS

The known optimum size does not describe the extremizers on this symmetric graph family. In contrast to the known single odd-order orbit, exactly four full orbits persist for every even order in scope. The defect analysis isolates precisely where the isolated selected edge changes the feasible shapes. Exact labeled counts then reveal that the class with two oppositely oriented P5s, not the familiar all-P4 construction, has limiting proportion one. This is a complete equality classification with quantitative consequences, not a restatement of the minimum size or an arbitrary small-board census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
