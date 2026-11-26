# Independent mathematical audit

## correctness

PASS

The selected set determines all labels: outside it a vertex is zero exactly when it has a selected neighbor. Minimality is equivalent to each selected vertex having a zero neighbor with no other selected neighbor; checking single decreases suffices because the Roman condition is upward closed. On a simple cycle a private zero is available on a side exactly when its gap has at least two positions. This applies also to one selected vertex, whose single gap has length n-1. Each gap carries precisely one selected vertex and max(g-2,0) ones. The short and long block weights give the stated 2-state matrix. Rooting at a distinguished selected vertex and choosing its labeled position gives n/k for k gaps even for periodic words. The trace-log determinant is D/(1-xz); its log derivative cancels the all-one term. Coefficient comparison yields the seeds and recurrence, and the unique simple smallest-modulus zero at y=z=1 produces leading coefficient one. Independent exhaustive enumeration of the 3^n words, testing the Roman condition and all single decreases, agreed coefficientwise for n=3 through 8 (totals 4,9,16,22,36,65). This complements, not replaces, the all-order proof. The reference to Proposition 10 for C5 is a bibliographic error: the result is Lemma 3 of arXiv:2204.04765, PDF p. 10.

## originality

FAIL

A distinct indexed weight-census record has the same labeled objects, the same legal cyclic words, and the exact same length-k trace contribution before it sums over k. Replacing its transition matrix M by yM multiplies its existing kth summand by y^k, since k there explicitly is the number of 2-labels. This immediately gives the frozen two-variable determinant and log derivative. The comparison shows present overlapping coverage and a mechanical implication, not which record was proved or written first. The numerical univariate counts already occur in Plouffe; the older Roman papers checked do not establish priority for the all-cycle interpretation.

## value

FAIL

The labeled-cycle classification would be useful in isolation. Against the exact existing gap census, however, the only claimed distinct increment is one factor per block whose number the existing formula already tracks. This does not supply an independently useful unknown census or a new structural ingredient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
