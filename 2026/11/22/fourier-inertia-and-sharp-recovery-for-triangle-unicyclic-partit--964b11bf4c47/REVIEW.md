# Independent mathematical audit

## correctness

PASS

Reviewed the unnormalized edge-coordinate count with multiplicities, not a probability kernel or full-pair transform. Expanding each edge sign and contracting the imposed co-block edges counts B_{c(F)}; precisely the subsets containing the triangle gain one extra component relative to a forest. This proves the sector formula and independence of all attachments. The Poisson moment U(n,k) has terminal value at k=n-1 given by Poisson size bias, namely the positive number of singleton-free partitions; the adjacent difference is twice the previous-row entry. In the triangle sector the moment factor is Q(X)=X(X^2-6X+4), and adjacent differences likewise come from the previous row. In the boundary moment for s>=6, the m=0,2 terms vanish; after removing the common e^-1, the positive m=6 contribution 4^s/30 dominates the absolute bound 1+5/2+2^(s+1)/3+3^s/24 from m=1,3,4,5, since the normalized bound is strictly decreasing and holds at s=6. The positive s=7 row has a unique last minimum even though it is not monotone; subsequent rows are strictly decreasing by the difference identity. Subtracting the triangle boundary from the minimum forest value gives 2U(s+2,s)>0 (including s=0 by U(2,0)=2). Thus the full edge character is uniquely smallest at n>=10; B_n is the largest absolute multiplier by the triangle inequality. The finite rows and their binomial multiplicities give all exceptional negative indices and gaps, with no zeros. Independent replay `python3 /workspace/review_replay.py 1` enumerated partitions by least-vertex blocks for two attachment constructions through n=10, recovered the seven negative-index/gap pairs and the n=10 minimum 1347, and checked the exact domination base inequality. The analytic proof, not that replay, certifies all orders.

## originality

PASS

The exact expansion is prior and the boundary numbers are expressible via a prior sequence. The surviving distinct contribution is the all-order inertia, sharp transition and exact unique minimum in the triangle-unicyclic class, not the spectral expansion or shifted Bell moments in isolation.

## value

PASS

This is the first cyclic dependency type beyond forest co-block profiles. Across a natural infinite family, the result distinguishes invertibility from positive definiteness, locates the exact transition at ten vertices, and identifies the unique worst-recovered mode and exact stability constant at every larger order. These sign and ordering facts are not supplied by the known coefficient formula or by computing a small table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
