# Independent mathematical audit

## correctness

PASS

The cubic complement bijection counts labelled undirected edge subsets exactly once. If a perfect matching has rungs, each unmatched rim run is an even path and has the same unique matching on both rims. With no rungs the only extra cases are the two opposite phases for even n, whose complements each follow a connected zigzag around the base. For a nonempty base matching of size k, deleting its edges partitions the base into k paths; the complement closes each doubled path into one cycle using its two endpoint rungs. The empty base matching gives two rims. Counting marked cyclic gaps gives k m_{n,k} = n binom(n-k-1,k-1) for k>0. The quotient by z has positive coefficients and, if real-rooted, all its roots would be negative. Newton applied to the coefficient triple at degrees 0,1,2 gives (d-1)b^2 >= 2dac. Both displayed parity factorizations of the opposite defect are positive for m>=4; the explicit factorizations for n=3 through 7 (quadratic discriminant 29 at n=7) give the other direction. There is always a zero at 0; for n>=8 the claim is existence of nonreal zeros, not absence of real ones. An independent bounded check, `python3 /workspace/branches/frozen_review_checks.py` (section 5, passes), exhausts the edge subsets that can be perfect matchings for n=3..7, counts complement components by disjoint sets, and recovers both Newton factors symbolically. The proof supplies all orders; the supplied checker was inspected, not executed.

## originality

PASS

Best-of-knowledge pass for the full complement-cycle refinement together with the uniform real-zero boundary. The same-graph total matching count and the connected-factor coefficient are credited prior coverage; the available statements do not determine the distribution or the threshold. The strongest same-graph older paper remains only partially accessible, not ruled out in full.

## value

PASS

Spanning two-factors are a natural prism invariant beyond the total and Hamiltonian coefficient. The distribution is uniformly exact and supplies a sharp, all-order change in zero geometry, contrasting with the unmodified cycle matching enumerator. The first-three-coefficient obstruction explains the boundary without fitting a finite table and is potentially useful for comparing nearby component polynomials.

The dated certificate retains the supplied scientific assessment, sources and limitations.
