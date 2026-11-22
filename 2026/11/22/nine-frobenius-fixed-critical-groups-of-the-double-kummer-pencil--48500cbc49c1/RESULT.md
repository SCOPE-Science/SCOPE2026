# Nine Frobenius-fixed critical groups of the double Kummer pencil

## Finding

Let \(E\) and \(F\) be elliptic curves over an odd-characteristic finite field \(k=\mathbb F_q\). The reduced union \(D\) of the 24 classical double Kummer pencil curves on the minimal resolution \(X=\mathrm{Km}(E\times F)\) is a connected nodal curve with 24 rational geometric components, 32 nodes, and arithmetic genus \(9\). Its graph Jacobian (critical group) and the groups of elements fixed by geometric Frobenius are determined by the two Frobenius permutations of the respective elliptic two-torsion sets.

Write \(C_n=\mathbb Z/n\mathbb Z\). Since the identity point of \(E[2]\) or \(F[2]\) is rational, Frobenius acts on the remaining three two-torsion points as one of \(I\) (identity), \(T\) (transposition), or \(C\) (three-cycle). For every pair \((a,b)\) of types, the complete invariant factors of \(K(\Gamma)^{\mathrm{Frob}_q}\) are:

| Type on \(E[2]\) | Type on \(F[2]\) | Fixed critical group | Order |
| --- | --- | --- | ---: |
| \(I\) | \(I\) | \(C_2^4\oplus C_8^4\oplus C_{32}\) | \(2^{21}\) |
| \(I\) | \(T\) | \(C_2^2\oplus C_8^3\oplus C_{32}\) | \(2^{16}\) |
| \(I\) | \(C\) | \(C_8^2\oplus C_{32}\) | \(2^{11}\) |
| \(T\) | \(I\) | \(C_2^2\oplus C_8^3\oplus C_{32}\) | \(2^{16}\) |
| \(T\) | \(T\) | \(C_2^2\oplus C_8^2\oplus C_{32}\) | \(2^{13}\) |
| \(T\) | \(C\) | \(C_8\oplus C_{32}\) | \(2^8\) |
| \(C\) | \(I\) | \(C_8^2\oplus C_{32}\) | \(2^{11}\) |
| \(C\) | \(T\) | \(C_8\oplus C_{32}\) | \(2^8\) |
| \(C\) | \(C\) | \(C_2^2\oplus C_{32}\) | \(2^7\) |

In particular, \(K(\Gamma)\cong C_2^4\oplus C_8^4\oplus C_{32}\). A stronger equivariant statement is

\[
K(\Gamma)^{\operatorname{GL}_2(\mathbb F_2)\times\operatorname{GL}_2(\mathbb F_2)}
=\langle[H_0-C_{00}]\rangle\cong C_{32},
\]

where \(0\) denotes the respective elliptic identity. Thus every Frobenius-fixed group contains the same distinguished element of exact order \(32\), independent of the characteristic (provided it is odd), the field size, or the isogeny classes of \(E,F\).

## Assumptions and scope

The field \(k\) is finite with \(\operatorname{char}k\ne2\); \(E,F/k\) are arbitrary elliptic curves, not necessarily nonisogenous. The group here is the **geometric graph critical group**, equipped with the permutation of geometric irreducible components induced by arithmetic Frobenius. It is not the two-torsion subgroup of either elliptic curve, nor the Néron–Severi discriminant group of the K3 surface.

Write \(E[2](\bar k)=\{P_0,P_1,P_2,P_3\}\) and \(F[2](\bar k)=\{Q_0,Q_1,Q_2,Q_3\}\), with \(P_0=O_E\), \(Q_0=O_F\). Let \(H_i\), \(V_j\) be the proper transforms of the quotients of \(\{P_i\}\times F\) and \(E\times\{Q_j\}\), and let \(C_{ij}\) be the exceptional curve over the corresponding ordinary double point of the quotient. All are geometrically rational. The only pairwise intersections are one transverse point at \(C_{ij}\cap H_i\) and one at \(C_{ij}\cap V_j\), these two intersection points being distinct. The 16 exceptional components have valence two, so the curve is semistable/nodal but not a stable curve in the unmarked sense.

The representatives for \(I,T,C\) on labels \(0,1,2,3\) are \((0,1,2,3)\), \((0,2,1,3)\), and \((0,2,3,1)\), respectively. All nine ordered pairs are considered, regardless of whether a particular finite field supports both chosen conjugacy types in a particular prescribed elliptic family.

## Proof

**1. Geometry and Laplacian.** The 24 curves and their incidence follow from the product quotient local model at each point of \(E[2]\times F[2]\). At the corresponding ordinary double point, the two coordinate curves have distinct tangent branches on the exceptional \(\mathbb P^1\). Consequently the graph \(\Gamma\) is the graph obtained by inserting a new vertex \(C_{ij}\) in every edge of the complete bipartite graph on \(H_0,\dots,H_3\) and \(V_0,\dots,V_3\). It has \(24\) vertices and \(32\) edges, hence first Betti number \(32-24+1=9\). All normalized components have genus zero, giving arithmetic genus \(9\). Its integer Laplacian \(L\) is specified uniquely by

\[
L_{H_iH_i}=L_{V_jV_j}=4,\quad L_{C_{ij}C_{ij}}=2,\quad
L_{H_i C_{ij}}=L_{C_{ij}H_i}=L_{V_j C_{ij}}=L_{C_{ij}V_j}=-1,
\]

with every other off-diagonal entry zero. Delete the row and column of the Frobenius-fixed vertex \(C_{00}\) to obtain the invertible \(23\times23\) integer matrix \(R\). Then \(K(\Gamma)=\operatorname{coker}R\). As an independent order check, each edge of \(K_{4,4}\) has been subdivided once, which multiplies the spanning-tree number by \(2^9\); since \(\tau(K_{4,4})=4^6\), one has \(|K(\Gamma)|=2^{21}\).

**2. Frobenius and integral coinvariants.** Arithmetic Frobenius fixes \(P_0,Q_0\) and independently permutes the three nonzero points of each elliptic two-torsion group. Because \(\operatorname{GL}_2(\mathbb F_2)\cong S_3\), the three conjugacy types above are exhaustive. For a chosen type pair \((a,b)\), let \(P_{a,b}\) be the \(23\times23\) permutation matrix induced on vertices other than \(C_{00}\). Then \(R P_{a,b}=P_{a,b}R\), and the coinvariant group of \(K(\Gamma)\) is

\[
K(\Gamma)_{a,b}\cong
\operatorname{coker}\,[R\mid P_{a,b}-I_{23}].
\]

The canonical graph monodromy pairing \(K(\Gamma)\times K(\Gamma)\to\mathbb Q/\mathbb Z\) is perfect and invariant under graph automorphisms. Therefore \(K(\Gamma)^{P_{a,b}}\) is Pontryagin dual to \(K(\Gamma)_{a,b}\), hence the two finite abelian groups have the same invariant factors. This pairing argument is essential: invariants are not in general obtained by merely taking fixed integral divisors before quotienting by principal divisors.

**3. Exact orbit presentation.** Partition the \(23\) nonroot vertices into orbits under \(P_{a,b}\). Write one generator for each orbit. Summing rows of \(R\) over an orbit and choosing any representative column of each column-orbit defines an integral square matrix \(M_{a,b}\) of size equal to the number of nonroot orbits, and the preceding coinvariant group is exactly \(\operatorname{coker}M_{a,b}\). That orbit-summed columns are independent of the chosen representative follows from \(RP=PR\). Here are the exact determinantal and Smith certificates:

| Type \((a,b)\) | Number of nonroot orbits | \(|\det M_{a,b}|\) | Nonunit invariant factors |
| --- | ---: | ---: | --- |
| \((I,I)\) | 23 | \(2^{21}\) | \(2^4,8^4,32\) |
| \((I,T),(T,I)\) | 18 | \(2^{16}\) | \(2^2,8^3,32\) |
| \((I,C),(C,I)\) | 13 | \(2^{11}\) | \(8^2,32\) |
| \((T,T)\) | 15 | \(2^{13}\) | \(2^2,8^2,32\) |
| \((T,C),(C,T)\) | 10 | \(2^8\) | \(8,32\) |
| \((C,C)\) | 9 | \(2^7\) | \(2^2,32\) |

All these finite groups are two-primary, since their exact determinant orders are powers of two. The stated invariant factors follow by integral prime-local diagonalization of the explicit matrices. The attached, dependency-free `verify_kummer.py` constructs every matrix from the defining incidences and checks the table by *two separate integer presentations*: the square orbit presentation and the original \(23\times46\) presentation. It computes exact determinants by fraction-free elimination and independently calculates two-primary elementary divisors by unimodular row/column elimination modulo \(2^{32}\). The modulus exceeds every possible elementary divisor exponent, because the original graph critical group has order \(2^{21}\). The program checks every row and column orbit identity and every factor/order equality.

**4. The universal fixed generator.** The class of \(H_0-C_{00}\) is fixed by the entire \(S_3\times S_3\) label group. Identify it with the standard basis vector \(e_{H_0}\) of the reduced divisor lattice. There is an integral vector \(x\) satisfying \(Rx=32e_{H_0}\), with coordinates

\[
\begin{array}{c|c}
\text{coordinate}&x\text{ value}\\\hline
H_0&23\\ H_i\ (i>0)&15\\ V_0&9\\ V_j\ (j>0)&17\\
C_{0j}\ (j>0)&20\\ C_{i0}\ (i>0)&12\\ C_{ij}\ (i,j>0)&16.
\end{array}
\]

Since \(R\) is invertible, \(R^{-1}e_{H_0}=x/32\) is the unique rational preimage. Its \(H_0\)-coordinate is \(23/32\), which has exact denominator \(32\); hence this divisor class has exact order \(32\). Adding to \(R\) the four relation blocks for the generators \((T,I),(C,I),(I,T),(I,C)\) yields a \(23\times115\) integral presentation whose only nonunit two-primary Smith factor is \(32\). Since this is a quotient of a two-group, there is no odd torsion. Duality proves the full \(S_3\times S_3\) fixed subgroup is exactly \(C_{32}\), generated by \(H_0-C_{00}\). This completes the proof.

## Verification

Run `python3 verify_kummer.py` using Python 3.8 or newer; the program uses only the standard library. The final output must end with `FULL_S3xS3_FIXED_GROUP_C32_OK`, `UNIVERSAL_FIXED_C32_OK`, and `DOUBLE_KUMMER_PENCIL_FROBENIUS_NINE_GROUPS_OK`. The certificate rechecks all nine ordered cases and the special universal generator, without any precomputed matrix, database, or external file.

## Relationship to prior work

Clingher–Doran–Malmendier, arXiv:1510.06435v1 (2015), §4, describes the 24 curves of the classical double Kummer pencil on a product Kummer surface. That paper studies fibrations and hypergeometric periods and does not supply the nine finite equivariant critical groups. Glass, arXiv:1508.05401v1 (2015), studies graph critical groups with dihedral actions and gives \(K_{4,4}\) as an example, but does not study its complete one-edge subdivision or the present elliptic two-torsion label action; its Theorem 1.1 explicitly cannot determine full structure at primes dividing the group order, and all groups here are two-primary. D'Adderio–Le Borgne, arXiv:1608.01521v1 (2016), studies chip-firing ranks on \(K_{m,n}\), not these fixed groups. This distinction concerns implications and the exact graph, not merely different titles.

## Limitations

The statement is for odd-characteristic product Kummer surfaces and the specified 24-curve divisor. It does not classify all Kummer curves, characteristic two, nonproduct abelian surfaces, or arbitrary Galois automorphisms of a different divisor. The curve \(D\) is nodal but not stable without contracting its sixteen valence-two components. Its graph critical group can describe the geometric Néron component group in an appropriate separate regular semistable smoothing with unit node thicknesses, but the present result does **not** construct or assert existence of such a smoothing. Historical novelty is provisional pending independent literature and mathematical review.

## References

1. A. Clingher, C. Doran, A. Malmendier, *Special function identities from superelliptic Kummer varieties*, first public arXiv version 2015-10-21, https://arxiv.org/abs/1510.06435 , §4, especially p. 24.
2. D. Glass, *Critical Groups of Graphs with Dihedral Actions II*, first public arXiv version 2015-08-21, https://arxiv.org/abs/1508.05401 , Theorem 1.1 and Example 2.3.
3. M. D'Adderio, Y. Le Borgne, *The sandpile model on \(K_{m,n}\) and the rank of its configurations*, first public arXiv version 2016-08-04, https://arxiv.org/abs/1608.01521 .
