# Independent mathematical audit

## correctness

PASS

Ordinary nonempty spheres are exactly radius-zero singleton sets and sibling shells (union of all children except the center child) at positive internal-node radius. For support {x,y}, singletons give traces and a containing shell exists except when LCA is binary root and pair crosses root children; s2=C(N,2)-1_{binary root} n1 n2. A shattered triple must be equilateral and choose three child branches at node v; containing/empty shells exist iff v is nonroot or root has >=4 children, giving s3=sum nonroot E3(v)+1_{root >=4}E3(root). Any four-support would need all triples equilateral, but a sibling shell cannot select exactly two of four distinct equal-distance branches, so s>=4=0. Covers N=1 and N=2 edge cases; full-b-ary formulas follow counting nodes. Fresh independent distance-sphere computations on nine hierarchies up to eight leaves matched pair, triple and four-support counts. Source verifier was inspected; its claimed all-405-shape computation was not rerun.

## originality

PASS

PASS qualified: Ordinary exact-distance spheres exclude the center when r>0, unlike centered spheres in existing ultrametric tree representation work; ball range systems are laminar and not equivalent to the sibling-shell family. No independently inspected prior claim provides the full degree-three shattering polynomial across arbitrary finite reduced ball hierarchies.

## value

PASS

A natural canonical metric range family receives a complete exact support enumeration depending only on the reduced rooted hierarchy, including root-versus-nonroot branching phase differences and all edge cases. The formula is directly usable for statistical learning/sample-compression comparisons without knowing numerical distance labels.

The dated certificate retains the supplied scientific assessment, sources and limitations.
