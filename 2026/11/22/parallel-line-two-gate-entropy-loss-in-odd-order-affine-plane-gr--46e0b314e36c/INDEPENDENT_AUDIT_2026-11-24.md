# Independent mathematical audit

## correctness

PASS

The crossing adjacency block is B with the omitted entries toggled over F₂. Directly, the reduced point density matrix has entry 2^(−q²) between bitstrings x,x′ exactly when their difference is in ker(B_Fᵀ); hence it is a sum of all-ones blocks on kernel cosets, with 2^rank equal nonzero eigenvalues. Odd order gives BBᵀ=I+J, whose kernel is span(1); Bᵀ1=1 rules out a nonzero left kernel of B. The sums in each parallel class of any Bᵀx are equal because each class partitions the points. In fact these q independent parity constraints define a q²-dimensional code, so they describe the whole row code. A nonzero word of weight at most two must thus have weight two on parallel lines. For at most two omitted entries, the rank-loss equation can realize that word only if the two omissions lie on those lines. The union indicator of the two parallel lines takes value 1 at the deleted endpoints and maps to this word, giving exactly one independent left-kernel vector by injectivity. Shared line or point endpoints cause no exception; no other placement can lose entropy. The count (q+1)·binom(q,2)·q² divided by binom(q²(q+1),2) is the stated probability. Independent column-rank replay for all one- and two-gate omissions at q=3,5,7 gives 108/630, 1500/11175 and 8232/76636 losing pairs.

## originality

PASS

The independent contribution retained is the exact odd-affine two-gate loss law and probability for graph states, not the graph-state cut-rank identity or the general theory of geometric codes. The strongest compared projective omission theorems do not state or imply the rectangular affine result under their hypotheses. A technically plausible odd-net code comparison remains limited by access; this is not a claim of new binary code theory or proven priority.

## value

PASS

This is a complete sharp fault-placement classification for a natural maximally entangled graph-state resource: one omission never reduces the cut entropy, and the minimal harmful two-omission geometry is completely identified. The exact uniform-pair loss frequency is an immediate, useful quantitative calibration of that geometric distinction; it is not a general graph-state rank identity or a table on isolated field orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
