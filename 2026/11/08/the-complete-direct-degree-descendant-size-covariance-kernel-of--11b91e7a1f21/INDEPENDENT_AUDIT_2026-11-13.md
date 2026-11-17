# Independent mathematical audit

## correctness

PASS

Write D_i=sum_{t=i}^{n-1} B_(i,t), use conditional S_j(n)=(n/(t+1))S_j(t+1) when t>=j, and conditional parent location. The probability a fixed vertex i belongs to j-subtree is zero for i<j, one for i=j, and 1/j for i>j. This gives Cov(B_(i,t),S_j(n))=n[p_(ij)-1/j]/[t(t+1)] for t>=max(i,j). For t<j the future j-subtree is independent of that earlier parent choice. Telescoping yields exactly the claimed triangular matrix and zero boundary columns; sum over i is zero because total offspring n-1 is deterministic. Independently enumerated every parent sequence n=2..7 using exact fractions, checking every i,j.

## originality

PASS

Kuba–Panholzer (2006, 2007, 2009) derive descendant subtree marginal and joint descendant statistics and degree laws, but the inspected 2009 primary text treats random vector of descendant counts, not mixed immediate-child count D_i against descendant size S_j. Related Resultary theorems on sibling leaves, degrees and depths, or covariance of two subtree sizes involve different random variables; they do not imply this mixed kernel by direct specialization. Originality accepted with possibility that a general multivariate generating function could imply it.

## value

PASS

The complete exact two-index covariance matrix is a natural local-global dependence invariant of the foundational recursive-tree growth model, revealing uniform negative predecessor entries, a balanced positive diagonal and an orthogonal younger region. This information is not determined by marginal laws and can be used in second-moment analysis of mixed tree statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
