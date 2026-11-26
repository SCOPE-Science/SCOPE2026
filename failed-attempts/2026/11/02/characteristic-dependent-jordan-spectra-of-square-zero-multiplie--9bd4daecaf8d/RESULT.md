# Characteristic-dependent Jordan spectra of square-zero multipliers on a two-variable Artin complete intersection

## Finding
Let \(k\) be any field, \(n\ge 2\), and \(A_n=k[x,y]/(x^2,y^n)\). For \(f\in A_n\) with \(f^2=0\), let \(m_f\) denote multiplication by \(f\) on the \(2n\)-dimensional vector space \(A_n\). Its Jordan type is \((2^r,1^{2n-2r})\), where \(r=\operatorname{rank}_k(m_f)\). Every \(r\in\{0,\ldots,n\}\) occurs.

For any finite field \(k=\mathbb F_q\), write \(C_{n,q}(r)\) for the number of square-zero \(f\) for which \(\operatorname{rank}(m_f)\le r\), and let \(s=\lfloor r/2\rfloor\) and \(e=r+s-n\). For \(0\le r\le n\), the complete cumulative distribution is
\[
C_{n,q}(r)=
\begin{cases}
q^{r+s},&\operatorname{char}k=2,\\
q^{r+s},&\operatorname{char}k\ne2,\ e\le0,\\
q^n+e(q^n-q^{n-1}),&\operatorname{char}k\ne2,\ e>0.
\end{cases}
\]
Set \(C_{n,q}(-1)=0\). The exact number with Jordan type \((2^r,1^{2n-2r})\) is \(C_{n,q}(r)-C_{n,q}(r-1)\). In particular, the total number of square-zero multipliers (including zero) equals \(q^{n+\lfloor n/2\rfloor}\) in characteristic two and \(q^n+\lfloor n/2\rfloor(q^n-q^{n-1})\) in odd characteristic.

There is a geometric refinement valid over every field. The **reduced** locus of square-zero elements of multiplication rank at most \(r\) is a single linear affine space of dimension \(r+s\) in characteristic two. In odd characteristic it is a single such linear space when \(e\le0\); when \(e>0\), it has exactly \(e+1\) distinct linear irreducible components, all dimension \(n\). With components indexed by \(i=n-r,n-r+1,\ldots,s\), the pairwise intersection of components \(i<j\) has dimension \(n-(j-i)\). The earliest rank where the characteristic-dependent formulas differ is \(\lceil 2(n+1)/3\rceil\).

## Assumptions and scope
Write \(R=k[y]/(y^n)\), and express uniquely \(f=a+xb\) with \(a,b\in R\). Define \(\nu(c)=\min\{i:[y^i]c\ne0\}\) for \(c\ne0\), and \(\nu(0)=n\); put \(u=\nu(a)\), \(v=\nu(b)\). The finite-field statements hold for arbitrary prime-power \(q\), including nonprime fields. Geometric components refer to the reduced affine variety after extension to an algebraic closure; no assertion about the defining nonreduced scheme is made. The restrictions \(n\ge2\), \(0\le r\le n\) and characteristic conditions are part of the theorem.

## Proof
**Square-zero equations.** Since \(x^2=0\),
\[
(a+xb)^2=a^2+2xab.
\]
In the principal Artin ring \(R\), \(a^2=0\) if and only if \(u\ge\lceil n/2\rceil\). If the characteristic is odd, \(2ab=0\) is equivalent to \(u+v\ge n\). In characteristic two the second constraint is automatic. These are both necessary and sufficient.

**Multiplication rank.** In the \(R\)-module decomposition \(A_n=R\oplus xR\), the matrix of multiplication by \(f\) is
\[
M_f=\begin{pmatrix}a&0\\b&a\end{pmatrix}.
\]
Its image-length over \(R\), equal to its \(k\)-rank, is
\[
\boxed{\operatorname{rank}_k(m_f)=\max\{2(n-u),\ n-v\}.}
\]
To see this, if \(v\ge u\) then \(b\) is divisible by \(a\), so elementary operations reduce \(M_f\) to \(\operatorname{diag}(a,a)\), giving rank \(2(n-u)\). If \(v<u\), write \(a=y^u a_0\), \(b=y^v b_0\) with \(b_0\) a unit. Elementary operations over the chain ring put \(M_f\) in Smith form with factors of valuations \(v\) and \(2u-v\), where a factor valuation at least \(n\) represents zero. Its image length is \((n-v)+\max(0,n-(2u-v))=\max\{n-v,2(n-u)\}\). The cases \(a=0\) or \(b=0\) follow directly from the displayed matrix and the convention \(\nu(0)=n\).

**Characteristic two.** For a square-zero element, \(u\ge\lceil n/2\rceil\). The additional rank restriction is equivalent to \(u\ge n-s\) and \(v\ge n-r\). Thus the reduced locus consists of the coefficient-linear subspace
\[
\{a\in y^{n-s}R,\ b\in y^{n-r}R\}
\]
of dimension \(s+r\). Over \(\mathbb F_q\) it has \(q^{s+r}\) elements.

**Odd characteristic: components.** Besides the same two rank inequalities, square-zero requires \(u+v\ge n\). For each integer \(0\le h\le s\), define the linear subspace
\[
L_h=\{a\in y^{n-h}R,\ b\in y^{\max(n-r,h)}R\}.
\]
Every admissible element belongs to \(L_h\) for \(h=n-u\), and every element of every \(L_h\) is admissible. If \(s\le n-r\), the \(L_h\) are nested and the locus equals \(L_s\), of dimension \(r+s\). If \(s>n-r\), the nested early spaces are absorbed into \(L_{n-r}\), and the maximal components are precisely \(L_{n-r},\ldots,L_s\). Each has dimension \(n\), and for indices \(i<j\) their intersection is specified by \(a\in y^{n-i}R\), \(b\in y^jR\), hence dimension \(i+(n-j)=n-(j-i)\). Each newly added component meets the union of earlier components exactly in its codimension-one intersection with the immediately preceding component; it therefore contributes \(q^n-q^{n-1}\) new \(\mathbb F_q\)-points. This proves all cumulative formulas. The equations and stratification are stable under algebraic closure, giving the reduced irreducible-component claims.

**Jordan types and sharp transition.** Because \(m_f^2=m_{f^2}=0\), it has exactly \(r\) size-two Jordan blocks and \(2n-2r\) size-one blocks. A difference of cumulative counts gives the exact multiplicity. The rank \(r\) first admits the odd-characteristic component splitting precisely when \(r+\lfloor r/2\rfloor>n\), whose least integer solution is \(\lceil2(n+1)/3\rceil\). All intermediate ranks occur: in characteristic two choose \(a=0\) and \(b=y^{n-r}\); the same choice works in odd characteristic. At \(r=0\) take \(f=0\).

## Verification
The companion standalone program `verify_square_zero_multiplication.py` performs an exhaustive independent coefficient census and row-reduction rank computation. It completed 18 field/truncation configurations over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\), including 6,244 square-zero elements; its terminal marker is `SQUARE_ZERO_MULTIPLICATION_JORDAN_CENSUS_OK 18 6244`. The enumeration verifies finite cases only; the universally quantified claims follow from the valuation and Smith-form arguments above.

## Relationship to prior work
David Cook II, *The Lefschetz properties of monomial complete intersections in positive characteristic* (arXiv:1111.4979, first public 2011-11-21), analyzes maximal-rank properties of multiplication by a **linear form**, particularly with characteristic-sensitive complete intersections. The general foundation for Jordan types and their loci in Artin algebras is given by Iarrobino, Macias Marques and McDaniel, *Artinian algebras and Jordan type* (arXiv:1802.07383). Altafi, Iarrobino and Khatami, *Complete intersection Jordan types in height two* (arXiv:1810.00716), focus on classifications associated with linear forms and different field hypotheses. Their theorems do not state the all-elements square-zero multiplier rank census or the characteristic-dependent union-of-linear-spaces decomposition shown here.

A separately published result on nilpotency indices of *matrix lifts* \(J_n+\varepsilon B\) over dual numbers concerns general dual-matrix perturbations, rather than the restricted commutative multiplication family \(M_f\) and its square-zero Jordan ranks. Likewise, general square-zero matrix distributions over chain rings do not determine the rank distribution inside the equal-diagonal triangular subfamily. Exhaustive historical priority is not claimed.

## Limitations
The formulas concern multiplication operators by square-zero elements, not arbitrary endomorphisms or arbitrary elements of the algebra. The geometric statement refers to reduced support only, not scheme-theoretic multiplicities or the unreduced ideal. The family has exactly two generators with one square-zero generator; extension to higher embedding dimension is open. Exact publication priority against all earlier specialized literature has not been independently established.

## References
1. D. Cook II, *The Lefschetz properties of monomial complete intersections in positive characteristic*, arXiv:1111.4979v1 (2011-11-21), https://arxiv.org/html/1111.4979v1.
2. A. Iarrobino, P. Macias Marques, C. McDaniel, *Artinian algebras and Jordan type*, arXiv:1802.07383 (2018-02-21), https://arxiv.org/html/1802.07383v6.
3. N. Altafi, A. Iarrobino, L. Khatami, *Complete intersection Jordan types in height two*, arXiv:1810.00716 (2018-10-01), https://arxiv.org/abs/1810.00716.
