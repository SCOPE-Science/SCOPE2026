# Primorial obstructions force \(b\log b\) growth for primitive Frobenius numbers

## Finding
For coprime positive integers \(a,b\), let \(g(a,b)\) denote the largest nonnegative integer not expressible as \(ax+by\) with nonnegative integer coefficients \(x,y\) satisfying \(\gcd(x,y)=1\). (Existence of this largest integer follows from Ding–Wang–Zhang and was independently studied by Jaffe.) For every fixed integer \(a\ge3\),
\[
\liminf_{\substack{b\to\infty\\\gcd(a,b)=1}}\frac{g(a,b)}{b\log b}\ge1.
\]
Thus \(g(a,b)/b\to\infty\) along coprime \(b\), whereas the previously established cases \(a=1\) and \(a=2\) have linear growth.

An explicit finite-parameter obstruction underlies the result. For integers \(K\ge a\), put
\[
P_a(K)=\prod_{\substack{p\le K\text{ prime}\\p\nmid a}}p.
\]
Whenever \(\gcd(a,b)=1\) and \(Kb>aP_a(K)\), there is a nonrepresentable positive integer \(N\) with
\[
Kb-aP_a(K)<N\le Kb,
\qquad N\equiv0\pmod{P_a(K)},\qquad N\equiv-b\pmod a.
\]
In particular, \(g(a,b)\ge N>Kb-aP_a(K)\).

## Assumptions and scope
The fixed coefficient \(a\) is an arbitrary integer at least three. The second coefficient \(b\) ranges over positive integers coprime to \(a\), and tends to infinity in the asymptotic assertion. All logarithms are natural. The coefficients \(x,y\) in a representation are nonnegative integers, including zero, and their gcd is the usual nonnegative gcd. The integer \(K\) in the explicit construction is a positive integer with \(K\ge a\).

## Proof
**1. Chinese remainder witness.** Because every prime dividing \(P_a(K)\) is coprime to \(a\), the two congruences
\[
N\equiv0\pmod{P_a(K)},\qquad N\equiv-b\pmod a
\]
select a unique class modulo \(aP_a(K)\). When \(Kb>aP_a(K)\), this class has a representative \(N\) in the interval \((Kb-aP_a(K),Kb]\). In particular \(N>0\). Choose the greatest such representative, which is uniquely determined.

**2. Obstruction to a primitive representation.** Suppose \(N=ax+by\) for some nonnegative integers \(x,y\). Reducing modulo \(a\), and using \(\gcd(a,b)=1\), yields \(y\equiv-1\pmod a\). Consequently \(y\ge a-1\ge2\) and \(\gcd(y,a)=1\). Furthermore \(y\le N/b\le K\). Select any prime \(p\mid y\). Then \(p\le K\), \(p\nmid a\), so \(p\mid P_a(K)\mid N\). As \(p\mid by\), the equality \(ax=N-by\) gives \(p\mid ax\). Because \(p\nmid a\), we have \(p\mid x\). Thus \(p\mid\gcd(x,y)\), ruling out a primitive representation. This proves the explicit obstruction.

**3. Asymptotic threshold.** Fix \(0<\varepsilon<1\) and put \(K=\lfloor(1-\varepsilon)\log b\rfloor\). As \(b\to\infty\), this eventually satisfies \(K\ge a\). The prime number theorem in Chebyshev's form says \(\sum_{p\le K}\log p=K+o(K)\). Since \(a\) is fixed, removing its finitely many prime divisors changes that sum by \(O_a(1)\). Hence
\[
\log P_a(K)=K+o(K),\qquad P_a(K)=b^{1-\varepsilon+o(1)}=o(b).
\]
For all sufficiently large coprime \(b\), the hypothesis \(Kb>aP_a(K)\) holds. The explicit obstruction yields
\[
\frac{g(a,b)}{b\log b}>\frac{K}{\log b}-\frac{aP_a(K)}{b\log b}=1-\varepsilon-o(1).
\]
Taking the liminf and then allowing \(\varepsilon\downarrow0\) proves the claim. \(\square\)

## Verification
The accompanying standard-library Python file `verify.py` evaluates the Chinese remainder witness with exact integers, checks its congruences and interval, and independently enumerates **every** nonnegative solution of \(ax+by=N\) in 408 finite parameter cases. Its output is `VERIFY_OK`. The analytic asymptotic is proved by the prime number theorem and does not follow from finite testing.

## Relationship to prior work
Yuchen Ding, Weijia Wang and Hao Zhang, *The Diophantine Frobenius Problem revisited* (arXiv:2509.08599v1, first submitted September 10, 2025), studied the same primitive-coefficient Frobenius number and proved the general two-sided bounds \(ab\le g(a,b)\ll ab(\log(ab))^2\). Those bounds do not contain the fixed-\(a\) logarithmically growing lower bound established here. Grace Natalie Jaffe, *Denominators in the Farey Sequence, the Stern Sequence, and the Frobenius Problem with Relatively Prime Multipliers* (arXiv:2610.17267v1, first submitted October 12, 2026), defines \(g(a,b)\), proves its finiteness, and analyzes special cases, numeric values, and the relation with Farey denominators and Jacobsthal-type problems. Shunpei Shimizu, *A factor-four lower bound for the Frobenius problem with relatively prime multipliers* (Zenodo, October 20, 2026), establishes a uniform lower bound proportional to the ordinary Frobenius number using finite prime coverings. The present asymptotic holds for **fixed \(a\ge3\)** and grows without bound relative to the ordinary Frobenius number; it is not implied by a constant-factor bound. Its Chinese remainder construction is related in method to Shimizu's.

## Limitations
Only a lower bound is proved: no matching upper bound \(O_a(b\log b)\), exact asymptotic, or optimality of the leading constant one is asserted. The limit considers fixed \(a\), not a uniform regime in which \(a\) grows with \(b\). A matching statement for \(a=1\) or \(2\) would be false. No claim of independent mathematical validation or exhaustive literature priority is made.

## References
1. Y. Ding, W. Wang and H. Zhang, *The Diophantine Frobenius Problem revisited*, arXiv:2509.08599v1 (2025), https://arxiv.org/abs/2509.08599.
2. G. N. Jaffe, *Denominators in the Farey Sequence, the Stern Sequence, and the Frobenius Problem with Relatively Prime Multipliers*, arXiv:2610.17267v1 (2026), https://arxiv.org/abs/2610.17267.
3. S. Shimizu, *A factor-four lower bound for the Frobenius problem with relatively prime multipliers (Jaffe's Conjecture 7.2)*, Zenodo DOI 10.5281/zenodo.23480212 (2026), https://doi.org/10.5281/zenodo.23480212.
4. The prime number theorem, in the classical equivalent form \(\vartheta(x)=\sum_{p\le x}\log p\sim x\).
