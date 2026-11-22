# Scientific review: sharp uniform-hypergraph recolouring diameter

## Correctness — PASS

Proper weak hypergraph colourings of the complete \(r\)-uniform graph coincide with colour occupancies at most \(q=r-1\). A no-direct-move sink strongly connected component in the unsettled transfer multigraph cannot be a singleton: all incoming target classes would violate capacity. Summing the occupancy inequalities proves the nontrivial component is isolated and balanced. An Eulerian rotation uses one temporary unused colour, settles every associated token, and permanently completes at least two saturated classes. Disjoint charging yields at most \(\lfloor n/(2q)\rfloor\) temporary moves. The two-full-colour-block construction supplies that many forced non-target moves in every path. Small exhaustive breadth-first searches and independent constructive route testing agree with the formula. The unrestricted conclusion rests on the proof rather than the tests.

## Originality — PASS, qualified priority

The primary hypergraph result in arXiv:2611.17022v1, Section 7, Lemma 15, provides only bounds \(n\le\operatorname{diam}\le2n-1\), and its Question 18 explicitly asks for stable diameters and stability thresholds. The full manuscript was inspected at the hypergraph section and question. The full arXiv:2412.19695v1 was inspected at the optimal-renaming lemma; it bounds recolouring with fixed colour-class partition and does not assert the all-pairs formula for complete \(r\)-uniform hypergraphs when \(r\ge3\). Related published-claim searches and accessible earlier claims did not identify a dominating theorem. The complete-graph case \(r=2\) and prior renaming technique are acknowledged. Priority risk persists for unindexed occupancy-reconfiguration formulations, so novelty is a best-knowledge claim and independent historical review remains open.

## Value — PASS

The exact stable diameter is a natural invariant explicitly singled out in the 2026 hypergraph reconfiguration problem. It classifies a uniform hypergraph family for every size and rank, establishes a sharp capacity-controlled transition in the number of compulsory buffer moves, and improves a general coarse interval to equality. It leaves the least stability threshold as a distinct future problem.

## Scientific limitations

The theorem requires at least \(n+1\) named colours and weak properness; no formula is asserted for smaller palettes. Finite checks cannot certify its all-parameter proof. Historical uniqueness and independent audit have not been established.

Self-review: passed. Independent audit: not yet performed.
