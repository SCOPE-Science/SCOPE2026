# A universal simplex and Ehrhart parity correction for pendant-decorated odd-cycle matching polytopes

## Finding
Fix any odd \(n\ge3\). Attach \(t\ge1\) pendant edges arbitrarily to vertices of a simple cycle \(C_n\), allowing several leaves at the same cycle vertex. The resulting simple graph \(G\) has \(d=n+t\) edges. In the standard \(d\)-dimensional edge-coordinate lattice, write
\[
F_G=\{x\in\mathbb R_{\ge0}^{E(G)}:\ \sum_{e\ni v}x_e\le1\ \text{for every vertex }v\},
\qquad M_G=\operatorname{conv}\{\mathbf1_H:H\text{ a matching of }G\}.
\]
Denote the Ehrhart counts by \(L_P(k)=|kP\cap\mathbb Z^d|\) for integers \(k\ge0\).

**Theorem (universal integrality defect).** The set \(F_G\setminus M_G\), with its base removed, is a single full-dimensional open simplex. Its ordinary coordinate Euclidean volume equals \(1/(2d!)\) for every attachment pattern and every odd cycle length. More strongly,
\[
L_{F_G}(k)-L_{M_G}(k)
=\sum_{\substack{0\le j<k\\j\equiv k\;(\mathrm{mod}\;2)}}\binom{d+j-1}{d-1},
\qquad
\sum_{k\ge0}(L_{F_G}(k)-L_{M_G}(k))z^k
=\frac{z^2}{(1-z)^d(1-z^2)}.
\]
In particular, the minimal Ehrhart quasiperiod of \(F_G\) is exactly two. The alternating, parity-dependent constant term in its constituent-polynomial representation is precisely \(2^{-(d+1)}(-1)^k\). All these differences depend only on the number \(d\) of edges, not on the cycle size or the positions of the leaves. The unadorned odd cycle is a known base case; the assertion here is for at least one pendant edge.

## Assumptions and scope
The cycle has odd size \(n\ge3\), all additional edges are *pendant edges attached directly to cycle vertices*, and there are \(t\ge1\) such edges. This is a narrower graph class than arbitrary unicyclic graphs with hanging trees of positive depth. Coordinates are indexed by the \(d\) undirected edges, and volume is ordinary full-dimensional Euclidean volume (not normalized lattice volume). The graph's fractional matching polytope is taken without any extra degree truncation. The parity term refers to the unique partial fraction at the simple pole \(z=-1\), not to the highest-degree coefficient of the Ehrhart quasipolynomial.

## Proof
**1. The sole fractional vertex and the cutting inequality.** Enumerate the rim edges cyclically as \(a_0,\ldots,a_{n-1}\), and leaf edges as \(b_1,\ldots,b_t\), with leaf \(\ell\) attached at cycle vertex \(i(\ell)\). The standard half-integrality theorem for fractional matching vertices states that their positive coordinates equal one on a matching and one-half on vertex-disjoint odd cycles. As the only odd cycle of \(G\) is its rim, the only nonintegral vertex of \(F_G\) is
\[
h=(\underbrace{1/2,\ldots,1/2}_{n\ \mathrm{rim}},\underbrace{0,\ldots,0}_{t\ \mathrm{leaves}}).
\]
Every other vertex is a matching vector. In particular the odd-cycle inequality
\[
\sum_{i=0}^{n-1}a_i\le(n-1)/2
\]
holds at all integral vertices, but is violated by \(h\).

**2. Entire cut-off is a simplex.** Put
\[
s_i=1-a_{i-1}-a_i-\sum_{\ell:i(\ell)=i}b_\ell,\qquad i\pmod n.
\]
The nonnegative \(s_i\) are the degree slacks at rim vertices. The graph's other constraints are merely \(b_\ell\ge0\), since every leaf-degree upper bound follows from its rim-degree bound. Summing the equations gives
\[
\sum_i s_i+\sum_\ell b_\ell=n-2\sum_i a_i.
\]
Thus the cut-off region is exactly \(s_i,b_\ell\ge0\) with \(\sum_i s_i+\sum_\ell b_\ell<1\), provided its inverse image always has nonnegative rim coordinates. Define \(u_i=s_i+\sum_{\ell:i(\ell)=i}b_\ell\). The cyclic linear system \(a_{i-1}+a_i=1-u_i\) has a unique solution, as \(n\) is odd. Every solved coordinate has the form
\[
a_i=\frac12\left(1+\sum_{j=0}^{n-1}\varepsilon_{ij}u_j\right),\qquad\varepsilon_{ij}\in\{-1,1\},
\]
so it is bounded below by \((1-\sum_j u_j)/2>0\). Hence the entire standard open \(d\)-simplex in \((s,b)\) maps into the feasible relaxation. Its apex \((s,b)=0\) is \(h\). When one of its \(d\) coordinates equals one and the others zero, the rim edges alternate between zero and one, with one rim vertex unpaired; if the unit coordinate is a leaf variable, that unpaired vertex is matched to its leaf. Every vertex of the simplex base is therefore an integral matching indicator. Consequently clipping off \(h\) along the cycle inequality introduces only integral base vertices and leaves all other integral vertices intact. The clipped polytope is exactly \(M_G\), proving the simplex description.

The linear map \((a,b)\mapsto(s,b)\) has block-triangular determinant of absolute value \(\lvert\det(I+P)\rvert=2\), where \(P\) is the cyclic coordinate shift of odd order. Therefore the inverse Jacobian is \(1/2\). The standard \(d\)-simplex has volume \(1/d!\), so the missing Euclidean volume is \(1/(2d!)\).

**3. All-dilation lattice defect.** At dilation \(k\), write
\[
s_i=k-a_{i-1}-a_i-\sum_{\ell:i(\ell)=i}b_\ell.
\]
An integer point of \(kF_G\setminus kM_G\) must have nonnegative integral \(s_i,b_\ell\) with total \(j=\sum_i s_i+\sum_\ell b_\ell<k\). The odd-cycle incidence matrix \(I+P\) has determinant two, and its image in \(\mathbb Z^n\) is precisely the index-two sublattice of vectors with even coordinate sum. Since the vector of rim-edge equations has total sum \(nk-j\), and \(n\) is odd, the inverse rim-edge coordinates are integral if and only if \(j\equiv k\pmod2\). For each such integer \(j\), the number of nonnegative integral slack-and-leaf vectors of length \(d\) with total \(j\) is \(\binom{d+j-1}{d-1}\). This gives the stated exact lattice-point formula.

Summing over all possible \(j\) and writing \(k=j+2r\) with \(r\ge1\), the generating function is
\[
\sum_{j\ge0}\binom{d+j-1}{d-1}z^j\sum_{r\ge1}z^{2r}
=\frac{z^2}{(1-z)^d(1-z^2)}
=\frac{z^2}{(1-z)^{d+1}(1+z)}.
\]
The matching polytope is a lattice polytope and hence \(L_{M_G}(k)\) is a polynomial in \(k\). The displayed difference has a genuine simple pole at \(z=-1\) with coefficient \(\lim_{z\to-1}(1+z)\Delta(z)=2^{-(d+1)}>0\), producing precisely \(2^{-(d+1)}(-1)^k\). Its other pole is at \(z=1\), so its constituent quasipolynomials have period dividing two and not one. This proves minimal quasiperiod exactly two for \(F_G\).

## Verification
Run `python3 verify_matching_cap.py` using the Python standard library only. Its exact integer-arithmetic diagnostics directly enumerate lattice points of the fractional relaxation and check violations of the odd-cycle inequality for ten sample graph configurations, totaling 47 dilations. These include odd cycles of sizes three, five, seven and multiple nonisomorphic leaf distributions, and use all indicated feasible integer edge assignments rather than random samples. The checker also reconstructs every cap simplex vertex in rational arithmetic and tests integral matching properties, with the unique fractional apex handled separately. The theorem in arbitrary dimension follows from the proof, not from this finite enumeration.

## Relationship to prior work
The definition of the fractional matching polytope and volume-approximation motivation follow Guo and Vishvajeet (2024), whose full first version addresses *truncated* fractional matching polytopes via cluster expansions, not differences from matching hulls or lattice-point defects. The general matching-polytope framework and circuit questions occur in Kafer, Pashkovich and Sanità (2017). The classical half-integral vertex characterization is used, not claimed. The published odd-cycle integrality-cap result identifies a half-simplex volume for the *bare cycle*, and a published odd cyclic block-polytope theorem determines other period-two Ehrhart defects. The present family is distinguished by pendant edge variables occurring in only one cycle-vertex degree constraint, unlike cyclic block polytopes where each coordinate occurs in two neighboring constraints. Neither result implies attachment-pattern-independent full lattice differences for every positive pendant count.

## Limitations
The result does not apply to graphs with two odd cycles, even cycles or nontrivial hanging trees. The theorem gives the *difference* of two Ehrhart functions, not an independent formula for either complete Ehrhart polynomial. It gives no independent validation and no assertion of mathematical priority beyond the primary literature and research-record comparisons described. Some unindexed literature or different terminology could contain an equivalent theorem. The numerical checks cover only the stated finite cases; all-dimensional conclusions are analytic.

## References
1. H. Guo and Vishvajeet N, *Deterministic approximation for the volume of the truncated fractional matching polytope*, arXiv:2409.07283v1, first public 2024-09-11, https://arxiv.org/html/2409.07283v1.
2. S. Kafer, K. Pashkovich and L. Sanità, *On the Circuit Diameter of some Combinatorial Polytopes*, arXiv:1709.09642v1, first public 2017-09-27, https://arxiv.org/html/1709.09642v1; SIAM J. Discrete Math. 33 (2019).
3. Balinski's 1965 half-integrality theorem for fractional matching polytopes, also described in the publicly available IPCO 2020 summer-school matching-polytope notes: https://www.lse.ac.uk/ipco-2020/summer-school/Sanita-complete.pdf.
4. *Antiperiodic Brownian geometry of the odd-cycle integrality cap*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-antiperiodic-brownian-geometry-of-the-odd-cycle-integrality-cap--826a819e0b80.
5. *Exact parity degree and minimal quasiperiod of odd cyclic block polytopes*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-parity-degree-and-minimal-quasiperiod-of-odd-cyclic-block--c9d98c9238ae.
6. R. Ehrenborg, *The Ehrhart and face polynomials of the graph polytope of a cycle*, European J. Combin. 118 (2024), article 103906, https://doi.org/10.1016/j.ejc.2023.103906.
