# Exact primitive-progression densities for coprime divisor matchings

## Finding

For every positive integer \(n\), let \(D(n)\) be its positive divisors and \(N=\tau(n)\). For positive integers \(a,b\) with \(\gcd(a,b)=1\), write \(\mathcal P_{a,b}=\{a+bt:0\le t<N\}\). Call the pair **successful** when there is a bijection \(f:D(n)\to\mathcal P_{a,b}\) with \(\gcd(d,f(d))=1\) for each \(d\mid n\). For real \(X\ge1\), let \(M_n(X)\) count successful pairs with \(1\le a,b\le X\).

For every prime \(p\mid n\), define \(e_p=\nu_p(n)\), \(T_p=\tau(n/p^{e_p})=N/(e_p+1)\), and \(h_p=\max\{0,e_p+1-p\}\). Then the following **exact density law** holds for every fixed \(n\ge1\):

\[
M_n(X)=\frac6{\pi^2}\,\delta(n)X^2+O_n(X\log(2X)),\qquad
\delta(n)=\prod_{p\mid n}\left(1-\frac{\min\{p,h_pT_p\}}{p+1}\right).
\]

The empty product for \(n=1\) equals one. In particular \(\delta(n)\) is a positive rational, \(\delta(n)=1\) precisely when \(p^p\nmid n\) for every prime \(p\), and \(n\mid m\) implies \(\delta(m)\le\delta(n)\).

For every prime \(p\) and integer \(e\ge1\), the complete prime-power spectrum is

\[
\delta(p^e)=\begin{cases}
1,&1\le e<p,\\
(2p-e)/(p+1),&p\le e\le2p-2,\\
1/(p+1),&e\ge2p-1.
\end{cases}
\]

Consequently \(\inf_{n\ge1}\delta(n)=0\), although \(\delta(n)>0\) for every fixed \(n\). For example \(\delta(4)=2/3\), \(\delta(8)=1/3\), \(\delta(27)=3/4\), \(\delta(81)=1/2\), and \(\delta(108)=1/12\).

## Assumptions and scope

The count treats ordered pairs of positive integers \((a,b)\), each independently bounded by \(X\), with \(\gcd(a,b)=1\). It does not weight progressions by their last term or count individual matchings. All implied constants may depend on the fixed integer \(n\); no uniform error estimate in growing \(n\) is asserted. The pointwise existence criterion from Alekseyev [1, Theorem 1.1] is used as a previously proved input. The new conclusion evaluates the distribution of successful primitive pairs rather than reproving this criterion.

## Proof

**1. Reduction to local counts.** By [1, Theorem 1.1], success is equivalent to the following independent inequalities for each \(p\mid n\): the number of indices \(0\le t<N\) for which \(p\mid a+bt\) is at most \(T_p\). If \(p\mid b\), primitiveness implies \(p\nmid a\), so the number is zero. If \(p\nmid b\), the values \(a+bt\pmod p\) cycle through all residues. Writing \(N=pk+r\), with \(0\le r<p\), the count equals \(k+1\) for exactly \(r\) residues of \(a\pmod p\), and equals \(k\) for the other \(p-r\) residues. This follows by splitting \(N\) indices into \(k\) full blocks of \(p\) and one block of length \(r\), whose \(r\) residues are distinct.

**2. Good and bad primes.** If \(e_p+1\le p\), then \(N=(e_p+1)T_p\le pT_p\), and every possible local count is at most \(T_p\). Such primes impose no restriction. Otherwise put \(h=e_p+1-p\ge1\). We have \(N=(p+h)T_p=pT_p+hT_p\). If \(hT_p\ge p\), then \(k\ge T_p+1\), so every primitive residue pair with \(p\nmid b\) fails; exactly the \(p-1\) pairs \((a,b)\in(\mathbb Z/p\mathbb Z)^2\) with \(b=0\) and \(a\ne0\) succeed. Among the \(p^2-1\) primitive residue pairs this gives the fraction \(1/(p+1)\).

If \(1\le hT_p<p\), then \(k=T_p\) and \(r=hT_p\). The \(p-1\) primitive pairs with \(b=0\) succeed, and for each of the \(p-1\) nonzero values of \(b\), precisely \(p-r\) residue values of \(a\) succeed. Thus the successful count is

\[
(p-1)+(p-1)(p-r)=(p-1)(p+1-r),
\]

and its ratio to \(p^2-1\) is \(1-r/(p+1)\). The two cases combine into the local factor \(1-\min\{p,hT_p\}/(p+1)\); with \(h=0\) this also covers good primes.

**3. Density of primitive pairs.** Put \(R=\prod_{p\mid n}p\), with \(R=1\) when \(n=1\). Let \(\mathcal S\subseteq(\mathbb Z/R\mathbb Z)^2\) consist of the CRT residue pairs satisfying the successful local conditions and \(\gcd(a,b,R)=1\). By the Chinese remainder theorem, the previous step gives

\[
\frac{|\mathcal S|}{\prod_{p\mid R}(p^2-1)}=\delta(n).
\]

For any fixed residue subset \(\mathcal S\) with every pair primitive modulo \(R\), the number of integer pairs \(1\le a,b\le X\), \(\gcd(a,b)=1\), and \((a,b)\pmod R\in\mathcal S\) equals

\[
\frac6{\pi^2}\frac{|\mathcal S|}{\prod_{p\mid R}(p^2-1)}X^2+O_R(X\log(2X)).
\]

Indeed, expand the indicator of \(\gcd(a,b)=1\) as \(\sum_{d\mid\gcd(a,b)}\mu(d)\). If \(\gcd(d,R)>1\), the residue condition makes its contribution zero. For \(\gcd(d,R)=1\), multiplying both coordinates by \(d^{-1}\) permutes primitive residue pairs, and there are \(|\mathcal S|(X/(dR))^2+O_R(X/d+1)\) admissible pairs before weighting by \(\mu(d)\). Summing \(1\le d\le X\) contributes an \(O_R(X\log(2X))\) error; extending the absolutely convergent quadratic main sum past \(X\) adds \(O_R(X)\). Its coefficient is

\[
\frac{|\mathcal S|}{R^2}\prod_{q\nmid R}\left(1-\frac1{q^2}\right)
=\frac6{\pi^2}\frac{|\mathcal S|}{\prod_{p\mid R}(p^2-1)}.
\]

This proves the count. The case \(R=1\) specializes to the classical count of coprime pairs, including \(n=1\).

**4. Structural consequences.** Each Euler factor lies in \([1/(p+1),1]\), and it equals one precisely when \(e_p<p\). This proves positivity and the \(M\)-number criterion. If \(n\mid m\), then for each prime dividing \(n\) both \(h_p\) and \(T_p=\prod_{q\ne p}(\nu_q(n)+1)\) cannot decrease on replacing \(n\) by \(m\). The corresponding factors therefore cannot increase, while new prime factors contribute at most one; hence \(\delta(m)\le\delta(n)\). If \(n=p^e\), then \(T_p=1\) and the three displayed regimes follow from whether \(h_p\) is zero, between one and \(p-1\), or at least \(p\). Setting \(e=2p-1\) gives \(\delta(p^{2p-1})=1/(p+1)\to0\) as \(p\to\infty\) through primes. All conclusions follow.

## Verification

The standalone Python 3 program `verify.py` evaluates the exact rational product, enumerates the local primitive residue classes, and independently constructs bipartite perfect matchings for finite examples rather than relying only on the criterion. Executing `python3 verify.py` produces `VERIFY_OK`, comparing 29 residue cases, 2703 independently computed perfect matchings, 112 prime-power cases, and 900 divisibility-monotonicity tests. These computations corroborate but do not replace the proof for all fixed positive integers \(n\).

## Relationship to prior work

Alekseyev [1, Theorem 1.1] gives the exact **yes/no criterion** for an individual progression, and [1, Corollary 5.1] classifies common differences permitting every primitive start. This work explicitly uses that theorem but computes a different statistic: the exact asymptotic frequency of successful progressions among **all** primitive pairs of bounded start and step. The local saturation law, its multiplicative evaluation, and its divisibility monotonicity are not stated in [1]. McNew and Pomerance [2] compute a density over the **integers being matched**, not the frequency of progressions for a fixed integer; the sample spaces differ. No claim is made that the existence criterion itself is new.

## Limitations

The conclusion is conditional on the proved matching-existence theorem [1]. The error term is for fixed \(n\); uniformity as \(n\) grows is not established. The formula counts progressions admitting at least one matching, not the number of matchings. Although the exact new statistic was not located in the inspected sources, equivalent earlier work may exist; priority has not been independently verified.

## References

[1] Max A. Alekseyev, *Coprime matchings of divisor sets*, arXiv:2610.37512v1, publicly submitted 2026-10-27, https://arxiv.org/html/2610.37512v1; Theorem 1.1, Theorem 1.2, Corollary 5.1, Section 6.

[2] Nathan McNew and Carl Pomerance, *Matchable numbers*, arXiv:2604.05304 (first submitted 2026-04-07), https://arxiv.org/html/2604.05304; Introduction and Section 6.
