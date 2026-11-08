# Exact order-five binary permutation Fourier spectrum and endpoint norm

## Finding

Let \(G=M_5(\mathbb F_2)\), with pairing \(\langle A,B\rangle=\sum_{i,j=0}^{4}A_{ij}B_{ij}\) in \(\mathbb F_2\), and let \(\mathcal P\subset G\) consist of the \(120\) permutation matrices. Use the unnormalized Walsh transform
\[
\widehat f(A)=\sum_{B\in G}f(B)(-1)^{\langle A,B\rangle}.
\]
The complete absolute-value distribution of \(\widehat{\mathbf1_{\mathcal P}}\) is

| \(t\) | \(0\) | \(8\) | \(16\) | \(24\) | \(32\) | \(48\) | \(72\) | \(120\) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Number of \(A\in G\) with \(|\widehat{\mathbf1_{\mathcal P}}(A)|=t\) | 10,342,400 | 15,267,840 | 5,959,680 | 1,561,600 | 307,200 | 102,400 | 12,800 | 512 |

Consequently, the Fourier projection \(P_{\mathcal P}\) with multiplier \(\mathbf1_{\mathcal P}\) has the **sharp** endpoint norms
\[
\boxed{\|P_{\mathcal P}\|_{\ell^1(G)\to\ell^1(G)}=\|P_{\mathcal P}\|_{\ell^\infty(G)\to\ell^\infty(G)}=\frac{33045}{4096}.}
\]
Its convolution kernel vanishes at exactly \(10,342,400\) group elements and is nonzero at exactly \(23,212,032\). An independent uniform random \(5\)-by-\(5\) sign matrix has vanishing **integer** permanent with exact probability \(2525/8192\).

## Assumptions and scope

The ambient additive group, Fourier convention, and frequency set are exactly those defined above. Matrix entries in the Walsh pairing are binary, while the permanent of a sign matrix is computed in the ordinary integers. The result concerns the single natural order \(5\), not arbitrary matrix sizes, matrix determinants, or the Fourier transform on the abstract symmetric group.

## Proof

**1. Fourier–permanent identity.** For a permutation \(\pi\in S_5\), write \(E_\pi\) for its permutation matrix. Then
\[
\widehat{\mathbf1_{\mathcal P}}(A)=\sum_{\pi\in S_5}\prod_{i=0}^{4}(-1)^{A_{i,\pi(i)}}=\operatorname{per}\bigl((-1)^{A_{ij}}\bigr).
\]
This identifies the complete absolute Fourier spectrum with the integer absolute-permanent distribution of sign matrices.

**2. Gauge normalization.** Multiplying any row or column of a sign matrix by \(-1\) changes the permanent by only an overall sign. Every \(5\)-by-\(5\) sign matrix is uniquely normalized to first row and first column all \(+1\) once the gauge action is taken modulo its simultaneous global sign. Exactly \(2^9=512\) original sign matrices correspond to each normalized sign matrix. Such normalized matrices are in bijection with the \(2^{16}=65536\) assignments of four binary negative-entry masks \(r_1,r_2,r_3,r_4\in\{0,\ldots,15\}\) to the lower-right \(4\)-by-\(4\) block.

**3. Finite exact coefficient calculation.** For \(T\subseteq\{0,1,2,3,4\}\), let \(k=|T|\) and let \(T'=T\cap\{1,2,3,4\}\). If \(r\) is identified with a subset of \(\{1,2,3,4\}\), then the sum of the entries of the corresponding normalized sign row over \(T\) is \(k-2|r\cap T'|\). Inclusion–exclusion for the permanent gives the explicit integer expression
\[
\Phi(r_1,r_2,r_3,r_4)=\sum_{T\subseteq\{0,1,2,3,4\}}(-1)^{5-|T|}|T|\prod_{i=1}^{4}\bigl(|T|-2|r_i\cap T'|\bigr).
\]
No unexamined sign configurations remain: each of the \(16^4\) choices is included exactly once. The following identity is an **exact finite integer coefficient identity**, not a numerical approximation:
\[
\sum_{r_1,r_2,r_3,r_4=0}^{15}z^{|\Phi(r_1,r_2,r_3,r_4)|}=20200+29820z^8+11640z^{16}+3050z^{24}+600z^{32}+200z^{48}+25z^{72}+z^{120}.
\]
For a smaller exhaustive certificate, reorder the four lower rows into a multiset of their \(16\) possible masks. There are \(\binom{19}{4}=3876\) multisets. A multiset with mask multiplicities \(m_r\) contributes the exact integer weight \(4!/\prod_r m_r!\). This weighted orbit enumeration yields precisely the same coefficient identity. The standalone checker independently evaluates the permanent both as the sum of all \(5!\) perfect-matchings and by the above inclusion–exclusion identity, for **every one** of the \(65536\) normalized matrices, and also checks the \(3876\)-multiset weighted count. The certificate is included as `check_permutation_wiener.py` and requires Python 3.10 or newer and no external modules.

**4. Fourier counts and sharpness.** Multiply each coefficient in the displayed polynomial by the gauge-fiber size \(512\) to obtain the table for all \(2^{25}\) Walsh frequencies. The number of zero frequencies is \(512\cdot20200=10342400\). The operator is convolution by \(K(A)=2^{-25}\widehat{\mathbf1_{\mathcal P}}(A)\). Every convolution operator on a finite group has \(\ell^1\)- and \(\ell^\infty\)-operator norms equal to the \(\ell^1\)-norm of its kernel: the point mass and a phase-aligned test function attain the two bounds. Thus
\[
\|P_{\mathcal P}\|=\sum_{A\in G}|K(A)|=\frac1{65536}\sum_{r_1,\ldots,r_4}|\Phi(r_1,\ldots,r_4)|=\frac{528720}{65536}=\frac{33045}{4096}.
\]
The vanishing-permanent probability is the same as the normalized zero proportion \(20200/65536=2525/8192\), because gauge normalization preserves the absolute permanent.

## Verification

Run `python check_permutation_wiener.py`. All integer operations are exact. The program checks the \(65536\)-element exhaustive domain using two algebraically distinct permanent algorithms, independently checks the \(3876\)-orbit weighted domain, verifies every table coefficient and their sum, verifies the random-permanent second moment \(\mathbb E|\operatorname{per}B|^2=120\), and checks the exact norm, zero probability and Fourier support count. Marker: `THREE_ENUMERATION_CERTIFICATES_PASS`. The proof is a finite exhaustive proof; it does not infer a universal-in-dimension law from small cases.

## Relationship to prior work

Wanless, *Permanents of matrices of signed ones*, studies possible values and the least positive permanent, including order \(5\), but its inspected results do not provide the **absolute-permanent multiplicity distribution** or the resulting Walsh-projection endpoint norm. Tao and Vu, *On the permanent of random Bernoulli matrices*, prove an asymptotic nonvanishing/magnitude theorem and state the second-moment formula, neither of which fixes the exact finite distribution here. Sanders' Fourier-algebra work motivates the study of \(\ell^1\) norms of indicator transforms, but provides no explicit order-five permutation-frequency computation. This is a bounded literature comparison, not a claim of exhaustive historical priority.

## Limitations

This is a complete **finite** theorem for \(M_5(\mathbb F_2)\), not a theorem for higher orders or other fields. The orbit-polynomial identity is certified by a finite exhaustive exact-arithmetic program rather than a compact hand-derived closed form for its coefficients. It gives no asymptotic estimate for large random permanents. The literature search may have missed an older equivalent enumeration. Independent mathematical validation has not been performed.

## References

1. I. M. Wanless, *Permanents of matrices of signed ones*, Linear and Multilinear Algebra 53 (2005), 427–433. DOI: `10.1080/03081080500093990`; lawful author-hosted full text: `https://users.monash.edu.au/~iwanless/papers/wangconjLAMA.pdf`.
2. T. Tao and V. Vu, *On the permanent of random Bernoulli matrices*, arXiv:0804.2362 (first arXiv submission 2008-04-15), `https://arxiv.org/abs/0804.2362`.
3. T. Sanders, *The \(\ell^1\)-norm of the Fourier transform on compact vector spaces*, arXiv:math/0605519 (initial submission 2006-05-18), `https://arxiv.org/abs/math/0605519`.
