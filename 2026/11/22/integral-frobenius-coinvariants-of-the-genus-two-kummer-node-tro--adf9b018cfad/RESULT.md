# Integral Frobenius coinvariants of the genus-two Kummer node–trope incidence

## Finding

Let \(C\) be a smooth geometrically connected curve of genus two over a finite field \(k=\mathbb F_q\) of odd characteristic, let \(X\) be the singular quartic Kummer surface of \(\operatorname{Jac}(C)\), and let \(N\) and \(T\) be the respective sets of its sixteen geometric nodes and sixteen geometric trope planes. Define the **formal incidence map**
\[
I:\mathbb Z[T]\longrightarrow\mathbb Z[N],\qquad [t]\longmapsto\sum_{n\in N\cap t}[n],
\]
and set \(Q=\operatorname{coker}(I)\). Geometric Frobenius \(F\) acts compatibly on \(N,T,Q\); its integral coinvariant group is \(Q_F=Q/(F-1)Q\).

Write \(\lambda\) for the partition of six recording the Frobenius cycle lengths on the Weierstrass points of \(C\). **For all eleven possible abstract cycle types**, the complete classification is
\[
\boxed{Q_F\cong(\mathbb Z/2\mathbb Z)^{a_\lambda}\oplus(\mathbb Z/4\mathbb Z)^{b_\lambda}\oplus\mathbb Z/3\mathbb Z.}
\]

| Weierstrass cycle partition \(\lambda\) | \(a_\lambda\) | \(b_\lambda\) | Elements of \(S_6\) of this type |
|---|---:|---:|---:|
| \((1,1,1,1,1,1)\) | 4 | 6 | 1 |
| \((2,1,1,1,1)\) | 2 | 5 | 15 |
| \((2,2,1,1)\) | 2 | 4 | 45 |
| \((2,2,2)\) | 4 | 3 | 15 |
| \((3,1,1,1)\) | 0 | 4 | 40 |
| \((3,2,1)\) | 0 | 3 | 120 |
| \((3,3)\) | 2 | 2 | 40 |
| \((4,1,1)\) | 2 | 2 | 90 |
| \((4,2)\) | 2 | 2 | 90 |
| \((5,1)\) | 0 | 2 | 144 |
| \((6)\) | 2 | 1 | 120 |

Every group has exponent twelve. The most informative distinction is between \(\lambda=(2,2,1,1)\) and \(\lambda=(2,2,2)\): **both the node scheme and the trope scheme separately have Frobenius orbit lengths \((1^4,2^6)\) in both cases**, yet the groups are respectively
\[
(\mathbb Z/2)^2\oplus(\mathbb Z/4)^4\oplus\mathbb Z/3
\quad\text{and}\quad
(\mathbb Z/2)^4\oplus(\mathbb Z/4)^3\oplus\mathbb Z/3.
\]
They are nonisomorphic despite having the same cardinality \(3072\). Both Weierstrass splitting types are attained by smooth genus-two curves over every finite field of odd cardinality.

## Assumptions and scope

All nodes and tropes are taken geometrically; no rational node or trope is assumed beyond the distinguished zero node. The Weierstrass branch divisor consists of six distinct geometric points on \(\mathbb P^1\) and Frobenius induces a permutation \(\sigma\in S_6\). The classification is conditional on its cycle partition: it does not assert that every one of the eleven cycle partitions is realized over every small field. The group \(Q\) is the cokernel of the **unsigned integral incidence map on free formal labels**; it is not a Picard, Brauer, Chow, critical, or Néron–Severi group.

## Proof

**1. Canonical combinatorial model.** Number the six geometric Weierstrass points by \(E=\{0,1,2,3,4,5\}\). Nodes are labelled by the empty set \(O\) and by the fifteen two-element subsets \(P_{ij}\). Tropes are labelled by the six singleton subsets \(T_i\) and the ten unordered partitions \(T_{A\mid E\setminus A}\) into triples. A singleton trope contains \(O\) and precisely the five nodes \(P_{ij}\) with \(j\ne i\). A triple-partition trope contains exactly the six nodes \(P_{ij}\) for which \(i,j\) lie in the same one of its two triples. These are the standard genus-two Kummer node–trope incidence relations. The permutations of the six Weierstrass labels act equivariantly on these sets.

**2. The geometric integral quotient and exponent.** Order nodes first by \(O\), then lexicographically by pairs, and order tropes first by the singleton labels, then lexicographically by triples containing \(0\). Let \(A\) be the resulting \(16\)-by-\(16\) zero–one incidence matrix. Every row and column sums to six, and every pair of distinct rows has exactly two common nonzero positions, so
\[
AA^{\mathsf T}=4\operatorname{Id}_{16}+2J_{16},\qquad
A(3A^{\mathsf T}-J_{16})=12\operatorname{Id}_{16}.
\]
Thus \(A\) is nonsingular over \(\mathbb Q\), and \(12Q=0\). Its exact Smith diagonal, obtained by integral elimination in the verifier, is
\[
\operatorname{diag}(1^6,2^4,4^5,12).
\]
In particular, \(Q\cong(\mathbb Z/2)^4\oplus(\mathbb Z/4)^6\oplus\mathbb Z/3\); its baseline invariant factors alone do not determine the Frobenius coinvariants.

**3. A finite presentation for every arithmetic form.** Let \(P_\sigma\) and \(R_\sigma\) be the node and trope permutation matrices induced by \(\sigma\). Their incidence compatibility \(P_\sigma A=AR_\sigma\) implies, by right exactness of coinvariants,
\[
Q_F\cong\mathbb Z^{16}/\operatorname{im}M_\sigma,\qquad
M_\sigma=\bigl[A\mid P_\sigma-\operatorname{Id}_{16}\bigr].
\]
Two permutations of the same cycle partition are conjugate in \(S_6\), hence produce integrally isomorphic presentations. The eleven representatives cover every possible Frobenius permutation, with conjugacy-class sizes displayed in the table (summing to \(720\)).

**4. Recovering the elementary divisors from exact finite determinants.** Since \(12Q_F=0\), its two-primary factors have orders at most four, and its three-primary factors have order at most three. If \(a\) and \(b\) count factors of orders two and four, then
\[
|Q_F/2Q_F|=2^{a+b},\qquad |Q_F/4Q_F|=2^{a+2b}.
\]
For \(m\in\{2,3,4\}\), each number \(|Q_F/mQ_F|\) is the index of the full-rank integer lattice generated by columns of \(\bigl[M_\sigma\mid m\operatorname{Id}_{16}\bigr]\). Its absolute Hermite determinant gives the index exactly. The independent Smith forms of the matrices \(M_\sigma\) agree with all residue indices. The complete residue certificate is:

| \(\lambda\) | \(|Q_F/2Q_F|\) | \(|Q_F/3Q_F|\) | \(|Q_F/4Q_F|\) |
|---|---:|---:|---:|
| \((1,1,1,1,1,1)\) | 1024 | 3 | 65536 |
| \((2,1,1,1,1)\) | 128 | 3 | 4096 |
| \((2,2,1,1)\) | 64 | 3 | 1024 |
| \((2,2,2)\) | 128 | 3 | 1024 |
| \((3,1,1,1)\) | 16 | 3 | 256 |
| \((3,2,1)\) | 8 | 3 | 64 |
| \((3,3)\) | 16 | 3 | 64 |
| \((4,1,1)\) | 16 | 3 | 64 |
| \((4,2)\) | 16 | 3 | 64 |
| \((5,1)\) | 4 | 3 | 16 |
| \((6)\) | 8 | 3 | 16 |

These indices uniquely recover the displayed pairs \((a_\lambda,b_\lambda)\), with exactly one order-three factor in each case. The persistence of that factor also follows without any computation: the coordinate-sum functional on node labels descends to a surjection \(Q_F\to\mathbb Z/3\), since every column of \(A\) has sum six and every column of \(P_\sigma-\operatorname{Id}\) has sum zero. The base group \(Q\) has only one order-three factor. Every row has \(b_\lambda\ge1\), proving exponent twelve.

**5. The arithmetic distinction is realized.** For \(q\ge3\) odd, there are \(q(q-1)/2\ge3\) distinct monic irreducible quadratic polynomials in \(\mathbb F_q[x]\). A squarefree sextic made from two distinct irreducible quadratics and two distinct linear polynomials has Frobenius partition \((2,2,1,1)\); a product of three distinct irreducible quadratics has partition \((2,2,2)\). In each case the smooth projective model \(y^2=f(x)\) has genus two. The verifier explicitly confirms that both node and trope orbit profiles coincide (four fixed labels and six two-cycles), while the groups have the two different decompositions above.

## Verification

Run `python verify_kummer_coinvariants.py` under Python 3 with SymPy. The program reconstructs the \(16\)-by-\(16\) incidence matrix from the incidence rules, verifies row and column degrees and the design identity, checks equivariance for **all \(720\) permutations of six letters**, groups them into exactly eleven conjugacy types, and computes exact integer Smith and Hermite normal forms. It checks the baseline Smith factors and the two equal-orbit/different-group cases. The execution must end with `PASSED: 11 classes, 720 permutations, 16x16 incidence, exact integral Smith forms`. All calculations use arbitrary-precision integers; no probabilistic enumeration or floating-point rank is involved. This finite exhaustion proves the stated eleven-class arithmetic presentation; the argument does not extrapolate a sample to an infinite set of fields.

## Relationship to prior work

The geometry and the full \(S_6\) action on sixteen Kummer nodes and sixteen tropes are classical: Ohashi (2009, Section 4) gives a fully equivariant incidence description, and Gonzalez-Hernandez (arXiv:2409.04532, v1 public 2024-09-06, Section 2.2) gives the same six singleton and ten triple-partition tropes over non-dyadic fields. Neither inspected section tabulates the **integral Frobenius coinvariant groups** of this incidence cokernel. The 2016 theorem of Ducey, Gerhard and Watson determines Smith groups for square-rook graph adjacency matrices, which display related \(16\)-by-\(16\) integral invariant factors at grid size four, but does not determine the Kummer-equivariant Frobenius action on this node–trope cokernel.

The previously studied Kummer **Göpel tetrad** incidence map has sixty columns, not sixteen tropes; it is not the map here. The previously studied Segre-cubic node–plane Frobenius coinvariant computation has ten nodes and fifteen planes and lacks the three-primary factor of this Kummer module. Even knowing the full Weierstrass cycle partition from finite-étale point counts does not supply the integral group presentations above. The new assertion is the exact arithmetic integral module classification and its nonisomorphic equal-orbit example, not the geometric configuration, the underlying permutation classes, or the general Smith-normal-form algorithm.

## Limitations

The calculations are confined to formal integral incidence groups for Jacobian Kummer quartics of smooth genus-two curves in odd characteristic. No identification with an arithmetic Picard group, Brauer group, descent obstruction for rational points, or geometric cohomology group is asserted. The classification does not claim eleven types are all realizable in every field; only the stated two types are separately constructed for all odd fields. Exact mathematical calculation and targeted prior-source comparison cannot exclude an older equivalent equivariant incidence computation under another terminology.

## References

1. A. Gonzalez-Hernandez, *Explicit desingularisation of Kummer surfaces in characteristic two via specialisation*, arXiv:2409.04532v1, first public 2024-09-06, especially Section 2.2. https://arxiv.org/abs/2409.04532 .
2. H. Ohashi, *Enriques surfaces covered by Jacobian Kummer surfaces*, Nagoya Math. J. **195** (2009), 165–186, especially Section 4. https://doi.org/10.1017/S0027763000009764 .
3. J. E. Ducey, J. Gerhard and N. Watson, *The Smith and Critical Groups of the Square Rook's Graph and its Complement*, Electron. J. Combin. **23**(4) (2016), #P4.9, Theorem 1.1. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v23i4p9 .
4. *The integral Göpel-tetrad lattice of a Kummer quartic*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-integral-g-pel-tetrad-lattice-of-a-kummer-quartic--2fe9c0537bec .
5. *Integral Frobenius coinvariants of the Segre cubic node–plane incidence*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-integral-frobenius-coinvariants-of-the-segre-cubic-node-plane-in--be1de342035c .
