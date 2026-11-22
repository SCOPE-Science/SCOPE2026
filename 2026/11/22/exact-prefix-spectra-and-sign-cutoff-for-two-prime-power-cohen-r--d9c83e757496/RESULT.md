# Exact prefix spectra and sign cutoff for two-prime-power Cohen–Ramanujan sums

## Finding

The cumulative Cohen–Ramanujan sum for a modulus with exactly two prime divisors has a complete, explicit value spectrum and a one-sided sign cutoff. With notation below, its values over a least period comprise exactly \(P^2\) points in \(P\) separated equal-length bands, with exact multiplicities. In particular,
\[
\max_{0\le n<k^s} F(n)=H(P-1),\qquad
\min_{0\le n<k^s} F(n)=-HQ(P-1).
\]
The latter is also the sharp absolute maximum. Every prefix in the initial interval \(0\le n<HQ\) is nonnegative; all later proper prefixes \(HQ\le n<k^s\) are strictly negative.

## Assumptions and scope

Let \(p<q\) be *distinct primes* and let \(a,b,s\) be positive integers. Set
\[
 k=p^a q^b,\quad P=p^s,\quad Q=q^s,\quad
 H=p^{(a-1)s}q^{(b-1)s},\quad k^s=HPQ.
\]
Define the generalized gcd \((u,v)_s\) as the greatest perfect \(s\)-th power dividing both \(u\) and \(v\). For every positive integer \(m\), Cohen's generalized Ramanujan sum is
\[
 c_k^{(s)}(m)=\sum_{\substack{1\le h\le k^s\\ (h,k^s)_s=1}}
 \exp(2\pi i mh/k^s).
\]
This is an integer, equivalently
\[
 c_k^{(s)}(m)=\sum_{\substack{d\mid k\\d^s\mid m}}d^s\mu(k/d),
\]
where \(\mu\) denotes the Möbius function. The divisor identity follows by Möbius inversion of the coprimality indicator in the defining exponential sum: each resulting complete geometric sum of order \((k/d)^s\) is zero unless \((k/d)^s\) divides \(m\), in which case its value is \((k/d)^s\). Put \(F(0)=0\) and \(F(n)=\sum_{m=1}^n c_k^{(s)}(m)\) for \(n\ge1\). All results below hold for every indicated tuple, without restrictions on the exponents.

## Proof

**Prime-power reduction.** The divisor formula shows that for every prime \(\ell\) and integer \(e\ge1\), \(c_{\ell^e}^{(s)}(m)=0\) unless \(\ell^{(e-1)s}\mid m\). If it divides, then
\[
 c_{\ell^e}^{(s)}(m)
 =\ell^{(e-1)s}\bigl(\ell^s\mathbf 1_{\ell^{es}\mid m}-1\bigr).
\]
Multiplicativity in coprime moduli gives \(c_k^{(s)}(m)=0\) unless \(H\mid m\); for \(m=Hu\), coprimality of the two prime powers yields
\[
 c_k^{(s)}(Hu)=H(1-P\mathbf 1_{P\mid u}-Q\mathbf 1_{Q\mid u}+PQ\mathbf 1_{PQ\mid u}).
\]
Consequently, if \(0\le n<HPQ\) and \(t=\lfloor n/H\rfloor\), the last indicator vanishes in the sum over \(1\le u\le t\), so
\[
 \begin{aligned}
 F(n)&=H\bigl(t-P\lfloor t/P\rfloor-Q\lfloor t/Q\rfloor\bigr)\\
 &=H\bigl((t\bmod P)-Q\lfloor t/Q\rfloor\bigr).
 \end{aligned}
\]
For \(n=HPQ\), the full-period term cancels and \(F(HPQ)=0\). Periodicity follows from the original periodic exponential definition and this vanishing full-period sum.

**Spectrum and multiplicity.** For each \(j=0,\ldots,P-1\), the block \(jQ\le t<(j+1)Q\) has \(\lfloor t/Q\rfloor=j\). As \(Q>P\), it contains every residue \(r\bmod P\). Thus the distinct values in that block are exactly \(H(r-jQ)\), \(0\le r<P\). The bands are disjoint because the highest member of band \(j+1\) is \(H(P-1-(j+1)Q)\), which is smaller than the lowest member \(-HjQ\) of band \(j\). It follows that the spectrum has \(P^2\) distinct values, namely
\[
 \mathcal V=\bigcup_{j=0}^{P-1}\{H(r-jQ):0\le r<P\}.
\]
For each fixed \(j,r\), the number of eligible \(t\) is
\[
 m_{j,r}=\left\lfloor\frac{(j+1)Q-1-r}{P}\right\rfloor
 -\left\lfloor\frac{jQ-1-r}{P}\right\rfloor.
\]
Every \(t\) corresponds to exactly \(H\) consecutive indices \(n\), so the multiplicity of \(H(r-jQ)\) is \(Hm_{j,r}\). Every \(m_{j,r}\) is either \(\lfloor Q/P\rfloor\) or \(\lceil Q/P\rceil\); all are positive. Summing their multiplicities yields \(HPQ\), as required.

**Extrema, signs, and least period.** The first band has maximum \(H(P-1)\), while the last band has minimum \(-HQ(P-1)\); since \(Q>P\), the absolute maximum is the latter magnitude. For \(t<Q\), the formula reduces to \(F(n)=H(t\bmod P)\ge0\). For \(Q\le t<PQ\), one has \(\lfloor t/Q\rfloor\ge1\) and \(t\bmod P\le P-1<Q\), so \(F(n)<0\). Together with \(F(HPQ)=0\), this proves the sharp cutoff.

The period \(HPQ\) is the *least* positive period of \(F\): if a smaller period \(d\) satisfied \(HQ<d<HPQ\), then \(F(d)<0=F(0)\), a contradiction. If \(0<d\le HQ\), periodicity would force all values of \(F\) to be nonnegative because its first \(d\) values are, contradicting the negative values in \(HQ\le n<HPQ\). This also proves that the sign transition cannot be explained by a shorter repeating block.

For clarity, in the special case \(k=6\), \(s=1\), the proper-prefix values for \(n=0,\ldots,5\) are \(0,1,0,-2,-3,-2\), with distinct values \(\{-3,-2,0,1\}\).

## Verification

The accompanying standalone `verify.py` computes \(c_k^{(s)}(m)\) independently through its Möbius–divisor formula, without using the closed form for the new theorem. It checks that actual cumulative sums agree with the formula at every index, and independently checks complete value sets, per-value multiplicities, extrema, and zero full-period sum. The reproduced output was: `PASS: 103 parameter tuples, 1138338 prefix indices, divisor-formula cross-check`. The finite experiment corroborates but is not used to infer the all-parameter theorem; that assertion rests on the elementary identities proved above.

## Relationship to prior work

Cohen introduced generalized Ramanujan sums. Thomas and Namboothiri (first arXiv version 2023-12-12) study their near-orthogonality and give a lower bound for certain maximal cumulative sums in Theorem 3.4; their paper does not furnish the above complete two-prime-power prefix spectrum, multiplicities, single sign transition, or exact extrema in this formulation. Kühn and Robles derive explicit formulas involving summation **over the modulus**, rather than the fixed-modulus prefix variable used here. The classical Möbius–divisor formula determines every value in principle; the additional content here is an explicit closed classification of the attainable partial-sum values and their counts for an infinite natural modulus family. This is a self-review, not a priority guarantee.

## Limitations

The theorem assumes exactly two *distinct* prime divisors and cannot be applied as stated to prime powers or moduli with three or more distinct prime divisors. The result gives no bound for a three-prime modulus. The published classical divisor identity means the proof is elementary once the appropriate two-prime block decomposition is isolated; the available literature search cannot rule out an earlier undocumented presentation of the same explicit spectrum. Independent audit and external verification have not been performed.

## References

- Neha Elizabeth Thomas and K. Vishnu Namboothiri, *On near orthogonality of certain k-vectors involving generalized Ramanujan sums*, arXiv:2312.07098 (first public version 2023-12-12), https://arxiv.org/abs/2312.07098 .
- Patrick Kühn and Nicolas Robles, *Explicit formulas of a generalized Ramanujan sum*, arXiv:1311.2816 (2013), https://arxiv.org/abs/1311.2816 .
- K. Vishnu Namboothiri, *On solving a restricted linear congruence using generalized Ramanujan sums*, arXiv:1708.04505 (2017), https://arxiv.org/abs/1708.04505 .
- E. Cohen, *An extension of Ramanujan's sum*, Duke Mathematical Journal 16 (1949), 85–90; standard source of the generalized sum and its divisor identities.
