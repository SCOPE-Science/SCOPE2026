# Independent mathematical audit

## correctness

PASS

The orbit matrix has determinant 1−(−w)^n and column sum w+1, so the affine hull is the full sum hyperplane. Using the basis e_i−e_0 of its lattice differences gives all integer coefficient vectors modulo constants. An entry attaining M gives a predecessor evaluation at least m+wM; an entry attaining m gives one at most M+wm. Width is thus ≥(w−1)(M−m). Even order attains this at coefficient range one by alternation. At odd order the coordinate indicator gives width w and range ≥2 is excluded by the bound except for w=2, range two. In that exception width ≤2 forces the shifted evaluations into [2,4]; a 2 must be preceded by 0 and a 0 by 2. Following predecessors cyclically then forces even order, excluding the exception. For binary coefficients, the mixed transitions both occur and yield 1 and w; exactly one equal transition type gives width w, both give w+1, and no equal transitions yields the even alternating optimum. At odd n, complementing thus gives a unique nonempty no-11 representative modulo reversal; it is primitive because an intrinsic difference of coefficients is one. Splitting the independent-set count by occupancy of one vertex gives F_(n+1)+F_(n−1)=L_n; subtract the empty support. These arguments include n=3 and w=2. A separate bounded ternary enumeration at w=2 for n=3,4,5,7,9 gave counts 3,1,10,28,75, respectively. The frozen Python checker was inspected, not executed; finite results are not needed for the exhaustive symbolic classification.

## originality

PASS

The same graph-polytope construction is known and the Doolittle–Katthän–Nill–Santos width theorem covers particular lattice-equivalent members, including P_(4,2) and P_(5,2). Those widths are not credited as new. The distinct contribution is the uniform width and complete primitive-direction classification for this weighted nonnegative orbit family, in particular the Lucas census rather than simply the value of the width. The compared circulant width theorem demonstrably does not transfer to the whole family and does not state this census.

## value

PASS

The simplices come from a known integer-polytope construction; the intrinsic width controls their thinnest integral slabs. The parity distinction is stronger for extremizing directions than for the width itself: on changing parity a unique unoriented direction becomes a canonical family of independent sets with exponential Lucas growth. The range-two obstruction at w=2 is necessary for completeness rather than a cosmetic special case. The reusable exact census and parity structure are not a rounded numerical or known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
