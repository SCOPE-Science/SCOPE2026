# Exact seven-node positive Fourier designs on four consecutive sites of the eleven-cycle

## Finding
Let \(A=\{0,1,2,3\}\subset\mathbb Z_{11}\), \(\omega=e^{2\pi i/11}\), and \(v_t=(1,\omega^t,\omega^{2t},\omega^{3t})\in\mathbb C^4\) for \(t\in\mathbb Z_{11}\). A positive Parseval Fourier design is a set of distinct frequencies \(S\subset\mathbb Z_{11}\), together with strictly positive real weights \(w_t\) for \(t\in S\), satisfying
\[
\sum_{t\in S}w_t v_tv_t^*=I_4.
\]
The minimum number of frequencies is **seven**. Exactly **33** seven-frequency sets admit strictly positive normalized weights, forming precisely three translation orbits, with representatives
\[
\begin{aligned}
S_1&=\{0,1,2,3,5,7,9\},\\
S_2&=\{0,1,2,4,6,7,9\},\\
S_3&=\{0,1,3,4,6,7,9\}.
\end{aligned}
\]
Every translation orbit has size eleven. For each of the 33 sets, the positive weights are **unique** after the Parseval normalization and admit an exact formula in the seven-node Lagrange interpolation basis, given below. No proper frequency set admits an equal-positive-weight Parseval design; without adjustable weights all eleven frequencies are necessary.

## Assumptions and scope
The ambient cyclic group is exactly \(\mathbb Z_{11}\), the observed sites are exactly \(A=\{0,1,2,3\}\), the Fourier coefficients are unnormalized complex characters, and frequencies are **distinct**. All weights must be strictly positive, not merely nonnegative. Equality \(I_4\) fixes the common frame bound; arbitrary positive common scaling yields the corresponding tight frames. Translation equivalence means \(S\mapsto S+a\) for \(a\in\mathbb Z_{11}\); no reflection/dilation quotient is imposed on the 33-set count.

## Proof
**Moment characterization.** Writing \(z_t=\omega^t\), the Gram identity is equivalent to seven real equations:
\[
\sum_{t\in S}w_t=1,\qquad \sum_{t\in S}w_t z_t^k=0\quad(k=1,2,3).
\tag{1}
\]
The negative Fourier moments follow by complex conjugation since weights are real. Introduce the real six-by-\(|S|\) matrix \(B(S)\) whose successive row pairs are \((\operatorname{Re}z_t^k)_{t\in S}\), \((\operatorname{Im}z_t^k)_{t\in S}\) for \(k=1,2,3\). Any solution to (1) lies in \(\ker B(S)\).

**Seven-frequency lower bound.** For every six-element \(T\subset\mathbb Z_{11}\), the actual finite certificate proves \(\det B(T)\ne0\) by rational outward-rounded interval arithmetic; there are exactly \(\binom{11}{6}=462\) such subsets. The smallest certified absolute-determinant lower bound over these is greater than \(0.4020\). Thus no nonzero homogeneous moment solution exists on six frequencies. A set of at most five frequencies could be extended to six by appending zero-weight columns, contradicting six-column nonsingularity. Hence \(|S|\ge7\) for any positive design. The certificate is a finite exhaustive mathematical proof for the **fixed eleven-cycle**, not an extrapolation to all primes.

**Unique seven-node weights.** For a seven-element set \(S\), the real seven-by-seven matrix \(C(S)\), formed by adjoining a constant row to \(B(S)\), is nonsingular for every one of the \(\binom{11}{7}=330\) choices, again as certified by the supplied rational interval eliminator. Thus (1) has a unique real solution, not necessarily positive. It can also be written explicitly. Let
\[
L_t(X)=\prod_{\substack{u\in S\\u\ne t}}\frac{X-z_u}{z_t-z_u}.
\]
Then the unique normalized weights are
\[
\boxed{\displaystyle w_t=z_t^3[X^3]L_t(X)
=-\frac{z_t^3 e_3(\{z_u:u\in S\setminus\{t\}\})}{\prod_{u\in S\setminus\{t\}}(z_t-z_u)}.}
\tag{2}
\]
Indeed Lagrange interpolation of \(X^r\), for every integer \(0\le r\le6\), followed by coefficient extraction at \(X^3\), yields \(\sum_{t\in S}w_tz_t^{r-3}=\mathbf1_{r=3}\). This is (1) and its conjugates. Uniqueness and invariance under complex conjugation of the real moment equations ensure the numbers in (2) are real.

**Exhaustive positivity and orbit certificate.** The accompanying `verify.py` constructs rigorous rational intervals for \(\pi\) via Machin's identity and alternating arctangent series, then for every \(\cos(2\pi j/11)\) and \(\sin(2\pi j/11)\) using Taylor expansions with rigorous remainders and outward-rounded fixed-point interval operations. For every one of the 330 seven-element sets it performs an interval Gaussian elimination of the seven-by-seven real moment system with certified nonzero pivots and encloses **all seven exact weights**. Exactly 33 sets have all weight lower endpoints positive (uniformly at least \(0.04335\)); each of the other 297 sets has a weight with rigorously negative upper endpoint. The 33 sets have precisely the three asserted translation representatives, each occurring eleven times. These facts establish the full exact count and classification, rather than merely providing candidate examples. The source file contains all constants, finite ranges, interval algorithms, and assertions needed to replay the certificate.

**Equal-weight obstruction.** If a proper nonempty \(S\) admitted equal weights, the first moment would give \(\sum_{t\in S}\omega^t=0\). The minimal polynomial \(1+X+\cdots+X^{10}\) of \(\omega\) over \(\mathbb Q\) forces the eleven rational indicator coefficients to be equal; they cannot be equal for a proper nonempty subset. All eleven frequencies with weights \(1/11\) do form a Parseval design. This proves the stated weighted/unweighted gap.

## Verification
Run `python3 verify.py` from the directory containing the embedded source. The verifier prints `CERTIFICATE_PASS` after 462 certified nonsingular six-node matrices, 330 uniquely solved seven-node systems, 33 strict-positive solutions, the three translation orbits, and explicit rigorous sign margins. The verifier uses the Python standard library and does **not** use floating-point arithmetic to decide any sign; floating-point conversion is only used to format already-certified positive or negative bounds for display. Its mathematical premise is exact rational interval inclusion. The finite exhaustive certificate covers only modulus eleven, and the proof explicitly depends on rerunning or independently inspecting this standalone artifact; the printed log alone is not an independent certificate.

## Relationship to prior work
Weighted Parseval exponential frames in the self-affine-measure setting are developed by Dutkay and Ranasinghe [1]. Frederick and Mayeli [2] study finite frame spectral pairs and their constructions. Bultheel, Cruz-Barroso, and Díaz Mendoza [3] give general positive Szegő-type quadrature with prescribed points on the unit circle. The published classification of positive Fourier sampling on **three** consecutive cyclic sites [4] finds a five-node minimum for many prime cycles, but concerns three spatial sites rather than the four-site eleven-cycle and does not imply the stated 33 seven-node classification. None of these inspected sources provides the exact 11th-root restricted four-site positivity census. Standard Fourier orthogonality, Lagrange interpolation, and finite interval certificates are acknowledged methods, not new general principles.

## Limitations
This is an exact, natural **finite-modulus** classification, not an infinite-family theorem, not a classification at other primes or other spatial supports, and not an optimal stability result. Its originality assessment is best knowledge: an older or unindexed equivalent seven-node cyclotomic cubature table cannot be categorically excluded. Independent scientific audit remains unperformed.

## References
1. D. E. Dutkay and R. Ranasinghe, *Weighted Fourier Frames on Self-Affine Measures*, arXiv:1710.01224v1, first publicly posted 2017-10-03, https://arxiv.org/abs/1710.01224.
2. C. Frederick and A. Mayeli, *Frame spectral pairs and exponential bases*, arXiv:2010.05667v1, first publicly posted 2020-10-12, https://arxiv.org/abs/2010.05667.
3. A. Bultheel, R. Cruz-Barroso, and C. Díaz Mendoza, *Zeros of quasi-paraorthogonal polynomials and positive quadrature*, arXiv:2110.10460v1, first publicly posted 2021-10-20, https://arxiv.org/abs/2110.10460.
4. *Sharp positive Fourier sampling on three consecutive cyclic sites*, publicly available mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-positive-fourier-sampling-on-three-consecutive-cyclic-site--29fa16b8c55a.
