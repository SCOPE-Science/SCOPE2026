# Resonant affine laws for residue-class gaps of two-generator numerical semigroups

## Finding
Let \(m\ge2\) and let \(a,b>1\) be coprime integers. Write \(N_r(a,b;m)\) for the number of positive integers outside \(\langle a,b\rangle\) congruent to \(r\pmod m\), where \(0\le r<m\). Put \(d=\gcd(a,m)\) and \(e=\gcd(b,m)\). In particular, \(\gcd(d,e)=1\).

**Exact generator-step law.** Whenever \(\gcd(a,b+m)=1\), for every \(0\le r<m\),
\[
N_r(a,b+m;m)-N_r(a,b;m)
=\frac{a-d}{2}+\operatorname{rem}_{d}(b^{-1}r).
\]
Here \(\operatorname{rem}_{d}(z)\) is the representative in \(\{0,\ldots,d-1\}\); \(b^{-1}\) is taken modulo \(d\), and the remainder is defined as zero when \(d=1\). Symmetrically, whenever \(\gcd(a+m,b)=1\),
\[
N_r(a+m,b;m)-N_r(a,b;m)
=\frac{b-e}{2}+\operatorname{rem}_{e}(a^{-1}r).
\]
Both right-hand sides are nonnegative integers. These identities include all nonunit cases \(\gcd(ab,m)>1\).

**Uniform sharp leading discrepancy.** Define \(\Delta_m(a,b)=\max_r N_r(a,b;m)-\min_r N_r(a,b;m)\). Then
\[
\left|\Delta_m(a,b)-\frac{(d-1)b+(e-1)a}{m}\right|
\le \frac{m^2}{4}+\frac m2.
\]
The coefficient of each generator is exact as a leading-order coefficient along every admissible fixed-residue progression. In particular, if \(m\mid a\), \(b\equiv1\pmod m\), and \(\gcd(a,b)=1\), there is a complete arithmetic-progression histogram:
\[
N_r(a,b;m)=\frac{(b-1)(a-m+2r)}{2m}\qquad(0\le r<m),
\]
so the discrepancy is exactly \((m-1)(b-1)/m\).

## Assumptions and scope
All statements quantify over every integer modulus \(m\ge2\) and every coprime generator pair \(a,b>1\). The step identities require the new pair also to be coprime, since otherwise the complement need not be finite. No inverse modulo one is needed: by convention the corresponding remainder is zero. The discrepancy bound is nonasymptotic; the leading-term phrase means its error is bounded solely in terms of \(m\), uniformly over all admissible pairs. It does not assert that the error is optimal.

## Proof
Let \(G_{a,b}(z)=\sum_{n\notin\langle a,b\rangle,\ n\ge0}z^n\). The standard unique-representative decomposition below \(ab\) gives the polynomial identity
\[
G_{a,b}(z)=\frac1{1-z}-\frac{1-z^{ab}}{(1-z^a)(1-z^b)}.
\]
Its value at one equals the classical genus \(g=(a-1)(b-1)/2\). Let \(\zeta\ne1\) be any \(m\)-th root of unity. Since \(\gcd(a,b)=1\), the equalities \(\zeta^a=1\) and \(\zeta^b=1\) cannot hold simultaneously. Taking removable limits gives
\[
G_{a,b}(\zeta)=\frac1{1-\zeta}-
\begin{cases}
\dfrac{b}{1-\zeta^b},&\zeta^a=1,\\[3pt]
\dfrac{a}{1-\zeta^a},&\zeta^b=1,\\[3pt]
\dfrac{1-\zeta^{ab}}{(1-\zeta^a)(1-\zeta^b)},&\zeta^a\ne1,\ \zeta^b\ne1.
\end{cases}
\]
Thus if \(b\) is replaced by \(b+m\), all nontrivial Fourier modes remain unchanged except those with \(\zeta^a=1\), where the difference is \(-m/(1-\zeta^b)\). There are precisely \(d\) roots with \(\zeta^a=1\), namely the \(d\)-th roots of unity. Finite Fourier inversion and the elementary identity
\[
\sum_{\substack{\zeta^d=1\\\zeta\ne1}}
\frac{\zeta^{-r}}{1-\zeta^b}
=\frac{d-1}{2}-\operatorname{rem}_{d}(b^{-1}r)
\]
show that the nonconstant part of the step is \(\operatorname{rem}_{d}(b^{-1}r)-(d-1)/2\). The genus increases by \(m(a-1)/2\), whose constant Fourier contribution is \((a-1)/2\). Adding these pieces gives the first claimed identity. Interchanging \(a\) and \(b\) proves the second. The Fourier identity follows by multiplying a finite sawtooth polynomial by \(1-z^b\) at all nontrivial \(d\)-th roots, or by summing a geometric series.

For the discrepancy statement, invert the same root-of-unity formulas but separate the resonant modes. For \(0\le r<m\) one obtains the *exact* decomposition
\[
N_r(a,b;m)=\frac{(a-1)(b-1)}{2m}
+\frac b m\left(\operatorname{rem}_d(b^{-1}r)-\frac{d-1}{2}\right)
+\frac a m\left(\operatorname{rem}_e(a^{-1}r)-\frac{e-1}{2}\right)
+R_{m;a\bmod m,b\bmod m}(r),
\]
where the two remainders vanish at modulus one and the residual term is
\[
R(r)=\frac1m\sum_{\substack{\zeta^m=1\\\zeta\ne1}}\frac{\zeta^{-r}}{1-\zeta}
-\frac1m\sum_{\substack{\zeta^m=1\\\zeta^a\ne1,\ \zeta^b\ne1}}\zeta^{-r}
\frac{1-\zeta^{ab}}{(1-\zeta^a)(1-\zeta^b)}.
\]
All summands in \(R\) depend only on the residue classes of \(a,b\pmod m\). For a nontrivial \(m\)-th root, every nonzero quantity \(1-\zeta^j\) has modulus at least \(2\sin(\pi/m)\ge4/m\). Hence \(\lvert R(r)\rvert\le m/4+m^2/8\).

Because \(d\) and \(e\) are coprime divisors of \(m\), the Chinese remainder theorem allows the two remainder values above to attain their independent minima \((0,0)\) and maxima \((d-1,e-1)\) as \(r\) ranges modulo \(m\). Thus the range of the two resonant terms is exactly \(((d-1)b+(e-1)a)/m\). Adding \(R\) changes a range by at most \(\max R-\min R\le m/2+m^2/4\), proving the uniform inequality. Finally, when \(m\mid a\) and \(b\equiv1\pmod m\), every nontrivial mode has \(G_{a,b}(\zeta)=(1-b)/(1-\zeta)\). Inverting that sawtooth and adding the genus yields the stated arithmetic-progression histogram.

## Verification
The included standalone `check.py` uses Boolean coin-representability up to the Sylvester conductor rather than Fourier sums or Apéry formulas. It passed 6,266 complete histogram/discrepancy comparisons, 4,383 valid steps in each generator direction, and 340 tests of the exact arithmetic-progression specialization. The finite tests are regression checks, not the proof of the universal identities.

## Relationship to prior work
Shor's work on equidistribution of numerical-semigroup gaps (first publicly available January 5, 2021) characterizes exact balancing, including the coprime-to-\(m\) restriction for the two-generator setting. Komatsu and Zhang's weighted Sylvester sums give general formulas from which individual Fourier modes can be evaluated, including resonant roots. Those results establish the raw generating-function ingredients; they do not state the generator-step sawtooth law or optimize the nonunit discrepancy simultaneously in both generators. The contribution here is the all-modulus affine transfer and the sharp simultaneous resonance coefficient, not the existence of the gap polynomial, the genus, or general weighted-Sylvester computability. A previously unnoticed equivalent consequence of the earlier weighted formulas remains a priority risk.

## Limitations
There is no claim that the residual error bound is sharp, or that every finite parameter pair achieves the leading term exactly. The source-based originality assessment remains provisional; the result is not independently audited. The method depends on the special two-generator rational Hilbert series and does not establish analogous formulas for arbitrary embedding dimension.

## References
- C. M. Shor, *Equidistribution of numerical semigroup gaps modulo \(m\)*, arXiv:2101.01760, first posted 2021-01-05, https://arxiv.org/abs/2101.01760.
- T. Komatsu and Y. Zhang, *Weighted Sylvester sums on the Frobenius set*, arXiv:2105.08274, first posted 2021-05-18, https://arxiv.org/abs/2105.08274.
- T. Komatsu and Y. Zhang, *Weighted Sylvester sums on the Frobenius set in more variables*, arXiv:2101.04298, first posted 2021-01-12, https://arxiv.org/abs/2101.04298.
