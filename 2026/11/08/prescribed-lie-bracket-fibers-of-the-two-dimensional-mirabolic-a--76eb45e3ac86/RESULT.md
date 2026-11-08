# Prescribed Lie-bracket fibers of the two-dimensional mirabolic algebra over finite fields

## Finding

Let \(k=\mathbb F_q\) be any finite field, including even characteristic, and let \(\mathfrak p_2(k)=M_2(k)\ltimes k^2\) be the six-dimensional Lie algebra of affine-plane transformations. For arbitrary \(Z\in M_2(k)\) and \(w\in k^2\), define the ordered bracket-fiber size
\[
F_q(Z,w)=\#\{((A,u),(B,v))\in\mathfrak p_2(k)^2:[(A,u),(B,v)]=(Z,w)\}.
\]
If \(\operatorname{tr}Z\ne0\), then \(F_q(Z,w)=0\). If \(\operatorname{tr}Z=0\), exactly the following exhaustive cases occur:
\[
\boxed{F_q(Z,w)=\begin{cases}
q^8+2q^7+q^6-3q^5-q^4+q^3,& Z=0,\ w=0,\\
q^3(q^2-1)(q^3+q^2+q-1),& Z=0,\ w\ne0,\\
q^3(q^2-1)(q^2+q-1),&Z\ne0,\det Z=0,\ w\in\operatorname{im} Z,\\
q^3(q^2-1)^2,&Z\ne0,\det Z=0,\ w\notin\operatorname{im} Z,\\
q^5(q^2-1),&\det Z\ne0.
\end{cases}}
\]
The image incidence \(w\in\operatorname{im}Z\) includes \(w=0\). Every trace-zero target is represented, in every characteristic. The five fiber sizes are distinct for every prime power \(q\ge2\).

The numbers of targets in the five displayed cases, respectively, are
\[
1,\quad q^2-1,\quad q(q^2-1),\quad(q^2-q)(q^2-1),\quad q^2(q^3-q^2).
\]
Consequently, the bracket map has \(q^5\) represented targets and the exact commuting probability is
\[
\Pr([X,Y]=0)=q^{-4}+2q^{-5}+q^{-6}-3q^{-7}-q^{-8}+q^{-9}.
\]

## Assumptions and scope

The ground field is any \(\mathbb F_q\), with \(q\) a prime power. All matrices, vectors, pairs, and fibers are labeled; no division by conjugacy or automorphism groups is made. Elements are block matrices \(\begin{psmallmatrix}A&u\\0&0\end{psmallmatrix}\), and their bracket is
\[
[(A,u),(B,v)]=([A,B],Av-Bu),\qquad [A,B]=AB-BA.
\]
The field characteristic may be two; in that case a nonzero scalar trace-zero matrix is invertible and belongs to the last case, so no hidden characteristic exclusion is present. A nonzero trace-zero singular two-by-two matrix always has rank one and is nilpotent.

## Proof

**1. Matrix commutator fibers.** Write \(G_q(Z)=\#\{(A,B)\in M_2(k)^2:[A,B]=Z\}\). The bracket has trace zero. Every nonscalar two-by-two matrix \(A\) has centralizer \(kI+kA\), of vector-space dimension two, because a nonscalar two-by-two matrix is cyclic. The nondegenerate trace pairing on \(M_2(k)\) identifies
\[
\operatorname{im}(\operatorname{ad}_A)=(kI+kA)^\perp.
\]
For nonzero trace-zero \(Z\), exactly \(q^3-q\) nonscalar \(A\)'s satisfy \(\operatorname{tr}(AZ)=0\); there are \(q^3\) solutions to the nonzero trace-linear equation, and all \(q\) scalar matrices lie in that hyperplane. Each admitted nonscalar \(A\) has exactly \(q^2\) solutions \(B\) to \([A,B]=Z\). Therefore
\[
G_q(Z)=q^5-q^3\quad(Z\ne0,\operatorname{tr}Z=0).
\]
For \(Z=0\), each of the \(q\) scalar \(A\)'s has \(q^4\) commuting partners, and each of the \(q^4-q\) nonscalar matrices has \(q^2\), giving
\[
G_q(0)=q^6+q^5-q^3.
\]
These identities hold over all finite fields.

**2. Exceptional translation maps.** For fixed \(A,B\), the linear map \(\tau_{A,B}:k^2\oplus k^2\to k^2\), \((u,v)\mapsto Av-Bu\), has image \(\operatorname{im}A+\operatorname{im}B\). It has rank zero exactly when \(A=B=0\), rank one precisely when \(A\) and \(B\) have their images in a common fixed line \(\ell\) and are not both zero, and rank two otherwise. A rank-\(r\) instance has exactly \(q^{4-r}\) preimages of any \(w\) in its image and no preimages outside.

Fix a projective line \(\ell=ke\) and a basis beginning with \(e\). The matrices with images in \(\ell\) are uniquely \(A=e\alpha\) and \(B=e\beta\) for row functionals \(\alpha=(a,b)\), \(\beta=(c,d)\). Their commutator is \(e(0,ad-bc)\). Thus for a prescribed nonzero \(Z\) with \(\operatorname{im}Z=\ell\), the number of such pairs is the number of two-by-two matrices with specified nonzero determinant:
\[
K_q=\frac{|\mathrm{GL}_2(k)|}{q-1}=q(q^2-1).
\]
This case can occur only when \(Z\) is nonzero, trace-zero, singular, and necessarily rank one. With \(Z=0\), the number of such pairs *including* \(A=B=0\) for each fixed \(\ell\) is
\[
D_q=q^4-|\mathrm{GL}_2(k)|=q^3+q^2-q.
\]
Distinct projective lines give disjoint rank-one-image pairs; the zero pair is counted in every line and must be separated. There are \(q+1\) lines, so for \(Z=0\) there are exactly \((q+1)(D_q-1)\) rank-one translation maps and one rank-zero map.

**3. Nonzero matrix targets.** If \(\det Z\ne0\), a common-image line is impossible, so every matrix-commutator witness contributes \(q^2\) translations, giving \(q^2(q^5-q^3)=q^5(q^2-1)\). If \(Z\ne0\) is singular and trace zero, exactly \(K_q\) of the \(G_q(Z)\) matrix pairs have rank-one translation maps, all with image \(\operatorname{im} Z\). Hence
\[
F_q(Z,w)=q^2(G_q(Z)-K_q)+q^3K_q\mathbf1_{w\in\operatorname{im} Z},
\]
which simplifies to the third and fourth entries of the formula.

**4. Zero matrix target.** Let \(H_q=G_q(0)-1-(q+1)(D_q-1)\) be the number of commuting matrix pairs for which \(\tau_{A,B}\) is onto. If \(w\ne0\), exactly one line contains \(w\), and
\[
F_q(0,w)=q^2H_q+q^3(D_q-1).
\]
For \(w=0\), all \(q+1\) exceptional lines contribute and the zero pair contributes \(q^4\):
\[
F_q(0,0)=q^2H_q+q^3(q+1)(D_q-1)+q^4.
\]
Expanding gives the first two displayed formulas.

**5. Completeness and counts.** There are \(q^2-1\) nonzero nilpotent two-by-two matrices: each is determined by its image line \(\ell\) and a nonzero scalar in \(\operatorname{Hom}(k^2/\ell,\ell)\), yielding \((q+1)(q-1)\). The remaining nonzero trace-zero matrices, \(q^3-q^2\) in number, are invertible. For each nilpotent \(Z\), exactly \(q\) vectors \(w\) lie in its image and \(q^2-q\) do not. The target populations therefore have the five asserted values and sum to \(q^5\). Their fiber-size-weighted sum is \(q^{12}\), the total number of ordered inputs. The probability formula is \(F_q(0,0)/q^{12}\). This completes the proof.

## Verification

Two independent finite-field implementations were used. `check_aff2.py` enumerates every ordered input pair in \(\mathfrak p_2(\mathbb F_2)^2\) and \(\mathfrak p_2(\mathbb F_3)^2\), evaluates the defining six-coordinate bracket, and compares every possible target against the formulas. The respective enumerations contain \(4096\) and \(531441\) pairs. `check_aff2_extension.py` uses polynomial-basis arithmetic in \(\mathbb F_4\), exhaustively enumerates all \(65536\) matrix pairs, calculates translation images independently, and checks all \(1024\) targets, accounting for \(16777216\) ordered inputs. Both report the terminal markers in `verification_output.txt`. For reproducibility run `python check_aff2.py` and `python check_aff2_extension.py` with the Python standard library. Neither finite enumeration establishes the all-field theorem, which is proved above.

## Relationship to prior work

Kirillov [2] studies this exact mirabolic Lie-algebra family, explicitly writing the \(n=2\) coadjoint alternating form and its Pfaffian and analyzing open coadjoint orbits over the real numbers. That work is the structural starting point but does not state finite-field prescribed *element-bracket* fiber populations. Stasinski [3], building on Albert–Muckenhoupt, establishes matrix-commutator existence and trace constraints over principal ideal rings; it supplies established matrix surjectivity context, whereas the finite-field affine translation and nilpotent-image incidence require new counting. Britnell–Wildon [1] study similarity-class commutation and centralizers of full matrix algebras, not target-by-target bracket fibers in this semidirect product. The asserted contribution is the exact five-stratum distribution, not the existence of commutators, cyclic-matrix centralizer facts, or the pre-existing mirabolic construction. Historical completeness cannot be guaranteed; an unlocated stronger matrix-word-map or finite mirabolic enumeration result may imply the formulas.

## Limitations

The theorem concerns \(\mathfrak p_2(\mathbb F_q)\), not higher mirabolic ranks or groups of affine transformations; its inputs are Lie-algebra elements, not group elements. It does not classify simultaneous conjugacy orbits of witnesses or scheme-theoretic fibers. Published priority and independent review remain open. Computational corroboration is exhaustive only in the three tested fields and is not a substitute for the arbitrary-field proof.

## References

1. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811 (first submitted 2010-01-06), https://arxiv.org/abs/1001.0811.
2. A. A. Kirillov, *On the Mirabolic Lie Algebra* \(\mathfrak p_n\), Functional Analysis and Its Applications 48 (2014), 145–149, DOI:10.1007/s10688-014-0055-y; Russian version https://www.mathnet.ru/eng/faa3142.
3. A. Stasinski, *Commutators of trace zero matrices over principal ideal rings*, arXiv:1607.07205 (first submitted 2016-07-25), https://arxiv.org/abs/1607.07205.
4. A. A. Albert and B. Muckenhoupt, *On matrices of trace zero*, Michigan Math. J. 4 (1957), 1–3; matrix commutator-surjectivity antecedent, cited and explained in [3].
