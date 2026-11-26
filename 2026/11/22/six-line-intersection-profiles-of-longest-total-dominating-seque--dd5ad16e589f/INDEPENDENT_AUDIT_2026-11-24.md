# Independent mathematical audit

## correctness

PASS

Reconstructed the last-point recurrence: a predecessor contributes exactly when its covered-line mask strictly increases with the last point, and the last point partitions the legal orders. An independently written forward recurrence over every mask, with incidence constructed over F4, reproduced 738840 reachable masks, maximum length 10, 140448 maximum supports, 36288000000 orders, coverage of all lines, and all six profile multiplicities. Any incomplete legal sequence admits a point on an uncovered line as an extension, so a maximum is complete. For a separate upper bound, the incidence entry over F4 is 1+(a dot p)^3; the cubic factors as (a dot p)(a dot p)^2, giving nine rank-one terms plus the constant and hence rank at most ten. Fresh-line witnesses form a unit triangular submatrix, bounding legal length by that rank. Dot-product duality and disjoint target shores justify squaring the support count and multiplying squared order counts by C(20,10). Four vertices cannot cover 21 opposite-side vertices; five points on a line and, dually, five lines through a point attain the ordinary minimum on their shores. These are exact results for the specified plane, not for every order.

## originality

PASS

The finite census of legal maximum supports, orders and intersection types is the distinct content on available evidence. Neither ordinary total domination nor the general incidence-graph conversion is credited as new. Even a rank bound and an exact maximum would not determine the census.

## value

PASS

The canonical order-four plane is a natural small test case where the gap between domination and legal sequential domination and the structure of extremizers can both be resolved exactly. The profile census distinguishes maximum supports containing a line from genuinely nontrivial blocking sets and supplies exact support and order benchmarks for future covering and configuration work. These quantities are not obtained from the rank bound or the domination identity alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
