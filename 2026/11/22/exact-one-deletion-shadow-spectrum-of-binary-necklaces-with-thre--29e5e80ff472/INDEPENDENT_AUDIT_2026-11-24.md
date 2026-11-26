# Independent mathematical audit

## correctness

PASS

Cyclic ordered zero gaps (a,b,c), total N=n-3, parametrize the rotation-only source classes. One-deletions give the unordered gap pair {g,N-g}, so two different gap values coincide only when they sum to N and the other gap is zero. Zero-deletions are positive-coordinate decrements and have a different weight from the one-deletions. To compare two decrements, cycle the positions to the first two: (a-1,b,c) cannot equal (a,b-1,c) directly, and the two nontrivial rotations force either a=b=c or a=b=c+1, respectively. Thus all-equal positive gaps lose two outputs, type (t,t,t-1) loses one (including t=1), and otherwise the positive-gap deletions are distinct. The resulting buckets count N=0, the one-positive/all-equal cases, the single (1,1,0) case, N-1 ordered positive pairs with a uniquely placed zero less that case plus the t>=2 exceptions, positive two-equal triples less those exceptions, and all-positive distinct triples modulo three-cycle rotation. Counting each by total gap sum and multiplying by z^3 gives all six GFs. The last begins with (1,2,3) in two orientations at n=9 and has coefficient n^2/6+O(n); the remaining classes together are O(n). Fresh literal bit-deletion histograms matched for n=3 through 30, with direct checks on 981 small gap orbits and a gap enumeration versus rational coefficients through n=57. Replay procedure and results: /workspace/branches/b6b33260-f8dc-4adb-adf1-05380715e304/independent-check.md.

## originality

PASS

The supported distinct contribution is the deletion-collision classification for three-one oriented necklaces and the resulting complete histogram, especially the collision type (t,t,t-1) and its zero-gap boundary. The prior three-marker gap-class enumeration covers the six-output column numerically after subtracting one from every positive gap, and covers the pre-exception enumeration for five outputs. Credit that overlap: the corresponding rational counting identities are not new by themselves. The earlier counted observable does not determine the collision law.

## value

PASS

Three ones give a natural small-content class in which clockwise order matters and distinct positive-gap decrements can coalesce modulo rotation. The full distribution explains the exact scarcity and mechanism of these collisions, including the isolated three-output case, and distinguishes generic six-output behavior from the lower-degree sources. This is useful for analyzing the cyclic one-deletion graph independently of its maximum degree or its packing optimum, rather than merely renaming a previously counted column.

The dated certificate retains the supplied scientific assessment, sources and limitations.
