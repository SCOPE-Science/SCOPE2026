# Independent mathematical audit

## correctness

PASS

An undominated cell is exactly the intersection of an empty row and an empty column. With m≤n the optimal size is m; optimizers are row transversals, together with column transversals exactly when m=n. The all-positive trace forces a support into one such transversal family, and each negative request in that family can be met by using a different cell in its queried row (or column), since m,n≥2. This proves both trace criteria. Counting the two families and their partial-permutation overlap gives the polynomials and VC dimension; extending within a family proves purity. The displayed row/column basis exchange fails for n≥3 because deleting (2,1) from column 1 still leaves (1,1) and another cell in column 1. The rectangular join is a wedge of (n−1)^m spheres of dimension m−1 by the suspension-smash description of joins. In the square case the intersection of the row and column joins is the chessboard complex; their homology vanishes below n−1, giving exactly the claimed reduced Mayer–Vietoris range. Jonsson's Theorem 3.1 supplies integral H2(M5,5)=Z/3 and Theorems 1.1 and 3 verify the degree bounds. The reduced Euler characteristic is 2104 and the top kernel is free. Jonsson's Theorem 2 applies at d=n−4 since (2n−4)/3≤n−4 precisely for n≥8, so the shift supplies the asserted lower-dimensional torsion and rules out pure shellability. A fresh direct closed-neighborhood/trace test exhausts 2×2, 2×3 and 3×3, and the size-five vector and Euler arithmetic were independently checked.

## originality

PASS

The dominating-set minimum and the chessboard torsion are known inputs. The distinct result is the trace classification for membership in minimum ordinary dominating sets, and the integral topology this gives for that specific shattering complex. The closest inspected rook shattering and dominance complexes have different defining predicates.

## value

PASS

The rectangular-to-square change in the optimizer families changes the topology of an intrinsically defined learning complex. It produces a natural, exactly described family of pure nonshellable shattering complexes with integral torsion and a simple rectangular control case. This is more than recomputing the known square optimizer count or rediscovering chessboard torsion on the original chessboard object.

The dated certificate retains the supplied scientific assessment, sources and limitations.
