# Numerator-independent gcd histograms for rational floor dilations

## Finding
For positive coprime integers \(p,q\), with \(q\ge 2\), consider the sequence
\[
G_{p,q}(n)=\gcd\left(n,\left\lfloor\frac{pn}{q}\right\rfloor\right),\qquad n\ge1.
\]
Put \(L=L_q=\operatorname{lcm}(1,2,\ldots,q-1)\), with \(L_2=1\), and let \(\varphi\) be Euler's totient function. Then for every integer \(B\ge0\) and \(d\ge1\),
\[
\boxed{\#\left\{BqL<n\le(B+1)qL:G_{p,q}(n)=d\right\}
=\mathbf1_{\{BL<d\le(B+1)L\}}
+\frac{L}{d}\sum_{j=1}^{\lfloor(q-1)/d\rfloor}\frac{\varphi(j)}j.}
\]
The sum is empty when its upper limit is zero. Hence *every* finite histogram on these blocks is independent of the numerator \(p\) of the reduced rational slope. In particular, for each fixed \(d\ge1\), its natural density is
\[
\delta_q(d)=\begin{cases}\displaystyle \frac1{dq}\sum_{j=1}^{\lfloor(q-1)/d\rfloor}\frac{\varphi(j)}j,&1\le d<q,\\0,&d\ge q.\end{cases}
\]
These densities have total mass \(\sum_{d\ge1}\delta_q(d)=(q-1)/q\), rather than one. For each fixed \(d\), as the reduced denominator \(q\to\infty\),
\[
\delta_q(d)=\frac1{\zeta(2)d^2}+O\!\left(\frac{\log(2q)}{dq}\right).
\]
Thus the familiar \(1/\zeta(2)\) coprimality law emerges from the rational side as \(q\) grows, even though at every fixed rational slope a proportion \(1/q\) of indices carries arbitrarily large gcd values.

## Assumptions and scope
All quantifiers in the finite-block identity are unrestricted: \(p,q\) are arbitrary positive coprime integers with \(q\ge2\); \(B\) is any nonnegative integer; and \(d\) any positive integer. The density statement is for fixed \(p,q,d\) as \(n\to\infty\). The subsequent denominator limit is for fixed \(d\) as \(q\to\infty\) through arbitrary integers, with any numerator \(p\) coprime to \(q\). No distributional limit with \(q\) varying along with \(n\) is asserted.

## Proof
Fix \(p,q\) as above. For any integer \(n\ge1\), write \(n=qk+r\) with \(k\ge0\), \(0\le r<q\). Put \(t_r=\lfloor pr/q\rfloor\) and \(s_r=pr-qt_r\). Then \(\lfloor pn/q\rfloor=pk+t_r\), and \(0\le s_r<q\). By coprimality, the list \(s_1,\ldots,s_{q-1}\) permutes \(1,\ldots,q-1\).

Choose integers \(U,V\) satisfying \(Uq+Vp=1\). The integer matrix
\[
\begin{pmatrix}U&V\\-p&q\end{pmatrix}
\]
has determinant one and therefore preserves the gcd of the coordinates of every integer column vector. Applied to \((qk+r,pk+t_r)\), this gives
\[
G_{p,q}(qk+r)=\gcd(k+Ur+Vt_r,s_r).
\]
In particular, for every fixed nonzero residue \(r\), the gcd is a translate of the periodic function \(k\mapsto\gcd(k,s_r)\). Its period divides \(s_r\), which divides \(L\) because \(1\le s_r\le q-1\). Among \(L\) consecutive \(k\)-values, exactly \((L/s_r)\varphi(s_r/d)\) have gcd equal to \(d\) if \(d\mid s_r\), and none otherwise.

In the interval \(BqL<n\le(B+1)qL\), every nonzero residue class \(r\) corresponds to exactly \(L\) consecutive indices \(k=BL,\ldots,(B+1)L-1\). Summing over the permutation \(s_r\in\{1,\ldots,q-1\}\), the number of terms contributed by all nonzero residue classes with gcd \(d\) is therefore
\[
\sum_{\substack{1\le s<q\\d\mid s}}\frac{L}{s}\varphi(s/d)
=\frac{L}{d}\sum_{j=1}^{\lfloor(q-1)/d\rfloor}\frac{\varphi(j)}j.
\]
For the remaining class \(r=0\), we have \(G_{p,q}(qk)=\gcd(qk,pk)=k\), because \(\gcd(p,q)=1\). Here \(BL<k\le(B+1)L\). Thus this residue class contributes exactly one occurrence for each \(d\) in that range, giving the displayed exact block formula. This also proves the integrality of its rational-looking sum.

For fixed \(d\), the contribution from \(r=0\) occurs in at most one of the blocks, while every block has the same contribution from \(r\ne0\). A final incomplete block has bounded length \(qL\); hence the fixed-fiber density exists with value \(\delta_q(d)\). Summing over \(d\), use the classical identity \(\sum_{e\mid s}\varphi(e)=s\) to compute
\[
\sum_{d=1}^{q-1}\delta_q(d)
=\frac1q\sum_{s=1}^{q-1}\frac1s\sum_{d\mid s}\varphi(s/d)
=\frac{q-1}{q}.
\]
The remaining \(1/q\) of indices are precisely the positive multiples \(n=qk\), whose gcd values equal \(k\) and tend to infinity. This describes loss of mass in the pointwise limiting gcd distribution, not a failure of the finite-block count.

Finally, Möbius inversion gives \(\varphi(j)/j=\sum_{e\mid j}\mu(e)/e\). Thus for \(M\ge1\),
\[
\sum_{j\le M}\frac{\varphi(j)}j
=\sum_{e\le M}\frac{\mu(e)}e\left\lfloor\frac Me\right\rfloor
=\frac{M}{\zeta(2)}+O(\log(2M)),
\]
using the absolutely convergent series \(\sum_{e\ge1}\mu(e)/e^2=1/\zeta(2)\), the bound \(\sum_{e\le M}1/e=O(\log(2M))\), and the tail \(M\sum_{e>M}1/e^2=O(1)\). Substitute \(M=\lfloor(q-1)/d\rfloor\) when \(q>d\); for \(q\le d\) the stated asymptotic is only an eventual claim in \(q\). This completes the proof.

## Verification
The standalone standard-library file `verify.py` checks the exact predicted block histograms against direct gcd enumeration for every reduced numerator in tested ranges \(2\le q\le11\) and three consecutive blocks, compares the unimodular gcd identity on independently generated integer inputs, and verifies the total finite-density mass using rational arithmetic. Its expected final record is `VERIFY_OK arithmetic=exact finite_checks_do_not_replace_general_proof=true`. The unrestricted theorem rests on the argument above, not on the finite checks.

## Relationship to prior work
Holdridge (arXiv:2611.02223v1, public November 1, 2026) proves the zeta-value coprimality law for polynomial families satisfying an irrational equidistribution hypothesis. Rational \(p/q\) does not satisfy that hypothesis, and its exact gcd histogram instead exhibits the escaping mass above. Sykora (2014) studies the specific slope \(p=1\) and the event \(G_{1,q}(n)=1\); the present theorem gives every gcd value, arbitrary reduced numerator, and an exact numerator-independent count *on each finite block*. Srichan (2023) treats pairs of floor-function values at independently varying input indices, not the same-index correlated gcd of a rational floor dilation. The pre-existing coprimality sequences in OEIS A250031 and Sykora's tables are recovered at \(p=1,d=1\) and are not claimed as new.

## Limitations
This does not cover negative or zero slopes, nonreduced numerator-denominator pairs, irrational slopes, higher-degree rational polynomials, or simultaneous variation of \(n\) and \(q\). The formula gives the distribution of single gcd values and cannot by itself settle joint correlations. Earlier unindexed versions of the full numerator-independent histogram are possible; the originality assessment is based on the identified primary literature and research-record searches, not a proof of historical uniqueness. No independent mathematical audit has been performed.

## References
- P. Holdridge, *On the probability that the integer parts of polynomials are coprime*, arXiv:2611.02223v1 (November 1, 2026), https://arxiv.org/html/2611.02223v1 .
- S. Sykora, *On some number densities related to coprimes* (November 15, 2014), doi:10.3247/SL5Math14.005, https://www.researchgate.net/publication/331586017_On_some_number_densities_related_to_coprimes .
- T. Srichan, *On the distribution of the greatest common divisor of the elements in integral part sets* (2023), doi:10.12697/ACUTM.2023.27.04, https://ojs.utlib.ee/index.php/ACUTM/article/download/ACUTM.2023.27.04/17067/30529 .
- OEIS A250031 (coprimality densities for truncation in base \(q\)), https://oeis.org/A250031 .
