# Review of optimal proper conflict-free wheel recolouring

## Correctness — PASS

The hub-colour argument reduces every proper conflict-free wheel assignment to a singleton colour on the rim. In an optimal four-palette assignment, exactly one rim singleton exists for rim length at least five, and the remaining two colours alternate. For seven or more rim vertices each occurs at least three times, making every permissible attempted single-vertex recolour eliminate the only singleton. At lengths five and six, a complete local-move analysis yields degree two; an explicit fifteen-word cyclic orbit plus colour swap exhausts the length-five states, while the invariant of thrice-used colour and singleton parity yields the length-six six-cycles. The exceptional complete-graph and four-rim cases are handled separately. A direct graph-enumeration checker, without assuming this characterization, verifies every state, edge and component for rim orders three through eleven. These finite checks do not serve as an infinite proof.

## Originality — PASS (historical priority provisional)

Santra's Theorem 22 on universal-vertex proper conflict-free colourings and the basic hub singleton criterion are related prior art; the scalar chromatic number four is not claimed as new. Caro, Petruševski and Škrekovski give ordinary cycle PCF results. The complete wheel paper on forced partial four-colourings counts a different set of configurations under a distinct forcing rule, while the inspected cycle-prism and friendship PCF papers have different cores and no one-site wheel transition graph. Seven targeted published-finding corpus searches, the accessible current historical ledger and these full-source comparisons did not reveal an implication covering the sharp wheel component classification. Unindexed literature remains a residual risk; no independence or global uniqueness is asserted.

## Value — PASS

Exact optimal-state reconfiguration is a structurally motivated question beyond computing the palette minimum: the classification shows that two small wheel orders have every optimum mobile and all larger orders have every optimum frozen, with the exact number and lengths of every exceptional component. The result holds for an unbounded natural graph family and clarifies which local moves cannot navigate its optimum colorings.

Self-review: passed. Independent audit: not yet performed.
