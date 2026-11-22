# Independent mathematical audit

## correctness

PASS

For a graded source-sink DAG with L>=2, new arc s->t is traversable in no longer directed walk because s has no in-arcs and t no out-arcs. Hence only metric d(s,t) changes, L to 1; magnitude chain complexes at all other ordered endpoints remain unchanged. At endpoint (s,t), k>=2 chains have length L and identify with simplices of open reachability interval P, where differential at k>=3 is the ordinary simplicial boundary; k=2 boundary to (s,t) vanishes after shortcut, producing unaugmented C_*(Delta(P)) shifted by 2. Before shortcut, (s,t) in length L gives augmented complex. Since P nonempty, H0(Delta(P))=reduced H0 ⊕ Z abstractly (including disconnected P) and all positive homology agrees. The new (s,t) at length1 contributes a Z at (1,1). No other bigraded integral group differs; at L=2 both new summands are diagonal and all height-two graded open intervals are discrete, while L>=3 supplies nonzero off-diagonal (2,L). Source checker enumerates full directed distances and boundary matrices over F2,F3, but does not certify integral torsion: integral proof is the actual chain-level identification.

## originality

PASS

The general degree-two magnitude-homology theorem already entails the isolated (2,L) generator, but the assigned all-(k,l), integral two-bidegree perturbation/invariance under a new transitive arc was not found as a prior theorem. Its novelty is the exact change map for all endpoint groups, not the known static degree-two formula.

## value

PASS

An exact integral edge-surgery formula on arbitrary graded st-DAGs is a reusable structural fact: one reachability-preserving shortcut changes only two groups for every k,l, and produces unbounded off-diagonal degree length while holding all others fixed. Separates combinatorial reachability from directed metric magnitude homology and works without torsion-freeness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
