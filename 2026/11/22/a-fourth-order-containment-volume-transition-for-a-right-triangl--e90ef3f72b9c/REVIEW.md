# Independent mathematical audit

## correctness

PASS

The containment inequalities follow by testing the three source vertices; their midpoint translation at s=t=0 is strict, and the three bounded images bound all four parameters. The independent translation intervals have lengths (a-W_x)_+, (b-W_y)_+, where their widths are the ranges of (0,s,-t) and (0,t,s). In the same-sign quadrants one gets (|s|+|t|,max(|s|,|t|)); the opposite sign swaps these. Independently integrated J by using w=|s|+|t| and m=max(|s|,|t|) on each symmetric half, with Jacobian 1, 0<=w<=min(A,2B) and w/2<=m<=min(w,B). Integrating (A-w)(B-m) and doubling reproduces all three pieces of J; summing 2J(a,b)+2J(b,a) reproduces (1). For a>=b the volume is ab^3-5b^4/8+(2b-a)_+^4/24. Thus the fourth derivative decreases from 1 to 0 (jump magnitude 1), with orders zero through three matching. The square is interior to the common central polynomial. Vertex verification used a fresh exact rational implementation: all 495 quartets, 208 nonsingular, 112 feasible on a/b>=1, 40 distinct feasible affine candidates across the whole parameter domain. Feasibility boundaries and feasible intersections of distinct candidates occur only at 1 or 2. Accordingly counts are 12,20,16,18 in the four stated cases, including nonsimple vertices. Interval endpoints alone should be supplemented by noncollision of affine candidates: if two feasible candidates meet in an open chamber, each of four active constraints of one has affine, nonnegative slack for the other and vanishes at the crossing, so the slack is identically zero; invertible normals force the two affine candidates to be identical. Reflection in x=y on source and target preserves orientation of the conjugated similarity and exchanges side lengths; common rescaling gives volume homogeneity four and preserves vertex counts. Replay: python3 /workspace/branches/1f07829d-39ea-4aab-af51-40fb51da1e72/geometry_check.py. The exact computation is a finite algebraic exhaustion for the entire normalized one-parameter family, not a sampled hull estimate.

## originality

PASS

The four-coordinate configuration space and general construction/optimization algorithms are prior. The inspected statements do not supply this explicit aspect-dependent four-volume or exact full-polytope vertex phases, and the closest exact volume analogues use a different source or target. No broad novelty claim about the containment polytope itself; historical assessment is best of knowledge.

## value

PASS

The full-domain four-volume is a natural configuration-space invariant distinct from maximal size, and the two non-generic aspect ratios are intrinsic. The result pinpoints an exceptional square vertex collapse invisible to volume and a separate ratio-two transition visible first at derivative order four. It gives exact normalizations and a complete shape-family comparison, not a single example or an unsupported algorithmic claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
