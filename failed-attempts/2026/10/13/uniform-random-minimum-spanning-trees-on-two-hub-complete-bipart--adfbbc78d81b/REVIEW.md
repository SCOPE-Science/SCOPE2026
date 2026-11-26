# Independent mathematical audit

## correctness

PASS

Every tree has exactly one double column and one edge per other column. Fixing the double column j, minimum weight is the sum of all column minima plus the maximum of column j. The maximum values are IID atomless, and swapping within each column shows the cheaper-edge labels are independent fair coins, independent of all maxima. Thus the minimum tree is indexed by a uniform j and n-1 fair bits. The marginal is 1/n+(1-1/n)/2. A same-column pair occurs iff that column is doubled; for distinct columns the joint probability is (2/n)/2+(1-2/n)/4, independent of which hubs are incident. Subtracting the squared marginal gives both stated covariances, strictly negative including n=2. An independent finite check counted linear extensions of the fundamental-path constraints per tree, not Kruskal outcomes per order. It verified all probabilities for n=2 through 5 and reproduced the nonuniform K_{3,3} boundary multiplicities 4200,4680,4800, attained by 36,36,9 trees, respectively. The unbounded result is analytic.

## originality

FAIL

Babson et al., arXiv:2407.20226v2, Appendix C.1, explicitly state that ordinary IID MST equals UST for a generalized theta graph if and only if its hub-to-hub paths all have the same length. K_{2,n} for n>=3 has n length-two paths, and n=2 is the classical cycle case. Their external probability formula also specializes directly to the displayed per-tree probability. The covariances and marginals are routine counts under that covered law.

## value

FAIL

The underlying equality-of-laws question is worthwhile, but the frozen record duplicates a documented equal-path theorem on a narrower family. The edge statistics and fixed K_{3,3} check are immediate counts or exact evaluations of an already available all-graph probability formula, not a distinct motivated contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
