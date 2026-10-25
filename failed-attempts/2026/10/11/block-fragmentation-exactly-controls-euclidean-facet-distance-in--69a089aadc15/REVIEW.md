# Independent mathematical audit

## correctness

PASS

For every m,n>=2 with N=m+n, Chapoton--Pilaud Proposition 3.19 fixes sum x_i=C(N+1,2) and Proposition 3.20 gives each actual facet support S=A union B with right side C(a+1,2)+sum_j C(b_j+1,2)+ab=C(s+1,2)-Gamma. At the uniform center c=(N+1)/2*1 the slack is s(N-s)/2+Gamma; its intrinsic projected normal has norm sqrt(s(N-s)/N), yielding delta=(1/2)sqrt(N s(N-s))+Gamma sqrt(N/(s(N-s))). Because s is nonempty proper and Gamma>=0, delta>=sqrt(N(N-1))/2, with equality iff s=1 or N-1 and Gamma=0 (equiv k<=1 for nonempty blocks). Every singleton Delta_{i} is a Minkowski summand in Proposition 3.21, so the valid x_i>=1 constraints give for any inscribed r-ball centered q: q_i-1>=r sqrt((N-1)/N); summing proves r<=sqrt(N(N-1))/2 and equality forces q=c. No assertion that every coordinate-subset inequality is a facet is required. Independently counted all simplex summands and support values for all 642 nontrivial subsets across (m,n)=(2,2),(2,3),(3,2),(3,3),(4,3),(3,4),(4,4), using exact rational distance squares, verifying Gamma identity, lower bound and equality cases. This finite check corroborates, rather than proves, the full parameter claim.

## originality

FAIL

The quantitative facet-shell law is a direct algebraic repackaging of the complete earlier facet description in Chapoton--Pilaud (2022 preprint, 2024 journal), Proposition 3.20: its right-hand side already equals C(s+1,2)-Gamma. Its Euclidean version follows by the standard projected-coordinate-normal length sqrt(s(N-s)/N). The inradius/unique-center conclusions then follow from the immediate elementary estimates s(N-s)>=N-1 and the singleton halfspaces supplied by Proposition 3.21. Moreover, the separately published same-date Resultary higher Hochschild shell theorem establishes the radius and unique incenter for the larger Hochschild polytope; Pilaud--Poliakova Remark 62 proves Mul(m,n) is contained in Hoch(m,n), and the Chapoton--Pilaud inequalities imply Perm(N) is contained in Mul(m,n). Thus those two metric conclusions also follow by the sandwich Perm(N) subset Mul subset Hoch. The same-date record has no established chronological priority here and is not the sole ground for rejection. The remaining Gamma term is exactly the binomial cross-term of the 2022 published facet constants, requiring only a routine normalization; it does not constitute an independent original theorem beyond that description. Searches did not identify a separately worded published distance law, but absence of that wording does not overcome the direct prior implication.

## value

PASS

The generalized multiplihedron is a natural two-parameter family interpolating permutahedral and associahedral structures. Its exact Euclidean facet-distance spectrum, all-radius optimum, unique center and fragmentation shell correction are meaningful intrinsic metrics of the specified realization across all m,n>=2. A mathematically motivated user of the family can use the explicit formula to identify which facets touch the canonical inball and how block splitting moves facets outward. The derivation is algebraically short and does not produce a new broad theory; this limits research depth, but an exact family-wide structural metric classification can have scholarly utility even when not independently original. Value does not compensate for failure of originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
