# Review of minimum isolating configurations in \(\operatorname{KG}(n,2)\)

## Correctness — PASS

The two-selected-edge obstruction proves \(\iota\ge3\). The four permitted three-edge shapes each meet the closed-neighborhood isolation condition and the excluded \(P_4\) shape has an explicit adjacent undominated pair. Counting \(12\) labelled \(P_4\) paths per four-set gives the complete minimum-configuration number. Degree formulas subtract explicit forbidden moves from the ambient Johnson degree. For the global diameter assertion, a restricted-growth enumeration covers all equivalence patterns on twelve edge-endpoint slots. All 500,759 valid ordered pair-patterns admit a legal path of length at most three using only their combined edges; a disjoint pair witnesses three as necessary. A second direct adjacency-based program checks the numerical and graph claims through the stated finite sizes. The finite certificate is logically universal because every pair of three-edge states has no more than twelve endpoint positions.

## Originality — PASS, with residual historical uncertainty

Caro and Hansberg (arXiv:1504.08055, 2015) give the isolation parameter and explicitly the Petersen numerical value three; that value is prior art, not claimed new. Their inspected sections do not give all optimum configurations or a reconfiguration graph. Boyer and Goddard (arXiv:2401.03933, 2024) discuss existence of disjoint isolating sets and equality extremizers, neither of which implies the present count, the degree profile, or three-step mobility. Searches including the vertex-edge-domination alias, Kneser parameters, and a three-edge-path characterization did not reveal a statement subsuming the combined claim. Historical priority outside indexed literature is not established as impossible.

## Value — PASS

An exact full classification and count on a canonical infinite vertex-transitive family, plus the state-dependent degrees and universally sharp three-step reconfiguration, reveal information not contained in the previously known Petersen isolation number or general isolation bounds. In particular, the optimum-state graph is connected of diameter three yet fails to inherit Johnson shortest paths, a meaningful boundary for minimum-set relocation.

## Limitations

The global diameter proof rests on the provided completely enumerated twelve-endpoint certificate and benefits from independent code inspection. The independent Python checks by themselves are finite experiments. Nothing is asserted for Kneser parameters other than two-subsets or for token sliding. Historical indexing and prior-work accessibility are not exhaustive.

Self-review: passed. Independent audit: not yet performed.
