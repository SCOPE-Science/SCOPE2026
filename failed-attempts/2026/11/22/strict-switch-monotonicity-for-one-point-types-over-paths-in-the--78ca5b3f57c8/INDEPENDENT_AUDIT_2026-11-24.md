# Independent mathematical audit

## correctness

PASS

A free homogeneous limit of the stated finite relational age realizes every compatible one-point extension over the named path, with infinitely many realizations by free amalgamation. Homogeneity and the finite language identify these with complete nonalgebraic types, one per allowed relation word. The only constraint on an occupied adjacent pair is (+,−) on a forward edge or (−,+) on a reverse edge. Thus each connected occupied block of length at least two has exactly one labeling if its edges alternate and none otherwise, with two choices per occupied singleton. Toggling one switch removes exactly one forbidden triple of occupied vertices without losing any support or weight; choosing that triple alone gives a strict increase, including at either end and for n=3. The frozen prefix/suffix calculation agrees: with forward old edges the gain is (L₋−L₊)R₋, where L₋−L₊ is a positive preceding-prefix count, and with reverse edges the signs swap. I checked the two transition matrices and their characteristic polynomials; in moving coordinates the alternating matrix is AJ (for a forward first edge and relabeling on the initial prefix, J fixes the all-ones vector). A and AJ have strictly positive squares via state 0; the initial and terminal vectors have nonzero positive Perron projections. This verifies the recurrences, initial values and ratio asymptotic.

## originality

FAIL

A distinct available Resultary record, 6db160410a0c, proves the exact conditional count for every support of an oriented named cycle in the same homogeneous graph, not merely a cycle extremum. Embed the n-vertex path as the n consecutive retained vertices of a cycle on n+1 vertices (n≥3), orient the retained edges as prescribed and the two extra edges arbitrarily, and restrict to supports not containing the omitted vertex. Equivalently the new point has no incident arc with that extra parameter. This gives exactly the allowed words of the original path, and preserves singletons and all internal forbidden triples. The cycle source's support-wise count therefore gives the path count with the same positive weight per support, and the path switch removes one forbidden triple. Taking that triple alone is a strict witness; the entire extremizer assertion follows. This conclusion does not use a logically invalid one-switch change around a fixed cycle: it compares two path orientations after restricting supports, independent of cycle closure at the added vertex. The two cubic recurrences then follow by standard three-state transfer and Cayley–Hamilton; they do not supply a separate substantive remainder. This is verified overlapping coverage, not a claim that the same-day cycle record has proven historical priority.

## value

FAIL

A local orientation monotonicity theorem for one-types is naturally motivated and would be worthwhile in isolation. Here the support-restricted cycle result gives exactly the useful information, even with degree grading. The remaining explicit all-zero/all-one transfer recurrences and numerical Perron rates are routine consequences of the local transition matrices, with no separate scientific need or application established for those constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
