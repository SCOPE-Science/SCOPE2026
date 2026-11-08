# A parity transition in square-zero centralizers of unequal Jordan blocks

## Finding
Let \(k\) be any field, let \(n\ge2\), and set \(B=J_n(0)\oplus J_1(0)\) on \(k^{n+1}\). Let \(\mathcal Z_n\) be the **reduced** affine variety of all \(X\in M_{n+1}(k)\) such that \(XB=BX\) and \(X^2=0\). The following classification is valid after arbitrary field extensions and in every characteristic.

* For \(n=2h\), there is an isomorphism \(\mathcal Z_{2h}\cong \mathbb A^h\times\operatorname{Spec}k[b,c]/(bc)\). It has exactly two smooth geometrically irreducible components, each of dimension \(h+1\), meeting in an \(h\)-dimensional affine space. In particular it is reducible.
* For \(n=2h+1\), there is an isomorphism \(\mathcal Z_{2h+1}\cong\mathbb A^h\times\operatorname{Spec}k[x,b,c]/(x^2+bc)\). It is geometrically integral and normal of dimension \(h+2\). Its **reduced singular locus** is exactly \(\mathbb A^h\times\{0\}\), of codimension two.

For every finite field \(\mathbb F_q\), the rank multiplicities \(H_{n,q}(r)=\#\{X\in\mathcal Z_n(\mathbb F_q):\operatorname{rank}X=r\}\) are given exactly by
\[
H_{n,q}(0)=1,\quad H_{n,q}(1)=(q-1)(2q+1),
\]
\[
H_{n,q}(r)=(q-1)(2q-1)q^{r-1}\quad(2\le r\le\lfloor n/2\rfloor),
\]
with one extra rank when \(n=2h+1\):
\[
H_{2h+1,q}(h+1)=q^h(q-1)^2.
\]
All unlisted ranks have multiplicity zero. Consequently
\[
\#\mathcal Z_{2h}(\mathbb F_q)=q^h(2q-1),\qquad
\#\mathcal Z_{2h+1}(\mathbb F_q)=q^{h+2}.
\]
Thus a single length-one Jordan summand produces an alternating geometric behavior: the square-zero centralizer is reducible in even block length, whereas its odd-block counterpart is an integral normal quadric cone times affine space. The rank distributions refine that distinction arithmetically.

## Assumptions and scope
The notation \(J_n(0)\) means the nilpotent Jordan block of length \(n\). We identify its representation with the \(k[t]\)-module \(R=k[t]/(t^n)\) on which \(t\) acts by multiplication, and the one-dimensional block with \(k=R/(t)\). A centralizing matrix is precisely a \(k[t]\)-module endomorphism of \(R\oplus k\). The word *reduced* refers to the reduced underlying affine scheme of the two matrix equations; no statement is made about its possibly nonreduced scheme structure. Normality and smoothness are geometric statements, including positive characteristic. The rank enumerator counts actual matrices, not conjugacy classes.

## Proof
**Centralizer coordinates.** Every \(k[t]\)-linear endomorphism of \(R\oplus k\) has the unique form
\[
X=\begin{pmatrix}a(t)&b t^{n-1}\\c\,\epsilon&d\end{pmatrix},
\quad a(t)=\sum_{j=0}^{n-1}a_jt^j\in R,\quad b,c,d\in k,
\]
where \(\epsilon:R\to k\) extracts the constant coefficient. This follows from \(\operatorname{Hom}_{k[t]}(k,R)=k t^{n-1}\), \(\operatorname{Hom}_{k[t]}(R,k)=k\epsilon\), and \(\operatorname{End}_{k[t]}(R)=R\). Squaring gives diagonal blocks \(a(t)^2+bc\,t^{n-1}\) and \(d^2\), and off-diagonal blocks \(b(a_0+d)t^{n-1}\) and \(c(a_0+d)\epsilon\).

**Reduction to one equation.** Over any field extension, \(X^2=0\) forces \(d=0\) and \(a_0=0\); conversely, with these equalities its sole remaining condition is
\[
a(t)^2+bc\,t^{n-1}=0\quad\text{in }R.
\]
If the first nonzero coefficient of \(a(t)\) were at index \(j<\lfloor n/2\rfloor\), then the coefficient \(a_j^2\ne0\) of \(t^{2j}\) would be noncancellable since \(2j<n-1\). Hence \(a_j=0\) for every \(j<\lfloor n/2\rfloor\). This argument uses only that a field has no nonzero element with square zero; no characteristic restriction is needed.

When \(n=2h\), the remaining \(a(t)\) is an arbitrary element of \(t^hR\), its square vanishes, and the equation is \(bc=0\). The coefficients \(a_h,\ldots,a_{2h-1}\) are \(h\) free affine coordinates. When \(n=2h+1\), the remaining \(a(t)\) lies in \(t^hR\), its square has the single possibly nonzero term \(a_h^2t^{2h}\), and the equation is \(a_h^2+bc=0\); the other \(h\) coefficients are free. Since these descriptions hold over the algebraic closure and the indicated equations are geometrically reduced, they identify the reduced schemes over \(k\).

**Components and singularities.** The equation \(bc=0\) is the reduced union of the two coordinate hyperplanes. The polynomial \(x^2+bc\) is geometrically irreducible: considered as a polynomial linear in \(b\) over \(k[x,c]\), it is primitive and its generic root is \(-x^2/c\); any factorization of total degree two would force a linear factor and, in particular, a factor of both \(c\) and \(x^2\), which is impossible. Equivalently, it is a rank-three quadric not a union of two hyperplanes over any extension. Its reduced hypersurface singular locus is \(x=b=c=0\) in every characteristic (in characteristic two the derivative with respect to \(x\) vanishes, but \(b=c=0\) together with the equation still forces \(x=0\) at every geometric point). The hypersurface has dimension two and singular locus of codimension two; it is Cohen–Macaulay and regular in codimension one, hence normal by Serre's criterion. Taking a product with affine space yields the assertions.

**Ranks and field counts.** Suppose \(a(t)\ne0\), with its first nonzero term in degree \(v\). Multiplication by \(a(t)\) on \(R\) has image \(t^vR\) and rank \(n-v\). Its kernel \(t^{n-v}R\) is contained in \(tR\), so the functional \(c\epsilon\) vanishes on that kernel; appending the lower scalar coordinate does not increase the rank. The column contributed by the \(k\) summand is \((b t^{n-1},0)\). If \(b\ne0\) and \(c\ne0\), choose its preimage \(t^{n-1-v}\) under multiplication by \(a(t)\), corrected by a unit; the preimage has zero constant term because \(v\le n-2\) in this case (the only such case is the odd-block boundary \(v=h\)). If either \(b\) or \(c\) vanishes, containment of that column in the existing image is immediate. Therefore \(\operatorname{rank}X=n-v\) whenever \(a(t)\ne0\).

If \(a(t)=0\), the equation imposes \(bc=0\). The zero matrix corresponds to \(b=c=0\), and the other \(2(q-1)\) possibilities have rank one. For \(2\le r\le h\), there are \((q-1)q^{r-1}\) polynomials \(a(t)\) of valuation \(n-r\) and \(2q-1\) choices of \((b,c)\); the same formula applies for \(r=1\) before adding the \(a=0\) cases. In the odd case the additional valuation \(v=h\) has \((q-1)q^h\) choices for \(a(t)\) and \(q-1\) solutions \((b,c)\) to the nonzero product equation. These cases exhaust the locus, and their sums give the stated totals.

## Verification
The files `checker.py` and `checker_gf4.py` independently construct actual centralizer matrices, square them, and perform Gaussian elimination to calculate ranks. The first enumerates *every* centralizer element for the listed prime-field cases and tests the predicted ranks and totals, including non-square-zero elements in the search space. The second implements genuine arithmetic in \(\mathbb F_4\) and repeats exhaustive centralizer enumeration. Recorded outputs are in `checker_output.txt` and `gf4_output.txt`. Invoke `python checker.py` and `python checker_gf4.py` using Python 3.11 or later. No external dependencies are needed. These are finite corroborations; the proof above is uniform over arbitrary fields.

## Relationship to prior work
The nilpotent centralizer of a fixed nilpotent matrix is known to be irreducible, and much work concerns generic Jordan partitions of elements commuting with a fixed Jordan form. Basili–Iarrobino (2007 preprint, 2008 journal) and Košir–Oblak (2007 preprint) establish statements about this unrestricted nilpotent centralizer. They do not state the present reduced **square-zero** fiber geometry or its finite-field rank multiplicities. Bogdanić–Đurić–Koljančić–Oblak–Šivic (2022 preprint) study centralizers of two **equal-length** blocks and explicitly list unequal-length blocks as a further question. This result treats the sharply specified square-zero slice of the first unequal family, with lengths \((n,1)\), not the full general unequal-block problem. Equal-block and orthogonal/symplectic centralizer classifications concern different fixed operators and do not imply this formula. The novelty comparison is based on the specific cited theorems and searches; it is not an exhaustive proof of priority.

## Limitations
The theorem concerns only the Jordan type \((n,1)\) and the equation \(X^2=0\), not the full classification of all nilpotent commuting matrices or all unequal block lengths. It establishes the reduced variety but not nilpotents or multiplicities in the original equation scheme. The computations exhaust finite examples but cannot certify the all-field statement independently. More general results not located by the available literature searches could subsume the classification; historical priority and mathematical correctness have not been independently audited.

## References
1. R. Basili and A. Iarrobino, *Pairs of commuting nilpotent matrices, and Hilbert function*, arXiv:0709.2304, first submitted 2007-09-14, especially Section 1, Theorem 1.12, and Section 2. https://arxiv.org/abs/0709.2304
2. T. Košir and P. Oblak, *On pairs of commuting nilpotent matrices*, arXiv:0712.2813, first submitted 2007-12-17, especially Sections 1–2. https://arxiv.org/abs/0712.2813
3. D. Bogdanić, A. Đurić, S. Koljančić, P. Oblak, and K. Šivic, *Jordan structures of nilpotent matrices in the centralizer of a nilpotent matrix with two Jordan blocks of the same size*, arXiv:2212.08425, submitted 2022-12-16, especially Theorem 3 and Question 10. https://arxiv.org/abs/2212.08425
