# Three extension degrees recover genus-three Frobenius from parity-separated theta characteristics

## Finding

**Theorem.** Let \(C\) be a smooth, projective, geometrically connected curve of genus \(3\) over a finite field \(\mathbb F_q\) of odd characteristic. Write \(J=\operatorname{Jac}(C)\), and let \(O_n\) and \(E_n\) be the respective numbers of odd and even geometric theta characteristics fixed by the \(n\)-th power of arithmetic Frobenius. Then the six integers
\[
 (O_1,E_1,O_2,E_2,O_3,E_3)
\]
uniquely determine the conjugacy class of Frobenius on \(J[2]\) in \(\operatorname{Sp}_6(\mathbb F_2)\). They consequently determine the two entire theta-characteristic finite-étale zeta functions, the complete cycle partitions on the \(28\) odd and \(36\) even characteristics, and the Frobenius cycle structure on the \(63\) nonzero geometric \(2\)-torsion points of \(J\).

The cutoff of **three** extension degrees is optimal for the stated universal theorem. For every odd \(q\) there are smooth genus-three hyperelliptic curves whose eight geometric Weierstrass branch points have Frobenius partitions \((7,1)\) and \((5,3)\); their corresponding pairs of theta counts are equal through degree two, but not degree three:
\[
\begin{array}{c|ccc}
\text{branch partition}&(O_1,E_1)&(O_2,E_2)&(O_3,E_3)\\\hline
(7,1)&(0,1)&(0,1)&(0,1)\\
(5,3)&(0,1)&(0,1)&(3,1).
\end{array}
\]

A complete reproducible table for all \(30\) symplectic Frobenius classes accompanies the proof. One degree yields \(18\) distinct signatures, two yield \(24\), and three yield all \(30\).

## Assumptions and scope

The characteristic of \(\mathbb F_q\) is different from \(2\); no assumption of nonhyperellipticity or rational theta characteristics is made. A geometric theta characteristic is an isomorphism class of degree-two line bundles \(\vartheta\) over \(\overline{\mathbb F}_q\) with \(\vartheta^{\otimes2}\simeq\omega_C\). Its parity is \(h^0(C,\vartheta)\bmod2\). Since multiplication by two on the Jacobian is étale, the sets of geometric theta characteristics form finite étale schemes of sizes \(28\) and \(36\) over the base field. By “Frobenius conjugacy class” we mean the conjugacy class in the symplectic group acting on the six-dimensional \(\mathbb F_2\)-space \(J[2](\overline{\mathbb F}_q)\); it is not a claim to reconstruct the curve or its Weil polynomial.

The Riemann–Mumford quadratic-refinement theorem identifies theta characteristics naturally and Galois-equivariantly with quadratic forms polarizing the Weil pairing on \(J[2]\). This identification is stated, for instance, as Theorem 5.1 in Bruin–Poonen–Stoll (2016). Odd and even correspond to Arf invariants one and zero respectively.

## Proof

**1. Explicit symplectic theta actions.** Choose a symplectic basis and write \(V=\mathbb F_2^3\oplus\mathbb F_2^3\), with elements \(v=(a,b)\). Let
\[
 B((a,b),(c,d))=a\cdot d+b\cdot c,\qquad Q(a,b)=a\cdot b.
\]
Every quadratic refinement of \(B\) is uniquely \(Q_u(v)=Q(v)+B(u,v)\) for \(u\in V\), and its Arf invariant is \(Q(u)\). Thus the \(28\) labels with \(Q(u)=1\) and the \(36\) labels with \(Q(u)=0\) model the two theta schemes.

For a symplectic matrix \(A\), there is a unique \(d_A\in V\) such that
\[
 B(d_A,e_i)=Q(Ae_i)+Q(e_i)\qquad (1\le i\le6).
\]
Direct substitution proves that the induced action on quadratic-refinement labels is
\[
 u\longmapsto A(u+d_A).
\]
Indeed \(Q(A^{-1}v)+Q(v)=B(Ad_A,v)\), so the pullback of \(Q_u\) under \(A^{-1}\) equals \(Q_{A(u+d_A)}\). This permutation preserves the Arf invariant. Hence its odd and even cycle partitions determine exactly the theta Frobenius spectra.

**2. Exhaustive exact group certificate.** The included C++17 source enumerates \(\operatorname{Sp}_6(\mathbb F_2)\) by breadth-first closure under the eight symplectic transvections associated with the six basis vectors and the two vectors encoded as \(3\) and \(6\) in the six-bit convention in the source. It obtains
\[
 |\operatorname{Sp}_6(\mathbb F_2)|=2^9(2^2-1)(2^4-1)(2^6-1)=1{,}451{,}520.
\]
Each generated matrix is a product of transvections and hence symplectic. Reaching the full independently known group order proves exhaustive enumeration, rather than sampling. Each matrix acts on all \(64\) refinements by the derived formula; the source checks preservation of parity. The certificate aggregates all elements according to their two cycle partitions and finds precisely \(30\) different joint spectra.

The independently tabulated group has exactly \(30\) conjugacy classes (ATLAS of Finite Group Representations, class \(S_6(2)\)). A joint spectrum is constant on a conjugacy class. Since \(30\) distinct joint spectra are attained and there are only \(30\) classes, each spectrum belongs to exactly one conjugacy class. As an extra check, the resulting spectrum frequencies agree as a multiset with the ATLAS class sizes.

**3. Reconstruction from three extension degrees.** For any permutation with \(c_d\) cycles of length \(d\), the number of fixed points of its \(n\)-th power is
\[
 N_n=\sum_{d\mid n}d\,c_d.
\]
Applying this formula separately to each odd/even cycle partition in the full \(30\)-row certificate, the numbers of distinct truncated signatures for degrees \(1\), \(1\) through \(2\), and \(1\) through \(3\) are respectively \(18\), \(24\), and \(30\). Thus the six stated numbers uniquely identify the row and therefore the underlying symplectic conjugacy class. Subsequent counts for every degree are read off using the same fixed-cycle formula, and the finite-étale zeta functions are \(\prod_d(1-T^d)^{-c_d}\).

**4. Optimality by actual smooth curves.** On a genus-three hyperelliptic curve in odd characteristic, let \(D\) be the hyperelliptic degree-two divisor class, so \(K_C\sim2D\), and let \(w_1,\ldots,w_8\) be the Weierstrass points. The \(28\) distinct classes \(w_i+w_j\) for \(i<j\) are odd theta characteristics. The even classes are \(D\) itself and the \(35\) classes \(w_i+w_j+w_k+w_l-D\), where the four-subsets and their complements define the same class. Indeed \(2w_i\sim D\), \(\sum_{i=1}^8 w_i\sim4D\), and the unique degree-two pencil is \(D\); these give theta relations, parity, completeness, and the complementary identification. This is an equivariant description for Frobenius on branch points. The included independent symmetric-eight enumeration establishes the two \(\mathfrak S_8\)-cycle types \((7,1)\) and \((5,3)\) have equal parity-separated fixed counts for the first two powers, but different third counts as displayed above. Over every finite field of odd order, monic irreducible polynomials of degrees \(1\), \(3\), \(5\), and \(7\) exist; take a product of degrees \(7+1\) and another of degrees \(5+3\). Their squarefree degree-eight equations \(y^2=f(x)\) define smooth genus-three hyperelliptic curves with exactly the claimed splitting types. Thus no uniform reconstruction from the first two extensions is possible even among genuine curves.

## Verification

Run \(\texttt{python3 verify_theta_certificate.py}\) with Python 3 and a C++17 compiler installed. The script compiles and runs \(\texttt{verify_sp6_theta.cpp}\), recreates the complete matrix group and checks each of the thirty records against \(\texttt{theta_frobenius_30_spectra.csv}\); it also independently enumerates the \(22\) symmetric-eight branch partitions using \(\texttt{verify_hyperelliptic_theta.py}\). The expected final marker is `VERIFIED_GROUP_1451520_CLASSES_30_PREFIX_18_24_30_SHARP_3`. The output CSV encodes a cycle multiset as dot-separated cycle lengths, and includes each class's number of group elements and six truncated fixed-count invariants. These exact finite computations exhaust the finite symplectic group; they are not a claim to enumerate all genus-three curves.

## Relationship to prior work

The Riemann–Mumford theta/quadratic-refinement identification and the odd-theta Galois geometry are classical. Bruin, Poonen and Stoll (2016), Theorem 5.1 and Section 12, state these correspondences and show how the Galois action on bitangents gives the symplectic action for nonhyperelliptic genus-three curves. Glass (1980) studies the genus-three symplectic theta configuration; ATLAS tabulates the group and its 30 conjugacy classes; Braden and Disney-Hogg (arXiv v1, April 15, 2024) treat orbits of theta characteristics under curve automorphisms using related affine actions. These ingredients are explicitly prior work, not newly claimed.

The separately assessed contribution is the **joint, universal, sharp degree-three Frobenius reconstruction theorem**, including a fully reproducible 30-profile certificate. The hyperelliptic degree-two collision is an already-established special-case phenomenon and is used here to prove optimality of the universal all-curves statement, not claimed as a separate new result. In the primary material inspected, no statement giving the exact \(18,24,30\) separation and this sharpness construction was identified. The possibility of an equivalent result implicit in older character tables or in unindexed papers remains an originality risk.

## Limitations

The theorem reconstructs the mod-two Frobenius conjugacy class, not the full \(\ell\)-adic representation, curve isomorphism class, or Hasse–Weil polynomial. The table contains all abstract symplectic classes; it does **not** assert that all thirty arise as Frobenius classes of genus-three curves over any fixed field. The sharpness examples, by contrast, are realized by actual smooth curves for every odd \(q\). 

## References

1. N. Bruin, B. Poonen and M. Stoll, *Generalized explicit descent and its application to curves of genus 3*, Forum of Mathematics, Sigma (2016), especially Theorem 5.1 and Section 12. Full open text: https://math.mit.edu/~poonen/papers/genus3.pdf.
2. H. W. Braden and L. Disney-Hogg, *Orbits of Theta Characteristics*, arXiv:2404.09890, first version April 15, 2024, especially Section 2 and its affine theta action: https://arxiv.org/abs/2404.09890.
3. J. Glass, *Theta constants of genus three*, Compositio Mathematica 40 (1980), pp. 123–137: https://www.numdam.org/article/CM_1980__40_1_123_0.pdf.
4. ATLAS of Finite Group Representations, class \(S_6(2)\) / \(\operatorname{Sp}_6(2)\), conjugacy-class data and permutation representations: https://brauer.maths.qmul.ac.uk/Atlas/v3/clas/S62/.
