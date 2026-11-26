# Independent mathematical audit

## correctness

PASS

In the 0/1 metric, the odd-corner constraints are Hamming-distance affine functions d_w≥1. The open removed simplices are disjoint, since d_w+d_{w'}≥2 for distinct odd corners. No fractional vertex is introduced: one tight odd cut with at least two fractional coordinates permits a small opposite signed perturbation, and a single fractional coordinate cannot make such an affine cut tight. Two distinct tight cuts force the centers to be distance two and all other coordinates to be fixed to their common values; the intersection then lies on the segment between two even vertices. With no active cut, fractional coordinates are free. Thus the given facets exhaust the polytope. Fixing two axes leaves a parity halfcube, of full remaining dimension when n≥5; fixing one coordinate at its odd-center value removes one vertex from the simplex facet, producing a simplex ridge. Two odd centers have at most two common even neighbors and cannot make a ridge. These intersections give both counts, including the absence of coordinate–coordinate ridges when n=4. Subtracting orthogonal corner volumes gives each halfcube measure; a simplex Gram determinant m+1 gives volume sqrt(m+1)/m!. Coordinate normals are orthogonal and a coordinate and incident odd-cut normal have cosine 1/sqrt(n). In the stated Steiner normalization, the outer normal sector occupies θ/(2π) of its plane, giving the formula and V2(H4)=8sqrt(3)/3. The displayed positive denominator D_n satisfies D_{n+1}−2D_n=(n−3)(n−2)!, so the ratio decreases with the stated crossing and factorial tail. The opposing limits refer to the probability of an exactly right angle; both angle distributions themselves converge weakly to a point mass at π/2. The frozen floating-point program covers only dimensions 4–7; it is not the all-dimensional proof.

## originality

FAIL

Green's earlier coordinate-level face classification and facet-intersection lemma cover the complete ridge census, with the same two types and counts. The remaining formulas are mechanical metric evaluations of these explicit faces and facet equations in the fixed 0/1 scale, followed by the standard polyhedral Steiner sum and a direct ratio of the resulting known face counts and elementary measures. The bounded search did not verify a prior table printing the final Steiner or crossover formulas verbatim; the FAIL is based on prior implication, not on assuming such a table exists.

## value

FAIL

The distinction between counting faces and weighting them by Euclidean measure is a meaningful question on this natural family. But here the precise cutoff and Steiner coefficient follow by routine metric evaluation and comparison of the established coordinate-level face census, without a surviving independently useful unknown structural or metric fact. The two angle measures actually have the same weak limit; the contrast is specifically in the mass at exactly π/2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
