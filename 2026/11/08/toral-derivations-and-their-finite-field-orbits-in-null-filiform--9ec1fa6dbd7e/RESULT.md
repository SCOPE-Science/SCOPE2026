# Toral derivations and their finite-field orbits in null-filiform Leibniz algebras

## Finding
For any field \(k\) of prime characteristic \(p\), any integer \(n\geq2\), and the null-filiform Leibniz algebra \(NF_n(k)\) defined below, every derivation \(D\) obeying \(D^p=D\) is either zero or conjugate under \(\operatorname{Aut}(NF_n(k))\) to \(cH\), for a *unique* \(c\in\mathbb F_p^\times\), where \(H(e_i)=i e_i\) (indices are interpreted in \(k\)). Each nonzero conjugacy class has rank \(n-\lfloor n/p\rfloor\). These \(p-1\) conjugacy classes remain distinct over every extension field.

Over \(k=\mathbb F_q\), \(q\) any power of \(p\), the exact population is
\[
\#\{D\in\operatorname{Der}(NF_n(\mathbb F_q)):D^p=D\}
=1+(p-1)q^{\,n-1-\lfloor(n-1)/p\rfloor}.
\]
Each nonzero class has \(q^{\,n-1-\lfloor(n-1)/p\rfloor}\) elements; its stabilizer has size \((q-1)q^{\lfloor(n-1)/p\rfloor}\). In particular, characteristic two has precisely \(1+q^{\lfloor n/2\rfloor}\) idempotent derivations, whereas in characteristic other than two the only derivation satisfying \(D^2=D\) is zero.

## Assumptions and scope
Fix a field \(k\) with \(\operatorname{char}(k)=p>0\) and an integer \(n\ge2\). The right Leibniz algebra \(NF_n(k)\) has ordered basis \(e_1,\ldots,e_n\) and products \([e_i,e_1]=e_{i+1}\) for \(1\le i<n\); all other basis brackets are zero. A derivation is a \(k\)-linear map satisfying \(D([u,v])=[D(u),v]+[u,D(v)]\). Composition powers are intended in \(D^p=D\). This is the restricted-toral equation (the natural restricted power on the derivation Lie algebra is composition). The rank statement is linear rank on \(NF_n\), and orbits concern conjugation by the full algebra automorphism group, not arbitrary invertible linear maps.

## Proof
**1. All derivations.** Since \(e_{i+1}=[e_i,e_1]\), the image of \(e_1\) determines a derivation. Put \(D(e_1)=\sum_{j=1}^n a_j e_j\). Induction using the derivation identity gives
\[
D(e_i)=i a_1 e_i+\sum_{t=1}^{n-i}a_{t+1}e_{i+t}\qquad(1\le i\le n).
\]
Conversely, every coefficient vector \((a_1,\ldots,a_n)\in k^n\) defines a derivation by this formula: products with right factor \(e_j\) for \(j\ge2\) vanish on both sides because \(D(e_j)\) has no \(e_1\)-component. Therefore \(\dim_k\operatorname{Der}(NF_n)=n\). Every derivation matrix is triangular with diagonal \(a_1,2a_1,\ldots,na_1\).

**2. Restriction of the diagonal and the zero case.** Suppose \(D^p=D\). The first diagonal entry gives \(a_1^p=a_1\); the roots of this equation in any field of characteristic \(p\) are exactly \(\mathbb F_p\). If \(a_1=0\), the matrix is strictly triangular and nilpotent. A nilpotent matrix satisfying \(D^p=D\) vanishes: iterating the equality yields \(D=D^{p^j}\) for all positive \(j\), and a sufficiently high power is zero.

**3. Conjugacy for nonzero diagonal.** Suppose \(a_1=c\in\mathbb F_p^\times\). The polynomial \(X^p-X\) has distinct roots in \(k\), so \(D\) is diagonalizable with spectrum contained in \(\mathbb F_p\). The polynomial
\[
P_c(D)=I-(D-cI)^{p-1}
\]
is projection onto its \(c\)-eigenspace: Fermat's identity makes it zero on each distinct \(\mathbb F_p\)-eigenspace. Write \(v=P_c(D)e_1\). Since the first coordinate of \(D\) is triangular with first diagonal entry \(c\), the first coordinate of \(v\) equals one. Hence \(v\) generates the whole Leibniz algebra. To see this explicitly, define \(v_1=v\) and \(v_{i+1}=[v_i,v]\). If the first coordinate of \(v\) is \(1\), each \(v_i\) equals \(e_i\) plus a combination of higher-index basis vectors; thus \((v_1,\ldots,v_n)\) is a basis and the assignment \(g(e_i)=v_i\) is an algebra automorphism. From \(Dv=cv\), induction shows \(D(v_i)=icv_i\) for every \(i\), so \(D=g(cH)g^{-1}\), with \(H(e_i)=ie_i\). The scalar \(c\) is determined by the induced map on the canonical one-dimensional quotient \(NF_n/[NF_n,NF_n]\), proving that the \(p-1\) nonzero classes are distinct.

**4. Automorphisms and finite-field orbit sizes.** Any vector \(w=\sum_{j=1}^n b_j e_j\) with \(b_1\ne0\) generates the algebra and determines a unique automorphism by \(g(e_1)=w\) and \(g(e_{i+1})=[g(e_i),w]\). Every automorphism arises this way; over \(\mathbb F_q\), the group has order \((q-1)q^{n-1}\). Commutation with \(cH\), with \(c\ne0\), is equivalent to \(cH(w)=c w\), or \(b_j=0\) for each \(j\not\equiv1\pmod p\). The free coordinates beyond \(b_1\) occur exactly at \(j=1+p,1+2p,\ldots\le n\), in number \(\lfloor(n-1)/p\rfloor\). Therefore the centralizer has order \((q-1)q^{\lfloor(n-1)/p\rfloor}\); orbit-stabilizer yields the claimed exact counts. The diagonal of \(cH\) vanishes exactly when \(p\mid i\), so the rank is \(n-\lfloor n/p\rfloor\).

**5. Idempotent derivations.** If \(p=2\), \(D^p=D\) is precisely \(D^2=D\), and the formula simplifies since \(n-1-\lfloor(n-1)/2\rfloor=\lfloor n/2\rfloor\). If \(p\ne2\) and \(D^2=D\), its first two diagonal entries \(a_1\) and \(2a_1\) must both be idempotent scalars (in \(\{0,1\}\)). If \(a_1\ne0\), then \(a_1=1\) and \(2a_1=2\notin\{0,1\}\), a contradiction. Hence \(a_1=0\), \(D\) is nilpotent, and idempotence forces \(D=0\).

## Verification
Run the accompanying self-contained standard-library script `verify_toral.py` with Python 3. It reconstructs the original bracket and derivation identity for all parameter matrices over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\), tests the \(p\)-th power equation, checks rank and explicit eigenvector-based conjugacy, and matches predicted counts in seventeen field/dimension configurations. It independently sweeps **all linear endomorphisms**, rather than only parameter-derived matrices, in six smaller configurations. The script prints the final marker `NULL_FILIFORM_P_TORAL_DERIVATIONS_PASS`; `toral_output.txt` holds the recorded output. Computations are finite corroboration, not an exhaustive proof for all \(n\) or \(q\).

## Relationship to prior work
Casas–Ladra–Omirov–Karimjanov (2012, arXiv:1202.5275) study null-filiform Leibniz nilradicals and a triangular derivation description in characteristic zero. Khudoyberdiyev–Omirov (2013, arXiv:1304.0126) develop deformations, including derivation calculations, in characteristic zero. Calderón–Camacho–Kaygorodov–Omirov (2017, arXiv:1708.01753, especially §3.1 and Theorem 4) classify group gradings of null-filiform Leibniz algebras and describe their automorphisms and torus; the equivalence of ordinary gradings and underlying diagonal patterns is not new here. These results supply much of the structural background.

The claim assessed here is specifically the positive-characteristic **composition equation** \(D^p=D\), its complete automorphism-conjugacy and finite-field element-population census, and the sharp characteristic-two idempotent boundary. A general classification of group gradings over characteristic zero does not itself state these finite-field operator counts; the prior automorphism-group formulas make this calculation accessible, however, and limit the originality claim. No assertion of a new general grading classification is made.

## Limitations
The theorem addresses the single null-filiform (one-generated) Leibniz family, not arbitrary filiform Leibniz algebras. It does not determine the scheme-theoretic structure or nonreduced multiplicities of the solution locus, or classify all derivation Jordan types. The available published comparisons do not prove historical uniqueness; more general unlocated results on restricted derivation Lie algebras or gradings may subsume its consequence. No independent audit has been performed.

## References
- Casas, J. M.; Ladra, M.; Omirov, B. A.; Karimjanov, I. A., *Classification of solvable Leibniz algebras with null-filiform nilradical*, first arXiv version 2012-02-23, https://arxiv.org/abs/1202.5275 .
- Khudoyberdiyev, A. Kh.; Omirov, B. A., *Infinitesimal deformations of null-filiform Leibniz superalgebras*, first arXiv version 2013-03-30, https://arxiv.org/abs/1304.0126 .
- Calderón, A. J.; Camacho, L. M.; Kaygorodov, I.; Omirov, B., *Abelian groups gradings on null-filiform and one-parametric filiform Leibniz algebras*, first arXiv version 2017-08-05, https://arxiv.org/abs/1708.01753 ; accessible full-text preprint https://www.math.uci.edu/~brusso/1708.01753.pdf .
- Jumayeva, *Derivations, Automorphisms and Local Derivations of Null-Filiform Leibniz Algebras* (2026), examined for the characteristic-zero derivation/automorphism formulas; only as supporting context.
