# Independent mathematical audit

## correctness

PASS

Every nonempty subset sum of the independent frame occurs as a vertex with the origin in some ordering, hence must have length at most 2 times the packet radius. Below 1/sqrt(2) all such sums lie in the 14-vector short shell: the six signed axial units and eight half diagonals. Two independent axial units have a length-sqrt(2) sum. With one axial unit, the other vectors must be half diagonals opposite to it in that coordinate; their sum can only be the negative of the axial unit, violating independence. Thus all three are half diagonals. A non-antipodal pair of them is short in sum only when it differs in two signs, so the triple is exactly three distinct vectors of one H_eta. Their Gram matrix has diagonal 3/4 and off-diagonal −1/4, eigenvalues 1,1,1/4, and determinant 1/4. This gives lattice determinant magnitude 1/2, the covolume of the unscaled BCC lattice. Every prefix tetrahedron then has vertices all at squared distance 5/16 from its centroid. Averaging the four squared distances from any other center adds the squared displacement to this value, proving the radius is minimal, not just circumscriptive. The two sign classes give eight unordered and 48 ordered minimizers. The complement has radius at least 1/sqrt(2); for the explicit frame the long pair 0,e_1+e_2 forces this value, and the six stated centers give squared upper bounds 1/2 in four orders and 5/16 in two. Independently checking that arithmetic and the eight shell survivors in doubled integer coordinates confirms the certificates. Vertex containment suffices by convexity of each ball. Long vectors cannot escape the subset-sum obstruction, so the proof covers arbitrary sublattice frames, not just the enumerated shell.

## originality

FAIL

The separate indexed RESULT.md 8e6d7843a500 demonstrably covers the complete claim: same unscaled lattice, maximum over the six prefix-simplex minimum enclosing radii with independent centers, arbitrary independent frames, exact two thresholds, optimizer sets and counts, automatic basis property, and a centrally reflected sharpness example. Its proof uses the same subset-sum shell argument. This is a coverage judgment, not a claim that its later-dated catalogue record precedes the frozen source or a judgment about historical attribution. The earlier kappa-covering and Delaunay literature gives relevant context but is not the reason for the FAIL.

## value

FAIL

The exact second level is a well-motivated rigidity benchmark for the kappa-covering certificate, and would be useful independently of the classical BCC covering radius. As a distinct narrow finding here, however, it adds no new extremal fact, classification or mechanism to the matching complete first-two-level theorem. Reversing the witness or expressing the gap as a ratio gives no additional mathematical value beyond that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
