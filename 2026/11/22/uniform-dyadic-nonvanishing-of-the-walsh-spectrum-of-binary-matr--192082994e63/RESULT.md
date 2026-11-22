# Uniform dyadic nonvanishing of the Walsh spectrum of binary matrix derangements

## Finding

For every integer \(n\ge2\), let \(\mathcal D_n\) consist of all invertible \(n\times n\) matrices over \(\mathbb F_2\) with zero diagonal. Regard their \(n(n-1)\) off-diagonal entries as elements of the additive group \(G_n=\mathbb F_2^{n(n-1)}\). Define, for every frequency \(B\in G_n\), the unnormalized binary Walsh multiplier
\[
W_n(B)=\sum_{X\in\mathcal D_n}(-1)^{\sum_{i\ne j}B_{ij}X_{ij}}.
\]
**Theorem.** If \(e_n=\binom{n-1}{2}\), then every \(B\in G_n\) satisfies
\[
\boxed{W_n(B)\equiv 2^{e_n}\pmod{2^{e_n+1}}.}
\]
Consequently, every multiplier is nonzero with exact two-adic valuation \(e_n\). Counting convolution by \(1_{\mathcal D_n}\) is invertible on all real and complex functions on \(G_n\), with rank \(2^{n(n-1)}\) and determinant of exact two-adic valuation \(e_n2^{n(n-1)}\). Its Hilbert-space inverse norm is at most \(2^{-e_n}\). The last upper bound is not asserted to be sharp for all sizes.

## Assumptions and scope

Matrices and ranks are over \(\mathbb F_2\); \(n\ge2\) is arbitrary. Frequencies are supported on off-diagonal coordinates only. The Walsh transform is the unnormalized character sum, and convolution uses counting measure, not probability normalization. The two-adic valuation of an integer is the exponent of the largest power of two dividing its absolute value. The case \(n=1\) is excluded because the zero-diagonal matrix is singular.

## Proof

**Rank-character formula.** For an arbitrary binary \(n\times n\) frequency matrix \(C\) of rank \(r\), let
\[
H_n(C)=\sum_{X\in\mathrm{GL}_n(\mathbb F_2)}(-1)^{\operatorname{tr}(C^{\mathsf T}X)}.
\]
Then
\[
H_n(C)=(-1)^r2^{\binom n2}\prod_{j=1}^{n-r}(2^j-1).\tag{1}
\]
Here the empty product is one. For completeness, use Möbius inversion on the lattice of binary subspaces: if \(U\le\mathbb F_2^n\) has dimension \(u\), its Möbius coefficient from zero is \((-1)^u2^{\binom u2}\). Writing \(R\) for the \(r\)-dimensional row space of \(C\), character orthogonality in the vector space of matrices vanishing on \(U\) gives
\[
H_n(C)=\sum_{u=r}^{n}{n-r\brack u-r}_2(-1)^u2^{\binom u2+n(n-u)}.\tag{2}
\]
Indeed, that inner character sum is zero unless \(R\subseteq U\), when it equals \(2^{n(n-u)}\), and there are \({n-r\brack u-r}_2\) such subspaces. Put \(k=n-r\), \(u=r+t\), and invoke the elementary Gaussian-binomial identity
\[
\sum_{t=0}^k{k\brack t}_2 2^{\binom t2}z^t=\prod_{j=0}^{k-1}(1+2^jz)
\]
with \(z=-2^{-k}\). This evaluates (2) as (1), including \(r=n\). The same rank-character evaluation is a special case of the bilinear-forms association scheme [2].

**Diagonal projection.** Extend \(B\) by inserting zero diagonal entries. Orthogonality for each diagonal coordinate gives
\[
W_n(B)=2^{-n}\sum_{d\in\mathbb F_2^n}H_n(B+\operatorname{diag}(d)).\tag{3}
\]
Define \(a_n(r)=(-1)^r\prod_{j=1}^{n-r}(2^j-1)\) and \(s_B=\sum_d a_n(\operatorname{rank}(B+\operatorname{diag}(d)))\). For \(n\ge3\), (1)–(3) yield the *integer* identity
\[
W_n(B)=2^{n(n-3)/2}s_B.\tag{4}
\]

**Oddness of invertible diagonal completions.** Let \(k_B\) denote the number of \(d\in\mathbb F_2^n\) for which \(B+\operatorname{diag}(d)\) is invertible. Over \(\mathbb F_2\), the polynomial \(\det(B+\operatorname{diag}(d))\) is multilinear in the variables \(d_i\) and has coefficient one on \(\prod_{i=1}^n d_i\), contributed by the identity permutation. Every other monomial omits at least one diagonal variable. Summing over all Boolean \(d\), each proper monomial contributes an even number, while the full product contributes exactly one. Hence
\[
k_B=\sum_{d\in\mathbb F_2^n}\det(B+\operatorname{diag}(d))\equiv1\pmod2.\tag{5}
\]

**Uniform valuation.** For every \(0\le r<n\), all factors \(2^j-1\) are odd, and
\[
a_n(r)\equiv (-1)^{n-1}\pmod4,
\qquad a_n(n)=(-1)^n.
\]
Thus by (5), for \(n\ge2\),
\[
s_B\equiv(-1)^{n-1}(2^n-2k_B)\equiv2\pmod4.\tag{6}
\]
For \(n\ge3\), equations (4) and (6) show that \(W_n(B)\) has exact two-adic valuation \(n(n-3)/2+1=\binom{n-1}{2}\), independently of \(B\). When \(n=2\), there is exactly one zero-diagonal invertible matrix, with off-diagonal entries both one, so every Walsh coefficient is \(+1\) or \(-1\); this has the asserted valuation zero. Finally, Walsh diagonalization of additive convolution gives all stated rank, determinant, and inverse-norm consequences. This completes the proof.

## Verification

The accompanying independent C++17 program enumerates every zero-diagonal binary matrix in sizes \(2\) through \(5\), computes its rank exactly, performs a complete integer Walsh transform, and verifies the uniform congruence on every character. The numbers of invertible matrices are respectively \(1,14,984,267968\). The numbers of Fourier characters are \(4,64,4096,1048576\), with no zero multipliers; their minimum absolute multipliers are respectively \(1,2,8,64\). The separate Python program verifies (1)–(3) against direct signed enumeration for all characters in sizes \(2\) through \(4\), plus further size-five completion tests. Both programs passed. These finite checks are confirmations, not the proof of the infinite theorem; the proof is above.

## Relationship to prior work

Lewis, Liu, Morales, Panova, Sam and Zhang [1] derive the *unsigned* number of zero-diagonal invertible matrices as a finite-field analogue of derangements. Their count is \(W_n(0)\), only one of the \(2^{n(n-1)}\) characters studied here. Delsarte [2] gives the rank-based finite-field Fourier framework that supplies the full-matrix transform (1), but the restriction to zero diagonal and the odd diagonal-completion lemma (5) are additional ingredients. Salmond, Grant, Grivell and Chan [3] examine full-rank probabilities with prescribed zero entries, but not the all-character Fourier spectrum. The theorem here combines these structures to show exact valuation and absence of Fourier zeros *simultaneously for every frequency*.

## Limitations

The theorem concerns only field order two and the complete zero-diagonal condition; it does not classify spectra for other prescribed-zero patterns or all finite fields. The global sharp smallest absolute multiplier at dimensions above five is not established. Independent mathematical validation has not been performed. A mathematically equivalent but unindexed treatment in the rank-metric or restricted-matrix literature cannot be ruled out by the bounded literature comparison.

## References

[1] J. B. Lewis, R. I. Liu, A. H. Morales, G. Panova, S. V. Sam and Y. X. Zhang, *Matrices with restricted entries and q-analogues of permutations*, first public arXiv version 2010-11-20, arXiv:1011.4539, Journal of Combinatorics 2 (2011), 355–396, DOI: 10.4310/JOC.2011.v2.n3.a2.

[2] P. Delsarte, *Bilinear Forms over a Finite Field, with Applications to Coding Theory*, Journal of Combinatorial Theory A 25 (1978), 226–241, Appendix Theorem A2, DOI: 10.1016/0097-3165(78)90015-8.

[3] D. Salmond, A. Grant, I. Grivell and T. Chan, *On the rank of random matrices over finite fields*, arXiv:1404.3250.
