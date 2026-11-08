# Local Smith invariants and self-Fourier uniqueness for prime-field norm-one conics

## Finding
Let \(p\ge3\) be an odd prime, let \(C_p=\{(x,y)\in\mathbb F_p^2:x^2+y^2=1\}\), let \(N=|C_p|=p-\left(\frac{-1}{p}\right)\), and put \(m=N/2\). For \(\zeta_p=\exp(2\pi i/p)\), form the unnormalized square restricted additive Fourier matrix
\[
F_p=\bigl(\zeta_p^{xu+yv}\bigr)_{(x,y),(u,v)\in C_p}.
\]
Let \(\mathcal O=\mathbb Z_p[\zeta_p]\), a discrete valuation ring, with uniformizer \(\pi=\zeta_p-1\) and valuation \(v_\pi(\pi)=1\). Its **complete Smith valuation list** over \(\mathcal O\), in nondecreasing order, is
\[
\boxed{0,1,1,2,2,\ldots,m-1,m-1,m.}
\]
In particular, \(\det F_p\ne0\) over \(\mathbb C\), every function supported on \(C_p\) is uniquely recovered from its Fourier transform restricted to the same conic, and
\[
\boxed{v_\pi(\det F_p)=m^2=N^2/4.}
\]
Equivalently, over a finite unramified extension of \(\mathcal O\), the multiplicative-character eigenvalues of this Fourier matrix have exact valuations \(\min(r,N-r)\) for \(0\le r<N\). The assertion covers both split and nonsplit conics, including the smallest prime \(p=3\).

## Assumptions and scope
The indices are the points of \(C_p\), with the dot-product character convention shown above; no factor of \(p^{-1}\) or \(N^{-1/2}\) is included. Reversing the additive-character sign merely conjugates the matrix and leaves all valuation invariants unchanged. Smith exponents concern the local cyclotomic ring at the unique prime over \(p\), not the integral Smith form of a matrix over \(\mathbb Z\), and make no assertion about the complex singular values or their condition number. The argument requires \(p\) prime: it does not assert identical invariants for extension fields.

Write \(E=\mathbb F_p[J]/(J^2+1)\), allowing the split case, with involution \(\overline{x+yJ}=x-yJ\). The group \(H=\{h\in E:h\bar h=1\}\) is naturally \(C_p\), is cyclic of size \(N\), and has \(p\nmid N\). Multiplication by the involution sends \(h\in H\) to \(h^{-1}\). Its field-valued real part is \(L(h)=(h+h^{-1})/2\in\mathbb F_p\).

## Proof
**1. Multiplicative convolution.** For \(z=x+Jy\) and \(w=u+Jv\) in \(H\),
\[
xu+yv=L(z\bar w)=L(zw^{-1}).
\]
Thus \(F_p\) is a convolution matrix on the cyclic group \(H\), with kernel \(K(h)=\zeta_p^{L(h)}\). After adjoining \(N\)-th roots of unity, the character matrix of \(H\) diagonalizes \(F_p\); its eigenvalues, up to replacing a character with its inverse, are
\[
B_r=\sum_{h\in H}\chi_r(h)\,\zeta_p^{L(h)},\qquad 0\le r<N.
\]
Because \(p\nmid N\), the character matrix and its inverse have integral entries in the unramified cyclotomic extension and are invertible over its valuation ring. We may therefore compute all elementary divisors from these \(B_r\).

**2. Integral Taylor expansion.** Let \(\mathcal O'\) be the integral ring obtained by adjoining \(N\)-th roots of unity to \(\mathcal O\). This is unramified over \(\mathcal O\); its residue field contains a copy of the norm-one group \(H\), and the character indexing can be chosen so that \(\chi_r(h)\) reduces to \(h^r\). For each \(h\), choose the integer \(e(h)\in\{0,\ldots,p-1\}\) representing \(L(h)\). Then exactly, in \(\mathcal O'\),
\[
B_r=\sum_{j=0}^{p-1}\pi^j A_{r,j},\qquad
A_{r,j}=\sum_{h\in H}\chi_r(h)\binom{e(h)}j.
\]
Here \(A_{r,j}\) lies in the unramified coefficient ring \(\mathbb Z_p[\mu_N]\), with \(v_\pi(p)=p-1\).

**3. First nonzero residue coefficient.** Fix \(r\in\{1,\ldots,N-1\}\) and set \(k=\min(r,N-r)\). Because \(N\le p+1\), we have \(1\le k\le(p+1)/2<p\). Reduction modulo \(p\) of \(\binom{e(h)}j\) is a polynomial of degree \(j\) in \(L(h)=(h+h^{-1})/2\) with leading term \(L(h)^j/j!\). Every monomial arising in \(h^r L(h)^i\) for \(0\le i\le j\) has exponent of the form \(r+i-2a\), \(0\le a\le i\). If \(j<k\), no such exponent is a multiple of \(N\); character orthogonality therefore gives \(A_{r,j}\equiv0\pmod p\). In fact \(A_{r,0}=\sum_h\chi_r(h)=0\) identically.

At \(j=k\), precisely one extremal monomial contributes to exponent zero modulo \(N\), except that two contribute when \(r=k=N/2\). Consequently,
\[
A_{r,k}\equiv\frac{N}{2^k k!}
\begin{cases}2,&r=N/2,\\1,&r\ne N/2\end{cases}
\pmod p.
\]
All factors on the right are units modulo the odd prime \(p\). Thus \(v_\pi(A_{r,k})=0\).

For \(1\le j<k\), the divisibility \(p\mid A_{r,j}\) implies \(v_\pi(\pi^jA_{r,j})\ge p-1+j>k\). The term \(j=0\) vanishes, and terms with \(j>k\) have valuation at least \(j>k\). No cancellation of the unique leading \(\pi^k\) term is possible. Hence \(v_\pi(B_r)=k\). For \(r=0\), \(B_0\equiv N\not\equiv0\pmod\pi\), giving valuation zero.

**4. Descent and complete list.** Since \(\mathcal O'/\mathcal O\) is unramified, extension of scalars preserves Smith exponents. The elementary divisors are therefore \(\min(r,N-r)\) for \(0\le r<N\). For \(N=2m\), this lists zero once, each \(1\le j<m\) twice, and \(m\) once. All the \(B_r\) are nonzero, so \(F_p\) is invertible over the cyclotomic fraction field and hence over \(\mathbb C\). Summing the exponents gives \(2\sum_{j=1}^{m-1}j+m=m^2\).

## Verification
The standalone `verify_conic_torus.py` independently constructs the conic in six prime fields \(p=3,5,7,11,13,17\), represents each Fourier entry by \((1+t)^{e}\) in the finite ring \(\mathbb F_p[t]/(t^L)\), and obtains the elementary divisor counts by exact modular Gaussian elimination. It compares the counts with the stated list at every checked truncation length through \(\min(p-1,m+1)\), and independently computes \(\det F_3=9\) by exact reduction modulo \(\zeta_3^2+\zeta_3+1\). Run `python3 verify_conic_torus.py` with the Python 3 standard library; successful output ends `CONIC_TORUS_LOCAL_SMITH_PASS`. Such finite checks do not prove the statement for every prime; the character-orthogonality argument does.

## Relationship to prior work
Finite-field Bessel functions are traditionally sums of additive characters twisted by norm-one-torus characters; Khekalo (2001) develops these kernels and identities. The present proof uses the familiar multiplicative Fourier diagonalization but extracts the entire local Smith invariant sequence of the self-conic Fourier restriction matrix. González Vieli (first online 2011-12-08) establishes a Euclidean-sphere uniqueness result via classical Bessel functions; its continuum setting does not imply the finite-field cyclotomic Smith valuation sequence. Garcia, Karaali and Katz (2018) treat symmetry-compressed Fourier matrices, minor nonvanishing, and Gauss sums on multiplicative subgroups of finite fields; their matrices have different source and frequency supports. Other previously described finite-conic tomography results concern unions of entire frequency lines and dihedral fibre sums rather than Fourier sampling on the conic itself. These are statement-level distinctions, not a proof of exhaustive historical priority.

## Limitations
The theorem is local at the cyclotomic prime over \(p\), not an exact Archimedean singular-value analysis or a complete classification of all Fourier minors. Only \(q=p\) with odd prime \(p\) is covered; characteristic two, extension fields and other quadratic varieties need separate arguments. Historical priority might be affected by an existing general valuation theorem for finite Bessel sums or Gauss sums not found in the bounded comparison. An independently performed review has not taken place.

## References
1. S. P. Khekalo, *The Bessel function on a finite field*, Izv. Vyssh. Uchebn. Zaved. Mat., 2001, no. 2, pp. 79–82. Full text: https://www.mathnet.ru/php/getFT.phtml?jrnid=ivm&option_lang=eng&paperid=855&what=fullt .
2. S. González Vieli, *A Uniqueness Result for Fourier Transform of Measures on the Sphere*, Bulletin of the Australian Mathematical Society, first published online 2011-12-08, DOI:10.1017/S0004972711002942.
3. S. R. Garcia, G. Karaali, D. J. Katz, *An improved uncertainty principle for functions with symmetry*, arXiv:1807.07648, first posted 2018-07-19.
