# Independent mathematical audit

## correctness

PASS

The Desargues graph is H(5,2)=GP(10,3), bipartite incidence graph between 2- and 3-subsets of a five-element set. Actual frozen verify_desargues.py reconstructs all distances, checks independent 2^20 face enumeration at r2/r3, exact deterministic Morse pairings and complete directed Hasse topological-sort acyclicity, with mod2 homology crosscheck. At r2 the 260 nonempty faces have f-vector (20,90,120,30) and acyclic matching leaves one vertex and 19 critical 2-cells, proving wedge^19 S2; at r3 the 3200 faces have f-vector (20,150,540,1000,960,450,80) and leave one vertex plus one 3-cell, proving S3. At r1 a graph with 30 edges,20 vertices gives wedge^11 S1; at r4 the only missing distance-pairs are 10 antipodal disjoint pairs, so the complex is join of ten S0 = S9; r5 full simplex. Fresh independent BFS verified distance multiplicities (30,60,60,30,10), both exceptional f-vectors and reduced Euler, not merely log. Every stage carries homology in a distinct degree, so integral barcode consists of nineteen [0,1) deg0, eleven [1,2) deg1, nineteen [2,3) deg2, one [3,4) deg3 and one [4,5) deg9. No assertion of general graph family.

## originality

FAIL

Earlier 2026-11-01 published Resultary full RESULT.md *Integral Vietoris–Rips persistence of the Desargues graph* explicitly gives precisely the SAME inclusive 20-vertex graph-metric VR filtration and COMPLETE integral barcode, including wedge^19 S2, S3, S9 at radii 2,3,4. It identifies G=GP(10,3)=Desargues Levi=H(5,2), so current 2/3-subsets model is just a relabeling. The earlier proof reconstructs both full face vectors, discrete Morse certificates and antipodal pair join. This exact same-object earlier published claim logically subsumes all present conclusions, not merely one threshold or a weaker field computation.

## value

PASS

The complete integral graph-metric Rips persistence of a natural Desargues incidence graph is mathematically useful and a nontrivial exact finite classification, with striking changes of homotopy dimension; nevertheless its entire final statement is already published and originality necessarily fails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
