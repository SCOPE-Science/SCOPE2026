# Central Walsh slice minors: an invertibility threshold and a Catalan conditioning jump

## Finding

For every integer \(k\ge 1\), set \(n=2k+a\), where \(a\in\{0,1,2\}\). Let \(\Omega_{n,k}\) be the collection of \(k\)-element subsets of \([n]\), and let \(W_{n,k}\) be the real symmetric matrix indexed by \(\Omega_{n,k}\) with entries
\[
W_{n,k}(A,B)=(-1)^{|A\cap B|}.
\]
This is an unnormalized principal submatrix of the Boolean Walsh–Hadamard transform. It has \(\binom{n}{k}\) rows and columns.

For \(j=0,\ldots,k\), put \(m=k-j\). The complete real spectrum is \(\lambda_j\) with multiplicity \(\binom nj-\binom n{j-1}\) (where \(\binom n{-1}=0\)), with
\[
\lambda_j=(-2)^j [z^m](1-z^2)^m(1+z)^a.
\]
The coefficients, including their signs, are exactly:

* \(a=0\): \([z^{2h}](1-z^2)^{2h}=(-1)^h\binom{2h}{h}\), and the coefficient vanishes for \(m=2h+1\).
* \(a=1\): the coefficient is \((-1)^h\binom{m}{h}\) for both \(m=2h\) and \(m=2h+1\).
* \(a=2\): for \(m=2h\) the coefficient is \((-1)^h C_h\), where \(C_h=\binom{2h}{h}/(h+1)\) is the \(h\)-th Catalan number; for \(m=2h+1\) it is \(2(-1)^h\binom{2h+1}{h}\).

Consequently, \(W_{2k,k}\) has rank exactly \(\frac12\binom{2k}{k}\), while both \(W_{2k+1,k}\) and \(W_{2k+2,k}\) are invertible. Their sharp spectral condition numbers are
\[
\boxed{\kappa_2(W_{2k+1,k})=\frac{2^k}{\binom{k}{\lfloor k/2\rfloor}},\qquad
\kappa_2(W_{2k+2,k})=\frac{4^{\lfloor k/2\rfloor}}{C_{\lfloor k/2\rfloor}}.}
\]
In particular,
\[
\kappa_2(W_{2k+1,k})\sim\sqrt{\frac{\pi k}{2}},\qquad
\kappa_2(W_{2k+2,k})\sim\frac{\sqrt{\pi}}{2\sqrt2}k^{3/2}.
\]
The exact ratio of the second condition number to the first is \((k+2)/2\) for even \(k\), and \(k/2\) for odd \(k\). Thus the passage from \(n=2k\) to \(n=2k+1\) restores unique interpolation, but adding another coordinate increases the sharp condition number by an asymptotic factor \(k/2\).

## Assumptions and scope

The field is \(\mathbb R\) or \(\mathbb C\); the matrix entries are \(\pm1\) with no normalization factor. The indices \(k,n,a,j,m,h\) have the ranges stated above, and the condition number uses the Euclidean operator norm \(\|W\|_2\|W^{-1}\|_2\) only for invertible \(W\). No claim is made for general \(n-2k\) outside \(\{0,1,2\}\), or for other alphabets or complex Fourier phases.

## Proof

**Harmonic decomposition and exact eigenvalue.** For each \(j\), choose \(j\) pairwise disjoint ordered pairs \((a_i,b_i)\) of points in \([n]\) and consider the function
\[
v(A)=\prod_{i=1}^j\bigl(\mathbf1_{a_i\in A}-\mathbf1_{b_i\in A}\bigr)
\quad(A\in\Omega_{n,k}).
\]
The standard harmonic decomposition on the Johnson slice states that these degree-\(j\) pair-difference functions span the \(j\)-th harmonic sector \(\mathcal H_j\), that the sectors are pairwise orthogonal and exhaust functions on the slice, and that \(\dim\mathcal H_j=\binom nj-\binom n{j-1}\). This standard fact can also be obtained from the pair-difference basis constructed in Filmus, Theorem 5.1 and Lemma 5.2; its dimension formula is independently recorded in his Lemma 2.1.

To calculate \(Wv\), sum over all \(B\in\Omega_{n,k}\). For any \(A\), the sum over the two choices of one element from the \(i\)-th distinguished pair contributes
\[
(-1)^{\mathbf1_{a_i\in A}}-(-1)^{\mathbf1_{b_i\in A}}.
\]
This factor is zero unless \(A\) contains exactly one member of the pair; otherwise it equals \(-2(\mathbf1_{a_i\in A}-\mathbf1_{b_i\in A})\). If any factor vanishes then both \(v(A)\) and \((Wv)(A)\) vanish. In the remaining case, \(A\) contains exactly one element from every selected pair, leaving \(m=k-j\) elements in the other \(n-2j=2m+a\) positions. Summing the remaining \(m\)-element subsets gives the coefficient
\[
\sum_{s=0}^m (-1)^s\binom ms\binom{m+a}{m-s}
=[z^m](1-z)^m(1+z)^{m+a}
=[z^m](1-z^2)^m(1+z)^a.
\]
Thus \(Wv=\lambda_jv\) with the stated \(\lambda_j\). The standard harmonic basis proves this is the *entire* spectrum with the stated multiplicities, not just a list of observed eigenvalues.

**Coefficient evaluation.** Expand \((1-z^2)^m\) and then multiply by \((1+z)^a\). For \(a=0,1\), the displayed binomial values follow immediately. For \(a=2\) and even \(m=2h\), the alternating coefficient reduces to
\[
(-1)^h\left(\binom{2h}{h}-\binom{2h}{h-1}\right)
=(-1)^h\frac1{h+1}\binom{2h}{h}.
\]
For odd \(m=2h+1\), only the middle term \(2z\) in \((1+z)^2\) contributes, giving \(2(-1)^h\binom{2h+1}{h}\).

**Rank and sharp singular extrema.** For \(a=0\), precisely the odd \(m\) sectors vanish, and the even sectors do not. Alternatively, for any \(A\in\Omega_{2k,k}\), the complementary column obeys \(W(\cdot,A^c)=(-1)^kW(\cdot,A)\), so rank is at most half the matrix size. The explicit nonzero sectors attain that bound, yielding rank \(\binom{2k}{k}/2\).

For \(a=1\) or \(a=2\), all displayed coefficients are nonzero. In each case the maximum absolute eigenvalue is \(2^k\): divide \(|\lambda_j|\) by \(2^k\) and write the result as the absolute coefficient divided by \(2^m\). For \(a=1\) these ratios are \(\binom m{\lfloor m/2\rfloor}/2^m\), a nonincreasing sequence in \(m\). The minimum occurs at \(m=k\) and is \(\binom k{\lfloor k/2\rfloor}/2^k\). For \(a=2\), the even-indexed ratios are \(C_h/4^h\) at \(m=2h\), strictly decreasing in \(h\); the odd-indexed ratios at \(m=2h+1\) equal \((2h+1)C_h/4^h\), are nonincreasing in \(h\), and are at least the adjacent even ratio. The global minimum therefore occurs at the largest even \(m=2\lfloor k/2\rfloor\) and equals \(C_{\lfloor k/2\rfloor}/4^{\lfloor k/2\rfloor}\). Since a real symmetric matrix has singular values equal to the absolute eigenvalues, the two condition-number formulas follow.

Finally, the central binomial estimate \(\binom{k}{\lfloor k/2\rfloor}\sim 2^k\sqrt{2/(\pi k)}\) and the Catalan estimate \(C_h\sim4^h/(\sqrt\pi h^{3/2})\) give the claimed asymptotics. The exact ratio follows from \(C_h=\binom{2h}{h}/(h+1)\) and \(\binom{2h+1}{h}=\frac{2h+1}{h+1}\binom{2h}{h}\).

## Verification

A standalone Python checker reproduces the claimed spectrum and multiplicities by constructing the actual signed-intersection matrices for \(1\le k\le4\) and every \(a\in\{0,1,2\}\), comparing against independent numerical symmetric eigenspectra and condition numbers. It also checks the coefficient formulas arithmetically for all \(1\le k\le149\) and three values of \(a\), giving 447 symbolic parameter sets. The checker uses Python 3 and NumPy; the exact proof above does not rely on floating-point computation. Run `python3 check_near_middle.py` from the extracted package. Observed result: `NEAR_MIDDLE_WALSH_SPECTRUM_PASS` with 12 constructed matrices and largest order 210.

## Relationship to prior work

The Johnson-slice harmonic decomposition and the simultaneous eigenbasis for every kernel depending only on \(|A\cap B|\) are established in Filmus (2014 preprint; 2016 journal), especially Theorem 5.1 and Lemma 5.2. Podestá (2016 preprint) develops reduction identities for binary Krawtchouk polynomials and binomial/Catalan relations. Those foundational results supply relevant machinery and overlapping coefficient identities; the claim here is restricted to the *sharp three-dimension rank and conditioning transition* for the specific principal Fourier compression, with all its spectral multiplicities and exact extremal sectors. The comparison is bounded rather than a priority certificate: a broader result on specialized Johnson-scheme eigenvalue extremality might imply this statement.

## Limitations

The argument treats the unnormalized binary kernel only, for the three exact ambient dimensions \(n=2k\), \(2k+1\), and \(2k+2\). The matrix at \(n=2k\) is singular, so no ordinary spectral condition number is assigned to it. Large-\(k\) asymptotics concern fixed offset \(a\), not a moving offset or general fixed-weight Fourier minors. Literature priority has not been independently certified; the cited standard Johnson harmonic framework is not claimed as new. Numerical checks are finite and do not constitute the all-rank proof.

## References

1. Yuval Filmus, *Orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142 (first public 2014-06-01). https://arxiv.org/abs/1406.0142 . In particular, Lemma 2.1, Theorem 5.1, and Lemma 5.2.
2. Ricardo A. Podestá, *New identities for binary Krawtchouk polynomials, binomial coefficients and Catalan numbers*, arXiv:1603.09156 (first public 2016-03-30). https://arxiv.org/abs/1603.09156 . In particular, Sections 2, 5, and 6.
