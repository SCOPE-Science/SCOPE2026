# Two-level commutator fibers of symmetric \(3\times3\) matrices over odd finite fields

## Finding
Let \(k=\mathbb F_q\), with \(q\) any odd prime power. Write \(\operatorname{Sym}_n(k)=\{X\in M_n(k):X^{\mathsf T}=X\}\) and \(\operatorname{Skew}_n(k)=\{C\in M_n(k):C^{\mathsf T}=-C\}\). For \(C\in\operatorname{Skew}_3(k)\), put
\[
F_q(C)=\#\{(X,Y)\in\operatorname{Sym}_3(k)^2:XY-YX=C\}.
\]
Then the **complete ordered-target fiber law** is
\[
\boxed{F_q(C)=\begin{cases}
q^9+q^8-q^5,&C=0,\\
q^9-q^5,&C\ne0.
\end{cases}}
\]
In particular, every skew-symmetric target occurs, and **all nonzero targets have precisely the same number of ordered witnesses**, irrespective of their rank or quadratic invariants. The commuting probability of two uniformly sampled symmetric matrices is \(q^{-3}+q^{-4}-q^{-7}\).

This two-level phenomenon has a dimension-four obstruction: for every odd prime power \(q\ge5\), the fiber function of the analogous commutator map \(\operatorname{Sym}_4(k)^2\to\operatorname{Skew}_4(k)\) **is not constant on its nonzero targets**. No assertion is made here about the dimension-four case \(q=3\).

## Assumptions and scope
All matrices are labeled, and each ordered pair is counted separately. The transpose is the ordinary coordinate transpose in the standard basis; no similarity or orthogonal-group quotient is taken. The field has odd characteristic. In dimension four, \(q\ge5\) is required to choose a nonzero scalar whose square is not one. The displayed counts are integers for all stated fields; the argument does not use a primitive root or any restriction on extension degree.

## Proof
**1. General Fourier identity.** For arbitrary \(n\ge2\) and odd \(q\), abbreviate \(S=\operatorname{Sym}_n(k)\), \(K=\operatorname{Skew}_n(k)\), \(s=n(n+1)/2\), and \(a=n(n-1)/2\). Equip \(K\) with the nondegenerate bilinear pairing \(\langle Z,C\rangle=\operatorname{tr}(ZC)\). Nondegeneracy follows because for skew matrices this equals \(-2\sum_{i<j}Z_{ij}C_{ij}\). Choose any nontrivial additive character \(\psi:k\to\mathbb C^\times\). For a target count \(F(C)=\#\{(X,Y)\in S^2:[X,Y]=C\}\), its Fourier transform is
\[
\widehat F(Z)=\sum_{C\in K}F(C)\psi(\operatorname{tr}(ZC))
=\sum_{X,Y\in S}\psi(\operatorname{tr}([Z,X]Y))
=q^{s+d(Z)},
\]
where \(d(Z)=\dim_k\{X\in S:[Z,X]=0\}\). Indeed \([Z,X]\) is symmetric, and the trace pairing on symmetric matrices is nondegenerate in odd characteristic; summing over \(Y\in S\) gives \(q^s\) precisely when \([Z,X]=0\), and zero otherwise. Fourier inversion on the additive group of \(K\) now determines all fibers from these dimensions.

**2. Three-dimensional skew centralizers.** Fix nonzero \(Z\in K=\operatorname{Skew}_3(k)\). Its rank is exactly two: a nonzero skew matrix has a nonzero principal two-by-two minor, while the determinant vanishes in odd dimension. Consequently \(Z^2\ne0\), since otherwise its two-dimensional image would lie in its one-dimensional kernel. Its minimal polynomial has degree three. To see this, a hypothetical monic quadratic relation \(Z^2+bZ+cI=0\) and its transpose give \(2bZ=0\), hence \(b=0\). Since \(Z\) is singular, \(c=0\), contradicting \(Z^2\ne0\). Linear or constant annihilating relations are also impossible. Therefore \(Z\) is cyclic, so its full matrix centralizer is exactly \(k[Z]=\operatorname{span}\{I,Z,Z^2\}\). A polynomial \(uI+vZ+wZ^2\) is symmetric if and only if \(v=0\). Thus \(d(Z)=2\) for every \(Z\ne0\), and \(d(0)=6\).

**3. Exact inversion.** Here \(s=6\) and \(a=3\), so \(\widehat F(0)=q^{12}\), whereas \(\widehat F(Z)=q^8\) for all nonzero \(Z\). Fourier inversion gives
\[
F(C)=q^{-3}\left(q^{12}+q^8\sum_{Z\in K\setminus\{0\}}\psi(-\operatorname{tr}(ZC))\right).
\]
The final character sum equals \(q^3-1\) if \(C=0\), and \(-1\) otherwise. This yields both asserted fiber formulas. The mass check is
\[
(q^9+q^8-q^5)+(q^3-1)(q^9-q^5)=q^{12}=|S|^2.
\]

**4. First obstruction.** In dimension four set \(J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\), and take \(t\in k^\times\) with \(t^2\ne1\), possible for \(q\ge5\). Define \(Z_1=J\oplus0_2\) and \(Z_2=J\oplus tJ\), both nonzero in \(\operatorname{Skew}_4(k)\). Writing a symmetric matrix in two-by-two blocks, commuting with \(Z_1\) forces its first diagonal block to be scalar and its off-diagonal block to vanish, while the final diagonal block is any symmetric two-by-two matrix. Hence \(d(Z_1)=1+3=4\). Commuting with \(Z_2\) forces both diagonal blocks to be scalar; its off-diagonal block \(B\) satisfies \(JB=tBJ\), and hence \((t^2-1)B=0\), so \(B=0\). Hence \(d(Z_2)=2\). The Fourier identity gives \(\widehat F(Z_1)=q^{10+4}\ne q^{10+2}=\widehat F(Z_2)\). If the target fiber were constant on all nonzero skew matrices, its Fourier transform would be constant on all nonzero dual frequencies. This contradiction proves the dimension-four obstruction.

## Verification
Two standalone programs are included. `check_symmetric_commutator.cpp` exhaustively checks all \(3^6\) symmetric matrices in each factor over \(\mathbb F_3\) by direct multiplication, thus checking all \(3^{12}\) ordered pairs and all \(3^3\) targets. For \(\mathbb F_5\) and \(\mathbb F_7\), it exhaustively enumerates every first symmetric matrix, computes the image of the linear commutator map on the six symmetric basis matrices, and adds the exact affine fiber \(q^{6-r}\) for each target in its image; all targets are checked. The output is recorded in `verification_output.txt`. `check_fourdim_boundary.py` computes, independently via modular row elimination, the dimensions of the symmetric centralizers of the two displayed skew matrices over \(\mathbb F_5\); its output is in `fourdim_output.txt`. Both programs have no third-party dependencies beyond a C++17 compiler and Python 3.

Reproduce with `g++ -std=c++17 -O2 check_symmetric_commutator.cpp -o check_symmetric_commutator && ./check_symmetric_commutator` and `python3 check_fourdim_boundary.py`. The computational checks cover prime fields of orders three, five and seven in dimension three, plus the dimension-four witness over the field of five elements; they are not substitutes for the arbitrary odd-prime-power proof.

## Relationship to prior work
The setting is the symmetric-pair decomposition of a general linear Lie algebra into its transpose-symmetric and transpose-skew spaces. Bulois, *Sheets of Symmetric Lie Algebras and Slodowy Slices* (first arXiv version 2009-06-21), develops type-AI orbit geometry and centralizers over algebraically closed characteristic-zero fields; its statements about sheets and Jordan classes do not enumerate prescribed finite-field bracket fibers. Lopatin, *Orthogonal invariants of skew-symmetric matrices* (arXiv 1004.3082, 2010-04-19), studies orthogonal conjugation invariants of skew matrices and their low-dimensional canonical forms; its full accessible text does not state the two-level fiber law for ordered symmetric factors. Grašič's *Zero product determined classical Lie algebras* (online 2010-04-16) concerns a universal property of bilinear maps on skew-symmetric Lie algebras, rather than ordered commutators of symmetric inputs; only accessible abstract/metadata were inspected. Fulman and Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields* (arXiv 1611.05499, first public 2016-11-16), count commuting pairs in full/general linear, unitary and symplectic Lie algebras, but not target-resolved brackets on the symmetric part of the orthogonal symmetric pair. These comparisons distinguish domains and conclusions; they are not claims of exhaustive historical novelty.

## Limitations
Odd characteristic is essential to the trace-pairing and transpose decomposition used here. The theorem does not classify dimension-four fibers, the dimension-four field of order three, higher-dimensional distributions, or conjugacy classes of witness pairs. No independent validation or comprehensive priority certification has been performed. A broader unidentified theorem on commutator Fourier transforms of symmetric pairs could imply the stated result.

## References
1. M. Bulois, *Sheets of Symmetric Lie Algebras and Slodowy Slices*, arXiv:0906.3881v1 (2009-06-21), https://arxiv.org/abs/0906.3881 .
2. A. A. Lopatin, *Orthogonal invariants of skew-symmetric matrices*, arXiv:1004.3082v1 (2010-04-19), https://arxiv.org/abs/1004.3082 .
3. M. Grašič, *Zero product determined classical Lie algebras*, Linear and Multilinear Algebra 58 (2010), 1007–1022, first online 2010-04-16, https://doi.org/10.1080/03081080903191672 .
4. J. Fulman and R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, arXiv:1611.05499v1 (2016-11-16), https://arxiv.org/abs/1611.05499 .
