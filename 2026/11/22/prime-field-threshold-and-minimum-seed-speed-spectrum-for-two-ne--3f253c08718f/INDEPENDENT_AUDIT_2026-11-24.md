# Independent mathematical audit

## correctness

PASS

Two active points give their unique join and two active lines their unique meet; by bipartiteness these are all the operations, hence the terminal set equals join–meet closure. Three or fewer seeds give at most a triangle with its sides, or, in the mixed case, a single joining line, the given line and points on the join, and duals. Four points with three collinear have only those points and their joins in their closure; the nondegenerate quadrangle normalizes over the prime field. For two points A,B and two lines L,M, let N=AB and C=L∩M. If C∉N, the closed configuration lies in the pencil through C plus its transversal N, with at most four points on N, namely A,B and its intersections with L,M, and at most five vertices on either shore. If C∈N, the points stay on N and lines in the pencil at C. Three collinear points plus a line give at most one extra point and the join; a triangle plus a line through a vertex adds at most its intersection with the opposite side, which yields three collinear points and the off-line vertex and their joins. These closures are proper even at q=2. For a triangle and a line avoiding its vertices, normalize to the coordinate triangle and x+y+z=0 by rescaling coordinates. The triangle sides and line meetings produce the frame consisting of e_1,e_2,(1:0:−1),(0:1:−1). Frame-only joins and meets stay over the prime field and generate it: construct affine axes, a unit mark and the slope −1; transport scalars across axes, add by slope −1, and multiply by constructing a similar triangle with parallels. The finite subring obtained is a field; affine points and infinity slopes over that field then give all lines by joins. In the five-seed construction the mark (1:α:0) yields α by intersecting its line through the origin with x=1 and projecting to an axis, so α generating F_q gives the whole plane. Point–line duality gives the reverse-shore cases. Ordered frames have v(v−1) choices for the first two points, q² for the noncollinear third and (q−1)² for the fourth off the sides; dividing by 24 gives Q_q. The noncollinear triples with one avoiding line give four times Q_q, since there are (q−1)² such lines by duality. Independent replay `python3 /workspace/review_calculations/bootstrap_affine.py` constructs the plane from affine slope lines, vertical lines and the line at infinity; it checks degrees and same-shore pair intersections, and updates both shores simultaneously by combining two split-shore neighbor-count tables. It exhausts 111,930 four-seeds (zero successes) and 850,668 five-seeds for q=4, exactly reproducing every composition-by-round cell, the round totals 22,176, 211,680, 100,800, and 334,656 successes overall. It also checks the 70 and 2,340 four-seed totals and zero three-seed successes at q=2 and 3. Finite counts do not extend to q>4.

## originality

PASS

The supported distinct contributions are the mixed-shore classification and exact prime-field enumeration, and the complete q=4 minimum-seed completion-round spectrum. The frame-generation lemma, point-only extension threshold ingredients and Heawood closure structure are prior and are not accepted as new. No checked result on the same process covers the mixed classification over all prime fields or the synchronous q=4 census.

## value

PASS

The all-order minimum size is sensitive to prime subplanes, but the point-only threshold leaves open whether mixing shores beats the obstruction. The classification and exact enumeration resolve this structurally and show which seed compositions realize the optimum. The first proper extension q=4 is intrinsic to the threshold change, not an arbitrary numerical slice: the complete synchronous profile distinguishes compositions with the same eventual success and determines the fastest and slowest minimum seeds in the smallest extension geometry. This is an exact baseline for comparison at larger extensions, not an extrapolation to them.

The dated certificate retains the supplied scientific assessment, sources and limitations.
