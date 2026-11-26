# Independent mathematical audit

## correctness

PASS

Reconstructed the proof over every finite field of characteristic >3. The rational locus follows from nonzero (q−1)-powers being 1. At a geometric singularity normalize the coordinate sum to 1; vanishing of the gradient gives x^(q−2)=y^(q−2)=z^(q−2)=3. The translated variables u=3x−1, v=3y−1, w=3z−1 have sum and sum of squares zero, satisfy T^3−uvw=0, and obey u^q=u^2+2u and analogues. Squaring and summing yields 12uvw=0, so all three vanish. The nondegenerate quadratic term gives the node; uniqueness and Bézout exclude reducibility in degree ≥4. For the incidence count, the normalized gradient is (1/x−3,1/y−3,1/z−3). The six vertices each exclude exactly three choices from q. The product equation on a coordinate nonvertex and the nonsingular conic on the sum-zero line each give q−4−χ(t²−t+1) after disjoint exclusions. The sum of χ(t²−t+1) is −1 by a factorization with nonzero constant; subtracting t=0,1 yields the claimed frequencies. For the cubic at the node, the three exceptional slopes 0, −1 and infinity retain distinct third points at infinity, and exactly 1+χ(−3) slopes lose their third point to the node. Removing six boundary points and the node leaves q−6−χ(−3). Checked the incidence total and the q=5,7 cases including the zero-frequency boundary row. The proof, not the frozen arithmetic logs, certifies the all-field formula. See checks/analytic-notes.md.

## originality

PASS

The supported contribution is the uniform exterior contact-count law and incidence total, not the curve, qualitative coverage for q≥11, or the uncovered node at q=7. The closest inspected results do not determine the point-side multiplicities including repeated contributions from one tangent line.

## value

PASS

Exact covering multiplicity is a natural refinement of tangent filling for the defining example. It quantifies redundancy at the exterior points, distinguishes the small fields from the general case, and isolates the dependence on the quadratic character. It is a uniform result, not a single-field recomputation or a renamed Gauss-fibre count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
