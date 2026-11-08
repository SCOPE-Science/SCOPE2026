# Self-review: exact logistic transition-edge census

## Correctness — PASS

The single theorem in `RESULT.md` concerns the positive-Lebesgue-measure directed one-step support graph of \(F(x)=4x(1-x)\) on \(m\ge2\) equal amplitude bins. The key all-resolution identity is \(m\mid4j^2\) if and only if \(R_m\mid j\), which follows from the prime valuations of \(m/\gcd(m,4)\). The proof counts unaligned interior image-boundaries separately on the two monotonic branches, and it handles the critical-point-spanning cell for odd \(m\) explicitly. The extremal inequality follows from \(R_m\ge\sqrt{m/\gcd(m,4)}\), with equality at \(m=4k^2\). The trajectory assertion is a standard consequence of the explicit doubling-map semiconjugacy and ergodicity; it excludes all grid-boundary orbit events on a null set.

An independent integer-numerator enumeration in `verify_edges.py` checked every resolution \(2\le m\le512\) and 100 exact square-family cases. It is evidence that the implementation and endpoint conventions agree with the proof, not an infinite proof. No unproved numerical extrapolation is used.

## Originality — PASS (provisional historical priority)

The 2026 motivating work by Balaji and collaborators constructs logistic amplitude-transition networks and examines centralities, degrees, entropy, and bifurcation signatures; the available abstract and deposited MATLAB source code were read. They do not state the all-integer-resolution number-theoretic edge census in the inspected material. The preprint's full text was inaccessible, so comparison with its uninspected pages remains an explicit residual risk.

The most directly relevant historical source is Kyriakopoulos and Thurner's 2007 *Directed Network Representation of Discrete Dynamical Maps*. Its accessible Method, logistic-map results, and Discussion were inspected. It defines a directed equal-bin graph and finds mean degree near three at the fully chaotic parameter, but does not give a divisibility-corrected exact support count for all integer resolutions. Its four-cell printed endpoint-inclusive matrix has ten entries; the present positive-measure convention has eight. Neither the older numerical mean-degree observation nor a general bin-by-bin adjacency construction implies the displayed closed prime-factor formula or sharp square-resolution correction as a previously proved result. The natural relationship to previous state-transition network theory is disclosed, not claimed as new.

Relevant mathematical-record searches (including exact arithmetic edge counts and alias formulations) and comparisons with accessible historical claims did not find an equivalent or stronger covering statement. Absence from a database is not a novelty proof, and the outstanding full-text limitation remains.

## Mathematical value — PASS

The number of active directed edges is a natural network invariant underlying degree and connectivity statistics for the equal-amplitude discretizations used in current work. Unlike an arbitrary isolated numerical statistic, its all-resolution formula makes the finite-size error in the observed mean degree exactly computable. The correction is not a generic rounding constant: it is controlled by the least integer square-root multiple of a normalized resolution and reaches sharp order \(\sqrt m\) on infinitely many grids. The almost-sure realization theorem connects the continuum graph to empirically observable long trajectories for typical initial data, while separating those from exceptional critical-point orbits. These supply a structural, reusable baseline beyond the old approximate mean-degree plot.

## Closest literature and limitations

Balaji et al., arXiv:2608.20956 (2026), with MATLAB code DOI:10.5281/zenodo.22114165; Kyriakopoulos and Thurner, DOI:10.1007/978-3-540-72586-2_91 (2007); and general state-transition network methods in *Entropy* 23, 103 (2021). The full motivating preprint was not available to read; this qualification prevents an unconditional historical-priority assertion. The result excludes other logistic parameters, endpoint-only contacts, finite-precision time series, and weighted edges. No independent scientific audit is asserted.

Self-review: passed. Independent audit: not yet performed.
