# Exact joint local-square laws for consecutive even-power sums at every odd prime

## Finding

For every odd prime \(p\) define the integer power sum
\[
S_p(n)=\sum_{j=1}^{n}j^{p-1}\qquad(n\ge0).
\]
A residue \(u\pmod{p^k}\) is called a *square* when \(u\equiv v^2\pmod{p^k}\) for some integer \(v\); in particular, zero is a square. Put \(\chi=\bigl(\frac{-1}{p}\bigr)\), \(\eta=(1+\chi)/2\), and \(R=(p-4-\chi)/4\). For integers \(k\ge1\), let
\[
Z_{p,k}=1+\frac{p-1}{2}\sum_{j=1}^{\lfloor(k-1)/2\rfloor}p^{k-2j-1},\qquad
H_{p,k}=\frac{p-1}{2}p^{k-1}+Z_{p,k},
\]
\[
J_{p,k}=H_{p,k}+(p-1)\left(Rp^{k-1}+(1+\eta)Z_{p,k}\right).
\]
The *exact* counts of integers \(0\le n<p^{k+1}\), classified according to whether \(S_p(n)\) and \(S_p(n+1)\) are squares modulo \(p^k\), are

| First square? | Second square? | Exact number |
|---|---|---|
| Yes | Yes | \(J_{p,k}\) |
| Yes | No | \(pH_{p,k}-J_{p,k}\) |
| No | Yes | \(pH_{p,k}-J_{p,k}\) |
| No | No | \(p^{k+1}-2pH_{p,k}+J_{p,k}\) |

Moreover, each residue of \(S_p(n)\pmod{p^k}\) occurs exactly \(p\) times in the displayed interval. The same holds for \(S_p(n+1)\).

Treating integer indices as equidistributed in the \(p\)-adic integers, a single power sum belongs to the square set in \(\mathbb Z_p\) with natural density
\[
\mu_p=\frac{p}{2(p+1)}.
\]
Both adjacent sums belong to that square set with joint natural density
\[
\delta_p=\begin{cases}
\dfrac{p^3-p^2+p+1}{4p^2(p+1)},&p\equiv3\pmod4,\\[3pt]
\dfrac{p^3-3p^2+3p+1}{4p^2(p+1)},&p\equiv1\pmod4.
\end{cases}
\]
Their Bernoulli indicators exhibit a *strict correlation sign reversal*:
\[
\delta_p-\mu_p^2=\begin{cases}
\dfrac{2p+1}{4p^2(p+1)^2}>0,&p\equiv3\pmod4,\\[3pt]
-\dfrac{2p^3-4p-1}{4p^2(p+1)^2}<0,&p\equiv1\pmod4.
\end{cases}
\]
For each of the four outcomes, its count among \(0\le n<N\) equals its corresponding limiting probability times \(N\), with error \(O_p(\log(2N))\).

## Assumptions and scope

Here \(p\) ranges over odd **rational primes**, \(k\) over all positive integers, and the index \(n\) over nonnegative integers. The \(p\)-adic square set includes zero; equivalently a nonzero \(x\in\mathbb Z_p\) is a square precisely when its valuation is even and its normalized leading unit has quadratic character \(+1\). The notation \(S_p\) fixes the exponent to \(p-1\), rather than allowing an arbitrary exponent. The complete-period result uses the period \(p^{k+1}\); it does not assert that this is a least period. The density statements concern the index variable, not the value-set Haar density of \(S_p\).

## Proof

**1. An isometric power-sum decomposition.** The classical Fermat power-sum congruence, as discussed by MacMillan and Sondow, is
\[
\sum_{i=1}^{p}i^{p-1}\equiv-1\pmod p.
\]
For every integer \(a\) and \(e\ge1\), its elementary block lifting gives
\[
\sum_{i=1}^{p^e}(a+i)^{p-1}\equiv-p^{e-1}\pmod{p^e}.\tag{1}
\]
Indeed, the sum is independent of the starting index \(a\) modulo \(p^e\). For \(e\ge2\), write \(i=t+b p^{e-1}\), with \(1\le t\le p^{e-1}\), \(0\le b<p\); binomial expansion of the \((p-1)\)-st power, summed over \(b\), yields the previous block sum multiplied by \(p\) modulo \(p^e\) (every nonconstant term has sufficient divisibility, since \(p\) is odd). This proves (1) inductively.

If \(n-m=p^e u\), \(p\nmid u\), with \(n,m\ge0\), divide into \(|u|\) blocks and use (1). Then
\[
S_p(n)-S_p(m)\equiv-u p^{e-1}\pmod{p^e},
\quad\text{hence}\quad
\nu_p(S_p(n)-S_p(m))=e-1.\tag{2}
\]
Thus for each \(r\in\{0,\ldots,p-1\}\), the map
\[
t\longmapsto F_r(t)=S_p(r+pt)
\]
initially defined for \(t\ge0\), extends by continuity to an isometric bijection \(\mathbb Z_p\to\mathbb Z_p\). In particular, each residue of \(S_p(n)\pmod{p^k}\) occurs once as \(n\) traverses each of the \(p\) classes \(n\equiv r\pmod p\) within \(0\le n<p^{k+1}\). Consequently each output residue appears \(p\) times, and the power sums have period dividing \(p^{k+1}\) modulo \(p^k\).

**2. The exceptional adjacent-index branch.** The Faulhaber polynomial for an even positive exponent vanishes at \(n=-1\); in particular \(S_p(-1)=0\) in its continuous \(p\)-adic extension (also immediate from its Bernoulli-polynomial expression and the vanishing of odd Bernoulli numbers beyond the first). By (2), on the branch \(n=-1+pt\) one has
\[
\nu_p(S_p(n))=\nu_p((n+1)/p),\tag{3}
\]
including the convention that both sides are infinite when \(n=-1\). Furthermore
\[
S_p(n+1)-S_p(n)=(n+1)^{p-1}.
\]
If \(\nu_p((n+1)/p)=a<\infty\), the difference has valuation \((a+1)(p-1)>a\) and changes neither the valuation nor the first nonzero unit digit of \(S_p(n)\). Therefore the two consecutive values have *identical* square status in \(\mathbb Z_p\), and also modulo \(p^k\) for every \(k\) (including zero-residue status). The branch contributes exactly \(H_{p,k}\) jointly square indices, where \(H_{p,k}\) is the number of square residues modulo \(p^k\).

**3. Other branches and quadratic-character pairs.** If \(n\not\equiv-1\pmod p\), then
\[
S_p(n+1)\equiv S_p(n)+1\pmod p.
\]
For \(x\) and \(x+1\) both nonzero squares modulo \(p\), the number of possibilities for \(x\) is
\[
R=\#\{x\in\mathbb F_p:x\ne0,-1,\ \chi_p(x)=\chi_p(x+1)=1\}
=\frac{p-4-\chi_p(-1)}4.\tag{4}
\]
This follows by expanding \((1+\chi_p(x))(1+\chi_p(x+1))/4\) and subtracting the two excluded endpoints, using \(\sum_x\chi_p(x(x+1))=-1\). For each such \(x\), every one of its \(p^{k-1}\) lifts is a square in both coordinates. When \(x\equiv0\), the first coordinate is square in exactly \(Z_{p,k}\) lifts, while the second is automatically a square unit. When \(x\equiv-1\), the shifted map \(n\mapsto S_p(n+1)\) is also an isometry on the fixed branch, so the second is square in \(Z_{p,k}\) lifts and the first is a square unit if and only if \(\eta=1\). Each of the \(p-1\) index branches is a bijection onto all possible \(x=S_p(n)\pmod{p^k}\), so their joint-square contribution is
\[
(p-1)\bigl(Rp^{k-1}+(1+\eta)Z_{p,k}\bigr).
\]
Together with step 2 this is precisely \(J_{p,k}\). The primitive square-unit residues number \((p-1)p^{k-1}/2\); residues of valuation \(2j\ge2\) have \((p-1)p^{k-2j-1}/2\) possibilities, and zero counts once. This proves the formulas for \(Z_{p,k}\), \(H_{p,k}\), and \(J_{p,k}\). Since each of the two marginals has size \(pH_{p,k}\), subtraction gives all other three table entries.

**4. Infinite-digit limit and quantitative cutoff.** Dividing by the period \(p^{k+1}\) and letting \(k\to\infty\) gives
\[
\lim_{k\to\infty}H_{p,k}/p^k=\frac p{2(p+1)},\qquad
\lim_{k\to\infty}Z_{p,k}/p^k=\frac1{2p(p+1)}.
\]
Insert these limits in \(J_{p,k}/p^{k+1}\), simplify separately for \(\chi_p(-1)=\pm1\), and subtract \(\mu_p^2\). This proves the displayed densities and the strict covariance signs. The equality of finite-level class counts and Haar cylinder measures gives existence of the natural densities. For a quantitative estimate, decompose each square preimage on each isometric index branch into cylinders of fixed exact even valuation. For levels \(j\le\log_p N\), at most \(O_p(1)\) relevant cylinders occur per level; counting elements of each cylinder in an interval of length \(N\) has error at most one. All deeper cylinders in a fixed branch meet the interval in at most \(O_p(1)\) indices because their modulus exceeds \(N\). There are \(O(\log(2N))\) levels, yielding the stated \(O_p(\log(2N))\) error simultaneously for all four outcomes. This proves the entire claim.

## Verification

Run `python3 verify.py` using Python 3 and no third-party dependencies. The standalone script recomputes the exact square-status table from integer power sums for 23 prime-power cases (84,031 indices in total), checks complete-period marginal multiplicities, tests isometric branch bijections in four cases, and verifies the covariance signs at thirteen odd primes. These finite checks independently corroborate, but do not replace, the proof for every odd prime and unbounded \(k\). Specific limiting densities are \(\delta_3=11/72\), \(\delta_5=11/100\), and \(\delta_7=151/784\).

## Relationship to prior work

MacMillan and Sondow (first public October 30, 2010) present the classical power-sum congruence used in step 1. Baoulina and Moree (2015) study integrality obstructions for ratios of adjacent power sums, rather than the joint arithmetic square-status distribution. Newsome, Nogin and Sabuwala (first public December 20, 2017, a *later* supporting source) establish prime-power power-sum congruences and periodicity, which can cover the block-lifting infrastructure, not the complete four-cell local-square table or its covariance sign reversal. A previously published exact residue-fiber theorem for square-pyramidal numbers addresses the single-output value frequencies of the \(p=3\) instance; those marginals do not imply adjacent square correlations. The new contribution is the exact all-prime finite-precision *joint* square-status distribution and its change of covariance sign with \(p\bmod4\).

## Limitations

No claim is made that the block congruence, Faulhaber interpolation, the elementary finite-field character sum, or the individual square-residue count is new. The novelty assessment is based on inspected primary literature and prior-result search, not a proof of absence from all historical sources. A stronger unpublished or older general quadratic-character correlation theorem could subsume this evaluation. Finite tests are not infinite certificates. The prime two and power exponents other than \(p-1\) are outside scope. No independent external audit has been performed.

## References

1. K. MacMillan and J. Sondow, *Proofs of power sum and binomial coefficient congruences via Pascal's identity*, arXiv:1011.0076 (first public October 30, 2010), https://arxiv.org/abs/1011.0076.
2. I. N. Baoulina and P. Moree, *Forbidden integer ratios of consecutive power sums*, arXiv:1510.06064 (first public October 20, 2015), https://arxiv.org/abs/1510.06064.
3. N. J. Newsome, M. S. Nogin and A. H. Sabuwala, *Congruences of Power Sums*, arXiv:1801.01542 (first public December 20, 2017; supporting material only), https://arxiv.org/abs/1801.01542.
4. Earlier exact prime-power residue-fiber work on the square-pyramidal sequence, cited for the distinction between a marginal output distribution and the present joint-index statistic.
