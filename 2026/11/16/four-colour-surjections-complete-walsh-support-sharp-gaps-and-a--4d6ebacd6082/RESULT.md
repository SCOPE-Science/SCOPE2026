# Four-colour surjections: complete Walsh support, sharp gaps and a parity jump in projection contractivity

## Finding
For every integer \(n\ge4\), consider the onto words \(A_n\subseteq V^n\), with \(V=\mathbb F_2^2\) the four-letter alphabet. Under the unnormalized Walsh transform, the indicator of \(A_n\) has no zeros except the characters forced by common-alphabet translation **when \(n\) is even**. When \(n\) is odd, exactly \((3^n-3)/4\) additional characters vanish. Consequently, convolution by this indicator has rank
\[
\operatorname{rank} C_n=\begin{cases}4^{n-1},&n\text{ even},\\4^{n-1}-(3^n-3)/4,&n\text{ odd} .\end{cases}
\]
Every Walsh coefficient is given explicitly below. The least positive *absolute* nonzero eigenvalue equals \(8\) for even \(n\) and \(16\) for odd \(n\). Thus \(\|C_n^\dagger\|_{2\to2}\) is respectively \(1/8\) or \(1/16\). The maximal absolute eigenvalue is the number of surjections \(4^n-4\cdot3^n+6\cdot2^n-4\), so division by \(8\) or \(16\) gives the exact nonzero-singular-value condition number.

Let \(R_n\) be the convolution range. The smallest possible \(\ell^1\)- and \(\ell^\infty\)-operator norms of projections onto \(R_n\) are exactly \(1\) when \(n\) is even and are **strictly larger than \(1\)** when \(n\) is odd. This is a norm-one complementability dichotomy; no closed formula for the odd-length endpoint norm is claimed.

## Assumptions and scope
Use the bilinear pairing on \(V=\mathbb F_2^2\), the additive group \(G_n=V^n\), and \(\chi_b(x)=(-1)^{\sum_i b_i\cdot x_i}\). Let \(f_n=\mathbf1_{A_n}\), where \(A_n\) consists exactly of words in which every member of \(V\) appears at least once. Set
\[
W_n(b)=\sum_{x\in G_n}f_n(x)\chi_b(x),\qquad
S(b)=\sum_i b_i\in V,\quad z(b)=\#\{i:b_i=0\},\quad k=n-z(b).
\]
Put \(t(b)=\#\{b_i:b_i\ne0\}\), the number of distinct nonzero frequency letters. The convolution is the *unnormalized* operator \((C_n h)(x)=\sum_y f_n(y)h(x-y)\) acting on counting-measure \(\ell^p(G_n)\). Its eigenvalues on Walsh characters are the signed integers \(W_n(b)\).

For every \(b\in G_n\), the **complete signed-multiplier formula** is
\[
W_n(b)=\begin{cases}
0,&S(b)\ne0,\\
4^n-4\cdot3^n+6\cdot2^n-4,&b=0,\\
2^{n+1}-4(1+3^{z(b)}),&S(b)=0,\quad t(b)=1,\\
-4(1+(-1)^{k}3^{z(b)}),&S(b)=0,\quad t(b)\ge2.
\end{cases}
\]
This formula also specifies all multiplicities: for each \(z\) with \(k=n-z>0\), put \(B_k=(3^k+3(-1)^k)/4\). Among the \(\binom nz B_k\) balanced frequencies with exactly \(z\) zero coordinates, precisely \(3\binom nz\) have \(t=1\) if \(k\) is even, and none if \(k\) is odd; the remainder have \(t\ge2\). Add the trivial frequency and the \(4^n-4^{n-1}\) unbalanced zeros. Coincident numerical values from different rows are understood to have their multiplicities added.

## Proof
**1. Exact transform by inclusion–exclusion.** For any allowed alphabet \(U\subseteq V\), the signed sum over words with letters in \(U\) factorizes as \(\prod_i\sum_{u\in U}\chi_{b_i}(u)\). Use inclusion–exclusion over the four forbidden letters. If \(S(b)\ne0\), translating all word letters by the same element of \(V\) pairs character values with opposite sign, so the coefficient vanishes. Suppose \(S(b)=0\). The four allowed singletons contribute \(-4\). Each three-letter allowed set, obtained by deleting \(u\), contributes \((-1)^k3^z\chi_{S(b)}(u)=(-1)^k3^z\), and its inclusion–exclusion sign is negative; together they contribute \(-4(-1)^k3^z\).

An allowed pair is \(\{u,u+d\}\) with \(d\ne0\). Its coordinate character sum vanishes unless \(b_i\cdot d=0\) for every \(i\); otherwise the product is \(2^n\chi_{S(b)}(u)=2^n\). There are two unordered pairs for each nonzero \(d\). Two distinct nonzero vectors of \(V\) are linearly independent, so for \(b\ne0\) a permitted \(d\) exists precisely when \(t(b)=1\), and then exactly one \(d\) works. Therefore pair contributions are \(2^{n+1}\) when \(t=1\) and zero when \(t\ge2\). For \(b=0\), all three directions work, contributing \(6\cdot2^n\); the full alphabet contributes \(4^n\) only at \(b=0\). This proves the formula with all signs and normalization.

**2. Classification of zeros and multiplicities.** With \(S=0\) and \(t=1\), the nonzero letter must appear an even number \(k\ge2\) of times. Thus \(W=4(2^{n-1}-1-3^z)\), which never vanishes when \(n\ge4\): modulo \(8\), \(2^{n-1}\equiv0\), whereas \(1+3^z\) is congruent to \(2\) or \(4\). With \(t\ge2\), cancellation requires simultaneously \(z=0\) and odd \(k=n\). Write the three nonzero vectors of \(V\) as \(a,c,a+c\); a zero vector sum for a frequency containing no zeros holds precisely when their three occurrence counts have the same parity. Since \(n\) is odd, each count must be odd. The number of ordered sequences of nonzero frequency vectors with sum zero is \(B_n=(3^n-3)/4\), obtained by character orthogonality because \(\sum_{v\ne0}\chi_u(v)=-1\) for \(u\ne0\). They are exactly the extra zeros. More generally the same orthogonality gives \(B_k\) and the signed-spectrum multiplicities above. The hyperplane \(S=0\) contains \(4^{n-1}\) frequencies, proving the rank formula.

**3. Sharp gap.** At even \(n\), every nonzero balanced frequency multiplier is divisible by \(8\): in the \(t\ge2\) case, \(1\pm3^z\) is even; the \(t=1\) case and the trivial coefficient have the same divisibility. Choose two occurrences of a nonzero vector \(a\), two of a distinct nonzero \(c\), and fill remaining coordinates with paired copies of \(a\). Then \(z=0\), \(t\ge2\), \(S=0\), giving \(W=-8\). At odd \(n\), every nonzero balanced frequency multiplier is divisible by \(16\). If \(t\ge2\), parity of \(n\) forces \(k\) and \(z\) to have opposite parity, and \(1+(-1)^k3^z\) is divisible by \(4\). If \(t=1\), \(k\) is even, so \(z\) is odd, and \(2^{n-1}-1-3^z\) is divisible by \(4\); the same holds for the trivial coefficient because \(3^n\equiv3\pmod4\). Choose two copies each of distinct nonzero \(a,c\), one zero coordinate, and fill all remaining positions with paired copies of \(a\). This gives \(z=1\), \(t\ge2\), \(S=0\), hence \(W=-16\). Both divisibility bounds are attained. The eigenvalue maximum in absolute value is \(W_n(0)=|A_n|\) by the triangle inequality, giving all claimed \(\ell^2\) consequences.

**4. Endpoint projection dichotomy.** Let \(D=\{(v,\ldots,v):v\in V\}\) and \(H=D^\perp=\{b:S(b)=0\}\). The unique translation-invariant projection onto \(R_n\) has Fourier multiplier \(\mathbf1_{\{W_n\ne0\}}\). Translation-averaging any projection onto this translation-invariant range cannot increase its \(\ell^1\) or \(\ell^\infty\) norm and produces that unique projection, so its norm is the minimum among *all* projections onto \(R_n\). For even \(n\), this is averaging over the four translates in \(D\), of norm exactly \(1\).

For odd \(n\ge5\), let \(E\subset H\) be the exceptional frequencies (all coordinates nonzero and each of the three nonzero symbols occurring an odd number of times). The unique projection kernel is
\[
p_n(x)=\frac14\mathbf1_D(x)-4^{-n}\sum_{b\in E}\chi_b(x).
\]
Take \(x=(a,c,0,\ldots,0)\) with \(a,c\) distinct nonzero members of \(V\). Then \(x\notin D\). By permutation symmetry among the three nonzero frequency letters, among frequencies in \(E\) the number with \(b_1=b_2=v\), for any fixed nonzero \(v\), is \(A=(3^{n-2}-3)/4\), while the number with \((b_1,b_2)=(v,w)\), for any fixed distinct nonzero \(v,w\), is \(B=(3^{n-2}+1)/4\). These counts follow from the same character-orthogonality formula on the remaining \(n-2\) positions. The diagonal sign products sum to \(-1\), and the six ordered off-diagonal sign products sum to \(2\); hence
\[
\sum_{b\in E}\chi_b(x)=-A+2B=\frac{3^{n-2}+5}{4}>0,
\qquad p_n(x)=-\frac{3^{n-2}+5}{4^{n+1}}<0.
\]
Since \(\sum_xp_n(x)=1\), the total-variation norm \(\sum_x|p_n(x)|\), which is the convolution operator norm at both endpoints, is strictly larger than \(1\). This proves the dichotomy without assuming an unavailable formula for the odd-length norm.

## Verification
The standalone standard-library checker `verify.py` independently enumerates every onto word and computes the *entire integer Walsh transform* for each \(n=4,5,6,7,8,9\), then compares each coefficient to the formula, the claimed rank and the sharp gap. The six tests comprise \(349{,}440\) frequency coefficients. It separately constructs the Fourier projection via its kernel for \(n=4,5,6,7\), tests the explicit negative-kernel witness, and obtains exact endpoint norms \(1\), \(91/16\), \(1\), and \(14107/1024\), respectively. The printed completion marker is `QUATERNARY_SURJECTION_WALSH_EXACT_PASS`. These are finite checks of, not substitutes for, the all-length argument.

## Relationship to prior work
Stirling enumeration of set partitions and onto words is classical; Bóna and Mező (first public version 2007-05-18) study restricted set partitions and their real-zero generating polynomials, not all Walsh characters of onto words. Carayol and Rotondo (2026) study profile sampling of surjections under relabelling, which does not give the character-resolved convolution eigenvalues. A closely relevant published Fourier study of all \(q\)-colour surjective words determines only the probability-normalized *first-coordinate Fourier sampling Gram spectrum*, not the complete Fourier transform of the onto-word indicator; its sampled degree-one Gram correlations cannot imply the complete all-degree support and gap. Classical inclusion–exclusion supplies the starting identity; the zero classification, exact resonance count, sharp divisibility gap, and endpoint-projection transition are the claims here. See references. An earlier equivalent character-weighted occupancy formula could cover the same result and remains a historical-priority risk.

## Limitations
The result is for the additive Klein-four alphabet, not automatically the cyclic group of order four or every four-letter group structure. No closed all-length expression for the endpoint projection norm at odd \(n\) is supplied; only its strict separation from \(1\) is proved. The result assumes \(n\ge4\); smaller lengths have no onto words. Historical-priority comparison is bounded, and there has been no independent mathematical validation.

## References
- M. Bóna and I. Mező, *Real Zeros and Partitions without singleton blocks*, arXiv:0705.2734, first submitted 2007-05-18; https://arxiv.org/abs/0705.2734 .
- A. Carayol and P. Rotondo, *Efficient sampling of the unlabeled structure of uniform random mappings and surjections*, arXiv:2605.24068, first submitted 2026-05-22; https://arxiv.org/abs/2605.24068 .
- *Exact first-band Fourier sampling spectra on surjective words*, published 2026; https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-first-band-fourier-sampling-spectra-on-surjective-words--38dfe55b7163 .
