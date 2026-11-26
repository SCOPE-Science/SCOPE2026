# Independent mathematical audit

## correctness

PASS

A pair in distinct rows and columns has exactly the other two rectangle corners as possible geodesic intermediates; a full selected rectangle is the only obstruction. Thus each unordered pair of rows may occur together in at most one column. If a column is full it consumes all three pairs and the others have sizes at most one. Without a full column, j distinct row pairs can be placed injectively in labelled columns, with empty/singleton choices elsewhere. These two disjoint cases give the face polynomial. A facet cannot have an empty column. With a full column, every other singleton is blocked from growing. Without a full column, zero or one pair leaves an augmentation (create a pair, or enlarge the unique pair to a triple). With exactly two pairs, a pair-to-triple addition duplicates the other pair, and a singleton is blocked precisely when it is in the common row of the two pairs. With three pairs, all augmentations of any nonempty column duplicate a used pair. These types give n·3^(n−1), 3n(n−1) and (n)₃·3^(n−3) facets respectively, of sizes n+2,n+2,n+3; the third type is absent at n=2. This establishes the unrestricted formulas and nonpurity exactly where claimed. An independent obstruction-mask check reproduced {4:12} facets at n=2 and {5:45,6:6} at n=3, with 334 faces at n=3. The frozen script was read, not run.

## originality

PASS

Pass is for the exact labelled face and facet enumerators and their counted support decomposition, not the C4-free encoding, the smaller facet size, or priority of the unweighted size spectrum. No inspected source determines the labelled counts. The Bryant–Fu full-text gap is real and keeps priority for the structural portion provisional.

## value

PASS

Three rows are the first width with distinct pair supports that interact. Their exact labelled occupancy and saturation distributions refine scalar maximum and minimum-size results; in particular they distinguish a large class of non-maximum maximal configurations from the largest facets and provide an exact test family for extremal and counting questions with more rows. The value is in the complete distributions, not rediscovery of their extrema.

The dated certificate retains the supplied scientific assessment, sources and limitations.
