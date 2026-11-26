# Independent mathematical audit

## correctness

PASS

A shortest-side plank and the 2d exterior coordinate strips give the two upper bounds. For a strictly cheaper hypothetical cover, slightly enlarge to open planks and perturb the normals to have no zero components, using the bounded outer box to retain coverage and the strict cost margins. Write T for total width and g_j=L_j−h_j; the normalized directional budget R_j sums to T, so some R_j<g_j. Lemma 6 of Bakaev–Polyanskii, applied to widths divided by T, gives r_j=1, r_k≥1 and X_j≤R_j, X_k≤T for k≠j. With A=diag(r), Bang's signed vectors in original coordinates are w_i A n_i/(2n_iᵀA n_i); the arbitrary offsets are allowed by Lemma 3. Adding the open hole plank in direction j contributes h_j only to the j-span. All signed sums are within the centered outer box since X_j+h_j<L_j and X_k<L_k, so the selected sum misses the enlarged cover and the open hole. In the plane at cost S<L_*, the same strict-margin argument forces R_j=g_j for each direction. An oblique term makes the Lemma 5 bound strict: the elementary fraction's tangent at λ=1+a/b is [a+b+(λ−1)a]/(1+ab), strictly below 1+(λ−1)a/(a+b) for 0<a,b<1 on the unit circle. Axial cases follow by substitution. If X_2 reaches S, the bound gives X_1<g_1 there; otherwise X_1 tends to the weight of the e_1 normals alone, strictly less than g_1, while X_2≤S<L_2. Either case gives strict geometric margins, permitting small enlargement of the original closed planks with λ fixed before applying the open-plank lemma. Thus all planks are axial. If one exterior coordinate is missed along its own axis, a coordinate missed along the other axis exists because its total strip width is less than the side length; the pair would be an uncovered shell point. Exact equality of widths with the exterior lengths then gives the partition, with no positive-width waste, and the converse is a strip cover. Replay: verify.py (Python 3.10+, inspected, not run) samples 1,332 rational inequalities/budgets and checks the outside-hole coordinate condition at 1,764 centered grid points. It does not explicitly build the covers or establish the universal lower bound.

## originality

PASS

The source explicitly does not claim the known unit-square law or its optimizer classification as new. The distinct contribution is the Euclidean cost law for general outer orthotopes and strict-regime rigidity for nonsquare outer rectangles. The strongest inspected geometric lemma is reused, not rediscovered; the directional budgets and strict equality analysis adapt it to the unequal-side constraints.

## value

PASS

This gives an exact Euclidean cost transition for arbitrary finite orientations in a natural nonconvex geometry, with no symmetry assumption on the hole location. Unequal outer side lengths cannot be removed by a width-preserving normalization. The planar equality result identifies every optimum, rather than just giving coordinate-strip examples, and distinguishes strict large-hole geometry from the unclassified threshold and other phases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
