# Independent mathematical audit

## correctness

PASS

For a fixed nonzero rectangle U×V the two products with an arbitrary X are U×W and Z×V, with W the column support of rows V of X and Z the row support of columns U of X. The equality is either W=Z=∅ or W=V and Z=U. The first case leaves exactly X[Vᶜ,Uᶜ] unconstrained. In the second, entries in V×Vᶜ and Uᶜ×U are forbidden; rows U must hit columns U and columns V must be hit by rows V. Put A=U∩V, B=U\V and C=V\U. The constraints act on disjoint blocks A×A (both covers), B×U (row cover) and V×C (column cover), leaving the same free rectangle. Inclusion–exclusion, including H_0=1, gives the overlap factor. Choosing the intersection and then both disjoint differences gives the parameter multiplicities; equal numerical sizes are combined. The singleton count follows in either overlap case. At the complete relation, the first-order zero-line probability is 2n 2^(-n), with Bonferroni error bounded by the sum over pairs, each probability ≤2^(1−2n). Independent entrywise Boolean multiplication exhausts all partners and rectangles for n≤3, and all partners for the three a=b=2 overlap representatives at n=4, recovering 1312,160,128. Replay: python3 /workspace/checks/3.py; /workspace/checks/3.out. The frozen checker and its recorded output were inspected but not executed; its claimed Python 3.8 minimum is a minor documentation error (int.bit_count needs 3.10), not a mathematical defect. The fresh reproduction does not claim all 26 n=4 strata were replayed.

## originality

PASS

The supported distinct part is the exact overlap-dependent centralizer cardinality and full rank-one multiplicity census with arbitrary-rank partners. The rectangle representation, rectangle products and special all-ones support criterion are antecedents. The strongest inspected matches restrict the partner family, address graph distance, or change the ambient algebra. The comparison is bounded and no priority is inferred from same-day dates.

## value

PASS

Centralizer size is the degree count (with the relevant trivial vertices and self counted as commuting partners) in a natural commuting problem. A count across the entire nonzero rank-one stratum is useful even without a higher-rank classification. The formula resolves why overlap changes sizes at the same two support cardinalities, and quantifies nearly universal versus exponentially rare commutation within one rank stratum. It is neither a finite-table extrapolation nor a count only of rectangle-to-rectangle products.

The dated certificate retains the supplied scientific assessment, sources and limitations.
