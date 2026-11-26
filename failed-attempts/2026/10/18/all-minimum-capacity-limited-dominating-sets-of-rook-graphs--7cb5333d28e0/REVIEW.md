# Independent mathematical audit

## correctness

PASS

For selected (i,j), outside degree is n+m-r_i-c_j, and domination is exactly full coverage in at least one orientation. Put p=max(1,n-k), u=max(1,m-k). The row-cover and column-cover bounds are mp and nu respectively, both attained by complete slabs in the corresponding orientations. At the smaller bound only its winning orientation(s) can occur; equality forces r_i=p in the row-cover orientation, and then every occupied column satisfies c_j>=m+n-k-p, which is also sufficient. If p=n-k>=1, each occupied column is full; if p=1, these are exactly maps from rows to columns with the stated lower fibre threshold. The column orientation is symmetric. This reproduces all regimes, including the strict rectangular large-k inequality m<n, the intermediate tie (one per column and full-column slabs cannot intersect), square k=q-1 (a single full row or column) and k>=2q-2 (permutations are the overlap). The factorial-weighted product counts all labelled assignments without quotienting. Phi is defined on positive integer arguments and can be zero for general t>b; this does not affect any claim about the minimum sets. The frozen exhaustive script, verification notes and output were read, not executed; the proof handles unbounded sizes and capacities.

## originality

FAIL

The previously proved all-parameter occupancy inequalities and minimum formula mechanically imply the full optimizer classification, including the allegedly new transition and restricted fibres. This is a stronger objection than noting overlap in the minimum, low-capacity cases, or two-row special case. Explicit all-regime wording need not have appeared before for the claim to be covered in this sense.

## value

FAIL

The labelled optimizer count is a natural quantity, but here the additional regimes only unpack known sharp occupancy bounds by equality and use standard labelled-fibre extraction. Transition, tie, and high-capacity shapes all follow from those same published equations without a new invariant, nonroutine counting argument, or additional structure. The complete presentation may be convenient, but no independent scientific remainder to repair was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
