# Independent mathematical audit

## correctness

PASS

For each s_i, if exactly one side is a descent the two products have different lengths. If both are descents the two products are w. If neither is a descent, equality means w conjugates s_i to itself, hence preserves its support pair, necessarily fixing both entries (a swap would be a descent). This criterion is invariant under inversion. A central w with w(1)=1 must fix successive entries; otherwise let j=w(1)>1. If j<n, then w⁻¹(j)=1<w⁻¹(j+1), so the criterion would force w(j)=j, impossible. Inversion then gives w(n)=1. The two new boundary indices are double descents, so restriction and extension give an exact recurrence on the middle block down to size 0 or 1. For k<m the first ascending comparator sweep of the reduced endpoint-transposition word pushes the minimum of the increasing middle block to its end without crossing its descending boundary. The return sweep places its maximum at the start, also without crossing a boundary; the omitted final comparator of index n−1 is not needed (the penultimate endpoint in a full-length first sweep has already been disposed of, and for k≥1 this index is in or at the end block). This includes middle lengths 2 and 3; the identity case is simply evaluation of the reduced word for (1 n). The longest element absorbs on both sides. Associativity gives truncated addition and only the two endpoint idempotents for n≥2; n=1 is trivial. Independently enumerated permutations through n=7 and tested every central product using reduced words from sequential inversion deletions, at /workspace/checks/hecke.py and hecke.txt. The proof, rather than that finite test, covers arbitrary n.

## originality

PASS

Pass is for the exhaustive classification of individual central elements of the type-A monoid and the resulting identification of its center, not the general Demazure product laws or the vector-space center. Same-type catalogue results for adjacent generators, idempotents and length thresholds do not state the intersection/classification at issue. Primary-text access leaves a specific unresolved possibility that algebra-center support descriptions make the classification implicit; the available results do not show this.

## value

PASS

The center of these standard finite monoids is a natural structural invariant, distinct from the associated algebra center and the idempotent commutation problem. The all-degree exclusion of every permutation except the nested reversals and the identification of their growing absorbing power chain give concrete uniform data about central, usually nonidempotent elements. This is a complete infinite-family classification, not a finite count or a new claim of general parabolic multiplication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
