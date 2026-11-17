# Scientific review: small symmetric directed-forest quotients

## Correctness — PASS

The directed-forest definition and quotient are explicit, including the distinction between original face orbits and whole flags. `verify.py` exhaustively enumerates original directed forests, orbit flags and their signed incidence numbers for graph sizes two through five. Exact Smith normal forms have only unit nonzero factors and yield integral Betti vectors \((1)\), \((1,1)\), \((1,0,1)\), and \((1,0,0,2)\); independent signed Burnside–Lefschetz Euler sums agree. The full homotopy statement additionally uses the complete-source shellability theorem to establish simple connectivity of the original complexes for sizes four and five, Armstrong's theorem to establish trivial orbit-space \(\pi_1\), and Hurewicz–Whitehead to promote the integral homology calculations to sphere-wedge homotopy types. Boundary of claim: no sizes above five and no Borel quotient.

## Originality — PASS relative to checked evidence

Engström, *Complexes of Directed Trees and Independence Complexes* (arXiv:math/0508148), introduces the same directed-forest construction but does not establish its ordinary full symmetric geometric quotient. Jojić, *Shellability of Complexes of Directed Trees* (arXiv:1109.4475), treats precisely the labeled complete bidirected graph and obtains its shelling and sphere decomposition, but the examined statements do not identify quotient flag incidence or integral quotient homotopy. Other indexed directed-forest and multipath results concern Cayley graphs, tournaments, or degree-constrained directed paths, not this object and action. An inaccessible later Cayley-graph thesis and possible unindexed treatments are explicit residual priority risks; absence of search hits is not proof of novelty.

## Value — PASS

The complete smallest-size classification isolates a natural first branching of the *unlabeled* directed-forest topology: the full symmetric quotient advances from a circle to a two-sphere and then to **two**, rather than one, independent three-sphere summands. This is not a relabeling of the well-known labeled-complex sphere count: for five vertices the labeled complex has 256 three-sphere generators but the quotient has two and its fundamental group is trivial. The precise ordinary quotient and integer homotopy type provide a grounded test case for the study of symmetries of combinatorial forest complexes, without claiming a general formula.

## Risks and limitations

The finite classification is complete only for sizes two through five. A stable family statement, integral equivariant homology decomposition, and independent external audit are not established. Direct full-text access to the 2020 Cayley-graph thesis was unsuccessful, although its accessible abstract does not state the current quotient conclusion. Priority remains provisional with respect to work not indexed by the checked sources.

Self-review: passed. Independent audit: not yet performed.
