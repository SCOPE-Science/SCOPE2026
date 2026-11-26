# Independent mathematical audit

## correctness

PASS

The original line 22 incorrectly uses a strict inequality for survival from sufficiently large initial biomass; the double-root case in its own theorem is a counterexample. The complete corrected RESULT.md uses ≤ there, retains strict < for the two-state regime, and explicitly gives survival at and above the semistable state at equality. Independently, G(x)−x has the sign of b−B_a(x), where B_a=((1+a²)x+2/x+1/x³)/a² is strictly convex, diverges at both ends, and has one minimum. At positive tangency, writing y=F_a(x), the derivative of G is 4/[(1+x²)(1+y²)]=1; put s=xy=4/(ab). Then x²+y²=3−s² and a−b=(y−x)(3+s)/s², which gives (a−b)²=(1−s)(3+s)³/s⁴ and H=0. For fixed a, H as a quadratic in b² has negative constant term and exactly one positive zero, hence its sign gives the three root regimes. The quartic discriminant also checks by substituting A=1+a², B=−ba² into 256A(A−1)²+(288A−32)B²−27B⁴ for Ax⁴+Bx³+2x²+1. Bounded, increasing G cannot cross a fixed point, so displacement signs determine all basins, including strict downward approach from above the double root and extinction below it. The odd-year limits follow by continuity of F_a. Substitution at fixed g gives H=(g²−4)(3g²+4)³−1024g² sinh² θ, so the repaired inclusive survival cutoff and exclusive two-state cutoff follow. The exact equal-product examples 132571 and −178229 check. The source checker was inspected, not executed.

## originality

PASS

The supported claim is the explicit symmetric contrast polynomial and its exact complete basins for this particular alternating sigmoid. The generic monotone-map argument and the homogeneous Allee threshold are standard and are not credited as new. No observed independent claim implies the exact contrast boundary; external same-family access limitations remain.

## value

PASS

The exact surface settles whether two environments with the same geometric mean can nonetheless lie on opposite sides of total extinction. The threshold and all initial-condition basins, including positive survival at equality, go beyond a qualitative fixed-point count and supply a usable benchmark for the standard saturating response.

The dated certificate retains the supplied scientific assessment, sources and limitations.
