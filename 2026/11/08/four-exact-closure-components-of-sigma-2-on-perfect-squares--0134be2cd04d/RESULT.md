# Four exact closure components of \(\sigma_{-2}\) on perfect squares

## Finding

For each positive integer \(n\), put
\[
F(n)=\sigma_{-2}(n^2)=\sum_{d\mid n^2}\frac{1}{d^2}.
\]
The complete closure of its range is
\[
\overline{F(\mathbb N)}=
[1,\pi^2/9]\ \cup\ [91/81,\pi^2/8]\ \cup\
[21/16,4\pi^2/27]\ \cup\ [637/432,\pi^2/6].
\]
The four intervals are pairwise disjoint. In increasing order they correspond to \(\gcd(n,6)=1\), \(3\mid n,\ 2\nmid n\), \(2\mid n,\ 3\nmid n\), and \(6\mid n\), with closure taken separately within each class. Hence the closure has exactly four components and exactly three nonempty gaps.

## Assumptions and scope

The domain is all positive integers \(n\); every prime factor of the argument \(n^2\) has an even nonnegative exponent. The theorem concerns ordinary positive divisors (not unitary or exponential divisors) and the topological closure in \(\mathbb R\). Endpoints arising from infinite Euler products or unbounded prime exponents need not themselves be values of \(F\). We use the classical identity \(\zeta(2)=\pi^2/6\) and the proven consecutive-prime ratio lemma cited below.

## Proof

**Local factors.** If \(n=\prod_p p^{a_p}\), multiplicativity gives
\[
 F(n)=\prod_p A_p(a_p),\qquad
 A_p(0)=1,\quad
 A_p(a)=\sum_{j=0}^{2a}p^{-2j}
 =\frac{1-p^{-4a-2}}{1-p^{-2}}\quad(a\ge1).
\]
The factors increase with \(a\), and tend to \(U_p=(1-p^{-2})^{-1}\). In particular,
\[
A_2(1)=21/16,\quad U_2=4/3,\qquad
A_3(1)=91/81,\quad U_3=9/8.
\]

**A full interval from primes at least five.** Put \(p_1=2,p_2=3,p_3=5,\ldots\), and let
\[
 M=\prod_{j\ge3}U_{p_j}
 =\zeta(2)(1-2^{-2})(1-3^{-2})=\pi^2/9.
\]
We prove that the closure of products \(\prod_{p\ge5}A_p(a_p)\), with finitely many nonzero integer exponents, is exactly \([1,M]\).

Set \(b_j=\log U_{p_j}>0\). The series \(\sum_{j\ge3}b_j\) converges to \(\log M\). We claim that for every \(j\ge3\),
\[
 U_{p_j}\le\prod_{i>j}U_{p_i},
 \quad\text{equivalently}\quad b_j\le\sum_{i>j}b_i. \tag{1}
\]
For \(p_j\in\{5,7,11,13,17,19,23\}\), exact rational multiplication already proves the stronger finite inequalities
\[
\prod_{p_j<q\le Q_j}(1+q^{-2})>\frac{p_j^2}{p_j^2-1},
\]
where the seven ordered pairs \((p_j,Q_j)\) are
\[
(5,23),\ (7,23),\ (11,17),\ (13,19),\ (17,23),\ (19,29),\ (23,31).
\]
Only **prime** values \(q\) enter each product; every inequality is exact and is recomputed by `verify.py` using rational arithmetic.

For \(j\ge10\), \(p_j\ge29\). Lemma 2.2 of Defant, *Ranges of Unitary Divisor Functions* (arXiv:1507.02654), states that \(p_{j+1}/p_j<\sqrt[3]{2}<4/3\) whenever \(j\notin\{1,2,3,4,6,9\}\). For \(r=1,2,3\) it follows that \(p_{j+r}<(4/3)^r p_j\). Consequently
\[
\prod_{r=1}^3 U_{p_{j+r}}
\ge\prod_{r=1}^3(1+p_{j+r}^{-2})
>1+\sum_{r=1}^3p_{j+r}^{-2}
>1+\frac{4329}{4096p_j^2}
>1+\frac1{p_j^2-1}=U_{p_j}.
\]
The penultimate inequality holds since \(4329/4096>29^2/(29^2-1)\ge p_j^2/(p_j^2-1)\). This proves (1) for all \(j\ge3\).

We spell out the needed binary-subsums lemma. For any positive summable sequence \((b_j)\) obeying \(b_j\le\sum_{i>j}b_i\), every \(t\in[0,\sum b_j]\) is a sum of some of its terms. To construct the subset, at the \(j\)-th step choose coefficient \(\varepsilon_j=0\) if the current residual is at most the remaining suffix sum, and otherwise choose \(\varepsilon_j=1\); the inequality on \(b_j\) ensures that the new residual lies between zero and the remaining suffix sum. That suffix tends to zero, yielding \(t=\sum\varepsilon_jb_j\). Exponentiation shows that all \(y\in[1,M]\) are infinite products \(\prod_{j\in J}U_{p_j}\). Such a product is a limit of **finite** products \(\prod_{j\in J,\,j\le L}A_{p_j}(a_j)\): first truncate its convergent Euler product and then let each of finitely many \(a_j\) grow. Those finite products are \(F(n)\) with \(\gcd(n,6)=1\). All these products are at most \(M\), proving the asserted exact tail closure.

**Four merging branches.** Fix whether \(2\mid n\) and \(3\mid n\), and fix their respective exponents \(a,b\), with \(0\) denoting absence. The tail result gives the complete interval
\[
 I_{a,b}=[A_2(a)A_3(b),\ M A_2(a)A_3(b)]
\]
as the closure for that fixed pair. When \(a\ge1\),
\[
 1<\frac{A_2(a+1)}{A_2(a)}\le\frac{U_2}{A_2(1)}=\frac{64}{63}<M.
\]
When \(b\ge1\), likewise
\[
1<\frac{A_3(b+1)}{A_3(b)}\le\frac{U_3}{A_3(1)}=\frac{729}{728}<M.
\]
Both strict final inequalities have the exact rational certificate
\[
M=\frac23\sum_{k=1}^{\infty}k^{-2}
>\frac23\sum_{k=1}^{8}k^{-2}>\frac{64}{63}>\frac{729}{728}.
\]
Hence every two adjacent exponent-index intervals overlap (vary one positive exponent while holding the other fixed). The grid of all such index pairs is connected, so the entire branch's union of intervals is connected. Its closure is the closed interval from its smallest endpoint to the product of its limiting local factors and \(M\). The four choices give, respectively,
\[
[1,M],\quad[91/81,(9/8)M],\quad
[21/16,(4/3)M],\quad[637/432,(3/2)M],
\]
which are precisely the claimed four intervals because \(M=\pi^2/9\).

**Exactly three gaps.** The classical upper bound \(\pi<22/7\) implies \(\pi^2<484/49\). Exact rational comparisons show
\[
\frac{\pi^2}{9}<\frac{91}{81},\qquad
\frac{\pi^2}{8}<\frac{21}{16},\qquad
\frac{4\pi^2}{27}<\frac{637}{432}.
\]
Therefore the four nonempty closed intervals are separated. Every positive integer falls in precisely one of the four classes by divisibility by \(2,3\); no other values or components are possible. This completes the proof.

## Verification

The included `verify.py` uses Python 3 standard-library rational arithmetic to validate all seven finite prime-tail products, the prime-ratio comparison, lower and upper rational inequalities for \(M\), local factor extrema, and the three strict gaps. It independently checks that \(F(n)\) for each integer \(1\le n\le60000\) belongs to exactly one predicted interval and that its interval agrees with the two divisibility flags. Its output begins `VERIFY_OK`. Floating-point calculations in this last diagnostic are not used to prove the theorem. The infinite prime-ratio lemma and binary-subsums argument are proved or sourced mathematically, not inferred from enumeration.

## Relationship to prior work

Defant, *On the Density of Ranges of Generalized Divisor Functions with Restricted Domains* (2015), investigates exponent-**bounded** domains (\(k\)-free integers), whereas the present domain has positive prime exponents constrained to be **even** and unbounded. His related 2015 paper on *unitary* divisor functions supplies the published prime-ratio lemma used above; its arithmetic function is different from \(F\). Sanna's 2015 preprint classifies the unrestricted range \(\overline{\sigma_{-2}(\mathbb N)}\) into three intervals, which does not imply the square-input restriction or its fourth component. The different domains/functions and the specific implication gap were checked; this historical search cannot rule out an earlier equivalent classification under different terminology.

## Limitations

The statement is only for the exponent \(-2\) and inputs restricted to perfect squares. It determines the closure, not exact arithmetic multiplicities, densities of interval components within square indices, or which individual real points belong to the nonclosed range. The argument imports the established consecutive-prime-ratio lemma. No independent mathematical audit has been performed.

## References

1. C. Defant, *On the Density of Ranges of Generalized Divisor Functions with Restricted Domains* (2015), arXiv:1507.02663, https://arxiv.org/abs/1507.02663.
2. C. Defant, *Ranges of Unitary Divisor Functions* (2015 preprint, later revision), arXiv:1507.02654, https://arxiv.org/abs/1507.02654, Lemma 2.2.
3. C. Sanna, *On the Closure of the Image of the Generalized Divisor Function* (2015 preprint), arXiv:1507.08091, https://arxiv.org/abs/1507.08091.
