# Independent mathematical audit

## correctness

PASS

Reconstructed the Franklin graph from the specified cycle and chords, and independently enumerated the paired dominating sets with an exact perfect-matching predicate. Domination is the union of closed neighborhoods. Recursing by the least remaining vertex and each possible partner exhausts perfect matchings, so the finite tests cover the whole predicate. Sizes 0,2,4 give no optima; complete six-set enumeration gives 184. Every one of 33,672 distinct ordered pairs has a target-improving exchange; induction gives the Johnson upper bound and each exchange changes overlap by at most one, giving the lower bound. Independent all-source BFS agrees including zero distances. The exhaustive results are 984 edges; degrees {10:120,12:64}; distances 1–6 with counts 984,3900,6640,4512,768,32; eccentricities {4:24,5:96,6:64}. Connected bipartiteness forces each automorphism to preserve or swap shores; distinct neighbor signatures on each shore make enumeration from one shore complete, giving group order 48 and orbit sizes 8,8,12,12,24,24,48,48. In the stated witness, adding 1 after removing 2 violates shore balance; adding 6 leaves both 0 and 6 with only the neighbor 11 in the selected opposite shore, violating Hall's condition. The two original sets are dominating and have matching witnesses (0,11),(2,3),(10,9) and (0,1),(6,11),(10,9), respectively. Frozen artifacts were inspected, not run.

## originality

PASS

The Franklin minimum size is already a published exact value; the independently supported distinctive claim is its optimum family, complete exchange metric and non-matroid witness. The strongest inspected same-object census and the structurally closest isometry results do not determine these facts.

## value

PASS

Franklin is distinguished before enumeration as the order-twelve cubic bipartite equality graph; its optima furnish a constrained natural example separating Johnson isometry from the matroid-basis axiom. The exact metric and explicit obstruction are independently useful for comparing exchange models, rather than merely re-counting the known minimum size. The census makes the example replayable and quantifies its path geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
