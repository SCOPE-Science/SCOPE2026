# Binomial multiplier anisotropy and folded-normal fluctuations in the planar twisted baker map

## Finding
For the two-dimensional twisted baker map defined below, let \(\operatorname{Fix}^*(F^n)\) denote its \(2^n-1\) nontrivial fixed points of the \(n\)-th iterate (points of smaller least period are included). For \(n\ge2\), exactly \(2^{n-1}-1\) such points have two real multipliers. Define \(S_n(x)\) on those points by the signed powers
\[
\operatorname{spec}(DF^n(x))=\left\{(-1)^{t/2}2^{(n+S_n(x))/2},\;(-1)^{t/2}2^{(n-S_n(x))/2}\right\},
\]
where \(t\) is the even number of right-branch visits in the length-\(n\) itinerary. For each integer \(0\le k\le n-1\), the **exact number** of these real-spectrum points with \(S_n=n-2k\) is
\[
\boxed{\binom{n-1}{k}-\mathbf 1_{\{k=0\}}.}
\]
This counts the *signed*, coordinate-ordered exponent difference, not only its absolute value. Every other nontrivial fixed point has the conjugate-pair spectrum \(\{+i2^{n/2},-i2^{n/2}\}\).

Write \(\chi_n(x)=\min\{\lvert\lambda\rvert^{1/n}:\lambda\in\operatorname{spec}(DF^n(x))\}\). Then the sharp minimum among all nontrivial fixed points is
\[
\boxed{\min_{x\in\operatorname{Fix}^*(F^n)}\chi_n(x)=2^{1/n}\qquad(n\ge2).}
\]
The minimum is achieved by the itinerary consisting of a right visit, \(n-2\) left visits, then a right visit.

If \(X_n\) is chosen uniformly from the \(2^{n-1}-1\) real-spectrum points, then, for a standard normal random variable \(Z\),
\[
\boxed{\sqrt n\left(\frac12-\log_2\chi_n(X_n)\right)\ \xrightarrow{\ d\ }\ \frac{|Z|}{2}.}
\]
If the uniform choice is instead among all \(2^n-1\) nontrivial fixed points, the limiting law is the mixture \(\tfrac12\delta_0+\tfrac12\mathcal L(|Z|/2)\). Thus worst-case expansion becomes arbitrarily weak, but the typical logarithmic expansion is \(\tfrac12\log2\), with an explicitly scaled folded-normal deficit.

## Assumptions and scope
Set \(X=[-1,1]\times[0,1]\) and let
\[
F(x,y)=\begin{cases}(1+2x,y),&x<0,\\(1-2y,x),&x\ge0.\end{cases}
\]
The face \(N=\{(-1,y):0\le y\le1\}\) is a continuum of trivial fixed points and is omitted from \(\operatorname{Fix}^*(F^n)=\{z\in X\setminus N:F^n(z)=z\}\). The right branch includes the switching line. All multipliers are computed from the Jacobian of the branch actually selected by the orbit, and boundary points use that one-sided convention. Counting \(\operatorname{Fix}^*(F^n)\) rather than least-period-\(n\) points is essential to the stated binomial distribution.

## Proof
**1. Symbolic points and branch derivatives.** Put \(D=\operatorname{diag}(2,1)\) and \(P=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\), so that the left and right branch Jacobians are respectively \(D\) and \(DP\). The coding result for this exact map (Saiki–Takahasi–Yorke, Lemmas 2.4–2.6) gives a bijection between non-all-left words \(w=(b_1,\ldots,b_n)\in\{0,1\}^n\) and nontrivial fixed points of \(F^n\), with \(b_j=1\) denoting the right branch. Thus there are \(2^n-1\) points. The excluded all-left periodic itinerary corresponds to the fixed face \(N\).

**2. Exact signed product.** Write \(t=\sum_{j=1}^n b_j\). The product in chronological order is
\[
A_w=DP^{b_n}DP^{b_{n-1}}\cdots DP^{b_1}.
\]
For \(1\le j\le n\), set \(\zeta_j=(-1)^{\sum_{i=j+1}^n b_i}\), and put \(S=\sum_{j=1}^n\zeta_j\). Since conjugation of \(D\) by \(P\) interchanges its two diagonal entries, moving the factors \(P\) to the right yields
\[
A_w=\operatorname{diag}\left(2^{(n+S)/2},2^{(n-S)/2}\right)P^t.
\]
In particular \(S\equiv n\pmod2\). If \(t\) is even, then \(P^t=(-1)^{t/2}I\), giving the two real multipliers stated in the finding. If \(t\) is odd, \(P^t\) is, up to sign, a quarter-turn, so \(\det(\lambda I-A_w)=\lambda^2+2^n\), proving the exact conjugate-pair assertion.

**3. A bijection to independent signs.** For every word with even \(t\), define \(u_j=(-1)^{b_j}\), so that \(\prod_{j=1}^n u_j=1\), and \(\zeta_j=u_{j+1}\cdots u_n\), with \(\zeta_n=1\). Conversely, every arbitrary choice of \((\zeta_1,\ldots,\zeta_{n-1})\in\{-1,1\}^{n-1}\) uniquely determines one even-parity word: \(u_1=\zeta_1\) and \(u_j=\zeta_{j-1}\zeta_j\) for \(2\le j\le n\). Hence the signs \(\zeta_1,\ldots,\zeta_{n-1}\) are independent fair signs under uniform selection of all even-parity words, and
\[
S=1+\sum_{j=1}^{n-1}\zeta_j.
\]
Exactly \(\binom{n-1}{k}\) such words have \(S=n-2k\). The all-left word is precisely the all-positive sign configuration, occurring only at \(k=0\); removing it proves the stated exact count. The remaining odd-parity words number \(2^{n-1}\).

**4. Extremal and typical expansion.** If \(t\) is even, \(\log_2\chi_n=(n-|S|)/(2n)\). The admissible values \(S=n-2k\), \(1\le k\le n-1\), satisfy \(\lvert S\rvert\le n-2\); both extreme magnitudes occur. If \(t\) is odd, \(\log_2\chi_n=1/2\). Thus the exact minimum is \(2^{1/n}\), and \(w=R L^{n-2}R\) realizes it. Conditioned on the real-spectrum set, the finite sign law differs from \(1+\sum_{j=1}^{n-1}\varepsilon_j\), for independent fair signs \(\varepsilon_j\), only by excluding one configuration of probability \(2^{-(n-1)}\). The classical central limit theorem and continuous mapping theorem imply \(\lvert S\rvert/\sqrt n\Rightarrow\lvert Z\rvert\), proving the folded-normal limit. Finally, the relative frequencies of even- and odd-parity nontrivial words approach \(1/2\) each, yielding the stated mixture law over all nontrivial points.

## Verification
Run `python check_2d_twisted.py` with Python 3 and no nonstandard dependencies. The supplied exact-rational program explicitly solves the affine fixed-point equations for every non-all-left word of length \(1\le n\le11\), verifies the itinerary and return, calculates the exact Jacobian, checks the signed multiplier powers and compares the complete histogram against \(\binom{n-1}{k}-\mathbf1_{\{k=0\}}\). Its expected terminal line is `TWISTED_BAKER_BINOMIAL_ANISOTROPY_CHECK_OK`. This finite exhaustive consistency check is supplementary: the proof for all \(n\) is the symbolic bijection and factorization above, not an extrapolation from the test.

## Relationship to prior work
Saiki, Takahasi and Yorke (2022/2023) define this map and establish the \(2^n-1\) symbolic fixed-point count, existence of both real and nonreal spectra, simultaneous spatial equidistribution, and nonuniform periodic expansion. They do not give the exact distribution of the two real multiplier magnitudes or a central limit theorem for their weakest expansion rate. A later published exact residue classification (see References) proves that the spectrum is entirely real exactly when the number of right visits is divisible by the dimension, and supplies a general weighted-cycle characteristic polynomial. In dimension two, this identifies the even-right-visit subset but **does not determine the distribution of how the \(n\) factors of two split between the two eigendirections**. Indeed \(LLRR\) and \(LRLR\) have the same right-visit count of two, yet their multiplier moduli are respectively \((8,2)\) and \((4,4)\). The present independent-sign bijection is the additional ingredient yielding the sharp binomial law, typical fluctuation scale, and exact finite-period extremum. Takahasi's 2024 periodic-point distribution theorem concerns the Dyck shift and a different, heterochaos baker-map family.

## Limitations
The exact distribution is for dimension two and fixed points of the \(n\)-th iterate, not a classification conditioned on *least period* \(n\); the latter requires additional divisibility corrections. Neither the folded-normal limit nor the finite checker describes an arbitrary measure of random initial points. The Gaussian statement is weak convergence of scaled expansion deficits; it is not total-variation convergence to a continuous law. Originality comparisons rely on the accessible primary preprint, inspected related literature, and published mathematical-record searches and cannot rule out unindexed equivalent results. Independent validation has not been performed.

## References
1. Y. Saiki, H. Takahasi, J. A. Yorke, *The twisted baker map*, arXiv:2202.04304, first publicly posted 2022-02-09, version 3 2023-01-13; *Nonlinearity* 36 (2023), 1776–1788, DOI: 10.1088/1361-6544/acb4d3. In particular Sections 1–3, Lemmas 2.1–2.6, Theorems B and C.
2. *Exact real-spectrum residue law for the twisted baker map*, public mathematical record 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-real-spectrum-residue-law-for-the-twisted-baker-map--f1bd1c74fb3b, especially the exact real/nonreal criterion and the general characteristic polynomial.
3. H. Takahasi, *Distributions of periodic points for the Dyck shift and the heterochaos baker maps*, arXiv:2409.01261, first posted 2024-09-02; different dynamical family.
