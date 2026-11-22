# Eleven arithmetic fixed critical groups of the genus-two Kummer node–trope graph

## Finding

Let \(k=\mathbb F_q\) be a finite field of odd characteristic, and let \(C:y^2=f(x)\) be a smooth genus-two curve, where \(f\in k[x]\) is a separable polynomial of degree six. Its six geometric roots are the Weierstrass points of the finite branch divisor. On the Jacobian Kummer quartic, consider the **incidence graph** \(\Gamma\) whose vertices are its sixteen geometric nodes and sixteen trope conics and whose edges join incident node–trope pairs. This is the classical 32-vertex, 96-edge Kummer \((16_6)\) Levi graph. Let \(K(\Gamma)\) be its finite graph Jacobian (critical/sandpile group), not the Jacobian of \(C\).

The arithmetic Frobenius on the six roots induces a permutation \(\sigma\in S_6\) and an automorphism of \(K(\Gamma)\). The **complete classification of the fixed finite abelian group** \(K(\Gamma)^\sigma\) is as follows. In the table, \(n^a\) denotes \((\mathbb Z/n\mathbb Z)^{\oplus a}\) and an omitted exponent means one copy; *these are actual invariant factors, not merely primary-component sizes.*

| Frobenius cycle partition | Nontrivial invariant factors of \(K(\Gamma)^\sigma\) | Group order |
|---|---|---|
| \(1^6\) | \(2^4,4,16^4,32^9,96\) | \(3\cdot2^{72}\) |
| \(2\,1^4\) | \(2^2,4,16^2,32^7,96\) | \(3\cdot2^{52}\) |
| \(2^2 1^2\) | \(2^2,4,16^2,32^5,96\) | \(3\cdot2^{42}\) |
| \(2^3\) | \(2^5,16^3,32^4,96\) | \(3\cdot2^{42}\) |
| \(3\,1^3\) | \(4,32^5,96\) | \(3\cdot2^{32}\) |
| \(3\,2\,1\) | \(4,32^3,96\) | \(3\cdot2^{22}\) |
| \(3^2\) | \(2^2,4,16^2,32,96\) | \(3\cdot2^{22}\) |
| \(4\,1^2\) | \(2^3,16,32^2,96\) | \(3\cdot2^{22}\) |
| \(4\,2\) | \(2^3,16,32^2,96\) | \(3\cdot2^{22}\) |
| \(5\,1\) | \(4,32,96\) | \(3\cdot2^{12}\) |
| \(6\) | \(2^3,16,96\) | \(3\cdot2^{12}\) |

The types \(4,1,1\) and \(4,2\) have the same fixed group, so the eleven permutation classes yield exactly **ten distinct group isomorphism types**. Thus Frobenius types \((2,2,1,1)\) and \((2,2,2)\) have the **same fixed-group order but nonisomorphic fixed groups** (their numbers of elements of order dividing two differ). Likewise \((3,2,1)\) and \((3,3)\) have the same order but different invariant factors. In every case the three-primary factor is \(\mathbb Z/3\), even though the two-primary structure varies widely.

## Assumptions and scope

The genus-two curve is smooth, the characteristic is odd, and the hyperelliptic model is separable of degree exactly six. No genericity of the coefficients beyond separability is imposed. The eleven partitions describe the Galois conjugacy classes of the six roots; the theorem is conditional on whichever class occurs for the given curve and does not assert that every class is realized over every fixed finite field. The graph has vertex labels fixed geometrically, but the isomorphism type of its fixed subgroup is independent of the choice of root labeling and of the chosen Laplacian sink.

The word 'fixed' denotes the subgroup of Frobenius-invariant elements of the **geometric graph critical group**. It does not refer to the rational point group of the abelian-surface Jacobian, the torsion of a Néron–Severi lattice, or the connected Picard torus of the reduced divisor.

## Proof

**1. Geometric graph and Frobenius action.** Number the six roots \(0,1,2,3,4,5\). The sixteen nodes are \(N_0\) (the origin in the two-torsion) and \(N_{ij}\) for unordered pairs \(\{i,j\}\). The sixteen tropes are six odd theta tropes \(T_i\) and ten even theta tropes \(T_{A|A^c}\), indexed by unordered partitions into two triples. The incidence predicates, all inherited from the standard genus-two Kummer geometry, are:

- \(T_i\) contains \(N_0\) and exactly the five \(N_{ij}\) with \(j\ne i\).
- \(T_{A|A^c}\) contains exactly the six nodes \(N_{ij}\) for which \(\{i,j\}\subset A\) or \(\{i,j\}\subset A^c\).

Galois acts on every label by permuting root indices; it fixes \(N_0\). Let \(B\) be the resulting \(16\times16\) zero–one incidence matrix, with nodes ordered first \(N_0\) then all pairs in lexicographic order and tropes ordered first \(T_i\), then the ten triple partitions represented by the triple containing label zero. Every row and column of \(B\) sums to six, and \(BB^\mathsf T=4I_{16}+2J_{16}\). The graph Laplacian is

\[
L=\begin{pmatrix}6I_{16}&-B\\-B^{\mathsf T}&6I_{16}\end{pmatrix}.
\]

**2. A fixed-subgroup presentation.** The finite graph Jacobian is \(K(\Gamma)=\operatorname{Div}^0(\Gamma)/L\mathbb Z^{32}\). Choose the final trope as sink \(v\), put \(b_j=e_j-e_v\) for the other 31 vertices, and let \(M\) denote the \(31\times31\) reduced Laplacian (last row and column deleted). If \(p\) is the induced permutation of all 32 vertices, the action on degree-zero divisors in the \(b_j\) basis has integral matrix

\[
U_{ij}=\mathbf1_{\{p(j)=i\}}-\mathbf1_{\{p(v)=i\}},\qquad 0\le i,j<31.
\]

Hence the **coinvariant** graph Jacobian has an exact 31-by-62 integer presentation

\[
K(\Gamma)_{\sigma}\cong\operatorname{coker}[\,M\mid U-I_{31}\,].
\]

To recover the **fixed subgroup** rather than just the quotient, use the graph critical group's canonical nondegenerate symmetric monodromy pairing with values in \(\mathbb Q/\mathbb Z\). Every graph automorphism preserves it. It identifies \(K(\Gamma)\) equivariantly with its Pontryagin dual, so \(K(\Gamma)^\sigma\) is Pontryagin dual to \(K(\Gamma)_\sigma\). Finite abelian groups and their duals have the same invariant factors. Therefore the Smith factors of the displayed rectangular matrix are precisely the invariant factors of the asserted **fixed subgroup**. This argument does not presume fixed elements and coinvariants to be canonically the same subgroup.

**3. Eleven exact integral Smith normal forms.** Each of the eleven conjugacy types has the explicit representative obtained by successively cycling disjoint blocks of sizes given by its partition. The supplied `kummer_frobenius_certificate.json` contains eleven complete ordered sequences of elementary integer row and column operations taking its corresponding \(31\times62\) matrix \([M\mid U-I]\) to a positive Smith diagonal. Operations are swaps, adding integer multiples of distinct rows or columns, and row sign flips. Each has determinant \(\pm1\) on the appropriate free lattice, so the computed diagonal is an exact integer presentation invariant. The standalone `kummer_frobenius_verifier.py` independently reconstructs all eleven matrices from the six-root labeling, checks graph automorphisms, replays every elementary operation, verifies every off-diagonal is zero, and checks positivity, the divisibility chain, and all table orders.

**4. Checks distinguishing the groups.** The identity case agrees with the independent graph Laplacian spectral tree count: the \((16_6)\) design has Laplacian eigenvalues \(0,12,4^{\times15},8^{\times15}\), whence the Matrix–Tree Theorem gives \(3\cdot2^{72}\). In the \((2,2,1,1)\) case there are eleven nontrivial cyclic factors; in the \((2,2,2)\) case there are thirteen. Because both groups have order \(3\cdot2^{42}\), their distinct minimal generator counts show why counting Frobenius-invariant chips alone or knowing the group order does not determine this classification.

## Verification

Run `python3 kummer_frobenius_verifier.py kummer_frobenius_certificate.json` using Python 3 and its standard library. The expected output is `KUMMER_FROBENIUS_ALL_ELEVEN_INTEGRAL_FIXED_GROUPS_OK`. The checker rebuilds the incidence rules and root-permutation action rather than loading a stored incidence matrix; it checks exact equality of each transformed \(31\times62\) matrix with its claimed Smith diagonal. It also verifies the identity-class spanning-tree order independently from the diagonal. Finite examples are not substituted for the all-curve proof: the eleven verified operations cover all conjugacy types of \(S_6\), and every such curve has one of them.

## Relationship to prior work

The \((16_6)\) Kummer incidence configuration, its genus-two Weierstrass labeling and the geometric Kummer surface are classical and not claimed as new. Kumar's 2006 thesis and Malmendier's paper (first posted 2009) exhibit the relevant 16 node–16 trope geometry and its \(S_6\) labels. Earlier results also compute the complete **geometric** graph critical group \(K(\Gamma)\), without the eleven fixed-subgroup structures. A separate calculation of Frobenius cycles on Göpel tetrads is a different incidence-set invariant. These neither state nor imply the individual fixed-group invariant factors without further integral analysis. Related integral Frobenius-coinvariant studies of different cubic-surface and Fermat/Hermitian configurations do not furnish the Kummer group's \(31\times62\) Smith forms.

The fresh content here is exactly the **eleven-case arithmetic fixed-subgroup classification and the equal-order/nonisomorphic distinctions**, not the graph's total critical group, incidence matrix, or general duality principle. Full historic priority is not certified: an unindexed classical biplane, folded-six-cube, or graph-Jacobian calculation might give an equivalent result.

## Limitations

The theorem uses the ordinary (unweighted) geometric incidence graph. There is no asserted identification with the Jacobian of \(C\), the Néron–Severi discriminant of the Kummer resolution, a component group of any unspecified degeneration, or the \(k\)-points of a separate graph scheme. The classification is for odd characteristic only. Realizability of every cycle partition over every finite field is not proved. The exact integer-operation certificates are complete for the eleven finite matrices; historical novelty and independent expert mathematical review remain unverified.

## References

1. A. Kumar, *K3 surfaces of high rank*, Ph.D. thesis, Harvard University, May 2006, §5.5, pp. 52–53. https://web.mit.edu/abhinavk/www/thesis.pdf
2. A. Malmendier, *Kummer surfaces associated with Seiberg–Witten curves*, arXiv:0912.4774, first posted December 24, 2009, §2.2, p. 6. https://arxiv.org/abs/0912.4774
3. H. S. M. Coxeter, *Self-dual configurations and regular graphs*, Bull. Amer. Math. Soc. 56 (1950), 413–455.
4. E. W. Weisstein, *Kummer Graph*, MathWorld, https://mathworld.wolfram.com/KummerGraph.html.
