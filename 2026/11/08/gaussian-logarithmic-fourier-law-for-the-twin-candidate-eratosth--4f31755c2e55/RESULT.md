# Gaussian logarithmic Fourier law for the twin-candidate Eratosthenes wheel

## Finding

Let \(P\geq5\) range through primes, \(N=P^{\#}=\prod_{p\le P}p\), and on the finite cyclic group \(\mathbb Z/N\mathbb Z\) put
\[
f_P(x)={\mathbf{1}}_{\gcd(x(x+2),N)=1},\qquad
F_P(a)=\sum_{x\bmod N}f_P(x)e^{-2\pi iax/N}.
\]
These are the candidate starting positions for a pair with difference two after sieving all primes through \(P\), *not* necessarily genuine twin primes. Let \(A_P\) be uniform on \(\mathbb Z/N\mathbb Z\), and put \(X_P=\log|F_P(A_P)|\). Define
\[
m_p=\frac{\log(p-2)}p,\quad
v_p=\frac{\log^2(p-2)+\sum_{j=1}^{p-1}\log^2(2|\cos(\pi j/p)|)}p-m_p^2
\]
for odd primes \(p\), and \(M_P=\sum_{3\le p\le P}m_p\), \(V_P=\sum_{3\le p\le P}v_p\). Every Fourier coefficient is nonzero, \(\mathbb E X_P=M_P\), and \(\operatorname{Var}(X_P)=V_P>0\). As \(P\to\infty\) through primes,
\[
M_P=\log P+O(1),\qquad
V_P=\frac{\pi^2}{12}\pi(P)+O((\log P)^3),
\]
and the **uniform quantitative central limit theorem** holds:
\[
\sup_{t\in\mathbb R}\left|\frac1N\#\left\{a\bmod N:\frac{\log|F_P(a)|-M_P}{\sqrt{V_P}}\le t\right\}-\Phi(t)\right|\le\frac{C}{\sqrt{\pi(P)}}
\]
for an absolute constant \(C\), where \(\Phi\) is the standard normal distribution function. Moreover, for the integer circulant \(\mathcal C_P=(f_P(i-j))_{i,j\bmod N}\),
\[
\det\mathcal C_P=-\prod_{3\le p\le P}(p-2)^{N/p}.
\]
Thus the entire convolution operator is invertible and its signed determinant is explicitly known.

## Assumptions and scope

The integer \(P\) is prime and at least \(5\); all products and sums indexed by \(p\) are over primes. The discrete Fourier transform is unnormalized, with the negative exponential convention above. A Fourier frequency is **uniformly chosen over all** \(N\) frequencies, including the zero frequency. The central limit theorem describes coefficients of a periodic *finite-sieve indicator*, not Fourier coefficients of the infinite set of primes. The hidden constants are absolute. A finite test up to any fixed prime cannot replace the limit proof.

## Proof

**1. Fourier factorization.** By the Chinese remainder theorem, \(x\bmod N\) is identified with independent local coordinates \(x_p\bmod p\). If \(q_p=N/p\), a character of frequency \(a\) becomes the product of local characters of frequencies \(b_p\equiv aq_p^{-1}\pmod p\). Consequently \(F_P(a)=\prod_{p\le P}S_p(b_p)\), where \(S_2(b)=(-1)^b\), and for odd \(p\)
\[
S_p(0)=p-2,\qquad S_p(b)=-1-e^{4\pi ib/p}\quad(1\le b<p).
\]
For odd \(p\), the latter factor is nonzero (otherwise an odd-order root of unity would equal \(-1\)). Hence \(F_P(a)\ne0\) for every \(a\). As \(a\) ranges uniformly, the \(b_p\) are independent and uniform residues. Therefore \(X_P\) is a sum of independent local logarithmic variables, each taking the value \(\log(p-2)\) at zero and, at a nonzero residue, the value \(\log(2|\cos(2\pi b/p)|)\). Multiplication by two permutes nonzero residues, giving precisely the second-moment formula in the statement.

**2. Local mean and moments.** For every odd prime \(p\),
\[
\prod_{j=1}^{p-1}(1+e^{2\pi ij/p})=1,
\]
by evaluating \((z^p-1)/(z-1)\) at \(z=-1\). Taking absolute logarithms gives \(\sum_{j=1}^{p-1}\log(2|\cos(\pi j/p)|)=0\). Thus \(\mathbb EX_P=M_P\) exactly. Let \(g(t)=\log(2|\cos\pi t|)\), which has one logarithmic singularity at \(t=1/2\). Fourier Parseval applied to the classical series \(g(t)=\sum_{n\ge1}(-1)^{n-1}\cos(2\pi nt)/n\) in \(L^2[0,1]\) gives
\[
\int_0^1g(t)^2\,dt=\frac12\sum_{n\ge1}n^{-2}=\frac{\pi^2}{12}.
\]
For \(r=2,3\), remove the interval \(|t-1/2|\le1/p\). Its integral of \(|g|^r\) and the contribution of its at most two sampled points are \(O(\log^r p/p)\); on the complement \(|g|^r\) has total variation \(O(\log^r p)\). The elementary bounded-variation Riemann-sum estimate therefore yields
\[
\frac1p\sum_{j=1}^{p-1}g(j/p)^2=\frac{\pi^2}{12}+O\left(\frac{\log^2p}{p}\right),\qquad
\frac1p\sum_{j=1}^{p-1}|g(j/p)|^3=O(1).
\]
The exceptional zero residue has mass \(1/p\), and \(\log^3(p-2)/p=O(1)\). Hence
\[
v_p=\frac{\pi^2}{12}+O\left(\frac{\log^2p}{p}\right),\qquad
\mathbb E|Y_p-m_p|^3=O(1),
\]
where \(Y_p\) is the local log-magnitude variable. The variance is strictly positive for \(p=5\), while for larger primes it is nonnegative, so \(V_P>0\).

**3. Quantitative normal limit.** Summing the variance remainder over primes gives
\[
V_P=\frac{\pi^2}{12}\bigl(\pi(P)-1\bigr)+O\left(\sum_{3\le n\le P}\frac{\log^2n}{n}\right)=\frac{\pi^2}{12}\pi(P)+O((\log P)^3).
\]
In particular \(V_P\asymp\pi(P)\) for large \(P\). The sum of third absolute centered moments is \(O(\pi(P))\). The independent-summand Berry--Esseen inequality implies the displayed bound for all large \(P\); enlarging its constant handles the finitely many smaller primes. Finally the classical Mertens-type estimate \(\sum_{p\le P}(\log p)/p=\log P+O(1)\), together with \(\log(p-2)=\log p+O(1/p)\), gives \(M_P=\log P+O(1)\).

**4. Exact determinant.** Fourier diagonalization of a circulant gives \(\det\mathcal C_P=\prod_{a\bmod N}F_P(a)\). Its absolute value is
\[
\exp\left(\sum_{a\bmod N}\log|F_P(a)|\right)=e^{NM_P}=\prod_{3\le p\le P}(p-2)^{N/p}.
\]
Because \(N\) is even and \(f_P\) is supported on odd residue classes, the real Fourier eigenvalues at \(a=0\) and \(a=N/2\) are respectively \(T\) and \(-T\), with \(T=\prod_{p\le P}(p-2)\) after interpreting the factor for \(p=2\) as one. All remaining eigenvalues occur in nonzero conjugate pairs, whose products are positive. This proves the negative sign and the exact formula.

## Verification

Run `python3 verify.py` with Python 3 standard library. The script directly forms the sieve indicator and complex Fourier sums for all frequencies modulo \(30\) and \(210\), and for thirteen frequencies modulo \(2310\). It independently checks the Chinese-remainder magnitude product, all empirical log-magnitude means and variances on these three wheels, local nonvanishing and logarithmic product identities, and the exact \(30\)-by-\(30\) circulant determinant by integer Bareiss elimination (result \(-729\)). Complex checks have stated numerical tolerances; the determinant is an exact integer computation. These finite tests support but cannot establish the infinite normal-limit theorem.

## Relationship to prior work

Holt's *Discrete dynamics in Eratosthenes sieve* (first posted 2026-08-26, arXiv:2608.26384) studies the same primorial sieve cycles, admissible gap constellations, and their populations via the Chinese remainder theorem. Its exact population formulas motivate asking what the **full character spectrum** of a candidate mask does as the sieve evolves. The present work studies the additive Fourier transform of the twin-candidate mask itself, rather than Holt's transfer-matrix eigenvalues or gap-count models. Petersen and collaborators' wave-optical prime-sieve construction analyzes different optical superpositions, not the empirical law of all discrete Fourier magnitudes of this mask. Standard CRT, circulant diagonalization, Parseval, prime logarithmic sums, and Berry--Esseen are acknowledged tools. The contribution is their explicit application to this particular multiplicative twin-candidate mask, including the exact local law, universal variance constant, quantitative global law, and determinant sign and magnitude.

## Limitations

This is not a result on the actual distribution of twin primes and does not address their infinitude. The bound concerns an unnormalized transform and uniform *frequency* sampling; neither random positions nor random primes are sampled. The Gaussian statement is asymptotic in the sieve-prime cutoff and supplies no optimized numerical Berry--Esseen constant. Earlier descriptions of CRT-factorized sieve spectra or a specialized equivalent asymptotic could affect priority. No external mathematical audit has been performed.

## References

1. F. B. Holt, *Discrete dynamics in Eratosthenes sieve*, arXiv:2608.26384 (first public version 2026-08-26; revised 2026-10-23), https://arxiv.org/abs/2608.26384 .
2. T. C. Petersen, M. Ceko, I. D. Svalbe, M. J. Morgan, A. I. Bishop, D. M. Paganin, *Simple wave-optical superpositions as prime number sieves*, arXiv:1812.04203 (2018), https://arxiv.org/abs/1812.04203 .
3. Classical ingredients: the Chinese remainder theorem; Fourier analysis of cyclic groups and Parseval's identity; the Mertens prime logarithm estimate; and the Berry--Esseen inequality.
