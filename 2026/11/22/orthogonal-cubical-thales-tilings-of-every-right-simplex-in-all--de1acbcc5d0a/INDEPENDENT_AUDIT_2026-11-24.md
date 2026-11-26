# Independent mathematical audit

## correctness

PASS

Faces through 0 give coordinate deletion and strictly positive retained barycentric weights, including the positive remaining weight at 0. For a face indexed by I not containing 0, the foot has retained coordinates b_i+λ_I/L_i, with λ_I>0 by the strict interior hypothesis. The origin normal cell is exactly the box [0,b_1]×…×[0,b_d]. At v_i set t=L_i(x_i−b_i); then the normal constraints are t≥0 and x_j≤b_j+t/L_j for j≠i. The original simplex constraints reduce to 0≤x_j for j≠i and the slanted top. In the full-dimensional cell, bottom t=0 and top cannot meet because at t=0 all x_j≤b_j and Σ b_j/L_j<1. Each upper/lower coordinate pair is also disjoint. A vertex needs d independent active inequalities, hence one per pair; all 2^d choices solve uniquely and feasibly as exactly the two families of feet, with independent active normals. Thus all stated inequalities really are facets and compatible intersections are precisely partial choices of the pairs, giving the cube and the antipodal v_i (top and lower choices) and B (bottom and upper choices). South/north intersections work coordinatewise in the cube, giving O1–O2. O3 can be checked directly: the edge at v_i for the bottom/top swap is along e_i, normal to the north facet t=0. The edge at v_i for a j-swap is along v_j−v_i, normal to the north facet x_j=b_j+t/L_j. At 0 it is coordinate perpendicularity. The inspected conditional Proposition 4.2 can also be used once the combinatorics and distinct projection vertices have established admissibility. Every point has at least one support-score maximizing vertex and two distinct cells meet on their tie hyperplane, a face of both. This verifies the normal-cell equality and face-to-face tiling for all allowed B and leg lengths, not just symmetric anchors or lengths.

## originality

PASS

The distinct conclusion supported by the inspected literature is the uniform metric result for right simplices, at every interior anchor and at every vertex, including dimensions at least four. The prior cube combinatorics, always-existing normal-fan tiling, conditional apex cutout machinery and low-dimensional results are substantial overlaps and are not claimed as new. The inspection does not establish historical priority for the remaining metric result.

## value

PASS

The theorem resolves the actual projection-cutout identification, a substantive part of the higher-dimensional Thales question, for a natural family of simplices with no tuning of the interior anchor. The exact cell inequalities and cube structure give concrete usable geometry, including non-box cells. An abstract cube subdivision by itself would not resolve that question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
