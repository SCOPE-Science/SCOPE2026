# A simplex and Ehrhart parity correction for pendant-decorated odd-cycle matching polytopes

## Finding

Let \(G\) be a simple odd cycle \(C_n\), \(n\ge3\), with \(t\ge1\) additional edges from cycle vertices to distinct new leaves. Several leaves may share a cycle vertex. Put \(d=n+t\), and in the standard edge coordinates define
\[
F_G=\{x\in\mathbb R_{\ge0}^{E(G)}:\sum_{e\ni v}x_e\le1\text{ for all }v\},
\qquad M_G=\operatorname{conv}\{\mathbf1_H:H\text{ a matching of }G\}.
\]
Then \(F_G\setminus M_G\) is a full-dimensional simplex with its base facet removed, **not** the interior of the simplex: it retains its apex and the portions of its lateral faces below the base. Its ordinary coordinate Euclidean volume is \(1/(2d!)\). For integers \(k\ge0\), let \(L_P(k)=|kP\cap\mathbb Z^d|\) and \(\Delta(k)=L_{F_G}(k)-L_{M_G}(k)\). Then
\[
\Delta(k)=\sum_{\substack{0\le j<k\\j\equiv k\pmod2}}\binom{d+j-1}{d-1},\qquad
\sum_{k\ge0}\Delta(k)z^k=\frac{z^2}{(1-z)^d(1-z^2)}.
\]
The minimal Ehrhart quasiperiod of \(F_G\) is exactly two. Its counting function is a polynomial in \(k\) plus \(2^{-(d+1)}(-1)^k\). The volume and the entire difference \(\Delta\) depend only on \(d\).

## Proof

Number the edge coordinates on the cycle cyclically as \(a_0,\ldots,a_{n-1}\); let \(b_1,\ldots,b_t\) denote the leaf edges, with \(b_\ell\) attached at vertex \(i(\ell)\). By the half-integral vertex characterization for fractional matching polytopes, the nonzero edges of a vertex consist of vertex-disjoint unit-weight matching edges and half-weight odd cycles. There is just one odd cycle, and no edge is disjoint from its vertices. The sole nonintegral vertex is therefore \(h=(1/2,\ldots,1/2,0,\ldots,0)\). All matching vectors satisfy \(\sum_i a_i\le(n-1)/2\), and \(h\) violates this inequality.

Put \(s_i=1-a_{i-1}-a_i-\sum_{\ell:i(\ell)=i}b_\ell\), with cyclic indices. The other degree inequalities (at the leaves) follow from nonnegativity and the cycle-vertex bounds. Since
\[
\sum_i s_i+\sum_\ell b_\ell=n-2\sum_i a_i,
\]
the region on the violating side is described in \((s,b)\) coordinates by nonnegativity and total less than one. To check that the whole region is feasible, put \(u_i=s_i+\sum_{\ell:i(\ell)=i}b_\ell\). Solving \(a_{i-1}+a_i=1-u_i\) gives each cycle coordinate as \(1/2\) plus an alternating signed sum of the \(u_i\), divided by two. Indeed for the cyclic shift \(P\), \((I+P)^{-1}=\tfrac12\sum_{r=0}^{n-1}(-P)^r\). Thus every rim coordinate is at least \((1-\sum_i u_i)/2\), nonnegative even on the base. The origin in \((s,b)\) gives the apex \(h\). A base vertex with unit coordinate \(s_i\) gives the alternating rim matching leaving vertex \(i\) unpaired. A base vertex with unit coordinate \(b_\ell\) gives that rim matching at \(i(\ell)\) and the associated leaf edge. All base vertices are therefore matching vectors. Clipping by the inequality leaves only integral vertices: a vertex off the clipping plane must already have been a vertex of \(F_G\), and vertices on the clipping plane are vertices of the base. The clipped polytope is \(M_G\).

The affine map from \((a,b)\) to \((s,b)\) has block triangular linear part of absolute determinant \(|\det(I+P)|=2\), since \(n\) is odd. Its inverse therefore maps the standard \(d\)-simplex of volume \(1/d!\) to a simplex of volume \(1/(2d!)\). Deleting a facet does not change this volume.

For \(k\ge1\), replace 1 in the slacks and cycle equations by \(k\). The total slack-and-leaf weight \(j\) must satisfy \(0\le j<k\). For integers \((s,b)\) in this range, the right side of the cycle equations has sum \(nk-j\). The lattice image of \(I+P\) is contained in the vectors of even coordinate sum, and both sublattices have index two; hence they are equal. Exactly the assignments with \(j\equiv k\pmod2\) have integral preimages. For each such \(j\) the nonnegative integral assignments number \(\binom{d+j-1}{d-1}\). At \(k=0\) both counts equal one and the empty sum gives zero as required. Summing with \(k=j+2r\), \(r\ge1\), gives the displayed generating function. In the form \(z^2/[(1-z)^{d+1}(1+z)]\), the coefficient of \(1/(1+z)\) is \(2^{-(d+1)}\); all remaining coefficients come from the pole at 1 and are polynomial in \(k\). Since \(M_G\) is a lattice polytope, its Ehrhart function is polynomial. This proves the claimed alternating term and excludes period one.

## Verification and scope

The accompanying `verify_matching_cap.py` uses the Python standard library. It enumerates feasible integer edge vectors and counts strict violations of the rim inequality for 47 graph-and-dilation cases, and reconstructs cap vertices in rational arithmetic. These are finite diagnostics; the proof above establishes the formulas in all stated dimensions. The theorem concerns leaves attached directly to the cycle, not arbitrary trees, even cycles, or multiple odd cycles, and gives the difference of the two counting functions rather than either polynomial separately.

## Relationship to prior work

The half-integral vertex theorem and the odd-set matching inequality are classical. Taking the line graph of the bare cycle identifies its matching cap with the fractional stable-set cap of the same odd cycle. The bare-cap slack argument, and hence its half-simplex volume, are known; see *Antiperiodic Brownian geometry of the odd-cycle integrality cap*, record `826a819e0b80`, proof §1. For a pendant edge, its variable splits one of those rim slacks into two nonnegative coordinates. The count above uses this split and tests the integer preimages in the enlarged lattice; it does not infer the decorated discrepancy just from the bare volume. Related parity statements for cyclic blocks (record `c9d98c9238ae`) or prescribed cycle capacities (record `4ce7355a2277`) concern models without these independent pendant coordinates. The comparison does not establish exhaustive priority.

### References

1. M. L. Balinski, half-integrality theorem for fractional matching polytopes (1965); see the [IPCO 2020 matching polytope notes](https://www.lse.ac.uk/ipco-2020/summer-school/Sanita-complete.pdf), fractional matching vertices section.
2. H. Guo and Vishvajeet N, *Deterministic approximation for the volume of the truncated fractional matching polytope*, [arXiv:2409.07283v1](https://arxiv.org/html/2409.07283v1).
3. S. Kafer, K. Pashkovich and L. Sanità, *On the Circuit Diameter of some Combinatorial Polytopes*, [arXiv:1709.09642v1](https://arxiv.org/html/1709.09642v1).
4. R. Ehrenborg, *The Ehrhart and face polynomials of the graph polytope of a cycle*, European Journal of Combinatorics **118** (2024), 103906, [doi:10.1016/j.ejc.2023.103906](https://doi.org/10.1016/j.ejc.2023.103906).
