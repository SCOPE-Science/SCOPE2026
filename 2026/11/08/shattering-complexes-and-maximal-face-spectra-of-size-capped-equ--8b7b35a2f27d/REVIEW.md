# Independent mathematical audit

## correctness

PASS

For all n,r>=1, shattering pairwise same-block equality supports under partitions with blocks of size≤r is equivalent to a forest with all components size≤r: cycles force transitivity contradiction, and a larger positive component exceeds the cap; every forest labeling is realized by grouping positive-edge components. The labeled tree exponential formula yields the face polynomial. The union-find predictor merges at most n-ceil(n/r) times, matching a spanning-forest VC witness. A forest facet precisely forbids merging any two components, hence all component size pairs have sum>r. Sorting sizes gives minimum total t*(floor(r/2)+1) minus 1 if r even, and monotone increments fill every intermediate feasible n; resulting gap-free facet-size interval as stated, including r=1, r≥n. Independently checked n4 cap2, n5 cap3 traces, and all 120 n<=15,r<=8 maximal-component cardinality intervals.

## originality

PASS

IMPORTANT PRIOR COVERAGE: the October/November earlier refinement-closed partition theorem already states and proves the forest cap criterion and exact VC=Ldim as its explicit cap specialization. They are not original here. The remaining all-r complete labeled-tree face enumerator and especially parity-sensitive, gap-free inclusion-maximal facet-size spectrum are not supplied by either earlier refinement-closed result or exact-q-block graphic-matroid theorem. O PASS best knowledge only for this surviving composite contribution.

## value

PASS

The exact maximal-face spectrum is a natural simplicial-complex structural invariant not determined by the known rank/VC dimension. It classifies precisely how finite block-size caps destroy purity and yields linearly expanding gaps for fixed r≥3, and is not an arbitrary tiny parametric slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
