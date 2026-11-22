# Independent mathematical audit

## correctness

PASS

For n≥4 and 2≤k≤n−2, H_{n,k} is a dimension-(n−1) Euclidean slice [0,1]^n∩{sum x=k}; V_{n−3} is the codimension-two Steiner intrinsic volume, not the facet area. Each ridge fixes two coordinates s,t∈{0,1}, with dimension n−3 only if 1≤k−s−t≤n−3. Each such ridge is a hypersimplex in n−2 coordinates with measure sqrt(n−2) E_{n−3,k−s−t−1}/(n−3)!; equal-coordinate normals have exterior angle acos(−1/(n−1)), mixed have acos(1/(n−1)). Inserting two equal and two mixed ridge types per coordinate pair with normal cone fraction angle/(2π) proves the exact Eulerian formula, with boundary Eulerian coefficients zero. Eulerian/Irwin–Hall correspondence expresses the ratio as α/β times [g_M(x+1)+g_M(x−1)]/[2g_M(x)] for M=n−2 and x=k−n/2. Fourier inversion and local derivative CLT yield [g(x±1)]/(2g(x))=1+6(z²−1)/M+O(M^{-2}) uniformly for bounded z=x/sqrt(M/12), while α/β=1+4/(πn)+O(n^{-2}); thus n(R−1)→6(z²−1)+4/π for z_n→z. Does not claim the limiting critical equality case or tails. Independently evaluated Eulerian recurrence for n=80,160,320 at z=0 converging to 4/π−6; inspected script separately reconstructs Euclidean ridge volumes and angles at n=4..9.

## originality

PASS

The Eulerian volume of hypersimplices and general Steiner face-angle formula are classical inputs, not the novelty. Primary amplituhedron/hypersimplex triangulation results concern Eulerian tilings and Euclidean geometry but do not state a codimension-two angle-weighted curvature balance or its Gaussian window sign change. Other indexed ridge curvature results involve different polytopes.

## value

PASS

A standard family of high-dimensional polytopes acquires an exact nontrivial second intrinsic volume and a sharp equal-versus-mixed ridge curvature crossover controlled by a natural Gaussian rank coordinate; this is meaningful convex-geometric information not tabulated by simple normalized volumes alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
