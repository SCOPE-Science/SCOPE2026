# A three-step singularity law for ternary nowhere-zero flow convolution

## Finding
For each integer \(n\ge2\), let \(G_n=(\mathbb Z/3\mathbb Z)^n\) and let \(F_n\subset G_n\) consist of vectors with every coordinate nonzero and coordinate sum zero. Let \(T_n:\ell^2(G_n)\to\ell^2(G_n)\) be the **unnormalized** convolution operator
\[
(T_nh)(x)=\sum_{y\in F_n}h(x-y).
\]
For a frequency \(\xi\in G_n\), write \(c_j(\xi)=\#\{i:\xi_i=j\}\), for \(j=0,1,2\). The complete signed eigenvalue multiset, and hence the complete singular-value multiset after taking absolute values, is
\[
\boxed{\ \widehat {\mathbf1_{F_n}}(\xi)=\frac{(-1)^n}{3}\left[(-2)^{c_0(\xi)}+(-2)^{c_1(\xi)}+(-2)^{c_2(\xi)}\right].\ }
\]
Every eigenvalue is an integer. More explicitly, a value associated with any ordered triple of nonnegative integers \((a,b,c)\) summing to \(n\) occurs with frequency weight \(n!/(a!b!c!)\); weights are added when distinct triples give equal values.

A Fourier frequency is invisible **if and only if** its three symbol counts, in some order, are \((m,m,m+1)\) for an integer \(m\ge1\). Consequently,
\[
\boxed{\ T_n\text{ is invertible}\iff n\not\equiv1\pmod3,\qquad
\operatorname{nullity}(T_{3m+1})=\frac{3(3m+1)!}{m!^2(m+1)!}\quad(m\ge1).\ }
\]
In the other two congruence classes, the nullity is zero. In the singular progression, the fraction of invisible Fourier modes has the exact first-order asymptotic
\[
\boxed{\ \frac{\operatorname{nullity}(T_n)}{3^n}
=\frac{9\sqrt3}{2\pi n}\left(1+O(n^{-1})\right),\quad n\to\infty,\ n\equiv1\pmod3.\ }
\]
Thus singularity recurs at infinitely many lengths although the fraction of lost modes tends to zero. The recoverable rank is always \(3^n-\operatorname{nullity}(T_n)\).

## Assumptions and scope
This is the additive three-element alphabet, with every edge oriented alike in the dipole multigraph having two terminals and \(n\) parallel edges. The condition that every coordinate is nonzero and the total sum vanishes is precisely the nowhere-zero modular flow constraint. The group, frequencies, and convolution are over the **entire ambient group** \(G_n\), not the smaller flow subspace. The eigenvalue normalization is unnormalized counting convolution. The adjoint and singular values are for complex Hilbert space with counting measure. There are no conclusions here for prime powers other than three or for arbitrary graph topologies.

The basic count of flows is the classical identity
\[
|F_n|=\widehat{\mathbf1_{F_n}}(0)=\frac{2^n+2(-1)^n}{3};
\]
this unsigned counting formula is given only as a normalization check and is **not** claimed as new.

## Proof
**Character reduction.** Let \(\omega=e^{2\pi i/3}\). With the convention
\[\widehat f(\xi)=\sum_{x\in G_n}f(x)\omega^{-\xi\cdot x},\]
the Fourier characters diagonalize convolution. The indicator of the checksum constraint has the standard root filter
\[
\mathbf1_{\{\sum_i x_i=0\}}=\frac13\sum_{s=0}^2\omega^{s\sum_i x_i}.
\]
For \(r\in\mathbb Z/3\mathbb Z\), the local nonzero-coordinate character sum is
\[
\sum_{t=1}^2\omega^{rt}=\begin{cases}2,&r=0,\\-1,&r\ne0.\end{cases}
\]
Substitution and separation of coordinates give
\[
\widehat{\mathbf1_{F_n}}(\xi)
=\frac13\sum_{s=0}^2\prod_{i=1}^n\sum_{t=1}^2\omega^{(s-\xi_i)t}
=\frac13\sum_{s=0}^2 2^{c_s(\xi)}(-1)^{n-c_s(\xi)}.
\]
This is the displayed integer-valued eigenvalue formula because \((-2)^r\equiv1\pmod3\) for every integer \(r\ge0\). The frequency multiplicities are multinomial counts. Since \(F_n=-F_n\), all these eigenvalues are real, and the singular values are their absolute values.

**Exact zero classification.** Suppose \((-2)^a+(-2)^b+(-2)^c=0\) for nonnegative integers \(a,b,c\). Put \(m=\min(a,b,c)\). After dividing by \((-2)^m\), if the minimum occurs once, the resulting sum is odd and cannot be zero. If it occurs three times, the sum is three, not zero. Thus it occurs exactly twice. Writing the third exponent as \(m+d\), with \(d\ge1\), gives \(2+(-2)^d=0\), which holds exactly for \(d=1\). Hence precisely the exponent multisets \(\{m,m,m+1\}\) vanish. Their sum is \(3m+1\). At \(m=0\) the length is one, excluded by \(n\ge2\), so the singular cases are \(n=3m+1\) with \(m\ge1\).

**Rank and asymptotic.** For \(n=3m+1\), there are three choices for which frequency symbol occurs \(m+1\) times and \((3m+1)!/(m!^2(m+1)!)\) frequency words with those ordered counts. Each contributes one one-dimensional zero eigenspace. This proves the exact nullity and all invertibility assertions. Stirling's formula, applied with \(n=3m+1\), gives
\[
\frac{n!}{m!^2(m+1)!\,3^n}
=\frac{3\sqrt3}{2\pi n}\left(1+O(n^{-1})\right),
\]
and multiplication by three proves the stated lost-mode density.

## Verification
The accompanying `check.py` uses only integer arithmetic and does **not** call the roots-of-unity formula to calculate observed coefficients. For every length \(2\le n\le9\), it enumerates the actual nowhere-zero zero-sum words and, for every frequency, counts the phases \(0,1,2\) in the character sum directly. It verifies equality of the two nonreal phase counts, evaluates the direct character sum as an integer, compares with the closed formula, and independently counts the exact zero frequencies. It checks all \(29{,}520\) Fourier frequencies in these eight lengths, yielding `VERIFY_OK direct_character_frequencies=29520 lengths=2..9`. The analytic proof, not these finite tests, proves the unrestricted statement.

## Relationship to prior work
The classical theory of nowhere-zero modular flows, including dipoles with parallel edges, is developed by Beck and Zaslavsky (2003, Sections 1, 3 and 4.1; their Example 3.4 explicitly gives the ordinary modular flow polynomials for several parallel-edge dipoles). Its unweighted count addresses only the trivial Fourier frequency; it does not provide an all-frequency signed spectrum, zero set or convolution nullity. Classical finite-field character orthogonality and complete-weight-enumerator/MacWilliams transforms imply the basic character-reduction identity above and are not claimed as discoveries. The specific all-length cancellation criterion \((m,m,m+1)\), exact ambient-convolution rank and asymptotic singular density are the assertions distinguished here.

A separately available result on parity-check hyperplane Fourier sampling studies restriction of low-weight characters to **all** checksum-zero words; it is not convolution by the indicator of the nowhere-zero subset in the full ambient group. A result about Fourier principal minors of fixed-weight slices likewise has different sampling objects and does not imply the present exact zero structure. These comparisons do not preclude an unindexed equivalent specialization of classical complete-weight-enumerator theory.

## Limitations
The theorem is specific to the ternary one-checksum system and to exact, noiseless full-group convolution. It gives all eigenvalues and exact zero multiplicities but does not optimize stable inversion constants at nonzero singular values. The unsigned flow count and the character filter are elementary and established. General MacWilliams-transform literature could conceal an equivalent zero classification, so historical priority remains bounded rather than exhaustive. Computational checks through length nine do not certify larger dimensions; the displayed algebraic proof does. No independent external validation has been performed.

## References
1. Matthias Beck and Thomas Zaslavsky, *The Number of Nowhere-Zero Flows on Graphs and Signed Graphs*, arXiv:math/0309331, first publicly posted 2003-09-19, https://arxiv.org/abs/math/0309331 ; especially Sections 1, 3 (Example 3.4), and 4.1.
2. *Exact alias spectra and the binary Nyquist boundary for parity-check Fourier sampling*, published research record, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-alias-spectra-and-the-binary-nyquist-boundary-for-parity-c--75b261de521c/RESULT.md .
3. *Sharp conditioning and the ternary threshold for balanced finite Fourier slices*, published research record, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-conditioning-and-the-ternary-threshold-for-balanced-finite--efbde5ac5a6a/RESULT.md .
4. *MacWilliams identities*, Encyclopedia of Mathematics, https://encyclopediaofmath.org/wiki/MacWilliams_identities .
