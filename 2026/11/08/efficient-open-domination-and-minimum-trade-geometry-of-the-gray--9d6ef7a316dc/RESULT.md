# Efficient open domination and minimum-trade geometry of the Gray graph

## Finding

Let \(G\) be the Gray graph in its point--line incidence model: the points are \(\mathbb F_3^3\), the lines are the \(27\) axis-parallel three-point lines, and incidence defines the \(81\) edges of a bipartite graph on \(54\) vertices. An **efficient open dominating set** is a vertex subset \(D\) such that every vertex has *exactly one neighbor* in \(D\). The graph has exactly \(252\) such sets, each of size \(18\).

Write each set uniquely as \(D=P\cup L\), with \(P\) consisting of nine point-vertices and \(L\) of nine line-vertices. Define an elementary minimum trade by either replacing exactly **six** selected point-vertices with six unselected point-vertices, leaving \(L\) unchanged, or replacing exactly **three** selected line-vertices with three unselected line-vertices, leaving \(P\) unchanged; both endpoints must be efficient open dominating sets. Six and three are the respective smallest possible nonzero replacement counts. The minimum-trade graph satisfies

\[
\boxed{\mathcal R(G)\cong K_{3,3,3,3}\mathbin\square T,}
\]

where \(T\) is obtained from three copies of the three-dimensional cube graph \(Q_3\), indexed by the three unordered pairs of coordinate axes, by identifying each pair of copies at the one all-parallel tiling they share. Distinct copies have no other common vertices or edges. Consequently, \(T\) has \(21\) vertices and \(36\) edges, is connected, and has radius and diameter \(4\).

The trade graph has \(252\) vertices, \(1566\) edges, and is connected. Exactly \(36\) vertices have degree \(15\), and \(216\) have degree \(12\). Every vertex has eccentricity \(6\), so both radius and diameter are \(6\). Its numbers of unordered vertex pairs at distances \(1,2,3,4,5,6\) are respectively

\[
\boxed{(1566,4896,8460,9180,6444,1080).}
\]

Under the natural \(1296\)-element coordinate-permutation group (the full automorphism group of the Gray graph), the efficient open dominating sets form precisely two orbits of sizes \(36\) and \(216\). They are characterized by whether their nine selected line-vertices are all parallel or use two axis directions.

## Assumptions and scope

Coordinates belong to \(\mathbb F_3=\{0,1,2\}\), with arithmetic modulo \(3\); an axis line consists of the three triples obtained by varying one coordinate with the other two fixed. A line-vertex is distinct from each of its incident point-vertices. The cardinalities above count *labelled geometric subsets* of this explicitly specified graph: no quotient by automorphisms is taken except in the orbit statement.

A replacement count refers to \(|P\setminus P'|\) on the point side or \(|L\setminus L'|\) on the line side; symmetric differences have twice these sizes. In one minimum trade exactly one side is altered, with the other fixed. These conventions exclude transformations that simultaneously change both sides or admit non-code intermediate states. The two smallest nonzero replacement counts are intrinsic because any efficient open dominating set decomposes into two independently feasible parts.

## Proof

**Step 1: reduction to two independent exact-cover problems.** Every point-vertex must have exactly one selected neighboring line-vertex, so \(L\) is a partition of the \(27\) grid points into axis lines. Every line-vertex must have exactly one selected neighboring point-vertex, so \(P\) meets every axis line in exactly one point. Conversely, any pair \((P,L)\) satisfying those two conditions gives an efficient open dominating set. Counting incidences in either condition yields \(|P|=|L|=9\), independently of the other side.

**Step 2: all point selections are affine Latin squares.** The condition that every line parallel to the third axis contains exactly one point of \(P\) expresses \(P\) as the graph \(\{(x,y,f(x,y)):x,y\in\mathbb F_3\}\). The other two directions say that \(f\) is a Latin square of order three. Every permutation of \(\mathbb F_3\) is affine, so for fixed \(x\) write \(f(x,y)=b_x y+c_x\), with \(b_x\in\{1,2\}\). If \(b_x\ne b_{x'}\), the two rows agree for exactly one \(y\), contradicting the Latin property. Hence \(b_x=b\) for all \(x\), and \(x\mapsto c_x\) is a permutation, necessarily \(c_x=ax+c\), with \(a\in\{1,2\}\). Thus precisely twelve point codes occur:

\[
P_{a,b,c}=\{(x,y,ax+by+c):x,y\in\mathbb F_3\},\qquad
(a,b,c)\in\{1,2\}^2\times\mathbb F_3.
\]

Two such codes with equal slope pair \((a,b)\) and different \(c\) have no point in common, so replacing one by the other requires nine replacements. With different slope pairs, their difference is a nonconstant affine map on \(\mathbb F_3^2\), whose zero-set has exactly three cells. Therefore they agree in three points and differ in six. The minimum point-trade graph is the complete four-partite graph \(K_{3,3,3,3}\): its four parts are the fixed-slope triples, and it has \(54\) edges, degree \(9\), radius \(2\), and diameter \(2\).

**Step 3: exact classification of line tilings.** Suppose \(L\) includes at least one line parallel to the first axis. In each plane of constant first coordinate, the cells occupied by those first-axis lines occupy the same subset \(S\) of the \(3\times3\) slice. All remaining cells must be covered by full rows or full columns in that slice. A full row intersects every full column, so no slice can contain both orientations. If \(S\) is neither empty nor the whole plane, its complement cannot simultaneously be a nonempty proper union of rows and a union of columns; hence all three slices use the same second orientation. Thus no tiling uses all three axes.

For any fixed unordered pair of axes, the remaining coordinate divides the box into three \(3\times3\) planes. In each plane one chooses one of the two axis orientations, independently, giving \(2^3=8\) tilings. The two constant orientation words correspond to all-parallel tilings, each shared with another axis-pair family. Consequently, the number of tilings is \(3+3(8-2)=21\): three all-parallel and eighteen mixed.

**Step 4: the minimum line trades form three glued cubes.** Let \(L,L'\) differ by exactly three selected lines on each side. All nine grid points covered by the removed lines must be covered by the three added lines. Distinct axis lines intersect in at most one point. Each removed line must meet each added line, for otherwise its three cells could not be covered by only three different added lines. If two removed lines had different directions, at most one axis line could meet both (the third-direction line fixed by their two coordinate constraints), contradicting the three distinct added lines. Thus all three removed lines are parallel; the same argument gives three parallel added lines in a different direction. Their nine pairwise intersections form a full \(3\times3\) coordinate plane. Every minimum trade therefore changes one plane's orientation from one axis to the other.

For each axis pair, the three plane-orientation bits form a copy of \(Q_3\); changing one bit gives exactly a three-line trade. Different axis-pair cubes meet only in their common all-parallel tiling, yielding the asserted graph \(T\). Each pure tiling has degree six, each mixed tiling degree three, so \(|E(T)|=(3\cdot6+18\cdot3)/2=36\). Its diameter is at most four: any two cubes share a pure tiling, and every mixed state is at distance at most two from either of its two pure endpoints; a pure tiling can reach a mixed state in the opposite cube via one of that cube's two endpoints in at most four moves. Each pure state is distance four from an appropriate mixed state in the opposite cube, and each mixed state is distance four from an appropriate mixed state in another cube. Therefore every eccentricity in \(T\) equals four.

**Step 5: product metric and exact enumerator.** Because every allowed move changes exactly one independent factor, the code graph is the Cartesian product of the two factor graphs. Its edges number \(54\cdot21+36\cdot12=1566\). Its degrees are \(9+6=15\) in \(12\cdot3=36\) states and \(9+3=12\) in \(12\cdot18=216\) states. Graph distance adds across factors, and both factors are self-centered, giving radius and diameter six. The unordered distance counts in the point factor are \((54,12)\) at distances \((1,2)\); in the line factor they are \((36,63,66,45)\) at distances \((1,2,3,4)\). Multiplying their *ordered* distance enumerators

\[
(12+108t+24t^2)(21+72t+126t^2+132t^3+90t^4)
\]

and dividing each positive-degree coefficient by two produces the stated six-distance histogram (the constant coefficient is \(252\)). The total is \(\binom{252}{2}=31626\).

**Step 6: two symmetry orbits.** Independent permutations of the three symbols in each coordinate, together with permutations of the three axes, act on points and axis lines; the group has order \(6^3\cdot6=1296\). These transformations preserve the number of line orientations, hence distinguish pure from mixed tilings. They act transitively on the three pure tilings, and the stabilizer of any pure tiling acts transitively on the twelve affine Latin squares. They also act transitively on the eighteen mixed tilings; after fixing a mixed tiling oriented along the first and second axes in distinct layers of the third coordinate, independent symbol permutations in the first and second coordinates act transitively on the twelve affine Latin squares. Thus the two orbit sizes are \(3\cdot12=36\) and \(18\cdot12=216\). The cited Gray-graph symmetry result identifies this coordinate group as the full graph automorphism group.

## Verification

The standalone programs `verify_exact_cover.py` and `verify_structural.py` require Python 3 and only the standard library. Run each directly from the extracted artifact directory. The first independently enumerates exact covers for both bipartition classes, tests all \(252\) codes against all \(54\) open-neighborhood conditions, generates the full trade graph, performs all-source breadth-first searches, and computes the coordinate-group orbits. The second constructs the twelve affine point codes and three families of cube-orientation line tilings directly; it derives both factor graphs and convolves their independent distance enumerators. Both reproduce the claimed counts and geometry.

## Relationship to prior work

The Gray graph and its point--line realization were studied by Bouwer and by Marušič--Pisanski; the latter's 2000 paper has a verified first-public date of 9 August 2000. Efficient open domination, also called total perfect codes or exact transversals, is an established notion. Kuziak--Peterin--González Yero (2014) develops the notion for standard graph products, rather than supplying this Gray-incidence classification. The count of \(21\) complete rod tilings of the \(3\times3\times3\) box already appears in OEIS A181323 (2011), and the existence of twelve Latin squares of order three is classical; neither raw factor count is claimed independently new.

The contribution here is the explicit code--factor bijection **together with the minimum-trade Cartesian-product structure**, the glued-cube classification, full metric and automorphism-orbit split. Neither the known rod count nor the general definition of efficient open domination implies these trade-graph conclusions alone. Searches of published research records and targeted literature yielded no matching prior theorem, but this is not a proof of historical uniqueness.

## Limitations

This classification is for the specified \(54\)-vertex Gray incidence graph, not all cubic or semisymmetric graphs or higher-dimensional incidence cubes. The diameter bound applies only to code-preserving trades that change exactly one factor with the stated minimum replacement size. It does not address arbitrary simultaneous changes or intermediate configurations failing the domination condition. Some relevant older graph-geometry papers were accessible only through abstracts or secondary references, leaving a residual literature-priority risk.

## References

1. D. Marušič and T. Pisanski, *The Gray graph revisited*, Journal of Graph Theory 35 (2000), 1–7; first published 9 August 2000. DOI: https://doi.org/10.1002/1097-0118(200009)35:1%3C1::AID-JGT1%3E3.0.CO;2-7.
2. D. Kuziak, I. Peterin, and I. G. Yero, *Efficient open domination in graph products*, Discrete Mathematics & Theoretical Computer Science 16:1 (2014), 105–120. DOI: https://doi.org/10.46298/dmtcs.1267; freely available PDF: https://dmtcs.episciences.org/1267/pdf.
3. M. Simões, OEIS A181323, *Number of ways of placing n rods of length 3 in a 3x3x3 cubic lattice without any two rods intersecting*, entry submitted 27 January 2011. https://oeis.org/A181323.
4. Gray graph, graph-data summary with the 27-point/27-line realization and 1296-element symmetry group: https://jaanos.github.io/tables/graphs/Gray.html.
5. I. Z. Bouwer, *An edge but not vertex transitive cubic graph*, Bulletin of the Canadian Mathematical Society 11 (1968), 533–535.
