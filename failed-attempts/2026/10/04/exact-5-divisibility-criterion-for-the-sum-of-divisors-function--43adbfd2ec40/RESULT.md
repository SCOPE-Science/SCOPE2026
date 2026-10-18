# Exact \(5\)-divisibility criterion for the sum-of-divisors function

## Finding
Let
\[
n=\prod_q q^{a_q}
\]
be the prime factorization of a positive integer. Then
\[
5\mid \sigma(n)
\]
if and only if at least one prime-power factor \(q^{a_q}\Vert n\) belongs to one of the following three classes:
\[
q\equiv1\pmod5,\qquad a_q\equiv4\pmod5;
\]
\[
q\equiv4\pmod5,\qquad a_q\equiv1\pmod2;
\]
or
\[
q\equiv2,3\pmod5,\qquad a_q\equiv3\pmod4.
\]
The factor \(5^{a_5}\) never contributes to \(5\)-divisibility of \(\sigma(n)\).

Equivalently,
\[
5\nmid\sigma(n)
\]
if and only if every prime exponent obeys
\[
\begin{cases}
a_q\not\equiv4\pmod5,&q\equiv1\pmod5,\\
a_q\equiv0\pmod2,&q\equiv4\pmod5,\\
a_q\not\equiv3\pmod4,&q\equiv2,3\pmod5,
\end{cases}
\]
with no restriction on \(a_5\).

As a consequence,
\[
\#\{n\le x:5\mid\sigma(n)\}=x-o(x).
\]
Thus the integers whose divisor sum is divisible by \(5\) have natural density \(1\).

There is also an exact first-valuation refinement. One has
\[
\nu_5(\sigma(n))=1
\]
if and only if exactly one prime-power factor is contributing and that factor is of one of the following types:
\[
q\equiv1\pmod5,\qquad \nu_5(a_q+1)=1;
\]
\[
q\equiv4\pmod5,\qquad a_q\equiv1\pmod2,\qquad 5\nmid a_q+1,\qquad q\not\equiv24\pmod{25};
\]
or
\[
q\equiv2,3\pmod5,\qquad a_q\equiv3\pmod4,\qquad 5\nmid a_q+1,\qquad q\not\equiv7,18\pmod{25}.
\]
Every other prime-power factor must satisfy the noncontributing conditions above.

## Assumptions and scope
The function
\[
\sigma(n)=\sum_{d\mid n}d
\]
is the ordinary sum-of-divisors function, and \(\nu_5(m)\) is the exponent of \(5\) in \(m\).

The classification is exact for every positive integer \(n\). The density statement uses the classical divergence of
\[
\sum_{\substack{q\ \mathrm{prime}\\q\equiv4\pmod5}}\frac1q.
\]
No quantitative error term for the density-one assertion is claimed.

## Proof
For a prime \(q\) and exponent \(a\ge1\), the odd-prime valuation formula of Amdeberhan, Moll, Sharma, and Villamizar specializes at \(p=5\) to
\[
\nu_5(\sigma(q^a))=
\begin{cases}
\nu_5(a+1),&q\equiv1\pmod5,\\
0,&q=5,\\
0,&q\not\equiv1\pmod5,\ \operatorname{ord}_5(q)\nmid a+1,\\
\nu_5(a+1)+\nu_5(q^{\operatorname{ord}_5(q)}-1),
&\text{otherwise.}
\end{cases}
\]
Since \(\sigma\) is multiplicative,
\[
\nu_5(\sigma(n))=\sum_{q^{a_q}\Vert n}\nu_5(\sigma(q^{a_q})).
\]

The nonzero residue classes modulo \(5\) have orders
\[
\operatorname{ord}_5(q)=
\begin{cases}
1,&q\equiv1\pmod5,\\
2,&q\equiv4\pmod5,\\
4,&q\equiv2,3\pmod5.
\end{cases}
\]

If \(q\equiv1\pmod5\), the local contribution is simply
\[
\nu_5(a+1),
\]
so it is positive exactly when
\[
a\equiv4\pmod5.
\]

If \(q\equiv4\pmod5\), a contribution occurs exactly when \(2\mid a+1\), or equivalently when \(a\) is odd. In that case
\[
\nu_5(q^2-1)=\nu_5(q+1),
\]
because \(5\nmid q-1\), and hence
\[
\nu_5(\sigma(q^a))=\nu_5(a+1)+\nu_5(q+1).
\]
It is therefore always positive for odd \(a\).

If \(q\equiv2,3\pmod5\), a contribution occurs exactly when
\[
4\mid a+1,
\]
or
\[
a\equiv3\pmod4.
\]
Here \(5\nmid q^2-1\), while \(5\mid q^2+1\), so
\[
\nu_5(q^4-1)=\nu_5(q^2+1).
\]
Thus
\[
\nu_5(\sigma(q^a))=\nu_5(a+1)+\nu_5(q^2+1)
\]
in the contributing case. This proves the divisibility classification.

For the level-one refinement, the sum of the nonnegative local contributions equals \(1\) exactly when one local term equals \(1\) and all others vanish.

For \(q\equiv1\pmod5\), this is precisely
\[
\nu_5(a+1)=1.
\]

For \(q\equiv4\pmod5\), the contribution is \(1\) exactly when
\[
5\nmid a+1
\]
and
\[
\nu_5(q+1)=1.
\]
Within the residue class \(q\equiv4\pmod5\), the latter fails exactly at
\[
q\equiv24\pmod{25}.
\]

For \(q\equiv2,3\pmod5\), the contribution is \(1\) exactly when
\[
5\nmid a+1
\]
and
\[
\nu_5(q^2+1)=1.
\]
The two roots of
\[
x^2\equiv-1\pmod{25}
\]
are \(7\) and \(18\), so the second condition is equivalent to
\[
q\not\equiv7,18\pmod{25}.
\]
This proves the exact valuation-one statement.

It remains to prove the density assertion. If
\[
5\nmid\sigma(n),
\]
then for every prime
\[
q\equiv4\pmod5
\]
the exponent \(\nu_q(n)\) is even. For any finite set \(P\) of primes in this residue class, the natural density of integers having even \(q\)-adic valuation for every \(q\in P\) is
\[
\prod_{q\in P}\frac{q}{q+1},
\]
because for one prime \(q\),
\[
\sum_{j\ge0}\left(\frac1{q^{2j}}-\frac1{q^{2j+1}}\right)
=\frac{q}{q+1}.
\]
Therefore the upper density of the set
\[
\{n:5\nmid\sigma(n)\}
\]
is at most
\[
\prod_{q\in P}\frac{q}{q+1}.
\]
As \(P\) exhausts the primes \(q\equiv4\pmod5\), this product tends to \(0\), because the reciprocal primes in that reduced arithmetic progression have divergent sum. Hence
\[
\{n:5\nmid\sigma(n)\}
\]
has density \(0\), proving the result.

## Verification
The accompanying `verify.py` independently factors integers, computes \(\sigma(n)\), and computes the local criterion from the prime factorization.

It checks, for every
\[
1\le n\le200000,
\]
that the predicted value of
\[
\nu_5(\sigma(n))
\]
equals the direct value. This simultaneously verifies the divisibility criterion and the \(\nu_5=1\) refinement on that range.

The checker also confirms that the numbers below \(100\) satisfying
\[
5\mid\sigma(n)
\]
begin exactly with
\[
8,19,24,27,29,38,40,54,56,57,58,59,72,76,79,87,88,89,95,
\]
matching the list displayed in the motivating source.

The finite replay is a regression check. The theorem for all positive integers is proved symbolically above.

## Relationship to prior work
Amdeberhan, Moll, Sharma, and Villamizar give the general local formula for
\[
\nu_p(\sigma(q^a))
\]
and, in Note 7.6, explicitly identify characterization of the integers \(r\) with
\[
\sigma(r)\equiv0\pmod5
\]
as an interesting question. They list the first examples but do not state the residue-and-exponent characterization above.

A related earlier result proves a logarithmic upper-bound condition for \(p=5\), but that extremal-valuation statement does not characterize the level set
\[
5\mid\sigma(n)
\]
or the exact level
\[
\nu_5(\sigma(n))=1.
\]

Zhao and Chen later prove the unconditional global upper bound
\[
\nu_p(\sigma(n))\le\lceil\log_p n\rceil
\]
and study equality in that bound. The accessible abstract and bibliographic material do not state the modular level-set classification here. The full text was not available through the consulted lawful sources, so hidden coverage inside that article remains a residual literature risk.

Targeted semantic searches for the modulo-\(5\) characterization, the exact level-one condition, and the density-one consequence did not locate a prior statement of this combined result.

## Limitations
The classification is specialized to \(p=5\). The same general valuation theorem can in principle be specialized to other odd primes, but the residue classes and order conditions become more elaborate.

The density proof gives no effective error term. Obtaining a sharp asymptotic for the exceptional set
\[
\{n\le x:5\nmid\sigma(n)\}
\]
would require additional analytic number theory.

The strongest residual originality risk is the inaccessible full text of the 2025 follow-up and unindexed sources that may have recorded the same elementary specialization.

## References
1. Tewodros Amdeberhan, Victor H. Moll, Vaishavi Sharma, Diego Villamizar, “Arithmetic properties of the sum of divisors,” arXiv:2007.03088v1, first public 6 July 2020; Journal of Number Theory 223 (2021), 325–349; primary MSC \(11A25\).
2. Junjia Zhao and Yonggao Chen, “\(p\)-adic Valuation of the Sum of Divisors,” Frontiers of Mathematics 20 (2025), 795–827.
3. Classical Mertens theorem for arithmetic progressions, in the form that the sum of reciprocal primes in any reduced residue class modulo \(5\) diverges.
