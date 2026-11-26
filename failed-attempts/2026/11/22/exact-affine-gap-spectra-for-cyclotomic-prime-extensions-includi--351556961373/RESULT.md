# Exact affine gap spectra for cyclotomic prime extensions, including every \(\Phi_{15p}\)

## Finding

For a polynomial \(H(x)\) with nonzero constant and leading coefficients, let \(N_\ell(H)\) count adjacent exponents of nonzero coefficients whose difference is exactly \(\ell\), including \(\ell=1\).

**Affine-spectrum theorem.** Let \(m>1\) be odd and squarefree, let \(p>m\) be prime, put \(d=\varphi(m)\), \(r\equiv p\pmod m\), \(1\le r<m\), and \(Q=(p-r)/m\). There are nonnegative integers \(A_{m,r,\ell}\) and \(B_{m,r,\ell}\), explicitly determined by at most \(d\) cyclic words of length \(m\) and a single base quotient polynomial, such that **for every** such prime,

\[
N_\ell(\Phi_{mp})=B_{m,r,\ell}+(Q-1)A_{m,r,\ell}\qquad(\ell\ge1).
\]

This is an exact affine law for the *entire* gap histogram, not just its largest value. The construction below defines the constants without relying on experimental interpolation. The same identity holds for the quotient \(\Phi_m(x^t)/\Phi_m(x)\) whenever \(t>m\) is coprime to \(m\), with \(r\equiv t\pmod m\) and \(Q=(t-r)/m\).

**Complete first ternary application.** For \(m=15\), the only possible gap lengths are \(1,\ldots,8\). In the following table the eight entries of each vector correspond in order to lengths \(1,2,3,4,5,6,7,8\). Write \(\mathbf A_r=(A_{15,r,1},\ldots,A_{15,r,8})\) and \(\mathbf B_r=(B_{15,r,1},\ldots,B_{15,r,8})\).

| \(r\) | \(\mathbf A_r\) (increment for \(p\mapsto p+15\)) | \(\mathbf B_r\) (base at \(t=15+r\)) |
|---:|---|---|
| 1 | (10, 4, 10, 2, 4, 0, 4, 2) | (10, 4, 10, 2, 4, 0, 4, 2) |
| 2 | (42, 16, 2, 0, 0, 4, 0, 2) | (46, 18, 2, 0, 0, 4, 0, 2) |
| 4 | (58, 12, 2, 4, 0, 0, 0, 2) | (74, 16, 2, 4, 0, 0, 0, 2) |
| 7 | (50, 6, 14, 0, 0, 0, 0, 2) | (72, 10, 20, 0, 0, 0, 0, 2) |
| 8 | (50, 6, 14, 0, 0, 0, 0, 2) | (78, 8, 22, 0, 0, 0, 0, 2) |
| 11 | (58, 12, 2, 4, 0, 0, 0, 2) | (100, 20, 4, 8, 0, 0, 0, 2) |
| 13 | (42, 16, 2, 0, 0, 4, 0, 2) | (80, 30, 4, 0, 0, 8, 0, 2) |
| 14 | (10, 4, 10, 2, 4, 0, 4, 2) | (20, 8, 20, 4, 8, 0, 8, 2) |

In particular, the *set* of gap lengths of \(\Phi_{15p}\), for primes \(p>15\), has precisely four possibilities, depending only on \(p\pmod{15}\):

| Residues of \(p\) modulo \(15\) | Set of gap lengths |
|---|---|
| \(\pm1\) | \(\{1,2,3,4,5,7,8\}\) |
| \(\pm2\) | \(\{1,2,3,6,8\}\) |
| \(\pm4\) | \(\{1,2,3,4,8\}\) |
| \(\pm7\) | \(\{1,2,3,8\}\) |

All other gap lengths occur zero times; the largest-gap multiplicity is \(N_8=2Q\) in all eight classes.

## Assumptions and scope

The base \(m\) is any odd squarefree integer greater than one. The parameter \(p\) is a rational prime exceeding \(m\); it is *not* required that \(m=15\), except in the numerical classification. The eight rows for \(m=15\) cover every prime exceeding \(15\), because its residue class is a unit modulo \(15\). The constants \(B_{m,r,\ell}\) are defined using an integral polynomial quotient at \(t=m+r\), even if \(m+r\) is composite. No claim is made here about prime parameters smaller than \(m\) or about all gap distributions for arbitrary ternary indices.

## Proof

**1. Exact periodic coefficients.** Write
\[
\Phi_m(x)=\sum_{i=0}^{d}a_i x^i,\qquad
U_m(x)=\frac{1-x^m}{\Phi_m(x)}=\sum_{s=0}^{m-1}u_s x^s,
\]
where \(u_s=0\) beyond the actual degree. The quotient is an integer polynomial. For every integer \(t>m\) coprime to \(m\), the polynomial
\[
F_t(x)=\frac{\Phi_m(x^t)}{\Phi_m(x)}
\]
is monic and integral: each primitive \(m\)-th root remains primitive on raising to the \(t\)-th power, so divisibility holds, and Gauss's lemma gives integrality. Its degree is \(D=d(t-1)\). Since \(1/\Phi_m(x)=U_m(x)/(1-x^m)\), the exact coefficient of \(x^k\), for \(0\le k\le D\), is
\[
[x^k]F_t(x)=\sum_{i=0}^{\lfloor k/t\rfloor} a_i u_{(k-it)\bmod m}.
\]
The upper index is at most \(d-1\), since \(k\le d(t-1)<dt\).

Partition the coefficient array into \(d\) consecutive blocks: for \(0\le j<d-1\), block \(j\) comprises exponents \(jt,\ldots,(j+1)t-1\), and the final block \(j=d-1\) comprises \((d-1)t,\ldots,D\). Their respective lengths are \(t\) and \(t-d+1\). Define the period-\(m\) word
\[
b_{j,r}(h)=\sum_{i=0}^j a_i u_{(jr+h-ir)\bmod m},\qquad 0\le h<m,
\]
where \(r\equiv t\pmod m\). Block \(j\) is an initial segment of this infinite periodic word of its stated length, independently of the quotient \(Q\) in \(t=mQ+r\).

**2. Each block contains a nonzero coefficient.** Let \(P_j(y)=\sum_{i=0}^j a_i y^i\). The cyclic word \(b_{j,r}\) vanishes identically only if the polynomial \(U_m(x)P_j(x^r)\) is zero modulo \(x^m-1\). Cancellation of \(U_m=(1-x^m)/\Phi_m\) forces \(\Phi_m\mid P_j(x^r)\). Evaluating on all primitive \(m\)-th roots and using \(\gcd(r,m)=1\) gives \(\Phi_m\mid P_j\), impossible because \(P_j\ne0\) and \(j<d\). Thus each cyclic word has support. Since the first \(d-1\) blocks have length \(t>m\), each contains an entire period and hence a nonzero coefficient. The final block contains the leading coefficient \(1\) at degree \(D\), so it too is nonempty.

**3. Period insertion lemma.** Let \(w\) be any bi-infinite periodic word with period \(m\), and suppose its length-\(L\) prefix has at least one nonzero entry. Write \(S\) for the support residues in a period. Enlarging the prefix from \(L\) to \(L+m\) leaves its first supported position unchanged and moves its last supported position forward by exactly \(m\). Between its old last support and the new last support, the lengths of successive gaps are precisely the \(|S|\) cyclic gaps between consecutive support residues in \(S\), including the wraparound gap. Therefore the internal histogram of the longer prefix equals that of the shorter prefix plus the cyclic gap histogram of \(S\). This statement also holds for \(L<m\), provided the original prefix has a nonzero entry.

**4. Assemble the whole polynomial.** Increasing \(t\) to \(t+m\) lengthens each of the \(d\) blocks by exactly \(m\) while retaining its periodic word, since \(t\equiv t+m\pmod m\). By step 3, first support positions relative to block starts remain fixed and last support positions relative to block ends remain fixed. Thus the gaps *crossing block boundaries* retain their lengths, and only internal gaps gain one cycle each. Put
\[
S_{j,r}=\{h\in\{0,\ldots,m-1\}:b_{j,r}(h)\ne0\},\quad
A_{m,r,\ell}=\sum_{j=0}^{d-1}\#\{h\in S_{j,r}:\text{the next cyclic support residue is }\ell\text{ steps after }h\}.
\]
This proves \(N_\ell(F_{t+m})-N_\ell(F_t)=A_{m,r,\ell}\) for every \(\ell\ge1\). Defining \(B_{m,r,\ell}=N_\ell(F_{m+r})\) and iterating proves the affine formula. For prime \(t=p\), the standard cyclotomic identity gives \(F_p=\Phi_{mp}\).

**5. Evaluate the \(m=15\) constants.** Direct multiplication gives
\[
\Phi_{15}(x)=1-x+x^3-x^4+x^5-x^7+x^8,
\qquad
U_{15}(x)=1+x+x^2-x^5-x^6-x^7.
\]
Hence \(d=8\) and the vectors \(\mathbf A_r\) are obtained by eight finite cyclic support lists of length \(15\). The vectors \(\mathbf B_r\) are obtained from the exact coefficient recursion for \(F_{15+r}\) in step 1. The table records the resulting exact integers. A second derivation using long division by \(\Phi_{15}\), verified coefficient by coefficient including the trailing product constraints, appears in the standalone checker. Its loop evaluates the two independent coefficient representations, cyclic increments and the entire histogram at 120 parameters. No finite experiment is needed to justify the infinite affine identity proved in steps 1–4.

## Verification

Run `python3 verify_gap_hist.py` with a standard Python 3 interpreter. The checker uses only the standard library. It confirms the identity \(\Phi_{15}U_{15}=1-x^{15}\); each of the eight cyclic slope vectors; all eight baseline vectors; and the complete histograms, endpoint coefficient support, degree sums and polynomial-product identities at 120 distinct parameters \(t=15Q+r\), for \(1\le Q\le15\) and all eight units \(r\pmod{15}\). These are finite checks of the explicit arithmetic data. They do not substitute for the universal block-insertion proof above.

## Relationship to prior work

Cafure and Cesaratto, first publicly available July 25, 2025, derive complete counts of binary cyclotomic gaps for two residual classes and use cyclic words for other binary gap questions. Their binary results do not determine the ternary \(\Phi_{15p}\) histograms or the all-odd-squarefree-cofactor affine law. An earlier paper, *The ternary cyclotomic polynomials \(\Phi_{3pq}\)*, provides explicit coefficient blocks for selected ternary cases and coefficient-value counts for all \(\Phi_{15p}\) (Table 9), as well as largest-gap counts. Because a coefficient-count table forgets coefficient *order*, it does not itself imply the adjacent-gap table. The earlier constructive coefficient-block formulas do permit reconstruction of individual polynomials and may offer a different derivation of this classification; the present contribution is the exact affine full-gap law, its cyclic-support formula, the complete eight-residue histogram and the four sharp support regimes, not the underlying coefficient block decomposition.

Zheng's November 17, 2026 preprint gives the maximum gap and its multiplicity for all odd squarefree cofactors, and proves a cyclic zero-run restriction; it does not state the complete gap-length histograms. In particular, the \(N_8=2Q\) column of the present table is already known, not asserted as new. The other explicit length-frequency columns and four-way support separation are not stated there. The later preprint was consulted only for coverage comparison, not used to assign the source date of this finding.

## Limitations

The results concern coefficient *support gaps*, not the signed coefficient distribution. The infinite law requires a fixed odd squarefree cofactor and a varying prime exceeding it; the explicit table is for cofactor \(15\) only. The exact numbers are conditional on the stated quotient-and-periodic-block identities, established in the proof. The general affine law is closely related to existing cyclic coefficient descriptions and may be an implicit corollary of published block machinery. A complete full-text search of all historical coefficient literature is not possible; independent novelty assessment remains necessary. Independent mathematical audit has not been performed.

## References

1. A. Cafure and E. Cesaratto, *Gaps in binary cyclotomic polynomials*, arXiv:2507.19381, first submitted 2025-07-25, https://arxiv.org/abs/2507.19381 ; full text https://arxiv.org/html/2507.19381v2 .
2. *The ternary cyclotomic polynomials \(\Phi_{3pq}\)*, full-text open-access manuscript, https://orbiserver.uni.lu/bitstream/10993/55534/1/ternary_cyclotomic_polynomials.pdf ; especially Sections 3 and 9.
3. Q.-Y. Zheng, *The totient bound and extremal gaps in cyclotomic polynomials*, arXiv:2611.22795v1, first submitted 2026-11-17, https://arxiv.org/html/2611.22795v1 ; especially Theorem 1.1 and Section 5.
