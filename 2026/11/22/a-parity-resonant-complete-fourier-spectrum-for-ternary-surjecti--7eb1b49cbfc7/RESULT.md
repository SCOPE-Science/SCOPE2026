# A parity-resonant complete Fourier spectrum for ternary surjections

## Finding
Let \(n\ge3\), let \(G=(\mathbb Z/3\mathbb Z)^n\), and let \(f_n:G\to\{0,1\}\) indicate the words in which each of the three alphabet symbols occurs at least once. Let \(T_nu=f_n*u\) be **unnormalized** counting convolution on complex functions on \(G\). With \(\omega=e^{2\pi i/3}\), define \(\widehat f_n(\xi)=\sum_{x\in G}f_n(x)\omega^{\langle\xi,x\rangle}\). For a nonzero frequency \(\xi\), write \(z=|\{j:\xi_j=0\}|\), \(r=n-z\), and \(s=\sum_j\xi_j\pmod3\). Then the **complete signed Fourier spectrum** is
\[
\widehat f_n(\xi)=
\begin{cases}
3^n-3\cdot2^n+3,&\xi=0,\\
0,&\xi\ne0,\ s\ne0,\\
3\bigl(1-(-1)^r2^z\bigr),&\xi\ne0,\ s=0.
\end{cases}
\]
Each nonzero frequency having \(z\) zero coordinates and \(s=0\) occurs with exact multiplicity
\[
M_{n,z}=\binom nz\frac{2^{n-z}+2(-1)^{n-z}}3\qquad(0\le z<n).
\]
The trivial frequency occurs once. Frequencies with \(s\ne0\) have multiplier zero. Consequently, the only zeros **beyond** those forced by diagonal colour translation occur when \(n\) is even and \(\xi\) has no zero coordinates. Their exact number is \((2^n+2)/3\). Thus
\[
\operatorname{rank}(T_n)=
\begin{cases}
3^{n-1},&n\text{ odd},\\
3^{n-1}-(2^n+2)/3,&n\text{ even},
\end{cases}
\qquad
\operatorname{nullity}(T_n)=3^n-\operatorname{rank}(T_n).
\]
The largest singular value is \(3^n-3\cdot2^n+3\) and the least strictly positive singular value is exactly \(3\) for odd \(n\), or \(9\) for even \(n\). In particular the sharp condition number on the recoverable Fourier range is \((3^n-3\cdot2^n+3)/3\) for odd \(n\), and \((3^n-3\cdot2^n+3)/9\) for even \(n\).

There is also an exact **projection dichotomy**. At odd lengths, the orthogonal projection onto the range of \(T_n\) is averaging over the three simultaneous colour translations and is positive and contractive in every \(\ell^p(G)\). At even lengths, the analogous Fourier-range projection has negative convolution-kernel values; hence it is not positivity-preserving, and its \(\ell^1\)- and \(\ell^\infty\)-operator norms are strictly greater than one.

## Assumptions and scope
The alphabet is the additive group \(\mathbb Z/3\mathbb Z\), positions are labelled, and the underlying domain is the full group \(G\), not the set of surjections alone. The transform and convolution are unnormalized, so the multiplier of the trivial character is the number of surjections. Convolution rank and nullity refer to the complex-linear operator on all \(3^n\) functions on \(G\). Singular values are absolute Fourier multipliers; the projection statement uses normalized inverse Fourier transformation. All assertions hold for every integer \(n\ge3\), without a finite-size extrapolation.

## Proof
**1. Inclusion–exclusion and characters.** The indicator of a word using all three symbols equals the indicator of all words minus the sum of the indicators of words using each particular pair of symbols, plus the sum of three constant-word indicators. For \(\xi\ne0\), full-word character orthogonality gives zero. Index a two-symbol alphabet by its missing colour \(c\). At a coordinate where \(\xi_j=0\), its character sum is \(2\). At a nonzero coordinate, the sum over the two allowed colours is \(-\omega^{c\xi_j}\), because the sum over all three colours is zero. Hence the two-symbol contribution is \(2^z(-1)^r\omega^{cs}\), while the singleton contribution is \(\omega^{cs}\). Therefore
\[
\widehat f_n(\xi)=\bigl(1-(-1)^r2^z\bigr)\sum_{c=0}^{2}\omega^{cs}.
\]
The last sum equals \(3\) exactly when \(s=0\) and zero otherwise. At \(\xi=0\), ordinary inclusion–exclusion gives \(3^n-3\cdot 2^n+3\). This proves the displayed spectrum, including the sign.

**2. All zero conditions and multiplicities.** If \(z\ge1\), \(2^z\ne1\), so the balanced-frequency factor cannot vanish. If \(z=0\), the factor is \(1-(-1)^n\), vanishing precisely for even \(n\). For \(r\ge1\), the number of ordered \(r\)-tuples of nonzero ternary frequency digits with sum zero is
\[
B_r=\frac13\sum_{t=0}^2(\omega^t+\omega^{-t})^r
=\frac{2^r+2(-1)^r}{3}.
\]
Choosing the \(z\) zero locations then gives \(M_{n,z}=\binom nz B_{n-z}\). There are exactly \(3^{n-1}\) balanced frequencies, because the last coordinate is uniquely determined by the preceding ones. For even \(n\), the additional vanished balanced frequencies number \(B_n=(2^n+2)/3\); for odd \(n\) there are none. Since the Fourier characters diagonalize convolution, the claimed rank and nullity follow.

**3. Sharp singular bounds.** The trivial coefficient is the cardinality of the support, so the triangle inequality bounds every multiplier's magnitude by \(3^n-3\cdot2^n+3\), with equality at the trivial frequency. For odd \(n\), the value at balanced frequencies with \(z=1\) is \(-3\), and such frequencies exist: the remaining even number of nonzero digits can be split equally between \(1\) and \(2\). All other nonzero multiplier magnitudes are at least \(3\). For even \(n\), the value at balanced frequencies with \(z=1\) is \(9\); these exist for all even \(n\ge4\), since the remaining odd number at least three can have sum zero. Frequencies with \(z=2\) have value \(-9\); those with \(z\ge3\) have magnitude at least \(21\), and \(z=0\) gives zero. Thus the least positive magnitude is \(9\). Ratios give the condition numbers.

**4. Positivity transition of recovery.** Let \(D=\{(t,\ldots,t):t\in\mathbb Z/3\mathbb Z\}\). Its annihilator is the balanced-frequency set. For odd \(n\), the range multiplier equals the indicator of \(D^\perp\), and the orthogonal projection is convolution with the positive probability measure uniformly supported on \(D\). For even \(n\), subtract from that projector the Fourier projection onto \(B=\{\xi\in D^\perp:\xi_j\ne0\ \forall j\}\). If \(K_B\) denotes the latter's convolution kernel and \(c_0,c_1,c_2\) are the counts of each symbol in \(x\), character orthogonality gives
\[
K_B(x)=3^{-(n+1)}\sum_{j=0}^2(-2)^{c_j},\quad n\text{ even}.
\]
Choose \(x\) with \(n-2\) zeros and two ones. This \(x\) is not in \(D\), and \(K_B(x)=3^{-(n+1)}(2^{n-2}+5)>0\). The range projection kernel at \(x\) is therefore negative. Its kernel sums to one because the trivial frequency survives; a real kernel with negative values and total mass one has total variation greater than one, giving both asserted endpoint operator norms greater than one. This completes the proof.

## Verification
The standalone standard-library program `verify_ternary_surjections.py` independently enumerates every surjective ternary word and all \(3^n\) characters for \(3\le n\le7\). It computes each coefficient exactly as a pair of Eisenstein-integer coordinates, not with floating-point root-of-unity tolerances, and compares with the theorem. It also checks rank, least nonzero magnitude and full balanced-frequency multiplicities at those sizes, then checks the derived binomial identities through \(n=49\). A fresh extraction ran successfully and checked 3,267 character coefficients. The infinite family follows from the algebraic argument above, not from these tests.

Examples: at lengths \(n=3,4,5,6,7,8\), the ranks are respectively \(9,21,81,221,729,2101\); at even lengths the extra balanced-frequency nullities are respectively \(6,22,86\) for \(n=4,6,8\).

## Relationship to prior work
Surjection counts and the classical coupon-collector model are longstanding. Myers and Wilf (2003), *Some New Aspects of the Coupon-Collector's Problem*, use Stirling numbers for complete coupon collections, but their explicit enumeration and related generating functions do not yield the Fourier coefficient classification or projection dichotomy here. The published *Exact first-band Fourier sampling spectra on surjective words* treats the Gram matrix obtained by restricting the constant character and single-coordinate characters to the surjection set. Its exact degree-one sampling eigenvalues do not imply the all-frequency counting-convolution eigenvalues: the former determine low-order correlations rather than arbitrary-coordinate Fourier coefficients. The present classification addresses a different, full-frequency operator and exposes even-length losses beyond translation invariance. The formulas are not claimed to be historically unique; unidentified equivalent Fourier or occupancy calculations may exist.

## Limitations
The result is for exactly three additive symbols, not arbitrary alphabet sizes, arbitrary surjection domains, or nonabelian colour groups. Its positive projection conclusion is specific to odd lengths, and no sharp numerical formula for the even-length projection endpoint norms is asserted. The originality comparison is bounded and independent external validation has not been performed.

## References
- A. N. Myers and H. S. Wilf, *Some New Aspects of the Coupon-Collector's Problem*, arXiv:math/0304229, first publicly submitted 2003-04-16, https://arxiv.org/abs/math/0304229 ; full HTML https://arxiv.org/html/math/0304229v1 .
- *Exact first-band Fourier sampling spectra on surjective words*, published 2026-11-01, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-exact-first-band-fourier-sampling-spectra-on-surjective-words--38dfe55b7163/RESULT.md .
