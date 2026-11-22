# The commuting-idempotent rank spectrum determines nilpotent Jordan form

## Finding
Let \(q\) be any prime power, let \(N\in M_n(\mathbb F_q)\) be nilpotent, and define its commuting-idempotent rank polynomial by
\[
P_N(z)=\sum_{r=0}^{n}c_r(N)z^r,\quad
c_r(N)=\#\{E\in M_n(\mathbb F_q):E^2=E,\ EN=NE,\ \operatorname{rank}(E)=r\}.
\]
**Spectral rigidity theorem.** For any two nilpotent matrices \(N,N'\) over the same field, equality \(P_N(z)=P_{N'}(z)\) holds if and only if the two matrices are similar, even without specifying their ambient dimension in advance. There is an explicit coefficient-by-coefficient reconstruction of every nilpotent Jordan-block multiplicity from \(P_N\).

The forward enumeration by ordered invariant direct-summand decompositions is classical orbit-stabilizer input and is **not** asserted independently novel. The contribution asserted is the inverse spectral-rigidity theorem and its explicit triangular reconstruction.

## Assumptions and scope
The finite field \(\mathbb F_q\) has arbitrary prime-power cardinality \(q\ge2\), without a characteristic restriction. The matrix \(N\) is nilpotent and the rank of \(E\) is ordinary vector-space image dimension. The zero-dimensional case has \(P_N(z)=1\) and is unique. For every positive dimension \(n\), let \(m_j\) be the number of nilpotent Jordan blocks of length \(j\), with \(\sum_j j m_j=n\). Write \(B=\sum_jm_j\). Nilpotent Jordan form exists over the base field because the only eigenvalue is zero. The theorem is a rigidity statement *within nilpotent matrices*; no analogous claim is made for arbitrary matrices.

## Proof
### 1. Exact spectrum from invariant direct sums
View \(\mathbb F_q^n\) as the \(\mathbb F_q[t]\)-module \(M=\bigoplus_{j\ge1}(\mathbb F_q[t]/(t^j))^{m_j}\), with \(t\) acting as \(N\). Then \(EN=NE\) and \(E^2=E\) are equivalent to an ordered internal module decomposition \(M=\operatorname{im}E\oplus\ker E\). The image of \(E\) has \(a_j\) blocks of length \(j\), and the kernel has \(b_j=m_j-a_j\), where \(0\le a_j\le m_j\). Every such choice occurs and, for this pair of module isomorphism types, the automorphism group of \(M\) acts transitively on internal ordered decompositions with stabilizer the product of the two constituent module automorphism groups.

For a block multiplicity vector \(u\), put
\[
D(u)=\sum_{i,j\ge1}u_i u_j\min(i,j),\quad
\Phi_s(q)=\prod_{h=1}^{s}(1-q^{-h}),\quad \Phi_0(q)=1.
\]
The endomorphism algebra has \(q^{D(u)}\) elements. Its unit group has order \(q^{D(u)}\prod_j\Phi_{u_j}(q)\): the Jacobson-radical quotient is the product of the matrix algebras \(M_{u_j}(\mathbb F_q)\), and an endomorphism is invertible precisely when all diagonal leading-coefficient matrices are invertible. Hence the number of commuting idempotents with a fixed image block profile \(a\) is
\[
C(a;m)=q^{D(m)-D(a)-D(b)}
 \prod_j\frac{\Phi_{m_j}(q)}{\Phi_{a_j}(q)\Phi_{b_j}(q)}
 =q^{\,2\sum_{i,j}a_i b_j\min(i,j)-\sum_j a_j b_j}
 \prod_j {m_j\brack a_j}_q.
\]
Here \({m\brack a}_q\) is the ordinary Gaussian binomial coefficient. In particular
\[
P_N(z)=\sum_{(a_j):\ 0\le a_j\le m_j}C(a;m)z^{\sum_j j a_j}.
\]
All exponents are nonnegative: \(2\sum a_i b_j\min(i,j)\ge2\sum_j j a_j b_j\ge\sum_j a_j b_j\). The forward expression is integral.

### 2. Recover the total number of blocks
For \(n\ge1\), the degree of \(P_N\) is \(n\), since the full identity is the unique rank-\(n\) idempotent. Let \(d\) be the smallest strictly positive exponent with a nonzero coefficient; it equals the shortest Jordan-block length. Only the choices of *one* of the length-\(d\) blocks contribute to rank \(d\). Therefore
\[
c_d=q^{2d(B-1)-(m_d-1)}{m_d\brack1}_q
=q^{2d(B-1)}\sum_{h=0}^{m_d-1}q^{-h}.
\]
Because \(1\le\sum_{h=0}^{m_d-1}q^{-h}<q\),
\[
\left\lfloor\log_q c_d\right\rfloor=2d(B-1).
\]
Thus \(B=1+\lfloor\log_qc_d\rfloor/(2d)\), a nonnegative integer that depends only on the polynomial. The same displayed coefficient then recovers \(m_d\), since the finite geometric sum increases strictly with its length.

### 3. Triangular reconstruction of every multiplicity
Suppose \(m_i\) have been recovered for all \(i<j\), and put \(S_j=\sum_{i<j}m_i\). Every idempotent of rank \(j\) whose image uses only blocks of lengths smaller than \(j\) has a known count. Let \(Q_j\) be the sum over all choices \(0\le a_i\le m_i\) for \(i<j\) with \(\sum_{i<j}i a_i=j\), of
\[
q^{\,2\sum_{i<j}a_i(\sum_{\ell<j}(m_\ell-a_\ell)\min(i,\ell)+i(B-S_j))
 -\sum_{i<j}a_i(m_i-a_i)}
\prod_{i<j}{m_i\brack a_i}_q.
\]
This is computable from previously recovered multiplicities and \(B\), because every *unknown* block of length at least \(j\) contributes \(i\) to \(\min(i,\ell)\) when \(i<j\le\ell\).

The only other possibility for a rank-\(j\) image is a single length-\(j\) block. Let \(R_j=c_j-Q_j\). The exact formula yields
\[
R_j=\begin{cases}
0,&m_j=0,\\
q^{\,2(\sum_{i<j}i m_i+j(B-S_j-1))}\displaystyle\sum_{h=0}^{m_j-1}q^{-h},&m_j>0.
\end{cases}
\]
If \(R_j=0\), recover \(m_j=0\). Otherwise its positive geometric sum, with prefactor already known, determines \(m_j\) uniquely. Repeating for \(j=1,\ldots,n\) recovers the entire Jordan partition (or starting at \(d\) makes the zero steps automatic). Hence equal spectra imply equal partitions and therefore similarity; similarity obviously preserves the commuting-idempotent rank polynomial. This completes the proof.

## Verification
A standalone, standard-library Python program `verify.py` implements the forward Gaussian-coefficient sum, the inverse coefficient recurrence, and direct matrix arithmetic. The direct independent brute force enumerates **every** matrix \(E\) over \(\mathbb F_2\) in dimensions \(1\) through \(4\), and over \(\mathbb F_3\) in dimensions \(1\) through \(3\), for every Jordan partition, testing \(E^2=E\), \(EN=NE\), and ordinary matrix rank before comparing the entire coefficient vectors. It further confirms exact coefficient reconstruction for every integer partition of all dimensions through \(22\), at \(q=2,3,4,5\); the latter test uses the formula, not finite-field matrix enumeration. Running `python verify.py` produces the terminal success marker `JORDAN_IDEMPOTENT_RECONSTRUCTION_VERIFIED`. This finite evidence is independent corroboration of calculations and not an infinite proof.

## Relationship to prior work
Mingueza, Montoro, and Roca (2019) give structural descriptions and dimensions of endomorphism centralizers. De la Cruz and Misa (2022) describe the semisimple quotient of a nilpotent matrix centralizer, a standard ingredient in the unit-group order used above. Classical module Krull--Schmidt decomposition and orbit-stabilizer already provide the **forward** image-Jordan-profile count. The published two-length Jordan-form idempotent study [3] explicitly credits that exact counting formula as earlier input while proving asymptotic theta limits, and it is not claimed again here. Another published study [4] has an inverse centralizer-rank statement, but for nilpotent **partial permutations in the symmetric inverse monoid** rather than the field-linear commuting-idempotent polynomial. The inspected material does not state the particular uniform coefficient reconstruction above. An earlier theorem for arbitrary module direct-summand rank distributions could still cover this rigidity statement and remains a priority risk.

## Limitations
No claim is made for nonnilpotent operators or for reconstructing an operator from only the *total* number of commuting idempotents. The theorem does not yield a numerical stability bound under noise in the coefficients. A simultaneous conjugacy-invariant derivation of the forward count is classical and not the new assertion. The smallest case tables do not prove the all-dimensional result, and the source search does not certify historical uniqueness. Independent mathematical review has not yet been performed.

## References
1. D. Mingueza, M. E. Montoro, and A. Roca, *The Centralizer of an Endomorphism over an Arbitrary Field*, arXiv:1909.06198, first public version 2019-09-12, https://arxiv.org/abs/1909.06198.
2. R. J. de la Cruz and E. Misa, *The Algebra Generated by Nilpotent Elements in a Matrix Centralizer*, *Electronic Journal of Linear Algebra* **38** (2022), 1–8, https://journals.uwyo.edu/index.php/ela/article/view/6503.
3. *Independent theta coordinates for idempotents centralizing two-length Jordan forms*, published 2026-10-26, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-independent-theta-coordinates-for-idempotents-centralizing-two-l--62a1fa4ec9b3.
4. *Nilpotent partial-permutation conjugacy is determined by its centralizer rank spectrum*, published 2026-10-26, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-nilpotent-partial-permutation-conjugacy-is-determined-by-its-cen--8be29dd91c24.
5. *Simultaneous idempotent spectra of split basic algebras and an inverse random-cluster invariant*, published 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-simultaneous-idempotent-spectra-of-split-basic-algebras-and-an-i--4fe52ac53574.
