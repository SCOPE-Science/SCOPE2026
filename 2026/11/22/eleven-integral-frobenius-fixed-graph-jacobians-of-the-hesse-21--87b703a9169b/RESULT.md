# Eleven integral Frobenius-fixed graph Jacobians of the Hesse 21-curve boundary

## Finding
Let \(S\) be the rational elliptic surface obtained by blowing up the nine base points of the classical Hesse pencil of plane cubics over an algebraically closed field of characteristic different from three. Let \(D\) be the reduced union of the nine exceptional sections and the twelve irreducible components of the four triangular singular fibers. The geometric dual graph \(\Gamma\) has 21 vertices, 48 ordinary edges and first Betti number 28.

Write \(C_n=\mathbb Z/n\mathbb Z\) and let \(K(\Gamma)=\operatorname{Div}^0(\Gamma)/\operatorname{im}\Delta\) be the graph Jacobian. The underlying group, **not claimed as new**, is
\[
K(\Gamma)\cong C_3^2\oplus C_{21}^{8}.
\]
The geometric affine symmetries form \(G=\operatorname{AGL}_2(\mathbb F_3)\), of order 432, containing the Hessian projective subgroup of order 216 as the determinant-one subgroup. The theorem classifies \(K(\Gamma)^g\) for **all eleven** conjugacy classes of \(G\).

In the following table, \(A=(a,b,c,d)\) means the matrix \(\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\) over \(\mathbb F_3\), \(t=(u,v)\), and the representative acts by \(x\mapsto Ax+t\). The class size is its cardinality inside the 432-element group; \(r_3,r_7\) are the dimensions of the respective primary fixed groups over \(\mathbb F_3\) and \(\mathbb F_7\).

| Class | Size | \(\det A\) | Order | Representative \(A\) | \(t\) | \((r_3,r_7)\) | Exact fixed group |
|---|---:|---:|---:|---|---|---|---|
| 1 | 36 | 2 | 2 | \((0,1,1,0)\) | \((0,0)\) | \((6,5)\) | \(C_3\oplus C_{21}^5\) |
| 2 | 72 | 2 | 6 | \((0,1,1,0)\) | \((0,1)\) | \((2,1)\) | \(C_3\oplus C_{21}\) |
| 3 | 54 | 2 | 8 | \((0,1,1,1)\) | \((0,0)\) | \((0,1)\) | \(C_7\) |
| 4 | 54 | 2 | 8 | \((0,1,1,2)\) | \((0,0)\) | \((0,1)\) | \(C_7\) |
| 5 | 54 | 1 | 4 | \((0,1,2,0)\) | \((0,0)\) | \((2,2)\) | \(C_{21}^2\) |
| 6 | 72 | 1 | 6 | \((0,1,2,1)\) | \((0,0)\) | \((2,2)\) | \(C_{21}^2\) |
| 7 | 24 | 1 | 3 | \((0,1,2,2)\) | \((0,0)\) | \((4,4)\) | \(C_{21}^4\) |
| 8 | 48 | 1 | 3 | \((0,1,2,2)\) | \((0,1)\) | \((4,2)\) | \(C_3^2\oplus C_{21}^2\) |
| 9 | 1 | 1 | 1 | \((1,0,0,1)\) | \((0,0)\) | \((10,8)\) | \(C_3^2\oplus C_{21}^8\) |
| 10 | 8 | 1 | 3 | \((1,0,0,1)\) | \((0,1)\) | \((4,2)\) | \(C_3^2\oplus C_{21}^2\) |
| 11 | 9 | 1 | 2 | \((2,0,0,2)\) | \((0,0)\) | \((6,4)\) | \(C_3^2\oplus C_{21}^4\) |

The eleven classes give eight distinct finite abelian groups. Both order-eight classes have no nonzero invariant three-primary torsion, but retain exactly one seven-primary cyclic group. Moreover,
\[
K(\Gamma)^{\mathbb F_3^2\rtimes\operatorname{SL}_2(\mathbb F_3)}=0,
\qquad K(\Gamma)^G=0,
\]
although every individual group element fixes a nonzero critical class. The two order-eight classes have identical cycle partitions on both the 21 curve components and the 48 nodes, as well as identical fixed critical groups; these three invariants do not distinguish them.

## Assumptions and scope
The graph theorem holds for the classical 21-component geometric Hesse boundary in every characteristic different from three and for every automorphism induced by an affine transformation of \(\mathbb F_3^2\). The nine exceptional curves are indexed by the affine points \(p\in\mathbb F_3^2\). The twelve fiber curves are indexed by affine lines \(\ell_{j,c}\), the three parallel lines in each of four directions \(j\). Every point component meets the four affine-line components containing its label; the three components of each direction form a triangle. There are no other component intersections.

For a Frobenius-stable form over \(k=\mathbb F_q\), geometric Frobenius acts by some \(g=(A,t)\in G\) and the table gives the abstract group of fixed geometric graph-critical classes. When the nine base points are the flex/three-torsion torsor of a smooth cubic over \(\mathbb F_q\), the determinant satisfies \(\det A\equiv q\pmod3\) by the Weil pairing. This is a necessary constraint, not a realization theorem for all classes over a specified field. The result concerns the graph critical group; it does not identify it with the Néron component group of the elliptic fibration itself.

## Proof
**Geometry and automorphisms.** Artebani--Dolgachev [1, Sections 1--2] identify the nine flex points with \(\mathbb F_3^2\), the twelve Hesse lines with all four parallel classes of affine lines, and the four triangular singular fibers after blowing up. The stated incidence description follows. A point vertex has degree four and a line vertex degree five; hence every graph automorphism preserves the bipartition into these two vertex types. Their incidence subgraph is the affine plane of order three, whose entire affine-collineation group is \(\operatorname{AGL}_2(\mathbb F_3)\) of order 432. Each affine collineation preserves parallel classes and therefore the four added triangles. The full geometric graph action is thus the stated affine group.

**Integral Jacobian.** Let \(L\) be the \(21\times21\) graph Laplacian, with four on the nine point-vertex diagonal entries and five on the twelve line-vertex diagonal entries; entries are \(-1\) exactly on edges. Delete the first point row and column to obtain \(B\) of size \(20\times20\). Exact integer elimination gives \(\det B=3^{10}7^8\), and direct calculation shows every entry of \(21B^{-1}\) is integral. Therefore \(K(\Gamma)=\operatorname{coker}B\) has order \(3^{10}7^8\) and exponent dividing 21. Every primary component is elementary abelian, so the stated group \(C_3^2\oplus C_{21}^8\) follows. An independent integer Smith normal form yields diagonal nonunits \((3,3,21,21,21,21,21,21,21,21)\).

**Frobenius coinvariants and fixed groups.** For \(g\in G\), write \(P_g\) for its integral \(20\times20\) action on the degree-zero divisor basis \([v]-[v_0]\), for all vertices \(v\ne v_0\). In that basis, its \(v\)-column is the coefficient vector of \([g(v)]-[g(v_0)]\). It preserves the image of the graph Laplacian. Thus the coinvariant group has the concrete presentation
\[
K(\Gamma)_g\cong\operatorname{coker}[\,B\mid P_g-I_{20}\,].
\]
The graph-monodromy pairing [2, Theorem 3.4] is perfect and invariant under every graph automorphism. Therefore \(K(\Gamma)^g\) is the Pontryagin dual of \(K(\Gamma)_g\), and the two groups have the same invariant factors.

For \(p\in\{3,7\}\), define \(r_p(g)=20-\operatorname{rank}_{\mathbb F_p}[\,B\mid P_g-I_{20}\,]\). Since the quotient exponent divides 21, these ranks determine its complete isomorphism type:
\[
K(\Gamma)^g\cong C_3^{\max(r_3-r_7,0)}\oplus C_7^{\max(r_7-r_3,0)}\oplus C_{21}^{\min(r_3,r_7)}.
\]
There are precisely 48 invertible matrices over \(\mathbb F_3\) and nine translations, giving 432 graph actions. Direct conjugation within this explicitly enumerated group partitions them into eleven classes of sizes \(1,8,9,24,36,48,54,54,54,72,72\), summing to 432. Exact modular Gaussian elimination calculates \(r_3\) and \(r_7\) for **each of the 432 actions**, agrees within every class, and gives the table. Independent integer Smith calculations of all eleven representatives, repeated after deleting a different Laplacian row and column, give the same invariant factors.

Finally, two independent translation generators and two elementary matrices generate the determinant-one subgroup. The augmented matrix with their action differences has no nonunit Smith factor, so its common fixed group is zero by the same perfect pairing. Adding a determinant-minus-one generator cannot increase the common invariant subgroup. The two distinct order-eight representatives have distinct matrix traces in \(\mathbb F_3\) and hence cannot be conjugate, whereas direct examination of their induced vertex and edge permutations gives the same cycle lengths. This establishes every assertion.

## Verification
Run `python hesse_boundary_verify.py` with Python 3.10 or newer and SymPy 1.11 or newer. The script constructs all 21 vertices and 48 edges from the affine-plane definition, computes the exact determinant, checks the integral inverse bound, enumerates all 432 affine actions and their eleven conjugacy classes, calculates modular ranks for every group element at both primes, independently calculates the eleven integer Smith forms using two deleted vertices, and verifies the common Hessian fixed subgroup. Successful execution ends with `HESSIAN_216_INVARIANTS_TRIVIAL; FULL_AFFINE_432_INVARIANTS_TRIVIAL`.

## Relationship to prior work
Artebani--Dolgachev [1] provide the Hesse-pencil geometry, the nine flexes, the twelve lines, and the Hessian symmetry group; those are not new. Anema--Top--Tuijp [3] study Hesse pencils and equivalent 3-torsion Galois representations, without tabulating the 21-curve graph critical-group actions. Shokrieh [2] gives the general graph-monodromy pairing needed to convert coinvariant presentations to fixed-group factors, not any table for this graph. Previous nonequivariant computations of the same graph and the published Hesse rational elliptic surface Zariski-chamber classification [4] address, respectively, its ordinary critical group and its negative-definite divisor supports, neither its eleven affine-equivariant fixed groups. The exact integral Frobenius table, vanishing of the full Hessian invariants, and two indistinguishable order-eight incidence spectra are the asserted contribution.

## Limitations
The table classifies abstract affine symmetry classes, not the existence of every arithmetic twist over every finite field. It applies to the geometric graph and its action, not automatically to Néron component groups; any such interpretation requires a separately specified proper regular semistable model with the appropriate node thicknesses. No priority claim is made against inaccessible or unindexed prior equivariant graph calculations. The computations are exhaustive for the finite affine group but do not address different curve configurations or characteristic three.

## References
1. M. Artebani and I. Dolgachev, *The Hesse pencil of plane cubic curves*, first public version November 19, 2006, [arXiv:math/0611590](https://arxiv.org/abs/math/0611590), Sections 1--2.
2. F. Shokrieh, *The Monodromy Pairing and Discrete Logarithm on the Jacobian of Finite Graphs*, first public version July 27, 2009, [arXiv:0907.4764](https://arxiv.org/abs/0907.4764), Theorem 3.4.
3. A. Anema, J. Top and A. Tuijp, *Hesse Pencils and 3-Torsion Structures*, first public version August 31, 2017, [arXiv:1708.09745](https://arxiv.org/abs/1708.09745), Sections 1--3.
4. *The Zariski-chamber polynomial of the Hesse rational elliptic surface*, [published indexed research record](https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-zariski-chamber-polynomial-of-the-hesse-rational-elliptic-su--ad77c7e792a1), same curve configuration with a different invariant.
