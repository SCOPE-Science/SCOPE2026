# Independent mathematical audit

## correctness

PASS

For n >= 3, w >= 2 and u >= 1 the cyclic column determinant D = 1 + u(-w)^(n-1) is nonzero. For z = adj(C^T)1 and g = gcd(z_i), the primitive normal z/g has integral height D/g. Subtracting the last vertex from the other columns and using a lattice basis adapted to that normal gives |D| = |D/g| times the intrinsic normalized volume, not the ambient Euclidean volume. Solving C^T z = D1 gives z_1 = s = sum_{k=0}^{n-1}(-w)^k and z_2 - s = -(u-w)(-w)^(n-2). Since s is 1 modulo w, the gcd of just these first two coordinates is gcd(|s|, |u-w|). The integral recurrence makes every coordinate affine in u and equal to s at u=w, proving the reverse divisibility and covering u=w itself. The maximal value at u=w forces every positive period to be divisible by |s|; u=w+d realizes each divisor d and the coprime residues give the totient count. In the unimodular case, subtracting m times the last vertex from a lattice point of mP gives nonnegative integral coordinates in the edge basis summing to at most m, proving both the Ehrhart count and IDP.

## originality

PASS

The covered uniform specializations, known cycle matrix and standard consequences of unimodularity receive no separate novelty credit. The distinct supported result is the intrinsic volume law for a variable single defect and the resulting complete divisor stratification. None of the strongest inspected prior statements covers that law or supplies an arbitrary-weight volume classification that specializes to it.

## value

PASS

Intrinsic volume is a natural arithmetic invariant of an edge polytope. A single exceptional arrival weight can collapse the exponentially growing uniform volume to one, and the formula classifies every possible intermediate index, the least period, and all defects with unimodularity. This gives exact Ehrhart and IDP cases for the weighted-cycle family rather than just an isolated small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
