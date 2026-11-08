# The exact logarithmic edge constant for reciprocal-mean divisibility graphs

## Finding
For each fixed positive integer \(m\) and each real \(X\geq1\), let \(E_m(X)\) be the number of unordered pairs of **distinct** positive integers \(1\leq a<b\leq X\) for which \(a+b\mid mab\). Then
\[
E_m(X)=C_mX\log X+O_m(X),\qquad
C_m=\frac{3\log 2}{\pi^2}\prod_{p^{\alpha}\parallel m}
\left(1+\alpha\frac{p-1}{p+1}\right).
\]
Here the empty product for \(m=1\) is one, the logarithm is natural, and the constants in the error term depend only on the fixed integer \(m\). Equivalently, the density of edges among pairs in the initial interval decays as \(2C_m\log X/X\). In the two Erdős–Graham variants,
\[
E_1(X)=\frac{3\log2}{\pi^2}X\log X+O(X),\qquad
E_2(X)=\frac{4\log2}{\pi^2}X\log X+O(X).
\]
Consequently \(E_2(X)/E_1(X)\to4/3\), and the average degrees of the corresponding graphs on \(\{1,\ldots,N\}\) are asymptotic to \(2C_m\log N\).

## Assumptions and scope
The parameter \(m\geq1\) is a **fixed** integer, while \(X\to\infty\). The divisibility relation uses ordinary positive integers, and ordered or diagonal pairs are not included. For \(m=2\), an edge is exactly a pair of denominators whose reciprocal average is another unit fraction; \(m=1\) is the companion reciprocal-sum relation. The asymptotic is not claimed uniform in growing \(m\).

## Proof
**1. Primitive parametrization and an exact identity.** Write \(a=rx\), \(b=ry\), where \(1\leq x<y\) and \(\gcd(x,y)=1\). Since \(\gcd(x+y,xy)=1\), the condition \(a+b\mid mab\) is equivalent to \(x+y\mid mr\). Thus \(r\) runs through positive multiples of \((x+y)/\gcd(m,x+y)\). Consequently,
\[
E_m(X)=\sum_{\substack{1\leq x<y\\\gcd(x,y)=1}}
\left\lfloor\frac{X\gcd(m,x+y)}{y(x+y)}\right\rfloor.
\tag{1}
\]
If a summand in (1) is nonzero, then \(y(x+y)\leq mX\), so \(y<\sqrt{mX}\). Set \(Y=\max(2,\lfloor\sqrt{mX}\rfloor)\). The number of candidate \((x,y)\) is at most \(Y^2\), hence replacing all floors by their arguments has total error \(O_m(X)\). The finitely many small \(X\) can be absorbed into the implied constant. Thus
\[
E_m(X)=X\sum_{y\leq Y}\sum_{\substack{1\leq x<y\\(x,y)=1}}
\frac{\gcd(m,x+y)}{y(x+y)}+O_m(X).
\tag{2}
\]

**2. A congruence-restricted primitive harmonic sum.** For a fixed integer \(d\geq1\), define
\[
T_d(Y)=\sum_{y\leq Y}\sum_{\substack{1\leq x<y\\(x,y)=1\\d\mid x+y}}\frac1{y(x+y)}.
\]
Using \({\mathbf{1}}_{(x,y)=1}=\sum_{r\mid(x,y)}\mu(r)\), substitute \(x=ru\), \(y=rv\), and put \(e=d/\gcd(d,r)\). This gives
\[
T_d(Y)=\sum_{r\leq Y}\frac{\mu(r)}{r^2}
\sum_{v\leq Y/r}\frac1v
\sum_{\substack{1\leq u<v\\u+v\equiv0\ (\mathrm{mod}\ e)}}\frac1{u+v}.
\tag{3}
\]
For **every** positive \(v,e\), the innermost sum is
\[
\frac{\log2}{e}+O\left(\frac1v\right).
\tag{4}
\]
Indeed, it is the sum of the decreasing function \(1/t\) over multiples of \(e\) in the interval \((v,2v)\), and comparison with the integral \(e^{-1}\int_v^{2v}dt/t\) has endpoint error at most a constant multiple of \(1/v\). The estimate is uniform in \(e\), including \(e>v\). Substitution in (3) and \(\sum_vv^{-2}<\infty\) show
\[
T_d(Y)=\log2\sum_{r\leq Y}
\frac{\mu(r)}{r^2}\frac{\gcd(d,r)}{d}\log(Y/r)+O(1).
\]
The absolutely convergent sums \(\sum_r r^{-2}\) and \(\sum_r (\log r)r^{-2}\) now imply
\[
T_d(Y)=A_d\log2\log Y+O_d(1),\qquad
A_d=\sum_{r\geq1}\frac{\mu(r)}{r^2}\frac{\gcd(d,r)}d.
\tag{5}
\]
The omitted tail contributes \(O(\log Y/Y)\), hence does not affect the stated error.

**3. Exact local factors.** The series for \(A_d\) has an Euler product. If \(p\nmid d\), its factor is \(1-p^{-2}\). If \(p^j\parallel d\) with \(j\geq1\), it is
\[
\frac1{p^j}-\frac1{p^{j+1}}=\frac{1-p^{-1}}{p^j}.
\]
Dividing by the ordinary zeta factor \(1-p^{-2}\) proves
\[
A_d=\frac1{\zeta(2)}
\prod_{p^j\parallel d}\frac1{p^{j-1}(p+1)}.
\tag{6}
\]
For every integer \(s\), \(\gcd(m,s)=\sum_{d\mid m,\ d\mid s}\varphi(d)\). Apply this identity to (2), insert (5)–(6), and evaluate the finite divisor sum multiplicatively:
\[
\begin{aligned}
\sum_{d\mid m}\varphi(d)A_d
&=\frac1{\zeta(2)}\prod_{p^\alpha\parallel m}
\left(1+\sum_{j=1}^\alpha\frac{\varphi(p^j)}{p^{j-1}(p+1)}\right)\\
&=\frac1{\zeta(2)}\prod_{p^\alpha\parallel m}
\left(1+\alpha\frac{p-1}{p+1}\right).
\end{aligned}
\tag{7}
\]
Finally \(\log Y=(\log X)/2+O_m(1)\), while \(\zeta(2)=\pi^2/6\). Equations (2), (5) and (7) give the result with error \(O_m(X)\). The ratio and average-degree assertions follow immediately. \(\square\)

## Verification
The accompanying `verify_pairs.py` performs two mathematically distinct exact enumerations: direct divisibility testing over all pairs \(a<b\) and enumeration via the unique coprime parameters in (1). These agree for \(m=1,\ldots,8\) and \(X=8,20,50,100,300\). It also evaluates exact pair counts at \(X=100000\) for \(m=1,2,3,4,6\), and checks the rational Euler factors. The computed values are independent sanity checks, not a substitute for the proof of the asymptotic. The program requires only Python's standard library.

## Relationship to prior work
The Erdős–Graham problem asks for large sets avoiding \(a+b\mid ab\) or \(a+b\mid2ab\). Korsky's July 2026 work on harmonic triples uses the same divisibility geometry and gives an **upper bound of order \(X\log X\)** for a suitable triple count, without deriving the leading constant. Sawin's July 2026 work settles the positive-density avoidance question for the second relation, by constructing edge-free sets; its method is not a formula for the unrestricted graph's total edge count. Fan and Tóth study the distinct statistic \(\gcd(ab,a+b)/\gcd(a,b)\); their density theorem for a fixed value of that statistic is not an edge-count asymptotic because the edge condition also depends on the varying quotient \((a+b)/\gcd(a,b)\). The present result concerns an exact unrestricted first-moment asymptotic, including a parameter-dependent Euler product and the comparison of the two classical relations. OEIS A362931 (2023) already defines and tabulates the **exact finite count** of ordered pairs for the integral harmonic-mean relation; specifically its entry equals \(X+2E_2(X)\) at integer \(X\). Those numerical values and the elementary coprime parametrization are not claimed as new. The claimed distinction is the exact large-interval leading constant, its linear remainder, and the arbitrary fixed-\(m\) Euler product. Neither the existence of dense independent sets nor their optimal density follows from counting all edges.

## Limitations
No assertion is made about maximal independent-set sizes, the number of edges induced by Sawin's selected subset, or uniform error bounds when \(m\) varies with \(X\). Historical priority may be affected by unindexed exact counts, especially older work on integer harmonic triples. The error term is linear and no second-order constant is asserted.

## References
1. S. Korsky, *Large Sets of Integers with No Harmonic Triples* (first posted 2026-07-07), https://arxiv.org/abs/2607.05823.
2. W. Sawin, *Sets of unit fractions without two members whose average is a unit fraction* (first posted 2026-07-16), https://arxiv.org/abs/2607.15419.
3. P. Erdős and R. L. Graham, *Old and New Problems and Results in Combinatorial Number Theory* (1980), problem referenced in the above papers.
4. OEIS A362931 (2023), number of ordered pairs with integral harmonic mean, https://oeis.org/A362931; numerical table https://oeis.org/A362931/b362931.txt.
5. OEIS A055081 (2000), count of partners with integral harmonic mean, https://oeis.org/A055081.
6. S. Fan and L. Tóth, *On the asymptotic density of the ordered pairs of positive integers such that \(\gcd(ab,a+b)=\gcd(a,b)\)*, https://arxiv.org/abs/2606.20057 (related but different statistic).
7. E. W. Weisstein, *Harmonic Triple*, MathWorld, https://mathworld.wolfram.com/HarmonicTriple.html (background and historical terminology).
