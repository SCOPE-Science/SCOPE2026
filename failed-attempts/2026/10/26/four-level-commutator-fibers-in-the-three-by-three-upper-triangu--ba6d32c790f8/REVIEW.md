# Independent mathematical audit

## correctness

PASS

The frozen proof gives ranks 0, 2, and 4 on the stated dual strata: for nonzero central coefficient the 4-by-4 principal determinant is its fourth power, and alternation gives even rank even in characteristic two. Independently, put a=(a1-a2,b1-b2), g=(a2-a3,b2-b3), X=(A12,B12), Z=(A23,B23), W=(A13,B13). The three constraints are det(a,X)=s, det(g,Z)=t, det(a+g,W)+det(X,Z)=h. Counting as if there were q choices of W per X,Z gives q^3[q(q^2-1)+q^2 1_{s=0}][q(q^2-1)+q^2 1_{t=0}], including two free scalars. This is exact when a+g is nonzero. For g=-a with a nonzero, X=x a+s b and Z=z a-t b in a basis with det(a,b)=1; the determinant is -xt-sz. If (s,t) is nonzero the baseline remains exact; otherwise the correction per a before the two free scalars is q^4 1_{h=0}-q^3. When a=g=0, the same correction follows by counting determinants of X,Z according to whether X is zero. The total correction at s=t=0 is q^8 1_{h=0}-q^7, canceling the baseline cross term. The resulting positive and distinct levels, normalization q^12 and zero-fiber polynomial follow over every finite field. The frozen verify.py was inspected, not run: the literal products cover q=2,3 and the pairing-rank check additionally covers q=4, not all fields.

## originality

FAIL

An earlier distinct Resultary record states the entire same four-level distribution, surjectivity, and all-field scope for the additive commutator on all ordered pairs in the full triangular algebra, not merely a prior zero-fiber count.

## value

FAIL

Full nonzero commutator-fiber statistics on a natural low-dimensional algebra would be useful if distinct. Here the exact statistic, all four levels and scope already occur together; no separately stated new invariant or general method survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
