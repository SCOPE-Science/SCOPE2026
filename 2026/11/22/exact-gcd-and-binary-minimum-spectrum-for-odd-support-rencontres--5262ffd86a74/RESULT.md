# Exact gcd and binary minimum spectrum for odd-support rencontres rows

## Finding
Let \(D_0=1\), \(D_1=0\), and \(D_m=mD_{m-1}+(-1)^m\) for \(m\ge2\). Thus \(D_m\) counts fixed-point-free permutations of \(m\) elements. For each integer \(n\ge4\), the rencontres number with exactly \(n-m\) fixed points is \(R(n,m)=\binom{n}{m}D_m\). Retain precisely those entries with an **odd number of moved elements** and at least one fixed point, namely odd \(m\) satisfying \(3\le m<n\). Define their row content
\[
G(n)=\gcd_{\substack{3\le m<n\\m\text{ odd}}}R(n,m).
\]
Let \(s_2(N)\) denote the number of ones in the base-two expansion of \(N\), and let \(\nu_p\) be the usual prime-adic valuation. Define \(P(n)=p\) when \(n=p^a\) for an odd prime \(p\) and integer \(a\ge1\), and \(P(n)=1\) otherwise. Then, **for every \(n\ge4\)**,
\[
\boxed{G(n)=2^{\nu_2(n(n-1)(n-2))}P(n).}
\]
In particular, an odd prime divides the content exactly when the row index is a power of that prime, and its exponent in the content is exactly one. The binary exponent can be arbitrarily large.

More precisely, **for every odd \(m\) with \(3\le m<n\)**,
\[
\boxed{\nu_2(R(n,m))=\nu_2(n(n-1)(n-2))+\nu_2\!\left(\binom{n-3}{m-3}\right).}
\]
The columns attaining the minimum binary valuation are exactly those for which every one-bit of \(m-3\) occurs in \(n-3\). Their number is
\[
\boxed{E(n)=\begin{cases}
2^{s_2(n-3)-1},&n\text{ even},\\
2^{s_2(n-3)}-1,&n\text{ odd}.
\end{cases}}
\]
The content and spectrum are parts of one rowwise divisibility classification.

## Assumptions and scope
The integers \(n\) and \(m\) have the ranges stated above. All selected entries are positive. The case \(m=1\) is excluded because \(D_1=0\), and the full derangement column \(m=n\) is excluded by the positive-fixed-point condition. The binary digit-subset criterion is equivalent to \(\binom{n-3}{m-3}\) being odd. The claim concerns the row content and **all binary valuations**; it does not claim the complete odd-prime valuation of each individual entry. When \(n\) is an odd prime power, the prime in \(P(n)\) is unique.

## Proof
**1. Odd derangements.** The standard recurrence also gives, for \(m\ge2\),
\[
D_m=(m-1)(D_{m-1}+D_{m-2}).
\]
By \(D_0=1,D_1=0\) and the first recurrence, \(D_j\) is odd for even \(j\) and even for odd \(j\). Thus for odd \(m\ge3\), \(D_{m-1}+D_{m-2}\) is odd, proving the exact identity
\[
\nu_2(D_m)=\nu_2(m-1).
\]

**2. Every selected binary valuation.** For odd \(m\ge3\), the factorial identity
\[
\binom nm(m-1)=
\frac{n(n-1)(n-2)}{m(m-2)}\binom{n-3}{m-3}
\]
is exact over the rationals. Both \(m\) and \(m-2\) are odd, so taking \(\nu_2\) of this identity and using Step 1 proves the displayed formula for every chosen column. Since the column \(m=3\) occurs in every selected row and \(\binom{n-3}{0}=1\), the minimum binary valuation is exactly \(\nu_2(n(n-1)(n-2))\).

**3. Excluding odd primes away from pure prime powers.** Let \(p\) be any odd prime. From \(D_m=mD_{m-1}+(-1)^m\) we have
\[
p\mid m\quad\Longrightarrow\quad D_m\equiv(-1)^m\pmod p.
\]
If \(p>n\), the selected entry at \(m=3\) equals \(2\binom n3\), which is a \(p\)-unit. Suppose next that \(p\le n\) and \(n\) is not a power of \(p\). In the base-\(p\) expansion of \(n\), some positive-position digit is nonzero, say at position \(j\ge1\). Set \(m=p^j\). Then \(m\) is odd, \(3\le m<n\), and Lucas's congruence gives \(\binom nm\not\equiv0\pmod p\) because the digit at \(j\) is nonzero. Since \(p\mid m\), the derangement factor is also a \(p\)-unit. Thus no odd prime divides all selected entries unless \(n\) is a pure power of that same prime.

**4. Exact odd-prime exponent at a prime-power row.** Suppose \(n=p^a\) for an odd prime \(p\), and since \(n\ge4\) necessarily either \(a\ge2\) or \(p\ge5\). Every \(1\le m<n\) has \(p\mid\binom{p^a}{m}\), by Lucas's theorem; hence \(p\mid G(n)\). If \(a\ge2\), take \(m=p^{a-1}\) (odd and strictly between 3 and \(n\)). Kummer's carry theorem or the factorial valuation formula yields \(\nu_p\binom{p^a}{p^{a-1}}=1\). As \(p\mid m\), \(p\nmid D_m\), so \(\nu_p(R(n,m))=1\). If \(a=1\), then \(p\ge5\); take \(m=3\), for which \(\binom p3=p(p-1)(p-2)/6\) has \(p\)-valuation one and \(D_3=2\) is a \(p\)-unit. Thus \(\nu_p(G(n))=1\) in both cases. Together with Steps 2–3, unique prime factorization proves the gcd formula.

**5. Exactly the minimizing columns.** By Step 2, a selected \(m\) minimizes the binary valuation if and only if \(\binom{n-3}{m-3}\) is odd. Lucas's theorem at \(p=2\) says this occurs exactly when \(j=m-3\) is a binary digit-subset of \(N=n-3\). The valid indices \(j\) are even and satisfy \(0\le j<N\). If \(n\) is even, \(N\) is odd; its lowest bit is one, so exactly half of all \(2^{s_2(N)}\) subsets have even \(j\), and none equals \(N\). If \(n\) is odd, \(N\) is even; every subset has even \(j\), and only \(j=N\) must be removed. This proves the displayed formula for \(E(n)\).

## Verification
The companion `check.py` is standalone Python 3 using only the standard library. Run `python3 check.py`. It constructs derangements independently by the recurrence, computes every actual selected rencontres entry and gcd for \(4\le n\le240\), checks the exact binary valuation and minimizer count for all selected columns, and independently checks the predicted odd-prime support for primes up to 151 in rows up to 151. The expected printed diagnostic is `PASS: 17648 exact assertions; all rows n=4..240 and prime-support checks n<=151.` These are finite diagnostic checks, **not** a proof for all integers; the proof is Steps 1–5.

## Relationship to prior work
The rencontres triangle and factorization \(R(n,m)=\binom nm D_m\) are classical. Lucas and Kummer provide the digit criterion and carry valuation for binomial coefficients, respectively; the derangement recurrence and its arithmetic consequences are studied by Miska. These inputs are not new. The result here is the simultaneous complete divisibility classification for odd moved-support, including a weighted-row gcd, every binary valuation and every binary minimum column. A published restricted-binomial-row count theorem handles unweighted coefficients at restricted **multiples** of a fixed integer and the event of prime divisibility; it does not imply the weighted odd-support content. The published strong-divisibility binomial-array theorem likewise treats generalized binomial arrays without derangement weights, and a published dyadic derangement-value theorem classifies residues of \(D_m\) alone rather than their products with rowwise binomial coefficients. Searches of full accessible primary texts and relevant published results did not recover this complete combined classification. The possibility of an unlocated earlier specialization is not excluded.

## Limitations
There is no assertion about selected rows including \(m=n\) or the zero-valued \(m=1\) column. The theorem does not classify all odd-prime valuations of individual entries or rowwise least common multiples. Diagnostic enumeration does not prove the infinite formulas. Historical uniqueness is not certified; the originality assessment is qualified by possible unindexed earlier work. No independent mathematical audit has been performed.

## References
1. Romeo Meštrović, *Lucas' theorem: its generalizations, extensions and applications (1878–2014)*, arXiv:1409.3820 (first publicly posted 2014-09-06), https://arxiv.org/abs/1409.3820.
2. Piotr Miska, *Arithmetic Properties of the Sequence of Derangements and its Generalizations*, arXiv:1508.01987 (first publicly posted 2015-08-09), https://arxiv.org/abs/1508.01987.
3. *Rencontres numbers*, OEIS Wiki, https://oeis.org/wiki/Rencontres_numbers (classical array formula; no first-posting date inferred).
4. *Exact logarithmic row counts for restricted binomial gcds*, publicly accessible manuscript, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-logarithmic-row-counts-for-restricted-binomial-gcds--339a752cfdc3 (different unweighted object and divisibility-count problem).
5. *Universal row content of strong-divisibility binomial arrays*, publicly accessible manuscript, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-universal-row-content-of-strong-divisibility-binomial-arrays--8c34899e8bac (different generalized unweighted binomial-array object).
6. *Exact dyadic residue multiplicities of derangement numbers*, publicly accessible manuscript, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-dyadic-residue-multiplicities-of-derangement-numbers--2db8513e1620 (individual derangement residue distribution rather than rencontres row content).
