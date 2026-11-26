# Exact Jordan-rank census of square-zero matrices centralizing two equal Jordan blocks

## Finding

Let \(q\) be a prime power, \(n\ge1\), \(J_n\) a nilpotent Jordan block over \(\mathbb F_q\), and \(B_n=J_n\oplus J_n\). The polynomial
\[
P_{n,q}(z)=\sum_{\substack{A\in M_{2n}(\mathbb F_q)\\A^2=0,\ AB_n=B_nA}}z^{\operatorname{rank}_{\mathbb F_q}A}
\]
has the following closed finite expression. Set \(c=\lceil n/2\rceil\), \(h=\lfloor n/2\rfloor\),
\[
C=(q^2-1)q^{2n-2},\quad R_1=(q-1)(q+1)^2,\quad G=q(q-1)^2(q+1).
\]
Then
\[
\begin{aligned}
P_{n,q}(z)={}&1+C\sum_{k=0}^{c-1}\left(q^{-k}z^{n-k}+\sum_{j=0}^{k-1}(q-1)q^{-j-1}z^{n-j}\right)\\
&+\sum_{m=1}^{h}q^{4(m-1)}\left[Gz^{2m}+R_1\left(q^{-(m-1)}z^m+\sum_{s=1}^{m-1}(q-1)q^{-s}z^{2m-s}\right)\right].
\end{aligned}
\]
Empty inner sums are zero. Every displayed coefficient is a nonnegative integer. In particular,
\[
P_{n,q}(1)=\lceil n/2\rceil(q^2-1)q^{2n-2}+q^{4\lfloor n/2\rfloor},
\]
and each rank \(0,1,\ldots,n\) occurs. Since \(A^2=0\), the coefficient of \(z^r\) also counts the matrices with precise Jordan partition \((2^r,1^{2n-2r})\) in the centralizer of \(B_n\).

## Assumptions and scope

The ground ring is the truncated polynomial ring \(R=\mathbb F_q[t]/(t^n)\); the result holds for every prime power, including characteristics two and three, and for each integer \(n\ge1\). We count individual labeled matrices in the fixed centralizer, not similarity classes or centralizer-conjugacy orbits. The rank is over \(\mathbb F_q\), not the minimum number of generators over \(R\). The correspondence between the centralizer and \(M_2(R)\) is induced by identifying \(\mathbb F_q^{2n}\) with the \(R\)-module \(R^2\), on which multiplication by \(t\) is \(B_n\).

## Proof

**1. Valuation split.** Every nonzero \(A\in M_2(R)\) has unique minimum entry valuation \(k\in\{0,\ldots,n-1\}\). It has a unique representation \(A=t^kU\), with \(U\) a primitive matrix over \(R_{n-k}=\mathbb F_q[t]/(t^{n-k})\). The condition \(A^2=0\) is equivalent to \((U\bmod t^{n-2k})^2=0\) if \(2k<n\); if \(2k\ge n\), it is automatic. These are disjoint cases.

**2. Primitive shallow matrices.** Fix \(0\le k<c\), and put \(m=n-2k\), so \(n-k=m+k\). A primitive square-zero \(U_0\in M_2(R_m)\) is conjugate to the elementary Jordan matrix \(\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}\). Indeed, modulo \(t\) a primitive square-zero matrix is nonzero nilpotent and has rank one. Choose a vector \(v\) so that \(U_0v\) is primitive; then \((U_0v,v)\) is a basis by reduction modulo \(t\), and in that basis the matrix is elementary Jordan. Its invertible centralizer consists of \(aI+bJ\), with \(a\in R_m^\times\) and \(b\in R_m\). Therefore its conjugacy orbit has size
\[
\frac{|\mathrm{GL}_2(R_m)|}{|R_m^\times|\,|R_m|}=(q^2-1)q^{2m-2}.
\]
There are \(q^{4k}\) lifts to \(U\in M_2(R_{m+k})\), hence exactly \(C=(q^2-1)q^{2n-2}\) matrices in this valuation stratum.

Every lift has unit entry and rank-one reduction, so one cofactor of \(U\) is a unit. Keeping three entries fixed and varying the fourth among its \(t^m\)-congruent lifts makes \(\det U\) **uniform over the ideal \(t^mR_{m+k}\)**. Thus, for \(0\le j<k\), the fraction of lifts with determinant valuation \(m+j\) is \((q-1)q^{-j-1}\); the remaining fraction \(q^{-k}\) has determinant zero in \(R_{m+k}\). The Smith exponents of primitive \(U\) are \((0,m+j)\), where the second exponent is capped at \(m+k\); the Smith exponents of \(t^kU\) over \(R_n\) are \((k,k+m+j)\), capped at \(n\). Multiplication by \(t^a\) on \(R_n\) has \(\mathbb F_q\)-rank \(n-a\), so the resulting ranks are \(n-j\) for \(j<k\) and \(n-k\) in the determinant-zero case. This yields the first sum in the displayed polynomial.

**3. Deep matrices.** Put \(h=n-c\), equal to \(\lfloor n/2\rfloor\). Multiplication by \(t^c\) identifies the deep matrices \(\{A:t^c\mid A\}\) bijectively with the unrestricted \(M_2(R_h)\). If \(h=0\), only the zero matrix occurs. For \(h\ge1\), each nonzero matrix can be written \(t^{h-m}U\) with \(1\le m\le h\) and primitive \(U\in M_2(R_m)\). Its rank as an endomorphism of \(R_n^2\) equals its rank as an endomorphism of \(R_m^2\): multiplying by \(t^c\) shifts images into a length-\(m\) tail without changing their \(\mathbb F_q\)-dimension.

The residue \(\bar U\in M_2(\mathbb F_q)\) is either invertible (\(G=q(q-1)^2(q+1)\) choices) or rank one (\(R_1=(q-1)(q+1)^2\) choices). Each residue lifts in \(q^{4(m-1)}\) ways. In the invertible case both Smith exponents vanish, giving rank \(2m\). In the rank-one case \(\det U\) is uniform on \(tR_m\), by varying an entry with unit cofactor. The determinant has valuation \(s\in\{1,\ldots,m-1\}\) with fraction \((q-1)q^{-s}\), yielding rank \(2m-s\); the complementary fraction \(q^{-(m-1)}\) has zero determinant, yielding rank \(m\). This gives the second sum. The zero matrix contributes \(1\).

**4. Exhaustiveness and total.** The shallow and deep strata partition all square-zero matrices. Substituting \(z=1\), the weights in each shallow stratum sum to \(1\), producing \(cC\). The deep matrices number \(q^{4h}\), producing the stated total. Their rank support together with shallow ranks covers all integers from \(0\) through \(n\): deep matrices provide ranks \(0\) through \(2h\), and the shallow stratum \(k=0\) provides rank \(n\), with the remaining boundaries covered automatically. This proves the result.

## Verification

A standalone standard-library Python script, `checker.py`, implements the closed coefficient formula separately from an exhaustive enumeration of \(2\times2\) matrices of truncated polynomials. Exhaustive tests compute the square and the \(\mathbb F_q\)-linear rank from polynomial arithmetic and elimination; they cover \((n,q)=(1,2),(2,2),(3,2),(4,2),(1,3),(2,3),(1,5),(2,5)\). They agree coefficient by coefficient. Independent rational-arithmetic checks of the coefficients and total are performed for \(1\le n\le12\) and \(q\in\{2,3,4,5,7,8,9,11\}\). The latter are algebraic consistency checks, not exhaustive matrix enumerations over extension fields. Running `python checker.py` prints `ALL_EXACT_CHECKS_PASSED`.

For illustration, the binary polynomials at lengths two and four are
\[
P_{2,2}(z)=1+9z+18z^2,\qquad
P_{4,2}(z)=1+9z+78z^2+168z^3+384z^4.
\]

## Relationship to prior work

Bogdanić–Đurić–Koljančić–Oblak–Šivic (2022), arXiv:2212.08425, study exactly the centralizer of \(J_n\oplus J_n\) but determine the **possible nilpotent Jordan partitions** rather than the **cardinality of each square-zero rank stratum**. Britnell–Wildon (2010/2011), arXiv:1001.0811, analyze commuting similarity-class types and determinant possibilities, not the rank-profile point counts inside a fixed commutant. Sharma (2014), arXiv:1409.2698, studies simultaneous-similarity orbits of commuting matrices over finite fields, a different quotient-counting problem. A previously obtained square-zero count by entry valuation over finite chain rings supplies the total \(P_{n,q}(1)\), but does not determine the rank coefficients; the new contribution is precisely the complete Jordan-rank distribution, requiring the determinant-valuation analysis within every primitive and deep stratum. The total alone does not imply these coefficients.

## Limitations

The fixed matrix consists of exactly two equally sized nilpotent Jordan blocks. The theorem does not count all commuting nilpotent matrices, arbitrary nilpotency exponents, or arbitrary numbers/unequal sizes of blocks. The formula counts labeled elements rather than conjugacy orbits. An equivalent rank distribution may exist in literature indexed under truncated-module representations or Hall-polynomial enumerations; searches are not a proof of absolute novelty. The computer tests are finite checks and do not replace the general proof.

## References

1. D. Bogdanić, A. Đurić, S. Koljančić, P. Oblak, K. Šivic, *Jordan structures of nilpotent matrices in the centralizer of a nilpotent matrix with two Jordan blocks of the same size*, arXiv:2212.08425v1 (first public 2022-12-16), https://arxiv.org/abs/2212.08425.
2. J. R. Britnell, M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811v1 (2010), https://arxiv.org/abs/1001.0811.
3. R. Sharma, *Simultaneous Similarity Classes of Commuting Matrices over a Finite Field*, arXiv:1409.2698 (2014), https://arxiv.org/abs/1409.2698.
