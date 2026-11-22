# Independent mathematical audit

## correctness

PASS

The actual RESULT.md at frozen Git blob e44a409d... was reconstructed: at most one coordinate can be negative, so the positive cube contributes 1 and n disjoint negative sectors each integrate to 1/n; the coordinate facets are P_(n-1) of volume 2 and a pair facet parametrization (t,-t), |t|<=1 has Jacobian sqrt(2), integrating 2sqrt(2)/(n-1). The cofactor area transform is det(D)||D^{-T}u||; two exact AM-GM steps minimize the determinant-normalized diagonal law, with equality only when all inverse scales agree. Exact c^4>8 and c^5<16 with c=1+1/sqrt(2) and monotonic 2^{1-1/n} prove n<=4 versus n>=5 without equality. The standalone checker uses scipy/Qhull n=2..5 only; additional independent symbolic/numeric n=2..15 tests agree and are not substituted for the proof.

## originality

PASS

Best-of-knowledge priority for exact geometry after object aliases and broader published findings are compared.

## value

PASS

A complete Euclidean boundary invariant of the natural complete-graph fractional stable-set polytope distinguishes the increasingly numerous pair facets from the fixed fraction of area borne by coordinate facets. The nontrivial diagonal-rigidity inequality and exact dimension-five isoperimetric reversal against an equal-volume cube are meaningful geometric consequences; not merely a known face count or volume calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
