# Four-phase Haar lattice-count law for fractionally dilated affine hexagons

## Finding
Let \(H_r=\{(x,y)\in\mathbb R^2:\max(|x|,|y|,|x+y|)\le r\}\) and let \(U\) be uniform on \([0,1)^2\). For every integer \(n\ge1\) and every \(0\le t\le1\), count \(N_{n,t}=\#((H_{n+t}+U)\cap\mathbb Z^2)\). Put \(B=3n^2\) and write \(\delta=N_{n,t}-B\). The complete probability law is the following table; within each displayed open interval each row gives the four attainable values of \(\delta\), in order, and their respective probabilities.

| Range | Attainable \(\delta\) | Corresponding probabilities |
|---|---|---|
| \(0<t<1/3\) | \(0, n, 2n, 3n+1\) | \((1-3t)^2,\ 3t(2-5t),\ 3t^2,\ 3t^2\) |
| \(1/3<t<1/2\) | \(n,2n,3n,3n+1\) | \(3(1-2t)^2,\ 3(1-2t)(4t-1),\ (3t-1)^2,\ 3t^2\) |
| \(1/2<t<2/3\) | \(3n,3n+1,4n+1,5n+2\) | \((3t-2)^2,\ 3(1-t)^2,\ 3(2t-1)(3-4t),\ 3(2t-1)^2\) |
| \(2/3<t<1\) | \(3n+1,4n+1,5n+2,6n+3\) | \(3(1-t)^2,\ 3(1-t)^2,\ 3(1-t)(5t-3),\ (3t-2)^2\) |

At \(t=0\) and \(t=1\) the count is almost surely constant, respectively \(3n^2\) and \(3(n+1)^2\). At \(t=1/3\) and \(t=2/3\) the law has exactly three equally likely values, obtained by continuous substitution in an adjacent row. At \(t=1/2\), the two values \(B+3n\) and \(B+3n+1\) occur with probabilities \(1/4\) and \(3/4\), respectively. In particular, outside those five special radii the law has exactly four atoms.

The expectation is \(\mathbb E N_{n,t}=3(n+t)^2\), the Euclidean area of \(H_{n+t}\). Its variance is exactly
\[
\operatorname{Var}(N_{n,t})=\begin{cases}
-3t(4n^2t-2n^2+12nt^2-6nt+3t^3-t),&0\le t\le1/2,\\
3(1-t)(4n^2t-2n^2+12nt^2-10nt+2n+3t^3+3t^2-6t+2),&1/2\le t\le1.
\end{cases}
\]
The polynomial variance can equivalently be evaluated directly from the four rows; the latter is the canonical exact specification. For each fixed nonintegral \(t\), \((N_{n,t}-3n^2)/n\) has a finite-support weak limit obtained by discarding the additive constants in the four displayed supports.

## Assumptions and scope
All counts include lattice points on the boundary, which changes nothing almost surely under continuously uniform translation. The orientation and fixed ambient lattice are essential: the hexagon is an affine-regular, centrally symmetric lattice hexagon with its facet normals \((1,0),(0,1),(1,1)\), rather than a Euclidean regular hexagon aligned with the square lattice. The radius is a real \(r=n+t\) with integer \(n\ge1\) and \(0\le t\le1\); no assertion is made for general planar lattice polygons, different orientations or a nonuniform translation law. The four phases refer to open parameter intervals; at the transition values atom masses can vanish.

## Proof
Fix \(0<x,y<1\) away from the finite arrangement of boundary lines in the unit square. For \(r=n+t\), set
\[
L_x=\lceil x-r\rceil,\quad R_x=\lfloor x+r\rfloor,\quad
L_y=\lceil y-r\rceil,\quad R_y=\lfloor y+r\rfloor,
\quad L_z=\lceil x+y-r\rceil,\quad R_z=\lfloor x+y+r\rfloor.
\]
An integer pair \((i,j)\) contributes exactly when \(L_x\le i\le R_x\), \(L_y\le j\le R_y\), \(L_z\le i+j\le R_z\). For integers \(s,A,B\), with \(A,B\ge0\), the number of integer \((i,j)\) with \(0\le i\le A\), \(0\le j\le B\), \(i+j\le s\) is
\[
F(s;A,B)=\binom{s+2}{2}_+-\binom{s-A+1}{2}_+-\binom{s-B+1}{2}_++\binom{s-A-B}{2}_+,
\]
where \(\binom{k}{2}_+=k(k-1)/2\) if the integer \(k\ge2\), and zero otherwise. This is inclusion-exclusion of lattice points under a diagonal in the first quadrant. Consequently the count is the exact difference
\[
F(R_z-L_x-L_y;R_x-L_x,R_y-L_y)
-F(L_z-1-L_x-L_y;R_x-L_x,R_y-L_y).
\]
Define integer step variables
\[
a_x=\lfloor x+t\rfloor,\quad b_x=\lceil x-t\rceil,\quad
a_y=\lfloor y+t\rfloor,\quad b_y=\lceil y-t\rceil,\quad
c=\lfloor x+y+t\rfloor,\quad d=\lceil x+y-t\rceil.
\]
For \(0<t<1\), \(a_x,a_y,b_x,b_y\in\{0,1\}\), \(c,d\in\{0,1,2\}\). Substituting \(L_x=-n+b_x\), \(R_x=n+a_x\) (and their analogues) into the preceding difference, every term with a nonpositive upper corner vanishes for all \(n\ge1\), yielding the explicit *ordinary polynomial* identity
\[
\boxed{N_{n,t}=\binom{3n+c-b_x-b_y+2}{2}-
\binom{n+c-b_y-a_x+1}{2}-
\binom{n+c-b_x-a_y+1}{2}-
\binom{n+d+1-b_x-b_y}{2}.}\tag{1}
\]
Each binomial in (1) is an ordinary polynomial \(k(k-1)/2\), including arguments zero or one. Thus on every open arrangement cell the count is a quadratic polynomial in \(n\) with leading term \(3n^2\); its remaining coefficients are integers depending only on the six step variables, not on \(n\) or on the precise position within the cell.

The six step variables change only across eight lines within \([0,1]^2\): \(x=t,1-t\), \(y=t,1-t\), and \(x+y=t,1-t,1+t,2-t\). Cutting the unit square along these eight lines and computing (1) at one interior point per cell gives the possible values of the count. A cell probability is its planar polygon area. The stated four table rows follow from clipping the unit square by these half-planes and summing the areas of the cells with the same count; all vertices are intersections of two listed lines. For a completely reproducible exact-arithmetic evaluation see `hex_distribution_verify.py`, which computes each area by rational polygon clipping and evaluates (1) independently through the original lattice inequalities.

For clarity why the table covers *all real parameters*, every intersection vertex of the eight lines and the four edges of the unit square depends affinely on \(t\) as long as its defining line pair is fixed. The only internal parameter values where three such lines meet in the unit square or where their order changes are \(1/3,1/2,2/3\), found by solving their linear equations. Consequently each cell has a fixed step-variable label in each of the four phases; its area is quadratic in \(t\) and its count label is independent of \(t\). Therefore three exact interior parameter evaluations in each phase uniquely determine every mass polynomial. The verifier uses precisely that finite interpolation certificate, with additional checks at all transition values. Since the quadratic-degree assertion, label stability and list of all transitions were independently proved, this is an exhaustive *symbolic* reduction, not inference about real parameters from scattered numerical sampling.

Summing the table probabilities gives one. Their first moment gives \(3(n+t)^2\), consistent independently with the unit-square translation-integral identity \(\mathbb EN=\operatorname{area}(H_{n+t})\). Squaring the displayed supports and taking their second moments gives the stated piecewise variance; at the transitions adjacent expressions agree. The two endpoint laws follow from the integer-dilate translational multi-tiling identity, or directly from (1) by continuity in measure.

## Verification
The standard-library standalone program `hex_distribution_verify.py` performs exactly rational clipping of the torus square by the eight parameter lines. It tests 15 nontrivial rational radii including all three transitions and six integer scales for 90 full distribution comparisons, reconstructing every cell area from scratch, checking the formula against direct lattice enumeration on each cell and checking the expected area. It also checks the integer-radius endpoint laws at six integer scales. These computations are finite and therefore diagnostic; the algebraic proof of (1), the exact description of the parameter transition set, and the quadratic interpolation degree bound are required for the all-parameter theorem. The small-radius endpoint limit is understood almost everywhere.

## Relationship to prior work
Freyer and Hofstätter (2026) study translation counts of convex bodies and a homogeneous decomposition for **integer** dilates of lattice polytopes; their Theorems A and B and the toric-arrangement framework do not give the stated explicit distribution for a *fractional* dilation of this hexagon. Tokmachev (2025) proves that centrally symmetric integer lattice polygons have almost-surely constant translation count, explaining the integer-radius endpoints, but their integer-vertex hypothesis does not imply the four-atom law at noninteger radius. Earlier work by Tokmachev (2024) gives a distribution for integer lattice triangles, not this fractionally dilated hexagon. Standard Ehrhart theory gives counts at the unshifted integer radii, not probability masses for arbitrary fractional radii. The novelty claimed here consists of the full four-phase distribution, sharp transition points and all exact probabilities, not the first-moment formula or the integer multi-tiling fact.

## Limitations
No result is claimed for general convex hexagons, irrational slopes, arbitrary lattice orientations, more than two dimensions, or nonuniform offsets. The parameter \(n\ge1\) excludes the small-radius interval \((0,1)\), whose phase diagram can differ. The distribution gives only a translation-average law, not equality of point-count functions of different bodies. Literature comparison is necessarily provisional against unindexed older computations; no independent mathematical audit was performed.

## References
1. A. Freyer and G. C. Hofstätter, *Counting Lattice Points in Translations: Uniqueness and Existence Results*, arXiv:2610.26523v1, first submitted 2026-10-19; https://arxiv.org/abs/2610.26523 (revised v2 inspected, especially Sections 1–2).
2. A. Tokmachev, *Lattice points inside a random shifted integer polygon*, arXiv:2407.09878, first submitted 2024-07-13; https://arxiv.org/abs/2407.09878.
3. A. Tokmachev, *On integer points inside a randomly shifted polyhedron*, arXiv:2507.09355, first submitted 2025-07-12; https://arxiv.org/abs/2507.09355.
4. M. N. Huxley and J. Žunić, *The number of configurations in lattice point counting II*, Proc. London Math. Soc. 107 (2013), 1331–1352, https://doi.org/10.1112/plms/pdt011.
