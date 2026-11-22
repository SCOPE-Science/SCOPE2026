# Quadratic-form reduction and prime-index dichotomy for tagged odd-part totals

## Finding

Let \(T(n)=\mathrm{PDO}_{\mathrm t}(n)\) be the total number of tagged parts in all designated-summand partitions of \(n\) using only odd parts, with \(T(0)=0\). Write \(x_t=6t-1\) for \(t\in\mathbb Z\), and for \(d\in\{1,3,12\}\) let
\[
R_d(n)=\#\{(t,j)\in\mathbb Z\times\mathbb Z_{\ge1}:n=x_t^2+d j^2\},\qquad
\varepsilon(n)=\sum_{t\in\mathbb Z:\,x_t^2=n}(-1)^t.
\]
Every one of these sums is finite for \(n\ge1\). Then, for every integer \(n\ge1\),
\[
\boxed{T(n)\equiv\varepsilon(n)+2R_1(n)-2R_3(n)-2R_{12}(n)\pmod4.}
\]
Consequently, for every prime \(p\ge5\), write \(p=a^2+b^2\) when \(p\equiv1\pmod4\), with the uniquely determined positive odd coordinate \(a\) and positive even coordinate \(b\). Then
\[
\boxed{T(p)\equiv\begin{cases}
2\pmod4,&p\equiv1\pmod4\text{ and }3\nmid a,\\
0\pmod4,&p\equiv3\pmod4\text{, or }(p\equiv1\pmod4\text{ and }3\mid a).
\end{cases}}
\]
In particular, every prime \(p\equiv5\pmod{12}\) has \(T(p)\equiv2\pmod4\), while primes \(p\equiv1\pmod{12}\) split according to the divisibility of their odd Gaussian coordinate by three. These are infinite arithmetic distinctions, with at least one quarter of all primes in the nonzero class, by Dirichlet's theorem.

There is also an explicit composite-index obstruction: if any prime \(r\equiv11\pmod{12}\) occurs to odd exponent in \(n\ge1\), then \(T(n)\equiv0\pmod4\). Independently, \(T(n)\equiv0\pmod4\) whenever \(n\equiv3\pmod4\).

## Assumptions and scope

The statement is about the tagged-part total, not the number of partitions and not the separately defined count \(\mathrm{PDO}(n)\). Standard arithmetic of Gaussian integers, Euler's pentagonal-number identity, parity of the divisor-count function, and the two-squares theorem for primes are used. The formula is coefficientwise for all positive integers, not just a finite computation. The displayed prime-index dichotomy is restricted to primes at least five; directly \(T(2)\equiv2\pmod4\) and \(T(3)\equiv0\pmod4\).

## Proof

Put \(E(q)=\prod_{m\ge1}(1-q^m)\), and \(P(q)=E(q^2)/E(q)^2\). The established generating function for the tagged odd-part total is
\[
F(q)=\sum_{n\ge0}T(n)q^n=q\frac{E(q^2)E(q^3)^2E(q^{12})^2}{E(q)^2E(q^6)}
=qE(q^{24})P(q)P(q^3)^{-1}P(q^{12})^{-1}.
\]
Because \(P(q)=\prod_{m\ge1}(1+q^m)/(1-q^m)\), every nonconstant factor is \(1+2\sum_{j\ge1}q^{mj}\) modulo four. Thus the cross terms vanish modulo four and
\[
P(q)\equiv1+2\sum_{n\ge1}d(n)q^n\pmod4,
\]
where \(d(n)\) is the positive-divisor count. That count is odd if and only if \(n\) is a square. Consequently, in \(\mathbb Z[[q]]/4\mathbb Z[[q]]\),
\[
P(q)\equiv1+2\sum_{j\ge1}q^{j^2},\qquad
P(q^h)^{-1}\equiv1-2\sum_{j\ge1}q^{h j^2}\quad(h=3,12).
\]
Euler's pentagonal-number theorem, on substituting \(q^{24}\), gives
\[
E(q^{24})=\sum_{t\in\mathbb Z}(-1)^tq^{12t(3t-1)},
\qquad 1+12t(3t-1)=(6t-1)^2.
\]
Multiplying the formal series and comparing coefficients gives the stated exact residue formula for all \(n\ge1\). This is a coefficientwise identity modulo four, not an asymptotic statement.

Now suppose \(p\ge5\) is prime. No \((6t-1)^2\) equals \(p\), so \(\varepsilon(p)=0\). If \(p\equiv3\pmod4\), the two-squares theorem eliminates \(R_1(p)\), while \(x_t\) is odd and the possible residues of \(x_t^2+3j^2\) and \(x_t^2+12j^2\) are respectively \(0,1\) and \(1\pmod4\); neither equals \(3\). Hence \(T(p)\equiv0\pmod4\).

For \(p\equiv1\pmod4\), the congruence \(x_t^2+3j^2\equiv1\pmod4\) forces \(j\) even. The map \(j\mapsto j/2\) therefore bijects every counted \(R_3(p)\)-solution to an \(R_{12}(p)\)-solution with the same \(t\). Their combined coefficient is \(-4R_{12}(p)\equiv0\pmod4\). The two-squares theorem expresses \(p\) uniquely as \(a^2+b^2\), with \(a>0\) odd and \(b>0\) even. Exactly one of \(a\) and \(-a\) is congruent to \(5\pmod6\) precisely when \(3\nmid a\); if \(3\mid a\), neither is congruent to \(5\pmod6\). Therefore \(R_1(p)\) is one or zero accordingly, proving the prime formula. If \(p\equiv5\pmod{12}\), reduction of \(a^2+b^2=p\) modulo three forces both \(a\) and \(b\) nonzero modulo three, so \(R_1(p)=1\). Dirichlet's theorem gives relative prime density \(1/4\) for this entire nonzero subfamily.

Finally let \(r\equiv11\pmod{12}\) be prime. Both \(-1\) and \(-3\) are quadratic nonresidues modulo \(r\). For either binary form \(u^2+v^2\) or \(u^2+3v^2\), if \(r\) divides its value then \(r\mid u,v\), so its value has even \(r\)-adic valuation; repeating after division by \(r^2\) proves this at every exponent. The forms \(x_t^2+j^2\), \(x_t^2+3j^2\), and \(x_t^2+12j^2=x_t^2+3(2j)^2\) are all excluded at indices with odd \(r\)-valuation, as is the single-square term. All summands in the residue formula vanish. The \(n\equiv3\pmod4\) conclusion follows by the same local congruence checks for the three forms and square term. This finishes the proof.

## Verification

The standalone standard-library script `verify.py` expands the original eta quotient, without using the square-representation formula, and compares its coefficients with the independent quadratic-form expression for each \(1\le n\le2000\). It separately tests every prime \(5\le p\le2000\) against the stated Gaussian-coordinate rule, as well as all odd-valuation inert-prime instances in this range. These finite calculations detect implementation errors, but the all-index conclusions follow from the formal-series and local arithmetic proof above, not from the finite tests.

Illustrative prime values: \(T(5)\equiv2\), \(T(13)\equiv0\), \(T(17)\equiv2\), \(T(37)\equiv2\), \(T(73)\equiv0\pmod4\).

## Relationship to prior work

Li and Tang's November 2026 study of \(\mathrm{PDO}_{\mathrm t}(n)\) established families of higher \(3\)-power congruences and states its exact generating function. Lin originally introduced the tagged-part total. Baruah and Kaur (2018) established modulo-two, four and eight congruences, including certain full progressions for this function. Chern and Hirschhorn (2021) proved selected progressions divisible by 36 and 3456, without giving a prime-index Gaussian classification. Barman, G. Singh and A. Singh (online 2023; 2024 volume) proved more power-of-two congruences and the general lacunarity of this function modulo arbitrary powers of two and three. OEIS A293422 provides the coefficient generating function and a finite numerical table, rather than a uniform prime-index law. None of those leading-density or progression assertions is claimed as new here. The present claim is the explicit all-index quadratic-form reduction and its prime-index odd-Gaussian-coordinate classification; the reviewed earlier results do not give these precise statements. An implicit equivalent in older modular identities or an unindexed source remains possible.

## Limitations

The formula is modulo four only; it does not classify residues modulo eight or high powers. The prime formula does not give a proven exact density for the subfamily \(p\equiv1\pmod{12}\) with \(3\nmid a\), nor does it establish a full prime-factorization characterization for all composite indices. Independent review of both novelty and proof is outstanding. Existing general lacunarity is stronger than any density-one consequence obtained here and is not a novelty claim.

## References

- X. Li and D. Tang, *Congruence properties modulo powers of 3 for designated summands in partitions into odd parts*, arXiv:2611.15164v1, publicly submitted 2026-11-11. https://arxiv.org/html/2611.15164v1
- N. D. Baruah and N. Kaur, *Number of tagged parts over the partitions of designated summands*, arXiv:1807.01074 (2018). https://arxiv.org/pdf/1807.01074
- S. Chern and M. D. Hirschhorn, *Some results concerning partitions with designated summands*, *The Ramanujan Journal* 54 (2021), 385–395. https://doi.org/10.1007/s11139-019-00198-1
- OEIS A293422, *The PDO_t(n) function*, coefficient sequence and original generating function. https://oeis.org/A293422
- R. Barman, G. Singh, and A. Singh, *Divisibility of the partition function PDO_t(n) by powers of 2 and 3*, *Bulletin of the Australian Mathematical Society* 109 (2024), 14–25, published online 2023. https://doi.org/10.1017/S0004972723000199
- G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers*, chapters on sums of squares, Euler products and the pentagonal-number theorem (classical background).
