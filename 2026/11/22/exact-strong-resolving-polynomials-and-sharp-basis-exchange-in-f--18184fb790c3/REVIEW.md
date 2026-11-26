# Independent mathematical audit

## correctness

PASS

The incidence axioms give distances 2 and 4 on each shore and 1 and 3 across shores. The distance-4 pairs are MMD; every shorter pair has a neighbor at a greater distance from its opposite end (for a nonincident point and line, use a different line through the point from the unique one meeting that line). A third vertex cannot strongly resolve an MMD pair, and every shortest path can be extended at its ends until the resulting end pair is MMD, showing why covering MMD pairs suffices. Omitted points must be pairwise collinear and hence on one line by the unique-collinear-point axiom; omitted lines obey the dual pencil criterion, independently. A subset of size at least two identifies its line or pencil uniquely. Counting empty, singleton and larger subsets gives the two polynomials; completing each shore yields every maximal omission, proving purity, dimension st(s+t+2) and N_P N_L bases. Exchange cost is half the symmetric difference, added over shores, giving costs s/s+1 and t/t+1 for the respective single-coordinate changes and at least s+t for simultaneous changes. Below max(s,t) a coordinate is fixed; at this budget the allowed single-coordinate moves yield the stated connected Cartesian factors. A point has s(t+1) collinear neighbors and s^2 t noncollinear others, so every point has collinearity-graph eccentricity 2 by the quadrangle axiom; dually every line has intersection-graph eccentricity 2. The complete factors have eccentricity 1. Additivity of product distances gives both the radius and diameter 4 or 3 for the two cases.

## originality

PASS

The general MMD vertex-cover criterion and the quadrangle axioms and distances are established inputs. The distinct claim is the full GQ-specific strong-resolving classification and polynomial coupled with the sharp exchange graph. Same-day and earlier catalogued analogues and ordinary GQ metric dimension were compared without treating a shared invariant name or date as equivalent coverage.

## value

PASS

An explicit geometric description of every strong resolving set is more useful than the minimum cardinality alone: it gives the full size distribution and shows all locally deletion-minimal sets are optimal. The sharp exchange budget and exact product distances determine how to reconfigure those optimal sets without increasing their size. This holds uniformly for thick quadrangles without symmetry assumptions, including unequal orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
