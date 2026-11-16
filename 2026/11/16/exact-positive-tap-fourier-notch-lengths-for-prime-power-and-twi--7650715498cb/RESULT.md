# Exact positive-tap Fourier-notch lengths for prime-power and twice-prime-power cyclic spectra

## Finding

A finite impulse-response filter with \(L+1\) taps \(a_0,\ldots,a_L\) is called *positive-tap* when all \(a_j>0\). At a cyclic period \(N\), require its frequency response to vanish at **all primitive Fourier characters**:

\[
\sum_{j=0}^{L}a_j e^{2\pi ijt/N}=0\qquad (1\le t<N,\ \gcd(t,N)=1).
\]

The complete set of feasible lengths is a tail of the nonnegative integers. Its first member is exactly

\[
L_{\min}+1=\begin{cases}
N,&N=p^k,\quad p\text{ prime},\ k\ge1,\\
N-\dfrac{N}{2p},&N=2^s p^k,\quad p\ge3\text{ odd prime},\ s,k\ge1.
\end{cases}
\]

Every feasible length admits strictly positive **integer** taps. In particular, for \(N=6\), exactly five or more positive taps are necessary and sufficient, while for \(N=20\), exactly eighteen or more suffice. The statements concern primitive frequencies as an entire collection; they do not claim simultaneous nulls at nonprimitive frequencies.

## Assumptions and scope

Throughout, \(N\ge2\), \(L\ge0\) and all taps are strictly positive real numbers. The two mutually exclusive families are prime powers and numbers \(2^s p^k\) with \(p\) odd prime and \(s,k\ge1\). No assertion is made for periods with two distinct odd prime factors, or for an arbitrary union of frequency notches. Put \(F(X)=\sum_{j=0}^{L}a_jX^j\) and let \(\Phi_N\) denote the cyclotomic polynomial. The primitive-frequency condition is equivalent to \(\Phi_N\mid F\) in \(\mathbb R[X]\), since \(\Phi_N\) has precisely the primitive \(N\)-th roots as simple zeros. Here \(L\) is exactly the degree because \(a_L>0\).

## Proof

**Residue decomposition.** For a positive integer \(q\), write uniquely

\[
F(X)=\sum_{r=0}^{q-1}X^rF_r(X^q),\qquad
F_r(Y)=\sum_{j=0}^{\lfloor(L-r)/q\rfloor}a_{r+qj}Y^j
\]

where an empty sum is zero. For any monic polynomial \(P\), the divisibility \(P(X^q)\mid F(X)\) is equivalent to \(P(Y)\mid F_r(Y)\) for every residue \(r\). Indeed, division by \(P(X^q)\) respects all \(q\) exponent residues. Whenever \(L\ge r\), the coefficients of \(F_r\) are strictly positive and occur at every degree from zero through its top degree.

**Prime powers.** If \(N=p^k\), set \(q=p^{k-1}\). Then \(\Phi_N(X)=\Phi_p(X^q)\) and \(\deg\Phi_p=p-1\). If \(\Phi_N\mid F\), then \(L\ge\deg\Phi_N=(p-1)q\), so residue \(r=q-1\) exists. The corresponding nonzero \(F_{q-1}\) must have degree at least \(p-1\). Hence

\[
\left\lfloor\frac{L-q+1}{q}\right\rfloor\ge p-1,
\qquad L\ge pq-1=N-1.
\]

The polynomial \(1+X+\cdots+X^{N-1}\) proves sharpness: it has exactly \(N\) strictly positive unit taps and vanishes at every nontrivial \(N\)-th root.

**Odd-prime mixed powers.** Suppose \(N=2^sp^k\), where \(p\ge3\) is odd, and set \(q=2^{s-1}p^{k-1}\). The identity \(\Phi_N(X)=\Phi_{2p}(X^q)\) reduces each residue polynomial to divisibility by

\[
P(Y)=\Phi_{2p}(Y)=1-Y+Y^2-\cdots+Y^{p-1}.
\]

We first prove the critical short-polynomial lemma: if \(B(Y)=\sum_{j=0}^{m}b_jY^j\), all \(b_j>0\), and \(P\mid B\), then \(m\ge2p-2\). If \(m<p-1\), degree alone forbids divisibility. If \(p-1\le m\le2p-3\), reduce \(B\) modulo \(Y^p+1\), which is divisible by \(P\). The remainder is

\[
R(Y)=\sum_{j=0}^{p-1}(b_j-b_{j+p})Y^j,
\]

where out-of-range coefficients are zero. Because \(P\mid R\) and \(\deg R\le p-1\), necessarily \(R=cP\) for some real \(c\). Yet its consecutive coefficients at degrees \(p-2\) and \(p-1\) are \(b_{p-2}>0\) and \(b_{p-1}>0\), whereas those of \(cP\) have opposite signs (or are zero). Contradiction. The lemma is proved.

For \(F\), again \(L\ge\deg\Phi_N=(p-1)q\), so \(F_{q-1}\ne0\). Applying the lemma gives

\[
\left\lfloor\frac{L-q+1}{q}\right\rfloor\ge2p-2,
\qquad L\ge(2p-1)q-1=N-q-1.
\]

To attain the bound, choose \(\varepsilon=1/2\) and define

\[
H_p(Y)=(1+Y^p)\sum_{j=0}^{p-2}Y^j
+\frac12Y^{p-1}\Phi_{2p}(Y).
\]

Both summands are divisible by \(\Phi_{2p}\), since \(\Phi_{2p}(Y)\mid(1+Y^p)\). The coefficients of \(H_p\) are: 1 in degrees \(0,\ldots,p-2\); \(1/2\) in degree \(p-1\); and \(1\pm1/2\) in degrees \(p,\ldots,2p-2\). Thus every coefficient is strictly positive and \(\deg H_p=2p-2\). Set

\[
F_*(X)=\left(\sum_{r=0}^{q-1}X^r\right)H_p(X^q).
\]

This has all coefficient positions filled positively, is divisible by \(\Phi_{2p}(X^q)=\Phi_N(X)\), and has degree \((2p-1)q-1=N-q-1\). Multiplying by 2 makes all coefficients positive integers.

**All longer lengths.** For either minimal construction \(F_*\), multiplying by \(1+X+\cdots+X^m\) for any integer \(m\ge0\) preserves strictly positive coefficients at every position, cyclotomic divisibility and integer positivity, and raises degree by exactly \(m\). This proves necessity and sufficiency for every proposed length, not merely the shortest one.

## Verification

The exact proof above applies to all stated primes and exponents. `verify.py` checks the two construction formulas and symbolic divisibility with exact rational arithmetic across a specified sample of 20 periods, including \(N=6,10,12,18,20,24,36,50,72,90\). A separate numerical linear-programming stress test of periods \(3,4,6,8,9,10,12,18,20\) found a strictly positive solution at the claimed boundary and none one degree earlier. These finite tests corroborate, but do not substitute for, the general residue proof.

## Relationship to prior work

Steinberger (2012) and Tan–Zhang (2026) determine the shortest *nonnegative*, potentially sparse cyclotomic multiples. Their exact solutions allow zero coefficients; the full-consecutive-support constraint here changes the feasible-length threshold and distinguishes prime powers from mixed powers. In particular their smallest nonnegative multiple for even \(N\) has degree \(N/2\), whereas the strictly positive family here has degree \(N-N/(2p)-1\) at \(N=2^sp^k\). Brunotte (2012, 2013) studies positive multiples of real polynomials and solves quadratic cases, which can include base-period instances; its accessible summaries do not establish the all-exponent, all-odd-prime formula above. The 2011 paper by Reddy concerns sparse zero–one polynomial multiples, not strict positivity of all consecutive taps.

## Limitations

No assertion is made for cyclic periods outside the two specified factorization families. The proof does not optimize the tap dynamic range or robustness near the notches. Earlier equivalences in the literature on positive polynomial multiples cannot be excluded without fuller access to the 2012–2013 Brunotte articles; their complete manuscripts were not obtained. This result is a mathematical self-review, not an independent audit.

## References

1. H. Tan and Y. Zhang, *Sharp Diameter Bounds for Nonnegative Cyclotomic Multiples*, arXiv:2609.07646, first public version 7 September 2026, https://arxiv.org/abs/2609.07646.
2. J. P. Steinberger, *The Lowest-Degree Polynomial with Nonnegative Coefficients Divisible by the \(n\)-th Cyclotomic Polynomial*, Electron. J. Combin. 19 (2012), P1, https://doi.org/10.37236/2755.
3. H. Brunotte, *Polynomials with nonnegative coefficients and a given factor*, Period. Math. Hung. 66 (2013), 61–72, https://doi.org/10.1007/s10998-012-7333-3.
4. H. Brunotte, *On some classes of polynomials with nonnegative coefficients and a given factor*, Period. Math. Hung. 67 (2013), 15–32, https://doi.org/10.1007/s10998-013-2367-8.
5. A. S. Reddy, *The lowest degree 0,1-polynomial divisible by cyclotomic polynomial*, arXiv:1106.1271, https://arxiv.org/abs/1106.1271.
