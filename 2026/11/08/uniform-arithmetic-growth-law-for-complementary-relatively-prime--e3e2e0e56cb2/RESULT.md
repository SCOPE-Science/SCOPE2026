# Uniform arithmetic growth law for complementary relatively-prime subset counts

## Finding
For \(n\ge4\), define \(R(n)=(2^n-D(n))/(2^n-\Phi(n))\), with \(D\) and \(\Phi\) as below. If \(a(n)\) is the least integer \(g\ge2\) not dividing \(n\), and \(p(n)\) is the least prime factor of \(n\), set
\[
h(n)=\left\lfloor\frac{n}{a(n)}\right\rfloor-\left\lfloor\frac{n}{p(n)}\right\rfloor.
\]
Then, for **every** \(n\ge4\),
\[
\frac{2^{h(n)}}{2(n+1)}\le R(n)\le 2(n+1)2^{h(n)}.
\]
In particular, \(\log_2R(n)=h(n)+O(\log n)\) uniformly, and
\[
\lim_{m\to\infty}R(2m)=0,\qquad
\lim_{m\to\infty}R(2m+1)=+\infty.
\]
Thus the lower and upper limits in Question 3.3 of Pongsriiam (2013) are exactly \(0\) and \(+\infty\).

## Assumptions and scope
For any positive integer \(m\), \(f(m)\) counts nonempty subsets of \(\{1,\ldots,m\}\) with gcd equal to one. Let \(D(n)=\sum_{d\mid n}f(d)\). Let \(\Phi(n)\) count nonempty subsets of \(\{1,\ldots,n\}\) whose gcd is coprime to \(n\). Define \(a(n)=\min\{g\ge2:g\nmid n\}\) and let \(p(n)\) be the smallest prime factor of \(n\). For \(n\ge4\), \(a(n)\le n-1\), since \(n-1\) cannot divide \(n\), so these numbers exist and all expressions are defined. Both deficits in the quotient are positive.

## Proof
For every \(1\le g\le n\), the number of nonempty subsets of \(\{1,\ldots,n\}\) having gcd exactly \(g\) equals \(f(\lfloor n/g\rfloor)\): divide each element by \(g\). The known gcd-divides-\(n\) interpretation of \(D(n)\) and the definition of \(\Phi(n)\) give exact, disjoint gcd-partitions
\[
\begin{aligned}
A(n):=2^n-D(n)&=1+\sum_{\substack{2\le g\le n\\g\nmid n}}f(\lfloor n/g\rfloor),\\
B(n):=2^n-\Phi(n)&=1+\sum_{\substack{2\le g\le n\\\gcd(g,n)>1}}f(\lfloor n/g\rfloor).
\end{aligned}
\]
The initial \(1\) counts the empty set, excluded from the defining counts. The smallest admissible \(g\) in the first sum is \(a(n)\). The smallest in the second is \(p(n)\): every integer not coprime to \(n\) is at least its smallest prime factor.

For any \(m\ge1\), every nonempty subset containing \(1\) has gcd one, while at most all nonempty subsets qualify. Hence \(2^{m-1}\le f(m)\le2^m-1\). Since each sum contains at most \(n\) terms and \(f(m)\) increases with \(m\), the leading admissible term gives
\[
2^{\lfloor n/a(n)\rfloor-1}\le A(n)\le (n+1)2^{\lfloor n/a(n)\rfloor},
\]
and likewise
\[
2^{\lfloor n/p(n)\rfloor-1}\le B(n)\le (n+1)2^{\lfloor n/p(n)\rfloor}.
\]
Divide these positive bounds to obtain the stated two-sided inequality and logarithmic law. In particular, \(\left|\log_2R(n)-h(n)\right|\le\log_2(2(n+1))\).

If \(n\) is even, \(p(n)=2\) and \(a(n)\ge3\). Therefore \(h(n)\le\lfloor n/3\rfloor-n/2\), and \(R(n)\le2(n+1)2^{\lfloor n/3\rfloor-n/2}\to0\) along even indices. If \(n\) is odd, \(a(n)=2\) and \(p(n)\ge3\). Thus \(h(n)\ge\lfloor n/2\rfloor-\lfloor n/3\rfloor\), and \(R(n)\ge 2^{\lfloor n/2\rfloor-\lfloor n/3\rfloor}/[2(n+1)]\to+\infty\). The two global limits follow.

## Verification
Run `python3 verify.py` in the same directory. The pure-standard-library program independently computes the Möbius formulas for \(f\) and \(\Phi\), checks \(f\) by direct enumeration of nonempty subsets through \(m=13\), confirms both complement identities and both exact integer inequalities for every \(4\le n\le400\), and tests the parity classification. Its expected last line is `VERIFY_OK direct_subset_n=1..13; complement_and_sandwich_n=4..400; exact_integer_only`. The proof, not this finite check, covers all \(n\ge4\).

## Relationship to prior work
Pongsriiam, *Relatively Prime Sets, Divisor Sums, and Partial Sums* (2013), develops these functions, gives their counting interpretations and asks in Question 3.3 for the limsup and liminf of the ratio of complementary counts. Pongsriiam, *Local Behaviors of the Number of Relatively Prime Sets* (2015/2016), Theorem 9, already proves the sign of \(D(n)-\Phi(n)\) alternates by parity, so **that sign result is not claimed as new**. The finding here is instead an explicit two-sided, uniform arithmetic exponential-growth law for the *ratio of deficits*, which resolves the two limits asked in Question 3.3. OEIS A224840 lists the divisor sum \(D\), not a statement implying the uniform quotient bounds.

## Limitations
The inequality is accurate up to a multiplicative factor \(2(n+1)\), not a relative asymptotic with constant one. It does not evaluate Pongsriiam's additional weighted or unweighted partial-sum questions, classify all lower-order fluctuations, or establish historical priority beyond the inspected sources. Independent mathematical review has not been conducted.

## References
1. P. Pongsriiam, *Relatively Prime Sets, Divisor Sums, and Partial Sums*, Journal of Integer Sequences 16 (2013), Article 13.9.1, arXiv:1306.4891 (first public June 20, 2013), Question 3.3. https://arxiv.org/abs/1306.4891
2. P. Pongsriiam, *Local Behaviors of the Number of Relatively Prime Sets*, International Journal of Number Theory 12 (2016), 1575–1593, Theorem 9. https://doi.org/10.1142/S1793042116500962
3. OEIS A224840, divisor sum of relatively prime subset counts. https://oeis.org/A224840
