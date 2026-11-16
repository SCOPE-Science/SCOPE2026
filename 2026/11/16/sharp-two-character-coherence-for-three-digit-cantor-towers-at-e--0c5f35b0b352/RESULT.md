# Sharp two-character coherence for three-digit Cantor towers at every integer base

## Finding
For integers \(b\ge4\) and \(n\ge1\), let \(\nu_{b,n}\) be the equally weighted probability measure on the \(3^n\) points
\[
\Bigl\{\sum_{j=1}^n d_j b^{-j}: d_j\in\{0,1,2\}\Bigr\}.
\]
Its Fourier coefficients are \(\widehat\nu_{b,n}(k)=\int e^{-2\pi ikx}\,d\nu_{b,n}(x)\). For distinct integer characters on this measure, let
\[
M_{b,n}=\min_{k\in\{1,\ldots,b^n-1\}}|\widehat\nu_{b,n}(k)|.
\]
This is the smallest attainable absolute Gram correlation for two distinct integer-frequency characters, where frequencies are considered modulo \(b^n\).

**Exact dichotomy.** If \(3\mid b\), then \(M_{b,n}=0\). If \(3\nmid b\), set \(\epsilon_j=+1\) when \(b^j\equiv2\pmod3\) and \(\epsilon_j=-1\) when \(b^j\equiv1\pmod3\). Then
\[
\boxed{M_{b,n}=\prod_{j=1}^n\frac{\sin(\pi/b^j)}{3\sin(\pi/3+\epsilon_j\pi/(3b^j))}>0.}
\]
For \(n\ge2\), the minimizing gaps are exactly the two residue classes
\[
\boxed{3k\equiv\pm1\pmod{b^n}.}
\]
The same classification holds when \(n=1\), except that \((b,n)=(4,1)\) has an additional minimizing residue \(k\equiv2\pmod4\).

The sharp two-character Gram eigenvalues at the optimal gap are \(1\pm M_{b,n}\); hence their best possible ratio of upper to lower squared Riesz bounds is \((1+M_{b,n})/(1-M_{b,n})\). When \(3\mid b\), orthogonality is attainable at every finite level. When \(3\nmid b\), it is never attained by distinct integer characters, despite the rapid approach below.

**Sharp depth law.** For every fixed \(b\ge4\) with \(3\nmid b\), the positive, convergent product
\[
C_b=\prod_{j=1}^{\infty}
\left[\frac{\sin(\pi/b^j)}{\pi/b^j}\cdot
\frac{\sqrt3/2}{\sin(\pi/3+\epsilon_j\pi/(3b^j))}\right]
\]
satisfies \(0<C_b<\infty\), and
\[
\boxed{M_{b,n}=C_b\left(\frac{2\pi}{3\sqrt3}\right)^n
 b^{-n(n+1)/2}\left(1+O_b(b^{-n})\right).}
\]
Thus optimal pairwise correlation decays superexponentially in depth whenever the digit count and base are coprime.

## Assumptions and scope
The digit set is precisely \(\{0,1,2\}\), each digit has weight \(1/3\), the level is finite, and \(b\ge4\) is an integer. Frequencies are integers. Distinct characters means their frequency gap is not divisible by \(b^n\); no conclusion is made about arbitrary real frequency sets, infinite-dimensional Fourier frames, or full multi-character Gram matrices. The algebraic congruences and products hold for all indicated \(b,n\), not only tested instances.

## Proof
**1. Fourier product and Gram normalization.** Independent uniform digits give
\[
\widehat\nu_{b,n}(k)=\prod_{j=1}^n \frac{1+e^{-2\pi ik/b^j}+e^{-4\pi ik/b^j}}3,
\quad
|\widehat\nu_{b,n}(k)|=\prod_{j=1}^n h_{b^j}(k),
\]
where \(h_N(k)=|1+2\cos(2\pi k/N)|/3\). The absolute value is periodic in \(k\) modulo \(N\). Every point of the measure is a multiple of \(b^{-n}\), so the integer characters have period \(b^n\) on its support. For two such unit vectors their Hermitian Gram matrix has off-diagonal magnitude \(|\widehat\nu_{b,n}(k)|\) and eigenvalues \(1\pm|\widehat\nu_{b,n}(k)|\).

**2. A sharp one-level three-tap mask lemma.** Let \(N\ge4\) and \(3\nmid N\). The smallest value of \(h_N(k)\) over integer residues is
\[
\frac{\sin(\pi/N)}{3\sin(\pi/3+\epsilon\pi/(3N))},
\quad
\epsilon=\begin{cases}-1&N\equiv1\pmod3,\\+1&N\equiv2\pmod3.\end{cases}
\]
When \(N\ge5\), equality holds exactly when \(3k\equiv\pm1\pmod N\). When \(N=4\), the equality residues are \(1,2,3\pmod4\).

To prove this, use the symmetry \(k\mapsto N-k\) and \(h_N(k)=|1+2\cos\theta|/3\) for \(\theta=2\pi k/N\in[0,\pi]\). The underlying signed expression strictly decreases and has its only zero at \(\theta=2\pi/3\), so it suffices to compare the two grid points on either side of that zero. If \(N=3q+1\), they are \(q,q+1\). Put \(\delta=2\pi/(3N)\in(0,\pi/6]\). The inequality \(h_N(q)\le h_N(q+1)\) is equivalent to
\[
G(\delta)=\cos(\pi/3+\delta)+\cos(\pi/3-2\delta)\ge1.
\]
Indeed \(G(0)=G(\pi/6)=1\), while \(G''(\delta)=-\cos(\pi/3+\delta)-4\cos(\pi/3-2\delta)<0\) on this interval. Strict concavity gives the desired comparison, with equality only at \(N=4\).

If \(N=3q+2\), the neighbors are \(q,q+1\). With the same \(\delta\) (now \(0<\delta\le2\pi/15\)), the inequality \(h_N(q+1)<h_N(q)\) is equivalent to
\[
H(\delta)=\cos(\pi/3+2\delta)+\cos(\pi/3-\delta)<1.
\]
Here \(H(0)=1\) and
\[
H'(\delta)=-2\sin(\pi/3+2\delta)+\sin(\pi/3-\delta)<0,
\]
since the first sine exceeds the second: their difference equals \(2\cos(\pi/3+\delta/2)\sin(3\delta/2)>0\). The exact value at the winner follows from
\[
|1+2\cos(2\pi k/N)|=\left|\frac{\sin(3\pi k/N)}{\sin(\pi k/N)}\right|,
\]
where the winner obeys \(3k\equiv\pm1\pmod N\). This completes the lemma.

**3. Simultaneous sharpness at every scale.** When \(3\nmid b\), apply the lemma with \(N=b^j\), obtaining the product lower bound in the statement. Because \(3\) is invertible modulo \(b^n\), there exist exactly two residues satisfying \(3k\equiv\pm1\pmod{b^n}\). Their reductions modulo every \(b^j\) satisfy the same signed congruence, so both attain every one-level minimum simultaneously. Conversely, any minimizer of the product must minimize its final factor \(h_{b^n}\); for \(n\ge2\), \(b^n\ge16\), and the lemma forces exactly those two gaps. At \((4,1)\), the lemma gives the extra residue. If \(3\mid b\), choose \(k=b/3\); the first factor is zero, proving \(M_{b,n}=0\).

**4. Depth asymptotics.** Divide each nonzero factor by \((2\pi/(3\sqrt3))b^{-j}\). The quotient equals the \(j\)-th bracket in the product defining \(C_b\), and is \(1+O_b(b^{-j})\). The sum of the absolute deviations is finite, and each bracket is strictly positive, so \(C_b\) exists and lies in \((0,\infty)\). The omitted tail product is \(1+O_b(b^{-n})\); multiplying the leading factors yields the displayed asymptotic. All limits are taken with \(b\) fixed.

## Verification
The independent-of-depth proof consists of the explicit factorization, the two elementary one-level comparisons, and the reduction of a single modular inverse through all powers of \(b\). The accompanying standalone script recomputes the exact formula numerically at high precision for multiple coprime bases and levels, checks the complete minimizing residue sets, and checks the divisibility case. These finite computations are consistency checks, not substitutes for the foregoing all-base proof.

## Relationship to prior work
Fu and Wang (2026) study the **same three-consecutive-digit Bernoulli family** within a general consecutive-digit frame-obstruction theorem: their Theorem 1.1 rules out infinite frame measures when the digit count does not divide the base. Their Section 3.2 (Lemmas 3.3–3.4) gives the mask-product identity and its cyclotomic zeros but no finite-level minimum of its modulus, arithmetic minimizing gaps, or rate. Dai, He, and Lai earlier classified orthogonality and spectrality for self-similar measures with consecutive digits. De Dios Pont, Liehr, and Taylor proved a 2026 absence-of-Fourier-frames theorem for the **different** family of two-digit odd-base Cantor measures. Related finite two-digit Cantor coherence results concern a two-tap cosine mask, whereas the present three-digit family has the three-tap Dirichlet mask. Neither qualitative spectral classification nor the two-digit coherence statements determine the sharp finite-level product, its complete minimizing residues, or the depth constant here.

## Limitations
The optimal Gram problem is for **two integer-frequency characters** only. It gives no uniform multi-character frame bounds and does not assert existence or nonexistence of infinite Fourier frames for the three-digit measure. Older literature may contain the identical finite-level mask minimization under a different terminology; this has not been independently audited. The cited 2012/2013 consecutive-digit primary paper's abstract and bibliographic material were available, but its full original text was not available for direct comparison here.

## References
1. X.-Y. Fu, W.-J. Wang, *Nonexistence of Frame Measures for Separated Uniform Consecutive-Digit Bernoulli Convolutions*, arXiv:2608.19676, first submitted 2026-08-20; full text: https://arxiv.org/html/2608.19676v1 .
2. J. de Dios Pont, L. Liehr, M. A. Taylor, *Cantor measures with odd base do not admit Fourier frames*, arXiv:2607.08656, first submitted 2026-07-09. Full accessible preprint text: https://www.researchgate.net/publication/408699358_Cantor_measures_with_odd_base_do_not_admit_Fourier_frames .
3. X.-R. Dai, X.-G. He, C.-K. Lai, *Spectral property of Cantor measures with consecutive digits*, arXiv:1209.4386 (first submitted 2012-09-19); *Advances in Mathematics* 242 (2013), 187–208, DOI:10.1016/j.aim.2013.04.016.
