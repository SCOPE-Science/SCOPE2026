# The first tangential-gradient blind harmonic on the 30 icosidodecahedral vertices

## Finding

Let \(V\subset\mathbb R^3\) be the twelve vertices of the regular icosahedron \(V=\{(0,\pm1,\pm\varphi),(\pm1,\pm\varphi,0),(\pm\varphi,0,\pm1)\}\), where \(\varphi=(1+\sqrt5)/2\). Let \(X\subset S^2\) consist of the thirty normalized midpoints of its thirty edges. Let \(\mathcal H_\ell\) be the complex vector space of homogeneous Euclidean-harmonic polynomials of degree \(\ell\), restricted to the unit sphere. For \(1\le\ell\le6\), define \(T_\ell H=(\nabla_{S^2}H(w))_{w\in X}\).

**Theorem.** The ranks of the derivative-only sampling maps \(T_1,\ldots,T_6\) are exactly \(3,5,7,9,11,12\). Consequently \(T_\ell\) is injective for each \(1\le\ell\le5\); at degree six, \(\ker T_6\) has dimension exactly one, spanned by the nonzero icosahedrally invariant harmonic \(F_6\) defined below. The degree-six defect is the first failure among positive harmonic degrees, even though 30 nodes provide up to 60 tangential coordinate measurements for a 13-dimensional harmonic space.

## Assumptions and scope

The nodes are the exact regular-icosahedron edge-midpoint orbit; all sampling weights are irrelevant for injectivity as long as positive. The data are *tangential gradients only*, not values or mixed jets. The theorem addresses **only** degrees \(1\) through \(6\); it makes no claim for higher degrees. Complex and real harmonic-space ranks coincide, since the matrix has real algebraic entries. Each \(\mathcal H_\ell\) has dimension \(2\ell+1\).

## Proof

**1. Exact geometry.** Every vertex \(v\in V\) has squared length \(q=\varphi+2\), and two distinct vertices are joined by an edge precisely when their dot product is \(\varphi\). For an edge \(\{u,v\}\), set \(w=(u+v)/(2\varphi)\). The golden-ratio relation \(\varphi^2=\varphi+1\) gives \(\lVert w\rVert^2=1\). There are exactly 30 such \(w\), forming the icosidodecahedral vertices.

**2. An explicit invariant sextic.** Put \(R^2=X_1^2+X_2^2+X_3^2\), \(q=\varphi+2\), and \(t_v=v\cdot X\). Define the homogeneous degree-six polynomial
\[
F_6(X)=\sum_{v\in V}\Big(231t_v^6-315q t_v^4R^2+105q^2t_v^2R^4-5q^3R^6\Big).
\]
Each summand equals \(16q^3R^6 P_6(t_v/(\sqrt q R))\), with \(P_6(s)=(231s^6-315s^4+105s^2-5)/16\). The solid zonal harmonics are harmonic, so \(F_6\in\mathcal H_6\). The icosahedral rotation group permutes \(V\), hence fixes \(F_6\). Every edge-midpoint direction \(w\in X\) is an axis of an order-two rotational symmetry. That rotation fixes \(w\) and acts by minus the identity on \(T_w S^2\); invariance forces \(\nabla_{S^2}F_6(w)=0\). Thus \(F_6\in\ker T_6\). The exact specialization \(\varphi\mapsto23\in\mathbb F_{101}\), which respects \(\varphi^2-\varphi-1=0\), gives \(F_6(1,0,0)\equiv85\pmod{101}\). Therefore \(F_6\ne0\), and \(\dim\ker T_6\ge1\).

**3. Exact modular lower-rank certificate.** Form for each degree \(\ell\) an integer-coefficient basis of the kernel of the degree-\(\ell\) polynomial Laplacian, using the monomials \(X_1^aX_2^bX_3^c\) in lexicographic iteration \(a=0,\ldots,\ell\), \(b=0,\ldots,\ell-a\), and \(c=\ell-a-b\). Clear each rational nullspace basis vector's denominators. For a basis polynomial \(H\), the three coordinate rows at each node \(w\) are \(\partial_j H(w)-\ell H(w)w_j\), since \(H\) is homogeneous and \(\lVert w\rVert=1\). List vertices, edges, nodes, rows and columns in exactly the algorithmic order of the accompanying `verify_h3.py` checker.

All matrix entries lie in \(\mathbb Z[\varphi,1/(2\varphi)]\), so reducing \(\varphi\mapsto23\) modulo 101 is legitimate. For degrees 1 to 6, the following actual row-index sets (zero-based, in the order built by the checker) and initial column sets \(0,\ldots,r-1\) give nonzero square minors:

| Degree | Claimed lower rank \(r\) | Selected row indices | Determinant modulo 101 |
|---|---:|---|---:|
| 1 | 3 | `0,1,3` | 10 |
| 2 | 5 | `0,1,3,4,6` | 46 |
| 3 | 7 | `0,1,4,3,6,7,9` | 22 |
| 4 | 9 | `0,1,3,4,7,9,6,10,12` | 60 |
| 5 | 11 | `0,1,3,4,6,7,9,10,12,15,13` | 5 |
| 6 | 12 | `0,1,3,4,6,7,9,10,15,16,18,19` | 61 |

The checker builds the exact matrices rather than trusting the table, verifies all six determinants, and independently reports the full modular ranks \(3,5,7,9,11,12\). Nonzero minors after reduction imply equally large ranks over \(\mathbb Q(\varphi)\) and \(\mathbb C\); reduction is used only for rank **lower bounds**. For degrees 1 through 5 the lower bounds equal \(\dim\mathcal H_\ell=2\ell+1\). For degree six, the symmetry-forced nonzero kernel supplies the upper bound \(\operatorname{rank}T_6\le12\), and the 12 by 12 minor supplies the reverse inequality. This proves the complete theorem.

## Verification

Execute `python verify_h3.py` with Python 3 and `sympy` installed. The checker (a) constructs all 12 original vertices and 30 exact edges, (b) proves the unit-length relation algebraically, (c) builds homogeneous harmonic polynomial bases from Laplacian nullspaces, (d) reduces the gradient matrices into \(\mathbb F_{101}\), (e) verifies ranks and explicit nonzero minor determinants, (f) verifies \(F_6(1,0,0)=85\) modulo 101, and (g) checks vanishing of all 90 coordinate components of the tangential gradient of \(F_6\) modulo 101. Symmetry and the zonal-harmonic identity in the proof, **not** the finite-field tests alone, establish the exact global kernel assertion.

## Relationship to prior work

Allasia, Cavoretto and De Rossi (2017) study general Hermite–Birkhoff interpolation for scattered manifold data and motivate derivative evaluations, without providing the present exact derivative-only nullity on this polyhedron. Baez (2023) describes the 30-point edge-midpoint geometry and its exceptional symmetries, not its harmonic gradient ranks. The classical icosahedral invariant-harmonic literature, including Cohan (1958), already supplies degree-six invariant harmonics; **existence of such an invariant is not claimed as new**. The specific first positive-degree failure, its exact one-dimensional kernel, and the full six-degree rank profile are the contributions. Earlier results on scalar point-value sampling at these or different sites do not imply the present derivative-only ranks.

## Limitations

No stability/condition number is calculated; injectivity does not imply good conditioning. Higher harmonic degrees are unclassified. The rank certificates are exact over a finite field but are used solely for lower bounds; the special invariant supplies the independent upper bound. Full historical priority remains uncertain, particularly because Cohan's 1958 full text could not be consulted despite an accessible abstract; a previously unstated consequence of character tables or generic Hermite interpolation could overlap the result. No independent mathematical audit is asserted.

## References

1. G. Allasia, R. Cavoretto, A. De Rossi, *Hermite-Birkhoff interpolation on scattered data on the sphere and other manifolds* (first posted 2017-05-02), https://arxiv.org/abs/1705.01032.
2. J. C. Baez, *The Icosidodecahedron* (posted 2023-09-26), https://arxiv.org/abs/2309.15774.
3. N. V. Cohan, *The spherical harmonics with the symmetry of the icosahedral group*, Math. Proc. Cambridge Philos. Soc. 54 (1958), 28–38, https://doi.org/10.1017/S0305004100033156 (only indexed extract accessible).
4. *Discriminant of the Icosahedral Group*, AMS Visual Insight (2016-05-15), https://blogs.ams.org/visualinsight/2016/05/15/discriminant-of-the-icosahedral-group/ (classical degree-six invariant context).
