# Independent mathematical audit

## correctness

PASS

Independently reconstruct the proof in the vertex coordinates y=Bx. Path matchings cover precisely the even-component subsets: each selected edge contributes its two endpoints, and every even component has its unique consecutive-pair matching. In edge coordinates, the consecutive-sum inequalities characterize the stable-set hull: choose one uniform threshold in [0,1], assign odd positions the initial intervals of length x_i and even positions the terminal intervals of length x_i; consecutive intervals overlap at most on a null boundary, so the resulting stable-set indicator has expectation x. The image of B is the orthogonal complement of the alternating-sign vector of squared length n. The functional x_i is represented in vertex coordinates by the alternating sum on the first i positions; projecting its representing vector onto the image gives squared norm i−i²/n. The functional x_i+x_(i+1) is y_(i+1), giving projected squared norm 1−1/n. The full containment system therefore has exactly the stated clearances. Feasibility at radius r is equivalent to all r(w_i+w_(i+1)+u)≤1, because the coordinatewise minima x_i=r w_i simultaneously attain the least adjacent sums. The difference between consecutive adjacent-sum weights is w_(i+2)−w_i; symmetry and strict increase toward the middle give one central maximizing pair in odd order and two overlapping maximizing pairs in even order. At optimal r their endpoints are forced; all other upper constraints have slack at the minima, and raising every free coordinate a sufficiently small amount puts the center in the relative interior of the claimed codimension-two or codimension-three subspace. This includes n=3 and 4 with no free coordinates. In the ordinary matching-edge metric all pairs are maximizing, which fixes every coordinate and gives 1/(2+√2). The central weights sum asymptotically to √n, yielding the stated scale.

## originality

PASS

Best-of-knowledge pass for the exact inball and full optimal-center classification in the vertex-incidence metric. Existing work on this polytope's incidence/toric description, ordinary path stable-set coordinates and different path polytopes does not supply the parity-split intrinsic metric result.

## value

PASS

This is an exact family-wide comparison of two natural realizations of the same polytope. It explains why one inradius is constant with a unique center while the canonical vertex-incidence inradius shrinks and its optimizer freedom has a parity split. The full optimizer locus and the proof of which constraints impose its affine dimension are useful information not captured by a face-lattice equivalence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
