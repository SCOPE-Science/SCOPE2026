# Independent mathematical audit

## correctness

PASS

The weighted cycle vertex metric is the two-bit weighted Hamming metric. Assume a≥b and set R=(a^p+b^p)^(1/p). Below R, a ball can leave its own long-bit fiber only for a neighbor with unchanged short label. A long-bit fiber omitted by the three centers therefore receives at most three labels and cannot be covered. At R the proposed complementary pair in one fiber and a center in its opposite cover both occupied fibers and all short labels in the two remaining fibers; this works also at p=1. For a>b and p>1 an R-ball consists of its own fiber and one two-point line in each adjacent fiber. Any pair intersects: equal fibers share their full fiber; for adjacent fibers use one center's own full fiber and the other's line there (clarifying the intermediate-fiber wording at line 28); for opposite fibers the two lines in a common adjacent fiber are perpendicular. Two eight-point balls cannot cover. Three distinct occupied fibers leave perpendicular lines in the missing fiber; two adjacent occupied fibers would require at least two centers in each; one occupied fiber cannot reach its opposite. For two opposite occupied fibers the repeated short labels must differ in both bits, giving 4×2×4=32 triples. For a=b and p>1 balls are 3×3 toroidal neighborhoods and pairwise intersections have at least four points. The minimum-distance graph is Q4 and its isometries act by bit translations and coordinate permutations: a zero-fixing automorphism is determined by the four neighbors, since distance to those and zero recovers every support. True metric distances 2a and 2^(1/p)a distinguish paired directions among the two-bit displacements, leaving exactly 128 maps. The fresh exhaustive replay over all 560 triples yielded 96 equal-edge covers with orbits of 32 and 64 under those maps, and checked the unequal count and two-center exclusion. Replay: python3 /workspace/branches/1dbfcd14-2b89-4a1d-864a-4f11e0ade3b9/record4_replay.py; saved output is record4_replay.txt in the same directory. The analytic threshold reduction is separate from this replay; the frozen script was not executed. Finally a≤R<a+b for p>1 so the factor needs exactly two balls, whereas the product needs three.

## originality

PASS

The distinct contribution is the sharp formula across alternating positive weightings, the complementary-pair classification, and the optimizer counts and equal-weight orbit structure. Do not credit the equal-edge three-ball counterexample as new. The strongest cited primary example was not retrievable; its further exact coverage remains a risk.

## value

PASS

The product-cover obstruction motivating the unweighted example survives a full natural family of alternating anisotropies at an exact threshold, including an analytic p=1 boundary. The asymmetric classification and exact jump at equality describe how many optimal three-center arrangements persist or become available, beyond a re-run of the known three-ball witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
