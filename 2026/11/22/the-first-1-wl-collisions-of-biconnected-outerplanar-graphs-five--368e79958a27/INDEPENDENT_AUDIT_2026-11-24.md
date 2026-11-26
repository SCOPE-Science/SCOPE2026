# Independent mathematical audit

## correctness

PASS

A biconnected outerplane embedding has a simple spanning boundary cycle. Any chord separates the two nonempty open boundary arcs, so a Hamiltonian cycle using the chord would require a single path between its endpoints covering both arcs without either endpoint in its interior, which is impossible. Thus the Hamiltonian cycle is unique; the isomorphisms in the cyclic labelling are exactly the dihedral relabellings preserving the chords. Conversely any noncrossing chord diagram with its polygon cycle is biconnected and outerplanar. Independent replay `python /workspace/replay/combinatorial.py outerplanar` generates diagrams by choosing the face incident with the root boundary edge and independently subdividing the intervals between consecutive face vertices; the unique incident face ensures completeness without duplication. It canonizes under the dihedral group and refines colors globally using exact neighbor histograms; a steady number of classes suffices because new keys contain the old color. Restricting to two components preserves key equalities round by round. For n=3..10 the raw counts are 1,3,11,45,197,903,4279,20793 and the orbit counts are 1,2,3,9,20,75,262,1117. The replay confirms no collision below 10, and 1107 singletons plus the five exact doubletons (0x8020,0x100040), (0x8028,0x100048), (0x108060,0x20100041), (0x108068,0x20100049), (0x128060,0x20120041), in agreement with the result and PAIRS.json. This is bounded to the stated orders and uniform-start unrooted 1-WL.

## originality

PASS

Credit Coste–Csikós–Viennot for the already documented existence of a 2-connected outerplanar collision. The supported distinct contribution is absence at all smaller orders together with the complete ten-vertex census and mask list, not the existence witness or the rooted classification theorem.

## value

PASS

The known root-dependent theorem and known unrooted witness motivate asking when the root first matters and what the full first obstruction set is. This threshold and the five precise colored-refinement doubletons are reusable as small tests for graph identification or structural analysis and are not merely another count of polygon dissections. The scope does not imply any result for larger orders or for automorphism-orbit recovery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
