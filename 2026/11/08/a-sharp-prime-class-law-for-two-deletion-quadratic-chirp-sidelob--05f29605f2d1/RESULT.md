# A sharp prime-class law for two-deletion quadratic chirp sidelobe energy

## Finding

Let \(p\ge3\) be an odd prime. For each root \(u\in\{1,\ldots,p-1\}\), form the periodic unimodular quadratic chirp
\[
c_u(n)=\exp\!\left(-\frac{\pi i u n(n+1)}p\right),\qquad n\in\mathbb Z/p\mathbb Z.
\]
Erase precisely two distinct entries, at sites \(a\) and \(a+d\), where \(d\not\equiv0\pmod p\), obtaining \(y(n)\). For its unnormalized cyclic autocorrelation
\[
R(k)=\sum_{n\bmod p}y(n+k)\overline{y(n)},
\]
let the integrated squared sidelobe energy be
\[
I_p(u,d)=\sum_{k=1}^{p-1}|R(k)|^2.
\]
Write \(r\in\{1,\ldots,p-1\}\) for the residue \(r\equiv u d^2 4^{-1}\pmod p\), and let \(\chi_p(r)\in\{-1,1\}\) be the Legendre symbol. The **exact all-prime identity** is
\[
\boxed{
I_p(u,d)=4p-22-8\cos\!\left(\frac{8\pi r}{p}\right)
+\begin{cases}
4\sqrt p\,\chi_p(r)\left(1+\cos\!\left(\frac{2\pi r}{p}\right)\right),&p\equiv1\pmod4,\\[2mm]
4\sqrt p\,\chi_p(r)\sin\!\left(\frac{2\pi r}{p}\right),&p\equiv3\pmod4.
\end{cases}}
\]
Equivalently, if \(Y(m)=\sum_{n\bmod p}y(n)\exp(-2\pi i mn/p)\) is the unnormalized discrete Fourier transform, then Parseval and the correlation identity give
\[
I_p(u,d)=\frac1p\sum_{m=0}^{p-1}|Y(m)|^4-(p-2)^2.
\]
Thus the result also determines an exact punctured-chirp Fourier fourth moment, a natural trigonometric-polynomial invariant.

The energy is independent of the erasure origin \(a\). As \(u\) runs through the nonzero roots, \(r\) also runs bijectively through the nonzero residues, for **every** spacing \(d\). Consequently the exact optimal energy and indeed the entire multiset of root energies are independent of erasure spacing; root optimizers for one spacing are transported to another by the inverse-square scaling.

A second, sharp conclusion describes the optimal energy as prime length increases. Put
\[
\gamma_p=\begin{cases}8,&p\equiv1\pmod4,\\4,&p\equiv3\pmod4.\end{cases}
\]
Then, uniformly over all \(d\not\equiv0\pmod p\),
\[
\boxed{\min_{1\le u<p} I_p(u,d)
=4p-30-\gamma_p\sqrt p
+O\!\left(\frac{(\log p)^2}{\sqrt p}\right).}
\]
More precisely, the error relative to the displayed lower bound is **nonnegative**, bounded above by an absolute multiple of \((\log p)^2/\sqrt p\) for sufficiently large primes, and therefore tends to zero. The \(\sqrt p\)-order saving is twice as large along primes \(p\equiv1\pmod4\) as along primes \(p\equiv3\pmod4\). This result is specific to two erased entries and is not a claim about aperiodic correlations or arbitrary phase codes.

## Assumptions and scope

The chirp is periodic modulo the odd prime \(p\), and both erased samples have amplitude exactly zero. All other entries retain their original values. All lag sums are cyclic over \(\mathbb Z/p\mathbb Z\), with no normalization by \(p\) or by the number of lags. The energy excludes lag zero, where \(R(0)=p-2\). For the all-prime formula \(p=3\) is allowed (then only one sample remains and the sidelobe energy is zero). The asymptotic formula concerns \(p\to\infty\) through odd primes and is uniform in the two erasure positions. The minimization is over root indices in the quadratic-chirp family, not all possible sequences.

## Proof

**1. Erasure identity and periodicity.** Since \(p\) is odd, \(c_u(n+p)=c_u(n)\). The chirp has perfect periodic autocorrelation:
\[
\sum_{n\bmod p}c_u(n+k)\overline{c_u(n)}
=p\,\mathbf1_{k=0},
\]
by summing the nontrivial character \(n\mapsto\exp(-2\pi i ukn/p)\) when \(k\ne0\). Translation of both erased sites only introduces a unit-modulus modulation of the translated chirp and hence preserves all autocorrelation magnitudes. Thus assume \(a=0\) without loss of generality.

For \(k\ne0\), let
\[
Q(k)=\sum_{b\in\{0,d\}}c_u(b+k)\overline{c_u(b)}
=\exp\!\left(-\frac{\pi iuk(k+1)}p\right)
\left(1+\exp\!\left(-\frac{2\pi iukd}p\right)\right).
\]
Deleting both endpoints of the two corrupted lag products gives, by inclusion-exclusion,
\[
R(k)=-Q(k)-\overline{Q(-k)}+E(k),
\]
where \(E(k)=0\) for \(k\not\equiv\pm d\), \(E(d)=c_u(d)\overline{c_u(0)}\), and \(E(-d)=\overline{E(d)}\). The two exceptional lags are distinct because \(p\) is odd. Factoring the first two terms gives
\[
-Q(k)-\overline{Q(-k)}
=-4\exp\!\left(-\frac{\pi iuk(d+1)}p\right)
\cos\!\left(\frac{\pi ukd}p\right)
\cos\!\left(\frac{\pi uk^2}p\right).
\]
At either exceptional lag the squared magnitude changes from \(16C^4\) to \((1-4C^2)^2\), where \(C=\cos(\pi u d^2/p)\). Hence
\[
I_p(u,d)=16\sum_{k=1}^{p-1}
\cos^2\!\left(\frac{\pi ukd}p\right)
\cos^2\!\left(\frac{\pi uk^2}p\right)
+2-16\cos^2\!\left(\frac{\pi ud^2}p\right).
\tag{1}
\]

**2. Exact quadratic-sum evaluation.** Put \(e_p(z)=\exp(2\pi i z/p)\), \(G_p(u)=\sum_{k\bmod p}e_p(uk^2)\), and write \(\bar4\) for the inverse of four modulo \(p\). Expanding \(4(1+\cos(2\pi ukd/p))(1+\cos(2\pi uk^2/p))\), and completing squares in the two sums with quadratic phases \(uk^2\pm ukd\), gives
\[
16\sum_{k=1}^{p-1}\cos^2\!\left(\frac{\pi ukd}p\right)
\cos^2\!\left(\frac{\pi uk^2}p\right)
=4(p-4)+4\operatorname{Re}\!\left[G_p(u)
\left(1+e_p(-u d^2\bar4)\right)\right].
\]
Indeed the four elementary sums appearing here are \(p-1\), \(-1\), \(\operatorname{Re}G_p(u)-1\), and \(\operatorname{Re}[G_p(u)e_p(-u d^2\bar4)]-1\), respectively. Equation (1) consequently becomes
\[
I_p(u,d)=4p-22-8\cos\!\left(\frac{2\pi ud^2}p\right)
+4\operatorname{Re}\!\left[G_p(u)
\left(1+e_p(-u d^2\bar4)\right)\right].
\tag{2}
\]
The classical quadratic Gauss-sum formula states
\[
G_p(u)=\varepsilon_p\chi_p(u)\sqrt p,
\quad\varepsilon_p=\begin{cases}1,&p\equiv1\pmod4,\\i,&p\equiv3\pmod4.\end{cases}
\]
Under \(r\equiv ud^2\bar4\), the character satisfies \(\chi_p(u)=\chi_p(r)\) because \(d^2\bar4\) is a square. Equation (2) simplifies exactly to the displayed two-branch energy formula. The map \(u\mapsto r\) is a permutation of the nonzero residues, proving all claimed spacing invariances.

**3. Sharp universal lower bound.** In the first branch, \(-8\cos(8\pi r/p)\ge-8\), while
\(4\sqrt p\chi_p(r)(1+\cos(2\pi r/p))\ge-8\sqrt p\). Thus
\[
I_p(u,d)\ge4p-30-8\sqrt p\qquad(p\equiv1\pmod4).
\]
In the second branch, the term \(4\sqrt p\chi_p(r)\sin(2\pi r/p)\) is at least \(-4\sqrt p\), giving
\[
I_p(u,d)\ge4p-30-4\sqrt p\qquad(p\equiv3\pmod4).
\]

**4. Quadratic characters of both signs in short intervals.** For completeness, the needed estimate is proved directly. For every interval \(J\subset\{1,\ldots,p-1\}\) and every odd prime \(p\),
\[
\left|\sum_{r\in J}\chi_p(r)\right|\le C\sqrt p\log p
\tag{3}
\]
with an absolute constant \(C\). In fact, the finite Fourier transform of the nontrivial quadratic character has zero frequency-zero coefficient and all remaining coefficients of magnitude \(\sqrt p\). To see the latter directly, square the modulus of its Fourier coefficient and put \(x=ty\) in the resulting double sum: character orthogonality reduces it to \(p\). The Fourier transform of an interval of length \(h\) has coefficient magnitude bounded by \(\min(h,1/|\sin(\pi m/p)|)\) at nonzero frequency \(m\). Summing this bound over \(m\) gives \(O(p\log p)\). Fourier inversion proves (3). Consequently, every interval of length greater than \(C\sqrt p\log p\), sufficiently far from the residue zero, contains both a quadratic residue and a nonresidue.

**5. Matching upper bound.** Let \(H=K\sqrt p\log p\) for a sufficiently large absolute \(K\). For all sufficiently large primes \(H=o(p)\). If \(p\equiv1\pmod4\), choose a nonresidue \(1\le r\le H\) using (3). Then \(\chi_p(r)=-1\), and the exact formula yields
\[
I_p(u,d)-(4p-30-8\sqrt p)
=8\left(1-\cos\!\frac{8\pi r}p\right)
+4\sqrt p\left(1-\cos\!\frac{2\pi r}p\right)
=O\!\left(\frac{(\log p)^2}{\sqrt p}\right).
\]
If \(p\equiv3\pmod4\), choose a nonresidue \(r\) in an interval of length \(O(H)\) centered on \(p/4\), again using (3). Now \(\sin(2\pi r/p)=1+O(H^2/p^2)\) and \(\cos(8\pi r/p)=1+O(H^2/p^2)\), so
\[
I_p(u,d)-(4p-30-4\sqrt p)
=8\left(1-\cos\!\frac{8\pi r}p\right)
+4\sqrt p\left(1-\sin\!\frac{2\pi r}p\right).
\]
Thus the difference is also \(O((\log p)^2/\sqrt p)\). Each chosen \(r\) corresponds to a unique \(u\) for every \(d\). Together with step 3 this proves the sharp uniform asymptotic.

## Verification

Run the standalone standard-library checker `python3 check_two_erasure.py`. It compares the closed expression against direct complex cyclic autocorrelation across both erased-site locations, all roots and all spacings for odd primes through \(17\). It also tests full root-energy multiset invariance for representative spacings through \(53\), and compares exact minima against the analytic lower bound at selected larger primes. The finite checks corroborate (but do not establish) the all-prime theorem. The analytical proof relies on the classical quadratic Gauss-sum formula and the explicitly proved character-interval estimate.

## Relationship to prior work

Gregoratti, Arteaga and Broquetas (arXiv:2311.01035v1, 2023) prove standard prime Zadoff–Chu autocorrelation and quadratic Gauss-sum formulas, including the DFT multiplier; they do not consider two erased positions, the resulting full-period squared sidelobe sum, or root-optimized sharp prime-class asymptotics. Andrews (arXiv:2211.05702v1, 2022) discusses CAZAC correlation and non-prime truncation, which differs from zeroing two positions while maintaining a prime-length cyclic correlator. Lee and Yang (2014) study partial-period correlations and moments; the mathematical overlap is plausible for adjacent missing positions, but their interval-restricted correlation is not the same as the both-endpoint-masked prime-cyclic correlation here. The complete 2014 paper was not available for a proof-by-proof comparison. Standard character-sum estimates furnish the short-interval nonresidue step; none alone supplies the exact erasure-energy identity or its sharp congruence-dependent constants.

## Limitations

Only odd prime cyclic lengths, standard quadratic chirp roots and exactly two fully erased coordinates are covered. The optimizing roots are described by the exact finite formula and sharp asymptotic; no simple closed formula for each finite-prime minimizing root is claimed. The result does not minimize the peak (maximum) sidelobe, handle arbitrary multi-erasure masks, or compare against non-chirp phase sequences. Its sharp asymptotic is proven as the prime length grows; it supplies no explicit numerical value of the implicit constant or a uniform small-prime cutoff. The full 2014 Lee–Yang article was inaccessible, leaving a bounded bibliographic priority risk.

## References

1. D. Gregoratti, X. Arteaga, J. Broquetas, *Mathematical Properties of the Zadoff-Chu Sequences*, arXiv:2311.01035v1 (first posted 2023-11-02), Sections 2–3 and Appendix B. https://arxiv.org/abs/2311.01035
2. J. G. Andrews, *A Primer on Zadoff Chu Sequences*, arXiv:2211.05702v1 (first posted 2022-11-10), Section II. https://arxiv.org/html/2211.05702v1
3. T.-K. Lee, K. Yang, *Partial-Period Correlations of Zadoff–Chu Sequences and Their Relatives*, IEEE Transactions on Information Theory **60** (2014), 5791–5802, doi:10.1109/TIT.2014.2334319 (abstract and bibliographic description only).
4. Classical quadratic Gauss-sum evaluation and the elementary finite-Fourier proof of the character-interval bound are stated and used explicitly in the proof above.
