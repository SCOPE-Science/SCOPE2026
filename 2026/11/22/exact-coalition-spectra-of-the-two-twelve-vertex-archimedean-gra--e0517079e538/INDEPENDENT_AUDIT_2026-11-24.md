# Independent mathematical audit

## correctness

PASS

With no universal vertices, every block must be non-dominating and have at least one other block with dominating union; partners need not be exclusive. The missed-set characterization is exact by the intersection law for complements. I inspected the supplied enumerators and certificates, but did not execute uploaded code. The independent Python replay /workspace/checks/5.py orders blocks by (cardinality, mask), uses direct intersection with every closed neighborhood to test domination, and checks the entire partition traversal against the Stirling counts for every k. Each graph visits all 4,213,597 partitions; the independent coefficient vectors for k=2,...,8 are (24,10128,194733,582874,378855,47900,762) and (171,24846,258625,441384,153715,7422,93), with zeros elsewhere. Totals are 1215276 and 886256. Every winning partition agrees with the frozen list after vertex renumbering. Counting profiles in these complete lists gives (420,180,162) and (12,81) in the stated order. Independently extending partial adjacency-preserving bijections over all unused images gives the full automorphism groups of orders 48 and 24; their actions yield 23 and 7 orbits, agreeing on every orbit representative up to action, size and profile with the frozen JSON. Replay: python3 /workspace/checks/5.py cubo <frozen directory> and similarly trunc, logs in /workspace/checks/5-cubo.txt and 5-trunc.txt. The packaged shell marker alone does not check every archived coefficient or profile; the independent comparisons and exhaustive counts are decisive. The result is finite and does not imply an all-graphs theorem.

## originality

PASS

No distinct covering claim was established for the complete labelled spectra or the optimum orbit census. Compare the edge-coalition alias literally, and distinguish the strongest nearby results on the scalar maximum, a different graph family, or the same graph with a different invariant.

## value

PASS

These are the two canonical Archimedean graphs on twelve vertices, not two arbitrary graph samples. The full labelled invariant and symmetry classification distinguish their coalition combinatorics despite equal maximum eight, and provide a reproducible benchmark for cubic coalition and cube edge-coalition computations beyond a scalar lookup. The precise counts and profiles, not just reproducing a maximum, are useful finite data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
